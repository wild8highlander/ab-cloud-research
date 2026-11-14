#!/usr/bin/env bash
# Build & run the canonical Java verifier (CANON_SPEC v3.0).
# Requires JDK 8+ (javac + java). On JDK 11+ the single-file source launcher
# also works without javac:  java ABCloudVerify.java --zeros 50000 --source 500k
# Exit code is the program's: 1 if any frozen self-check anchor failed, 2 on
# load/CLI error.
set -euo pipefail
cd "$(dirname "$0")"
javac -encoding UTF-8 ABCloudVerify.java ABCloudVerifyEn.java ABCloudVerifyRu.java
exec java -Dfile.encoding=UTF-8 ABCloudVerify "$@"
