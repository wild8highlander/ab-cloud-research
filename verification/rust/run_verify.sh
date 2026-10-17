#!/usr/bin/env bash
# Build & run the canonical Rust verifier (CANON_SPEC v3.0).
set -euo pipefail
cd "$(dirname "$0")"
cargo build --release
exec ./target/release/ab-cloud-verify "$@"
