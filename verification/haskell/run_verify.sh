#!/usr/bin/env bash
# Build & run the Haskell verifier (ghc --make, base + array only).
set -e
cd "$(dirname "$0")"
ghc -O2 --make Main.hs -o ab_cloud_verify 2>build.log
./ab_cloud_verify "$@"
