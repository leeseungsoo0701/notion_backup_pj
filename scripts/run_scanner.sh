#!/usr/bin/env bash
set -euo pipefail

DIR="$(cd "$(dirname "$0")"/.. && pwd)"
cd "$DIR"

LOG_DIR="$DIR/out"
mkdir -p "$LOG_DIR"

# Output manifest path (incremental-safe between runs)
OUT_PATH="$DIR/out/manifest.csv"

# Keep Mac awake while scanning; stream logs to file
(
  caffeinate -dimsu -w $$ 2>/dev/null &
  exec python3 -u "$DIR/notion_backup.py" \
    --out "$OUT_PATH" \
    --include-mentions \
    --mentions-block-limit 200 \
    --incremental
) 2>&1 | tee -a "$LOG_DIR/scan.log"

