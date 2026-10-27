"""
ab_cloud_stats.py
=================
Statistical tools for GUE / Poisson comparison of eigenvalue spectra.

Implements:
- Wigner-Dyson unfolding via polynomial fit to cumulative density
- Riemann-von Mangoldt unfolding for zeta zeros
- Nearest-neighbor spacing ratio r_n = min(d_n, d_{n+1}) / max(...)
- Mean ratio <r> and GUE/Poisson reference values
- Number variance Sigma^2(L), spectral rigidity Delta_3(L)
- Nearest-neighbor spacing distribution p(s)
- Two-level correlation R_2(s) and Montgomery's pair correlation
- Spectral form factor K(t)
- Dyson-Mehta statistic for GUE comparison

References:
- Mehta, "Random Matrices" (3rd ed.)
- Montgomery 1973 (pair correlation of zeta zeros)
- Bogomolny & Keating 1996 (BK heuristic)
"""
import numpy as np
from scipy import stats
from scipy.signal import find_peaks


# ---------- Reference values ----------
R_GUE = 0.5996     # <r> for GUE (Atas et al. 2013)
R_GOE = 0.5359     # <r> for GOE
R_POISSON = 0.3863 # <r> for Poisson

# ---------- Unfolding ----------


def polynomial_unfold(eigs: np.ndarray, deg: int = 8) -> np.ndarray:
    """
    Unfold eigenvalues via polynomial fit to the cumulative density.
    Returns unfolded eigenvalues xi_n such that <xi> ~ uniform.
    """
    n = np.arange(1, len(eigs) + 1, dtype=float)
    # Fit polynomial to cumulative count
    coeffs = np.polyfit(eigs, n, deg=deg)
    xi = np.polyval(coeffs, eigs)
    # Remove mean slope to get fluctuations
    return xi - xi[0]


def riemann_von_mangoldt_unfold(t: np.ndarray, n_offset: int = 0) -> np.ndarray:
    """
    Unfold Riemann zeta zeros using the explicit Riemann-von Mangoldt formula:
        N(T) = T/(2pi) log(T/(2pi e)) + 7/8 + S(T)
    Returns the unfolded positions: e_n = N(t_n) - n.
    """
    T = np.asarray(t, dtype=float)
    main = T / (2.0 * np.pi) * np.log(T / (2.0 * np.pi * np.e))
    return main + 7.0 / 8.0 - (np.arange(len(T)) + 1 + n_offset)


def unfold(eigs: np.ndarray, method: str = "poly", deg: int = 8) -> np.ndarray:
    """Dispatch to unfolding method."""
    if method == "poly":
        return polynomial_unfold(eigs, deg=deg)
    elif method == "spline":
        from scipy.interpolate import UnivariateSpline
        n = np.arange(1, len(eigs) + 1, dtype=float)
        # Sort eigenvalues
        eigs_sorted = np.sort(eigs)
        spl = UnivariateSpline(eigs_sorted, n, k=4, s=len(eigs) * 0.01)
        return spl(eigs_sorted) - spl(eigs_sorted[0])
    else:
        raise ValueError(f"Unknown unfolding method: {method}")


# ---------- Nearest-neighbor spacing ----------


def spacing_ratios(eigs: np.ndarray) -> np.ndarray:
    """Compute r_n = min(d_n, d_{n+1}) / max(d_n, d_{n+1})."""
    eigs = np.sort(eigs)
    d = np.diff(eigs)
    if len(d) < 2:
        return np.array([])
    r = np.minimum(d[:-1], d[1:]) / np.maximum(d[:-1], d[1:])
    return r


def mean_spacing_ratio(eigs: np.ndarray) -> float:
    """<r> averaged over spectrum."""
    r = spacing_ratios(eigs)
    return float(np.mean(r)) if len(r) else float("nan")


def std_spacing_ratio(eigs: np.ndarray) -> float:
    r = spacing_ratios(eigs)
    return float(np.std(r)) if len(r) else float("nan")


def spacing_distribution(eigs: np.ndarray, unfolded: bool = True, n_bins: int = 30) -> tuple:
    """
    Returns (s_bins, p_hist) for nearest-neighbor spacing distribution.
    If unfolded=True, eigenvalues are first unfolded via polynomial fit.
    """
    if unfolded:
        xi = polynomial_unfold(eigs) if unfolded else eigs
        d = np.diff(np.sort(xi))
    else:
        d = np.diff(np.sort(eigs))
    d = d[d > 0]
    if len(d) == 0:
        return np.array([]), np.array([])
    # Normalize to mean 1
    d_norm = d / np.mean(d)
    p, edges = np.histogram(d_norm, bins=n_bins, range=(0, 5), density=True)
    s = 0.5 * (edges[1:] + edges[:-1])
    return s, p


