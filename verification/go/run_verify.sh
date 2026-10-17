#!/usr/bin/env bash
# Build & run the canonical Go verifier (CANON_SPEC v3.0).
# NOTE: paths are resolved relative to the BINARY location — build into this
# directory (go build -o ab_cloud_verify .) rather than `go run` (whose exe
# lands in a temp dir and cannot find ../data).
set -euo pipefail
cd "$(dirname "$0")"
go build -o ab_cloud_verify .
exec ./ab_cloud_verify "$@"
