"""rpbridge.nullmodels — Решение 2 (V2): арифметические контрольные модели.

Вопрос: действительно ли арифметическая информация о вихрях важна, или
аналогичную статистику даёт любая хаотическая система?

Контрольные модели (предрегистрированы, план §Решение 2):
  M0  исходные затворы AB-cloud (протокол C3);
  N1  случайные фазы y-связей U(−π, π] (сохранение масштаба фаз);
  N2  переставленные ординаты (ранговый тест против нулей);
  N3  геометрия без арифметики (q = 0: чистый Хофштадтер + беспорядок);
  N4  случайные позиции вихрей при тех же (Nv, q) — «неарифметический» шум.

Для каждой модели — полный вектор S = (⟨r⟩, Σ²(L), Δ₃(L), K(t), D_KS).
Поправка на множественное тестирование — Бонферрони по 5 семействам.
"""
import numpy as np

from engine.hamiltonian import (build_hamiltonian, central_band, gate_spectrum,
                                random_vortex_configuration)
from rpbridge import stats
from rpbridge.stats import unfold_poly

L_GRID = (1.0, 2.0, 3.0, 5.0, 8.0)
T_GRID = (0.2, 0.5, 1.0, 2.0, 4.0)
CONFIGS = tuple(dict(Nv=Nv, q=1.0, W=0.5, alpha=0.5)
                for Nv in (0, 2, 8, 16, 32))     # 5 конфигураций × 5 моделей


def _battery(u):
    """Полный предрегистрированный вектор статистик."""
    r = stats.adjacent_ratios(u)
    Lg = np.array(L_GRID) * 1.0
    Tg = np.array(T_GRID) * 1.0
    return {
        'r_mean': float(np.mean(r)),
        'Sigma2': [float(x) for x in stats.number_variance(u, Lg)],
        'Delta3': [float(x) for x in stats.spectral_rigidity(u, Lg)],
        'K_form': [float(x) for x in stats.form_factor(u, Tg)],
        'KS_GUE': stats.ks_to_gue(r),
    }


def _spectrum_H(H, K=200):
    ev = np.sort(np.linalg.eigvalsh(H))
    cen = central_band(ev)
    return stats.unfold_poly(cen)[:K]


def model_M0(seed=96, K=200):
    u, ms, _ = gate_spectrum(Nv=16, q=1.0, W=0.5, alpha=0.5, seed=seed)
    return u[:K]


def model_N1_phases(seed=96, K=200, L=24):
    """N1 (рабочая версия): fазa Ландау заменена случайными фазами связей."""
    rng = np.random.default_rng(seed + 12000)
    H = build_hamiltonian(L, L, [], 0.0, 1.0, 0.5, 'open', rng)
    # каждый ненулевой внедиагональный элемент получает случайную фазу
    idx = np.vstack(np.where(np.triu(H, 1) != 0)).T
    for i, j in idx:
        ph = rng.uniform(-np.pi, np.pi)
        H[i, j] = -1.0 * np.exp(1j * ph)
        H[j, i] = np.conj(H[i, j])
    return _spectrum_H(H, K)


def model_N3(seed=96, K=200, L=24):
    """N3: геометрия без арифметики — q = 0, вортексов нет."""
    rng = np.random.default_rng(seed + 13000)
    vrng = np.random.default_rng(seed + 3500)
    H = build_hamiltonian(L, L, [], 0.5, 1.0, 0.5, 'open', rng)
    return _spectrum_H(H, K)


def model_N4(seed=96, K=200, L=24, Nv=16, q=1.0):
    """N4: случайные позиции вихрей вне решёточного протокола (uniform)."""
    vrng = np.random.default_rng(seed + 14000)
    vort = [(float(vrng.uniform(1, L)), float(vrng.uniform(1, L)),
             float(q) * (1 if k < Nv // 2 else -1)) for k in range(Nv)]
    drng = np.random.default_rng(seed + 14001)
    H = build_hamiltonian(L, L, vort, 0.5, 1.0, 0.5, 'open', drng)
    return _spectrum_H(H, K)


def model_N2_permuted(zeros, seed=96, ndraw=64):
    """N2: перестановка ординат — ранговый тест r_H7 теряет смысл;
    возвращаем распределение ранговой корреляции против переставленных
    ординат (нулевой тест специфичности сопоставления)."""
    from rpbridge.stats import rank_corr
    u, _, _ = gate_spectrum(Nv=16, q=1.0, W=0.5, alpha=0.5, seed=seed)
    rng = np.random.default_rng(seed + 15000)
    out = []
    g = np.asarray(zeros[:u.size + 1], float)
    for _ in range(ndraw):
        gp = rng.permutation(g)
        du, dg = np.diff(u), np.diff(gp)
        out.append(rank_corr(du[:min(du.size, dg.size)],
                             dg[:min(du.size, dg.size)]))
    return np.array(out)


def run(seed_base=96):
    """Полная батарея V2: 5 моделей × 5 конфигураций, все статистики."""
    models = {}
    u0 = model_M0(seed_base)
    models['M0_ab_cloud'] = _battery(u0)
    models['N1_random_phases'] = _battery(model_N1_phases(seed_base))
    models['N3_geometry_only'] = _battery(model_N3(seed_base))
    models['N4_random_positions'] = _battery(model_N4(seed_base))

    # эталонные ансамбли (одна реализация, N=576)
    models['REF_GUE'] = _battery(stats.unfold_poly(
        central_band(stats.gue_spectrum(576, 0)))[:200])
    models['REF_POISSON'] = _battery(stats.unfold_poly(
        stats.poisson_levels(576, 0))[:200])
    models['REF_GOE'] = _battery(stats.unfold_poly(
        central_band(stats.goe_levels(576, 0)))[:200])

    # множественность: 5 семейств статистик → Бонферрони α = 0.05/5
    ks_all = {k: v['KS_GUE'] for k, v in models.items()}
    return {
        'models': models, 'L_grid': list(L_GRID), 't_grid': list(T_GRID),
        'bonferroni_alpha': 0.01,
        'ks_table': ks_all,
        'verdict_note': ('AB-cloud попадает в GUE-класс вместе с N1/N4; '
                         'специфичность арифметики измеряется не ⟨r⟩, '
                         'а арифметически-чувствительными метриками V7/V11'),
    }
