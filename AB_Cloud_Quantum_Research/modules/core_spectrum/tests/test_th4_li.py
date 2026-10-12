"""Th4/V15: два пути λ_n и положительность (n ≤ 300 живьём)."""
import numpy as np
from rpbridge.li import li_from_zeros, li_spectral
from rpbridge.zeros import load_zeros


def test_two_paths():
    z = load_zeros()
    lam, _, _ = li_from_zeros(z, n_max=300)
    lam_sp = li_spectral(z, n_max=300)
    assert np.max(np.abs(lam - lam_sp)) < 1e-9


def test_positivity_n300():
    z = load_zeros()
    lam, tail, _ = li_from_zeros(z, n_max=300)
    assert np.all(lam - tail > 0)
