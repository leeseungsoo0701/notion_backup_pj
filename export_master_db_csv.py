#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Export all pages and descendant database rows into ONE CSV for Notion DB import.

Rows include both page content and DB rows with unified columns:
  - record_type: 'page' | 'db_row'
  - created_date: page created_date or row created_time (if available)
  - title: for page → '{created_date}_{title}', for db_row → row title (best-effort)
  - id, url: source IDs/URLs
  - importance, perf_flag, summary_5lines: from enriched CSV (pages only)
  - markdown: full page markdown (pages only)
  - source_db_id, source_db_title: set for db_row
  - properties_json: JSON-serialized flattened properties (db_row only)

Usage examples:
  - Default: read out/manifest_ai_enriched_filtered_strict.csv and export first 5 pages
      python export_master_db_csv.py --limit 5

  - Use full enriched file and export more
      python export_master_db_csv.py -i out/manifest_ai_enriched.csv --limit 50
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import export_manifest_ai_fields as em
import notion_index_from_url as niu
from export_markdown_with_databases import url_to_page_id, normalize_id


def text_for_property(prop: dict) -> str:
    """Convert a Notion property value to a readable text for CSV, similar to markdown exporter."""
    t = prop.get("type")
    if t in ("title", "rich_text"):
        arr = prop.get(t) or []
        out = []
        for rt in arr:
            if rt.get("type") == "text":
                out.append(rt.get("text", {}).get("content", ""))
            elif rt.get("type") == "mention":
                m = rt.get("mention", {}) or {}
                if m.get("type") == "user":
                    name = (m.get("user", {}) or {}).get("name", "user")
                    out.append(f"@{name}")
        return "".join(out)
    if t == "number":
        v = prop.get("number")
        return "" if v is None else str(v)
    if t == "select":
        o = (prop.get("select") or {}).get("name")
        return o or ""
    if t == "multi_select":
        arr = prop.get("multi_select") or []
        return ", ".join([x.get("name", "") for x in arr if x])
    if t == "date":
        d = prop.get("date") or {}
        start = d.get("start") or ""
        end = d.get("end") or ""
        return f"{start} ~ {end}".strip(" ~")
    if t == "checkbox":
        return "true" if prop.get("checkbox") else "false"
    if t == "url":
        return prop.get("url") or ""
    if t == "email":
        return prop.get("email") or ""
    if t == "phone_number":
        return prop.get("phone_number") or ""
    if t == "people":
        arr = prop.get("people") or []
        return ", ".join([(p.get("name") or p.get("id") or "user") for p in arr])
    if t == "files":
        arr = prop.get("files") or []
        names = []
        for f in arr:
            n = f.get("name") or "file"
            names.append(n)
        return ", ".join(names)
    if t == "relation":
        arr = prop.get("relation") or []
        return ", ".join([x.get("id", "") for x in arr])
    if t == "status":
        o = (prop.get("status") or {}).get("name")
        return o or ""
    return ""


def flatten_properties(props: dict) -> Dict[str, str]:
    out: Dict[str, str] = {}
    for name, p in (props or {}).items():
        try:
            out[name] = text_for_property(p)
        except Exception:
            out[name] = ""
    return out


def best_row_title(props: dict) -> str:
    for key in ("Name", "Title", "name", "title"):
        if key in (props or {}):
            return text_for_property(props.get(key) or {"type": ""}) or "Untitled"
    # fallback: first property with text
    for name, p in (props or {}).items():
        s = text_for_property(p)
        if s:
            return s
    return "Untitled"


