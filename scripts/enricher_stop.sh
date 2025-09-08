#!/usr/bin/env bash
set -euo pipefail
PLIST="$HOME/Library/LaunchAgents/com.leeseungsoo.notion_ai_enricher.plist"
launchctl stop com.leeseungsoo.notion_ai_enricher 2>/dev/null || true
launchctl unload -w "$PLIST" 2>/dev/null || true
echo "Stopped and unloaded: com.leeseungsoo.notion_ai_enricher"

