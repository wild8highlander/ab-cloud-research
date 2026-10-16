# -*- coding: utf-8 -*-
"""HP-аудит: развёртка, регрессия и H1-детектор — 1:1 с ab_cloud_full.jl §7
и hp_audit_standalone.jl (детектор H1 + вспомогательная статистика)."""

from math import log, sqrt, fabs, pi, cos, sin, exp, isnan
from .gof import linreg


def hp_kgue_envelope(t):
    """GUE form-factor envelope K_box(t): t*(1-sinc(2pi t)) for t<1, else 1."""
    if t < 1.0:
        x = 2 * pi * t
        sn = 1.0 if fabs(x) < 1e-12 else sin(x) / x
        return t * (1.0 - sn)
    return 1.0


def hp_raw_ft(zs, omega):
    """H1 periodogram: |sum_i Hann(t_i) e^{-i omega z_i}|^2 / sum Hann^2."""
    n = len(zs)
    w = [0.5 * (1.0 - cos(2 * pi * i / max(n - 1, 1))) for i in range(n)]
    sw2 = sum(wi * wi for wi in w)
    P = []
    for om in omega:
        re = 0.0
        im = 0.0
        for i in range(n):
            re += w[i] * cos(om * zs[i])
            im -= w[i] * sin(om * zs[i])
        P.append((re * re + im * im) / sw2)
    return P


def hp_unfold_local(eigs, win_frac=0.05):
    """Local-density unfolding with window = max(3, round(n*win_frac))."""
    s = sorted(eigs)
    n = len(s)
    if n < 10:
        return [float(i) for i in range(n)]
    window = max(3, int(round(n * win_frac)))
    u = [0.0] * n
    for i in range(1, n):
        i_lo = max(0, i - window)
        i_hi = min(n - 1, i + window)
        dens = (i_hi - i_lo + 1) / (s[i_hi] - s[i_lo] + 1e-12)
        u[i] = u[i - 1] + (s[i] - s[i - 1]) * dens
    ms = (u[-1] - u[0]) / max(n - 1, 1)
    if ms > 1e-12:
        u = [v / ms for v in u]
    return u


def hp_k_residual(K, tvals, dpoly=3):
    """K(t) residual for H1 (Julia _hp_k_residual): measured form factor minus
    the analytic GUE envelope, then a degree-`dpoly` polynomial detrend (least
    squares on the full window — a quadratic cannot absorb the log-p
    oscillations whose periods are >= 2.45)."""
    import numpy as np
    base = [hp_kgue_envelope(t) for t in tvals]
    res = [K[i] - base[i] for i in range(len(tvals))]
    X = np.array([[float(t) ** k for k in range(dpoly + 1)] for t in tvals])
    y = np.array(res)
    coef, _, _, _ = np.linalg.lstsq(X, y, rcond=None)
    out = y - X @ coef
    return [float(v) for v in out]


def hp_periodogram(res, ts, omega):
    """H1 D2 route (Julia _hp_periodogram): mean-subtracted Hann-weighted FT of
    a residual series over the UNFOLDING time axis, P = 2|sum|^2 / sum w^2."""
    n = len(res)
    if n == 0:
        return [0.0] * len(omega)
    m = sum(res) / n
    r = [v - m for v in res]
    w = [0.5 * (1.0 - cos(2 * pi * k / max(n - 1, 1))) for k in range(n)]
    sw2 = sum(wi * wi for wi in w)
    if not sw2 > 1e-300:
        sw2 = 1.0
    t0 = ts[0]
    P = []
    for om in omega:
        acc_re = 0.0
        acc_im = 0.0
        for k in range(n):
            ph = om * (ts[k] - t0)
            wk = w[k] * r[k]
            acc_re += wk * cos(ph)
            acc_im -= wk * sin(ph)
        P.append(2.0 * (acc_re * acc_re + acc_im * acc_im) / sw2)
    return P