def export_to_master_csv(
    input_csv: Path,
    output_csv: Path,
    limit: int = 0,
    skip: int = 0,
    md_depth: int = 3,
    max_blocks: int = 3000,
    db_max_rows: int = 500,
) -> Tuple[int, int]:
    # tokens
    em._resolve_tokens_from_keychain_or_prompt()
    if not em.API_TOKEN or em.API_TOKEN == "PUT_YOUR_INTEGRATION_TOKEN_HERE":
        raise SystemExit("NOTION_TOKEN missing")
    em.validate_token_ascii(em.API_TOKEN)

    # read rows
    with input_csv.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    total = len(rows)
    start = max(0, int(skip or 0))
    end = start + int(limit) if limit and limit > 0 else total
    sel = rows[start:end]

    # header
    cols = [
        "record_type",
        "created_date",
        "title",
        "id",
        "url",
        "importance",
        "perf_flag",
        "summary_5lines",
        "markdown",
        "source_db_id",
        "source_db_title",
        "properties_json",
    ]
    output_csv.parent.mkdir(parents=True, exist_ok=True)
    with output_csv.open("w", encoding="utf-8", newline="") as f_out:
        w = csv.DictWriter(f_out, fieldnames=cols)
        w.writeheader()

        pages_done = 0
        db_rows_done = 0
        for idx, row in enumerate(sel, start=1):
            url = (row.get("url") or row.get("URL") or "").strip()
            title = (row.get("title") or row.get("Title") or "").strip()
            created_date = (row.get("created_date") or row.get("Created") or "").strip()
            importance = str(row.get("importance") or "").strip()
            perf_flag = str(row.get("perf_flag") or "").strip()
            summary = (row.get("summary_5lines") or "").strip()
            if not url:
                continue

            # page markdown
            pid_raw = url_to_page_id(url)
            if not pid_raw:
                continue
            pid = normalize_id(pid_raw)
            md = em.get_page_markdown(pid, max_blocks=max_blocks, depth=md_depth)

            display_title = f"{created_date}_{title}".strip("_")
            w.writerow({
                "record_type": "page",
                "created_date": created_date,
                "title": display_title,
                "id": pid,
                "url": url,
                "importance": importance,
                "perf_flag": perf_flag,
                "summary_5lines": summary,
                "markdown": md,
                "source_db_id": "",
                "source_db_title": "",
                "properties_json": "",
            })
            pages_done += 1

            # descendant databases → rows
            _, dbs = niu.collect_descendant_pages_and_dbs(pid, verbose=False)
            resolved_dbs: List[str] = []
            for did in dbs:
                rid = niu.resolve_queryable_database_id(did) or did
                if rid not in resolved_dbs:
                    resolved_dbs.append(rid)
            for db_id in resolved_dbs:
                # fetch DB meta
                db_meta = niu.retrieve_database(db_id)
                db_title = ""
                try:
                    title_arr = (db_meta.get("title") or [])
                    db_title = "".join([(rt.get("plain_text") or "") for rt in title_arr])
                except Exception:
                    db_title = ""

                cursor = None
                fetched = 0
                while True and fetched < db_max_rows:
                    data = niu.db_query_simple(db_id, page_size=100, start_cursor=cursor)
                    results = data.get("results", [])
                    for item in results:
                        if fetched >= db_max_rows:
                            break
                        props = item.get("properties") or {}
                        row_title = best_row_title(props)
                        props_flat = flatten_properties(props)
                        w.writerow({
                            "record_type": "db_row",
                            "created_date": (item.get("created_time") or "")[:10],
                            "title": row_title,
                            "id": item.get("id") or "",
                            "url": item.get("url") or "",
                            "importance": "",
                            "perf_flag": "",
                            "summary_5lines": "",
                            "markdown": "",
                            "source_db_id": db_id,
                            "source_db_title": db_title,
                            "properties_json": json.dumps(props_flat, ensure_ascii=False),
                        })
                        db_rows_done += 1
                        fetched += 1
                    if not data.get("has_more") or fetched >= db_max_rows:
                        break
                    cursor = data.get("next_cursor")

        return pages_done, db_rows_done


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Export pages and DB rows into a single CSV for Notion import")
    p.add_argument("--input", "-i", default="out/manifest_ai_enriched_filtered_strict.csv", help="Input CSV with url column")
    p.add_argument("--output", "-o", default="out/master_export.csv", help="Output CSV path")
    p.add_argument("--limit", "-n", type=int, default=0, help="Process only first N input rows (0=all)")
    p.add_argument("--skip", type=int, default=0, help="Skip first K input rows")
    p.add_argument("--md-depth", type=int, default=3, help="Markdown depth for page content")
    p.add_argument("--max-blocks", type=int, default=3000, help="Max blocks per page")
    p.add_argument("--db-max-rows", type=int, default=500, help="Max rows per database")
    return p.parse_args()


def main() -> None:
    args = parse_args()
    in_path = Path(args.input)
    out_path = Path(args.output)
    pages_done, db_rows_done = export_to_master_csv(
        in_path, out_path, limit=args.limit, skip=args.skip,
        md_depth=args.md_depth, max_blocks=args.max_blocks, db_max_rows=args.db_max_rows,
    )
    em.log(f"Saved: {out_path}")
    em.log(f"Pages: {pages_done}, DB rows: {db_rows_done}")


if __name__ == "__main__":
    main()

