# -*- coding: utf-8 -*-
"""GOF tests + long-range spectral statistics — 1:1 with ab_cloud_full.jl §4-5.

KS / Cramer-von Mises / Anderson-Darling / chi2 against the GUE reference
law, mean adjacent spacing ratio, unfolded positions, number variance S2(L),
spectral rigidity Delta3(L), two-level form factor K(t).
"""

from math import log, sqrt, fabs, pi, cos, sin, nan, isnan, floor
from bisect import bisect_left

from .special import ks_asymptotic_pvalue, chi2_cdf
from .rmt_table import RMT


def normalized_spacings(z):
    """delta_k * rho(t_k) with rho(t) = log(t/2pi)/2pi (strictly positive t)."""
    sp = []
    for k in range(len(z) - 1):
        if z[k] <= 0:
            continue
        sp.append((z[k + 1] - z[k]) * log(z[k] / (2 * pi)) / (2 * pi))
    return sp


class Linreg(object):
    __slots__ = ("a", "b", "R2", "se_b", "res")

    def __init__(self):
        self.a = self.b = self.R2 = 0.0
        self.se_b = nan
        self.res = []

    def __iter__(self):
        """Tuple-style unpacking: a, b, R2, se, res = linreg(x, y)."""
        return iter((self.a, self.b, self.R2, self.se_b, self.res))


def linreg(x, y):
    n = len(x)
    r = Linreg()
    if n == 0:
        return r
    mx = sum(x) / n
    my = sum(y) / n
    Sxx = sum((xi - mx) * (xi - mx) for xi in x)
    Sxy = sum((xi - mx) * (yi - my) for xi, yi in zip(x, y))
    if Sxx == 0.0 or n < 2:
        r.a = r.b = r.R2 = 0.0
        r.se_b = nan
        r.res = [0.0] * n
        return r
    r.b = Sxy / Sxx
    r.a = my - r.b * mx
    r.res = [yi - (r.a + r.b * xi) for xi, yi in zip(x, y)]
    ss_res = sum(e * e for e in r.res)
    ss_tot = sum((yi - my) * (yi - my) for yi in y)
    r.R2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else 0.0
    r.se_b = sqrt(ss_res / ((n - 2) * Sxx)) if (n > 2 and Sxx > 0) else nan
    return r


def ks_test(sp, cdf_func=None):
    n = len(sp)
    s = sorted(sp)
    cdf = cdf_func if cdf_func is not None else RMT.gue_cdf
    D = 0.0
    for i in range(1, n + 1):
        F = cdf(s[i - 1])
        D = max(D, fabs(i / n - F), fabs((i - 1) / n - F))
    lam = (sqrt(n) + 0.12 + 0.11 / sqrt(n)) * D
    return D, ks_asymptotic_pvalue(lam)


def cvm_test(sp):
    n = len(sp)
    s = sorted(sp)
    W2 = 0.0
    for i in range(1, n + 1):
        u = RMT.gue_cdf(s[i - 1])
        d = u - (2.0 * i - 1.0) / (2.0 * n)
        W2 += d * d
    return W2 + 1.0 / (12.0 * n)


def anderson_darling_stat(sp):
    n = len(sp)
    s = sorted(sp)
    acc = 0.0
    for i in range(1, n + 1):
        Fi = RMT.gue_cdf(s[i - 1])
        Fni = RMT.gue_cdf(s[n - i])
        Fi = min(max(Fi, 1e-300), 1.0 - 1e-16)
        Fni = min(max(Fni, 1e-300), 1.0 - 1e-16)
        acc += (2.0 * i - 1.0) * (log(Fi) + log(1.0 - Fni))
    return -n - acc / n


def chi2_gue_test(sp, nbins):
    s = sorted(sp)
    s_max = min(s[-1], 4.0)
    obs = [0] * nbins
    for v in s:
        if v >= s_max:
            obs[nbins - 1] += 1
        else:
            b = min(int(floor(v / s_max * nbins)) + 1, nbins)
            obs[b - 1] += 1
    N = len(s)
    edges = [s_max * i / nbins for i in range(nbins + 1)]
    chi2 = 0.0
    df = 0
    for i in range(1, nbins + 1):
        if i < nbins:
            ec = N * (RMT.gue_cdf(edges[i]) - RMT.gue_cdf(edges[i - 1]))
        else:
            ec = N * (1.0 - RMT.gue_cdf(edges[i - 1]))
        if ec < 5:
            continue
        chi2 += (obs[i - 1] - ec) * (obs[i - 1] - ec) / ec
        df += 1
    df = max(df - 1, 1)
    return chi2, df, 1.0 - chi2_cdf(chi2, df)