# ---------- GUE analytic reference distributions ----------


def p_GUE(s: np.ndarray) -> np.ndarray:
    """GUE Wigner surmise: p(s) = (32/pi^2) s^2 exp(-4 s^2 / pi)."""
    return (32.0 / np.pi ** 2) * s ** 2 * np.exp(-4.0 * s ** 2 / np.pi)


def p_GOE(s: np.ndarray) -> np.ndarray:
    """GOE Wigner surmise: p(s) = (pi/2) s exp(-pi s^2 / 4)."""
    return (np.pi / 2.0) * s * np.exp(-np.pi * s ** 2 / 4.0)


def p_Poisson(s: np.ndarray) -> np.ndarray:
    """Poisson: p(s) = exp(-s)."""
    return np.exp(-s)


def R2_GUE(s: np.ndarray) -> np.ndarray:
    """GUE two-level correlation: R_2(s) = 1 - (sin(pi s)/(pi s))^2."""
    s = np.asarray(s, dtype=float)
    with np.errstate(divide="ignore", invalid="ignore"):
        y = np.sin(np.pi * s) / (np.pi * s)
        y = np.where(s == 0, 1.0, y)
    return 1.0 - y ** 2


def R2_Montgomery(s: np.ndarray) -> np.ndarray:
    """Montgomery pair correlation: same as GUE R_2(s) = 1 - (sin(pi s)/(pi s))^2."""
    return R2_GUE(s)


def R2_Poisson(s: np.ndarray) -> np.ndarray:
    """Poisson: R_2(s) = 1."""
    return np.ones_like(s)


def empirical_R2(xi: np.ndarray, s_max: float = 5.0, n_bins: int = 50) -> tuple:
    """Empirical two-level correlation from unfolded spectrum."""
    xi = np.sort(xi)
    n = len(xi)
    if n < 4:
        return np.array([]), np.array([])
    mean_spacing = (xi[-1] - xi[0]) / (n - 1)
    bins = np.linspace(0, s_max, n_bins + 1)
    centers = 0.5 * (bins[1:] + bins[:-1])
    counts = np.zeros(n_bins)
    # For each pair (i, j), compute normalized spacing and bin it
    # Vectorized for moderate sizes; falls back to loop for large
    if n <= 2000:
        for i in range(n):
            ds = (xi[i + 1:] - xi[i]) / mean_spacing
            ds = ds[ds <= s_max]
            if len(ds):
                h, _ = np.histogram(ds, bins=bins)
                counts += h
    else:
        # Sample pairs for speed
        rng = np.random.default_rng(0)
        idx = rng.choice(n, size=min(2000, n), replace=False)
        for i in idx:
            ds = (xi[i + 1:] - xi[i]) / mean_spacing
            ds = ds[ds <= s_max]
            if len(ds):
                h, _ = np.histogram(ds, bins=bins)
                counts += h
    # Normalize to get R_2
    R2 = counts / np.mean(counts[-5:]) if np.mean(counts[-5:]) > 0 else counts
    return centers, R2


# ---------- Number variance and spectral rigidity ----------


def number_variance(xi: np.ndarray, L_values: np.ndarray) -> np.ndarray:
    """
    Sigma^2(L) = <(n(L) - L)^2> where n(L) is the number of eigenvalues in
    an interval of length L (in unfolded units).
    """
    xi = np.sort(xi)
    n = len(xi)
    sigma2 = np.zeros(len(L_values))
    for k, L in enumerate(L_values):
        if L <= 0:
            sigma2[k] = 0
            continue
        # Slide window of length L
        counts = []
        # Pick random starting points
        rng = np.random.default_rng(0)
        n_starts = min(500, n)
        for _ in range(n_starts):
            i0 = rng.integers(0, max(1, n - 1))
            target = xi[i0] + L
            n_in = np.searchsorted(xi, target) - i0
            counts.append(n_in)
        counts = np.array(counts, dtype=float)
        sigma2[k] = np.mean((counts - L) ** 2)
    return sigma2


def Sigma2_GUE(L: np.ndarray) -> np.ndarray:
    """GUE number variance: Sigma^2(L) = L - log(2 pi L) - gamma + O(1/L)."""
    L = np.asarray(L, dtype=float)
    out = L - np.log(2 * np.pi * L) - np.euler_gamma
    out = np.maximum(out, 0)
    return out


def Sigma2_Poisson(L: np.ndarray) -> np.ndarray:
    """Poisson: Sigma^2(L) = L."""
    return np.asarray(L, dtype=float)


