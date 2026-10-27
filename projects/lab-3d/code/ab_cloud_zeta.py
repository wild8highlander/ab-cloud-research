"""
ab_cloud_zeta.py
================
Riemann zeros with PROPER Riemann-von Mangoldt unfolding.

CRITICAL FIX vs v17:
--------------------
v17 used polynomial regression  N(γ) ≈ a + b·γ + c·γ·log(γ)  as the unfolding.
That is a hack: the coefficients a,b,c float to fit the data, so the unfolded
sequence is by construction closer to mean-spacing 1 than a true Weyl unfolding
would give.  Different choices of fitting basis give ⟨r⟩ in [0.51, 0.60] for
N=1000 — i.e. the result is dominated by the unfolding choice, not by the data.

Here we use the EXACT Riemann-von Mangoldt formula

    N(T) = T/(2π) · log(T/(2π)) - T/(2π) + 7/8 + S(T)

and unfold via ξ_n = N(γ_n).  The S(T) term (the argument of ζ on the critical
line) is O(log T / log log T), much smaller than the main term, so we neglect
it (standard practice in Montgomery-style analysis).  We then verify that the
mean unfolded spacing is ≈ 1 as a sanity check.

Zeros are computed via mpmath (high-precision), then cast to float64.
"""
from __future__ import annotations

import numpy as np
from mpmath import mp, zetazero


def riemann_von_mangoldt_N(T: float) -> float:
    """
    Smooth counting function (Riemann-von Mangoldt main terms):
        N(T) = (T/2π) · log(T/2π) - T/2π + 7/8
    Returns float.
    """
    if T <= 0.0:
        return 0.0
    c = T / (2.0 * np.pi)
    return c * np.log(c) - c + 7.0 / 8.0


def fetch_riemann_zeros(N: int, dps: int = 25) -> np.ndarray:
    """
    Fetch the first N non-trivial Riemann zeros γ_n (imaginary parts).
    Uses mpmath.zetazero at decimal precision `dps`.
    """
    mp.dps = dps
    zs = np.empty(N, dtype=float)
    for n in range(1, N + 1):
        zs[n - 1] = float(zetazero(n).imag)
    return zs


def unfold_rvm(zeros: np.ndarray) -> np.ndarray:
    """
    Unfold via x_n = N(γ_n)  (Riemann-von Mangoldt, no S(T) term).
    Returns the unfolded sequence (NOT the spacings).
    """
    return np.array([riemann_von_mangoldt_N(float(z)) for z in zeros], dtype=float)


def unfolded_spacings(zeros: np.ndarray) -> np.ndarray:
    """
    Returns s_n = x_{n+1} - x_n  with x_n = N(γ_n).
    """
    x = unfold_rvm(zeros)
    s = np.diff(x)
    return s[s > 0]


def sanity_check_unfolding(zeros: np.ndarray, label: str = "") -> dict:
    """
    Sanity check: mean unfolded spacing should be ≈ 1.
    If it isn't, the unfolding is wrong and ALL downstream statistics are biased.
    """
    s = unfolded_spacings(zeros)
    return {
        "label": label,
        "n_zeros": len(zeros),
        "mean_spacing": float(np.mean(s)),
        "std_spacing": float(np.std(s)),
        "mean_to_one_err": float(abs(np.mean(s) - 1.0)),
    }
