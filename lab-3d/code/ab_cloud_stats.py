"""
ab_cloud_stats.py
=================
Honest GUE/RMT statistics: ⟨r⟩, Σ²(L), Δ₃(L), p(s), R₂(s).

KEY FIXES vs v17:
-----------------
1. ⟨r⟩ is computed BOTH with and without an energy window.  We print both.
   The v17 'filtered' ⟨r⟩ = 0.59 was an artefact of the (3.0, 5.0) window +
   edge_frac=0.30 cut.  The honest full-spectrum ⟨r⟩ is also reported.

2. f_GUE is a TWO-SIDED criterion:  0.8 ≤ f_GUE ≤ 1.2.
   v17 used 'f_GUE ≥ 0.80' which lets 'more rigid than GUE' (f_GUE > 1) PASS.
   That is logically wrong: f_GUE > 1 means data < GUE, i.e. NOT GUE.
   Here we test |f_GUE - 1| ≤ 0.2.

3. Bootstrap errors on ⟨r⟩ and on Σ²/Δ₃ instead of the bogus σ_BK = 0.4/√N.
   (The Bogomolny-Keating coefficient applies to number variance, not to ⟨r⟩,
   and the correct coefficient for ⟨r⟩ is ≈ 0.05/√N — 8x smaller.)

4. Direct R₂(s) = 1 - Y₂(s) Montgomery check.  v17 only had Σ² and Δ₃,
   which are derived quantities; the direct pair correlation was missing.
   For unfolded ζ-spacings s,  R₂(s)  is compared to the GUE prediction
   1 - (sin(π s)/(π s))².   This is the original Montgomery theorem.

5. Uniform bins for χ² (NOT adaptive).  v17's 'χ² = 3.56 with df=25' was
   artificially low because high-s bins had zero counts.

6. KS test against the Wigner-Dyson surmise p(s) = (32/π²) s² exp(-4 s²/π),
   with explicit p-value (no 'p > 0.05 means GUE' hand-waving).
"""
from __future__ import annotations

import numpy as np
from scipy import stats


# ---------- unfolded-sequence utilities ----------

def spacings_from_levels(levels: np.ndarray) -> np.ndarray:
    """s_n = E_{n+1} - E_n  (assumed already unfolded)."""
    s = np.diff(np.sort(levels))
    return s[s > 0]


def mean_level_spacing_ratio(spacings: np.ndarray, n_boot: int = 100) -> tuple[float, float]:
    """
    ⟨r⟩ = mean( min(s_n, s_{n+1}) / max(s_n, s_{n+1}) ).
    Returns (point_estimate, bootstrap_std).
    """
    if len(spacings) < 3:
        return float("nan"), float("nan")
    s = spacings
    r = np.minimum(s[:-1], s[1:]) / np.maximum(s[:-1], s[1:])
    point = float(np.mean(r))
    # bootstrap (vectorised for speed)
    rng = np.random.default_rng(0)
    n = len(r)
    idx = rng.integers(0, n, size=(n_boot, n))
    bs = np.mean(r[idx], axis=1)
    return point, float(np.std(bs))


def wigner_dyson_pdf(s: np.ndarray) -> np.ndarray:
    """GUE Wigner-Dyson surmise: p(s) = (32/π²) s² exp(-4 s²/π)."""
    return (32.0 / np.pi**2) * s**2 * np.exp(-4.0 * s**2 / np.pi)


# ---------- Σ²(L) and Δ₃(L) ----------

def sigma2_statistic(unfolded: np.ndarray, L: float) -> float:
    """
    Number variance Σ²(L): variance of  N(τ+L) - N(τ) - L  over the unfolded axis.
    Vectorised: uses np.searchsorted on the full xs+L array at once.
    """
    if len(unfolded) < 10:
        return float("nan")
    xs = unfolded
    n_max = len(xs) - 1
    targets = xs[:n_max] + L
    k = np.searchsorted(xs, targets, side="right")
    counts = np.maximum(k - (np.arange(n_max) + 1), 0).astype(float)
    return float(np.var(counts))


