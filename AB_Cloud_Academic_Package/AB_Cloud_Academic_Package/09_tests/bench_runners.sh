#!/usr/bin/env bash
# quick benchmark of the contract runners
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
for impl in python bash js; do
  case "$impl" in
    python) cmd=(python3 "$DIR/python/run.py" --quiet analyze);;
    bash)   cmd=(bash "$DIR/bash/run.sh" analyze);;
    js)    cmd=(node "$DIR/js/run.js" analyze);;
  esac
  s=$(date +%s.%N)
  "${cmd[@]}" >/dev/null
  e=$(date +%s.%N)
  printf "  %-8s %.2fs\n" "$impl" "$(echo "$e - $s" | bc)"
done
