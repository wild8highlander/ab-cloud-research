"""
t34_engine.py — верный Python-порт модели AB-Cloud v23 и протокола Теста 34
(direct AB vs ζ, HARDCORE pass 2, test36b_ab_vs_zeta_hardcore) для
масштабной развёртки параметров вихрей.

Источники (repo wild8highlander/ab-cloud-research):
  * build_ab_cloud_hamiltonian        — ab_cloud_v23.jl:2975  (модель :monumental)
  * ab_phase_vortex_monumental        — ab_cloud_v23.jl:2765
  * vortex_onsite_potential           — ab_cloud_v23.jl:2790
  * random_vortex_configuration       — ab_cloud_v23.jl:4228 (place_at_centers=true)
  * central_band_eigs                 — ab_cloud_v23.jl:3270 (frac=0.6)
  * normalized_spacings (ζ unfolding) — ab_cloud_v23.jl:1828
  * ks2sample / pair_corr_R2 / вердикт — test36b_ab_vs_zeta_hardcore:27563
Референсный прогон: run_20260914_234626/test_34_direct_vs_zeta
  96×96 open, α=0.5, t=1, W_eff=1.0, Nv=2, q=1.0, n=5 real → D=0.1096

Совместимость: bit-exact воспроизведение Julia невозможно (другие PRNG/BLAS),
как и оговорено в python_clone/abcloud/core.py; воспроизводится СЕМАНТИКА
(та же статистика, те же окна, тот же вердикт).
"""
from __future__ import annotations

import numpy as np
from scipy.linalg import eigvalsh

# ── Константы протокола (Julia defaults, двухпроходный режим) ────────────────
BASE_SEED = 96            # cfg.ab_seed
HARDCORE_OFFSET = 3500    # MersenneTwister(ab_seed + 3500) — vortex RNG stream
ALPHA_DEFAULT = 0.5       # критическая линия
T_HOP = 1.0               # cfg.ab_t
W_EFF = 1.0               # ab_w_eff = min(ab_W=4.0, ab_W_max=1.0)
CENTER_FRACTION = 0.6     # cfg.ab_center_fraction
UNFOLD_WINDOW = 0.05      # cfg.ab_unfold_window
N_REAL = 5                # ab_n_realizations / ab_hc_nreal (прогон: n=5)
EPS_AMP = 0.02            # ε ~ U(−0.01, 0.01) → (rand−0.5)*0.02 при W>0

R_MEAN_GUE = 0.5996       # Atas et al. 2013 (константы сьюта)
R_MEAN_POISSON = 0.3863


def malloc_trim():
    """Возврат glibc-арен ОС (аналог ab_gc! оригинала; без него серии
    диагонализаций удерживают гигабайты в аренах — см. комментарий Julia)."""
    try:
        import ctypes
        ctypes.CDLL("libc.so.6").malloc_trim(0)
    except Exception:
        pass


# ── Вихри ────────────────────────────────────────────────────────────────────
def random_vortex_configuration(Nv: int, Nx: int, Ny: int, q_mag: float,
                                rng: np.random.Generator,
                                placement: str = "protocol"):
    """Порт random_vortex_configuration (place_at_centers=true, нейтральность).

    protocol: случайные центры ячеек (ix+0.5, iy+0.5), ix,iy ∈ 1..N−1 —
              точный протокол Теста 34.
    regular:  упорядоченная решётка вихрей с чередованием зарядов
              (монография §4.2, фиксированная конфигурация).
    cluster:  вихри стянуты к центру решётки (гауссов джиттер σ=L/10).
    Заряды: чётный Nv → первые Nv/2 = +q, остальные −q (нейтральность);
            нечётный → (Nv+1)/2 положительных (|net|=1, минимальный дисбаланс).
    """
    vortices = []
    if placement == "protocol":
        for k in range(Nv):
            ix = int(rng.integers(1, Nx))      # rand(rng, 1:Nx-1)
            iy = int(rng.integers(1, Ny))
            x, y = float(ix) + 0.5, float(iy) + 0.5
            q = q_charge(k, Nv, q_mag)
            vortices.append((x, y, q))
    elif placement == "regular":
        side = int(np.ceil(np.sqrt(Nv)))
        xs = np.linspace(1.5, Nx - 0.5, side)
        ys = np.linspace(1.5, Ny - 0.5, side)
        coords = [(x, y) for y in ys for x in xs][:Nv]
        for k, (x, y) in enumerate(coords):
            vortices.append((float(x), float(y), q_charge(k, Nv, q_mag)))
    elif placement == "cluster":
        cx, cy = Nx / 2.0, Ny / 2.0
        for k in range(Nv):
            x = float(np.clip(cx + rng.normal(0, Nx / 10.0), 1.5, Nx - 0.5))
            y = float(np.clip(cy + rng.normal(0, Ny / 10.0), 1.5, Ny - 0.5))
            vortices.append((x, y, q_charge(k, Nv, q_mag)))
    else:
        raise ValueError(placement)
    return vortices


