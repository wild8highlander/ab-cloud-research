"""hpbridge.qinfo — квантово-информационный слой (C16, пункт 13, T18).

Корректный объект для одночастичных гамильтонианов — ФЕРМИОННАЯ
запутанность слейтеровского морского уголка: заполняем n нижних орбиталей,
корреляционная матрица C_A = P_A (Σ_occ ψψ†) P_A на половине решётки,
спектр λ ∈ [0,1] даёт S_vN = −Σλ ln λ − Σ(1−λ)ln(1−λ) (Peschel).

Q1  S_vN(filling) затвора против GUE-базы (Haar-подобные орбитали);
Q2  взаимная информация I(A:B)(filling); корреляция MI-профиля с нулевым
    окном против случайного окна — «видит ли MI нули»;
Q3  спектральный форм-фактор: наклон рампы (квантовая сложность спектра)
    затвора против GUE и против H_ξ-окна нулей.
"""
import numpy as np
from scipy.linalg import eigh


def fermi_correlations(vecs, occ):
    """Матрица корреляций C[s,s'] = Σ_{n<occ} ψ_n(s)ψ*_n(s')."""
    return (vecs[:, :occ] @ vecs[:, :occ].conj().T)


def region_entropy(C_sub):
    """S_vN и вклады из спектра корреляционной матрицы области."""
    lam = np.linalg.eigvalsh(C_sub)
    lam = np.clip(lam.real, 1e-12, 1 - 1e-12)
    S = float(-np.sum(lam * np.log(lam) + (1 - lam) * np.log(1 - lam)))
    return S, lam


def s_profile(H, L, fillings=(0.25, 0.4, 0.5, 0.6, 0.75)):
    """S_vN и MI половинок (левые L//2 столбца) по уровням заполнения."""
    N = L * L
    ev, vec = eigh(H, check_finite=False)
    idx_A = np.array([iy * L + ix for iy in range(L) for ix in range(L // 2)])
    idx_B = np.array([iy * L + ix for iy in range(L) for ix in range(L // 2, L)])
    out = []
    for f in fillings:
        occ = max(2, int(N * f))
        C = fermi_correlations(vec, occ)
        SA, _ = region_entropy(C[np.ix_(idx_A, idx_A)])
        SB, _ = region_entropy(C[np.ix_(idx_B, idx_B)])
        SAB, _ = region_entropy(C)
        out.append({"filling": f, "S_A": SA, "S_B": SB, "S_AB": SAB,
                    "MI": SA + SB - SAB})
    return out


def page_fermion_baseline(L, fillings=(0.25, 0.4, 0.5, 0.6, 0.75),
                          reps=30, seed=31337):
    """Фермионная база Пейджа: морской уголок из HAAR-орбиталей (GUE)."""
    from engine.solver import gue_spectrum
    rng = np.random.default_rng(seed)
    idx_A = np.array([iy * L + ix for iy in range(L) for ix in range(L // 2)])
    idx_B = np.array([iy * L + ix for iy in range(L)
                      for ix in range(L // 2, L)])
    accS, accMI = [], []
    for k in range(reps):
        ev, vec = eigh(np.array(gue_spectrum_matrix(rng, L * L)),
                       check_finite=False)
        row = []
        for f in fillings:
            occ = max(2, int(L * L * f))
            C = fermi_correlations(vec, occ)
            SA, _ = region_entropy(C[np.ix_(idx_A, idx_A)])
            SB, _ = region_entropy(C[np.ix_(idx_B, idx_B)])
            SAB, _ = region_entropy(C)
            row.append((SA + SB - SAB))
        accMI.append(row)
    arr = np.array(accMI)
    return arr.mean(axis=0), arr.std(axis=0)


def gue_spectrum_matrix(rng, n):
    X = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
    return (X + X.conj().T) / 2


def mi_alignment(H, L, zero_profile, k=64):
    """MI-профиль (скользящее заполнение в центральной полосе) против
    рангового профиля нулевого окна и случайного окна."""
    N = L * L
    ev, vec = eigh(H, check_finite=False)
    idx_A = np.array([iy * L + ix for iy in range(L) for ix in range(L // 2)])
    idx_B = np.array([iy * L + ix for iy in range(L)
                      for ix in range(L // 2, L)])
    n = ev.size
    half = int((n * 0.6) // 2)
    sel = np.linspace(n // 2 - half, n // 2 + half - 1, k).astype(int)
    MI = []
    for j in sel:
        occ = max(2, j)
        C = fermi_correlations(vec, occ)
        SA, _ = region_entropy(C[np.ix_(idx_A, idx_A)])
        SB, _ = region_entropy(C[np.ix_(idx_B, idx_B)])
        SAB, _ = region_entropy(C)
        MI.append(SA + SB - SAB)
    MI = np.array(MI)
    MI_n = (MI - MI.mean()) / MI.std()
    zw = np.asarray(zero_profile, dtype=float)
    zw = np.interp(np.linspace(0, 1, k), np.linspace(0, 1, zw.size),
                   (zw - zw.mean()) / zw.std())
    corr_zero = float(np.corrcoef(MI_n, zw)[0, 1])
    rng = np.random.default_rng(99)
    rnd = rng.standard_normal(k)
    corr_rnd = float(np.corrcoef(MI_n, rnd)[0, 1])
    return {"MI_mean": float(MI.mean()), "MI_std": float(MI.std()),
            "corr_MI_vs_zerowindow": corr_zero,
            "corr_MI_vs_random": corr_rnd, "MI_profile": MI.tolist()}


def spectral_form_factor(eigs, t_grid, unfolding=True):
    """SFF(t) = |Σ e^{−iE_n t}|²; вход — уже развёрнутое окно (window_u).
    Параметр unfolding — ЛИНЕЙНАЯ стандартизация (E−⟨E⟩)/std, а не
    развёртка (исправление подписи v2.0.1; развёртку выполняет
    вызывающий код через central_band → unfold_poly → window_u)."""
    E = np.asarray(eigs, dtype=float)
    if unfolding:
        E = (E - E.mean()) / E.std()
    out = np.empty(t_grid.size)
    for i, t in enumerate(t_grid):
        z = np.sum(np.exp(-1j * E * t))
        out[i] = float(np.abs(z) ** 2)
    return out


def sff_ramp_slope(eigs, t_grid):
    """Наклон линейной рампы SFF ВНУТРИ роста (до плато Гейзенберга):
    1 для GUE-класса, ~0 для Пуассона, жёсткий ранний рост у нулей."""
    sff = spectral_form_factor(eigs, t_grid)
    N = eigs.size
    t_h = 2 * np.pi * N / (eigs.max() - eigs.min())
    mask = (t_grid > 0.25 * t_h) & (t_grid < 0.75 * t_h)
    if mask.sum() < 3:
        return float("nan")
    c = np.polyfit(t_grid[mask], sff[mask], 1)
    return float(c[0] / N)
