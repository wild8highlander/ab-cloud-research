"""hpbridge.metrics_v2 — общие метрики кампаний v2.0 (C9–C16).

Протокол C3 в новой редакции, не зависящей от внешнего файла нулей:
  * окно нулей — первые k уровней из внутреннего кэша hpbridge.zeros_mp;
  * r_H7 — максимум пирсоновской корреляции безлинейного-тренда окна затвора
    против окна нулей по дробному сдвигу выравнивания;
  * p_r — против 64 случайных сдвигов нулевого окна (перестановочный нуль);
  * r_GUE_z — z-оценка против 40 GUE-спектров того же объёма;
  * ⟨r⟩ — среднее отношение соседних зазоров (класс статистики, C8).
Позитивные контроли повторяют дисциплину v1: PC1 (изоспектральные близнецы)
и PC2 (функция тождеств против прямого счёта нулей) обязаны давать r = 1.
"""
import numpy as np
from scipy.linalg import eigvalsh
from scipy.stats import kstest

from engine.hamiltonian import central_band, unfold_poly, window_u
from engine.solver import gue_spectrum


# ── окна и тренды ────────────────────────────────────────────────────────────
def rampless(w):
    """Убрать линейный рампу (МНК)."""
    w = np.asarray(w, dtype=float)
    n = np.arange(w.size, dtype=float)
    c = np.polyfit(n, w, 1)
    return w - np.polyval(c, n)


def corr_shift(gate_w, zeros_w, span=1.0, step=0.05):
    """r_H7: max по дробному сдвигу s (в уровнях) корреляции безрампных окон.
    Сдвиг реализуется линейной интерполяцией нулевого окна; при несовпадении
    длин развёрнутые координаты растягиваются (единичная плотность)."""
    g = rampless(gate_w)
    z = rampless(zeros_w)
    ng, nz = g.size, z.size
    if ng != nz:
        z = np.interp(np.linspace(0.0, nz - 1.0, ng),
                      np.arange(nz, dtype=float), z)
    n = g.size
    idx = np.arange(n, dtype=float)
    best_r, best_s = -2.0, 0.0
    for s in np.arange(-span, span + 1e-12, step):
        zs = np.interp(idx + s, idx, z, left=z[0], right=z[-1])
        r = float(np.corrcoef(g, zs)[0, 1])
        if r > best_r:
            best_r, best_s = r, float(s)
    return best_r, best_s


def rank_profile(window):
    """Нормированный ранговый профиль окна (для D_nn)."""
    w = rampless(window)
    return w / (np.linalg.norm(w) + 1e-30)


def d_nn(gate_w, zeros_w):
    """D_nn: минимальный среднеквадратичный остаток нормированных
    безтрендовых профилей по НЕциклическим сдвигам (общие перекрытия).

    Исправление v2.0.1 (баг v2.0): прежняя версия использовала np.roll —
    ЦИКЛИЧЕСКИЙ сдвиг — на нециклическом (детрендированном) профиле;
    заворот края создавал ложные краевые разрывы и фиктивную
    минимизацию. Здесь сдвиг реализован перекрытием без заворота.

    КАЛИБРОВКА (v2.0.1): метрика ОГРАНИЧЕНА — профили нормированы на
    единичную норму, поэтому её область значений разбита на два режима:
      * тождественные объекты      ~1e-14…1e-10 (машинная точность);
      * ЛЮБАЯ нетождественная пара ~2/n (n — длина окна; ≈0.008 при
        n=200) — GUE-суррогаты, сдвинутые окна нулей и затворы сидят
        на одном уровне. До исправления завороты края раздували этот
        уровень до 0.23–0.29 (закоммиченные числа C3), но отношение
        «затвор/суррогат» оставалось ≈ 1.0.
    Отсюда: «порядки величины» по D_nn НЕ ОПРЕДЕЛЕНЫ — прежний
    «разрыв 9–10 порядков» сравнивал уровень насыщения с машинным
    нулём контролей (1e-10), т.е. ошибку категории. Честная
    шкала — z-оценка против суррогатного нуля: d_nn_null_stats().
    """
    g, z = rank_profile(gate_w), rank_profile(zeros_w)
    ng, nz = g.size, z.size
    best = np.inf
    span = min(ng, nz) // 2
    for s in range(-span, span + 1):
        i0 = max(0, -s)
        i1 = min(ng, nz - s)
        m = i1 - i0
        if m < 8:            # слишком короткое перекрытие пропускаем
            continue
        gs = g[i0:i1]
        zs = z[i0 + s:i1 + s]
        d = float(np.mean((gs - zs) ** 2))
        if d < best:
            best = d
    return float(best)


