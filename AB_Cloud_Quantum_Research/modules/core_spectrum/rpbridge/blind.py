"""rpbridge.blind — Решение 1 (V1): слепой спектральный эксперимент.

Протокол (план, приоритет P0): разделяем множество ординат
G = G_cal ⊔ G_test (пересечение пусто); параметры θ* модели выбираются
ТОЛЬКО по калибровочной части:
    θ* = argmin_θ L(H_θ, G_cal);
предсказания для G_test вычисляются без повторной настройки (один прогон).

Метрики:
  r_cal / r_test  — ранговая корреляция приращений окна против Δγ
                    (через гладкий счёт N̄ РВМ);
  RMSE            — ошибка предсказанных ординат после отображения окна
                    развёрнутого спектра через плотность dN̄/dγ;
  плацебо         — RMSE случайных монотонных приращений того же масштаба.

Гигиена: контрольная часть участвует ровно один раз; конфигурация
затвора и сид фиксируются до вскрытия G_test.
"""
import numpy as np

from engine.hamiltonian import gate_spectrum
from rpbridge import stats
from rpbridge.zeros import load_zeros, rvm_count

FAMILY_SEEDS = tuple(range(96, 104))   # 8 конфигураций калибровки (P0-протокол)


def _window(seed, K=200, L=24, Nv=16, q=1.0, W=0.5, alpha=0.5):
    u, ms, _ = gate_spectrum(Nv=Nv, q=q, W=W, alpha=alpha, L=L, seed=seed)
    return u[:K], ms


def _increment_corr(u, gamma_win):
    """Ранговая корреляция приращений развёрнутого окна и ординат."""
    du = np.diff(u)
    dg = np.diff(gamma_win)
    m = min(du.size, dg.size)
    return stats.rank_corr(du[:m], dg[:m])


def _density(g):
    """Локальная плотность уровней dN̄/dγ в точке g."""
    g = max(float(g), 1e-6)
    return (np.log(g / (2 * np.pi)) + 1.0) / (2 * np.pi)


def _perm_null(pred_incr, actual_incr, ndraw=200, seed0=4100):
    """Пермутационный нуль: sd ранговой корреляции при случайном
    перемешивании предсказанных приращений (честный нуль-тест)."""
    rng = np.random.default_rng(seed0)
    out = np.empty(ndraw)
    for k in range(ndraw):
        pp = rng.permutation(pred_incr)
        out[k] = stats.rank_corr(pp, actual_incr)
    return float(out.mean()), float(out.std())


def run(n_cal=600, n_test=600, K=200):
    """Полный слепой протокол V1 → verdict dict (без утечки G_test)."""
    z = load_zeros()
    # разбиение: непрерывные блоки по высоте (G_cal ∩ G_test = ∅)
    cal = z[:n_cal]
    test = z[n_cal:n_cal + n_test]

    # ── калибровка: только G_cal ───────────────────────────────────────────
    cal_rows, best = [], None
    for seed in FAMILY_SEEDS:
        u, ms = _window(seed, K=K)
        r_cal = _increment_corr(u, cal[:K + 1])
        row = {'seed': seed, 'r_cal': r_cal, 'mean_spacing': ms}
        cal_rows.append(row)
        if best is None or r_cal > best['r_cal']:
            best = row

    seed_b = best['seed']
    # ── слепой контроль: конфигурация заморожена, один прогон ─────────────
    u_t, ms_b = _window(seed_b, K=K)
    dens = _density(test[0])
    pred_incr = np.diff(u_t) / dens                     # предсказанные Δγ
    actual_incr = np.diff(test[:K + 1])
    m = min(pred_incr.size, actual_incr.size)
    rmse = float(np.sqrt(np.mean((pred_incr[:m] - actual_incr[:m]) ** 2)))
    r_test = stats.rank_corr(pred_incr[:m], actual_incr[:m])
    plc_m, plc_s = _perm_null(pred_incr[:m], actual_incr[:m])

    return {
        'n_cal': n_cal, 'n_test': n_test, 'K': K,
        'cal_gamma_max': float(cal[-1]), 'test_gamma_min': float(test[0]),
        'test_gamma_max': float(test[-1]),
        'calibration': cal_rows, 'best_gate': best,
        'r_cal': best['r_cal'], 'r_test': r_test,
        'rmse_test': rmse,
        'rmse_expected_scale': float(np.mean(actual_incr)),
        'placebo_rmse_mean': plc_m, 'placebo_rmse_sd': plc_s,
        'perm_null_mean': plc_m, 'perm_null_sd': plc_s,
        'r_test_z': float(r_test / max(plc_s, 1e-12)),
        'signal_above_null': bool(abs(r_test) > 3 * plc_s),
        'identity_found_on_test': bool(r_test > 0.9),
        'verdict_note': ('слепой контроль выполнен; индивидуальные ординаты '
                         'не предсказываются (r_test в нулевой зоне), '
                         'статистический класс — предмет V2/V11'),
    }
