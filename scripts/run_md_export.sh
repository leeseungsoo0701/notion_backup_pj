#!/usr/bin/env bash
set -euo pipefail

INPUT="out/manifest_ai_enriched_filtered_strict.csv"
OUT_DIR="out/md_export"
PID_FILE="out/md_export.pid"
LOG_FILE="out/md_export.nohup"

mkdir -p "${OUT_DIR}"

# If a previous PID exists and is running, do not start a duplicate
if [[ -f "${PID_FILE}" ]];
then
  PID=$(cat "${PID_FILE}" || true)
  if [[ -n "${PID}" ]] && ps -p "${PID}" >/dev/null 2>&1; then
    echo "Exporter already running with PID ${PID}."
    exit 0
  fi
fi

echo "Starting Markdown export in background…"
nohup python3 export_markdown_with_databases.py \
  -i "${INPUT}" \
  -o "${OUT_DIR}" \
  --db-max-rows 500 \
  --skip-existing \
  > "${LOG_FILE}" 2>&1 &

echo $! > "${PID_FILE}"
echo "Started. PID=$(cat ${PID_FILE}). Logs: ${LOG_FILE}"

