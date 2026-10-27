"""Th1: эрмитовость и вещественность (живой пересчёт, порог 1e-12)."""
from rpbridge.operator import passport_entry


def test_hermiticity_exact():
    r = passport_entry(16, 96)
    assert r['hermiticity_max'] < 1e-12


def test_residuals_machine():
    r = passport_entry(24, 96)
    assert r['eigpair_residual_max'] < 1e-11


def test_chiral_pairing_w0():
    r = passport_entry(24, 96, W=0.0)
    assert r['chiral_pair_max'] < 1e-12