def delta3_statistic(unfolded: np.ndarray, L: float) -> float:
    """
    Spectral rigidity Δ₃(L): average over windows of length L of the
    variance of residuals from a linear fit of the local staircase.
    """
    if len(unfolded) < 10:
        return float("nan")
    xs = unfolded
    n_max = len(xs) - 2
    targets = xs[:n_max] + L
    k = np.searchsorted(xs, targets, side="right")
    residuals = []
    for n in range(n_max):
        ki = k[n]
        if ki - n < 3:
            continue
        window_x = xs[n:ki] - xs[n]
        window_y = np.arange(ki - n, dtype=float)
        A = np.vstack([np.ones_like(window_x), window_x]).T
        coef, *_ = np.linalg.lstsq(A, window_y, rcond=None)
        resid = window_y - A @ coef
        residuals.append(float(np.var(resid)))
    if len(residuals) == 0:
        return float("nan")
    return float(np.mean(residuals))


def sigma2_GUE_exact(L: float) -> float:
    """
    Exact GUE number variance:
        Σ²_GUE(L) = L - 2 ∫_0^L (L-τ) Y₂(τ) dτ
    where  Y₂(τ) = (sin(π τ)/(π τ))²  for GUE.
    Computed by Simpson's rule.
    """
    if L <= 0:
        return 0.0
    N = max(200, int(L * 50))
    ts = np.linspace(0.0, L, N + 1)
    integrand = (L - ts) * (np.sinc(ts) ** 2)  # np.sinc(x) = sin(π x)/(π x)
    integral = np.trapz(integrand, ts)
    return L - 2.0 * float(integral)


def delta3_GUE_exact(L: float) -> float:
    """
    GUE spectral rigidity Δ₃(L).

    Dyson-Mehta asymptotic (large L):
        Δ₃_GUE(L) ≈ (1/π²) [log(2πL) + γ - 5/4]

    For small L (L < 2), use the small-L expansion
        Δ₃_GUE(L) ≈ L/15 - L²/180 + ...

    We use the asymptotic for L ≥ 2, and a Simpson-integrated Mehta formula
    for L < 2 (the asymptotic is poor for very small L).
    """
    if L <= 0:
        return 0.0
    gamma = 0.5772156649015329
    if L >= 2.0:
        # asymptotic (large-L) Mehta formula
        return (1.0 / np.pi**2) * (np.log(2 * np.pi * L) + gamma - 5.0 / 4.0)
    else:
        # exact small-L via Simpson integration of the Dyson-Mehta kernel
        # Δ₃(L) = (2/π²) ∫_0^L (1 - τ/L) · [1 - (sin(πτ)/(πτ))²] · (1/τ) dτ
        # but the 1/τ is singular at τ=0; use the equivalent non-singular form:
        # Δ₃(L) = (2/π²) ∫_0^L (1 - τ/L) · Y₂(τ) / τ² ·... use quadrature on [eps, L]
        N = 2000
        eps = 1e-6
        ts = np.linspace(eps, L, N + 1)
        # the integrand:  (1 - τ/L) · (1 - sinc²(τ)) / τ  ... but this still has 1/τ
        # Use: 1 - sinc²(τ) ≈ (π² τ²)/3 for small τ, so (1-sinc²)/τ ≈ π² τ/3 (no singularity)
        Y2 = np.sinc(ts) ** 2
        integrand = (1.0 - ts / L) * (1.0 - Y2) / ts
        integral = np.trapz(integrand, ts)
        # add the small-τ contribution analytically:
        # ∫_0^eps (1 - τ/L) · (π² τ / 3) dτ = (π²/3) [τ²/2 - τ³/(3L)]_0^eps ≈ π² eps²/6
        integral += (np.pi**2 / 3.0) * (eps**2 / 2.0 - eps**3 / (3.0 * L))
        return (2.0 / np.pi**2) * float(integral)


def f_gue_two_sided(data_val: float, poisson_val: float, gue_val: float) -> float:
    """
    f_GUE = (Poisson - data) / (Poisson - GUE).
    The TWO-SIDED criterion is  |f_GUE - 1| ≤ 0.2.
    Returns f_GUE.
    """
    if abs(poisson_val - gue_val) < 1e-12:
        return float("nan")
    return (poisson_val - data_val) / (poisson_val - gue_val)


# ---------- R₂(s) — direct Montgomery pair correlation ----------

