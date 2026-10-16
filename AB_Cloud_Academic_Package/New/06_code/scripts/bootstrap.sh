#!/usr/bin/env bash
# install everything needed to run the unified package
set -euo pipefail
python3 -m pip install -r "$(dirname "$0")/../requirements.txt"
echo "bootstrap: python deps installed; julia/rust/go are optional runners"
