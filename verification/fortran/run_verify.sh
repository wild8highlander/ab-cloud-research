#!/usr/bin/env bash
# =============================================================================
# AB-CLOUD Verification — Fortran Compile & Run Script
# =============================================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Defaults
FC="${FC:-gfortran}"
FFLAGS="-O2 -std=f2018 -fcheck=all -Wall -Wextra"
ZEROS=10000
SOURCE="auto"
OBJECTION="all"
LANG="en"
SRC="ab_cloud_verify.f90"

usage() {
  echo "Usage: $0 [options]"
  echo "  --zeros N        Number of zeta zeros to use (default: 10000)"
  echo "  --source NAME    Data file name in ../data/ (default: auto)"
  echo "  --objection 1|2|3|all  Which objection to run (default: all)"
  echo "  --lang en|ru     Language output (default: en)"
  echo "  --compiler FC    Fortran compiler (default: gfortran)"
  echo "  --help           Show this help"
  exit 0
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --zeros)    shift; ZEROS="$1" ;;
    --source)   shift; SOURCE="$1" ;;
    --objection) shift; OBJECTION="$1" ;;
    --lang)
      shift; LANG="$1"
      if [[ "$LANG" == "en" ]]; then
        SRC="ab_cloud_verify_en.f90"
      elif [[ "$LANG" == "ru" ]]; then
        SRC="ab_cloud_verify_ru.f90"
      else
        SRC="ab_cloud_verify.f90"
      fi
      ;;
    --compiler) shift; FC="$1" ;;
    --help|-h)  usage ;;
    *) echo "Unknown option: $1"; usage ;;
  esac
  shift
done

echo "=========================================="
echo "  AB-CLOUD Fortran Verification"
echo "=========================================="
echo "  Compiler:  $FC"
echo "  Source:    $SRC"
echo "  Zeros:     $ZEROS"
echo "  Source:    $SOURCE"
echo "  Objection: $OBJECTION"
echo "  Language:  $LANG"
echo "=========================================="

# Compile
echo ""
echo "Compiling..."
"$FC" $FFLAGS -o ab_cloud_verify "$SRC"

if [[ ! -f ab_cloud_verify ]]; then
  echo "ERROR: Compilation failed!"
  exit 1
fi

echo "Compilation successful."
echo ""

# Run
echo "Running verification..."
echo ""
./ab_cloud_verify --zeros "$ZEROS" --source "$SOURCE" --objection "$OBJECTION" --lang "$LANG"

echo ""
echo "Done."
