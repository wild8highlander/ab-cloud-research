#!/usr/bin/env bash
# RUN_ALL.sh — полный прогон протокола независимой верификации IVP01–IVP10.
set -u
cd "$(dirname "$0")/.."

echo "=== Hilbert Polya Bridge · Independent Verification Protocol ==="
echo "version: $(cat VERSION) · $(date -u '+%Y-%m-%dT%H:%M:%SZ')"
echo

# 0. мультиязычный C-двойник (если есть cc) — свежий управляющий блок
if command -v cc >/dev/null 2>&1 || command -v gcc >/dev/null 2>&1; then
    CC_BIN="$(command -v cc || command -v gcc)"
    "$CC_BIN" -O2 multilang/c/verify_core.c -lm -o /tmp/hpb_c && \
        /tmp/hpb_c multilang/c/verify_control.txt
else
    echo "[warn] cc недоступен — IVP10 использует закоммиченный блок"
fi
echo

# 1..10 — проверки протокола
python3 - <<'EOF'
import sys
sys.path.insert(0, ".")
from hpbridge.validate import run_all

results = run_all()
npass = 0
for r in results:
    mark = "PASS" if r["passed"] else "FAIL"
    npass += bool(r["passed"])
    print(f"[{mark}] {r['name']}: {r['detail']}")
print(f"\nИТОГ: {npass}/{len(results)} PASS")
sys.exit(0 if npass == len(results) else 1)
EOF
rc=$?
echo
if [ $rc -eq 0 ]; then
    echo "=== IVP: ALL CHECKS PASSED ==="
else
    echo "=== IVP: FAILURES PRESENT (rc=$rc) ==="
fi
exit $rc