def q_charge(k: int, Nv: int, q_mag: float) -> float:
    if Nv % 2 == 0:
        return q_mag if k < Nv // 2 else -q_mag
    return q_mag if k < (Nv + 1) // 2 else -q_mag


# ── Гамильтониан (:monumental, векторизованный порт) ─────────────────────────
def build_ab_cloud_hamiltonian(Nx: int, Ny: int, vortices, alpha: float,
                               t: float, W: float, bc: str,
                               rng_dis: np.random.Generator,
                               order: str = "C") -> np.ndarray:
    """Верный порт build_ab_cloud_hamiltonian (model=:monumental).

    * x-хоп (ix→ix+1, строка iy): φ = 2π·α·iy  (iy 1-based, Landau gauge)
    * y-хоп (iy→iy+1): φ = Σ_k q_k·(θ_j − θ_i)·0.5, θ = atan2(y−y_k, x−x_k),
      спец-случай (0,0) → 0 (np.arctan2(0,0)=0 — совпадает с Julia);
    * on-site: V_i = Σ_k q_k·W/(r_i²·N⁻¹ + 1) + ε_i ~ U(−0.01,0.01) при W>0;
    * открытые границы: без wrap-связей; торус: assert α·Ny ∈ ℤ (как в Julia);
    * Эрмитовость — по построению (H[i,j]=−t·e^{iφ}, H[j,i]=−t·e^{−iφ}).
    """
    N = Nx * Ny
    if bc == "torus" and abs(alpha * Ny - round(alpha * Ny)) > 1e-10:
        raise AssertionError(f"torus needs α·Ny ∈ ℤ, got {alpha * Ny}")

    ix = np.arange(Nx, dtype=np.float64)
    iy1 = np.arange(1, Ny + 1, dtype=np.float64)          # 1-based
    XX, YY = np.meshgrid(ix + 1.0, iy1)                   # координаты сайтов (1..N)
    XX = XX.ravel()                                       # порядок i=(iy-1)*Nx+ix
    YY = YY.ravel()

    H = np.zeros((N, N), dtype=np.complex128, order=order)
    torus = (bc == "torus")

    # ── x-хопы: пары (i, i+1) внутри строк; открытая решётка: ix=1..Nx−1
    rows = np.repeat(np.arange(Ny), Nx - 1)
    cols_in_row = np.tile(np.arange(Nx - 1), Ny)
    i_from = rows * Nx + cols_in_row
    i_to = i_from + 1
    phi_x = 2.0 * np.pi * alpha * (rows + 1.0)            # iy = row+1 (1-based)
    if torus:  # wrap-связь (Nx, iy) → (1, iy), фаза Ландау та же (vortex — только y-хопы)
        rows_w = np.arange(Ny)
        i_from = np.concatenate((i_from, rows_w * Nx + (Nx - 1)))
        i_to = np.concatenate((i_to, rows_w * Nx + 0))
        phi_x = np.concatenate((phi_x, 2.0 * np.pi * alpha * (rows_w + 1.0)))
    H[i_from, i_to] = -t * np.exp(1j * phi_x)
    H[i_to, i_from] = -t * np.exp(-1j * phi_x)

    # ── y-хопы: пары (i, i+Nx), iy=1..Ny−1; для торуса wrap (ix, Ny)→(ix, 1)
    # с НЕРАЗВЁРНУТОЙ верхней координатой (ix, Ny+1) и фазой 2πα·Ny (≡ 0 mod 2π)
    i_from = np.arange((Ny - 1) * Nx)
    i_to = i_from + Nx
    phi_y = np.zeros((Ny - 1) * Nx)
    for (vx, vy, qk) in vortices:
        dx = XX - vx
        dy = YY - vy
        theta = np.arctan2(dy, dx)                        # atan2(0,0)=0 ✓
        phi_y += qk * (theta[i_to] - theta[i_from]) * 0.5
    if torus:
        i_fw = (Ny - 1) * Nx + np.arange(Nx)
        i_tw = np.arange(Nx)
        phi_w = np.full(Nx, 2.0 * np.pi * alpha * Ny)
        for (vx, vy, qk) in vortices:
            th_bot = np.arctan2(Ny - vy, np.arange(1, Nx + 1) - vx)
            th_top = np.arctan2(Ny + 1.0 - vy, np.arange(1, Nx + 1) - vx)  # unwrapped
            phi_w += qk * (th_top - th_bot) * 0.5
        i_from = np.concatenate((i_from, i_fw))
        i_to = np.concatenate((i_to, i_tw))
        phi_y = np.concatenate((phi_y, phi_w))
    H[i_from, i_to] = -t * np.exp(1j * phi_y)
    H[i_to, i_from] = -t * np.exp(-1j * phi_y)

    # ── on-site: вихревой кулоновский потенциал + ε
    V = np.zeros(N)
    if W > 0 and vortices:
        for (vx, vy, qk) in vortices:
            r2 = (XX - vx) ** 2 + (YY - vy) ** 2
            V += qk * W / (r2 / N + 1.0)
        V += (rng_dis.random(N) - 0.5) * EPS_AMP
        H[np.arange(N), np.arange(N)] += V.astype(np.complex128)
    elif W > 0:  # Nv=0, W>0: только ε (как в Julia: vortex term пуст, ε активен)
        V += (rng_dis.random(N) - 0.5) * EPS_AMP
        H[np.arange(N), np.arange(N)] += V.astype(np.complex128)

    return H
    # Примечание: Julia делает H=(H+H†)/2; здесь H эрмитов по построению
    # (каждая пара задана ровно один раз сопряжёнными значениями), поэтому
    # симметризация — тождественная операция. herm_defect проверяется в тестах.


