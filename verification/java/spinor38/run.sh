#!/usr/bin/env bash
# Build and run the Java port of Test 38 (spinor38).
# Optional first argument: path to the repository root.
set -e
cd "$(dirname "$0")"
javac Spinor38.java && java Spinor38 "$@"
