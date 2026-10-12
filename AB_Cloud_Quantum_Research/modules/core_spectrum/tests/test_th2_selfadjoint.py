"""Th2: дефектные индексы (0,0) и унитарность."""
from rpbridge.selfadjoint import defect_indices_finite, unitarity_and_current


def test_defect_indices_zero():
    for L in (12, 16):
        d = defect_indices_finite(L)
        assert d['n_plus'] == 0 and d['n_minus'] == 0


def test_unitarity_and_imag_form():
    u = unitarity_and_current(12)
    assert u['unitarity_drift_max'] < 1e-12
    assert u['imag_form'] < 1e-12
