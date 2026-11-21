#!/bin/bash
# Build & run the canonical C++ verifier (CANON_SPEC v3.0).
#   ./run_verify.sh --objection all --lang en      # default: 50000 zeros, selfcheck on
#   ./run_verify.sh --module en|ru|all             # thin language-pinned binaries
set -e
cd "$(dirname "$0")"
MOD="bilingual"
ARGS=()
while [[ $# -gt 0 ]]; do
  if [[ "$1" == "--module" ]]; then MOD="$2"; shift 2;
  elif [[ "$1" == "--clean" ]]; then rm -f ab_cloud_verify ab_cloud_verify_en ab_cloud_verify_ru; exit 0;
  else ARGS+=("$1"); shift; fi
done
g++ -O2 -std=c++17 -Wall -o ab_cloud_verify ab_cloud_verify.cpp
[[ "$MOD" == "en" || "$MOD" == "all" ]] && g++ -O2 -std=c++17 -o ab_cloud_verify_en ab_cloud_verify_en.cpp
[[ "$MOD" == "ru" || "$MOD" == "all" ]] && g++ -O2 -std=c++17 -o ab_cloud_verify_ru ab_cloud_verify_ru.cpp
case "$MOD" in
  en) exec ./ab_cloud_verify_en "${ARGS[@]}" ;;
  ru) exec ./ab_cloud_verify_ru "${ARGS[@]}" ;;
  *)  exec ./ab_cloud_verify "${ARGS[@]}" ;;
esac
