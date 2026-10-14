# -*- coding: utf-8 -*-
"""rpbridge.fullham — Решение 16 (V16): полный гамильтониан × полная
алгебраическая функция критической прямой.

Ключевой сдвиг относительно V1–V15: мы НЕ зацикливаемся на классе GUE.
Вся предыстория серии мерила решётку статистикой (⟨r⟩, D_KS к GUE-сюрмизе).
Здесь связь решётки с арифметикой строится напрямую через ПОЛНУЮ
алгебраическую функцию критической прямой — сборку Z_id(t) = e^{iθ(t)}ζ(½+it)
из Γ-лестницы (Th-ядро эталона C1):

  * фазовый вес вихрей: q_k = θ(γ̃_k)/π, где θ(t) = Im ln Γ(¼+it/2)
    − t ln √π — риман-зигелевская тета-фаза; аргумент ζ совершает скачок π
    на каждом нуле, поэтому фазовый вес кодирует ПОЗИЦИИ нулей, а не их
    плотность;
  * ПОЛНОЕ пространство ручек гамильтониана (все ручки эталона C5):
    знаки зарядов, профиль вихря, анизотропия, стэггерд-масса, твисты,
    сдвиг флакса δα — факторный план 2·2·3·2·2·2 = 96 конфигураций
    × 3 seeds = 288 спектров 24×24;
  * метрика выравнивания r_align: корреляция Пирсона между приращениями
    развёрнутых уровней ΔU_n и приращениями ординат нулей Δγ_n на общем
    окне 200; нулевая модель — 200 пермутаций ординат (та же гладкая
    плотность, стёртая фаза); позитивный контроль — график Z_id против
    файла нулей (обязан дать r = 1.0).

Вердикт компонентный: (a) фазовый вес θ даёт r_align выше пермутационной
нулевой зоны или нет; (b) существует ли точка полного пространства ручек,
где ранговое соответствие выходит из нулевой зоны (Г2 эталона); (c) карта ручек — где
живут лучшие и худшие выравнивания.
"""
import itertools

import numpy as np
import mpmath as mp

from engine.hamiltonian import build_hamiltonian
from rpbridge import stats
from rpbridge.stats import unfold_poly
from rpbridge.zeros import load_zeros

SEEDS = (96, 196, 296)
WINDOW = 200
CALIB = 50          # первые CALIB уровней — подгонка линейного моста
mp.mp.dps = 30


# ── алгебраическая функция критической прямой ───────────────────────────────
def theta_phase(t):
    """θ(t) = Im ln Γ(¼+it/2) − t·ln√π (риман-зигелевская тета)."""
    t = mp.mpf(t)
    return float(mp.im(mp.log(mp.gamma(mp.mpf(0.25) + 1j * t / 2)))
                 - t * mp.log(mp.sqrt(mp.pi)))


def algebraic_weights(gamma_mid):
    """Фазовый вес вихрей q_k = θ(γ̃_k)/π ∈ (−1, 1) — код позиций нулей."""
    return np.array([theta_phase(g) / np.pi for g in gamma_mid])


def zid_graph(T=200.0, n_grid=4001):
    """График Z_id(t) = e^{iθ(t)}ζ(½+it) на решётке — позитивный контроль."""
    ts = np.linspace(1e-6, T, n_grid)
    vals = np.empty(n_grid)
    for i, t in enumerate(ts):
        tm = mp.mpf(float(t))
        zid = mp.e ** (1j * theta_phase(tm)) * mp.zeta(mp.mpf(0.5) + 1j * tm)
        vals[i] = float(mp.re(zid))
    return ts, vals


# ── протокол вихрей (эталон C3) ──────────────────────────────────────────────
def _vortex_protocol(L, seed, Nv=16):
    vrng = np.random.default_rng(seed + 3500)
    return [(float(vrng.integers(1, L)) + 0.5,
             float(vrng.integers(1, L)) + 0.5) for _ in range(Nv)]


def _signs(Nv, mode, q_mag, rng):
    if mode == 'neutral':
        half = Nv // 2 if Nv % 2 == 0 else (Nv + 1) // 2
        q = np.full(Nv, float(q_mag))
        q[half:] = -float(q_mag)
        return q
    if mode == 'all_plus':
        return np.full(Nv, float(q_mag))
    if mode == 'random':
        return float(q_mag) * rng.choice([-1.0, 1.0], size=Nv)
    raise ValueError(mode)


