#!/usr/bin/env bash
# The unified entry point: ./06_code/cli/run.sh [--lang=..] [--theme=..] <command>
# Dispatches to the Python reference implementation by default; set
# AB_CLOUD_IMPL=python|julia|rust|go|js|bash to pick another contract runner.
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CODE="$(cd "$DIR/.." && pwd)"
IMPL="${AB_CLOUD_IMPL:-python}"
case "$IMPL" in
  python) exec python3 "$CODE/python/run.py" "$@" ;;
  julia)  exec julia "$CODE/julia/run.jl" "$@" ;;
  rust)   exec "$CODE/rust/target/release/abcloud-run" "$@" ;;
  go)     exec "$CODE/go/run" "$@" ;;
  js)     exec node "$CODE/js/run.js" "$@" ;;
  bash)   exec bash "$CODE/bash/run.sh" "$@" ;;
  *) echo "unknown impl: $IMPL (python|julia|rust|go|js|bash)"; exit 2 ;;
esac
