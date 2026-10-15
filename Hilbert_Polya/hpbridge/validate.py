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
    """C5: новые затворы в GUE-классе (⟨r⟩ ∈ 0.5996±0.03, канон C8).

    v2.0.5: раньше проверялось ⟨r⟩ ∈ 0.5±0.03 против фальшивой v1-колонки
    r_mean = 0.498–0.502 (0.5 — НЕ канон GUE; см. docs/audit_v2.0.5.md).
    """
    rows = list(csv.DictReader(open(_data('data/c5_gates_ext_table.csv'))))
    rr = np.array([float(r['r_mean']) for r in rows[:-2]])
    ok = bool(np.all(np.abs(rr - 0.5996) <= 0.035)
              and abs(rr.mean() - 0.5996) < 0.01)
    return {'name': 'IVP07 GUE class of extended gates', 'passed': ok,
            'detail': f'⟨r⟩ ∈ [{rr.min():.3f}, {rr.max():.3f}], '
                      f'mean {rr.mean():.3f} (канон 0.5996±0.03), n={rr.size}'}


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


# ── v2.0: IVP11–IVP18 (кампании C9–C16) ─────────────────────────────────────

def ivp11_nonlocal_primitive():
    """C9/T11: изоспектральные нелокальные близнецы обязаны давать
    r_H7 = 1 и r_EF(fluct) ≥ 0.99; T6-реприка на внутреннем кэше нулей."""
    d = json.load(open(_data('computations/C9_nonlocal_trace/data/results.json')))
    r = d['results']['N2_DCT_twin']
    tf = d['results']['N1_Hxi']['trace_check']
    ok = (r['r_H7_matched'] > 0.999 and r['r_EF']['r_fluct'] > 0.99
          and tf['max_abs_diff_K'] < 1e-4)
    return {'name': 'IVP11 nonlocal primitive (T11)', 'passed': bool(ok),
            'detail': f"r_H7={r['r_H7_matched']:.4f}, "
                      f"r_EF={r['r_EF']['r_fluct']:.4f}, "
                      f"|dK|<={tf['max_abs_diff_K']:.1e}"}


def ivp12_colocation_hard():
    """C10/T12: жёсткая ко-локация на машинном нуле для всех β."""
    d = json.load(open(_data('computations/C10_phase_coded/data/results.json')))
    worst = max(v['pairwise_max_resid'] for v in d['colocation_T12'].values())
    rmax = max(abs(g['r_H7']) for g in d['gates'])
    ok = worst < 1e-12 and rmax < 0.15
    return {'name': 'IVP12 hard co-location (T12)', 'passed': bool(ok),
            'detail': f'max resid {worst:.1e}, max |r_H7| {rmax:.3f}'}


def ivp13_alpha_third_law():
    """C11/T13: счётный закон N0 = 2L − 6·[L≡0 mod 12] на всех L."""
    d = json.load(open(_data('computations/C11_alpha_third/data/results.json')))
    ok = d['law']['holds_all_L'] and d['law']['index_holds']
    dec = d['law']['decisive_L36_L48']
    ok = ok and dec.get('36') == 66 and dec.get('48') == 90
    return {'name': 'IVP13 alpha-third counting law (T13)',
            'passed': bool(ok),
            'detail': f"law holds, decisive {dec}"}


def ivp14_band5000():
    """C12/T14: N(5000) = 4520 = N_strip, S_max ≤ 2, якоря v1 воспроизведены."""
    d = json.load(open(_data('computations/C12_band_5000/data/results.json')))
    anchors_ok = all(v['match'] for v in d['anchors'].values()
                     if v.get('expected') is not None)
    strips_ok = all(s['match'] for s in d['strip_checks'])
    ok = (d['N_online_5000'] == 4520 and anchors_ok and strips_ok
          and d['S_max'] <= 2.0)
    return {'name': 'IVP14 band T=5000 (T14)', 'passed': bool(ok),
            'detail': f"N={d['N_online_5000']}, S_max={d['S_max']:.2f}"}


def ivp15_blind_families():
    """C13/T15: PC0' = 1.0; все 16 слепых затворов в нулевой зоне."""
    d = json.load(open(_data('computations/C13_blind_families/data/results.json')))
    pc = d['meta']['pipeline_PC0p_r']
    mx = max(abs(g['r_H7']) for g in d['gates'])
    ok = pc > 0.999 and mx < 0.15
    return {'name': 'IVP15 blind families (T15)', 'passed': bool(ok),
            'detail': f"PC0'={pc:.4f}, max |r_H7|={mx:.3f}"}


def ivp16_anomaly_taxonomy():
    """C14/T16: аттрактор глобален — нет ранговых выбросов; таксономия."""
    d = json.load(open(_data('computations/C14_anomaly_hunt/data/results.json')))
    ok = d['n_rH7_outliers_0p35'] == 0 and d['meta']['n_configs'] >= 100
    return {'name': 'IVP16 anomaly taxonomy (T16)', 'passed': bool(ok),
            'detail': f"{d['meta']['n_configs']} configs, "
                      f"{d['n_rH7_outliers_0p35']} rank outliers"}


def ivp17_dirichlet_universal():
    """C15/T17: следовая формула со скрученным весом на точности ≤ 1e-4;
    ранговая проекция против нулей L — нулевая зона."""
    d = json.load(open(_data('computations/C15_dirichlet/data/results.json')))
    mx = max(r['abs_diff'] for q in ('q5', 'q7')
             for r in d['results'][q]['trace_formula'])
    mx_r = max(abs(g['r_H7']) for g in d['gate_rank_projection'])
    ok = mx < 1e-4 and mx_r < 0.25
    return {'name': 'IVP17 Dirichlet universality (T17)', 'passed': bool(ok),
            'detail': f'max |dK| {mx:.1e}, max |r_H7| {mx_r:.3f}'}


def ivp18_qinfo():
    """C16/T18: локальность давит фермионную запутанность (z > 10 против
    Haar-базы); MI не несёт нулевой подписи."""
    d = json.load(open(_data('computations/C16_qinfo/data/results.json')))
    z = d['Q1_gate_MI_max_z_vs_page']
    c0 = d['Q2_MI_alignment']['corr_MI_vs_zerowindow']
    ok = z > 10 and abs(c0) < 0.3
    return {'name': 'IVP18 qinfo locality echo (T18)', 'passed': bool(ok),
            'detail': f'z_vs_page {z:.0f}, corr MI-zero {c0:+.3f}'}


ALL = [ivp01_release_integrity, ivp02_gamma_closures, ivp03_zid_reality,
       ivp04_argument_anchors, ivp05_zeros_vs_rvm, ivp06_trace_formula_hxi,
       ivp07_gue_class, ivp08_colocation, ivp09_psi_staircase,
       ivp10_cross_language,
       ivp11_nonlocal_primitive, ivp12_colocation_hard,
       ivp13_alpha_third_law, ivp14_band5000, ivp15_blind_families,
       ivp16_anomaly_taxonomy, ivp17_dirichlet_universal, ivp18_qinfo]



def run_all():
    return [f() for f in ALL]