def mean_adjacent_spacing_ratio(eigs):
    n = len(eigs)
    if n < 3:
        return nan, 0
    s = sorted(eigs)
    d = [s[i + 1] - s[i] for i in range(n - 1)]
    if len(d) < 2:
        return nan, 0
    acc = 0.0
    cnt = 0
    for i in range(len(d) - 1):
        a, b = d[i], d[i + 1]
        if a == 0.0 and b == 0.0:
            continue
        acc += min(a, b) / max(a, b)
        cnt += 1
    if cnt <= 0:
        return nan, 0
    return acc / cnt, cnt


def _smooth_counting_function(T):
    if T <= 0.0:
        return 0.0
    x = T / (2 * pi)
    return x * log(x) - x + 7.0 / 8.0


# public name (the Julia original exports the same symbol)
smooth_counting_function = _smooth_counting_function


def unfolded_positions(z):
    return [_smooth_counting_function(t) for t in z]


def number_variance(pos, L, n_windows, rng):
    Ltot = pos[-1] - pos[0]
    if Ltot <= L:
        return nan
    counts = []
    for _ in range(n_windows):
        x0 = pos[0] + rng.random() * (Ltot - L)
        lo = bisect_left(pos, x0)
        hi = bisect_left(pos, x0 + L)
        counts.append(float(hi - lo))
    mean = sum(counts) / n_windows
    var = sum((c - mean) * (c - mean) for c in counts)
    return var / (n_windows - 1)


def delta3_rigidity(pos, L, n_windows, n_grid, rng):
    Ltot = pos[-1] - pos[0]
    if Ltot <= L:
        return nan
    xs = [L * float(i) / (n_grid - 1) for i in range(n_grid)]
    total = 0.0
    n_ok = 0
    for _ in range(n_windows):
        x0 = pos[0] + rng.random() * (Ltot - L)
        idx0 = bisect_left(pos, x0)
        Nv = [float(bisect_left(pos, x0 + xs[gi]) - idx0) for gi in range(n_grid)]
        r = linreg(xs, Nv)
        m2 = sum(e * e for e in r.res)
        total += m2 / n_grid
        n_ok += 1
    return total / n_ok


def _compute_K_single_seed(eigs, tvals, smooth_window=3):
    """Two-level form factor K(t) — verbatim (local unfold, smooth_window=3)."""
    n = len(eigs)
    K = [0.0] * len(tvals)
    if n < 10:
        return K
    s = sorted(eigs)
    window = max(3, int(round(n * 0.05)))
    u = [0.0] * n
    for i in range(1, n):
        i_lo = max(0, i - window)
        i_hi = min(n - 1, i + window)
        dens = (i_hi - i_lo + 1) / (s[i_hi] - s[i_lo] + 1e-12)
        u[i] = u[i - 1] + (s[i] - s[i - 1]) * dens
    ms = (u[-1] - u[0]) / (n - 1)
    if ms > 1e-12:
        u = [v / ms for v in u]
    for idx, t in enumerate(tvals):
        if t == 0.0:
            K[idx] = 0.0
            continue
        re = 0.0
        im = 0.0
        for k in range(n):
            ph = 2 * pi * t * u[k]
            re += cos(ph)
            im += sin(ph)
        K[idx] = max(0.0, (re * re + im * im) / n)
    w = 3 if smooth_window is None else int(smooth_window)  # callers default 3
    if len(K) > 2 * w:
        Ks = list(K)
        for j in range(w, len(K) - w):
            if tvals[j] < 0.5:
                continue
            acc = 0.0
            cnt = 0
            for q in range(-w, w + 1):
                acc += K[j + q]
                cnt += 1
            Ks[j] = acc / cnt
        K = Ks
    return K


def compute_K_form_factor(eigs, tvals, smooth_window=3):
    return _compute_K_single_seed(eigs, tvals, smooth_window=smooth_window)


# ── two-sample helpers (suite Tests 12/34) ──────────────────────────────────

def ks2(a, b):
    """Two-sample KS with tie discipline (ab_cloud_full.jl ks_test_2sample)."""
    xs = sorted(a)
    ys = sorted(b)
    n, m = len(xs), len(ys)
    i = j = 0
    D = 0.0
    while i < n and j < m:
        if xs[i] < ys[j]:
            i += 1
        elif ys[j] < xs[i]:
            j += 1
        else:
            xv = xs[i]
            while i < n and xs[i] == xv:
                i += 1
            while j < m and ys[j] == xv:
                j += 1
        D = max(D, fabs(i / n - j / m))
    return D


def unit_spacings(u):
    d = [u[i + 1] - u[i] for i in range(len(u) - 1)]
    if not d:
        return d
    m = sum(d) / len(d)
    if m > 1e-300:
        d = [v / m for v in d]
    return d
