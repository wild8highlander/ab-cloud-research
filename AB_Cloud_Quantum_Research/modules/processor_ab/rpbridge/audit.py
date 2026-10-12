# -*- coding: utf-8 -*-
"""rpbridge.audit — аудит утверждений (схема V14 материнского пакета).

Каждый claim-файл (verification/claim_audit/claims/claim_vXX.json)
содержит: statement, premises, code, controls, does_not_prove, status.
Аудит проверяет согласованность числовых полей claim-файла с
закоммиченным вердиктом data/v20_verdict.json (консистентность), а
также полноту списка does_not_prove.
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

REQUIRED_KEYS = ('id', 'statement', 'premises', 'code', 'controls',
                 'does_not_prove', 'status')
REQUIRED_NUMERIC = 'numeric_check'


def _verdict():
    with open(os.path.join(ROOT, 'data', 'v20_verdict.json'),
              encoding='utf-8') as f:
        return json.load(f)


def audit_claim(claim):
    """Проверка одного claim: ключи, статус, числовая согласованность.

    numeric_check: список объектов {path, value, tol} — значение claim
    должно совпадать со значением вердикта по пути (относительный
    допуск tol)."""
    v = _verdict()
    problems = []
    for k in REQUIRED_KEYS:
        if k not in claim:
            problems.append(f'missing key: {k}')
    if claim.get('status') not in ('verified', 'committed'):
        problems.append(f"bad status: {claim.get('status')}")
    if not claim.get('does_not_prove'):
        problems.append('does_not_prove list is empty')
    for item in claim.get('numeric_check', []):
        path, val, tol = item['path'], item['value'], item['tol']
        try:
            node = v
            for part in path.split('.'):
                node = node[part]
            ref = float(node)
            if abs(float(val) - ref) > tol * max(1.0, abs(ref)):
                problems.append(f'{path}: claim {val} != verdict {ref}')
        except Exception as e:  # noqa: BLE001
            problems.append(f'{path}: {e}')
    return dict(id=claim.get('id'), ok=not problems,
                problems=problems)


def run():
    """Полный аудит всех claim-файлов пакета."""
    cdir = os.path.join(ROOT, 'verification', 'claim_audit', 'claims')
    results = []
    for fn in sorted(os.listdir(cdir)):
        if fn.endswith('.json'):
            with open(os.path.join(cdir, fn), encoding='utf-8') as f:
                results.append(audit_claim(json.load(f)))
    n = len(results)
    ok = sum(1 for r in results if r['ok'])
    return dict(total=n, passed=ok, results=results,
                consistency='PASS' if ok == n and n > 0 else 'FAIL')