def hp_fluct_hp(f, win=8):
    """H7 fluctuation high-pass (Julia _hp_fluct_hp): subtract the centered
    moving average (half-width `win`) from a fluctuation series — removes the
    slow deterministic estimator bias shared by every spectrum processed with
    the same local-window unfolding."""
    n = len(f)
    win = max(1, min(win, n // 2))
    out = []
    for i in range(n):
        lo = max(0, i - win)
        hi = min(n, i + win + 1)
        seg = f[lo:hi]
        out.append(f[i] - sum(seg) / len(seg))
    return out


def hp_unit_spacings(u):
    """Unit spacings (mean 1) — alias used by the HP gates."""
    return unit_spacings(u)


def unit_spacings(u):
    from .gof import unit_spacings as _us
    return _us(u)


def hp_rankdata(x):
    """1-based average ranks (ties get the mean rank)."""
    n = len(x)
    ord_ = sorted(range(n), key=lambda i: x[i])
    ranks = [0.0] * n
    i = 0
    while i < n:
        j = i
        while j + 1 < n and x[ord_[j + 1]] == x[ord_[i]]:
            j += 1
        avg = (i + j) / 2.0 + 1.0
        for k in range(i, j + 1):
            ranks[ord_[k]] = avg
        i = j + 1
    return ranks


def pearson_cor(x, y):
    n = len(x)
    if n == 0:
        return float("nan")
    mx = sum(x) / n
    my = sum(y) / n
    sxy = sxx = syy = 0.0
    for xi, yi in zip(x, y):
        sxy += (xi - mx) * (yi - my)
        sxx += (xi - mx) * (xi - mx)
        syy += (yi - my) * (yi - my)
    if sxx <= 0 or syy <= 0:
        return float("nan")
    return sxy / sqrt(sxx * syy)


def hp_aicc(n, rss, k):
    """Akaike information criterion with small-sample correction."""
    denom = n - k - 1
    aic = n * log(max(rss, 1e-300) / n) + 2.0 * k
    return aic + 2.0 * k * (k + 1) / denom if denom > 0 else aic


def hp_wald_ci(k, n):
    """Wald 95% interval for a proportion k/n -> (p, lo, hi)."""
    if n == 0:
        return 0.0, 0.0, 0.0
    p = float(k) / n
    h = 1.96 * sqrt(p * (1 - p) / n)
    lo = min(max(p - h, 0.0), 1.0)
    hi = min(max(p + h, 0.0), 1.0)
    return p, lo, hi


def default_omega_grid():
    """726-point band [0.3, 3.2] step 0.004 — the H1 default scan grid."""
    return [0.3 + 0.004 * k for k in range(726)]


def h1_detect(zs, omega=None):
    """H1 primary detector: SNR of log-prime harmonics against band median."""
    if omega is None:
        omega = default_omega_grid()
    P = hp_raw_ft(zs, omega)
    Ps = sorted(P)
    n = len(Ps)
    med = Ps[n // 2] if n % 2 == 1 else 0.5 * (Ps[n // 2 - 1] + Ps[n // 2])
    out = []
    for pr in (2, 3, 5, 7, 11, 13):
        tgt = log(pr)
        best = 0
        bd = 1e300
        for i, om in enumerate(omega):
            d = fabs(om - tgt)
            if d < bd:
                bd = d
                best = i
        out.append((pr, P[best] / med))
    return med, out


def h1_report(zs, omega=None, snr_gate=10.0):
    """Full H1 report: median, per-prime SNR verdicts, aggregate verdict."""
    med, snrs = h1_detect(zs, omega)
    hits = 0
    lines = []
    for pr, snr in snrs:
        peak = snr >= snr_gate
        hits += 1 if peak else 0
        lines.append("  SNR(log %2d) = %.6e  [%s]" % (pr, snr, "PEAK" if peak else "-"))
    verdict = "%d/6 prime harmonics above SNR %g" % (hits, snr_gate)
    strong = all(snr >= 100.0 for _, snr in snrs)
    return {
        "median": med,
        "snrs": snrs,
        "hits": hits,
        "verdict": verdict,
        "strong": strong,
        "lines": lines,
    }
