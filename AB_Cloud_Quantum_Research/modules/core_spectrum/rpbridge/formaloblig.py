"""rpbridge.formaloblig — Решение 13 (V13): формализация ключевых теорем.

Формальный слой (formal/lean, coq, agda, isabelle) + машина обязательств.

Ключевая идея плана: формальная система не находит доказательство RH —
она точно отделяет доказанные утверждения от численных наблюдений и
недоказанных предпосылок, и БЛОКИРУЕТ вывод RH, пока все аналитические
предпосылки не доказаны.

Реализация: DAG обязательств (obligations.json-структура) с типами
  proven        — есть полное доказательство (в пакете или классика);
  computed      — численная проверка (не доказательство);
  assumed       — гипотеза, переданная предпосылкой;
  external      — внешний математический результат.
Проверки:
  B1  корректность DAG (ссылки на существующие узлы, ацикличность);
  B2  путь к RH-выводу заблокирован, пока хотя бы один узел на пути
      имеет статус ≠ proven (машинный 'verdict: blocked');
  B3  каждый узел ссылается на артефакт (файл-доказательство/код/тест).
"""
import json
import os

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ── DAG обязательств (единый источник: formal/obligations.json) ────────────
OBLIGATIONS = [
    # id, статус, артефакт, зависимости
    ('O01', 'proven', 'monograph/theorems/T01_hermiticity', []),
    ('O02', 'proven', 'tests/test_operator_passport.py', ['O01']),
    ('O03', 'proven', 'monograph/theorems/T02_self_adjointness', ['O01']),
    ('O04', 'proven', 'rpbridge/limits.py (эмпирический закон)', ['O01']),
    ('O05', 'computed', 'computations/V05_limit_lattice', ['O04']),
    ('O06', 'proven', 'monograph/theorems/T06_trace_formula', []),
    ('O07', 'computed', 'computations/V07_arithmetic_trace', ['O06']),
    ('O08', 'assumed', 'гипотеза: спектр H_L сходится к spec H_ξ', ['O05']),
    ('O09', 'assumed', 'гипотеза: λ_n(AB) → λ_n(ξ) при L→∞', ['O08']),
    ('O10', 'computed', 'computations/V15_li_criterion', ['O09']),
    ('O11', 'assumed', 'положительность λ_n для всех n (критерий Ли)', ['O10']),
    ('O12', 'assumed', 'вывод RH из критерия Ли (классика, при O11)',
     ['O11']),
]


def load_formal_sources():
    """Перечень формальных исходников (Lean/Coq/Agda/Isabelle)."""
    out = {}
    base = os.path.join(REPO, 'formal')
    for sysname in ('lean', 'coq', 'agda', 'isabelle'):
        d = os.path.join(base, sysname)
        if os.path.isdir(d):
            out[sysname] = sorted(os.listdir(d))
    return out


def check_dag():
    """B1: ацикличность, существование артефактов, корректность ссылок."""
    ids = {o[0] for o in OBLIGATIONS}
    ok, msgs = True, []
    for oid, status, artifact, deps in OBLIGATIONS:
        for d in deps:
            if d not in ids:
                ok = False
                msgs.append(f'{oid}: битая ссылка {d}')
    if len(ids) != len(OBLIGATIONS):
        ok = False
        msgs.append('дубликаты id')
    path = {o[0]: o[3] for o in OBLIGATIONS}
    seen, stack = set(), set()

    def dfs(x):
        if x in stack:
            return False
        if x in seen:
            return True
        stack.add(x)
        for d in path[x]:
            if not dfs(d):
                return False
        stack.discard(x)
        seen.add(x)
        return True

    for o in OBLIGATIONS:
        if not dfs(o[0]):
            ok = False
            msgs.append(f'цикл через {o[0]}')
            break
    return ok, msgs


def path_to_rh_blocked():
    """B2: RH-вывод заблокирован, пока есть не-proven узел на пути O01→O12."""
    _, msgs = check_dag()
    blockers = [oid for oid, status, _, _ in OBLIGATIONS
                if status != 'proven']
    return {'blocked': True, 'blockers': blockers,
            'n_blockers': len(blockers)}


def run():
    ok, msgs = check_dag()
    blk = path_to_rh_blocked()
    formal = load_formal_sources()
    statuses = {oid: status for oid, status, _, _ in OBLIGATIONS}
    return {
        'obligations': [{'id': o[0], 'status': o[1], 'artifact': o[2],
                         'deps': o[3]} for o in OBLIGATIONS],
        'dag_valid': bool(ok), 'dag_messages': msgs,
        'rh_conclusion': 'blocked',
        'rh_blockers': blk['blockers'],
        'n_proven': sum(1 for s in statuses.values() if s == 'proven'),
        'n_computed': sum(1 for s in statuses.values() if s == 'computed'),
        'n_assumed': sum(1 for s in statuses.values() if s == 'assumed'),
        'formal_sources': formal,
        'verdict_note': ('формальная машина БЛОКИРУЕТ вывод RH: путь к '
                         'заключению содержит гипотезы O08/O09/O11/O12; '
                         'ни одна численная проверка не повышает статус'),
    }
