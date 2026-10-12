# -*- coding: utf-8 -*-
"""rpbridge.electron — Решение 17 (V17): электрон на критической прямой.

Физическая постановка (в духе эталона C7, но на ПОЛНОМ гамильтониане
и на вытянутой решётке-волноводе): электрон (волновой пакет) запускается
вдоль оси x решётки 96×24 при полфлакса α = ½ — самодуальной линии, где
π-флакс превращает решётку в дискретизированное безмассовое уравнение
Дирака. Ось x интерпретируется как критический канал; вопрос — проходит
ли пакет когерентно вдоль него и различает ли ζ-облако вихрей (фазовый
вес log|ζ(½+iγ̃_k)|, протокол V3) случайное облако той же плотности.

Метрики (все — честные, детерминированные, с сохранением энергии):
  * ⟨x(t)⟩, ⟨y(t)⟩ — траектория центроида; отклонение от канала
    D_y = max|⟨y⟩ − y_c|;
  * транзит P(x ≥ x_exit = 88), отражение R = P(x ≤ 4) на горизонте;
  * поперечный разброс σ_y(t);
  * сохранение энергии: max_t |E(t) − E(0)| / |E(0)|;
  * когерентность C(t) = |⟨ψ(0), ψ(t)⟩|;
  * ГЛАВНОЕ новое: фазовое сопровождение θ(t) — корреляция Пирсона между
    накопленной динамической фазой пакета arg⟨ψ(0),ψ(t)⟩ и θ(⟨x(t)⟩·k₀)
    алгебраической функции (масштабированной в спектральную переменную);
    это измеримый мост «динамика ↔ алгебраическая функция».

Три облака: 'zeta' (ζ-вес), 'random' (случайные фазы, та же плотность),
'clean' (без вихрей) — сид 96, идентичные пакеты.
"""
import numpy as np
import mpmath as mp

from engine.hamiltonian import build_hamiltonian

LX, LY = 96, 24
X_EXIT = 88
X_MIRROR = 4
T_HORIZON = 40.0
DT = 0.1
N_FRAMES = 201          # сетка времени 0..40 шаг 0.2
Y_CENTER = 12.0
SIGMA0 = 3.0
K0 = np.pi / 2
NV = 48
SEED = 96
mp.mp.dps = 25


def _gaussian_packet(lx, ly, x0, y0, sigma, k0):
    """Нормированный гауссов пакет с продольным импульсом k0."""
    ix = np.arange(1, lx + 1, dtype=float)
    iy = np.arange(1, ly + 1, dtype=float)
    XX, YY = np.meshgrid(ix, iy, indexing='ij')
    env = np.exp(-((XX - x0) ** 2 + (YY - y0) ** 2) / (2 * sigma ** 2))
    psi = (env * np.exp(1j * k0 * XX)).ravel().astype(np.complex128)
    return psi / np.linalg.norm(psi)


def _vortex_positions(nv, lx, ly, seed):
    vrng = np.random.default_rng(seed + 3500)
    return [(float(vrng.integers(1, lx)) + 0.5,
             float(vrng.integers(1, ly)) + 0.5) for _ in range(nv)]


def _cloud_phases(mode, zeros, nv, seed):
    """Фазовые веса вихрей: ζ-вес против случайного против нуля."""
    if mode == 'clean':
        return np.zeros(nv)
    if mode == 'zeta':
        z = np.asarray(zeros, float)
        gm = 0.5 * (z[:nv] + z[1:nv + 1])
        return np.array([float(mp.log(abs(mp.zeta(mp.mpf(0.5)
                                                  + 1j * mp.mpf(g)))))
                         for g in gm])
    if mode == 'random':
        rng = np.random.default_rng(seed + 7700)
        return rng.uniform(-1.5, 1.5, nv)
    raise ValueError(mode)


def build_operator(mode, zeros, lx=LX, ly=LY, nv=NV, seed=SEED, W=0.5):
    """Полный гамильтониан волновода с выбранным облаком."""
    pts = _vortex_positions(nv, lx, ly, seed)
    w = _cloud_phases(mode, zeros, nv, seed)
    vort = [(x, y, float(wi)) for (x, y), wi in zip(pts, w)]
    drng = np.random.default_rng(seed + 3501)
    H = build_hamiltonian(lx, ly, vort, 0.5, 1.0, W, 'open', drng)
    return H


