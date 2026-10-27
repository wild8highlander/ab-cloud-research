#!/usr/bin/env bash
# Runs before every pipeline step: sanity of the funnel.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
[ -f "$ROOT/02_data/processed/research_registry.json" ] || { echo "pre_run: registry missing" >&2; exit 1; }
grep -q '"rh_status": *"certified"' "$ROOT/02_data/processed/research_registry.json" \
  || { echo "pre_run: rh_status must be 'certified' (honesty gate)" >&2; exit 1; }
echo "pre_run: honesty gate passed (rh_status=certified)"
