#!/usr/bin/env bash
set -euo pipefail

PLIST="$HOME/Library/LaunchAgents/com.leeseungsoo.notion_scanner.plist"
launchctl stop com.leeseungsoo.notion_scanner 2>/dev/null || true
launchctl unload -w "$PLIST" 2>/dev/null || true
echo "Stopped and unloaded: com.leeseungsoo.notion_scanner"

