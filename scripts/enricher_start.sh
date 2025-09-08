#!/usr/bin/env bash
set -euo pipefail
PLIST="$HOME/Library/LaunchAgents/com.leeseungsoo.notion_ai_enricher.plist"
if [[ ! -f "$PLIST" ]]; then
  echo "LaunchAgent not installed. Installing now..."
  SRC="$(cd "$(dirname "$0")"/.. && pwd)/tools/launchagent/com.leeseungsoo.notion_ai_enricher.plist"
  mkdir -p "$HOME/Library/LaunchAgents"
  cp -f "$SRC" "$PLIST"
fi
launchctl unload "$PLIST" 2>/dev/null || true
launchctl load -w "$PLIST"
launchctl kickstart -k "gui/$(id -u)/com.leeseungsoo.notion_ai_enricher" || true
echo "Started: com.leeseungsoo.notion_ai_enricher"

