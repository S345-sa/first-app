#!/usr/bin/env bash
# Print every retrieval question in srs-queue.md due today or earlier.
# ISO dates (YYYY-MM-DD) compare correctly as strings.
set -euo pipefail

queue="$(dirname "$0")/../srs-queue.md"
today="$(date +%F)"

found=0
while IFS= read -r line; do
  case "$line" in
    "- due: "*)
      d="${line#- due: }"
      d="${d%% *}"
      if [[ "$d" < "$today" || "$d" == "$today" ]]; then
        echo "$line"
        found=1
      fi
      ;;
  esac
done < "$queue"

if [[ "$found" -eq 0 ]]; then
  echo "No retrieval questions due today ($today)."
fi
