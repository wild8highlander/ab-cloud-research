#!/usr/bin/env bash
# Независимая верификация ABQP 0.1.0 (из корня пакета)
set -e
cd "$(dirname "$0")/.."
echo "== ABQP 0.1.0 independent verification =="
python3 - <<'PY'
import sys
sys.path.insert(0, '.')
from rpbridge import ivp
r = ivp.run_all()
for p in r['protocols']:
    print(('PASS' if p['passed'] else 'FAIL'), '-', p['name'])
print(f"SUMMARY: {r['summary']['passed']}/{r['summary']['n']} PASS")
sys.exit(0 if r['summary']['passed'] == r['summary']['n'] else 1)
PY
echo "== pytest =="
python3 -m pytest tests/ -q
echo "== claim audit =="
python3 - <<'PY'
import sys
sys.path.insert(0, '.')
from rpbridge import audit
r = audit.run()
print(f"CLAIM AUDIT: {r['consistency']} ({r['passed']}/{r['total']})")
sys.exit(0 if r['consistency'] == 'PASS' else 1)
PY
echo "== ALL INDEPENDENT VERIFICATION PASSED =="
