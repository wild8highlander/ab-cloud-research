# -*- coding: utf-8 -*-
"""Scalar special functions — 1:1 with ab_cloud_full.jl §3.

Lanczos lgamma (g=7, n=9), regularized lower incomplete gamma (series +
Lentz continued fraction), chi2 CDF, Kolmogorov-Smirnov asymptotic p-value,
GOE/GUE₂ Wigner surmises, Lambert W (Halley), Gram points, b(N) statistic.
"""

from math import log, sin, cos, sqrt, exp, fabs, pi, isnan

_LANCZOS_COEF = (
    0.99999999999980993, 676.5203681218851, -1259.1392167224028,
    771.32342877765313, -176.61502916214059, 12.507343278686905,
    -0.13857109526572012, 9.9843695780195716e-6, 1.5056327351493116e-7,
)


def lgamma_lanczos(x):
    if x < 0.5:
        return log(pi / sin(pi * x)) - lgamma_lanczos(1.0 - x)
    x -= 1.0
    a = _LANCZOS_COEF[0]
    t = x + 7.0 + 0.5
    for i in range(1, 8):
        a += _LANCZOS_COEF[i] / (x + i)
    return 0.5 * log(2 * pi) + (x + 0.5) * log(t) - t + log(a)


def gammp_series(a, x):
    ap = a
    total = 1.0 / a
    delta = total
    for _ in range(200):
        ap += 1.0
        delta *= x / ap
        total += delta
        if fabs(delta) < fabs(total) * 1e-15:
            break
    return total * exp(-x + a * log(x) - lgamma_lanczos(a))


def gammq_cf(a, x):
    FPMIN = 1e-300
    b = x + 1.0 - a
    c = 1.0 / FPMIN
    d = 1.0 / b
    h = d
    for i in range(1, 201):
        an = -float(i) * (i - a)
        b += 2.0
        d = an * d + b
        if fabs(d) < FPMIN:
            d = FPMIN
        c = b + an / c
        if fabs(c) < FPMIN:
            c = FPMIN
        d = 1.0 / d
        delta = d * c
        h *= delta
        if fabs(delta - 1.0) < 1e-15:
            break
    return exp(-x + a * log(x) - lgamma_lanczos(a)) * h


def regularized_gamma_p(a, x):
    if x <= 0.0:
        return 0.0
    if x < a + 1.0:
        return gammp_series(a, x)
    return 1.0 - gammq_cf(a, x)


def chi2_cdf(x, df):
    return regularized_gamma_p(df / 2.0, x / 2.0)


def ks_asymptotic_pvalue(lam):
    if lam <= 0.0:
        return 1.0
    if lam < 0.6:
        s2 = 0.0
        for k in range(1, 1001):
            term2 = exp(-(((2.0 * k - 1.0) * (2.0 * k - 1.0)) * pi * pi)
                        / (8.0 * lam * lam))
            s2 += term2
            if term2 < 1e-18:
                break
        v = 1.0 - sqrt(2 * pi) / lam * s2
        return 0.0 if v < 0.0 else (1.0 if v > 1.0 else v)
    s = 0.0
    sign = 1.0
    for k in range(1, 101):
        term = sign * exp(-2.0 * k * k * lam * lam)
        s += term
        sign = -sign
        if fabs(term) < 1e-18:
            break
    v = 2.0 * s
    return 0.0 if v < 0.0 else (1.0 if v > 1.0 else v)


def goe_surmise_cdf(s):
    return 1.0 - exp(-pi * s * s / 4.0)


def gue2_surmise_cdf(s):
    if s < 0:
        return 0.0
    x2 = 4.0 * s * s / pi
    return regularized_gamma_p(0.5, x2) - (4.0 * s / pi) * exp(-x2)


def gue2_surmise_pdf(s):
    return (32.0 / (pi * pi)) * s * s * exp(-4.0 * s * s / pi)


def lambert_w(x):
    """W0 branch, Newton-Halley — verbatim with the Julia original."""
    if x <= -1.0 / exp(1.0):
        return -1.0
    w = x if x < 1.5 else log(x) - log(log(x))
    for _ in range(50):
        ew = exp(w)
        f = w * ew - x
        fp = ew * (w + 1.0)
        fpp = ew * (w + 2.0)
        delta = -f / (fp - 0.5 * f * fpp / fp)
        w += delta
        if fabs(delta) < 1e-15 * fabs(w):
            break
    return w


def gram_point(n):
    """Gram point g_n: theta(t) = n*pi solved by 8 Newton steps."""
    if n <= 0:
        return 0.0
    t = 2 * pi * float(n) / lambert_w(float(n) / exp(1.0))
    for _ in range(8):
        arg = t / (2 * pi)
        if arg <= 0:
            break
        theta = (t / 2 * log(arg) - t / 2 - pi / 8 + 1.0 / (48 * t)
                 + 7.0 / (5760 * t * t * t))
        dtheta = 0.5 * log(arg) - 1.0 / (48 * t * t) - 21.0 / (5760 * t ** 4)
        if fabs(dtheta) < 1e-30:
            break
        t -= (theta - float(n) * pi) / dtheta
    return t


def compute_bN(z, N, offset=0):
    """b(N) = <|gamma_k - g_k|> over the first N zeros."""
    N = min(N, len(z))
    s = 0.0
    for k in range(1, N + 1):
        s += fabs(z[k - 1] - gram_point(offset + k))
    return s / float(N)
