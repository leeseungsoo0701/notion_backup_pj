#!/usr/bin/env bash
set -euo pipefail

DIR="$(cd "$(dirname "$0")"/.. && pwd)"
cd "$DIR"

LOG_DIR="$DIR/out"
mkdir -p "$LOG_DIR"

INPUT="$DIR/out/manifest_dedup_sorted.csv"
OUTPUT="$DIR/out/manifest_ai_enriched.csv"

BASE_ARGS=(
  "--input" "$INPUT"
  "--output" "$OUTPUT"
  "--resume" "--only-missing"
  "--md-depth" "2"
  "--autosave-every" "20"
  "--autosave-interval-seconds" "30"
  "--progress-every" "200"
)

: ${OPENAI_API_KEY:=}
USE_OPENAI_ARGS=()
if [[ -n "${OPENAI_API_KEY}" ]]; then
  USE_OPENAI_ARGS=("--use-openai" "--summary-lang" "ko" "--min-ai-interval" "0.2")
fi

# prevent system sleep while running, print logs to console and file
(
  caffeinate -dimsu -w $$ 2>/dev/null &
  # Safe array expansion even when USE_OPENAI_ARGS is empty under set -u
  if [[ ${#USE_OPENAI_ARGS[@]:-0} -gt 0 ]]; then
    exec python3 -u "$DIR/export_manifest_ai_fields.py" "${BASE_ARGS[@]}" "${USE_OPENAI_ARGS[@]}"
  else
    exec python3 -u "$DIR/export_manifest_ai_fields.py" "${BASE_ARGS[@]}"
  fi
) 2>&1 | tee -a "$LOG_DIR/ai_job.log"
