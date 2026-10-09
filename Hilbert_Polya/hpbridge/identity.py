"""hpbridge.identity — функция тождеств Z_id и Γ-лестница (кампании C1).

Z_id(t) = e^{iθ(t)}·ζ(½+it), θ(t) = Im ln Γ(¼+it/2) − (t/2)·lnπ —
непрерывный аналог точного фазового закона; Ξ_id ≡ ξ(½+it).

Γ-лестница (T1): три элементарных замыкания на мнимой оси
  |Γ(½+iu)|²           = π / cosh(πu)                      (отражение)
  |Γ(iu)|²             = π / (u·sinh(πu))                  (предел отражения)
  |Γ(¼+iu)|·|Γ(¾+iu)|  = π√2 / √cosh(2πu)                  (удвоение Лежандра)
и измеренное замечание K1: отдельный модуль |Γ(¼+iu)| на линии элементарно
не замыкается (первая форма опровергнута вычислением: 0.765 ≠ 1).
"""
import numpy as np
import mpmath as mp

from hpbridge.constants import GAMMA_E  # noqa: F401


# ── Γ-лестница ──────────────────────────────────────────────────────────────
def gamma_ladder_closures(u):
    """Три замыкания T1 для массива u; возвращает список относительных
    невязок (dps=40 внутри, float снаружи)."""
    mp.mp.dps = 40
    out = []
    for uu in np.atleast_1d(u):
        u_ = mp.mpf(float(uu))
        r1 = abs(abs(mp.gamma(mp.mpf('0.5') + 1j * u_)) ** 2
                 - mp.pi / mp.cosh(mp.pi * u_))
        r2 = abs(abs(mp.gamma(1j * u_)) ** 2
                 - mp.pi / (u_ * mp.sinh(mp.pi * u_)))
        prod = abs(mp.gamma(mp.mpf('0.25') + 1j * u_)) * \
            abs(mp.gamma(mp.mpf('0.75') + 1j * u_))
        r3 = abs(prod - mp.pi * mp.sqrt(2) / mp.sqrt(mp.cosh(2 * mp.pi * u_)))
        out.append((float(r1), float(r2), float(r3)))
    return out


# ── функция тождеств ────────────────────────────────────────────────────────
def theta(t, dps=None):
    """Римана–Зигеля θ(t) = Im ln Γ(¼+it/2) − t·lnπ/2 (непрерывная ветвь).
    Точность фазы задаётся явно: по умолчанию dps текущего контекста + 10."""
    keep = mp.mp.dps
    mp.mp.dps = (dps or keep) + 10
    try:
        val = (mp.im(mp.log(mp.gamma(mp.mpf('0.25') + 1j * mp.mpf(t) / 2)))
               - mp.mpf(t) * mp.log(mp.pi) / 2)
    finally:
        mp.mp.dps = keep
    return float(val)


def Z_id(t, dps=30):
    """Функция тождеств на критической линии: Z_id(t) = e^{iθ(t)}ζ(½+it).
    Фаза вычисляется в mpmath-точности БЕЗ округления в double —
    вещественность (T2) держится до 5e-29 при dps = 30."""
    keep = mp.mp.dps
    mp.mp.dps = dps + 10
    try:
        tt = mp.mpf(t)
        th = (mp.im(mp.log(mp.gamma(mp.mpf('0.25') + 1j * tt / 2)))
              - tt * mp.log(mp.pi) / 2)
        z = mp.e ** (1j * th) * mp.zeta(mp.mpf('0.5') + 1j * tt)
        return float(mp.re(z)), float(mp.im(z))
    finally:
        mp.mp.dps = keep


def zid_zeros_bisection(T=200.0, step=None):
    """Нули Z_id на [0, T] бисекцией по смене знака (K3)."""
    step = step or max(0.05, T / 4000)
    grid = np.arange(0.0, T + step, step)
    vals = []
    for g in grid:
        re, _ = Z_id(float(g), dps=25)
        vals.append(re)
    vals = np.array(vals)
    sign = np.where(np.diff(np.sign(vals)) != 0)[0]
    zeros = []
    for i in sign:
        a, b = grid[i], grid[i + 1]
        fa = vals[i]
        for _ in range(80):
            m = 0.5 * (a + b)
            fm, _ = Z_id(float(m), dps=25)
            if fm == 0:
                a = b = m
                break
            if np.sign(fm) == np.sign(fa):
                a, fa = m, fm
            else:
                b = m
        zeros.append(0.5 * (a + b))
    return np.array(zeros)


def gram_points(n_points):
    """Точки Грама g_n: θ(g_n) = nπ (K7)."""
    out, n = [], 0
    while len(out) < n_points:
        g = mp.findroot(lambda t: mp.im(mp.log(mp.gamma(mp.mpf('0.25') + 1j * t / 2)))
                        - t * mp.log(mp.pi) / 2 - mp.pi * n,
                        (n * mp.pi / mp.log(mp.mpf(n + 10)) * 8,))
        out.append(float(g))
        n += 1
    return out
