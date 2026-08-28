#!/bin/bash
# ============================================================================
# run_verify.sh — Compile and run the AB-Cloud Verification Suite
#
# Usage: ./run_verify.sh [OPTIONS]
#   --zeros   N       Number of zeros to load (default: 200000)
#   --source  SRC     Data source: 50k, 500k, 2M, highT, zeros6, auto (default: auto)
#   --objection O     Which objection to verify: 1, 2, 3, or all (default: all)
#   --lang    LANG    Language for bilingual module: en, ru (default: en)
#   --module  MOD     Which module to build: bilingual, en, ru, all (default: bilingual)
#   --data-dir DIR    Path to data directory (default: ../data)
#   --clean          Remove compiled binaries
#   --help           Show this help message
#
# Examples:
#   ./run_verify.sh --zeros 200000 --source 500k --objection all --lang en
#   ./run_verify.sh --module en --zeros 50000 --source 50k
#   ./run_verify.sh --module all --objection 1
#   ./run_verify.sh --clean
#
# Author:  AB-Cloud Verification Team
# License: MIT
# ============================================================================

set -euo pipefail

# --- Color output helpers ---
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'  # No Color

info()  { echo -e "${CYAN}[INFO]${NC} $*"; }
ok()    { echo -e "${GREEN}[OK]${NC} $*"; }
warn()  { echo -e "${YELLOW}[WARN]${NC} $*"; }
err()   { echo -e "${RED}[ERROR]${NC} $*"; }

# --- Defaults ---
ZEROS=200000
SOURCE="auto"
OBJECTION="all"
LANG="en"
MODULE="bilingual"
DATA_DIR="../data"
CLEAN=false

# --- Parse arguments ---
while [[ $# -gt 0 ]]; do
    case "$1" in
        --zeros|-z)
            ZEROS="$2"; shift 2 ;;
        --source|-s)
            SOURCE="$2"; shift 2 ;;
        --objection|-o)
            OBJECTION="$2"; shift 2 ;;
        --lang|-l)
            LANG="$2"; shift 2 ;;
        --module|-m)
            MODULE="$2"; shift 2 ;;
        --data-dir|-d)
            DATA_DIR="$2"; shift 2 ;;
        --clean)
            CLEAN=true; shift ;;
        --help|-h)
            head -25 "$0" | tail -20
            exit 0 ;;
        *)
            err "Unknown option: $1"
            echo "Use --help for usage information."
            exit 1 ;;
    esac
done

# --- Clean mode ---
if [[ "$CLEAN" == true ]]; then
    info "Removing compiled binaries..."
    rm -f ab_cloud_verify ab_cloud_verify_en ab_cloud_verify_ru
    ok "Clean complete."
    exit 0
fi

# --- Detect C++ compiler ---
CXX="${CXX:-}"
if [[ -z "$CXX" ]]; then
    if command -v g++ &>/dev/null; then
        CXX="g++"
    elif command -v clang++ &>/dev/null; then
        CXX="clang++"
    else
        err "No C++17 compiler found (g++ or clang++). Please install one."
        exit 1
    fi
fi

CXXFLAGS="-std=c++17 -O2 -Wall -Wextra"

info "Compiler: $CXX $CXXFLAGS"
info "Configuration:"
info "  Zeros:     $ZEROS"
info "  Source:    $SOURCE"
info "  Objection: $OBJECTION"
info "  Language:  $LANG"
info "  Module:    $MODULE"
info "  Data dir:  $DATA_DIR"
echo ""

# --- Verify data directory ---
if [[ ! -d "$DATA_DIR" ]]; then
    warn "Data directory '$DATA_DIR' not found."
    warn "Zero files will fail to load. Ensure data files are in place."
fi

# --- Build function ---
build_binary() {
    local src="$1"
    local out="$2"
    info "Compiling $src -> $out ..."
    if $CXX $CXXFLAGS -o "$out" "$src" -lm 2>&1; then
        ok "Compiled $out successfully."
    else
        err "Compilation of $src failed!"
        exit 1
    fi
}

# --- Run function ---
run_binary() {
    local bin="$1"
    shift
    info "Running $bin $*"
    echo "=========================================================================="
    if ./"$bin" "$@"; then
        echo "=========================================================================="
        ok "$bin completed successfully (exit code 0)."
    else
        local rc=$?
        echo "=========================================================================="
        warn "$bin exited with code $rc."
    fi
}

# --- Build and run based on module selection ---
case "$MODULE" in
    bilingual|all)
        build_binary "ab_cloud_verify.cpp" "ab_cloud_verify"
        run_binary "ab_cloud_verify" \
            --zeros "$ZEROS" \
            --source "$SOURCE" \
            --objection "$OBJECTION" \
            --lang "$LANG" \
            --data-dir "$DATA_DIR"
        ;;&  # Fall through for 'all'

    en|all)
        if [[ "$MODULE" == "all" ]] || [[ "$MODULE" == "en" ]]; then
            build_binary "ab_cloud_verify_en.cpp" "ab_cloud_verify_en"
            run_binary "ab_cloud_verify_en" \
                --zeros "$ZEROS" \
                --source "$SOURCE" \
                --objection "$OBJECTION" \
                --data-dir "$DATA_DIR"
        fi
        ;;&  # Fall through for 'all'

    ru|all)
        if [[ "$MODULE" == "all" ]] || [[ "$MODULE" == "ru" ]]; then
            build_binary "ab_cloud_verify_ru.cpp" "ab_cloud_verify_ru"
            run_binary "ab_cloud_verify_ru" \
                --zeros "$ZEROS" \
                --source "$SOURCE" \
                --objection "$OBJECTION" \
                --data-dir "$DATA_DIR"
        fi
        ;;

    *)
        err "Unknown module: '$MODULE'. Use: bilingual, en, ru, or all."
        exit 1
        ;;
esac

echo ""
info "All requested verifications complete."