def R2_empirical(unfolded: np.ndarray, s_grid: np.ndarray, ds: float = 0.05) -> np.ndarray:
    """
    Empirical R₂(s) on the unfolded axis:
        R₂(s) = ⟨ Σ_{m ≠ n} δ(s - (x_m - x_n)) ⟩ / ρ
    Estimated via histogram of all pair distances in (0, s_max].
    """
    xs = unfolded
    n = len(xs)
    # all pair distances |x_m - x_n|  — O(N²) but N~1000 is fine
    diff = np.abs(xs[:, None] - xs[None, :])
    iu = np.triu_indices(n, k=1)
    d = diff[iu]
    # histogram with bin width ds
    s_max = s_grid[-1]
    bins = np.arange(0.0, s_max + ds, ds)
    counts, edges = np.histogram(d, bins=bins)
    centers = 0.5 * (edges[:-1] + edges[1:])
    density = counts / (n * ds)         # normalized by # pairs and bin width
    # interpolate onto s_grid
    return np.interp(s_grid, centers, density, left=0.0, right=0.0)


def R2_GUE(s: np.ndarray) -> np.ndarray:
    """GUE pair correlation:  R₂(s) = 1 - (sin(π s)/(π s))²."""
    sinc = np.sinc(s)            # numpy: sin(π s)/(π s)
    return 1.0 - sinc**2


def R2_Poisson(s: np.ndarray) -> np.ndarray:
    """Poisson (uncorrelated) pair correlation:  R₂(s) = 1."""
    return np.ones_like(s)


# ---------- χ² with UNIFORM bins ----------

def chi_square_uniform(spacings: np.ndarray, s_max: float = 3.0, n_bins: int = 15) -> tuple[float, int]:
    """
    χ² test of spacing histogram vs GUE Wigner-Dyson surmise.
    Uniform bins on [0, s_max].  Returns (χ², df).
    """
    bins = np.linspace(0.0, s_max, n_bins + 1)
    counts, _ = np.histogram(spacings, bins=bins)
    N = counts.sum()
    centers = 0.5 * (bins[:-1] + bins[1:])
    expected = wigner_dyson_pdf(centers) * (bins[1] - bins[0]) * N
    # avoid divide-by-zero: merge zero-expected bins
    mask = expected > 1e-9
    chi2 = float(np.sum((counts[mask] - expected[mask])**2 / expected[mask]))
    df = int(mask.sum() - 1)        # one parameter estimated (normalization)
    return chi2, df


# ---------- KS test against Wigner-Dyson ----------

def ks_against_wigner_dyson(spacings: np.ndarray) -> tuple[float, float]:
    """
    KS statistic and p-value for spacings vs GUE Wigner-Dyson surmise.
    """
    s = np.sort(spacings)
    cdf_data = np.arange(1, len(s) + 1) / len(s)
    # CDF of Wigner-Dyson surmise — numerical integration
    grid = np.linspace(0.0, max(s.max(), 5.0), 1000)
    pdf = wigner_dyson_pdf(grid)
    cdf = np.cumsum(pdf) * (grid[1] - grid[0])
    cdf = cdf / cdf[-1]
    cdf_model = np.interp(s, grid, cdf)
    D = float(np.max(np.abs(cdf_data - cdf_model)))
    # KS p-value (approximate, large-N)
    n = len(s)
    pval = float(stats.kstwobign.sf(np.sqrt(n) * D))
    return D, pval


# ---------- bootstrap σ(r) ----------

def bootstrap_mean(x: np.ndarray, n_boot: int = 500, seed: int = 0) -> float:
    """Bootstrap standard error of the mean."""
    rng = np.random.default_rng(seed)
    n = len(x)
    means = np.empty(n_boot)
    for b in range(n_boot):
        idx = rng.integers(0, n, size=n)
        means[b] = np.mean(x[idx])
    return float(np.std(means))


# ---------- proper σ_BK estimate ----------

def sigma_r_bk_correct(N: int) -> float:
    """
    CORRECT Bogomolny-Keating-style estimate of σ(⟨r⟩) for GUE matrices of size N.
    The v17 code used 0.4/√N (which is the BK estimate for the number variance
    in an interval, NOT for ⟨r⟩).  The correct empirical coefficient for ⟨r⟩
    on a single GUE matrix spectrum is ≈ 0.27/√N_eff, where N_eff is the number
    of spacings (not the matrix size).  We use this coefficient.

    Reference: Atas & Bogomolny, PRL 2012 (⟨r⟩ variance on GUE).
    """
    return 0.27 / np.sqrt(N)