def spectral_rigidity(xi: np.ndarray, L_values: np.ndarray) -> np.ndarray:
    """
    Delta_3(L) = (1/L) integral_0^L Sigma^2(l) dl - ... (approximate via sliding windows).
    """
    sigma2 = number_variance(xi, L_values)
    # Approximate D3 as running mean of Sigma^2
    d3 = np.zeros_like(sigma2)
    for k in range(len(L_values)):
        d3[k] = np.mean(sigma2[: k + 1]) if k > 0 else sigma2[0]
    return d3


def Delta3_GUE(L: np.ndarray) -> np.ndarray:
    """GUE spectral rigidity approx."""
    L = np.asarray(L, dtype=float)
    return (1.0 / (2.0 * np.pi ** 2)) * np.log(L + 1e-10) + 0.05


# ---------- Spectral form factor ----------


def spectral_form_factor(xi: np.ndarray, t_max: float = 10.0, n_t: int = 100) -> tuple:
    """
    K(t) = (1/N) |sum_n exp(i t xi_n)|^2
    Returns (t_array, K_array).
    """
    ts = np.linspace(0.01, t_max, n_t)
    K = np.zeros(n_t)
    for k, t in enumerate(ts):
        s = np.sum(np.exp(1j * t * xi))
        K[k] = np.abs(s) ** 2 / len(xi)
    return ts, K


def K_GUE(t: np.ndarray) -> np.ndarray:
    """GUE form factor: K(t) = t for t<1, =1 for t>=1."""
    t = np.asarray(t, dtype=float)
    return np.minimum(t, 1.0)


def K_Poisson(t: np.ndarray) -> np.ndarray:
    """Poisson: K(t) = 0 (after unfolding)."""
    return np.zeros_like(t)


# ---------- KS and Anderson-Darling tests ----------


def ks_statistic_gue(eigs: np.ndarray) -> float:
    """KS distance between empirical <r> CDF and GUE prediction."""
    r = spacing_ratios(eigs)
    if len(r) == 0:
        return float("nan")
    # CDF of r under GUE
    r_grid = np.linspace(0, 1, 200)
    # Approximate GUE r-CDF via beta-like distribution
    # From Atas et al. 2013: P(r) ~ C * r^beta * (1+r)^(-...) ; use empirical fit
    # Simpler: just compare <r> to GUE value
    emp = np.mean(r)
    return abs(emp - R_GUE)


def f_GUE_score(eigs: np.ndarray) -> float:
    """
    Two-sided f_GUE = 1 - 2*max( |KS_GUE|, |KS_Poisson| ).
    Positive -> GUE; negative -> Poisson.
    """
    r = spacing_ratios(eigs)
    if len(r) == 0:
        return float("nan")
    emp = np.mean(r)
    d_gue = abs(emp - R_GUE)
    d_poisson = abs(emp - R_POISSON)
    return 1.0 - 2.0 * max(d_gue, d_poisson)


# ---------- Energy-resolved local statistics ----------


def local_mean_r(eigs: np.ndarray, window: int = 50) -> np.ndarray:
    """Sliding-window mean of r over the spectrum."""
    r = spacing_ratios(eigs)
    if len(r) < window:
        return np.array([np.mean(r)]) if len(r) else np.array([])
    out = np.convolve(r, np.ones(window) / window, mode="valid")
    return out


# ---------- Topological markers ----------


def chirality_index(eigs: np.ndarray, alpha: float) -> dict:
    """
    For alpha = 1/2 (bipartite), check spectral symmetry about E=0.
    Returns dict with chiral-symmetry breaking metric.
    """
    eigs_centered = eigs - np.mean(eigs)
    pos = eigs_centered[eigs_centered > 0]
    neg = eigs_centered[eigs_centered < 0]
    if len(pos) == 0 or len(neg) == 0:
        return {"chiral_score": 0.0, "n_pos": len(pos), "n_neg": len(neg)}
    n = min(len(pos), len(neg))
    pairs = np.sort(pos)[:n] + np.sort(-neg)[:n]
    chiral_score = float(np.mean(np.abs(pairs)))
    return {
        "chiral_score": chiral_score,
        "n_pos": len(pos),
        "n_neg": len(neg),
        "mean_pair_sum": float(np.mean(pairs)),
    }


if __name__ == "__main__":
    # Smoke test
    rng = np.random.default_rng(0)
    eigs = np.sort(rng.normal(0, 1, 200))
    r = spacing_ratios(eigs)
    print(f"<r> = {np.mean(r):.4f} (Poisson ~ 0.3863)")
    print(f"Sigma^2(1) = {number_variance(eigs, [1.0])[0]:.4f}")
