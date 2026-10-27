"""rpbridge.stats — спектральная статистическая батарея V2/V3/V11.

Предрегистрация метрик (до запусков, план §Решение 2):
  S = (⟨r⟩, Σ²(L), Δ₃(L), K(t), D_KS→GUE) — никаких метрик,
  выбранных постфактум; диапазоны и seeds зафиксированы в constants.
"""
import numpy as np
from scipy.linalg import eigvalsh
from scipy.special import erf


def adjacent_ratios(levels):
    """r_n = min(s_n, s_{n+1}) / max(s_n, s_{n+1}) по развёрнутым уровням."""
    s = np.diff(np.asarray(levels, dtype=float))
    s = s[s > 0]
    a = np.minimum(s[:-1], s[1:])
    b = np.maximum(s[:-1], s[1:])
    return a / b


def _window_counts(u, L, n_win=60):
    """Числа уровней в n_win скользящих окнах длины L (регулярная сетка)."""
    starts = np.linspace(u[0], max(u[-1] - L, u[0]), n_win)
    lo = np.searchsorted(u, starts, side='left')
    hi = np.searchsorted(u, starts + L, side='left')
    return (hi - lo).astype(float)


def number_variance(u, L_grid):
    """Σ²(L) — дисперсия числа уровней в окне длины L."""
    u = np.asarray(u, dtype=float)
    return np.array([float(np.var(_window_counts(u, L))) for L in L_grid])


def spectral_rigidity(u, L_grid):
    """Δ₃(L) = min_c ⟨(N(E;L) − cL − α)²⟩ — спектральная жёсткость."""
    u = np.asarray(u, dtype=float)
    out = []
    for L in L_grid:
        n = _window_counts(u, L, n_win=40)
        x = n - L                      # отклонение лестницы от прямой c=L
        c = np.mean(x) / L             # оптимальный наклон (МНК по cL+α)
        seg = n - c * L
        out.append(float(np.var(seg)))
    return np.array(out)


def form_factor(u, t_grid):
    """K(t) = |Σ_n e^{−2πi u_n t}|²/N — форм-фактор развёрнутого спектра."""
    u = np.asarray(u, dtype=float)
    out = []
    for t in t_grid:
        ph = np.exp(-2j * np.pi * u * t)
        out.append(float(abs(ph.sum()) ** 2 / u.size))
    return np.array(out)


def gue_spectrum(n=576, seed=0):
    """GUE-нуль: (X+X†)/2, X комплексный гауссовский."""
    rng = np.random.default_rng(9000 + seed)
    X = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
    return np.sort(eigvalsh((X + X.conj().T) / 2, check_finite=False,
                            driver='evr'))


def poisson_levels(n=576, seed=0):
    rng = np.random.default_rng(7000 + seed)
    return np.cumsum(rng.exponential(1.0, n))


def goe_levels(n=576, seed=0):
    rng = np.random.default_rng(8000 + seed)
    X = rng.standard_normal((n, n))
    return np.sort(eigvalsh((X + X.T) / 2, check_finite=False, driver='evr'))


def unfold_poly(vals, degs=(6, 5, 4, 3)):
    """Развёртка полиномиальным счётом (протокол C3 эталона)."""
    vals = np.asarray(vals, dtype=float)
    idx = np.arange(vals.size, dtype=float)
    for deg in degs:
        c = np.polyfit(vals, idx, deg)
        u = np.polyval(c, vals)
        if np.all(np.diff(u) > 0):
            return u
    knots = np.linspace(0, vals.size - 1, max(8, vals.size // 16)).astype(int)
    return np.interp(vals, vals[knots], idx[knots])


def gue_surmise_cdf(x):
    """CDF сюрмизы GUE p(s) = (32/π²)·s²·e^{−4s²/π}."""
    x = np.asarray(x, dtype=float)
    return erf(2 * x / np.sqrt(np.pi)) \
        - (4 * x / np.pi) * np.exp(-4 * x * x / np.pi)


def gue_r_pool(n_mat=16, n=576, seed0=9000, K=200):
    """Объединённая выборка {r_n} ансамбля GUE (эталон для D_KS)."""
    pool = []
    for k in range(n_mat):
        w = gue_spectrum(n, k)
        half = int((w.size * 0.6) // 2)
        cen = w[w.size // 2 - half: w.size // 2 + half]
        u = unfold_poly(cen)[:K]
        pool.append(adjacent_ratios(u))
    return np.concatenate(pool)


def ks_to_gue(r, ref=None):
    """D_KS между {r_n} и эмпирическим GUE-эталоном (ансамбль)."""
    r = np.sort(np.asarray(r, dtype=float))
    ref = np.sort(gue_r_pool()) if ref is None \
        else np.sort(np.asarray(ref, float))
    n, m = r.size, ref.size
    data_all = np.concatenate([r, ref])
    cdf1 = np.searchsorted(r, data_all, side='right') / n
    cdf2 = np.searchsorted(ref, data_all, side='right') / m
    return float(np.max(np.abs(cdf1 - cdf2)))


def rank_corr(a, b):
    """Ранговая корреляция Спирмена (без scipy.stats — устойчивая версия)."""
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    ra = np.argsort(np.argsort(a)).astype(float)
    rb = np.argsort(np.argsort(b)).astype(float)
    ra -= ra.mean()
    rb -= rb.mean()
    d = np.sqrt((ra * ra).sum() * (rb * rb).sum())
    return float((ra * rb).sum() / d) if d > 0 else 0.0
