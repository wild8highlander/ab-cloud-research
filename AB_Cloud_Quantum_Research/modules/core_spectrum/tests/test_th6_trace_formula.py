"""Th6/V7: следовая формула (живой пересчёт, 20k нулей)."""
from rpbridge.arithmetic_trace import verify_hxi
from rpbridge.zeros import load_zeros


def test_q_identity():
    v = verify_hxi(load_zeros(nmax=20000))
    assert v['M0_max_abs_diff_Q'] < 1e-6


def test_k_identity():
    v = verify_hxi(load_zeros(nmax=20000))
    assert v['M1_max_abs_diff_K'] < 5e-5