# ── один спектр полного гамильтониана ───────────────────────────────────────
def gate_spectrum_full(zeros, seed, signs='neutral', profile='site',
                       aniso=1.0, mass=0.0, twist=(0.0, 0.0), dalpha=0.0,
                       weight_mode='theta', L=24, Nv=16, q_mag=1.0, W=0.5):
    """Спектр одной точки полного пространства ручек.

    weight_mode: 'theta'  — q_k = θ(γ̃_k)/π (алгебраическая фаза);
                 'logzeta'— q_k = log|ζ(½+iγ̃_k)| (протокол V3, сравнение);
                 'none'   — q_k = 1 (чистая решётка с вихрями без веса).
    """
    pts = _vortex_protocol(L, seed, Nv)
    z = np.asarray(zeros, float)
    gamma_mid = 0.5 * (z[:Nv] + z[1:Nv + 1])
    if weight_mode == 'theta':
        wk = algebraic_weights(gamma_mid)
    elif weight_mode == 'logzeta':
        wk = np.array([float(mp.log(abs(mp.zeta(mp.mpf(0.5) + 1j * mp.mpf(g)))))
                       for g in gamma_mid])
    elif weight_mode == 'none':
        wk = np.ones(Nv)
    else:
        raise ValueError(weight_mode)
    vrng = np.random.default_rng(seed + 3502)
    qk = _signs(Nv, signs, q_mag, vrng)
    vort = [(x, y, float(qi * w)) for (x, y), qi, w in zip(pts, qk, wk)]
    drng = np.random.default_rng(seed + 3501)
    H = build_hamiltonian(L, L, vort, 0.5 + dalpha, 1.0, W, 'open', drng,
                          twist=twist, aniso=aniso, mass=mass,
                          profile=profile)
    ev = np.sort(np.linalg.eigvalsh(H))
    half = int((ev.size * 0.6) // 2)
    cen = ev[ev.size // 2 - half: ev.size // 2 + half]
    u = unfold_poly(cen)[:WINDOW]
    r = stats.adjacent_ratios(u)
    return u, stats.ks_to_gue(r), float(np.mean(r))


# ── метрика выравнивания с арифметикой ──────────────────────────────────────
def align_metric(u, zeros, start_index=0):
    """r_align: Пирсон между ΔU_n и Δγ_n (в-окно ординат) + RMSE out-of-sample.

    Линейный мост U ≈ a·γ + b подгоняется ПЕРВЫМ CALIB уровням окна,
    невязка считается на остальных (честный out-of-sample).
    """
    z = np.asarray(zeros, float)[start_index:start_index + WINDOW]
    if z.size < WINDOW:
        raise ValueError('not enough zeros')
    du = np.diff(u)
    dg = np.diff(z)
    r = float(np.corrcoef(du, dg)[0, 1])
    # линейный мост по первым CALIB точкам
    A = np.vstack([z[:CALIB], np.ones(CALIB)]).T
    coef, *_ = np.linalg.lstsq(A, u[:CALIB], rcond=None)
    pred = coef[0] * z + coef[1]
    rmse_out = float(np.sqrt(np.mean((u[CALIB:] - pred[CALIB:]) ** 2)))
    span = float(u.max() - u.min())
    return r, rmse_out / span


def permutation_null(u, zeros, n_perm=200, start_index=0, seed=96):
    """Нулевая зона r_align: пермукации приращений ординат против ΔU.

    Разрушается соответствие «уровень n ↔ нуль n», маргинальные
    распределения приращений сохраняются — та же гладкая плотность,
    стёртая фаза (в духе V1/V3).
    """
    z = np.asarray(zeros, float)[start_index:start_index + WINDOW]
    du = np.diff(np.asarray(u, float))
    dg = np.diff(z)
    rng = np.random.default_rng(seed + 9100)
    vals = []
    for _ in range(n_perm):
        p = rng.permutation(dg)
        vals.append(float(np.corrcoef(du, p)[0, 1]))
    return float(np.mean(vals)), float(np.std(vals))


# ── полный факторный план ────────────────────────────────────────────────────
def handle_grid():
    """96 конфигураций: 2 signs × 2 profile × 3 aniso × 2 mass × 2 twist
    × 2 dalpha."""
    grid = []
    for signs, profile, aniso, mass, twist, dalpha in itertools.product(
            ('neutral', 'all_plus'), ('site', 'midpoint'),
            (0.85, 1.0, 1.2), (0.0, 0.25),
            ((0.0, 0.0), (np.pi / 3, np.pi / 4)), (0.0, 0.02)):
        grid.append(dict(signs=signs, profile=profile, aniso=aniso,
                         mass=mass, twist=twist, dalpha=dalpha))
    return grid


def run(zeros, full=True):
    """Полный прогон V16.

    full=True  — 96 конфигураций × 3 seeds (≈ 2–3 мин);
    full=False — быстрый режим тестов: 6 конфигураций × 1 seed.
    """
    z = np.asarray(zeros, float)
    grid = handle_grid() if full else handle_grid()[:6]
    seeds = SEEDS if full else (96,)
    rows = []
    best_u = None
    best_row = None
    for i, cfg in enumerate(grid):
        for sd in seeds:
            u, d_ks, r_mean = gate_spectrum_full(z, sd, **cfg)
            r_al, rmse = align_metric(u, z)
            row = dict(cfg_id=i, seed=sd, **{k: str(v) for k, v in
                                             cfg.items()},
                       r_align=r_al, rmse_out=rmse, D_KS=d_ks,
                       r_mean=r_mean)
            rows.append(row)
            if best_row is None or r_al > best_row['r_align']:
                best_row = row
                best_u = u
    ra = np.array([r['r_align'] for r in rows])
    # нулевая зона: на лучшей конфигурации (честно — против её же ΔU)
    nm, nsd = permutation_null(best_u, z)
    best = best_row
    worst = min(rows, key=lambda r: r['r_align'])
    z_best = (best['r_align'] - nm) / nsd if nsd > 0 else 0.0
    # вес-сравнение: theta против logzeta против none на базовой конфигурации
    base = dict(signs='neutral', profile='site', aniso=1.0, mass=0.0,
                twist=(0.0, 0.0), dalpha=0.0)
    wcomp = {}
    for wm in ('theta', 'logzeta', 'none'):
        u, d_ks, r_mean = gate_spectrum_full(z, 96, weight_mode=wm, **base)
        r_al, rmse = align_metric(u, z)
        wcomp[wm] = dict(r_align=r_al, rmse_out=rmse, D_KS=d_ks,
                         r_mean=r_mean)
        if wm == 'theta':
            nm_base, nsd_base = permutation_null(u, z)
    # позитивный контроль: Z_id против файла
    ts, vals = zid_graph(T=120.0, n_grid=2401)
    sgn = np.sign(vals)
    cross = np.where(np.diff(sgn) != 0)[0]
    found = []
    for i in cross:
        a, b = ts[i], ts[i + 1]
        for _ in range(80):
            m = 0.5 * (a + b)
            tm = mp.mpf(float(m))
            vm = float(mp.re(mp.e ** (1j * theta_phase(tm))
                             * mp.zeta(mp.mpf(0.5) + 1j * tm)))
            if np.sign(vals[i]) * vm <= 0:
                b = m
            else:
                a = m
        found.append(0.5 * (a + b))
    ref = z[(z > 0) & (z < 120.0)]
    n = min(len(found), len(ref))
    pc_resid = float(np.max(np.abs(np.array(found[:n]) - ref[:n])))
    pc_r = float(np.corrcoef(found[:n], ref[:n])[0, 1])
    return dict(
        meta=dict(package='AB Research Program', campaign='V16',
                  name='full hamiltonian x full algebraic function',
                  seeds=list(seeds), n_configs=len(grid), window=WINDOW,
                  weight='theta', date='2026-10-10'),
        null=dict(best_mean=nm, best_sd=nsd, base_mean=nm_base,
                  base_sd=nsd_base, n_perm=200),
        summary=dict(r_align_max=float(ra.max()),
                     r_align_min=float(ra.min()),
                     r_align_mean=float(ra.mean()),
                     z_best=float(z_best),
                     identity_closed=bool(abs(best['r_align'] - 1.0) < 0.5
                                          and z_best > 10)),
        best=dict(best), worst=dict(worst), weight_compare=wcomp,
        positive_control=dict(pc_Z_id_vs_file=dict(r=pc_r,
                                                   max_residual=pc_resid,
                                                   n_zeros=n)),
        rows_count=len(rows),
        rows=rows,
    )
