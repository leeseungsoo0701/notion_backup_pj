#!/usr/bin/env bash
set -euo pipefail

DIR="$(cd "$(dirname "$0")"/.. && pwd)"
cd "$DIR"

LOG_DIR="$DIR/out"
mkdir -p "$LOG_DIR"

OUT_PATH="$DIR/out/manifest.csv"

# Loop interval sources (priority: arg > env > file > default)
DEFAULT_SECS=60
CLI_SECS="${1:-}"
ENV_SECS="${SCAN_LOOP_SECONDS:-}"
FILE_SECS_PATH="$LOG_DIR/scan_interval_seconds"

resolve_secs() {
  local v="$1"
  if [[ -n "$v" && "$v" =~ ^[0-9]+$ && "$v" -gt 0 ]]; then
    echo "$v"
  else
    echo ""
  fi
}

BASE_SECS=$(resolve_secs "$CLI_SECS") || true
if [[ -z "$BASE_SECS" ]]; then BASE_SECS=$(resolve_secs "$ENV_SECS") || true; fi
if [[ -z "$BASE_SECS" ]]; then BASE_SECS="$DEFAULT_SECS"; fi

trap 'echo "[scanner] received TERM, exiting"; exit 0' TERM INT

# Keep Mac awake while this daemon runs
caffeinate -dimsu -w $$ 2>/dev/null &

echo "[scanner] daemon started at $(date '+%F %T')"
echo "[scanner] base interval: ${BASE_SECS}s (arg/env/default)"
while true; do
  echo "[scanner] pass start $(date '+%F %T')"
  python3 -u "$DIR/notion_backup.py" \
    --out "$OUT_PATH" \
    --include-mentions \
    --mentions-block-limit 200 \
    --incremental \
    --verbose || true
  echo "[scanner] pass done $(date '+%F %T')"
  # Allow dynamic override via file each loop
  LOOP_SECS=$(resolve_secs "$(cat "$FILE_SECS_PATH" 2>/dev/null || true)") || true
  if [[ -z "$LOOP_SECS" ]]; then LOOP_SECS="$BASE_SECS"; fi
  echo "[scanner] sleeping ${LOOP_SECS}s (update by writing seconds to $FILE_SECS_PATH)"
  sleep "$LOOP_SECS"
done 2>&1 | tee -a "$LOG_DIR/scan.log"
