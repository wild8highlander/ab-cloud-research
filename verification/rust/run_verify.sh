#!/usr/bin/env bash
# =============================================================================
# AB-CLOUD Verification — Rust Cargo Run Wrapper
# =============================================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Defaults
ZEROS=10000
SOURCE="auto"
OBJECTION="all"
LANG="en"
RELEASE=""

usage() {
  echo "Usage: $0 [options]"
  echo "  --zeros N        Number of zeta zeros to use (default: 10000)"
  echo "  --source NAME    Data file name in ../data/ (default: auto)"
  echo "  --objection 1|2|3|all  Which objection to run (default: all)"
  echo "  --lang en|ru     Language output (default: en)"
  echo "  --release        Build in release mode (optimized)"
  echo "  --help           Show this help"
  exit 0
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --zeros)     shift; ZEROS="$1" ;;
    --source)    shift; SOURCE="$1" ;;
    --objection) shift; OBJECTION="$1" ;;
    --lang)      shift; LANG="$1" ;;
    --release)   RELEASE="--release" ;;
    --help|-h)   usage ;;
    *) echo "Unknown option: $1"; usage ;;
  esac
  shift
done

echo "=========================================="
echo "  AB-CLOUD Rust Verification"
echo "=========================================="
echo "  Zeros:     $ZEROS"
echo "  Source:    $SOURCE"
echo "  Objection: $OBJECTION"
echo "  Language:  $LANG"
echo "  Mode:      ${RELEASE:-debug}"
echo "=========================================="

# Build
echo ""
echo "Building..."
cargo build $RELEASE --quiet 2>/dev/null || cargo build $RELEASE

echo "Build successful."
echo ""

# Run
echo "Running verification..."
echo ""
cargo run $RELEASE -- --zeros "$ZEROS" --source "$SOURCE" --objection "$OBJECTION" --lang "$LANG"

echo ""
echo "Done."
