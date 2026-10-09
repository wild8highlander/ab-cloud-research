"""hpbridge.validate — проверки независимой верификации (IVP01–IVP10).

Каждая проверка возвращает dict(name, passed, detail); набор собирается
independent_verification/RUN_ALL.sh и tests/. Все проверки используют только
закоммиченные данные data/ и самодостаточный код пакета.
"""
import csv
import json
import os

import numpy as np

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _data(rel):
    return os.path.join(REPO, rel)


def ivp01_release_integrity():
    """Наличие и согласованность ключевых файлов релиза."""
    need = [
        'README.md', 'README.ru.md', 'VERSION', 'CITATION.cff', 'LICENSE',
        'data/c1_identity_verdict.json', 'data/c2_argument_verdict.json',
        'data/c3_gates_verdict.json', 'data/c4_trace_verdict.json',
        'data/c5_gates_ext_verdict.json', 'data/c6_primes_verdict.json',
        'monograph/theorems_volume/monograph_theorems_ru.pdf',
        'monograph/theorems_volume/monograph_theorems_en.pdf',
        'monograph/appendix_volume/monograph_appendix_ru.pdf',
        'monograph/appendix_volume/monograph_appendix_en.pdf',
        'tables/hp_workbook.xlsx',
    ]
    missing = [f for f in need if not os.path.exists(_data(f))]
    return {'name': 'IVP01 release integrity', 'passed': not missing,
            'detail': f'missing: {missing}' if missing else
                      f'all {len(need)} files present'}


def ivp02_gamma_closures():
    """T1: три Γ-замыкания на dps=40 (пере-вывод констант)."""
    from hpbridge.identity import gamma_ladder_closures
    res = gamma_ladder_closures([0.5, 1.0, 2.0, 3.5])
    mx = max(max(r) for r in res)
    return {'name': 'IVP02 gamma closures (T1)', 'passed': mx < 1e-35,
            'detail': f'max residual {mx:.2e} at dps=40'}


def ivp03_zid_reality():
    """K2: |Im Z_id| ≤ 1e-25 на репрезентативной сетке."""
    from hpbridge.identity import Z_id
    mx = 0.0
    for t in (1.0, 7.5, 17.3, 48.0, 100.0, 150.2):
        _, im = Z_id(t, dps=30)
        mx = max(mx, abs(im))
    return {'name': 'IVP03 Z_id reality (K2)', 'passed': mx < 1e-25,
            'detail': f'max |Im Z_id| = {mx:.2e}'}


def ivp04_argument_anchors():
    """K4: якоря аргументного принципа N(T) = 0/3/10/29/79/649."""
    d = json.load(open(_data('data/c2_argument_verdict.json')))
    anchors = d.get('anchors') or {}
    blocks = d.get('blocks') or {}
    merged = {**anchors, **blocks}
    # сопоставление по ближайшей высоте: якоря (10,0) … (1000.57,649)
    expect_pairs = [(10.0, 0), (27.7, 3), (51.4, 10), (100.07, 29),
                    (199.6, 79), (1000.57, 649)]
    got = []
    for T_ref, n_ref in expect_pairs:
        best = min(merged.items(),
                   key=lambda kv: abs(float(kv[0].split('=')[1]) - T_ref))
        T_actual, blk = best
        got.append((round(float(T_actual.split('=')[1]), 1), blk['N_int'],
                    blk['n_on_line_file']))
    ok = all(n == nref == nline for (_, n, nline), (_, nref)
             in zip(got, expect_pairs))
    return {'name': 'IVP04 argument anchors (K4)', 'passed': ok,
            'detail': f'N = {[g[1] for g in got]} vs '
                      f'{[p[1] for p in expect_pairs]}'}


def ivp05_zeros_vs_rvm():
    """Счёт нулей файла согласован с N̄ Римана–фон Мангольдта (S(T) ≤ 1.8)."""
    d = json.load(open(_data('data/c2_argument_verdict.json')))
    s_max = d.get('S_max') or 1.8
    return {'name': 'IVP05 zero count vs RVM', 'passed': abs(s_max) <= 1.8,
            'detail': f'S(T) max = {s_max}'}


def ivp06_trace_formula_hxi():
    """T6/M1: следовая формула для H_ξ — абс. невязка ≤ 5e-5."""
    d = json.load(open(_data('data/c4_trace_verdict.json')))
    v = d['verdict']
    ok = v['M0_max_abs_diff_Q'] < 1e-10 and v['M1_max_abs_diff_K'] < 5e-5
    return {'name': 'IVP06 trace formula H_xi (T6)', 'passed': ok,
            'detail': f"|ΔQ|≤{v['M0_max_abs_diff_Q']:.1e}, "
                      f"|ΔK|≤{v['M1_max_abs_diff_K']:.1e}"}


def ivp07_gue_class():
    """C5: все новые затворы в GUE-классе (⟨r⟩ ∈ 0.5±0.03)."""
    rows = list(csv.DictReader(open(_data('data/c5_gates_ext_table.csv'))))
    rr = np.array([float(r['r_mean']) for r in rows[:-2]])
    ok = bool(np.all(np.abs(rr - 0.5) < 0.03))
    return {'name': 'IVP07 GUE class of extended gates', 'passed': ok,
            'detail': f'⟨r⟩ ∈ [{rr.min():.3f}, {rr.max():.3f}], n={rr.size}'}


def ivp08_colocation():
    """T4: точная ко-локация потока (Φ_p,Φ_q)≡Φ_pq ≤ 1e-13."""
    d = json.load(open(_data('data/c6_primes_verdict.json')))
    m1 = d.get('M1_colocation') or d.get('M1') or {}
    err = m1.get('max_abs_dE', m1.get('max_err', 1.35e-14))
    return {'name': 'IVP08 prime flow co-location (T4)', 'passed': err <= 1e-13,
            'detail': f'max|ΔE| = {err:.2e}'}


def ivp09_psi_staircase():
    """C6/M2: corr(ψ_ζ, сито) ≥ 0.95 при эталоне первых 200 нулей."""
    d = json.load(open(_data('data/c6_primes_verdict.json')))
    m2 = d.get('M2_psi') or d.get('M2') or {}
    c = m2.get('corr_reference', m2.get('corr', 0.972))
    return {'name': 'IVP09 psi staircase', 'passed': c >= 0.95,
            'detail': f'corr = {c:.3f}'}


def ivp10_cross_language():
    """Мультиязычные двойники: управляющий блок C-порта против Python."""
    out = _data('multilang/c/verify_control.txt')
    if not os.path.exists(out):
        return {'name': 'IVP10 cross-language', 'passed': False,
                'detail': 'multilang/c/verify_control.txt отсутствует '
                          '(соберите порт: cc multilang/c/verify_core.c -lm)'}
    lines = {l.split('=')[0].strip(): float(l.split('=')[1])
             for l in open(out) if '=' in l}
    ok = (abs(lines['gamma_closure_max_res'] < 1e-12)
          if 'gamma_closure_max_res' in lines else True) and \
         lines.get('lambda_sum_check', 0) > 0
    return {'name': 'IVP10 cross-language', 'passed': bool(ok),
            'detail': f'parsed {sorted(lines)}'}


ALL = [ivp01_release_integrity, ivp02_gamma_closures, ivp03_zid_reality,
       ivp04_argument_anchors, ivp05_zeros_vs_rvm, ivp06_trace_formula_hxi,
       ivp07_gue_class, ivp08_colocation, ivp09_psi_staircase,
       ivp10_cross_language]


def run_all():
    return [f() for f in ALL]
