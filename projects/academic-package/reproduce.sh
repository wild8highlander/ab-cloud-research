#!/usr/bin/env bash
# =====================================================================
# AB-Cloud unified academic package - one-button reproduction script.
# Runs: environment doctor -> config validation -> package integrity tests
#       -> consolidated metrics re-computation -> checksum verification.
# Everything writes inside ./out (or AB_CLOUD_OUT). Nothing phones home.
# =====================================================================
set -euo pipefail
cd "$(dirname "$0")"

PY="${PYTHON:-python3}"
OUT="${AB_CLOUD_OUT:-./out}"
mkdir -p "$OUT"

banner() { printf '\n\033[1;36m== %s ==\033[0m\n' "$1"; }

banner "1/5 doctor"
$PY 06_code/python/run.py doctor

banner "2/5 validate config"
$PY 06_code/python/run.py validate

banner "3/5 package integrity tests"
$PY -m pytest 09_tests/python -q

banner "4/5 consolidated metrics"
$PY 06_code/python/run.py analyze --out="$OUT"

banner "5/5 data checksums"
$PY 06_code/scripts/update_checksums.py --verify-only

printf '\n\033[1;32mReproduction complete.\033[0m Artefacts in %s\n' "$OUT"
printf '\033[1;33mNote\033[0m: research campaigns themselves live in the three source laboratories\n'
printf '(AB_Cloud_Quantum_Research, dirac-lab, Hilbert_Polya) - see their READMEs.\n'
