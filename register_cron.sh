#!/usr/bin/env bash
#set -euo pipefail

# ───────── CONFIG ─────────
# Absolute path to your run.sh
CURRENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

SCRIPT_PATH="$CURRENT_DIR/run.sh"
# Optional: where to log output
LOG_PATH="$CURRENT_DIR/run.log"
# ──────────────────────────

# Ensure the script exists and is executable
if [ ! -x "$SCRIPT_PATH" ]; then
  echo "❌ Cannot execute $SCRIPT_PATH. Please check the path and permissions." >&2
  exit 1
fi

# The exact cron line we want
CRON_ENTRY="0 6,18 * * * $SCRIPT_PATH >> $LOG_PATH 2>&1"

# Install (or update) it into crontab
( crontab -l 2>/dev/null | grep -Fv "$SCRIPT_PATH" ; echo "$CRON_ENTRY" ) | crontab -

echo "Crontab updated. The job will run at 06:00 and 18:00 daily."