def d_nn_null_stats(zref, n_surr=40, k=200, seed=77):
    """Суррогатный нуль D_nn: (mean, std) по n_surr GUE-матрицам.

    Правильная точка отсчёта для «расстояния» в D_nn — не пол
    позитивных контролей (машинная точность тождества), а уровень
    насыщения случайных пар ≈ 2/n. Интерпретация отношения
    D_nn(объект)/mean(D_nn_null):
      ~1.0  — объект неотличим от случайного (нулевая зона);
      < 0.7 — заметное совпадение профиля (частичный сигнал);
      ~0    — тождество (уровень PC1/PC2).
    Возвращаемое std даёт z-оценку: (D_nn − mean)/std.
    Санити-проверка v2.0.1 на реальных данных: null = 0.0079 ± 0.0004,
    затвор Nv=16 = 0.0079 → отношение 0.99 (нулевая зона подтверждена).
    """
    vals = []
    for j in range(n_surr):
        ev = gue_spectrum(576, seed + j)
        w, _, _ = spectrum_window(ev, k)
        vals.append(d_nn(w, zref.window))
    return float(np.mean(vals)), float(np.std(vals))


# ── нули ─────────────────────────────────────────────────────────────────────
class ZeroReference:
    """Единый нулевой эталон v2 (внутренний кэш, детерминизм).

    v2-конвенция (документирована в docs/v2): и затвор, и нули проходят
    ОДИН конвейер (центральная полоса 0.6 → развёртка poly-6 → окно),
    поэтому развёрнутое сравнивается с развёрнутым; изоспектральный
    объект обязан давать r_H7 = 1 (PC0'). Сырое окно сохраняется для
    следовых метрик и совместимости с v1.
    """

    def __init__(self, gamma, k0=224, k_seg=240, k_win=200):
        self.gamma = np.asarray(gamma, dtype=float)
        self.k0, self.k_seg, self.k_win = k0, k_seg, k_win
        self.seg = self.gamma[k0:k0 + k_seg]
        self.window_raw = self.seg - self.seg[0]
        u = unfold_poly(self.seg)
        kw = min(k_win, u.size - 12)
        w = window_u(u, kw)
        self.window = w                      # развёрнутое окно (v2-конвенция)

    def random_windows(self, n_windows=64, seed=4242, unfolded=True):
        """Перестановочный нуль: n случайных окон того же объёма."""
        rng = np.random.default_rng(seed)
        out = []
        hi = self.gamma.size - self.k_seg - 1
        for _ in range(n_windows):
            i = int(rng.integers(0, hi))
            if unfolded:
                out.append(window_u(unfold_poly(self.gamma[i:i + self.k_seg]),
                                    self.window.size))
            else:
                out.append(self.gamma[i:i + self.k_seg] - self.gamma[i])
        return out


# ── затворные спектры ────────────────────────────────────────────────────────
def spectrum_window(eigs, k=200, frac=0.6):
    """центральная полоса → развёртка → окно k уровней (протокол C3)."""
    cen = central_band(np.asarray(eigs, dtype=float), frac)
    return window_u(unfold_poly(cen), k), float(np.mean(np.diff(cen))), cen


