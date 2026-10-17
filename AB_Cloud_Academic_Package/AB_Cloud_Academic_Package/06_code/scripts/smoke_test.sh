#!/usr/bin/env bash
# smoke: every runner speaks the contract
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
python3 "$DIR/python/run.py" doctor
bash "$DIR/bash/run.sh" doctor
node "$DIR/js/run.js" doctor
echo "smoke: OK (python + bash + js)"
