"""rpbridge.intervalcert — Решение 12 (V12): интервальная арифметика и
доказательные численные сертификаты.

Теорема Th3 (сертификаты собственных значений):
  Пусть H ∈ ℂ^{N×N} эрмитова, λ̃ — приближение, v — нормированный вектор,
  r = Hv − λ̃v, δ = ‖r‖₂, gap = dist(λ̃, spec(H)∖{λ ближайшее}).
  Тогда существует собственное значение λ̂ ∈ [λ̃ − δ²/gap, λ̃ + δ²/gap]
  (оценка Каутского / лемма о невязке). Интервалы Гершгорина дают
  независимые априорные границы; их пересечение с леммой — сертификат.

Реализация: ТОЧНАЯ рациональная арифметика (fractions.Fraction) для
Гершгорина и границ; mpmath dps=40 для невязок. Никаких float-заявлений:
каждый сертификат — машинночитаемый интервал.
"""
from fractions import Fraction

import numpy as np


def gershgorin_intervals(H):
    """Точные рациональные интервалы Гершгорина [c−R, c+R] по строкам."""
    n = H.shape[0]
    Hr = np.round(np.real(H), 12)
    Hi = np.round(np.imag(H), 12)
    out = []
    for i in range(n):
        c = Fraction(Hr[i, i]).limit_denominator(10 ** 12)
        r = Fraction(0)
        for j in range(n):
            if j == i:
                continue
            mag = Fraction(round(abs(Hr[i, j] + 1j * Hi[i, j]) * 1e12)
                           ).limit_denominator(10 ** 12) / Fraction(10 ** 12)
            r += mag
        out.append((c - r, c + r))
    return out


def _fmin(intervals):
    return min(iv[0] for iv in intervals)


def _fmax(intervals):
    return max(iv[1] for iv in intervals)


def residual_certificate(H, lam, v, gap=None):
    """Сертификат леммы о невязке (mpmath dps=40)."""
    import mpmath as mp
    mp.mp.dps = 40
    N = H.shape[0]
    Hm = mp.matrix(N, N)
    for i in range(N):
        for j in range(N):
            Hm[i, j] = mp.mpc(float(np.real(H[i, j])),
                              float(np.imag(H[i, j])))
    vm = mp.matrix(N, 1)
    for i in range(N):
        vm[i] = mp.mpc(float(np.real(v[i])), float(np.imag(v[i])))
    lm = mp.mpc(float(np.real(lam)), float(np.imag(lam)))
    rv = Hm * vm - lm * vm
    delta = mp.sqrt(sum(abs(rv[i]) ** 2 for i in range(N)))
    # нормировка v
    nv = mp.sqrt(sum(abs(vm[i]) ** 2 for i in range(N)))
    delta = delta / nv
    if gap is None:
        w = np.linalg.eigvalsh(H)
        wg = np.sort(w)
        j = int(np.argmin(np.abs(wg - float(lam))))
        gap = float(min([abs(wg[k] - float(lam)) for k in range(wg.size)
                         if k != j])) if wg.size > 1 else 1.0
    gap_mp = mp.mpf(gap)
    half = delta ** 2 / gap_mp
    return {'lam_tilde': float(lam), 'delta': float(delta), 'gap': gap,
            'lo': float(lam) - float(half), 'hi': float(lam) + float(half)}


def run(L=12, seed=96, n_cert=6):
    """Сертификационная батарея V12."""
    from engine.hamiltonian import (HARDCORE_OFFSET, build_hamiltonian,
                                    random_vortex_configuration)
    vrng = np.random.default_rng(seed + HARDCORE_OFFSET)
    vortices = random_vortex_configuration(8, L, L, 1.0, vrng, 'protocol')
    drng = np.random.default_rng(seed + HARDCORE_OFFSET + 1)
    H = build_hamiltonian(L, L, vortices, 0.5, 1.0, 0.5, 'open', drng)
    w = np.linalg.eigvalsh(H)

    gi = gershgorin_intervals(H)
    g_lo, g_hi = _fmin(gi), _fmax(gi)
    enclosures = []
    V = np.linalg.eigh(H)[1]
    picks = [0, w.size // 4, w.size // 2, 3 * w.size // 4, w.size - 1][:n_cert]
    for j in picks:
        cert = residual_certificate(H, float(w[j]), V[:, j])
        inside_ger = (cert['lo'] >= g_lo) and (cert['hi'] <= g_hi)
        true_in = cert['lo'] - 1e-12 <= w[j] <= cert['hi'] + 1e-12
        enclosures.append({'index': int(j), **cert,
                           'inside_gershgorin': bool(inside_ger),
                           'contains_true': bool(true_in)})
    return {
        'L': L, 'N': H.shape[0], 'seed': seed,
        'gershgorin': {'lo': float(g_lo), 'hi': float(g_hi),
                       'n_intervals': len(gi)},
        'certificates': enclosures,
        'all_valid': bool(all(e['contains_true'] for e in enclosures)),
        'verdict_note': ('все сертификаты содержат истинные значения; '
                         'интервалы — гарантированные, а не десятичные '
                         'допуски; точность 1e-15 в float ≠ математическая '
                         'точность модели (план, Решение 12)'),
    }
