#!/usr/bin/env bash
# build the distributable ZIP of the package
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
OUT="${1:-$ROOT/../AB_Cloud_Academic_Package.zip}"
cd "$ROOT/.."
python3 "$ROOT/06_code/scripts/update_checksums.py" >/dev/null
zip -qr "$OUT" AB_Cloud_Academic_Package -x "*/node_modules/*" "*/rust/target/*" "*/__pycache__/*" "*/.pytest_cache/*"
echo "release: $OUT ($(du -h "$OUT" | cut -f1))"
