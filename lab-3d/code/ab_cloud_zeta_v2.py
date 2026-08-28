"""
ab_cloud_zeta.py
================
Riemann zeta zeros and analytic number theory utilities.

- mpmath-based computation of zeta zeros (high precision)
- Riemann-von Mangoldt explicit formula
- Montgomery-Odlyzko pair correlation of zeta zeros
- Bogomolny-Keating sigma_BK bootstrap
- Spectral form factor of zeta zeros (long-time regime)
"""
import json
import os
import numpy as np
import mpmath
from mpmath import mp

# Set high precision for zeta-zero computation
mp.dps = 25

# ---------------------------------------------------------------------------
# Zeta zeros cache: avoid recomputing the first 500 zeros on every run.
# The cache file is created by /home/z/my-project/scripts/cache_zeta_zeros.py
# ---------------------------------------------------------------------------
_ZETA_CACHE_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "results", "data", "zeta_zeros_cache.json",
)
_ZETA_CACHE: list = []

def _load_zeta_cache():
    """Load cached zeta zeros if available."""
    global _ZETA_CACHE
    if _ZETA_CACHE:
        return
    try:
        if os.path.exists(_ZETA_CACHE_PATH):
            with open(_ZETA_CACHE_PATH, "r") as f:
                _ZETA_CACHE = json.load(f).get("zeros", [])
    except Exception:
        _ZETA_CACHE = []


def compute_zeta_zeros(n_zeros: int, n_start: int = 0, dps: int = 25) -> np.ndarray:
    """
    Compute the first n_zeros Riemann zeta zeros on the critical line.
    Uses the cached zeros when available; falls back to mpmath.zetazero
    for indices beyond the cache.
    """
    _load_zeta_cache()
    cached = _ZETA_CACHE
    needed_end = n_start + n_zeros

    zeros = []
    # Use cached zeros for the requested range
    if n_start < len(cached):
        cached_slice = cached[n_start:min(needed_end, len(cached))]
        zeros.extend(cached_slice)

    # Compute any remaining zeros beyond the cache
    if needed_end > len(cached):
        old_dps = mp.dps
        mp.dps = dps
        try:
            compute_start = max(n_start, len(cached)) + 1
            compute_end = needed_end + 1
            for k in range(compute_start, compute_end):
                t = float(mpmath.im(mpmath.zetazero(k)))
                zeros.append(t)
        finally:
            mp.dps = old_dps

    return np.array(zeros[:n_zeros])


def riemann_von_mangoldt_N(T: float) -> float:
    """
    Riemann-von Mangoldt: N(T) = T/(2pi) log(T/(2pi e)) + 7/8 + S(T).
    Approximation ignoring S(T) (mean zero).
    """
    if T <= 0:
        return 0.0
    return T / (2 * np.pi) * np.log(T / (2 * np.pi * np.e)) + 7.0 / 8.0


def unfold_zeta_zeros(zeros: np.ndarray) -> np.ndarray:
    """Unfold zeta zeros via the smooth Riemann-von Mangoldt counting function.

    The unfolded energies are xi_n = N_bar(t_n), where N_bar(T) is the smooth
    part of the zero-counting function.  These have mean spacing 1 by
    construction, so spacing_ratios(xi) yields a value comparable to the
    GUE prediction <r> = 0.5996.

    Returns
    -------
    np.ndarray of length len(zeros): the unfolded levels xi_n.
    """
    return np.array([riemann_von_mangoldt_N(float(t)) for t in zeros])


def normalized_zeta_spacings(zeros: np.ndarray) -> np.ndarray:
    """Normalized spacings (mean 1) of zeta zeros."""
    d = np.diff(zeros)
    return d / np.mean(d)


def pair_correlation_zeta(
    zeros: np.ndarray, s_max: float = 3.0, n_bins: int = 50, n_sample: int = 2000
) -> tuple:
    """
    Empirical pair correlation of zeta zeros.
    Returns (s_centers, R_2_emp).
    """
    n = len(zeros)
    if n < 4:
        return np.array([]), np.array([])
    # Use mean spacing of unfolded zeros
    unfolded = unfold_zeta_zeros(zeros)
    # Actually use raw zeros with mean spacing
    mean_sp = np.mean(np.diff(zeros))
    bins = np.linspace(0, s_max, n_bins + 1)
    centers = 0.5 * (bins[1:] + bins[:-1])
    counts = np.zeros(n_bins)
    rng = np.random.default_rng(42)
    n_use = min(n, n_sample)
    idx = rng.choice(n, size=n_use, replace=False)
    for i in idx:
        ds = (zeros[i + 1:] - zeros[i]) / mean_sp
        ds = ds[ds <= s_max]
        if len(ds):
            h, _ = np.histogram(ds, bins=bins)
            counts += h
    R2 = counts / max(np.mean(counts[-5:]), 1e-10)
    return centers, R2


def bogomolny_keating_sigma(N: float) -> float:
    """
    BK heuristic: sigma_BK = C / sqrt(N), C calibrated to give correct
    long-range correlations of zeta zeros.
    Monograph: C = 0.27 (after bootstrap SEM).
    """
    return 0.27 / np.sqrt(N)


def zeta_form_factor(zeros: np.ndarray, t_array: np.ndarray) -> np.ndarray:
    """
    Spectral form factor of zeta zeros (in unfolded time):
        K(t) = (1/N) |sum_n exp(i t e_n)|^2
    """
    e = unfold_zeta_zeros(zeros)
    K = np.zeros(len(t_array))
    for k, t in enumerate(t_array):
        s = np.sum(np.exp(1j * t * e))
        K[k] = np.abs(s) ** 2 / len(e)
    return K


def hardy_Z(t: float, n_terms: int = 50) -> float:
    """
    Hardy Z function: Z(t) = e^{i theta(t)} zeta(1/2 + i t),
    where theta is the Riemann-Siegel theta.
    """
    theta = float(mpmath.sievet(theta_arg=t)) if hasattr(mpmath, "sievet") else 0.0
    # Use mpmath.siegelz
    return float(mpmath.siegelz(t))


def prime_counting_comparison(N: int) -> dict:
    """
    Compare pi(N) (prime counting) with Li(N) (logarithmic integral)
    and Riemann R(N) — these are connected to zeta zeros via explicit formula.
    """
    from sympy import primepi, li
    pi_N = int(primepi(N))
    Li_N = float(li(N))
    R_N = float(mpmath.RiemannR(N))
    return {
        "N": N,
        "pi_N": pi_N,
        "Li_N": Li_N,
        "R_N": R_N,
        "Li_minus_pi": Li_N - pi_N,
        "R_minus_pi": R_N - pi_N,
    }


if __name__ == "__main__":
    # Smoke test: small set of zeta zeros
    z = compute_zeta_zeros(20)
    print(f"First 20 zeta zeros: {z[:5]} ...")
    print(f"Mean spacing (unfolded): {np.mean(np.diff(unfold_zeta_zeros(z))):.4f}")
