#!/usr/bin/env bash
# RUN_ALL.sh — полный прогон независимой верификации (IVP01–IVP16)
set -u
cd "$(dirname "$0")/.."
echo "=== AB Research Program IVP — $(cat VERSION 2>/dev/null || echo 'dev') ==="
echo "UTC: $(date -u '+%Y-%m-%d %H:%M:%S')"
rc=0
python3 - <<PYEOF
import sys
sys.path.insert(0, ".")
from rpbridge.ivp import run_all

results = run_all()
npass = 0
for r in results:
    mark = "[PASS]" if r["passed"] else "[FAIL]"
    if r["passed"]:
        npass += 1
    print(f"{mark} {r['name']}: {r['detail']}")
total = len(results)
print(f"ИТОГ: {npass}/{total} PASS")
sys.exit(0 if npass == total else 1)
PYEOF
rc=$?
if [ $rc -eq 0 ]; then
  echo "=== IVP: ALL CHECKS PASSED ==="
else
  echo "=== IVP: FAILURES PRESENT (rc=$rc) ==="
fi
exit $rc
