#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
notion_index_from_url.py - URL(여러 개) 기준으로 트리 전체 인덱싱 (속도↑/URL단위 로그/재처리 제어)

- 입력 URL(페이지/DB/뷰/링크드DB)에서 시작해 모든 하위 페이지/DB/DB아이템까지 재귀 크롤링
- 정확 매칭(기본): 이름=="이승수(PM팀)" AND 이메일=="ss.lee@teamsparta.co"
- 옵션(기본 ON): --include-mentions 페이지 속성/일부 블록 텍스트에서 멘션/이메일 포함 시 매칭
- manifest.csv 중복(id) 저장 방지 / scan_registry.json 증분 스캔
- **로그 최소화**: 기본은 URL 시작/요약만 출력(quiet). 상세는 --verbose
- **URL 재처리 제어**: url_runs에 마지막 실행/매칭 시각 저장. 이미 처리된 URL은 묻고/자동스킵/강제재처리 가능
"""

import os
import sys
import csv
import json
import time
import signal
import re
import hashlib
from typing import Dict, List, Set, Optional, Tuple
from datetime import datetime

import requests

# ================= 사용자 설정 =================
TARGET_NAME = "이승수(PM팀)"
TARGET_EMAIL = "ss.lee@teamsparta.co"

API_TOKEN = os.environ.get("NOTION_TOKEN", "").strip() or "PUT_YOUR_INTEGRATION_TOKEN_HERE"
NOTION_VERSION = "2022-06-28"
BASE_URL = "https://api.notion.com/v1"

# 출력 경로
OUT_DIR = "./out"
MANIFEST_CSV = os.path.join(OUT_DIR, "manifest.csv")
FAIL_LOG = os.path.join(OUT_DIR, "failures_index.txt")
SCAN_REGISTRY = os.path.join(OUT_DIR, "scan_registry.json")

# ================= 전역 =================
_session = requests.Session()
_session.trust_env = True

TARGET_USER_ID: Optional[str] = None

# ================= 유틸 =================
def log(msg=""):
    try:
        print(msg, flush=True)
    except Exception:
        print(str(msg).encode("ascii", "replace").decode("ascii"), flush=True)

def vlog(enabled: bool, msg: str):
    if enabled:
        log(msg)

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
        log("HTTP 헤더 'Authorization(Token)'에 비-ASCII 문자가 포함되어 있습니다.")
        sys.exit(2)

def headers() -> Dict[str, str]:
    return {
        "Authorization": f"Bearer {API_TOKEN}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json",
    }

def created_date(item: dict) -> str:
    iso = item.get("created_time") or ""
    try:
        return iso.split("T")[0] if iso else "1970-01-01"
    except Exception:
        return "1970-01-01"

def get_title(item: dict) -> str:
    if item.get("object") == "database":
        arr = item.get("title") or []
        parts = []
        for t in arr:
            if t.get("type") == "text":
                parts.append(t.get("text", {}).get("content", ""))
        return "".join(parts) or "제목없는 DB"

    props = item.get("properties") or {}
    for _, prop in props.items():
        if prop and prop.get("type") == "title":
            arr = prop.get("title") or []
            if arr:
                parts = []
                for it in arr:
                    t = it.get("text", {})
                    parts.append(t.get("content", "") or "")
                s = "".join(parts).strip()
                return s or "제목없음"
    return "제목없음"

def now_ts() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# ================= 스토리지 =================
def ensure_manifest_header(csv_path: str):
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)
    if not os.path.exists(csv_path) or os.path.getsize(csv_path) == 0:
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["created_date", "title", "id", "url", "object_type", "methods"])

def append_rows(csv_path: str, rows: List[Dict]):
    if not rows:
        return
    ensure_manifest_header(csv_path)
    with open(csv_path, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        for r in rows:
            w.writerow([r["created_date"], r["title"], r["id"], r["url"], r["object_type"], r["methods"]])

def load_manifest_ids(csv_path: str) -> Set[str]:
    ids: Set[str] = set()
    try:
        if os.path.exists(csv_path) and os.path.getsize(csv_path) > 0:
            with open(csv_path, "r", newline="", encoding="utf-8") as f:
                rdr = csv.DictReader(f)
                for row in rdr:
                    rid = (row.get("id") or "").strip()
                    if rid:
                        ids.add(rid)
    except Exception as e:
        append_failure(FAIL_LOG, f"매니페스트 로드 실패: {e}")
    return ids

def _json_set_default(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError

def load_scan_registry(path: str) -> dict:
    try:
        if not os.path.exists(path):
            return {"pages": {"seen_ids": set()}, "databases": {"seen_ids": set()}, "db_items": {}, "url_runs": {}}
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        pages_seen = set(data.get("pages", {}).get("seen_ids", []))
        dbs_seen = set(data.get("databases", {}).get("seen_ids", []))
        db_items = data.get("db_items", {}) or {}
        norm_db_items = {}
        for k, v in db_items.items():
            s = set((v or {}).get("seen_ids", []))
            norm_db_items[k] = {"seen_ids": s}
        return {
            "pages": {"seen_ids": pages_seen},
            "databases": {"seen_ids": dbs_seen},
            "db_items": norm_db_items,
            "url_runs": data.get("url_runs", {}) or {},
        }
    except Exception as e:
        append_failure(FAIL_LOG, f"레지스트리 로드 실패: {e}")
        return {"pages": {"seen_ids": set()}, "databases": {"seen_ids": set()}, "db_items": {}, "url_runs": {}}

def save_scan_registry(path: str, reg: dict):
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        to_save = {
            "pages": {"seen_ids": list(reg.get("pages", {}).get("seen_ids", set()))},
            "databases": {"seen_ids": list(reg.get("databases", {}).get("seen_ids", set()))},
            "db_items": {},
            "url_runs": reg.get("url_runs", {}) or {},
        }
        db_items = reg.get("db_items", {}) or {}
        for k, v in db_items.items():
            if isinstance(v, dict):
                s = list(v.get("seen_ids", set()))
            elif isinstance(v, set):
                s = list(v)
            else:
                s = list(v or [])
            to_save["db_items"][k] = {"seen_ids": s}
        with open(path, "w", encoding="utf-8") as f:
            json.dump(to_save, f, ensure_ascii=False, indent=2, default=_json_set_default)
    except Exception as e:
        append_failure(FAIL_LOG, f"레지스트리 저장 실패(I/O): {e}")

# ================= Notion API 래퍼 =================
def _req(method: str, url: str, **kwargs):
    tries = 0
    while True:
        tries += 1
        try:
            r = _session.request(method, url, headers=headers(), timeout=60, **kwargs)
            if r.status_code in (429, 502, 503):
                time.sleep(min(1.0 * tries, 5))
                continue
            return r
        except Exception:
            if tries < 3:
                time.sleep(0.5 * tries)
                continue
            raise

def blocks_children(parent_id: str, start_cursor: Optional[str] = None, page_size: int = 100):
    params = {"page_size": min(100, page_size)}
    if start_cursor:
        params["start_cursor"] = start_cursor
    url = f"{BASE_URL}/blocks/{parent_id}/children"
    r = _req("GET", url, params=params)
    if r.status_code != 200:
        if r.status_code == 404:
            append_failure(FAIL_LOG, f"/blocks/{parent_id}/children 404 → 삭제/권한/잘못된ID 가능. URL/권한 확인 필요")
        else:
            append_failure(FAIL_LOG, f"/blocks/{parent_id}/children 실패 status={r.status_code}")
        return {"results": [], "has_more": False}
    return r.json()

def retrieve_page(page_id: str) -> Optional[dict]:
    r = _req("GET", f"{BASE_URL}/pages/{page_id}")
    if r.status_code != 200:
        append_failure(FAIL_LOG, f"/pages/{page_id} 실패 status={r.status_code}")
        return None
    return r.json()

def retrieve_database(db_id: str) -> Optional[dict]:
    r = _req("GET", f"{BASE_URL}/databases/{db_id}")
    if r.status_code != 200:
        append_failure(FAIL_LOG, f"/databases/{db_id} 실패 status={r.status_code}")
        return None
    return r.json()

def db_query_simple(db_id: str, page_size=100, start_cursor: Optional[str] = None) -> dict:
    payload = {"page_size": min(100, page_size)}
    if start_cursor:
        payload["start_cursor"] = start_cursor
    r = _req("POST", f"{BASE_URL}/databases/{db_id}/query", json=payload)
    if r.status_code != 200:
        if r.status_code == 400:
            append_failure(FAIL_LOG, f"/databases/{db_id}/query 400 → DB 아님(링크드/뷰/페이지?) 또는 요청 형식 문제. 정규화 시도 필요", {"payload": payload})
        else:
            append_failure(FAIL_LOG, f"/databases/{db_id}/query 실패 status={r.status_code}", {"payload": payload})
        return {"results": [], "has_more": False}
    return r.json()

def list_users_page(start_cursor: Optional[str] = None) -> dict:
    params = {"page_size": 100}
    if start_cursor:
        params["start_cursor"] = start_cursor
    r = _req("GET", f"{BASE_URL}/users", params=params)
    if r.status_code != 200:
        append_failure(FAIL_LOG, f"/users 실패 status={r.status_code}")
        return {"results": [], "has_more": False}
    return r.json()

# ================= 타깃 유저 =================
def resolve_target_user_id() -> Optional[str]:
    cursor = None
    pages = 0
    while True:
        data = list_users_page(cursor)
        results = data.get("results", [])
        for u in results:
            if u.get("type") != "person":
                continue
            name = (u.get("name") or "").strip()
            email = (u.get("person", {}) or {}).get("email", "").strip()
            if name == TARGET_NAME and email == TARGET_EMAIL:
                return u.get("id")
        if not data.get("has_more"):
            break
        cursor = data.get("next_cursor")
        pages += 1
        if pages % 10 == 0:
            # 이 로그는 드물게만 발생
            log(f"  /users 페이지 {pages}개 스캔 중…")
    return None

def is_target_user(user_id: Optional[str]) -> bool:
    return bool(user_id) and (user_id == TARGET_USER_ID)

# ================= 멘션/속성 검사 =================
def page_has_target_in_properties(page: dict, target_email: str) -> bool:
    props = page.get("properties") or {}
    for p in props.values():
        t = p.get("type")
        if t == "people":
            for person in p.get("people", []):
                if person.get("object") == "user" and is_target_user(person.get("id")):
                    return True
        elif t == "email":
            if (p.get("email") or "").strip().lower() == target_email.lower():
                return True
        elif t in ("rich_text", "title"):
            arr = p.get(t) or []
            text = []
            for rt in arr:
                if rt.get("type") == "text":
                    text.append(rt.get("text", {}).get("content", ""))
                elif rt.get("type") == "mention":
                    m = rt.get("mention", {})
                    if m.get("type") == "user":
                        user = m.get("user", {})
                        if user.get("object") == "user" and is_target_user(user.get("id")):
                            return True
            if text:
                s = "".join(text)
                if target_email.lower() in s.lower() or TARGET_NAME in s:
                    return True
    return False

def blocks_contains_target(page_id: str, target_email: str, max_blocks: int = 200, verbose: bool = False) -> bool:
    scanned = 0
    cursor = None
    while True and scanned < max_blocks:
        vlog(verbose, f"[본문스캔] blocks.children parent={page_id} cursor={cursor or 'start'}")
        data = blocks_children(page_id, start_cursor=cursor, page_size=100)
        for blk in data.get("results", []):
            scanned += 1
            rt = blk.get("paragraph") or blk.get("heading_1") or blk.get("heading_2") or blk.get("heading_3") \
                or blk.get("bulleted_list_item") or blk.get("numbered_list_item") or blk.get("to_do") \
                or blk.get("toggle") or blk.get("callout") or blk.get("quote")
            if not rt:
                continue
            arr = rt.get("rich_text", []) or []
            textbuf = []
            for rto in arr:
                if rto.get("type") == "text":
                    textbuf.append(rto.get("text", {}).get("content", ""))
                elif rto.get("type") == "mention":
                    m = rto.get("mention", {})
                    if m.get("type") == "user":
                        user = m.get("user", {})
                        if is_target_user(user.get("id")):
                            return True
            if textbuf:
                s = "".join(textbuf)
                if target_email.lower() in s.lower() or TARGET_NAME in s:
                    return True
        if not data.get("has_more"):
            break
        cursor = data.get("next_cursor")
    return False

# ================= URL → ID 파싱 =================
UUID_RE = re.compile(r"([0-9a-f]{32}|[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})", re.IGNORECASE)

def extract_id_from_url(url: str) -> Optional[str]:
    m = UUID_RE.search(url)
    if not m:
        return None
    raw = m.group(1).replace("-", "")
    # Notion canonical id 형식으로 변환
    return f"{raw[0:8]}-{raw[8:12]}-{raw[12:16]}-{raw[16:20]}-{raw[20:32]}"

def url_key_from_url(url: str) -> str:
    rid = extract_id_from_url(url)
    if rid:
        return rid.lower()
    # fallback: full url hash (뷰 파라미터만 있고 UUID가 안 잡히는 링크 대비)
    return hashlib.sha1(url.encode("utf-8")).hexdigest()

# ================= DB 정규화 =================
def resolve_queryable_database_id(maybe_id: str) -> Optional[str]:
    """
    주어진 ID가 데이터베이스로 쿼리 가능한지 확인하고,
    아니라면 link_to_database 블록을 통해 원본 DB id로 치유한다.
    반환: 쿼리 가능한 database_id 또는 None(스킵)
    """
    try:
        r = _session.get(f"{BASE_URL}/databases/{maybe_id}", headers=headers(), timeout=60)
    except Exception as e:
        append_failure(FAIL_LOG, f"DB 확인 중 네트워크 오류: {e}", {"database_id": maybe_id})
        return None
    if r.status_code == 200:
        return maybe_id

    # DB가 아니면 블록으로 확인 (link_to_database 치유)
    try:
        rb = _session.get(f"{BASE_URL}/blocks/{maybe_id}", headers=headers(), timeout=60)
    except Exception as e:
        append_failure(FAIL_LOG, f"블록 확인 중 네트워크 오류: {e}", {"block_id": maybe_id})
        return None
    if rb.status_code != 200:
        append_failure(FAIL_LOG, f"DB 식별 실패: {maybe_id} (db_get={r.status_code}, block_get={rb.status_code})")
        return None
    b = rb.json()
    if b.get("type") == "link_to_database":
        src = (b.get("link_to_database") or {}).get("database_id")
        if src:
            r2 = _session.get(f"{BASE_URL}/databases/{src}", headers=headers(), timeout=60)
            if r2.status_code == 200:
                return src
            append_failure(FAIL_LOG, "link_to_database 원본 검증 실패", {"source_database_id": src, "status": r2.status_code})
            return None
    append_failure(FAIL_LOG, f"DB 아님 또는 권한 없음: {maybe_id}")
    return None

# ================= 트리 수집 =================
def collect_descendant_pages_and_dbs(root_id: str, verbose: bool = False) -> Tuple[Set[str], Set[str]]:
    """
    주어진 root_id(페이지/DB/블록) 아래 전체 child_page / child_database / link_to_database 원본 DB를 수집
    """
    pages: Set[str] = set()
    dbs: Set[str] = set()
    stack = [root_id]

    while stack:
        parent = stack.pop()
        cursor = None
        while True:
            vlog(verbose, f"[하위 스캔] blocks.children parent={parent} cursor={cursor or 'start'}")
            data = blocks_children(parent, start_cursor=cursor, page_size=100)
            results = data.get("results", [])
            for blk in results:
                btype = blk.get("type")
                blk_id = blk.get("id")
                if btype == "child_page":
                    pid = blk.get("id")
                    if pid and pid not in pages:
                        pages.add(pid)
                        stack.append(pid)
                        vlog(verbose, f"  · child_page: {pid}")
                elif btype == "child_database":
                    did = blk.get("id")
                    if did and did not in dbs:
                        dbs.add(did)
                        vlog(verbose, f"  · child_database: {did}")
                elif btype == "link_to_database":
                    info = blk.get("link_to_database") or {}
                    src_id = info.get("database_id")
                    if src_id and src_id not in dbs:
                        dbs.add(src_id)
                        vlog(verbose, f"  · link_to_database 원본 DB: {src_id}")
                if blk.get("has_children"):
                    stack.append(blk_id)
            if not data.get("has_more"):
                break
            cursor = data.get("next_cursor")
    return pages, dbs

# ================= 메인 =================
def main():
    import argparse

    parser = argparse.ArgumentParser(description="Notion URL에서 시작해 트리 전체 인덱싱")
    parser.add_argument("--url", action="append", help="시작 Notion URL (여러 번 지정 가능)")
    parser.add_argument("--urls-file", type=str, help="URL 목록 파일(줄바꿈 구분)")
    parser.add_argument("--incremental", action="store_true", help="증분 모드(레지스트리 사용/갱신)")
    parser.add_argument("--autosave-every", type=int, default=300, help="N개마다 manifest/레지스트리 자동 저장")
    parser.add_argument("--registry-flush-every", type=int, default=500, help="페이지/블록 N개 스캔마다 레지스트리 저장/로그")
    # 로그 모드: 기본 quiet, 상세는 --verbose
    grp = parser.add_mutually_exclusive_group()
    grp.add_argument("--quiet", action="store_true", default=True, help="URL 단위 요약 로그만 표시(기본 권장, 속도 ↑)")
    grp.add_argument("--verbose", action="store_true", help="상세 진행 로그 표시(느려질 수 있음)")
    # include-mentions 기본 ON
    mentions_group = parser.add_mutually_exclusive_group()
    mentions_group.add_argument("--include-mentions", "--include_mentions", action="store_true",
                                dest="include_mentions", default=True,
                                help="(기본) 페이지 속성/일부 블록 텍스트에서 대상 언급/이메일 포함시 매칭 간주")
    mentions_group.add_argument("--no-include-mentions", "--no_include_mentions", action="store_false",
                                dest="include_mentions",
                                help="멘션/속성 스캔 끄기")
    parser.add_argument("--mentions-block-limit", "--mentions_block_limit", type=int, default=200,
                        dest="mentions_block_limit",
                        help="본문 블록 스캔 최대 개수(기본 200)")
    # 재처리 제어
    parser.add_argument("--auto-skip-processed", action="store_true", help="이전에 처리한 URL은 묻지 않고 건너뜀")
    parser.add_argument("--force-reprocess", action="store_true", help="이전에 처리한 URL이라도 무조건 재처리(프롬프트 없이)")
    parser.add_argument("--no-ask-existing", action="store_true", help="이미 처리한 URL에 대해 묻지 않음(기본은 묻기)")
    args = parser.parse_args()

    # 토큰 체크
    if not API_TOKEN or API_TOKEN == "PUT_YOUR_INTEGRATION_TOKEN_HERE":
        log("❗ NOTION_TOKEN 환경변수를 설정하거나 스크립트의 API_TOKEN을 실제 토큰으로 바꾸세요.")
        sys.exit(2)
    validate_token_ascii(API_TOKEN)

    # URL 준비
    urls: List[str] = []
    if args.url:
        urls.extend(args.url)
    if args.urls_file and os.path.exists(args.urls_file):
        with open(args.urls_file, "r", encoding="utf-8") as f:
            for line in f:
                s = line.strip()
                if s:
                    urls.append(s)
    if not urls:
        log("시작 URL이 없습니다. --url 또는 --urls-file 을 사용하세요.")
        sys.exit(1)

    # 중단 처리
    stop_flag = {"stop": False}
    def on_sigint(signum, frame):
        stop_flag["stop"] = True
        log("\n사용자 중단: 진행분 저장 중…")
    signal.signal(signal.SIGINT, on_sigint)

    # 타깃 유저
    log("대상 사용자 ID 확인 중…")
    global TARGET_USER_ID
    TARGET_USER_ID = resolve_target_user_id()
    if not TARGET_USER_ID:
        msg = f"대상 사용자 미발견: name='{TARGET_NAME}', email='{TARGET_EMAIL}'"
        log(msg); append_failure(FAIL_LOG, msg); sys.exit(1)
    log(f"대상 사용자 ID: {TARGET_USER_ID}")
    log(f"멘션/속성 스캔: {'ON' if args.include_mentions else 'OFF'} (블록 최대 {args.mentions_block_limit})")
    if args.verbose:
        log("로그: 상세(Verbose)")
    else:
        log("로그: URL 단위 요약만 출력(quiet)")

    verbose = bool(args.verbose)

    # 상태/스토리지
    scan_reg = load_scan_registry(SCAN_REGISTRY)
    seen_pages: Set[str] = scan_reg.get("pages", {}).get("seen_ids", set())
    seen_dbs: Set[str] = scan_reg.get("databases", {}).get("seen_ids", set())
    seen_db_items: Dict[str, Dict[str, Set[str]]] = scan_reg.get("db_items", {})
    url_runs: Dict[str, dict] = scan_reg.get("url_runs", {}) or {}
    manifest_ids: Set[str] = load_manifest_ids(MANIFEST_CSV)
    log(f"manifest.csv 로드됨: {len(manifest_ids)}건 (중복 저장 스킵)")

    processed_since_autosave = 0
    pending_rows: List[Dict] = []

    def persist_progress(reason: str, log_it: bool = False):
        nonlocal pending_rows
        if pending_rows:
            append_rows(MANIFEST_CSV, pending_rows)
            pending_rows.clear()
        # 레지스트리 저장
        fixed = {}
        for k, v in (seen_db_items or {}).items():
            if isinstance(v, dict):
                s = v.get("seen_ids", set())
                s = s if isinstance(s, set) else set(s or [])
            else:
                s = set(v or [])
            fixed[k] = {"seen_ids": s}
        save_scan_registry(SCAN_REGISTRY, {
            "pages": {"seen_ids": seen_pages},
            "databases": {"seen_ids": seen_dbs},
            "db_items": fixed,
            "url_runs": url_runs,
        })
        if log_it or verbose:
            log(f"[저장] {reason} → manifest/registry 동기화 완료")

    # 매칭 추가 (URL 단위 누적 카운터/마지막 매칭 시각 업데이트를 호출측에서 주입)
    def make_add_match_row(url_match_counts: dict, last_match_ts_holder: dict):
        def add_match_row(obj: dict, obj_type: str, matched_reason: str):
            nonlocal processed_since_autosave, pending_rows
            oid = obj.get("id")
            if oid in manifest_ids:
                return
            pending_rows.append({
                "created_date": created_date(obj),
                "title": get_title(obj),
                "id": oid,
                "url": obj.get("url"),
                "object_type": obj_type,
                "methods": matched_reason,
            })
            manifest_ids.add(oid)
            url_match_counts[obj_type] = url_match_counts.get(obj_type, 0) + 1
            last_match_ts_holder["ts"] = now_ts()
            processed_since_autosave += 1
            if args.autosave_every and processed_since_autosave >= args.autosave_every:
                persist_progress("자동 저장")
                processed_since_autosave = 0
        return add_match_row

    # URL별 실행
    for idx, url in enumerate(urls, start=1):
        if stop_flag["stop"]:
            break

        # URL 메타/키
        log(f"\n[{idx}/{len(urls)}] 시작 URL: {url}")
        root = extract_id_from_url(url)
        if not root:
            log("  · ID 추출 실패 → 스킵"); append_failure(FAIL_LOG, "URL ID 추출 실패", {"url": url}); continue

        ukey = url_key_from_url(url)
        meta = url_runs.get(ukey)

        # 이미 처리된 URL 제어
        if meta and not args.force_reprocess:
            last_run = meta.get("last_run_ts")
            last_match = meta.get("last_match_ts")
            if args.auto_skip_processed or args.no_ask_existing:
                log(f"[SKIP] 이전 처리(URL): last_run={last_run}, last_match={last_match} → {url}")
                continue
            # 묻기
            print(f"이미 처리된 URL입니다. 마지막 실행: {last_run}, 마지막 매칭: {last_match} — 다시 처리할까요? [y/N]: ", end="", flush=True)
            try:
                ans = input().strip().lower()
            except EOFError:
                ans = "n"
            if ans != "y":
                log(f"[SKIP] 사용자 선택으로 건너뜀 → {url}")
                continue

        url_start = time.time()
        url_match_counts = {"page": 0, "database": 0, "database_item": 0}
        last_match_ts_holder = {"ts": None}
        add_match_row = make_add_match_row(url_match_counts, last_match_ts_holder)

        # 트리 수집 (조용)
        pages, dbs = collect_descendant_pages_and_dbs(root, verbose=verbose)

        # 루트 자체도 페이지/DB일 수 있으니 추가 시도
        p = retrieve_page(root)
        if p:
            pages.add(root)
        else:
            d = retrieve_database(root)
            if d:
                dbs.add(root)

        vlog(verbose, f"  · 수집 요약: pages={len(pages)}, dbs(raw)={len(dbs)}")

        # 페이지 처리
        for i, pid in enumerate(pages, start=1):
            if stop_flag["stop"]: break
            vlog(verbose, f"[페이지] ({i}/{len(pages)}) page={pid}")
            page = retrieve_page(pid)
            if not page:
                continue
            if args.incremental and pid in seen_pages:
                continue
            cby = (page.get("created_by") or {}).get("id")
            eby = (page.get("last_edited_by") or {}).get("id")
            matched = None
            if is_target_user(cby):
                matched = "페이지 생성자"
            elif is_target_user(eby):
                matched = "페이지 편집자"
            elif args.include_mentions:
                if page_has_target_in_properties(page, TARGET_EMAIL) or \
                   blocks_contains_target(pid, TARGET_EMAIL, args.mentions_block_limit, verbose=verbose):
                    matched = "페이지 속성/본문 언급"
            if matched:
                add_match_row(page, "page", matched)
            if args.incremental:
                seen_pages.add(pid)

        # DB 처리
        for j, raw_did in enumerate(dbs, start=1):
            if stop_flag["stop"]: break
            vlog(verbose, f"[DB] ({j}/{len(dbs)}) normalize & retrieve: raw={raw_did}")
            did = resolve_queryable_database_id(raw_did)
            if not did:
                vlog(verbose, f"  · DB 스킵(식별 실패/권한): {raw_did}")
                continue

            dbobj = retrieve_database(did)
            if not dbobj:
                continue
            if not (args.incremental and did in seen_dbs):
                cby = (dbobj.get("created_by") or {}).get("id")
                eby = (dbobj.get("last_edited_by") or {}).get("id")
                matched = None
                if is_target_user(cby):
                    matched = "DB 생성자"
                elif is_target_user(eby):
                    matched = "DB 편집자"
                elif args.include_mentions and page_has_target_in_properties(dbobj, TARGET_EMAIL):
                    matched = "DB 속성 언급"
                if matched:
                    add_match_row(dbobj, "database", matched)
                if args.incremental:
                    seen_dbs.add(did)

            # DB 아이템 페이지네이션
            cursor = None
            queried_items = 0
            db_seen = (seen_db_items.get(did, {}) or {}).get("seen_ids", set())
            db_seen = db_seen if isinstance(db_seen, set) else set(db_seen or [])
            while True:
                data = db_query_simple(did, page_size=100, start_cursor=cursor)
                results = data.get("results", [])
                if not results:
                    break
                for item in results:
                    iid = item.get("id")
                    if args.incremental and iid in db_seen:
                        continue
                    cby = (item.get("created_by") or {}).get("id")
                    eby = (item.get("last_edited_by") or {}).get("id")
                    matched = None
                    if is_target_user(cby):
                        matched = "DB항목 생성자"
                    elif is_target_user(eby):
                        matched = "DB항목 편집자"
                    elif args.include_mentions and page_has_target_in_properties(item, TARGET_EMAIL):
                        matched = "DB항목 속성 언급"
                    if matched:
                        add_match_row(item, "database_item", matched)
                    if args.incremental and iid:
                        db_seen.add(iid)
                queried_items += len(results)
                vlog(verbose, f"  · [DB 진행] {did} 누적 아이템 {queried_items}")
                if args.incremental:
                    seen_db_items[did] = {"seen_ids": db_seen}
                if not data.get("has_more"):
                    break
                cursor = data.get("next_cursor")

        # URL 단위 저장/요약
        url_end = time.time()
        dur = int(url_end - url_start)
        url_runs[ukey] = {
            "source_url": url,
            "root_id": root,
            "last_run_ts": now_ts(),
            "last_match_ts": last_match_ts_holder["ts"],
            "counts": url_match_counts,
            "include_mentions": args.include_mentions,
        }
        persist_progress(f"URL 완료: {url}", log_it=False)
        log(f"URL 완료: {url}")
        log(f" - 처리 시간: {dur}s, 매칭(page/db/item): {url_match_counts['page']}/{url_match_counts['database']}/{url_match_counts['database_item']}")
        log(f" - 마지막 매칭 시각: {last_match_ts_holder['ts'] or '없음'}")

    # 최종 저장
    persist_progress("최종 저장", log_it=False)
    log("\n완료 ✅")
    log(f"매니페스트: {MANIFEST_CSV}")
    log(f"레지스트리: {SCAN_REGISTRY}")
    log(f"실패로그: {FAIL_LOG}")
    log("힌트: 다음 실행 시 이미 처리한 URL을 자동 스킵하려면 --auto-skip-processed 옵션을 사용하세요.")

# ================= 엔트리 =================
if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception as e:
        append_failure(FAIL_LOG, f"치명적 오류: {e}")
        raise