# ── Статистика (порты 1:1) ───────────────────────────────────────────────────
def central_band_eigs(sorted_eigs: np.ndarray, frac: float) -> np.ndarray:
    """Порт central_band_eigs (fld-арифметика Julia)."""
    n = len(sorted_eigs)
    if n == 0:
        return sorted_eigs[:0]
    frac = min(max(frac, 0.05), 1.0)
    if frac >= 1.0:
        return sorted_eigs.copy()
    half = (n * frac) // 2                                # Int(fld(n*frac, 2))
    half = int(half)
    j_lo = max(0, n // 2 - half)                          # 0-based
    j_hi = min(n, n // 2 + half)
    return sorted_eigs[j_lo:j_hi]


def unfold_spacings(central: np.ndarray, window_frac: float = UNFOLD_WINDOW):
    """Скользяще-оконная развёртка Теста 34: s_i = δ_i / mean(окно), окно
    win = max(5, round(0.05·n_cent)), фильтр 0<s<10, нормировка на среднее."""
    n_cent = len(central)
    win = max(5, int(round(window_frac * n_cent)))
    d = np.diff(central)
    # локальное среднее по δ[j], j ∈ [i−win, i+win−1] (0-based порт Julia-окна
    # [j_lo, j_hi] по 1-based d: j_lo=max(1,i−win), j_hi=min(n_cent−1,i+win))
    idx = np.arange(n_cent - 1)
    j_lo = np.maximum(0, idx - win)
    j_hi = np.minimum(n_cent - 2, idx + win - 1)
    # префиксные суммы для среднего окна
    cs2 = np.concatenate(([0.0], np.cumsum(d)))
    counts = (j_hi - j_lo + 1).astype(np.float64)
    sums = cs2[j_hi + 1] - cs2[j_lo]
    lm = sums / counts
    ok = lm > 1e-12
    sp = d[ok] / lm[ok]
    sp = sp[(sp > 0) & (sp < 10)]
    if len(sp) > 50:
        sp = sp / sp.mean()
        return sp
    return np.empty(0)


def normalized_spacings(zeros: np.ndarray) -> np.ndarray:
    """Порт normalized_spacings (ζ-сторона): s_k = Δγ·log(γ_k/2π)/2π."""
    g = zeros
    sp = (g[1:] - g[:-1]) * np.log(g[:-1] / (2 * np.pi)) / (2 * np.pi)
    sp = sp[(sp > 0) & (sp < 10)]
    if len(sp):
        sp = sp / sp.mean()
    return sp


def ks2sample(x: np.ndarray, y: np.ndarray):
    """Порт ks2sample Теста 34 (двухвыборочный KS + асимптотическое p)."""
    xs = np.sort(x)
    ys = np.sort(y)
    nx, ny = len(xs), len(ys)
    allv = np.concatenate((xs, ys))
    allv.sort(kind="mergesort")
    # позиции: число элементов ≤ v с каждой стороны (как в Julia-цикле)
    ix = np.searchsorted(xs, allv, side="right")
    iy = np.searchsorted(ys, allv, side="right")
    D = np.max(np.abs(ix / nx - iy / ny))
    n_eff = np.sqrt(nx * ny / (nx + ny))
    lam = (n_eff + 0.12 + 0.11 / n_eff) * D
    k = np.arange(1, 201)
    p = np.sum((-1.0) ** (k + 1) * np.exp(-2 * k * k * lam * lam))
    return float(D), float(min(max(2 * p, 0.0), 1.0))


def pair_corr_R2(pos: np.ndarray, s_max: float = 4.0, ds: float = 0.05):
    """Порт pair_corr_R2 (Patch C: вложенные циклы, inner-break, полная
    разрешающая способность). pos = cumsum([0; sp]) — позиции по возрастанию.
    Julia-биннинг: b = fld(d, ds) + 1 ∈ [1, n_bins] → бин [0, ds) включён."""
    n_bins = int(s_max // ds)
    hist = np.zeros(n_bins)
    M = len(pos)
    for i in range(M - 1):
        hi = np.searchsorted(pos, pos[i] + s_max, side="left")
        if hi <= i + 1:
            continue
        d = pos[i + 1:hi] - pos[i]
        b = np.floor(d / ds).astype(np.int64)             # fld(d, ds) ∈ [0, n_bins−1]
        b = b[(b >= 0) & (b < n_bins)]
        np.add.at(hist, b, 1)
    s_grid = (np.arange(n_bins) + 0.5) * ds
    return s_grid, hist / (M * ds)


def mean_adjacent_r(ev: np.ndarray) -> float:
    """⟨r⟩ Оганесяна-Хьюза по сырым расстояниям центральной полосы."""
    d = np.diff(ev)
    if len(d) < 2:
        return float("nan")
    a, b = d[:-1], d[1:]
    mx = np.maximum(a, b)
    ok = mx > 0
    return float(np.mean(np.minimum(a, b)[ok] / mx[ok]))


# ── Полный протокол Теста 34b для одной конфигурации ────────────────────────
def run_config(Nv: int, q: float, W: float, alpha: float, L: int, bc: str,
               placement: str = "protocol", n_real: int = N_REAL,
               seed_base: int = BASE_SEED, eig_kwargs: dict | None = None,
               zeta_unf: np.ndarray | None = None,
               keep_R2: bool = False, r2_params=(4.0, 0.05)):
    """Прогон протокола Теста 34b (HARDCORE): n_real реализаций, pooled KS vs ζ,
    R₂-метрики, ⟨r⟩, per-realization стабильность. Возвращает dict метрик."""
    eig_kwargs = eig_kwargs or {"check_finite": False, "driver": "evr",
                                "overwrite_a": True}
    if zeta_unf is None:
        zeta_unf = ZETA_UNF
        assert zeta_unf is not None, "вызовите load_zeta() до run_config()"
    vortex_rng = np.random.default_rng(seed_base + HARDCORE_OFFSET)
    ab_all = []
    per_real_D = []
    r_means = []
    R2_first = None
    for k in range(1, n_real + 1):
        vortices = random_vortex_configuration(Nv, L, L, q, vortex_rng,
                                               placement) if Nv > 0 else []
        dis_rng = np.random.default_rng(seed_base + HARDCORE_OFFSET + k)
        H = build_ab_cloud_hamiltonian(L, L, vortices, alpha, T_HOP, W, bc,
                                       dis_rng)
        ev = eigvalsh(H, **eig_kwargs)                    # values-only, in-place
        ev.sort()
        central = central_band_eigs(ev, CENTER_FRACTION)
        r_means.append(mean_adjacent_r(central))
        sp = unfold_spacings(central)
        if len(sp) > 50:
            ab_all.append(sp)
            D_k, _ = ks2sample(sp, zeta_unf)
            per_real_D.append(D_k)
            if keep_R2 and R2_first is None:
                s_grid, R2_k = pair_corr_R2(np.concatenate(([0.0], np.cumsum(sp))),
                                            *r2_params)
                R2_first = (s_grid, R2_k)
        del H, ev
    ab_pooled = np.concatenate(ab_all)
    D_pooled, p_pooled = ks2sample(ab_pooled, zeta_unf)
    pos = np.concatenate(([0.0], np.cumsum(ab_pooled)))
    s_grid, R2_ab = pair_corr_R2(pos, *r2_params)
    R2_gue = 1.0 - (np.sin(np.pi * s_grid) / (np.pi * s_grid)) ** 2
    mean_dR2 = float(np.mean(np.abs(R2_ab - R2_ZETA_CACHE)))
    d_gue = float(np.mean(np.abs(R2_ab - R2_gue)))
    d_pois = float(np.mean(np.abs(R2_ab - 1.0)))
    per_real_D.sort()
    res = {
        "L": L, "Nv": Nv, "q": q, "W": W, "alpha": alpha, "bc": bc,
        "placement": placement, "n_real": n_real, "seed_base": seed_base,
        "n_spacings": int(len(ab_pooled)),
        "D_pooled": D_pooled, "p_pooled": p_pooled,
        "D_min": per_real_D[0], "D_med": float(np.median(per_real_D)),
        "D_max": per_real_D[-1],
        "mean_abs_dR2": mean_dR2, "d_GUE": d_gue, "d_Pois": d_pois,
        "r_mean": float(np.mean(r_means)),
        "ks_pass": bool((p_pooled > 0.01) or (D_pooled < 0.10)),
        "r2_pass": bool(mean_dR2 < 0.10),
        "gue_closer": bool(d_gue < d_pois),
        "stab_pass": bool((per_real_D[-1] - per_real_D[0]) < 0.10),
        "runtime_s": 0.0,
    }
    res["composite_ok"] = bool(res["ks_pass"] and res["r2_pass"] and
                               res["gue_closer"] and res["stab_pass"])
    if keep_R2:
        res["_R2"] = (s_grid, R2_ab, R2_first)
    return res


# ── ζ-справочник (инициализируется один раз) ────────────────────────────────
R2_ZETA_CACHE = None
ZETA_UNF = None


def load_zeta(path: str):
    global ZETA_UNF, R2_ZETA_CACHE
    vals = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                vals.extend(float(x) for x in line.split())
    zs = np.array(vals)
    assert len(zs) == 50000, f"ожидалось 50000 нулей, получено {len(zs)}"
    ZETA_UNF = normalized_spacings(zs)
    s_grid, R2_z = pair_corr_R2(np.concatenate(([0.0], np.cumsum(ZETA_UNF))),
                                4.0, 0.05)
    R2_ZETA_CACHE = R2_z
    return zs


def gue_control(L: int, n_real: int = 3, seed: int = 777) -> dict:
    """Статистический пол: GUE-матрица размера L² через ТОТ ЖЕ конвейер
    (центральная полоса 0.6, та же развёртка, pooled KS vs ζ). Даёт якорь
    «если бы AB был идеально GUE» для данного L и честное сравнение между L."""
    rng = np.random.default_rng(seed)
    sps, n = [], L * L
    for _ in range(n_real):
        X = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
        H = (X + X.conj().T) / 2
        del X
        ev = eigvalsh(H, check_finite=False, driver="evr", overwrite_a=True)
        ev.sort()
        central = central_band_eigs(ev, CENTER_FRACTION)
        sp = unfold_spacings(central)
        if len(sp) > 50:
            sps.append(sp / sp.mean())
        del H, ev
    pooled = np.concatenate(sps)
    D, p = ks2sample(pooled, ZETA_UNF)
    pos = np.concatenate(([0.0], np.cumsum(pooled)))
    s_grid, R2_g = pair_corr_R2(pos, 4.0, 0.05)
    R2_theory = 1.0 - (np.sin(np.pi * s_grid) / (np.pi * s_grid)) ** 2
    return {"L": L, "n_real": n_real, "n_spacings": len(pooled),
            "D_gue_vs_zeta": D, "p": p,
            "mean_abs_dR2_cal": float(np.mean(np.abs(R2_g - R2_theory))),
            "mean_abs_dR2_vs_zeta": float(np.mean(np.abs(R2_g - R2_ZETA_CACHE)))}
