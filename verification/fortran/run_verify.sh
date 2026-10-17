#!/usr/bin/env bash
# =============================================================================
# AB-Cloud Verification — Fortran compile & run script (canon spec v3.0)
# =============================================================================
# Builds the main bilingual binary plus the two THIN language wrappers
# (CANON_SPEC §10: the *_en / *_ru sources are one-line #define + #include
# wrappers around ab_cloud_verify.f90 — no duplicated math), then runs the
# main binary with the canonical CLI:
#
#   --zeros N --source NAME --objection X --lang L --data-dir D
#
# Extra flags understood by the program itself: --no-selfcheck, --help.
# Exit code is the program's: 1 if any frozen self-check anchor failed (§8).
# =============================================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Defaults (CANON_SPEC §9)
FC="${FC:-gfortran}"
FFLAGS="-cpp -O2 -std=f2008 -Wall"
ZEROS=50000
SOURCE="auto"
OBJECTION="all"
LANGOPT=""          # empty -> the binary auto-detects from $LANG
DATA_DIR="../data"

usage() {
  cat <<'EOF'
Usage: ./run_verify.sh [options]
  --zeros N          number of zeta zeros to load (default 50000; 0 = all)
  --source NAME      auto|50k|50k_full|500k|2M|highT|2M_gz|csv|zeros6 (default auto)
  --objection X      1|2|3|all (default all)
  --lang L           en|ru (default: auto-detect from $LANG)
  --data-dir DIR     path to the data/ directory (default ../data)
  --compiler FC      Fortran compiler (default gfortran)
  --skip-wrappers    build only the main binary
  --help             show this help
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --zeros)     shift; ZEROS="$1" ;;
    --source)    shift; SOURCE="$1" ;;
    --objection) shift; OBJECTION="$1" ;;
    --lang)      shift; LANGOPT="$1" ;;
    --data-dir)  shift; DATA_DIR="$1" ;;
    --compiler)  shift; FC="$1" ;;
    --skip-wrappers) SKIP_WRAPPERS=1 ;;
    --help|-h)   usage; exit 0 ;;
    *) echo "Unknown option: $1" >&2; usage >&2; exit 2 ;;
  esac
  shift
done

echo "=========================================="
echo "  AB-Cloud Fortran Verification"
echo "=========================================="
echo "  Compiler:  $FC $FFLAGS"
echo "  Zeros:     $ZEROS"
echo "  Source:    $SOURCE"
echo "  Objection: $OBJECTION"
echo "  Language:  ${LANGOPT:-auto}"
echo "  Data dir:  $DATA_DIR"
echo "=========================================="

# --- compile (-cpp is required: the sources use #ifdef/#include) -------------
echo ""
echo "Compiling..."
"$FC" $FFLAGS -I "$SCRIPT_DIR" -o ab_cloud_verify ab_cloud_verify.f90

if [[ "${SKIP_WRAPPERS:-0}" != "1" ]]; then
  "$FC" $FFLAGS -I "$SCRIPT_DIR" -o ab_cloud_verify_en ab_cloud_verify_en.f90
  "$FC" $FFLAGS -I "$SCRIPT_DIR" -o ab_cloud_verify_ru ab_cloud_verify_ru.f90
fi

echo "Compilation successful."
echo ""

# --- run ----------------------------------------------------------------------
RUN_ARGS=( --zeros "$ZEROS" --source "$SOURCE" --objection "$OBJECTION" --data-dir "$DATA_DIR" )
if [[ -n "$LANGOPT" ]]; then
  RUN_ARGS+=( --lang "$LANGOPT" )
fi

echo "Running verification..."
echo ""
set +e
./ab_cloud_verify "${RUN_ARGS[@]}"
RC=$?
set -e

echo ""
if [[ $RC -eq 0 ]]; then
  echo "Done (exit 0)."
else
  echo "Done with exit code $RC (nonzero = self-check anchor failure or load error)."
fi
exit $RC