def propagate(H, psi0, times):
    """Точная динамика в собственном базисе; возвращает кадры ⟨x⟩, ⟨y⟩,
    P(x≥exit), P(x≤mirror), σ_y, C(t), динамическую фазу, E(t)."""
    lx, ly = LX, LY
    ix = np.arange(1, lx + 1, dtype=float)
    iy = np.arange(1, ly + 1, dtype=float)
    XX, YY = np.meshgrid(ix, iy, indexing='ij')
    xr, yr = XX.ravel(), YY.ravel()
    ev, V = np.linalg.eigh(H)
    c0 = V.conj().T @ psi0
    E0 = float(np.real(c0.conj() @ (ev * c0)))
    out = dict(t=[], x=[], y=[], p_exit=[], p_mirror=[], sy=[], C=[],
               phase=[], E=[])
    psi0c = psi0.conj()
    for t in times:
        c = c0 * np.exp(-1j * ev * t)
        psi = V @ c
        p = np.abs(psi) ** 2
        Z = p.sum()
        out['t'].append(float(t))
        out['x'].append(float((p * xr).sum() / Z))
        out['y'].append(float((p * yr).sum() / Z))
        out['p_exit'].append(float(p[xr >= X_EXIT].sum() / Z))
        out['p_mirror'].append(float(p[xr <= X_MIRROR].sum() / Z))
        my = (p * yr).sum() / Z
        out['sy'].append(float(np.sqrt((p * (yr - my) ** 2).sum() / Z)))
        ov = psi0c @ psi
        out['C'].append(float(abs(ov)))
        ph = float(np.angle(ov))
        out['phase'].append(ph)
        out['E'].append(float(np.real(c.conj() @ (ev * c))))
    return out, E0, ev


def theta_along(t_arr, x_arr, k0=K0):
    """θ-сопровождение: алгебраическая фаза вдоль траектории,
    θ(k0·⟨x(t)⟩) — глобальный дрейф фазы сопоставляется с динамической."""
    out = []
    for t, x in zip(t_arr, x_arr):
        out.append(float(mp.im(mp.log(mp.gamma(mp.mpf(0.25)
                                               + 1j * mp.mpf(k0 * x / 2))))
                         - mp.mpf(k0 * x) * mp.log(mp.sqrt(mp.pi))))
    return np.array(out)


def run(zeros, full=True):
    """Полный прогон V17: три облака × одна геометрия (детерминизм)."""
    times = np.linspace(0.0, T_HORIZON, N_FRAMES if full else 41)
    z = np.asarray(zeros, float)
    results = {}
    for mode in ('clean', 'random', 'zeta'):
        H = build_operator(mode, z)
        psi0 = _gaussian_packet(LX, LY, 8.0, Y_CENTER, SIGMA0, K0)
        traj, E0, ev = propagate(H, psi0, times)
        traj['E0'] = E0
        dE = max(abs(e - E0) / abs(E0) for e in traj['E'])
        dy = max(abs(y - Y_CENTER) for y in traj['y'])
        th = theta_along(np.array(traj['t']), np.array(traj['x']))
        # корреляция форм фаз (обе непрерывны) — r_phase
        ph = np.unwrap(np.array(traj['phase']))
        th_u = np.unwrap(th)
        r_phase = float(np.corrcoef(ph, th_u)[0, 1])
        results[mode] = dict(
            traj=traj, dE_rel=float(dE), Dy_max=float(dy),
            transit=float(traj['p_exit'][-1]),
            mirror=float(traj['p_mirror'][-1]),
            sy_final=float(traj['sy'][-1]),
            C_final=float(traj['C'][-1]), r_phase=r_phase)
    zt, rt = results['zeta']['transit'], results['random']['transit']
    ratio = (zt / rt) if rt > 1e-12 else float('inf')
    return dict(
        meta=dict(package='AB Research Program', campaign='V17',
                  name='electron on the critical line', lattice=f'{LX}x{LY}',
                  alpha=0.5, Nv=NV, seed=SEED, dt=DT,
                  T=T_HORIZON, date='2026-10-10'),
        summary=dict(
            transit_zeta=zt, transit_random=rt,
            transit_clean=results['clean']['transit'],
            ratio_zeta_over_random=float(ratio),
            Dy_zeta=results['zeta']['Dy_max'],
            Dy_random=results['random']['Dy_max'],
            energy_max_dev=max(results[m]['dE_rel'] for m in results),
            r_phase_zeta=results['zeta']['r_phase'],
            r_phase_random=results['random']['r_phase']),
        modes=results,
    )
