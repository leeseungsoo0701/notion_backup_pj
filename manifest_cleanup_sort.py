#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
manifest_cleanup_sort_date_in_title.py
- manifest.csv 중복 제거 + 제목 앞 날짜 또는 created_date 기준 정렬
"""

import csv
import os
import re
from datetime import datetime

IN_PATH = "/Users/seungsoo/Desktop/notion_backup_0907/out/manifest.csv"
OUT_PATH = "/Users/seungsoo/Desktop/notion_backup_0907/out/manifest_dedup_sorted.csv"

HEADERS = ["created_date", "title", "id", "url", "object_type", "methods"]

DATE_PATTERN = re.compile(r"^(20\\d{2}-\\d{2}-\\d{2})")

def _parse_date(s: str) -> datetime:
    s = (s or "").strip()
    for fmt in ("%Y-%m-%d", "%Y/%m/%d", "%Y.%m.%d"):
        try:
            return datetime.strptime(s, fmt)
        except Exception:
            pass
    return datetime(9999, 12, 31)

def extract_date_from_title_or_created(row) -> datetime:
    """제목 앞 날짜 있으면 그걸, 없으면 created_date 사용"""
    title = (row.get("title") or "").strip()
    m = DATE_PATTERN.match(title)
    if m:
        try:
            return datetime.strptime(m.group(1), "%Y-%m-%d")
        except Exception:
            pass
    return _parse_date(row.get("created_date", ""))

def main():
    if not os.path.exists(IN_PATH):
        raise SystemExit(f"입력 파일이 없습니다: {IN_PATH}")

    # id별 병합
    by_id = {}
    with open(IN_PATH, "r", newline="", encoding="utf-8") as f:
        rdr = csv.DictReader(f)
        for row in rdr:
            rid = (row.get("id") or "").strip()
            if not rid:
                continue
            if rid not in by_id:
                by_id[rid] = row
                by_id[rid]["methods_set"] = set([row.get("methods","")])
            else:
                d = by_id[rid]
                # created_date는 가장 이른 것 선택
                if _parse_date(row["created_date"]) < _parse_date(d["created_date"]):
                    d["created_date"] = row["created_date"]
                if row.get("methods"):
                    d["methods_set"].add(row["methods"])

    merged = []
    for rid, d in by_id.items():
        merged.append({
            "created_date": d["created_date"],
            "title": d["title"],
            "id": d["id"],
            "url": d["url"],
            "object_type": d["object_type"],
            "methods": " | ".join(sorted([m for m in d["methods_set"] if m]))
        })

    # 정렬: 제목 앞 날짜 or created_date → title
    merged.sort(key=lambda x: (extract_date_from_title_or_created(x),
                               (x["title"] or "").casefold()))

    # 기존 파일 삭제 후 새로 작성
    if os.path.exists(OUT_PATH):
        os.remove(OUT_PATH)

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=HEADERS)
        w.writeheader()
        for r in merged:
            w.writerow(r)

    print(f"입력: {IN_PATH}")
    print(f"출력: {OUT_PATH}")
    print(f"정렬된 행 수: {len(merged):,}")

if __name__ == "__main__":
    main()