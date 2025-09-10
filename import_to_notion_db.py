#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Import pages into a single Notion database: creates DB (optional) and for each input row
creates a DB item (page) with properties and clones the original page blocks (best effort).

Input CSV columns expected: created_date, title, id, url, perf_flag, importance, summary_5lines

Examples
  - Use an existing database and import first 5 rows:
      python import_to_notion_db.py -i out/manifest_ai_enriched.csv --database-id YOUR_DATABASE_ID --limit 5

  - Create a new database under a parent page and import 5 rows:
      python import_to_notion_db.py -i out/manifest_ai_enriched.csv --parent-page-id YOUR_PARENT_PAGE_ID --create-db --limit 5
"""

from __future__ import annotations

import argparse
import csv
import time
from typing import Dict, List, Optional, Tuple

import export_manifest_ai_fields as em
import notion_index_from_url as niu
from export_markdown_with_databases import url_to_page_id, normalize_id, database_to_markdown_table


# ---------------- Notion helpers (write) ----------------
def notion_headers() -> Dict[str, str]:
    return {
        "Authorization": f"Bearer {em.API_TOKEN}",
        "Notion-Version": em.NOTION_VERSION,
        "Content-Type": "application/json",
    }


def create_database(parent_page_id: str, title: str = "Imported Pages") -> Optional[str]:
    body = {
        "parent": {"type": "page_id", "page_id": parent_page_id},
        "title": [{"type": "text", "text": {"content": title}}],
        "properties": {
            "Title": {"title": {}},
            "Importance": {"number": {"format": "number"}},
            "Perf": {"checkbox": {}},
            "Summary": {"rich_text": {}},
            "Source URL": {"url": {}},
            "Source ID": {"rich_text": {}},
            "Created Date": {"date": {}},
        },
    }
    r = niu._req("POST", f"{niu.BASE_URL}/databases", json=body)
    if r.status_code != 200:
        em.append_failure(em.FAIL_LOG, f"DB 생성 실패 status={r.status_code}", {"body": body})
        return None
    return r.json().get("id")


def create_page_in_database(
    db_id: str,
    title_text: str,
    importance: Optional[int],
    perf_flag: Optional[str],
    summary_text: str,
    source_url: str,
    source_id: str,
    created_date: str,
    children: Optional[List[dict]] = None,
) -> Optional[str]:
    props = {
        "Title": {"title": [{"type": "text", "text": {"content": title_text[:200]}}]},
        "Importance": {"number": int(importance) if str(importance).strip().isdigit() else None},
        "Perf": {"checkbox": str(perf_flag).strip().lower() in {"yes", "y", "true", "1"}},
        "Summary": {"rich_text": [{"type": "text", "text": {"content": summary_text[:2000]}}]} if summary_text else {"rich_text": []},
        "Source URL": {"url": source_url or None},
        "Source ID": {"rich_text": [{"type": "text", "text": {"content": source_id}}] if source_id else []},
        "Created Date": {"date": {"start": created_date}} if created_date else {"date": None},
    }
    body = {
        "parent": {"type": "database_id", "database_id": db_id},
        "properties": props,
    }
    if children:
        body["children"] = children[:90]  # initial chunk, rest appended
    r = niu._req("POST", f"{niu.BASE_URL}/pages", json=body)
    if r.status_code != 200:
        em.append_failure(em.FAIL_LOG, f"페이지 생성 실패 status={r.status_code}", {"db_id": db_id})
        return None
    return r.json().get("id")


def append_children(parent_block_id: str, children: List[dict]) -> bool:
    if not children:
        return True
    body = {"children": children}
    r = niu._req("PATCH", f"{niu.BASE_URL}/blocks/{parent_block_id}/children", json=body)
    if r.status_code != 200:
        em.append_failure(em.FAIL_LOG, f"children append 실패 status={r.status_code}")
        return False
    return True


def strip_rich_text(rt_arr: List[dict]) -> List[dict]:
    out = []
    for o in rt_arr or []:
        t = o.get("type")
        if t not in ("text", "mention", "equation"):
            continue
        obj = {"type": t}
        if t == "text":
            obj["text"] = (o.get("text") or {})
        elif t == "mention":
            obj["mention"] = (o.get("mention") or {})
        elif t == "equation":
            obj["equation"] = (o.get("equation") or {})
        ann = o.get("annotations") or {}
        if ann:
            obj["annotations"] = ann
        href = o.get("href")
        if href:
            obj["href"] = href
        out.append(obj)
    return out


def block_to_creatable(block: dict) -> Tuple[Optional[dict], List[dict]]:
    """Map a fetched Notion block to a creatable block (best effort). Returns (block, children_to_fetch)."""
    btype = block.get("type")
    data = block.get(btype) or {}
    children_ids: List[dict] = []

    def rt(key: str) -> List[dict]:
        return strip_rich_text(data.get(key) or [])

    if btype in ("paragraph", "quote"):
        return ({btype: {"rich_text": rt("rich_text")}}, [])
    if btype in ("heading_1", "heading_2", "heading_3"):
        return ({btype: {"rich_text": rt("rich_text")}}, [])
    if btype in ("bulleted_list_item", "numbered_list_item"):
        creatable = {btype: {"rich_text": rt("rich_text")}}
        if block.get("has_children"):
            children_ids.append({"id": block.get("id")})
        return (creatable, children_ids)
    if btype == "to_do":
        creatable = {"to_do": {"rich_text": rt("rich_text"), "checked": bool(data.get("checked"))}}
        if block.get("has_children"):
            children_ids.append({"id": block.get("id")})
        return (creatable, children_ids)
    if btype == "code":
        creatable = {"code": {"rich_text": rt("rich_text"), "language": data.get("language") or ""}}
        return (creatable, [])
    if btype == "divider":
        return ({"divider": {}}, [])
    if btype == "bookmark":
        url = data.get("url") or ""
        return ({"bookmark": {"url": url}}, [])
    if btype == "image":
        # Convert to paragraph with URL (avoid expired file URLs)
        url = ""
        try:
            img = data
            t = img.get("type")
            if t == "external":
                url = (img.get("external") or {}).get("url", "")
            elif t == "file":
                url = (img.get("file") or {}).get("url", "")
        except Exception:
            url = ""
        txt = {"type": "text", "text": {"content": url or ""}}
        return ({"paragraph": {"rich_text": [txt]}}, [])
    if btype in ("toggle",):
        creatable = {"toggle": {"rich_text": rt("rich_text")}}
        if block.get("has_children"):
            children_ids.append({"id": block.get("id")})
        return (creatable, children_ids)
    if btype == "table":
        # Fallback: render table as a code block with markdown table text
        tbl_md = ""
        try:
            from export_manifest_ai_fields import _table_block_to_md
            tbl_md = _table_block_to_md(block.get("id"))
        except Exception:
            tbl_md = ""
        txt = {"type": "text", "text": {"content": tbl_md or "(table omitted)"}}
        return ({"code": {"rich_text": [txt], "language": "markdown"}}, [])
    # Skip unsupported or structural blocks (child_page, child_database, link_to_database handled separately)
    return (None, [])


def fetch_children_blocks(block_id: str) -> List[dict]:
    """Fetch direct children blocks of a block/page."""
    results: List[dict] = []
    cursor = None
    while True:
        data = niu.blocks_children(block_id, start_cursor=cursor, page_size=100)
        arr = data.get("results", [])
        results.extend(arr)
        if not data.get("has_more"):
            break
        cursor = data.get("next_cursor")
    return results


def collect_creatable_tree(root_page_id: str, max_blocks: int = 800) -> List[dict]:
    """Collect blocks from source page and convert to creatable blocks with nested children (best effort)."""
    created: List[dict] = []
    count = 0

    def walk(parent_id: str, attach_to: List[dict]):
        nonlocal count
        children = fetch_children_blocks(parent_id)
        for blk in children:
            if count >= max_blocks:
                break
            b, child_refs = block_to_creatable(blk)
            if not b:
                # Skip child_page / child_database etc.
                continue
            # If there are children to fetch (list/toggle), fetch and attach recursively
            if child_refs and blk.get("has_children"):
                b[ list(b.keys())[0] ]["children"] = []
                attach_to.append(b)
                count += 1
                try:
                    walk(blk.get("id"), b[ list(b.keys())[0] ]["children"])  # recurse into this block's children
                except Exception:
                    pass
            else:
                attach_to.append(b)
                count += 1

    walk(root_page_id, created)
    return created


# ---------------- Main import flow ----------------
def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Import pages into one Notion database and clone content")
    p.add_argument("--input", "-i", default="out/manifest_ai_enriched.csv", help="Input CSV with enriched fields")
    p.add_argument("--limit", "-n", type=int, default=5, help="Process first N rows")
    p.add_argument("--skip", type=int, default=0, help="Skip first K rows")
    p.add_argument("--database-id", type=str, help="Target Notion database ID (existing)")
    p.add_argument("--parent-page-id", type=str, help="Parent page ID to create new database under")
    p.add_argument("--create-db", action="store_true", help="Create a new database under parent page")
    p.add_argument("--include-child-dbs", action="store_true", help="Append child databases as markdown tables at bottom")
    p.add_argument("--db-max-rows", type=int, default=200, help="Max rows per child database when included")
    p.add_argument("--max-blocks", type=int, default=800, help="Max blocks to clone per page")
    return p.parse_args()


def main() -> None:
    args = parse_args()

    # tokens
    em._resolve_tokens_from_keychain_or_prompt()
    if not em.API_TOKEN or em.API_TOKEN == "PUT_YOUR_INTEGRATION_TOKEN_HERE":
        raise SystemExit("❗ NOTION_TOKEN 미설정: .env/Keychain/프롬프트로 설정하세요.")
    em.validate_token_ascii(em.API_TOKEN)

    # read input
    with open(args.input, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    start = max(0, int(args.skip or 0))
    end = start + int(args.limit) if args.limit and args.limit > 0 else len(rows)
    sel = rows[start:end]

    # resolve database
    db_id = (args.database_id or "").strip()
    if not db_id and args.create_db:
        parent = (args.parent_page_id or "").strip()
        if not parent:
            raise SystemExit("--create-db requires --parent-page-id")
        db_id = create_database(parent, title="Imported Pages")
        if not db_id:
            raise SystemExit("Failed to create database")
        em.log(f"DB created: {db_id}")
    if not db_id:
        raise SystemExit("Provide --database-id to use existing DB or --create-db with --parent-page-id")

    # process rows
    em.log(f"Importing {len(sel)} rows into DB {db_id}")
    done = 0
    for idx, r in enumerate(sel, start=1):
        url = (r.get("url") or r.get("URL") or "").strip()
        title = (r.get("title") or r.get("Title") or "").strip()
        created_date = (r.get("created_date") or "").strip()
        perf_flag = (r.get("perf_flag") or "").strip()
        importance = (r.get("importance") or "").strip()
        summary = (r.get("summary_5lines") or "").strip()
        if not url:
            continue
        pid_raw = url_to_page_id(url)
        if not pid_raw:
            continue
        pid = normalize_id(pid_raw)

        display_title = f"{created_date}_{title}".strip("_")
        # collect content blocks to clone
        try:
            children = collect_creatable_tree(pid, max_blocks=args.max_blocks)
        except Exception as e:
            children = []

        page_id = create_page_in_database(
            db_id,
            title_text=display_title,
            importance=importance,
            perf_flag=perf_flag,
            summary_text=summary,
            source_url=url,
            source_id=pid,
            created_date=created_date,
            children=children[:80],
        )
        if not page_id:
            em.log(f"[{idx}/{len(sel)}] ✗ {display_title} (page create failed)")
            continue

        # Append remaining blocks in chunks
        rest = children[80:]
        while rest:
            chunk = rest[:80]
            rest = rest[80:]
            ok = append_children(page_id, chunk)
            if not ok:
                break
            time.sleep(0.2)

        # Include child databases as markdown tables at bottom
        if args.include_child_dbs:
            try:
                _, dbs = niu.collect_descendant_pages_and_dbs(pid)
                md_blocks: List[dict] = []
                if dbs:
                    # heading
                    md_blocks.append({"heading_2": {"rich_text": [{"type": "text", "text": {"content": "Databases"}}]}})
                    for did in dbs:
                        rid = niu.resolve_queryable_database_id(did) or did
                        tbl_md, _cnt = database_to_markdown_table(rid, max_rows=args.db_max_rows)
                        if tbl_md.strip():
                            md_blocks.append({"code": {"language": "markdown", "rich_text": [{"type": "text", "text": {"content": tbl_md[:1800]}}]}})
                if md_blocks:
                    append_children(page_id, md_blocks)
            except Exception:
                pass

        done += 1
        em.log(f"[{idx}/{len(sel)}] ✓ {display_title} → page_id={page_id}")

    em.log(f"Done. Imported {done}/{len(sel)} rows → DB {db_id}")


if __name__ == "__main__":
    main()