def r_H7(eigs, zref, k=200):
    """Ранговая проекция: r_H7 + оптимальный сдвиг."""
    w, mean_sp, _ = spectrum_window(np.asarray(eigs), k)
    r, s = corr_shift(w, zref.window)
    return r, s, w, mean_sp


def null_pvalue(r_obs, null_rs):
    """p = (1 + #{null ≥ r}) / (1 + n) — протокол C3."""
    null_rs = np.asarray(null_rs, dtype=float)
    return float((1.0 + np.sum(null_rs >= r_obs)) / (1.0 + null_rs.size))


def gue_null_stats(zref, n_gue=40, k=200, seed=77):
    """GUE-нуль протокола: (mean, std) r_H7 по n_gue РАЗЛИЧНЫМ матрицам."""
    rs = []
    for j in range(n_gue):
        ev = gue_spectrum(576, seed + j)
        w, _, _ = spectrum_window(ev, k)
        rs.append(corr_shift(w, zref.window)[0])
    return float(np.mean(rs)), float(np.std(rs))


# ── класс статистики (C8-протокол) ──────────────────────────────────────────
def spacing_ratio_mean(eigs, frac=0.6):
    """⟨r⟩ = ⟨min(δ_i,δ_{i+1})/max(δ_i,δ_{i+1})⟩ в центральной полосе."""
    cen = central_band(np.asarray(eigs, dtype=float), frac)
    d = np.diff(cen)
    d = d[d > 0]
    return float(np.mean(np.minimum(d[:-1], d[1:])
                         / np.maximum(d[:-1], d[1:])))


def gue_class_verdict(eigs, r_gue=0.5996, tol=0.03):
    """Вердикт класса: GUE при |⟨r⟩ − 0.5996| ≤ tol (C8-константы)."""
    r = spacing_ratio_mean(eigs)
    return r, bool(abs(r - r_gue) <= tol)


# ── суррогатный нуль тепловой метрики (v1-протокол, переиспользование) ──────
def ef_fluct_corr(D, P):
    """r_EF на детрендированных кривых (v2-конвенция): корреляция ФЛУКТУАЦИЙ
    теплового следа и простой гребёнки — сырая корреляция v1 слишком легко
    ловит общий тренд двух гладких кривых."""
    from hpbridge.metrics_v2 import rampless
    return float(np.corrcoef(rampless(D), rampless(P))[0, 1])


def ef_report2(window, U, P):
    """Полный v2-отчёт тепловой проекции: D(u), r_raw (v1), r_fluct (v2)."""
    from hpbridge.traceformula import heat_trace_fluct
    D = heat_trace_fluct(np.asarray(window, dtype=float), U)
    from hpbridge.traceformula import fit_corr
    r_raw, _, c = fit_corr(D, P)
    return {"D": D, "r_raw": float(r_raw), "coef": float(c),
            "r_fluct": ef_fluct_corr(D, P)}


def ef_report(D, P, ndraw=120, seed0=1234):
    """Полный отчёт r_EF: корреляция при фикс. масштабе, остаток, нуль."""
    from hpbridge.traceformula import fit_corr, resid_rel, surrogate_null
    r, _, c = fit_corr(D, P)
    res = resid_rel(D, P)
    m, s = surrogate_null(D, P, ndraw, seed0=seed0)
    return {"r_EF": r, "coef": c, "resid_rel": res,
            "null_mean": m, "null_std": s}


def ks_vs_reference(sample, reference):
    """Двухвыборочный KS: зазоры объекта против эталонных зазоров."""
    from scipy.stats import ks_2samp
    s = np.asarray(sample, dtype=float)
    r = np.asarray(reference, dtype=float)
    out = ks_2samp(s, r, alternative="two-sided", method="asymp")
    return float(out.statistic), float(out.pvalue)
