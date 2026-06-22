#!/bin/sh
set -eu

if [ "$#" -ne 1 ]; then
  echo "usage: $0 <logs-dir>" >&2
  exit 2
fi

LOG_DIR="$1"

if [ ! -d "$LOG_DIR" ]; then
  echo "ALLOW | archive gate satisfied (no logs dir)"
  exit 0
fi

unreviewed=$(grep -rl "reviewed: false" "$LOG_DIR" 2>/dev/null | wc -l | tr -d ' ')
if [ "$unreviewed" -gt 0 ]; then
  echo "BLOCK | $unreviewed unreviewed logs"
  exit 1
fi

echo "ALLOW | archive gate satisfied"
