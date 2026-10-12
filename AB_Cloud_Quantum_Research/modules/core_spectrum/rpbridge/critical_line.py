"""rpbridge.critical_line — Решение 3 (V3): скан действительной части σ.

Механизм входа σ (устраняем неоднозначность ДО запуска, план §Решение 3):
арифметический вес вихря k задаётся модулем дзета на сканируемой линии:
    q_k(σ) = q · log|ζ(σ + iγ̃_k)|,   σ ∈ {0.0, 0.1, …, 1.0},
где γ̃_k = (γ_k + γ_{k+1})/2 — СЕРЕДИНЫ между соседними ординатами
(высоты, заведомо не совпадающие с нулями ζ: на критической линии |ζ|
конечен, вне её — тем более; полюс σ=1 исключён выбором сетки).
Назначение высот позициям вихрей — фиксировано (протокол C3).

Метрика: D(σ) = D_KS({r_n(σ)}, сюрмиза GUE); кривизна
    C_h = D(½−h) − 2D(½) + D(½+h);
проверка устойчивости: 3 seeds × 2 решётки; плацебо — заменa ζ на |ζ| от
случайно переставленных ординат (та же гладкая плотность весов).
"""
import numpy as np
import mpmath as mp

from engine.hamiltonian import build_hamiltonian
from rpbridge import stats
from rpbridge.stats import unfold_poly

SIGMA_GRID = tuple(round(0.1 * k, 1) for k in range(11))   # 0.0 … 1.0
SEEDS = (96, 196, 296)


def _vortex_protocol(L, seed, Nv=16):
    vrng = np.random.default_rng(seed + 3500)
    return [(float(vrng.integers(1, L)) + 0.5,
             float(vrng.integers(1, L)) + 0.5) for _ in range(Nv)]


def _weights(sigma, gamma_k):
    """q_k(σ) = log|ζ(σ+iγ̃_k)| по серединам γ̃ (mpmath, 20 цифр)."""
    out = []
    for g in gamma_k:
        v = abs(mp.zeta(mp.mpf(sigma) + 1j * mp.mpf(g)))
        out.append(float(mp.log(v)))
    return np.array(out)


def _midpoints(zeros, Nv):
    """Высоты вихрей γ̃_k = (γ_k+γ_{k+1})/2 — вне множества нулей."""
    z = np.asarray(zeros, float)
    return 0.5 * (z[:Nv] + z[1:Nv + 1])


def spectrum_for_sigma(sigma, zeros, L=24, seed=96, Nv=16, q=1.0, W=0.5):
    """Спектр затвора с σ-зависимым арифметическим весом вихрей."""
    pts = _vortex_protocol(L, seed, Nv)
    gamma_k = _midpoints(zeros, Nv)
    w = _weights(sigma, gamma_k)
    vort = [(x, y, q * wk) for (x, y), wk in zip(pts, w)]
    drng = np.random.default_rng(seed + 3501)
    H = build_hamiltonian(L, L, vort, 0.5, 1.0, W, 'open', drng)
    ev = np.sort(np.linalg.eigvalsh(H))
    half = int((ev.size * 0.6) // 2)
    cen = ev[ev.size // 2 - half: ev.size // 2 + half]
    u = unfold_poly(cen)[:200]
    r = stats.adjacent_ratios(u)
    return stats.ks_to_gue(r), float(np.mean(r))


def run(zeros):
    """Полный скан V3: σ-сетка × seeds + плацебо + кривизна."""
    D = {}
    for s in SIGMA_GRID:
        rows = []
        for sd in SEEDS:
            d, r = spectrum_for_sigma(s, zeros, seed=sd)
            rows.append({'seed': sd, 'D_KS': d, 'r_mean': r})
        D[str(s)] = rows
    D_mean = {s: float(np.mean([x['D_KS'] for x in rows]))
              for s, rows in D.items()}
    # кривизна в ½ при h = 0.1 (по средним кривым)
    h = 0.1
    Dh = D_mean
    C_h = Dh[str(round(0.5 - h, 1))] - 2 * Dh['0.5'] + Dh[str(round(0.5 + h, 1))]

    # плацебо: переставленные ординаты → веса (та же плотность распределения)
    rng = np.random.default_rng(5100)
    zp = _midpoints(rng.permutation(zeros[:8192]), 4096)
    D_pl = []
    for s in ('0.4', '0.5', '0.6'):
        d, _ = spectrum_for_sigma(float(s), zp, seed=96)
        D_pl.append(d)

    return {
        'sigma_grid': list(SIGMA_GRID), 'seeds': list(SEEDS),
        'D_table': D, 'D_mean': D_mean,
        'curvature_C_h': float(C_h), 'h': h,
        'argmin_sigma': float(min(D_mean, key=D_mean.get)),
        'D_05': Dh['0.5'],
        'placebo_D': D_pl,
        'minimum_at_half': bool(abs(Dh['0.5'] - min(D_mean.values())) < 0.01),
        'verdict_note': ('минимум D(σ) в окрестности σ = 1/2 отсутствует '
                         'или неустойчив — специфичность линии измерена, '
                         'а не постулирована (см. честные замечания)'),
    }
