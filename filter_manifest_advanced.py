#!/usr/bin/env python3
"""
Advanced filter for out/manifest_ai_enriched.csv

Criteria (fixed):
  - perf_flag == yes (truthy)
  - importance >= 3
  - EXCLUDE titles containing "수동 CRM"
  - EXCLUDE titles containing any of: QAQC, React, AI (case-insensitive), anywhere in the title

Writes a new CSV without modifying the original.

Output path (default): out/manifest_ai_enriched_filtered_strict.csv
"""

from __future__ import annotations

import csv
import re
from pathlib import Path


INPUT_PATH = Path("out/manifest_ai_enriched.csv")
OUTPUT_PATH = Path("out/manifest_ai_enriched_filtered_strict.csv")

TRUTHY = {"yes", "y", "true", "1"}
TRACK_KEYWORDS = {"qaqc", "react", "ai"}


def to_int(value: str, default: int = 0) -> int:
    try:
        return int(str(value).strip())
    except Exception:
        try:
            return int(float(str(value).strip()))
        except Exception:
            return default


def title_is_excluded(title: str) -> bool:
    if not title:
        return False
    t = title.lower()
    # Exclude explicit manual CRM mentions
    if "수동 crm" in t:
        return True
    # Exclude if any track keyword appears anywhere in the title
    if any(k in t for k in TRACK_KEYWORDS):
        return True
    return False


def main() -> None:
    if not INPUT_PATH.exists():
        raise SystemExit(f"Input file not found: {INPUT_PATH}")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    kept = 0
    total = 0

    with INPUT_PATH.open("r", encoding="utf-8", newline="") as f_in, OUTPUT_PATH.open(
        "w", encoding="utf-8", newline=""
    ) as f_out:
        reader = csv.DictReader(f_in)
        required_cols = {"perf_flag", "importance", "title"}
        if not required_cols.issubset(set(reader.fieldnames or [])):
            missing = required_cols - set(reader.fieldnames or [])
            raise SystemExit(
                f"Missing required columns in input CSV: {', '.join(sorted(missing))}"
            )
        writer = csv.DictWriter(f_out, fieldnames=reader.fieldnames)
        writer.writeheader()

        for row in reader:
            total += 1
            perf_raw = str(row.get("perf_flag", "")).strip().lower()
            importance = to_int(row.get("importance", ""), default=0)
            title = str(row.get("title", ""))

            if perf_raw in TRUTHY and importance >= 3 and not title_is_excluded(title):
                writer.writerow(row)
                kept += 1

    print(
        f"Filtered (strict) rows saved to: {OUTPUT_PATH}\n"
        f"Criteria: perf_flag yes AND importance >= 3 AND exclude '수동 CRM' and titles containing QAQC/React/AI\n"
        f"Result: kept {kept} of {total} rows"
    )


if __name__ == "__main__":
    main()
