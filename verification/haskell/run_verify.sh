#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

# Try runhaskell first, fall back to ghc compile + run
if command -v runhaskell &>/dev/null; then
    exec runhaskell Main.hs "$@"
elif command -v ghc &>/dev/null; then
    ghc -O2 -o ab-cloud-verify Main.hs ZerosLoader.hs VerifyEN.hs VerifyRU.hs
    exec ./ab-cloud-verify "$@"
else
    echo "Error: neither runhaskell nor ghc found in PATH" >&2
    exit 1
fi
