"""
abcloud.core — computational core of the Python reimplementation of the
AB-Cloud v23 SUPERCOMBO verification suite.

This module provides the numerical primitives shared by all 38 tests:

* Riemann zeta zeros (mpmath) with on-disk caching;
* Riemann–Siegel theta function and Gram points;
* Random-matrix reference laws (Wigner surmises for GUE/GOE/Poisson,
  exact mean adjacent-gap ratios from Atas et al. 2013);
* Statistical estimators: one- and two-sample Kolmogorov–Smirnov tests,
  Anderson–Darling (with Monte-Carlo calibration), chi-square binned
  comparison, bootstrap confidence intervals, number variance Σ²(L),
  spectral rigidity Δ₃(L), spectral form factor K(t);
* The Aharonov–Bohm (AB) lattice Hamiltonian: an L×L square lattice with a
  uniform flux α per plaquette (Landau gauge), optional vortex fluxes ±2πq
  threaded through Nv plaquettes (Dirac strings), and optional diagonal
  disorder W;
* Byte-level quantization diagnostics used by Test 36.

Equivalence note.  The clone reproduces the *semantics* of every Julia test
(same statistic, same acceptance windows, same verdict algebra, same report
structure).  Bit-exact numeric agreement with the Julia run is neither
expected nor required: Julia and Python use different PRNG streams and
different BLAS backends.  Every place where a clone-specific convention had
to be chosen is marked with "CLONE-CONVENTION" in the docstrings.

The reference constants below follow the Julia original (lines 3398-3400 and
3624 of ab_cloud_v23_v3.jl): R_MEAN_POISSON, R_MEAN_GOE, R_MEAN_GUE,
R_MEAN_GSE.  Test 27 uses R_MEAN_POISSON (the v3.1 patch fixes the
`R_POISSON` UndefVarError of the unpatched v3 build).
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Sequence

import numpy as np

# ----------------------------------------------------------------------------
# Reference constants (identical to the Julia suite)
# ----------------------------------------------------------------------------

R_MEAN_POISSON = 2.0 * np.log(2.0) - 1.0   # ≈ 0.38629  (Atas et al. 2013)
R_MEAN_GOE = 0.5307                        #            (Atas et al. 2013)
R_MEAN_GUE = 0.59960                       #            (Atas et al. 2013)
R_MEAN_GSE = 0.67620                       #            (Atas et al. 2013)

# Reference run configuration (FINAL_REPORT/final_report.md, end-of-run values)
REFERENCE_RUN = {
    "zeros_count": 50000,
    "lattice_primary": (72, 72),
    "lattice_secondary": (96, 96),
    "alpha": 0.5,
    "ab_W": 4.0,
    "ab_W_max": 1.0,
    "n_realizations": 5,
    "seed": 12345,
    "julia": "1.12.0",
    "wall_seconds": 93748.1,
}

DEFAULT_CACHE_DIR = Path(
    os.environ.get("ABCLOUD_CACHE", Path.home() / ".cache" / "abcloud")
)


# ----------------------------------------------------------------------------
# Zeta zeros and Gram points
# ----------------------------------------------------------------------------

_EMBEDDED_ZEROS_FILE = Path(__file__).parent / "data" / "zeta_zeros_50000.txt"
_EMBEDDED_CACHE: dict[int, np.ndarray] = {}


def zeta_zeros(n: int, cache_dir: Path | None = None) -> np.ndarray:
    """First n positive imaginary parts γ_k of the Riemann zeta zeros.

    Primary source: the embedded 50,000-zero dataset shipped with the clone
    (extracted verbatim from the Julia original's EMBEDDED_ZEROS_50K_STR,
    ab_cloud_v23_v3.jl line 4679) — the clone therefore validates the SAME
    dataset as the reference run.  Only for n > 50,000 does it fall back to
    computing further zeros with mpmath (cached in ~/.cache/abcloud).
    """
    if n <= 0:
        return np.zeros(0)
    if n in _EMBEDDED_CACHE:
        return _EMBEDDED_CACHE[n][:n]
    if _EMBEDDED_ZEROS_FILE.exists():
        emb = np.loadtxt(_EMBEDDED_ZEROS_FILE, dtype=np.float64).ravel()
        _EMBEDDED_CACHE[len(emb)] = emb
        if n <= len(emb):
            return emb[:n]
    # fallback (n > 50000): mpmath with on-disk cache
    from mpmath import zetazero

    cache_dir = Path(cache_dir or DEFAULT_CACHE_DIR)
    cache_dir.mkdir(parents=True, exist_ok=True)
    cache = cache_dir / f"zeta_zeros_{n}.npy"
    if cache.exists():
        return np.load(cache)
    out = np.empty(n, dtype=np.float64)
    base = zeta_zeros(min(n, 50000))
    out[: len(base)] = base
    step = 200
    for start in range(len(base), n, step):
        end = min(start + step, n)
        out[start:end] = [float(zetazero(k + 1).imag) for k in range(start, end)]
    np.save(cache, out)
    return out


def riemann_siegel_theta(t):
    """Riemann–Siegel theta θ(t) = Im ln Γ(¼ + it/2) − (t/2)·ln π.

    Log-Gamma asymptotic with Bernoulli corrections; accurate to ≲1e-12 for
    t ≳ 8 (covers every Gram point of the suite, γ̃₀ ≈ 17.85).
    """
    t = np.asarray(t, dtype=np.float64)
    x = 0.25
    y = t / 2.0
    r2 = x * x + y * y
    r = np.sqrt(r2)
    arg = np.arctan2(y, x)
    # Im ln Γ(x+iy) = (x−½)·arg + y·ln r − y + Im(Σ B_{2k}/(2k(2k−1) z^{2k−1}))
    im_lg = (x - 0.5) * arg + y * np.log(r) - y
    # corrections: Σ_k B_{2k}/(2k(2k−1)) · Im(1/z^{2k−1}) with B2 = 1/6,
    # B4 = −1/30, B6 = 1/42  →  coefficients 1/12, −1/360, 1/1260:
    #   Im(1/z)   = −y/r²
    #   Im(1/z³)  = −(3x²y − y³)/r⁶
    #   Im(1/z⁵)  = (−5x⁴y + 10x²y³ − y⁵)/r⁸
    corr = (-(y / r2) / 12.0
            + (3 * x ** 2 * y - y ** 3) / r2 ** 3 / 360.0
            + (-5 * x ** 4 * y + 10 * x ** 2 * y ** 3 - y ** 5) / r2 ** 4 / 1260.0)
    theta = -(t / 2.0) * np.log(np.pi) + im_lg + corr
    return theta


def gram_points(n: int) -> np.ndarray:
    """First n Gram points γ̃ solving θ(γ̃) = kπ for k = 0..n−1.

    CLONE-CONVENTION: Newton refinement on a dense grid (monotone θ/π for
    t > 8); accuracy ≈ 1e-11 at ~1e4× lower cost than per-point root finding.
    """
    if n <= 0:
        return np.zeros(0)
    t_max = 2.0 * np.pi * n / max(np.log(max(n, 3)) + 1.0, 1.0) * 1.9 + 120.0
    m = int(max(60 * n, 40000))
    grid = np.linspace(6.0, t_max, m)
    vals = riemann_siegel_theta(grid) / np.pi
    target = np.arange(n, dtype=np.float64)
    idx = np.clip(np.searchsorted(vals, target) - 1, 0, m - 2)
    t = grid[idx].copy()
    for _ in range(10):
        f = riemann_siegel_theta(t) / np.pi - target
        h = 1e-6 * np.maximum(t, 10.0)
        fp = (riemann_siegel_theta(t + h) / np.pi
              - riemann_siegel_theta(t - h) / np.pi) / (2.0 * h)
        t = np.maximum(t - f / fp, 6.0)
    return t


def b_statistic(gammas, grams) -> float:
    """b(N) = (1/N) Σ|γ_k − γ̃_k| — mean absolute Gram-point deviation.

    Pairing convention (validated against the Julia reference run): γ_k (the
    k-th zero, γ₁ = 14.1347) is paired with the k-th Gram point γ̃_k = g_k
    (g₁ = 23.1703, i.e. the array of Gram points EXCLUDING g₀ = 17.8456).
    Peak deviation |γ₁ − g₁| = 9.0356 matches the Julia H6 audit exactly;
    with this convention b(50000) = 1.2128 vs the Julia reference 1.2126
    (difference = Gram-point interpolation accuracy).
    """
    g = np.asarray(gammas, dtype=np.float64)
    gp = np.asarray(grams, dtype=np.float64)
    n = min(len(g), len(gp))
    return float(np.mean(np.abs(g[:n] - gp[:n])))


# ----------------------------------------------------------------------------
# Random-matrix spacing laws
# ----------------------------------------------------------------------------

def wigner_surmise_gue(s):
    """GUE Wigner surmise p(s) = (32/π²) s² exp(−4s²/π), unit mean."""
    s = np.asarray(s, dtype=np.float64)
    return (32.0 / np.pi ** 2) * s ** 2 * np.exp(-4.0 * s ** 2 / np.pi)


def wigner_surmise_goe(s):
    """GOE Wigner surmise p(s) = (π/2) s exp(−π s²/4), unit mean."""
    s = np.asarray(s, dtype=np.float64)
    return (np.pi / 2.0) * s * np.exp(-np.pi * s ** 2 / 4.0)


def goe_cdf(s):
    """GOE surmise CDF: 1 − exp(−π s²/4)."""
    s = np.asarray(s, dtype=np.float64)
    return 1.0 - np.exp(-np.pi * s ** 2 / 4.0)


def poisson_spacing(s):
    """Poisson (uncorrelated) spacing law p(s) = exp(−s)."""
    return np.exp(-np.asarray(s, dtype=np.float64))


def normalized_spacings(levels):
    """Mean-spacing-normalized nearest-neighbour spacings of a sorted list.

    CLONE-CONVENTION: s_i = δ_i / mean(δ), the same normalization the Julia
    suite documents for its KS/AD/χ² tests.
    """
    z = np.sort(np.asarray(levels, dtype=np.float64))
    d = np.diff(z)
    d = d[d > 0]
    if len(d) == 0:
        return np.zeros(0)
    return d / float(np.mean(d))


def mean_adjacent_spacing_ratio(levels):
    """Honest Oganesyan–Huse ⟨r⟩ over consecutive raw gaps (unfolding-free)."""
    z = np.sort(np.asarray(levels, dtype=np.float64))
    d = np.diff(z)
    d = d[d > 0]
    if len(d) < 2:
        return float("nan"), 0
    r = np.minimum(d[:-1], d[1:]) / np.maximum(d[:-1], d[1:])
    return float(np.mean(r)), len(r)


# ----------------------------------------------------------------------------
# Statistical tests
# ----------------------------------------------------------------------------

def ks_test(spacings):
    """One-sample KS test of spacings against the GUE surmise → (D, p).
    NOTE: scipy.kstest requires a CDF callable, not a density."""
    from scipy import stats

    s = np.asarray(spacings, dtype=np.float64)
    if len(s) < 2:
        return float("nan"), float("nan")
    res = stats.kstest(s, gue_cdf_values)
    return float(res.statistic), float(res.pvalue)


def ks_test_law(spacings, cdf):
    """One-sample KS test against an arbitrary law (CDF callable) → (D, p)."""
    from scipy import stats

    s = np.asarray(spacings, dtype=np.float64)
    res = stats.kstest(s, cdf)
    return float(res.statistic), float(res.pvalue)


def ks_two_sample(a, b):
    from scipy import stats

    res = stats.ks_2samp(np.asarray(a, dtype=np.float64),
                         np.asarray(b, dtype=np.float64))
    return float(res.statistic), float(res.pvalue)


_GUE_CDF = None  # (x_grid, cdf_grid)


def gue_random_matrix_eigs(n: int, rng: np.random.Generator) -> np.ndarray:
    """Eigenvalues of an n×n GUE matrix H = (A + A†)/2, A ~ complex Ginibre.
    Used by Test 12 as the GUE-matrix reference spectrum."""
    A = (rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))) / np.sqrt(2.0)
    H = (A + A.conj().T) / 2.0
    from scipy.linalg import eigvalsh

    return eigvalsh(H, check_finite=False)


def _gue_cdf():
    global _GUE_CDF
    if _GUE_CDF is None:
        from scipy.integrate import cumulative_trapezoid

        x = np.linspace(0.0, 9.0, 400001)
        cdf = cumulative_trapezoid(wigner_surmise_gue(x), x, initial=0.0)
        _GUE_CDF = (x, cdf)
    return _GUE_CDF


def gue_cdf_values(s):
    x, cdf = _gue_cdf()
    return np.interp(s, x, cdf)


def gue_surmise_sample(n: int, rng: np.random.Generator) -> np.ndarray:
    """Inverse-CDF sample from the GUE surmise (grid-interpolated)."""
    x, cdf = _gue_cdf()
    u = rng.uniform(1e-9, 1 - 1e-9, size=n)
    return np.interp(u, cdf, x)


def anderson_darling_stat(spacings) -> float:
    """A² statistic for spacings vs the GUE surmise (numerical CDF)."""
    s = np.sort(np.asarray(spacings, dtype=np.float64))
    n = len(s)
    if n < 8:
        return float("nan")
    u = np.clip(gue_cdf_values(s), 1e-12, 1.0 - 1e-12)
    i = np.arange(1, n + 1)
    a2 = -n - np.mean((2.0 * i - 1.0) * (np.log(u) + np.log1p(-u[::-1])))
    return float(a2)


def ad_monte_carlo_p(a2_obs: float, n: int, n_mc: int = 2000,
                     seed: int = 12345) -> float:
    """MC p-value of A² vs the GUE surmise (vectorized)."""
    rng = np.random.default_rng(seed)
    u = rng.uniform(1e-9, 1 - 1e-9, size=(n_mc, n))
    x, cdf = _gue_cdf()
    s = np.interp(u, cdf, x)
    s.sort(axis=1)
    uu = np.clip(np.interp(s, x, cdf), 1e-12, 1 - 1e-12)
    i = np.arange(1, n + 1)
    a2s = (-n - np.mean((2.0 * i - 1.0)
                        * (np.log(uu) + np.log1p(-uu[:, ::-1])), axis=1))
    return float(np.mean(a2s >= a2_obs))


def chi2_binned(spacings, n_bins: int = 50, s_max: float = 3.5):
    """χ² of a spacing histogram vs the GUE surmise → (χ², dof, p, obs)."""
    from scipy import stats as st

    s = np.asarray(spacings, dtype=np.float64)
    s = s[s <= s_max]
    edges = np.linspace(0.0, s_max, n_bins + 1)
    obs, _ = np.histogram(s, bins=edges)
    n = float(len(s))
    x, cdf = _gue_cdf()
    cdf_edges = np.interp(edges, x, cdf)
    exp = n * np.diff(cdf_edges)
    mask = exp > 5.0
    chi2 = float(np.sum((obs[mask] - exp[mask]) ** 2 / exp[mask]))
    dof = int(mask.sum()) - 1
    p = float(st.chi2.sf(chi2, dof)) if dof > 0 else float("nan")
    return chi2, dof, p, obs


def bootstrap_ci(values, stat: Callable = np.mean, n_boot: int = 2000,
                 alpha: float = 0.05, seed: int = 12345):
    """Percentile bootstrap CI for `stat` over resamples of `values`."""
    rng = np.random.default_rng(seed)
    v = np.asarray(values, dtype=np.float64)
    n = len(v)
    stats_ = np.empty(n_boot)
    for b in range(n_boot):
        idx = rng.integers(0, n, size=n)
        stats_[b] = stat(v[idx])
    lo, hi = np.percentile(stats_, [100 * alpha / 2, 100 * (1 - alpha / 2)])
    return float(stat(v)), float(lo), float(hi)


def number_variance_curve(levels, l_values):
    """Number variance Σ²(L) on the unfolded scale (unit mean spacing).

    CLONE-CONVENTION: disjoint (non-overlapping) windows — the spectrum is
    split into floor(M/L) consecutive windows of unfolded length L and Σ² is
    the variance of their level counts (standard RMT estimator)."""
    z = np.asarray(levels, dtype=np.float64)
    g = np.diff(z)
    g = g[g > 0]
    g = g / np.mean(g)
    cs = np.concatenate([[0.0], np.cumsum(g)])
    M = len(cs) - 1
    out = []
    for L in l_values:
        if L < 2 or L >= M:
            out.append(np.nan)
            continue
        n_win = int(M // L)
        if n_win < 2:
            out.append(np.nan)
            continue
        bounds = cs[0:n_win * L + 1:L]
        counts = np.searchsorted(cs, bounds, side="left")[1:] \
            - np.searchsorted(cs, bounds, side="left")[:-1]
        out.append(float(np.var(counts)))
    return np.asarray(l_values, dtype=np.float64), np.asarray(out)


def sigma2_gue_reference(L):
    """GUE number variance Σ²(L) ≈ (1/π²)(ln(2πL) + γ + 1)."""
    L = np.asarray(L, dtype=np.float64)
    return (np.log(2 * np.pi * L) + np.euler_gamma + 1.0) / (np.pi ** 2)


def sigma2_poisson_reference(L):
    """Poisson number variance Σ²(L) = L."""
    return np.asarray(L, dtype=np.float64)


def spectral_rigidity_curve(levels, l_values, n_win_max: int = 400,
                            seed: int = 12345):
    """Spectral rigidity Δ₃(L): mean least-squares deviation of the staircase
    from the best straight line over windows of unfolded length L."""
    z = np.asarray(levels, dtype=np.float64)
    g = np.diff(z)
    g = g[g > 0]
    g = g / np.mean(g)
    cs = np.concatenate([[0.0], np.cumsum(g)])
    M = len(cs) - 1
    rng = np.random.default_rng(seed)
    out = []
    for L in l_values:
        if L < 2 or L >= M:
            out.append(np.nan)
            continue
        n_win = int(min(n_win_max, max(30, M // L)))
        starts = rng.integers(0, M - L, size=n_win)
        devs = np.empty(n_win)
        for w, a in enumerate(starts):
            seg = cs[a:a + L + 1]
            y = seg - seg[0]
            x = np.arange(len(y), dtype=np.float64)
            slope = np.polyfit(x, y, 1)
            devs[w] = float(np.mean((y - np.polyval(slope, x)) ** 2))
        out.append(float(np.mean(devs)))
    return np.asarray(l_values, dtype=np.float64), np.asarray(out)


def delta3_gue_reference(L):
    """Asymptotic GUE rigidity Δ₃^GUE(L) ≈ (1/π²)(ln 2πL + γ − 5/4 − π²/8)."""
    L = np.asarray(L, dtype=np.float64)
    return (np.log(2 * np.pi * L) + np.euler_gamma - 1.25
            - (np.pi ** 2) / 8.0) / (np.pi ** 2)


def delta3_poisson_reference(L):
    """Poisson rigidity Δ₃^Poisson(L) = L/15."""
    return np.asarray(L, dtype=np.float64) / 15.0


def spectral_form_factor(levels, n_tau: int = 120, t_max: float = 3.0,
                         n_blocks: int = 50):
    """Spectral form factor K(t) of the unfolded level sequence.

    CLONE-CONVENTION: unfolded coordinate s with unit mean spacing (t in
    units of the mean level spacing), K(t) = |Σ_k e^{2πi t s_k}|²/n_block,
    averaged over `n_blocks` energy blocks of the sequence and smoothed over
    the t-grid (block + window averaging is what makes a single finite
    sequence's K(t) converge to the ramp-plateau shape)."""
    z = np.asarray(levels, dtype=np.float64)
    g = np.diff(z)
    g = g[g > 0]
    g = g / np.mean(g)
    s = np.concatenate([[0.0], np.cumsum(g)])
    n = len(s)
    n_blocks = max(2, min(n_blocks, n // 50))
    block_len = n // n_blocks
    taus = np.linspace(0.05, t_max, n_tau)
    K_acc = np.zeros(n_tau)
    for b in range(n_blocks):
        sb = s[b * block_len:(b + 1) * block_len]
        sb = sb - sb[0]
        for i, t in enumerate(taus):
            K_acc[i] += np.abs(np.sum(np.exp(2j * np.pi * t * sb))) ** 2 / len(sb)
    K = K_acc / n_blocks
    # smooth over the t-grid (window 7)
    kernel = np.ones(7) / 7.0
    K = np.convolve(K, kernel, mode="same")
    K[:2] = K[2]
    K[-2:] = K[-3]
    return taus, K


def k_gue_reference(t):
    """GUE ramp-plateau reference K(t): 2t on [0,1], 1 above."""
    t = np.asarray(t, dtype=np.float64)
    return np.where(t <= 1.0, 2.0 * t, 1.0)


# ----------------------------------------------------------------------------
# AB-lattice Hamiltonian
# ----------------------------------------------------------------------------

@dataclass
class ABConfig:
    """Configuration of the AB-lattice suite (mirrors the Julia Config)."""
    L: int = 24                      # linear lattice size (primary pass)
    L_secondary: int = 32            # linear size (secondary HARDCORE pass)
    alpha: float = 0.5               # uniform AB flux per plaquette
    W: float = 4.0                   # on-site disorder width (Julia ab_W=4)
    Nv: int = 0                      # number of vortex fluxes
    q: float = 1.0                   # vortex charge
    n_realizations: int = 5
    seed: int = 12345
    fast: bool = True                # clone fast mode (reduced sizes)
    zeros: int = 2000                # number of zeta zeros

    def W_eff(self) -> float:
        return min(self.W, REFERENCE_RUN["ab_W_max"])


def ab_lattice_hamiltonian(L: int, alpha: float = 0.5, W: float = 0.0,
                           Nv: int = 0, q: float = 1.0,
                           rng: np.random.Generator | None = None,
                           pbc: bool = True):
    """Build the L×L Aharonov–Bohm lattice Hamiltonian (dense, Hermitian).

    Construction (clone convention, following the documented v23 design):
    * L×L square lattice, periodic boundaries;
    * uniform AB flux α per plaquette via Landau gauge: horizontal link
      (x,y)→(x+1,y) carries phase exp(2πi·α·y); vertical links carry 1;
    * Nv vortex fluxes of charge ±q threaded through Nv plaquettes by adding
      ±q·2π to the vertical bond of the vortex plaquette (integer q is
      Byers–Yang invisible to the spectrum; the gauge twist is exact);
    * diagonal disorder W: i.i.d. uniform [−W/2, W/2] on sites.

    Returns (H, flux) with flux the L×L array of plaquette fluxes in 2π units.
    """
    n = L * L
    rng = rng or np.random.default_rng(12345)
    H = np.zeros((n, n), dtype=np.complex128)

    def idx(x: int, y: int) -> int:
        return (x % L) * L + (y % L)

    # vortex placement: random cells, alternating charges, shared RNG stream
    vortex_cells = []
    if Nv > 0:
        cells = [(x, y) for x in range(L) for y in range(L)]
        chosen = rng.choice(len(cells), size=Nv, replace=False)
        vortex_cells = [cells[int(c)] for c in chosen]
    vortex_flux = {c: (q if k % 2 == 0 else -q)
                   for k, c in enumerate(vortex_cells)}

    flux = np.full((L, L), alpha, dtype=np.float64)
    for c, chg in vortex_flux.items():
        flux[c[0], c[1]] += chg

    for x in range(L):
        for y in range(L):
            i = idx(x, y)
            # horizontal link with Landau-gauge phase
            phi_h = 2.0 * np.pi * alpha * y
            j = idx(x + 1, y)
            H[i, j] += np.exp(1j * phi_h)
            H[j, i] += np.exp(-1j * phi_h)
            # vertical link; vortex inside plaquette (x,y) twists this bond by
            # the full charge flux 2π·q·charge (peel-off gauge)
            phi_v = 0.0
            if (x, y) in vortex_flux:
                phi_v += 2.0 * np.pi * vortex_flux[(x, y)]
            j2 = idx(x, y + 1)
            H[i, j2] += np.exp(1j * phi_v)
            H[j2, i] += np.exp(-1j * phi_v)

    if W > 0:
        diag = rng.uniform(-W / 2.0, W / 2.0, size=n)
        H[np.arange(n), np.arange(n)] += diag.astype(np.complex128)

    # Expected unwrapped plaquette flux map (Dirac-string gauge of this
    # construction): the vortex bond carries ±2πq, so the vortex plaquette
    # sees +q·charge and its LEFT neighbour sees −q·charge (the flux line
    # exits through the shared bond — net flux zero on the torus, as required
    # by periodic boundary conditions / Gauss law).
    for (vx, vy), chg in vortex_flux.items():
        flux[vx, vy] += chg
        flux[(vx - 1) % L, vy] -= chg

    return H, flux


def ab_spectrum(cfg: ABConfig, L=None, W=None, Nv=None, seed=None,
                central_fraction: float = 0.6, full: bool = False) -> dict:
    """Diagonalize the AB lattice; return full/central spectrum + diagnostics."""
    L = int(L or cfg.L)
    W = cfg.W if W is None else W
    Nv = cfg.Nv if Nv is None else Nv
    seed = cfg.seed if seed is None else seed
    rng = np.random.default_rng(seed)
    H, flux = ab_lattice_hamiltonian(L, cfg.alpha, W, Nv, cfg.q, rng)
    from scipy.linalg import eigvalsh

    ev = eigvalsh(H, check_finite=False)
    n = len(ev)
    drop = int(round(n * (1.0 - central_fraction) / 2.0))
    central = ev[drop:n - drop]
    return {
        "eigs": ev if full else ev,
        "central": central,
        "flux": flux,
        "herm_defect": float(np.max(np.abs(H - H.conj().T))),
        "L": L,
        "W": float(W),
        "Nv": int(Nv),
        "seed": int(seed),
    }


def plaquette_flux_check(H: np.ndarray, L: int) -> np.ndarray:
    """Extract plaquette phases from the built Hamiltonian via the loop
    product P = H[i,j]·H[j,k]·H[k,l]·H[l,i] — gauge-covariant and wrap-proof
    (a single final np.angle on the product, never per-bond)."""
    n = L * L

    def idx(x, y):
        return (x % L) * L + (y % L)

    flux = np.zeros((L, L))
    for x in range(L):
        for y in range(L):
            i, j = idx(x, y), idx(x + 1, y)
            k, l = idx(x + 1, y + 1), idx(x, y + 1)
            P = H[i, j] * H[j, k] * np.conj(H[l, k]) * np.conj(H[i, l])
            flux[x, y] = np.angle(P) / (2 * np.pi)
    return flux


def byte_quantize_r(window, n_levels: int = 256) -> float:
    """Byte-quantized ⟨r⟩ over a window (Test 36 estimator)."""
    w = np.sort(np.asarray(window, dtype=np.float64))
    if len(w) < 3:
        return float("nan")
    lo, hi = w[0], w[-1]
    span = hi - lo
    if span <= 0:
        return float("nan")
    qb = np.round((w - lo) / span * (n_levels - 1))
    d = np.diff(qb)
    d = d[d > 0]
    if len(d) < 2:
        return float("nan")
    r = np.minimum(d[:-1], d[1:]) / np.maximum(d[:-1], d[1:])
    return float(np.mean(r))


def shannon_entropy_bits(counts) -> float:
    c = np.asarray(counts, dtype=np.float64)
    n = c.sum()
    if n <= 0:
        return 0.0
    p = c[c > 0] / n
    return float(-(p * np.log2(p)).sum())


# ----------------------------------------------------------------------------
# Small utilities shared by tests
# ----------------------------------------------------------------------------

def runs_test_signs(residuals):
    """Wald–Wolfowitz runs count of the residual sign sequence → (runs, E[runs])."""
    r = np.asarray(residuals, dtype=np.float64)
    signs = np.sign(r)
    signs = signs[signs != 0]
    if len(signs) == 0:
        return 0, float("nan")
    runs = 1 + int(np.sum(signs[1:] != signs[:-1]))
    n1 = int(np.sum(signs > 0))
    n2 = int(np.sum(signs < 0))
    n = n1 + n2
    if n1 == 0 or n2 == 0:
        return runs, float("nan")
    return runs, float(2.0 * n1 * n2 / n + 1.0)


def linreg(x, y):
    """OLS y = a + b·x → (a, b, R², se(b))."""
    x = np.asarray(x, dtype=np.float64)
    y = np.asarray(y, dtype=np.float64)
    A = np.vstack([x, np.ones_like(x)]).T
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    b, a = float(coef[0]), float(coef[1])
    yhat = A @ coef
    ss_res = float(np.sum((y - yhat) ** 2))
    ss_tot = float(np.sum((y - np.mean(y)) ** 2))
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else float("nan")
    dof = max(len(x) - 2, 1)
    se_b = float(np.sqrt(ss_res / dof / max(np.sum((x - np.mean(x)) ** 2), 1e-30)))
    return a, b, r2, se_b


def verdict(ok: bool) -> str:
    return "PASS" if ok else "FAIL"


def safe_json(obj) -> str:
    def default(o):
        if isinstance(o, (np.floating, np.integer)):
            return float(o)
        if isinstance(o, np.ndarray):
            return o.tolist()
        if isinstance(o, Path):
            return str(o)
        return str(o)

    return json.dumps(obj, indent=1, default=default, ensure_ascii=False)
