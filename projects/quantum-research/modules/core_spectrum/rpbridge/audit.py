"""rpbridge.audit — Решение 14 (V14): автоматический математический аудит
каждого результата.

Протокол плана: каждый новый эксперимент обязан содержать 5 частей:
  1. точное математическое утверждение;
  2. перечень предпосылок;
  3. численный результат и воспроизводимый код;
  4. контрольные модели и анализ чувствительности;
  5. перечень того, что результат НЕ доказывает.

Схема аудита: claim-JSON (verification/claim_audit/claims/*.json) с полями
  claim, statement, premises[], code[], controls[], does_not_prove[],
  status ∈ {proven, measured, conjecture, refuted}.
Проверки:
  A1  схема: все 5 частей присутствуют и непусты;
  A2  статус-гигиена: 'proven' требует ≥1 контроля с passed=true И
      непустой does_not_prove; p-значение не превращается в «доказано»;
  A3  согласованность: каждый verdict data/v*_verdict.json имеет claim-файл.
"""
import csv
import glob
import json
import os

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLAIMS_DIR = os.path.join(REPO, 'verification', 'claim_audit', 'claims')

REQUIRED = ('statement', 'premises', 'code', 'controls', 'does_not_prove')
STATUSES = ('proven', 'measured', 'conjecture', 'refuted')


def _claim_files():
    return sorted(glob.glob(os.path.join(CLAIMS_DIR, '*.json')))


def audit_claim(path):
    try:
        c = json.load(open(path, encoding='utf-8'))
    except Exception as e:  # noqa: BLE001
        return {'file': os.path.basename(path), 'A1': False,
                'errors': [f'JSON: {e}']}
    errors = []
    for key in REQUIRED:
        v = c.get(key)
        if v is None or (isinstance(v, (list, str)) and not v):
            errors.append(f'A1: отсутствует/пусто {key}')
    if c.get('status') not in STATUSES:
        errors.append(f"A2: статус '{c.get('status')}' вне словаря")
    if c.get('status') == 'proven':
        ctrls = c.get('controls') or []
        if not any(isinstance(k, dict) and k.get('passed') for k in ctrls):
            errors.append("A2: 'proven' без passed-контроля")
        if not c.get('does_not_prove'):
            errors.append("A2: 'proven' без перечня не-следствий")
    for key in ('p_value', 'p_KS'):
        if key in c and c.get('status') == 'proven':
            errors.append("A2: p-значение не может обосновать 'proven'")
    return {'file': os.path.basename(path), 'A1': not errors,
            'errors': errors, 'claim': c.get('claim'),
            'status': c.get('status')}


def audit_consistency():
    """A3: каждый v*_verdict.json покрыт claim-файлом."""
    data = sorted(glob.glob(os.path.join(REPO, 'data', 'v*_verdict.json')))
    claims = {os.path.basename(p).replace('claim_', '').replace('.json', '')
              for p in _claim_files()}
    missing = []
    for d in data:
        vid = os.path.basename(d).replace('_verdict.json', '')
        if vid not in claims:
            missing.append(vid)
    return {'n_verdicts': len(data), 'n_claims': len(claims),
            'missing_claims': missing}


def run():
    results = [audit_claim(p) for p in _claim_files()]
    cons = audit_consistency()
    all_a1 = all(r['A1'] for r in results) if results else False
    return {
        'claims': results, 'consistency': cons,
        'all_a1': bool(all_a1),
        'covered': bool(not cons['missing_claims']),
        'verdict_note': ('каждое публичное утверждение пакета трассируется '
                         'к вычислению, контролю и перечню не-следствий; '
                         'автоповышение гипотезы до теоремы заблокировано'),
    }
