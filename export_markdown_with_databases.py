#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Export Notion page(s) to Markdown including descendant databases (raw rows as Markdown tables).

Input source: a CSV with a `url` column (default: out/manifest_ai_enriched_filtered_strict.csv).
Output: one .md per page under out/md_export/ that can be pasted/imported into a new Notion workspace.

Examples
  - Export first 5 pages from the filtered manifest:
      python export_markdown_with_databases.py --limit 5

  - Export specific input file and change output dir, limit DB rows per database:
      python export_markdown_with_databases.py -i out/manifest_ai_enriched_filtered.csv -o out/md_export --db-max-rows 300
"""

from __future__ import annotations

import argparse
import csv
import os
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# Reuse Notion API helpers and Markdown conversion
import export_manifest_ai_fields as em
import notion_index_from_url as niu


def normalize_id(s: str) -> str:
    """Return a hyphenated Notion UUID if given a 32-hex string; otherwise passthrough."""
    s = (s or "").strip()
    if not s:
        return s
    if "-" in s:
        return s
    if re.fullmatch(r"[0-9a-fA-F]{32}", s):
        return f"{s[0:8]}-{s[8:12]}-{s[12:16]}-{s[16:20]}-{s[20:32]}"
    return s


def url_to_page_id(url: str) -> Optional[str]:
    """Extract Notion page ID from a typical URL."""
    if not url:
        return None
    # Prefer the 32-hex at end
    m = re.search(r"([0-9a-fA-F]{32})(?:\?.*)?$", url)
    if m:
        return m.group(1)
    # Fallback: last hyphen part
    if "-" in url:
        tail = url.rsplit("-", 1)[-1]
        tail = re.sub(r"[^0-9a-fA-F]", "", tail)
        if re.fullmatch(r"[0-9a-fA-F]{32}", tail):
            return tail
    return None


def sanitize_filename(name: str) -> str:
    s = (name or "untitled").strip()
    s = re.sub(r"[\\/:*?\"<>|]+", "_", s)
    s = re.sub(r"\s+", " ", s)
    return s[:120].strip() or "untitled"


def property_value_to_text(prop: dict) -> str:
    t = prop.get("type")
    if t in ("title", "rich_text"):
        arr = prop.get(t) or []
        out = []
        for rt in arr:
            if rt.get("type") == "text":
                out.append(rt.get("text", {}).get("content", ""))
            elif rt.get("type") == "mention":
                m = rt.get("mention", {})
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
    # fallback: try simple stringification
    try:
        return str(prop.get(t, ""))
    except Exception:
        return ""


def database_to_markdown_table(db_id: str, max_rows: int = 500) -> Tuple[str, int]:
    """Query a database and return a Markdown table string and row count."""
    db_meta = niu.retrieve_database(db_id)
    if not db_meta:
        return "", 0
    title = ""
    try:
        title_arr = (db_meta.get("title") or [])
        title = "".join([(rt.get("plain_text") or "") for rt in title_arr])
    except Exception:
        title = ""

    # Collect properties (stable order: Name first if exists, then others by name)
    props = db_meta.get("properties") or {}
    prop_names = list(sorted(props.keys()))
    # Ensure title-like property first if present
    for key in ("Name", "Title", "name", "title"):
        if key in prop_names:
            prop_names.remove(key)
            prop_names.insert(0, key)
            break
    # We add a notion_url column at the end
    headers = prop_names + ["notion_url"]

    # Fetch rows
    rows: List[List[str]] = []
    cursor = None
    fetched = 0
    while True and fetched < max_rows:
        data = niu.db_query_simple(db_id, page_size=100, start_cursor=cursor)
        results = data.get("results", [])
        for item in results:
            if fetched >= max_rows:
                break
            props_obj = item.get("properties") or {}
            line: List[str] = []
            for name in prop_names:
                line.append(property_value_to_text(props_obj.get(name) or {"type": ""}))
            line.append(item.get("url") or "")
            rows.append(line)
            fetched += 1
        if not data.get("has_more") or fetched >= max_rows:
            break
        cursor = data.get("next_cursor")

    # Build Markdown table
    md_lines = []
    db_heading = f"### Database: {title or db_id}"
    md_lines.append(db_heading)
    md_lines.append("")
    # Header row
    md_lines.append("| " + " | ".join(headers) + " |")
    md_lines.append("| " + " | ".join(["---"] * len(headers)) + " |")
    for r in rows:
        # Escape pipe
        esc = [ (c or "").replace("|", "\|") for c in r ]
        md_lines.append("| " + " | ".join(esc) + " |")
    md_lines.append("")
    if fetched >= max_rows:
        md_lines.append(f"_…truncated to {max_rows} rows_\n")
    return "\n".join(md_lines), fetched


def export_page_with_databases(
    page_url: str,
    out_dir: Path,
    md_depth: int = 3,
    max_blocks: int = 3000,
    db_max_rows: int = 500,
    created_date: Optional[str] = None,
    csv_title: Optional[str] = None,
    csv_id: Optional[str] = None,
    perf_flag: Optional[str] = None,
    importance: Optional[str] = None,
    summary_5lines: Optional[str] = None,
) -> Path:
    """Export a page's markdown plus descendant databases into a single .md file.

    The output document header uses CSV-provided values:
      H1: "{created_date}_{title}"
      Then: Importance and Summary(5 lines), followed by page Markdown and DB tables.
    """
    pid_raw = url_to_page_id(page_url)
    if not pid_raw:
        raise ValueError(f"Invalid Notion URL (no page id): {page_url}")
    pid = normalize_id(pid_raw)

    # Page meta (title): prefer CSV title if provided; fallback to API
    title = (csv_title or "").strip()
    if not title:
        page = niu.retrieve_page(pid)
        title = "Untitled"
        try:
            props = page.get("properties", {})
            if "title" in props:
                arr = (props.get("title") or {}).get("title", [])
                if arr:
                    title = arr[0].get("plain_text", "Untitled")
        except Exception:
            pass

    # Markdown
    md = em.get_page_markdown(pid, max_blocks=max_blocks, depth=md_depth)

    # Descendant databases
    _, dbs = niu.collect_descendant_pages_and_dbs(pid, verbose=False)
    # Resolve linked databases to source if needed
    resolved_dbs: List[str] = []
    for did in dbs:
        rid = niu.resolve_queryable_database_id(did) or did
        if rid not in resolved_dbs:
            resolved_dbs.append(rid)

    # Build final markdown
    out_lines = []
    display_title = f"{(created_date or '').strip()}_{title}".strip("_")
    # Add YAML front matter for properties
    fm_lines: List[str] = [
        "---",
        f"created_date: {(created_date or '').strip()}",
        f"id: {(csv_id or '').strip()}",
        f"url: {page_url}",
        f"perf_flag: {(perf_flag or '').strip()}",
        f"importance: {(importance or '').strip()}",
    ]
    if summary_5lines:
        fm_lines.append("summary_5lines:")
        for s in [x for x in str(summary_5lines).splitlines() if x.strip()][:5]:
            fm_lines.append(f"  - {s}")
    fm_lines.append("---")
    out_lines.extend(fm_lines)
    out_lines.append("")
    out_lines.append(f"# {display_title}")
    out_lines.append("")
    # Properties as markdown table for readability
    out_lines.append("| Property | Value |")
    out_lines.append("| --- | --- |")
    out_lines.append(f"| created_date | {(created_date or '').strip()} |")
    out_lines.append(f"| id | {(csv_id or '').strip()} |")
    out_lines.append(f"| url | {page_url} |")
    out_lines.append(f"| perf_flag | {(perf_flag or '').strip()} |")
    out_lines.append(f"| importance | {(importance or '').strip()} |")
    if summary_5lines:
        out_lines.append("| summary_5lines | |")
        for s in [x for x in str(summary_5lines).splitlines() if x.strip()][:5]:
            out_lines.append(f"|  | - {s.strip()} |")
    out_lines.append("")
    # Original URL for traceability
    out_lines.append(f"Original: {page_url}")
    out_lines.append("")
    if md:
        out_lines.append(md)
        out_lines.append("")

    if resolved_dbs:
        out_lines.append("## Databases")
        out_lines.append("")
        for db_id in resolved_dbs:
            try:
                tbl_md, cnt = database_to_markdown_table(db_id, max_rows=db_max_rows)
                if tbl_md.strip():
                    out_lines.append(tbl_md)
                    out_lines.append("")
            except Exception as e:
                em.append_failure(em.FAIL_LOG, f"DB export failed: {db_id}")

    # Write file
    out_dir.mkdir(parents=True, exist_ok=True)
    fname = f"{sanitize_filename(display_title)}__{pid_raw[:8]}.md"
    out_path = out_dir / fname
    with out_path.open("w", encoding="utf-8") as f:
        f.write("\n".join(out_lines).strip() + "\n")
    return out_path


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Export Notion page(s) markdown + descendant DBs")
    p.add_argument("--input", "-i", default="out/manifest_ai_enriched_filtered_strict.csv", help="CSV path with a url column")
    p.add_argument("--output-dir", "-o", default="out/md_export", help="Output directory for .md files")
    p.add_argument("--limit", "-n", type=int, default=0, help="Process only first N rows (0=all)")
    p.add_argument("--skip", type=int, default=0, help="Skip first K rows before processing")
    p.add_argument("--md-depth", type=int, default=3, help="Markdown children depth (default 3)")
    p.add_argument("--max-blocks", type=int, default=3000, help="Max blocks to scan per page")
    p.add_argument("--db-max-rows", type=int, default=500, help="Max rows per database table")
    return p.parse_args()


def main() -> None:
    args = parse_args()

    # Ensure tokens (env/Keychain/prompt)
    em._resolve_tokens_from_keychain_or_prompt()
    if not em.API_TOKEN or em.API_TOKEN == "PUT_YOUR_INTEGRATION_TOKEN_HERE":
        em.log("❗ NOTION_TOKEN을 설정하세요 (.env, Keychain, 또는 프롬프트)")
        raise SystemExit(2)
    em.validate_token_ascii(em.API_TOKEN)

    in_path = Path(args.input)
    if not in_path.exists():
        raise SystemExit(f"Input CSV not found: {in_path}")

    out_dir = Path(args.output_dir)

    # Read CSV and iterate
    total = 0
    done = 0
    with in_path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    total = len(rows)

    start = max(0, int(args.skip or 0))
    end = start + int(args.limit) if args.limit and args.limit > 0 else total
    sel = rows[start:end]

    em.log(f"Exporting {len(sel)} of {total} rows → {out_dir}")
    for idx, row in enumerate(sel, start=1):
        url = (row.get("url") or row.get("URL") or "").strip()
        title = (row.get("title") or row.get("Title") or "").strip()
        rid = (row.get("id") or row.get("ID") or "").strip()
        created_date = (row.get("created_date") or row.get("Created") or "").strip()
        perf_flag = (row.get("perf_flag") or row.get("Perf") or "").strip()
        importance = str(row.get("importance") or "").strip()
        summary = (row.get("summary_5lines") or "").strip()
        if not url:
            continue
        try:
            out_path = export_page_with_databases(
                url, out_dir,
                md_depth=args.md_depth, max_blocks=args.max_blocks, db_max_rows=args.db_max_rows,
                created_date=created_date, csv_title=title, csv_id=rid, perf_flag=perf_flag,
                importance=importance, summary_5lines=summary
            )
            done += 1
            em.log(f"[{idx}/{len(sel)}] ✓ {title or url} → {out_path}")
        except Exception as e:
            em.append_failure(em.FAIL_LOG, f"Export failed: {url}")
            em.log(f"[{idx}/{len(sel)}] ✗ {title or url} → error: {e}")

    em.log(f"Done. Exported {done}/{len(sel)} pages. Output: {out_dir}")


if __name__ == "__main__":
    main()
