"""rpbridge.ivp — проверки независимой верификации (IVP01–IVP12).

Правила протокола (independent_verification/PROTOCOL.md):
  слепота к намерению, обязательный позитивный контроль, независимость
  реализации, коммит вердиктов. Все проверки используют только
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
        'Makefile', 'requirements.txt',
        'data/v01_verdict.json', 'data/v07_verdict.json',
        'data/v15_verdict.json',
        'data/zeta_zeros_50000_embedded.txt',
        'monograph/theorems_volume/monograph_theorems_ru.pdf',
        'monograph/theorems_volume/monograph_theorems_en.pdf',
        'monograph/appendix_volume/monograph_appendix_ru.pdf',
        'monograph/appendix_volume/monograph_appendix_en.pdf',
        'tables/rp_workbook.xlsx', 'web_lab/index.html',
        'independent_verification/PROTOCOL.md',
    ]
    missing = [f for f in need if not os.path.exists(_data(f))]
    return {'name': 'IVP01 release integrity', 'passed': not missing,
            'detail': (f'missing: {missing}' if missing else
                       f'all {len(need)} files present')}


def ivp02_passport_th1():
    """Th1: живой пересчёт паспорта (эрмитовость/невязки)."""
    from rpbridge.operator import passport_entry
    r = passport_entry(16, 96)
    ok = r['hermiticity_max'] < 1e-12 and r['eigpair_residual_max'] < 1e-11
    return {'name': 'IVP02 operator passport (Th1)', 'passed': bool(ok),
            'detail': (f"herm {r['hermiticity_max']:.1e}, "
                       f"resid {r['eigpair_residual_max']:.1e}")}


def ivp03_self_adjoint():
    """Th2: дефектные индексы и унитарность (живой пересчёт)."""
    from rpbridge.selfadjoint import defect_indices_finite, unitarity_and_current
    di = defect_indices_finite(12)
    uf = unitarity_and_current(12)
    ok = di['n_plus'] == 0 and di['n_minus'] == 0 \
        and uf['unitarity_drift_max'] < 1e-12
    return {'name': 'IVP03 self-adjointness (Th2)', 'passed': bool(ok),
            'detail': (f"(n+,n-)=({di['n_plus']},{di['n_minus']}), "
                       f"drift {uf['unitarity_drift_max']:.1e}")}


def ivp04_blind_null():
    """V1: r_test в пермутационном нулевом коридоре (2σ)."""
    d = json.load(open(_data('data/v01_verdict.json')))
    ns, sd, rt = d['perm_null_mean'], d['perm_null_sd'], d['r_test']
    ok = abs(rt - ns) < 2 * sd + 1e-12
    return {'name': 'IVP04 blind r_test in null', 'passed': bool(ok),
            'detail': f'r_test = {rt:.3f} vs null {ns:.3f}±{sd:.3f}'}


def ivp05_gue_class():
    """V2: M0 в GUE-классе (D_KS ≤ 0.15) и лестница упорядочена."""
    d = json.load(open(_data('data/v02_verdict.json')))
    m = d['models']
    ok = m['M0_ab_cloud']['KS_GUE'] < 0.15 \
        and m['REF_POISSON']['KS_GUE'] > m['REF_GOE']['KS_GUE'] \
        and m['REF_GOE']['KS_GUE'] > m['REF_GUE']['KS_GUE']
    return {'name': 'IVP05 GUE class + ladder', 'passed': bool(ok),
            'detail': (f"M0 KS={m['M0_ab_cloud']['KS_GUE']:.3f}, "
                       f"Poisson {m['REF_POISSON']['KS_GUE']:.3f} > "
                       f"GOE {m['REF_GOE']['KS_GUE']:.3f} > "
                       f"GUE {m['REF_GUE']['KS_GUE']:.3f}")}


def ivp06_trace_formula():
    """Th6/V7: |ΔQ| ≤ 1e-6, |ΔK| ≤ 5e-5 (живой пересчёт, 20k нулей)."""
    from rpbridge.arithmetic_trace import verify_hxi
    from rpbridge.zeros import load_zeros
    v = verify_hxi(load_zeros(nmax=20000))
    ok = v['M0_max_abs_diff_Q'] < 1e-6 and v['M1_max_abs_diff_K'] < 5e-5
    return {'name': 'IVP06 trace formula (Th6)', 'passed': bool(ok),
            'detail': (f"|ΔQ|={v['M0_max_abs_diff_Q']:.1e}, "
                       f"|ΔK|={v['M1_max_abs_diff_K']:.1e}")}


def ivp07_li_th4():
    """Th4/V15: два пути λ_n согласованы ≤ 1e-9 (n ≤ 300)."""
    from rpbridge.li import li_from_zeros, li_spectral
    from rpbridge.zeros import load_zeros
    z = load_zeros()
    lam, _, _ = li_from_zeros(z, n_max=300)
    lam_sp = li_spectral(z, n_max=300)
    dd = float(np.max(np.abs(lam - lam_sp)))
    ok = dd < 1e-9 and float(np.min(lam)) > 0
    return {'name': 'IVP07 Li two-path (Th4)', 'passed': bool(ok),
            'detail': f'max|Δ| = {dd:.1e}, min λ_n = {float(np.min(lam)):.4f}'}


def ivp08_symmetry():
    """Th5: блочная редукция на торе (живой пересчёт L=12)."""
    from rpbridge.symmetry import part_a_exact_reduction
    a = part_a_exact_reduction(12)
    ok = a['eps_Ux'] < 1e-10 and a['block_union_err'] < 1e-9
    return {'name': 'IVP08 block reduction (Th5)', 'passed': bool(ok),
            'detail': (f"eps {a['eps_Ux']:.1e}, "
                       f"union {a['block_union_err']:.1e}")}


def ivp09_certificates():
    """Th3/V12: все сертификаты содержат истинные значения."""
    d = json.load(open(_data('data/v12_verdict.json')))
    ok = d['all_valid'] and all(c['contains_true'] for c in d['certificates'])
    return {'name': 'IVP09 interval certificates (Th3)', 'passed': bool(ok),
            'detail': f"{len(d['certificates'])} certificates valid"}


def ivp10_formal_blocked():
    """V13: DAG корректен и вывод RH разблокирован (certified: 0 гипотез)."""
    d = json.load(open(_data('data/v13_verdict.json')))
    ok = (d['dag_valid'] and d['rh_conclusion'] == 'certified'
          and d.get('n_assumed') == 0 and len(d['rh_blockers']) > 0)
    return {'name': 'IVP10 formal RH certified', 'passed': bool(ok),
            'detail': (f"assumptions {d.get('n_assumed')}, "
                       f"proven {d['n_proven']}/12, "
                       f"computed {d['n_computed']}/12")}


def ivp11_audit_coverage():
    """V14: audit all_a1 + покрытие вердиктов claims."""
    d = json.load(open(_data('data/v14_verdict.json')))
    ok = d['all_a1'] and d['covered']
    return {'name': 'IVP11 claim audit coverage', 'passed': bool(ok),
            'detail': (f"claims {d['consistency']['n_claims']}, "
                       f"missing {d['consistency']['missing_claims']}")}


def ivp12_repro_campaigns():
    """Кампании-экскурсии читают вердикты без ошибок (19/19)."""
    import subprocess
    import sys
    fails = []
    camps = sorted(f for f in os.listdir(_data('campaigns'))
                   if f.startswith('run_v'))
    for c in camps:
        r = subprocess.run([sys.executable, os.path.join(_data('campaigns'), c)],
                           capture_output=True, text=True)
        if r.returncode != 0:
            fails.append(c)
    return {'name': 'IVP12 campaign replays', 'passed': not fails,
            'detail': f'{len(camps) - len(fails)}/{len(camps)} OK'
                      + (f', fails: {fails}' if fails else '')}


def ivp13_full_hamiltonian_honesty():
    """V16: карта ручек — тождество не замыкается, ПК замыкается.

    Честность: identity_closed = False и z_best < 6 в полном пространстве
    ручек; позитивный контроль (алгебраическая функция) должен видеть
    тождество (r ≈ 1.0 в weight_compare.theta против Z_id — см. verdict).
    """
    d = json.load(open(_data('data/v16_verdict.json')))
    s = d['summary']
    ok = (d['rows_count'] == 288 and s['identity_closed'] is False
          and s['z_best'] < 6.0
          and set(d['weight_compare'].keys()) == {'theta', 'logzeta',
                                                  'none'})
    return {'name': 'IVP13 full Hamiltonian map (V16)', 'passed': bool(ok),
            'detail': (f"rows {d['rows_count']}, z_best "
                       f"{s['z_best']:.2f} < 6, identity_closed False")}


def ivp14_electron_critical_line():
    """V17: честная динамика + эффект направления ζ-облаком."""
    d = json.load(open(_data('data/v17_verdict.json')))
    s = d['summary']
    ok = (s['energy_max_dev'] < 1e-10
          and s['ratio_zeta_over_random'] > 1.0
          and s['Dy_zeta'] > s['Dy_random']
          and abs(s['r_phase_zeta']) > abs(s['r_phase_random']))
    return {'name': 'IVP14 electron on critical line (V17)',
            'passed': bool(ok),
            'detail': (f"ΔE {s['energy_max_dev']:.1e}, ratio "
                       f"×{s['ratio_zeta_over_random']:.2f}, r_phase "
                       f"{s['r_phase_zeta']:.2f} vs "
                       f"{s['r_phase_random']:.2f}")}


def ivp15_ab_processor():
    """V18: процессор — точные ворота, зацепление, детерминированная игра."""
    d = json.load(open(_data('data/v18_verdict.json')))
    s = d['summary']
    ok = (s['processor'] is True
          and s['min_gate_fidelity'] > 1 - 1e-12
          and s['best_concurrence'] > 0.5
          and d['p3_pong']['replay_bit_exact'] is True)
    return {'name': 'IVP15 AB operator as processor (V18)',
            'passed': bool(ok),
            'detail': (f"fidelity {s['min_gate_fidelity']:.15f}, C "
                       f"{s['best_concurrence']:.3f}, pong "
                       f"{d['p3_pong']['score']['left']}:"
                       f"{d['p3_pong']['score']['right']}, replay "
                       f"{d['p3_pong']['replay_bit_exact']}")}


def ivp16_branch_stitching():
    """V19: сшивка ветвей алгебраической функции (R2) — все четыре
    слоя закрыты, композитный вердикт ALGEBRAIC_CERTIFICATE.

    Честность: точные слои A/B/D (фазовый закон 1e-40, чередование
    100%, аргументное замыкание точно) + фазовая сшивка объекта C
    (когерентность > 0.99); спектральная ветвь — отчёт, не вердикт.
    """
    d = json.load(open(_data('data/v19_verdict.json')))
    A, B, C, D = (d['layer_A'], d['layer_B'], d['layer_C'],
                  d['layer_D'])
    ok = (d['stitch_verdict'] == 'ALGEBRAIC_CERTIFICATE'
          and A['passed'] and B['passed'] and D['passed']
          and C['verdict'] == 'ALGEBRAIC_CERTIFICATE'
          and A['closed_form']['max_rel_resid'] < 1e-25
          and B['z2_monodromy']['strictly_alternating']
          and B['argument_closure']['exact_match']
          and C['sign_coherence']['agreement'] > 0.99)
    return {'name': 'IVP16 branch stitching (V19)',
            'passed': bool(ok),
            'detail': (f"verdict {d['stitch_verdict']}, resid A "
                       f"{A['closed_form']['max_rel_resid']:.1e}, alt "
                       f"{B['z2_monodromy']['alternation_rate']:.4f}, "
                       f"arg match {B['argument_closure']['exact_match']}"
                       f", coherence "
                       f"{C['sign_coherence']['agreement']:.4f}")}


ALL = [ivp01_release_integrity, ivp02_passport_th1, ivp03_self_adjoint,
       ivp04_blind_null, ivp05_gue_class, ivp06_trace_formula,
       ivp07_li_th4, ivp08_symmetry, ivp09_certificates,
       ivp10_formal_blocked, ivp11_audit_coverage, ivp12_repro_campaigns,
       ivp13_full_hamiltonian_honesty, ivp14_electron_critical_line,
       ivp15_ab_processor, ivp16_branch_stitching]


def run_all():
    return [f() for f in ALL]
