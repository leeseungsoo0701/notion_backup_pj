#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
export_manifest_ai_fields.py
- 입력: manifest_dedup_sorted.csv (created_date,title,id,url)
- 출력: manifest_ai_enriched.csv (created_date,title,id,url,perf_flag,importance,summary_5lines)
- 기능:
  * Notion 페이지 본문을 Markdown으로 수집(블록 페이지네이션)
  * OpenAI로 '성과에 쓸만한지' 기준 5줄 요약 + 중요도(1~5) + perf_flag(yes/no)
  * --resume: 기존 출력이 있으면 이어서(이미 처리한 id는 스킵)
  * --force / --force-retry-failed / --only-missing 로 재처리 선택
  * 진행 로그(행 단위/구간 단위), 자동 저장, 예외 상세 로그
  * latin-1 헤더 보호(토큰에 비ASCII가 섞일 때 urllib3 UnicodeEncodeError 방지)
"""

import os
import sys
import csv
import json
import time
import signal
import re
from typing import Dict, List, Set, Optional, Tuple
from datetime import datetime

import requests

# -------------------- 환경/설정 --------------------
BASE_URL = "https://api.notion.com/v1"
NOTION_VERSION = "2022-06-28"
API_TOKEN = os.environ.get("NOTION_TOKEN", "").strip() or "PUT_YOUR_INTEGRATION_TOKEN_HERE"

OUT_DIR = "./out"
FAIL_LOG = os.path.join(OUT_DIR, "failures_index.txt")

_session = requests.Session()
_session.trust_env = True

# OpenAI 호출 간 최소 간격(Throttle) 관리
_last_ai_ts: float = 0.0

def _throttle(min_interval: float):
    global _last_ai_ts
    if min_interval <= 0:
        return
    now = time.time()
    wait = (_last_ai_ts + min_interval) - now
    if wait > 0:
        time.sleep(wait)
    _last_ai_ts = time.time()

# -------------------- 공용 유틸 --------------------
def log(msg: str = ""):
    try:
        print(msg, flush=True)
    except Exception:
        print(str(msg).encode("ascii", "replace").decode("ascii"), flush=True)

def append_failure(path: str, msg: str, context: Optional[dict] = None):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        line = {"ts": ts, "message": msg}
        if context:
            line["context"] = context
        f.write(json.dumps(line, ensure_ascii=False) + "\n")

def validate_token_ascii(token: str):
    try:
        _ = token.encode("latin-1")
    except Exception:
        log("❗ HTTP 헤더 'Authorization'에 비-ASCII 문자가 섞였습니다. NOTION_TOKEN 값을 다시 붙여넣으세요.")
        sys.exit(2)

def headers() -> Dict[str, str]:
    return {
        "Authorization": f"Bearer {API_TOKEN}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json",
    }

# -------------------- Notion API --------------------
def req(method: str, url: str, **kwargs):
    tries = 0
    while True:
        tries += 1
        try:
            r = _session.request(method, url, headers=headers(), timeout=60, **kwargs)
            if r.status_code in (429, 502, 503):
                time.sleep(min(1.0 * tries, 5))
                continue
            return r
        except Exception as e:
            if tries < 3:
                time.sleep(0.5 * tries)
                continue
            raise

def retrieve_page(page_id: str) -> Optional[dict]:
    r = req("GET", f"{BASE_URL}/pages/{page_id}")
    if r.status_code != 200:
        append_failure(FAIL_LOG, f"/pages/{page_id} 실패 status={r.status_code}")
        return None
    return r.json()

def blocks_children(parent_id: str, start_cursor: Optional[str] = None, page_size: int = 100) -> dict:
    params = {"page_size": min(100, page_size)}
    if start_cursor:
        params["start_cursor"] = start_cursor
    r = req("GET", f"{BASE_URL}/blocks/{parent_id}/children", params=params)
    if r.status_code != 200:
        # 404는 삭제/권한/잘못된ID 등
        append_failure(FAIL_LOG, f"/blocks/{parent_id}/children 실패 status={r.status_code}")
        return {"results": [], "has_more": False}
    return r.json()

# -------------------- Markdown 빌드 --------------------
# ---- 로컬 요약기(Heuristic Summarizer) ----
import math

_METRIC_PAT = re.compile(r"(\d{1,3}(?:[,\d]{0,3})+(?:\.\d+)?%?)|(%|\bp\d+\b|\bkr\d+\b)", re.I)
_KEYWORDS = [
    "성과","지표","데이터","전환","전환율","매출","구매","가입","잔존","리텐션","KPI","OKR","KR",
    "달성","개선","증가","감소","상승","하락","출시","배포","런칭","도입","실험","A/B","AB","가설",
    "결정","합의","우선순위","리팩터","리팩토링","비용","효율","속도","성능","버그","장애","해결",
    "효과","임팩트","영향","목표","결과","Outcome","Impact"
]

_NEGATIVE_HINTS = [
    "회의록","안건","목차","템플릿","작성요령","예시","샘플","TODO","To Do","to-do","참고","링크","링크모음",
    "제목없음","빈 페이지","빈페이지","미정","TBD","N/A"
]

# 우선순위 키워드 (성과 관점 가중치) - 사용자가 지정한 단어 기반
# 가중치 기준(권장): 1=낮음, 2=보통, 3=높음
PRIORITY_KEYWORDS = {
    "성과": 3,
    "전환율": 3,
    "roas": 3,       # 대소문자 무시
    "abt": 2,        # ABT (A/B 테스트 관련)
    "a/b": 2,        # 'A/B' 표기도 보강
    "실험": 2,
    "배포 공유": 2,
    "효율화": 2,
    "자동화": 2,
    "prd": 2,
    "문제 정의": 2,
    "uxui": 1,
    "요약": 1,
}

def _clean_line(s: str) -> str:
    s = s.strip()
    # 마크다운 머리기호 제거
    s = re.sub(r"^#{1,6}\s*", "", s)   # headings
    s = re.sub(r"^[-*+]\s+", "", s)    # bullets
    s = re.sub(r"^\d+\.\s+", "", s)    # ordered list
    s = re.sub(r"^>\s*", "", s)        # quote
    s = s.replace("[x]", "").replace("[ ]", "")
    # 코드/구분선/빈 줄 제거
    if s.startswith("```") or s == "---":
        return ""
    return s.strip()

def _score_line(s: str) -> int:
    if not s or len(s) < 4:
        return 0
    score = 0
    # 핵심 키워드
    for kw in _KEYWORDS:
        if kw.lower() in s.lower():
            score += 2
            break
    # 우선순위 키워드 가중치 (여러 개 포함 시 누적)
    low = s.lower()
    for kw, weight in PRIORITY_KEYWORDS.items():
        if kw in low:
            score += weight * 3  # 우선순위 키워드는 강하게 반영
    # 수치/퍼센트/지표
    if _METRIC_PAT.search(s):
        score += 2
    # 강한 동사
    for v in ["달성","개선","증가","감소","감소시킴","상승","출시","배포","도입","해결","성과","효율"]:
        if v in s:
            score += 1
            break
    # 결정/정책/우선순위
    for v in ["결정","합의","정책","가이드","우선순위","중요", "핵심"]:
        if v in s:
            score += 1
            break
    # 부정적/형식적 라인 감점
    for ng in _NEGATIVE_HINTS:
        if ng.lower() in s.lower():
            score -= 1
            break
    # 너무 짧거나 너무 길면 약간 감점/보정
    if len(s) > 220:
        score -= 1
    return max(score, 0)

def summarize_locally(markdown_text: str, title: str, created_date: str, url: str) -> dict:
    """
    마크다운을 가볍게 스캔하여 '성과 관점' 5줄 요약, perf_flag, importance를 생성.
    - 후보: 헤딩/리스트/숫자포함/키워드 포함 라인 위주
    - 점수: 키워드/숫자/동사/결정 키워드로 가중
    """
    lines = []
    for raw in (markdown_text or "").splitlines():
        s = _clean_line(raw)
        if not s:
            continue
        # 의미 없는 라인 필터
        if s.lower().startswith(("http://","https://")):
            continue
        # callout 이모지 제거 흔적
        s = s.replace("💡", "").strip()
        lines.append(s)

    # 후보 선별
    candidates = []
    for s in lines:
        base = 0
        if any(s.startswith(prefix) for prefix in ("#", "-", "1.", "2.", "3.", "OKR", "KR", "[", "•", "·")):
            base += 1
        if any(kw.lower() in s.lower() for kw in _KEYWORDS) or _METRIC_PAT.search(s):
            base += 1
        score = _score_line(s) + base
        if score > 0:
            candidates.append((score, s))

    # 중복/유사 문장 제거 간단 처리
    seen = set()
    deduped = []
    def _priority_hit(t: str) -> int:
        tl = t.lower()
        return 1 if any(pk in tl for pk in PRIORITY_KEYWORDS.keys()) else 0

    for score, s in sorted(candidates, key=lambda x: (-x[0], -_priority_hit(x[1]), len(x[1]))):
        key = s.lower()
        if key in seen:
            continue
        seen.add(key)
        deduped.append((score, s))
        if len(deduped) >= 80:
            break

    # 최고 점수 기반 perf/importance 산출
    top_score = deduped[0][0] if deduped else 0
    perf_flag = "yes" if top_score >= 3 else ("yes" if any(k in (markdown_text or "").lower() for k in ["okr","kr","kpi","전환","매출"]) else "no")

    if top_score >= 7:
        importance = 5
    elif top_score >= 5:
        importance = 4
    elif top_score >= 3:
        importance = 3
    elif top_score >= 2:
        importance = 2
    else:
        importance = 1

    # 상위 5줄 구성
    top_lines = [s for _, s in deduped][:5]
    if len(top_lines) < 5:
        # 보강: 제목/날짜/링크로 채움
        filler = [
            f"[제목] {title}".strip(),
            f"[날짜] {created_date}".strip(),
            f"[링크] {url}".strip()
        ]
        for x in filler:
            if len(top_lines) >= 5: break
            if x and x not in top_lines:
                top_lines.append(x)
    # 길이 제한
    top_lines = [ (l[:240] + "…") if len(l) > 240 else l for l in top_lines ]
    # 5개 맞추기
    top_lines = (top_lines + [""]*5)[:5]

    return {"perf_flag": perf_flag, "importance": importance, "summary_5lines": top_lines}
def _rich_text_to_plain(rt_arr: list) -> str:
    buf = []
    for o in rt_arr or []:
        t = o.get("type")
        if t == "text":
            buf.append(o.get("text", {}).get("content", ""))
        elif t == "mention":
            m = o.get("mention", {}) or {}
            if m.get("type") == "user":
                name = (m.get("user", {}) or {}).get("name", "")
                buf.append(f"@{name}" if name else "@user")
            else:
                buf.append("@mention")
        elif t == "equation":
            buf.append(o.get("equation", {}).get("expression", ""))
    return "".join(buf)

def block_to_md(block: dict) -> str:
    t = block.get("type")
    b = block.get(t) or {}
    if t == "paragraph":
        return _rich_text_to_plain(b.get("rich_text"))
    if t in ("heading_1", "heading_2", "heading_3"):
        hashes = {"heading_1": "#", "heading_2": "##", "heading_3": "###"}[t]
        return f"{hashes} {_rich_text_to_plain(b.get('rich_text'))}"
    if t in ("bulleted_list_item", "numbered_list_item"):
        prefix = "-" if t == "bulleted_list_item" else "1."
        return f"{prefix} {_rich_text_to_plain(b.get('rich_text'))}"
    if t == "to_do":
        chk = "[x]" if b.get("checked") else "[ ]"
        return f"- {chk} {_rich_text_to_plain(b.get('rich_text'))}"
    if t == "quote":
        return f"> {_rich_text_to_plain(b.get('rich_text'))}"
    if t == "callout":
        return f"> 💡 {_rich_text_to_plain(b.get('rich_text'))}"
    if t == "code":
        lang = b.get("language") or ""
        txt = _rich_text_to_plain(b.get("rich_text"))
        return f"```{lang}\n{txt}\n```"
    if t == "divider":
        return "---"
    if t == "bookmark":
        url = b.get("url", "")
        cap = _rich_text_to_plain(b.get("caption") or [])
        return f"[{cap or url}]({url})" if url else cap
    if t == "image":
        cap = _rich_text_to_plain(b.get("caption") or [])
        return f"![image]({cap})" if cap else "![image]"
    # child_page/child_database 등은 상위에서 별도로 순회하므로 스킵
    return ""

def get_page_markdown(page_id: str, max_blocks: int = 2000) -> str:
    """첫 max_blocks 만큼 1단계 children을 Markdown으로 단순 결합(깊이 1, 속도 우선)"""
    lines: List[str] = []
    cursor = None
    scanned = 0
    while True and scanned < max_blocks:
        data = blocks_children(page_id, start_cursor=cursor, page_size=100)
        results = data.get("results", [])
        if not results:
            break
        for blk in results:
            if scanned >= max_blocks:
                break
            md = block_to_md(blk)
            if md:
                lines.append(md)
            scanned += 1
        if not data.get("has_more"):
            break
        cursor = data.get("next_cursor")
    return "\n".join(lines).strip()

# -------------------- OpenAI --------------------
# pip install openai
from openai import OpenAI
_openai_client = None

def get_openai():
    global _openai_client
    if _openai_client is None:
        _openai_client = OpenAI()  # 키는 OPENAI_API_KEY 환경변수에서 자동 로드
    return _openai_client

def parse_ai_output(text: str) -> dict:
    """
    모델이 아래 JSON을 반환한다고 가정:
    {
      "perf_flag": "yes"|"no",
      "importance": 1..5,
      "summary_5lines": ["...","...","...","...","..."]
    }
    코드블록 ```json ... ``` 형태도 허용.
    """
    import json as _json, re as _re

    # 코드블록 제거
    code_match = _re.search(r"```(?:json)?(.*?)```", text, _re.S | _re.I)
    if code_match:
        text = code_match.group(1).strip()

    # 첫 번째 JSON 오브젝트만 추출
    m = _re.search(r"\{.*\}", text, _re.S)
    raw = m.group(0) if m else text.strip()

    # JSON 파싱 (실패 시 안전 기본값 반환)
    try:
        data = _json.loads(raw)
    except Exception:
        return {"perf_flag": "no", "importance": 1, "summary_5lines": ["", "", "", "", ""]}

    perf = str(data.get("perf_flag", "no")).lower()
    perf = "yes" if perf in ("yes", "y", "true", "1") else "no"

    try:
        imp = int(data.get("importance", 1))
    except Exception:
        imp = 1
    imp = min(5, max(1, imp))

    lines = data.get("summary_5lines", [])
    if isinstance(lines, str):
        lines = [s.strip() for s in lines.split("\n") if s.strip()]
    if not isinstance(lines, list):
        lines = []
    lines = (lines + [""] * 5)[:5]

    return {"perf_flag": perf, "importance": imp, "summary_5lines": lines}

def call_openai_summary(
    markdown_text: str,
    model: str,
    timeout: int,
    debug: bool = False,
    max_retries: int = 8,
    initial_backoff: float = 1.0,
    max_backoff: float = 60.0,
    min_interval: float = 0.0,
) -> dict:
    """
    전체 마크다운을 읽고 '성과에 쓸만한가' 기준으로 5줄 요약/중요도/성과여부를 JSON으로 반환.
    429/5xx/네트워크 오류는 지수 백오프+지터로 재시도. 호출 간 최소간격(min_interval) 보장.
    실패 시 예외 그대로 던짐(상위에서 기본요약 처리).
    """
    client = get_openai()

    sys_prompt = (
        "You are a performance review assistant for a PM.\n"
        "Given a single Notion page (rendered as Markdown), read ALL content and decide:\n"
        "1) perf_flag: 'yes' if there is any content usable for performance review; otherwise 'no'.\n"
        "2) importance: integer 1~5 (5 is most impactful to performance review).\n"
        "3) summary_5lines: a 5-line summary capturing concrete achievements, metrics, decisions, and outcomes.\n"
        "Return ONLY valid JSON with keys: perf_flag, importance, summary_5lines (array of 5 strings)."
    )
    user_prompt = f"# Notion Markdown\n{markdown_text}\n"

    tries = 0
    last_err = None
    backoff = max(0.1, float(initial_backoff))

    while tries < max_retries:
        tries += 1
        try:
            _throttle(min_interval)
            resp = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": sys_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                temperature=0.2,
                timeout=timeout,
            )
            text = resp.choices[0].message.content.strip()
            if debug:
                print("[OpenAI][raw]", text[:500], "..." if len(text) > 500 else "")
            return parse_ai_output(text)
        except KeyboardInterrupt:
            raise
        except Exception as e:
            # 쿼터 부족은 빠르게 상위로
            es = str(e)
            if "insufficient_quota" in es or "You exceeded your current quota" in es:
                raise e
            last_err = e
            # 지수 백오프 + 지터
            wait = min(max_backoff, backoff) * (1.0 + (0.25 * (time.time() % 1)))
            time.sleep(wait)
            backoff *= 2

    raise last_err

# -------------------- Hugging Face Summarizer --------------------
_hf_summarizer = None

def get_hf_summarizer(model_name: str = "facebook/bart-large-cnn"):
    """
    Lazy-load a HF summarization pipeline. We import inside to avoid hard dependency
    when the user doesn't pass --use-hf.
    """
    global _hf_summarizer
    if _hf_summarizer is None:
        try:
            from transformers import pipeline
        except Exception as e:
            raise RuntimeError(
                "transformers 패키지가 필요합니다. `pip install transformers torch` 후 다시 실행하세요."
            ) from e
        _hf_summarizer = pipeline("summarization", model=model_name)
    return _hf_summarizer

def _hf_chunk(text: str, chunk_chars: int = 3500, overlap: int = 200) -> List[str]:
    """
    Rough character-based chunking to avoid exceeding model max length.
    """
    if not text:
        return []
    chunks = []
    i = 0
    n = len(text)
    while i < n:
        j = min(n, i + chunk_chars)
        chunk = text[i:j]
        chunks.append(chunk)
        if j >= n:
            break
        i = j - overlap if j - overlap > i else j
    return chunks

def summarize_with_hf(markdown_text: str,
                      model_name: str = "facebook/bart-large-cnn",
                      max_length: int = 220,
                      min_length: int = 60) -> dict:
    """
    Summarize with Hugging Face pipeline.
    For long content: summarize chunks, then summarize the concatenated chunk-summaries.
    Returns the same schema as OpenAI path: {perf_flag, importance, summary_5lines}.
    """
    text = (markdown_text or "").strip()
    if not text:
        return {"perf_flag": "no", "importance": 1, "summary_5lines": ["", "", "", "", ""]}

    pipe = get_hf_summarizer(model_name=model_name)

    # 1) chunked summarization
    pieces = _hf_chunk(text, chunk_chars=3500, overlap=200)
    if not pieces:
        pieces = [text]

    inter_summaries = []
    for p in pieces:
        try:
            out = pipe(p, max_length=max_length, min_length=min_length, do_sample=False)
            inter_summaries.append(out[0]["summary_text"].strip())
        except Exception as e:
            inter_summaries.append("")

    # 2) merge summaries and summarize again if needed
    merged = "\n".join([s for s in inter_summaries if s]).strip()
    if not merged:
        merged = text[:3500]

    try:
        out2 = pipe(merged, max_length=max_length, min_length=max(30, min_length // 2), do_sample=False)
        final_sum = out2[0]["summary_text"].strip()
    except Exception:
        final_sum = merged

    # 3) performance-centric scoring (reuse local heuristics)
    perf_flag = "yes" if any(k in final_sum.lower() for k in ["성과","매출","전환","지표","okr","kpi","kr","효율","임팩트"]) else "no"
    if any(k in final_sum.lower() for k in ["큰 임팩트","매출","전환율","%","달성","목표 달성","지표 개선"]):
        importance = 4 if perf_flag == "yes" else 2
        if any(k in final_sum.lower() for k in ["전사", "핵심", "대규모", "크리티컬", "장애 해결", "출시"]):
            importance = 5
    else:
        importance = 3 if perf_flag == "yes" else 1

    # 4) split into 5 lines
    # prefer sentence-like splits; fallback to newline split
    parts = re.split(r'(?<=[.!?])\s+|\n+', final_sum)
    parts = [p.strip(" \t\n\r•-") for p in parts if p and len(p.strip()) > 2]
    summary_5 = (parts + [""]*5)[:5]

    # length guard per line
    summary_5 = [(s[:240] + "…") if len(s) > 240 else s for s in summary_5]

    return {"perf_flag": perf_flag, "importance": importance, "summary_5lines": summary_5}

# -------------------- CSV I/O --------------------
def ensure_header(path: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        with open(path, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["created_date", "title", "id", "url", "perf_flag", "importance", "summary_5lines"])

def read_input(path: str) -> List[dict]:
    rows = []
    with open(path, "r", newline="", encoding="utf-8") as f:
        rdr = csv.DictReader(f)
        for r in rdr:
            rows.append({
                "created_date": (r.get("created_date") or "").strip(),
                "title": (r.get("title") or "").strip(),
                "id": (r.get("id") or "").strip(),
                "url": (r.get("url") or "").strip(),
            })
    return rows

def load_done_ids(path: str) -> Dict[str, dict]:
    done = {}
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        return done
    with open(path, "r", newline="", encoding="utf-8") as f:
        rdr = csv.DictReader(f)
        for r in rdr:
            rid = (r.get("id") or "").strip()
            if not rid:
                continue
            done[rid] = {
                "created_date": (r.get("created_date") or "").strip(),
                "title": (r.get("title") or "").strip(),
                "url": (r.get("url") or "").strip(),
                "perf_flag": (r.get("perf_flag") or "").strip() or "no",
                "importance": (r.get("importance") or "").strip() or "1",
                "summary_5lines": (r.get("summary_5lines") or "").strip(),
            }
    return done

def append_result(path: str, rows: List[dict]):
    if not rows:
        return
    ensure_header(path)
    with open(path, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        for r in rows:
            w.writerow([
                r["created_date"],
                r["title"],
                r["id"],
                r["url"],
                r["perf_flag"],
                r["importance"],
                r["summary_5lines"],
            ])

# -------------------- 메인 --------------------
def main():
    import argparse

    parser = argparse.ArgumentParser(description="manifest_dedup_sorted.csv → AI enriched CSV")
    parser.add_argument("--input", required=True, help="입력 CSV (manifest_dedup_sorted.csv)")
    parser.add_argument("--output", required=True, help="출력 CSV (manifest_ai_enriched.csv)")

    # 재실행/건너뛰기 정책
    parser.add_argument("--resume", action="store_true", default=False, help="기존 출력에서 이어서 진행")
    parser.add_argument("--overwrite", action="store_true", default=False, help="출력 파일을 새로 생성(기존 무시)")
    parser.add_argument("--force", "--force-retry-failed", dest="force_retry_failed",
                        action="store_true", default=False,
                        help="이전 실패(기본요약/빈요약 포함) 건 재시도")
    parser.add_argument("--only-missing", dest="only_missing",
                        action="store_true", default=False,
                        help="기존 출력에 없는 id만 처리")

    # OpenAI 옵션
    parser.add_argument("--use-openai", action="store_true", default=False,
                        help="OpenAI로 요약/스코어 생성")
    parser.add_argument("--openai-model", type=str, default="gpt-4o-mini",
                        help="OpenAI 모델명 (기본 gpt-4o-mini)")
    parser.add_argument("--openai-timeout", type=int, default=60,
                        help="OpenAI 호출 타임아웃(초)")
    parser.add_argument("--openai-debug", action="store_true", default=False,
                        help="OpenAI 응답 원문 일부 로그")
    parser.add_argument("--openai-sanity-check", action="store_true", default=False,
                        help="시작 시 1회 테스트 콜 후 진행")
    parser.add_argument("--openai-max-retries", type=int, default=8, help="OpenAI 재시도 최대 횟수")
    parser.add_argument("--openai-initial-backoff", type=float, default=1.0, help="OpenAI 재시도 초기 대기(초)")
    parser.add_argument("--openai-max-backoff", type=float, default=60.0, help="OpenAI 재시도 최대 대기(초)")
    parser.add_argument("--min-ai-interval", type=float, default=0.0, help="OpenAI 호출 최소 간격(초) - 레이트리밋 회피")

    # Hugging Face 옵션
    parser.add_argument("--use-hf", action="store_true", default=False,
                        help="Hugging Face transformers 요약 사용 (OpenAI 대체)")
    parser.add_argument("--hf-model", type=str, default="facebook/bart-large-cnn",
                        help="HF summarization 모델명 (ex. facebook/bart-large-cnn, google/pegasus-xsum)")
    parser.add_argument("--hf-max-length", type=int, default=220,
                        help="HF 요약 max_length")
    parser.add_argument("--hf-min-length", type=int, default=60,
                        help="HF 요약 min_length")

    # 진행/성능 옵션
    parser.add_argument("--max-blocks", type=int, default=2000, help="본문 스캔 최대 블록 수")
    parser.add_argument("--autosave-every", type=int, default=200, help="N건마다 자동 저장")
    parser.add_argument("--progress-every", type=int, default=50, help="N건마다 진행 로그")
    parser.add_argument("--per-item-log", action="store_true", default=False, help="각 행 시작 로그")

    args = parser.parse_args()

    # Notion 토큰 검증(요약에 필요한 본문을 불러오려면 필요)
    if not API_TOKEN or API_TOKEN == "PUT_YOUR_INTEGRATION_TOKEN_HERE":
        log("❗ NOTION_TOKEN 환경변수를 설정하거나 스크립트 상단 API_TOKEN을 실제 토큰으로 바꾸세요.")
        sys.exit(2)
    validate_token_ascii(API_TOKEN)

    # OpenAI 키 확인
    if args.use_openai and not os.environ.get("OPENAI_API_KEY"):
        log("❗ OPENAI_API_KEY 환경변수가 없습니다. --use-openai 를 끄거나 키를 설정하세요.")
        sys.exit(2)

    # Ctrl+C 안전 종료
    stop_flag = {"stop": False}
    def on_sigint(signum, frame):
        stop_flag["stop"] = True
        log("\n사용자 중단: 현재까지 진행분 저장 중…")
    signal.signal(signal.SIGINT, on_sigint)

    # 입력/출력 준비
    in_rows = read_input(args.input)

    if args.overwrite and os.path.exists(args.output):
        os.remove(args.output)
    ensure_header(args.output)

    done_map = {}
    if args.resume and os.path.exists(args.output):
        done_map = load_done_ids(args.output)
        log(f"재개 모드: 기존 출력 {len(done_map)}건 로드")

    # OpenAI 샌티티 체크(옵션)
    if args.use_openai and args.openai_sanity_check:
        try:
            _ = call_openai_summary(
                "This is a sanity check.",
                model=args.openai_model,
                timeout=args.openai_timeout,
                debug=args.openai_debug,
                max_retries=args.openai_max_retries,
                initial_backoff=args.openai_initial_backoff,
                max_backoff=args.openai_max_backoff,
                min_interval=args.min_ai_interval,
            )
            log("[OpenAI] Sanity check OK")
        except KeyboardInterrupt:
            raise
        except Exception as e:
            msg = f"[OpenAI] Sanity check FAILED({type(e).__name__}): {e}"
            log(msg)
            append_failure(FAIL_LOG, msg)
            # 'insufficient_quota' 등은 자동 폴백
            log("→ OpenAI 요약을 비활성화하고 기본 요약으로 계속 진행합니다. (나중에 --force 로 재시도 가능)")
            args.use_openai = False
            if getattr(args, "use_hf", False):
                log("→ 이후 모든 항목은 HF 요약기로 처리합니다.")
            else:
                log("→ 이후 모든 항목은 로컬 요약기로 처리합니다.")
        
    total = len(in_rows)
    # 처리 대상 판별
    def is_failed_row(v: dict) -> bool:
        s = (v.get("summary_5lines") or "").strip()
        return (not s) or ("AI 요약 실패" in s)

    targets = []
    for r in in_rows:
        rid = r["id"]
        if not rid:
            continue
        if args.only_missing:
            if rid in done_map:
                continue
        elif args.force_retry_failed:
            if rid in done_map and is_failed_row(done_map[rid]):
                pass  # 재처리
            elif rid in done_map:
                continue  # 성공건은 스킵
        else:
            if rid in done_map:
                continue
        targets.append(r)

    log(f"시작: 전체 {total}건 / 처리대상 {len(targets)}건 "
        f"(resume={'ON' if args.resume else 'OFF'}, overwrite={'ON' if args.overwrite else 'OFF'})")

    processed = 0
    written_since_autosave = 0
    pending_rows: List[dict] = []

    def flush(reason: str):
        nonlocal pending_rows, written_since_autosave
        if pending_rows:
            append_result(args.output, pending_rows)
            pending_rows.clear()
            written_since_autosave = 0
        log(f"[저장] {reason} → {args.output}")

    for idx, r in enumerate(targets, start=1):
        if stop_flag["stop"]:
            break

        created_date = r["created_date"]
        title = r["title"]
        nid = r["id"]
        url = r["url"]

        if args.per_item_log:
            log(f"[{idx}/{len(targets)}] start id={nid} title={title}")

        # 본문 수집
        md = ""
        try:
            page = retrieve_page(nid)
            if page:
                md = get_page_markdown(nid, max_blocks=args.max_blocks)
        except KeyboardInterrupt:
            raise
        except Exception as e:
            append_failure(FAIL_LOG, f"본문 수집 실패: {type(e).__name__}: {e}", {"id": nid})

        # 요약 경로 선택: OpenAI → HF → 로컬 휴리스틱
        if args.use_openai:
            try:
                ai = call_openai_summary(
                    md[:80000],  # 과도한 길이 방지
                    model=args.openai_model,
                    timeout=args.openai_timeout,
                    debug=args.openai_debug,
                    max_retries=args.openai_max_retries,
                    initial_backoff=args.openai_initial_backoff,
                    max_backoff=args.openai_max_backoff,
                    min_interval=args.min_ai_interval,
                )
                perf_flag = ai["perf_flag"]
                importance = ai["importance"]
                summary_lines = ai["summary_5lines"]
                log(f"[OPENAI] 요약 성공 id={nid} imp={importance} perf={perf_flag}")
            except KeyboardInterrupt:
                raise
            except Exception as e:
                print(f"[AI-ERROR] {type(e).__name__}: {e}")
                append_failure(FAIL_LOG, f"OpenAI 실패: {type(e).__name__}: {e}", {"id": nid})
                # OpenAI 실패 시 HF가 켜져 있으면 HF로 폴백
                if getattr(args, "use_hf", False):
                    try:
                        ai = summarize_with_hf(
                            md[:40000],
                            model_name=args.hf_model,
                            max_length=args.hf_max_length,
                            min_length=args.hf_min_length,
                        )
                        perf_flag = ai["perf_flag"]
                        importance = ai["importance"]
                        summary_lines = ai["summary_5lines"]
                        log(f"[HF-FB] OpenAI 실패 → HF 요약 사용 id={nid} imp={importance} perf={perf_flag}")
                    except Exception as e2:
                        append_failure(FAIL_LOG, f"HF 실패: {type(e2).__name__}: {e2}", {"id": nid})
                        local = summarize_locally(md, title, created_date, url)
                        perf_flag = local["perf_flag"]
                        importance = local["importance"]
                        summary_lines = local["summary_5lines"]
                        log(f"[LOCAL-FB] HF 실패 → 로컬 요약 사용 id={nid} imp={importance} perf={perf_flag}")
                else:
                    local = summarize_locally(md, title, created_date, url)
                    perf_flag = local["perf_flag"]
                    importance = local["importance"]
                    summary_lines = local["summary_5lines"]
                    log(f"[LOCAL-FB] OpenAI 실패 → 로컬 요약 사용 id={nid} imp={importance} perf={perf_flag}")
        elif getattr(args, "use_hf", False):
            try:
                ai = summarize_with_hf(
                    md[:40000],
                    model_name=args.hf_model,
                    max_length=args.hf_max_length,
                    min_length=args.hf_min_length,
                )
                perf_flag = ai["perf_flag"]
                importance = ai["importance"]
                summary_lines = ai["summary_5lines"]
                log(f"[HF] 요약 사용 id={nid} imp={importance} perf={perf_flag}")
            except Exception as e:
                append_failure(FAIL_LOG, f"HF 실패: {type(e).__name__}: {e}", {"id": nid})
                local = summarize_locally(md, title, created_date, url)
                perf_flag = local["perf_flag"]
                importance = local["importance"]
                summary_lines = local["summary_5lines"]
                log(f"[LOCAL-FB] HF 실패 → 로컬 요약 사용 id={nid} imp={importance} perf={perf_flag}")
        else:
            # 로컬 휴리스틱 요약
            local = summarize_locally(md, title, created_date, url)
            perf_flag = local["perf_flag"]
            importance = local["importance"]
            summary_lines = local["summary_5lines"]
            log(f"[LOCAL] 요약 사용 id={nid} imp={importance} perf={perf_flag}")

        # 결과 적재
        out_row = {
            "created_date": created_date,
            "title": title,
            "id": nid,
            "url": url,
            "perf_flag": perf_flag,
            "importance": str(importance),
            "summary_5lines": "\n".join(summary_lines),
        }
        pending_rows.append(out_row)
        written_since_autosave += 1
        processed += 1

        # 진행 로그/자동 저장
        if args.progress_every and (processed % args.progress_every == 0):
            log(f"[진행] {processed}/{len(targets)}")
        if args.autosave_every and (written_since_autosave >= args.autosave_every):
            flush("자동 저장")

    # 마지막 저장
    flush("최종 저장")
    log(f"\n완료 ✅ 결과 저장: {args.output}")
    log(f"총 처리: {processed}/{len(targets)}")

if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except KeyboardInterrupt:
        log("\n사용자 중단(KeyboardInterrupt)")
        raise
    except Exception as e:
        append_failure(FAIL_LOG, f"치명적 오류: {type(e).__name__}: {e}")
        raise