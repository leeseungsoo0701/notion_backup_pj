from typing import Optional, Dict, List, Set, Union
from pathlib import Path
import notion_index_from_url as niu
from notion_index_from_url import *  # reuse helpers/constants (log, _req, BASE_URL, etc.)

BASE_DIR = Path(__file__).resolve().parent
DEFAULT_OUT_PATH = BASE_DIR / "out" / "manifest.csv"


def scan_mentions_workspace_batch20_autosave(
    out_csv_path: Union[str, Path] = DEFAULT_OUT_PATH,
    include_mentions: bool = True,
    mentions_block_limit: int = 200,
    incremental: bool = True,
    verbose: bool = False,
):
    """
    워크스페이스 전체를 /search + DB 쿼리로 훑되,
    '20개' 단위로 스캔 & 자동 저장하는 경량 스캐너.
    - 페이지(독립 페이지)와 DB 아이템(페이지)만 기록
    - 매칭 기준: 생성자/편집자 == 타깃, 또는 속성/본문에 타깃 멘션/이메일/이름 문자열 포함
    - out_csv_path: manifest.csv 저장 경로 (기본: 프로젝트 루트/out/manifest.csv)
    - include_mentions: 속성/본문 검색 ON/OFF
    - mentions_block_limit: 본문 블록 최대 스캔 수
    - incremental: seen_ids 기반 증분 실행
    """
    # --- 사전 준비 ---
    def _search(filter_type: Optional[str], start_cursor: Optional[str] = None, page_size: int = 20) -> dict:
        payload: dict = {
            "page_size": min(100, page_size),
            "sort": {"direction": "descending", "timestamp": "last_edited_time"},
        }
        if start_cursor:
            payload["start_cursor"] = start_cursor
        if filter_type in ("page", "database"):
            payload["filter"] = {"value": filter_type, "property": "object"}
        r = niu._req("POST", f"{BASE_URL}/search", json=payload)
        if r.status_code != 200:
            append_failure(FAIL_LOG, f"/search 실패 status={r.status_code}", {"payload": payload})
            return {"results": [], "has_more": False}
        return r.json()

    # 타깃 유저 ID 확보 (원본 모듈 전역 갱신)
    if not niu.TARGET_USER_ID:
        log("대상 사용자 ID 확인 중…")
        niu.TARGET_USER_ID = resolve_target_user_id()
        if not niu.TARGET_USER_ID:
            msg = f"대상 사용자 미발견: name='{TARGET_NAME}', email='{TARGET_EMAIL}'"
            log(msg); append_failure(FAIL_LOG, msg); return

    # 상태 로드
    scan_reg = load_scan_registry(SCAN_REGISTRY)
    seen_pages: Set[str] = scan_reg.get("pages", {}).get("seen_ids", set())
    seen_dbs: Set[str] = scan_reg.get("databases", {}).get("seen_ids", set())
    seen_db_items: Dict[str, Dict[str, Set[str]]] = scan_reg.get("db_items", {})
    out_csv_path = Path(out_csv_path).expanduser()
    manifest_ids: Set[str] = load_manifest_ids(out_csv_path)

    pending_rows: List[Dict] = []
    scanned_since_save = 0  # "스캔" 카운트(페이지/아이템 등 대상 1개 == 1)

    def _persist(reason: str):
        nonlocal pending_rows, scanned_since_save
        if pending_rows:
            append_rows(out_csv_path, pending_rows)
            pending_rows.clear()
        # 레지스트리 동기화
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
            "url_runs": scan_reg.get("url_runs", {}) or {},
        })
        if verbose:
            log(f"[저장] ({reason}) manifest & registry 저장 완료")
        scanned_since_save = 0

    def _maybe_persist():
        # 20개 스캔될 때마다 저장
        nonlocal scanned_since_save
        if scanned_since_save >= 20:
            _persist("20개 단위 자동 저장")

    def _add_if_match(obj: dict, obj_type: str, matched_reason: Optional[str]):
        nonlocal pending_rows
        if not matched_reason:
            return
        oid = obj.get("id")
        if not oid or oid in manifest_ids:
            return
        pending_rows.append({
            "created_date": created_date(obj),
            "title": get_title(obj),
            "id": oid,
            "url": obj.get("url"),
            "object_type": obj_type,   # 'page' 또는 'database_item'
            "methods": matched_reason,
        })
        manifest_ids.add(oid)

    def _match_page(page_id: str, page_obj: dict) -> Optional[str]:
        """페이지 단위 매칭 로직: 생성/편집자 or 속성/본문 멘션."""
        cby = (page_obj.get("created_by") or {}).get("id")
        eby = (page_obj.get("last_edited_by") or {}).get("id")
        if is_target_user(cby):
            return "페이지 생성자"
        if is_target_user(eby):
            return "페이지 편집자"
        if include_mentions:
            if page_has_target_in_properties(page_obj, TARGET_EMAIL) or \
               blocks_contains_target(page_id, TARGET_EMAIL, mentions_block_limit, verbose=verbose):
                return "페이지 속성/본문 언급"
        return None

    log("\n[배치20 스캔] 워크스페이스 전체 스캔 시작 (20개 단위 자동 저장)")
    # --- 1) 독립 페이지(= DB 소속이 아닐 수도 있는 페이지) 20개 단위 ---
    cur = None
    total_pages_scanned = 0
    while True:
        data = _search("page", start_cursor=cur, page_size=20)
        pages = data.get("results", [])
        if not pages:
            break
        for p_meta in pages:
            pid = p_meta.get("id")
            # 증분 체크
            if incremental and pid in seen_pages:
                scanned_since_save += 1
                total_pages_scanned += 1
                _maybe_persist()
                continue

            p = retrieve_page(pid)
            if not p:
                scanned_since_save += 1
                total_pages_scanned += 1
                _maybe_persist()
                continue

            matched = _match_page(pid, p)
            _add_if_match(p, "page", matched)

            if incremental:
                seen_pages.add(pid)

            scanned_since_save += 1
            total_pages_scanned += 1
            _maybe_persist()

        if not data.get("has_more"):
            break
        cur = data.get("next_cursor")

    # --- 2) 데이터베이스 → 각 아이템(페이지) 20개 단위 ---
    cur_db = None
    total_db_items_scanned = 0
    while True:
        data_db = _search("database", start_cursor=cur_db, page_size=20)
        dbs = data_db.get("results", [])
        if not dbs:
            break

        for db_meta in dbs:
            raw_did = db_meta.get("id")
            did = resolve_queryable_database_id(raw_did)
            if not did:
                continue

            # DB 메타는 seen_dbs 로 증분 관리(아이템을 별도로 스캔하므로 DB 자체 기록은 생략)
            if incremental and did in seen_dbs:
                pass  # 계속 진행

            # 아이템 페이지네이션 20개 단위
            cursor_items = None
            db_seen = (seen_db_items.get(did, {}) or {}).get("seen_ids", set())
            db_seen = db_seen if isinstance(db_seen, set) else set(db_seen or [])
            while True:
                q = db_query_simple(did, page_size=20, start_cursor=cursor_items)
                items = q.get("results", [])
                if not items:
                    break
                for it in items:
                    iid = it.get("id")
                    # 증분 체크
                    if incremental and iid in db_seen:
                        scanned_since_save += 1
                        total_db_items_scanned += 1
                        _maybe_persist()
                        continue

                    # DB 아이템도 본질적으로 페이지이므로 같은 매칭 로직 사용
                    matched = _match_page(iid, it)
                    _add_if_match(it, "database_item", matched)

                    if incremental and iid:
                        db_seen.add(iid)

                    scanned_since_save += 1
                    total_db_items_scanned += 1
                    _maybe_persist()

                if incremental:
                    seen_db_items[did] = {"seen_ids": db_seen}
                if not q.get("has_more"):
                    break
                cursor_items = q.get("next_cursor")

            if incremental:
                seen_dbs.add(did)

        if not data_db.get("has_more"):
            break
        cur_db = data_db.get("next_cursor")

    # 남은 것 저장
    _persist("최종 저장")

    log(f"[배치20 스캔] 완료 ✅  (독립 페이지 스캔={total_pages_scanned}, DB 아이템 스캔={total_db_items_scanned})")
    log(f"매니페스트: {out_csv_path}")
    log(f"레지스트리: {SCAN_REGISTRY}")
    log(f"실패로그: {FAIL_LOG}")

