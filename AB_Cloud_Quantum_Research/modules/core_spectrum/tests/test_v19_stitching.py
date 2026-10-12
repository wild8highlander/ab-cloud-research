"""V19: сшивка ветвей алгебраической функции (живой пересчёт).

Проверяет:
  1. Структуру Ферма-накрытия: листы, коммутативная монодромия,
     граф Γ_N (χ = −N², цикломатика N²+1).
  2. Фазовый закон ζ^{ra+sb} и ортогональность характеров (слой A)
     до 1e-25 (машинный пол tanh-sinh по гладкой параметризации).
  3. Z₂-монодромию Z_id: строгое чередование знаков и точное
     аргументное замыкание (слой B, малый масштаб).
  4. Знаковую когерентность Γ-фазы: согласие sign(cos θ) с (−1)^k
     > 0.99 и z против пермукаций (слой C).
  5. Регрессию R1/R2/R4 (слой D) — flagship до 1e-25.
"""
import numpy as np

from rpbridge.stitching import (cover_sheets, cover_graph,
                                beta_period_exact, beta_period_numeric,
                                phase_check, stitch_phase, stitch_closure,
                                layer_a_reference, layer_b_transfer,
                                sign_phase_coherence, theta_ladder,
                                layer_d_regression)
from rpbridge.zeros import load_zeros


def _zeros():
    return load_zeros(nmax=260)


def test_cover_structure():
    sheets, s0, s1, comm = cover_sheets(15)
    assert len(sheets) == 225
    assert comm
    assert s0((3, 5)) == (4, 5) and s1((3, 5)) == (3, 6)
    g = cover_graph(15)
    assert g['V'] == 225 and g['E'] == 450
    assert g['chi_ok'] and g['cyclomatic_ok']
    g1 = cover_graph(1)
    assert g1['V'] == 1 and g1['cyclomatic_ok']


def test_phase_law_machine_precision():
    # точный против численного (гладкая параметризация)
    ex = beta_period_exact(1, 1, 2)
    num = beta_period_numeric(1, 1, 2)
    assert abs(num - ex) / abs(ex) < 1e-25
    # фазовый закон на листе
    got = phase_check(7, 3, 5, 11, 15)
    pred = stitch_phase(7, 3, 5, 11, 15)
    assert abs(got - pred) / abs(pred) < 1e-25
    # ортогональность характеров
    c0 = stitch_closure(0, 0, 15)
    assert c0['closure'] and c0['value'] == 225
    c1 = stitch_closure(1, 1, 15)
    assert c1['closure'] and c1['value'] < 1e-20


def test_layer_a_full():
    A = layer_a_reference(N=15, n_ab=3, seed=96)
    assert A['passed']
    assert A['closed_form']['max_rel_resid'] < 1e-25
    assert A['phase_law']['max_rel_resid'] < 1e-25


def test_layer_b_z2_monodromy_and_closure():
    z = _zeros()
    B = layer_b_transfer(z, n_zeros=200, T=60.0)
    assert B['passed']
    alt = B['z2_monodromy']
    assert alt['strictly_alternating']
    assert alt['alternation_rate'] == 1.0
    arg = B['argument_closure']
    assert arg['exact_match'] and arg['n_zeros'] == arg['n_sign_changes']


def test_layer_c_phase_stitching():
    z = _zeros()
    lad = theta_ladder(z, n_zeros=200)
    assert lad['concentration_ok']
    assert lad['concentration'] > 0.5
    coh = sign_phase_coherence(z, n_zeros=200, n_perm=40)
    assert coh['coherent']
    assert coh['agreement'] > 0.99
    assert coh['z_score'] > 5.0


def test_layer_d_regression():
    D = layer_d_regression(n_suite=500, seed=96)
    assert D['passed']
    assert D['R1_flagship']['resid_rel'] < 1e-25
    assert D['R2_suite']['worst_phase_dev'] < 1e-15


def test_run_fast_verdict():
    from rpbridge.stitching import run as run_v19
    v = run_v19(_zeros(), full=False)
    assert v['stitch_verdict'] == 'ALGEBRAIC_CERTIFICATE'
    assert v['layers_closed'] == dict(A=True, B=True, C=True, D=True)
    assert v['layer_C']['sign_coherence']['agreement'] > 0.99
