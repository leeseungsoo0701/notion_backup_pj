#!/usr/bin/env python3
"""
Filter rows from out/manifest_ai_enriched.csv where perf_flag is yes and
importance >= threshold, and write them to a new CSV file while preserving
the original file unchanged.

Usage examples:
  - Default paths (reads out/manifest_ai_enriched.csv, writes out/manifest_ai_enriched_filtered.csv)
      python filter_manifest_ai_enriched.py

  - Custom paths and threshold
      python filter_manifest_ai_enriched.py \
        --input out/manifest_ai_enriched.csv \
        --output out/manifest_ai_enriched_perf3plus.csv \
        --min-importance 3
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


TRUTHY = {"yes", "y", "true", "1"}


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Filter enriched manifest by perf_flag and importance")
    p.add_argument(
        "--input",
        "-i",
        default="out/manifest_ai_enriched.csv",
        help="Input CSV path (default: out/manifest_ai_enriched.csv)",
    )
    p.add_argument(
        "--output",
        "-o",
        default="out/manifest_ai_enriched_filtered.csv",
        help="Output CSV path (default: out/manifest_ai_enriched_filtered.csv)",
    )
    p.add_argument(
        "--min-importance",
        "-m",
        type=int,
        default=3,
        help="Minimum importance to keep (default: 3)",
    )
    return p.parse_args()


def to_int(value: str, default: int = 0) -> int:
    try:
        return int(str(value).strip())
    except Exception:
        try:
            return int(float(str(value).strip()))
        except Exception:
            return default


def main() -> None:
    args = parse_args()
    in_path = Path(args.input)
    out_path = Path(args.output)

    if not in_path.exists():
        raise SystemExit(f"Input file not found: {in_path}")

    kept = 0
    total = 0

    # Ensure parent directory for output exists
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with in_path.open("r", encoding="utf-8", newline="") as f_in, out_path.open(
        "w", encoding="utf-8", newline=""
    ) as f_out:
        reader = csv.DictReader(f_in)

        required_cols = {"perf_flag", "importance"}
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

            if perf_raw in TRUTHY and importance >= args.min_importance:
                writer.writerow(row)
                kept += 1

    print(
        f"Filtered rows saved to: {out_path}\n"
        f"Criteria: perf_flag in {sorted(TRUTHY)} AND importance >= {args.min_importance}\n"
        f"Result: kept {kept} of {total} rows"
    )


if __name__ == "__main__":
    main()