if __name__ == "__main__":
    import argparse

    default_out = str(DEFAULT_OUT_PATH)

    parser = argparse.ArgumentParser(description="Workspace-wide mention scan (20-per-batch autosave)")
    parser.add_argument("--out", type=str, default=default_out, help="manifest.csv 저장 경로")
    parser.add_argument("--include-mentions", dest="include_mentions", action="store_true", default=True,
                        help="속성/본문 멘션/이메일/이름 문자열 검색 ON (기본)")
    parser.add_argument("--no-include-mentions", dest="include_mentions", action="store_false",
                        help="속성/본문 멘션 검색 OFF")
    parser.add_argument("--mentions-block-limit", dest="mentions_block_limit", type=int, default=200,
                        help="본문 블록 스캔 상한 (기본 200)")
    parser.add_argument("--incremental", action="store_true", default=True,
                        help="증분 실행: 이미 저장/스캔한 페이지/아이템은 스킵 (기본 ON)")
    parser.add_argument("--full-rescan", dest="incremental", action="store_false",
                        help="증분 OFF: 전체 재스캔")
    parser.add_argument("--verbose", action="store_true", help="상세 로그 ON")

    args = parser.parse_args()

    # 실행: 20개씩 조회 & 20개씩 저장
    scan_mentions_workspace_batch20_autosave(
        out_csv_path=args.out,
        include_mentions=args.include_mentions,
        mentions_block_limit=args.mentions_block_limit,
        incremental=args.incremental,
        verbose=args.verbose,
    )
