#!/bin/sh
set -eu

if [ "$#" -ne 1 ]; then
  echo "usage: $0 <change-dir>" >&2
  exit 2
fi

CHANGE_DIR="$1"

missing=0
for file in proposal.md design.md tasks.md; do
  if [ ! -f "$CHANGE_DIR/$file" ]; then
    echo "BLOCK | missing $file"
    missing=1
  fi
done

if [ "$missing" -ne 0 ]; then
  exit 1
fi

echo "ALLOW | apply gate satisfied"
