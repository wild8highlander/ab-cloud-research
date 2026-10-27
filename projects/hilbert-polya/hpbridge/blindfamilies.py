"""hpbridge.blindfamilies — пять новых семейств затворов v2 (C13, R5, T15).

Слепой протокол: семейства спроектированы ДО измерений, метрики считаются
единым конвейером, вердикты коммитятся без перебора. Ручки, которых не было
в v1 (Nv, q, W, α, aniso, dalpha, mass, profile, signs, bc, twist):

  BF1 imag-x      — чисто мнимые x-прыжки (фаза +π/2 на каждой x-связи):
                    TRS сломан иначе, чем вихрями;
  BF2 golden      — квазипериодические позиции вихрей (золотое сечение),
                    без RNG;
  BF3 dimers      — стаггерд-колонки вихревых димеров (±q парами);
  BF4 plaw2       — дальнодействующие прыжки ~1/r² (радиус 3) поверх NN;
  BF5 dither      — построчный дизеринг флакса dα·(−1)^iy.
"""
import numpy as np
from scipy.linalg import eigvalsh

from engine.hamiltonian import (BASE_SEED, HARDCORE_OFFSET, T_HOP,
                                random_vortex_configuration)


def _grid(L):
    ix = np.arange(L, dtype=np.float64)
    iy1 = np.arange(1, L + 1, dtype=np.float64)
    XX, YY = np.meshgrid(ix + 1.0, iy1)
    return XX.ravel(), YY.ravel()


def vortex_phi_field(vortices, XX, YY, j_from, j_to):
    phi = np.zeros(j_from.size)
    for (vx, vy, qk) in vortices:
        th = np.arctan2(YY - vy, XX - vx)
        phi += 0.5 * qk * (th[j_to] - th[j_from])
    return phi


def build_BF1(L, vortices, alpha, W=0.0):
    """BF1: x-прыжки с фазой +π/2 (чисто мнимые), остальное — протокол."""
    Nx = Ny = L
    N = Nx * Ny
    XX, YY = _grid(L)
    H = np.zeros((N, N), dtype=np.complex128)
    rows = np.repeat(np.arange(Ny), Nx - 1)
    cols = np.tile(np.arange(Nx - 1), Ny)
    i_from = rows * Nx + cols
    i_to = i_from + 1
    phi_x = 2.0 * np.pi * alpha * (rows + 1.0) + np.pi / 2   # ← фаза BF1
    H[i_from, i_to] = -T_HOP * np.exp(1j * phi_x)
    H[i_to, i_from] = -T_HOP * np.exp(-1j * phi_x)
    iy_pairs = np.arange(Ny - 1)
    cols_v = np.tile(np.arange(Nx), iy_pairs.size)
    rows_v = np.repeat(iy_pairs, Nx)
    j_from = rows_v * Nx + cols_v
    j_to = j_from + Nx
    phi_y = vortex_phi_field(vortices, XX, YY, j_from, j_to)
    H[j_from, j_to] = -T_HOP * np.exp(1j * phi_y)
    H[j_to, j_from] = -T_HOP * np.exp(-1j * phi_y)
    if W > 0:
        diag = np.zeros(N)
        for (vx, vy, qk) in vortices:
            r2 = (XX - vx) ** 2 + (YY - vy) ** 2
            diag += qk * W / (r2 / N + 1.0)
        H[np.arange(N), np.arange(N)] = diag
    return H


def build_BF2(L, alpha, Nv, q=1.0, W=0.0):
    """BF2: квазипериодические вихри (золотое сечение), детерминированно."""
    g = (np.sqrt(5.0) - 1.0) / 2.0
    pts = []
    for k in range(1, Nv + 1):
        x = (np.mod(k * g, 1.0) * (L - 2)) + 1.5
        y = (np.mod(k * g * g, 1.0) * (L - 2)) + 1.5
        pts.append((float(x), float(y)))
    half = Nv // 2
    vortices = [(x, y, q if i < half else -q)
                for i, (x, y) in enumerate(pts)]
    Nx = Ny = L
    N = Nx * Ny
    XX, YY = _grid(L)
    H = np.zeros((N, N), dtype=np.complex128)
    rows = np.repeat(np.arange(Ny), Nx - 1)
    cols = np.tile(np.arange(Nx - 1), Ny)
    i_from = rows * Nx + cols
    i_to = i_from + 1
    phi_x = 2.0 * np.pi * alpha * (rows + 1.0)
    H[i_from, i_to] = -T_HOP * np.exp(1j * phi_x)
    H[i_to, i_from] = -T_HOP * np.exp(-1j * phi_x)
    iy_pairs = np.arange(Ny - 1)
    cols_v = np.tile(np.arange(Nx), iy_pairs.size)
    rows_v = np.repeat(iy_pairs, Nx)
    j_from = rows_v * Nx + cols_v
    j_to = j_from + Nx
    phi_y = vortex_phi_field(vortices, XX, YY, j_from, j_to)
    H[j_from, j_to] = -T_HOP * np.exp(1j * phi_y)
    H[j_to, j_from] = -T_HOP * np.exp(-1j * phi_y)
    if W > 0:
        diag = np.zeros(N)
        for (vx, vy, qk) in vortices:
            r2 = (XX - vx) ** 2 + (YY - vy) ** 2
            diag += qk * W / (r2 / N + 1.0)
        H[np.arange(N), np.arange(N)] = diag
    return H


def golden_vortices(L, Nv, q=1.0):
    g = (np.sqrt(5.0) - 1.0) / 2.0
    pts = []
    for k in range(1, Nv + 1):
        x = (np.mod(k * g, 1.0) * (L - 2)) + 1.5
        y = (np.mod(k * g * g, 1.0) * (L - 2)) + 1.5
        pts.append((float(x), float(y)))
    half = Nv // 2
    return [(x, y, q if i < half else -q) for i, (x, y) in enumerate(pts)]


def dimer_vortices(L, n_dimers=8, q=1.0, seed=11):
    """BF3: димеры ±q в стаггерд-колонках."""
    rng = np.random.default_rng(seed)
    vortices = []
    cols = rng.choice(np.arange(1, L - 1), size=n_dimers, replace=False)
    for c in cols:
        y = float(rng.integers(3, L - 3))
        s = 1.0 if (int(c) % 2 == 0) else -1.0
        vortices.append((c + 0.5, y - 1.0, q * s))
        vortices.append((c + 0.5, y + 1.0, -q * s))
    return vortices


def build_BF4(L, vortices, alpha, t2=0.35, W=0.0):
    """BF4: NN-протокол + дальние прыжки −t2/r² (r ≤ 3, эрмитово,
    фаза = среднее Ландау-фаз концов)."""
    H = _protocol_H(L, vortices, alpha, W)
    N = L * L
    idx = np.arange(N).reshape(L, L)
    ph_row = 2.0 * np.pi * alpha * np.arange(1, L + 1)
    for iy in range(L):
        for ix in range(L):
            s = idx[iy, ix]
            for dy in range(0, 4):
                for dx in range(-3, 4):
                    if dy == 0 and dx <= 0:
                        continue
                    if dx * dx + dy * dy > 9 or dx * dx + dy * dy == 0:
                        continue
                    jx, jy = ix + dx, iy + dy
                    if jx < 0 or jx >= L or jy >= L:
                        continue
                    t_ = idx[jy, jx]
                    r2 = dx * dx + dy * dy
                    amp = -t2 / r2
                    ph = 0.5 * (ph_row[iy] + ph_row[jy])
                    H[s, t_] += amp * np.exp(1j * ph)
                    H[t_, s] += amp * np.exp(-1j * ph)
    return H


def build_BF5(L, vortices, alpha, dith=0.02, W=0.0):
    """BF5: построчный дизеринг флакса: φ_x(iy) = 2π(α·iy + dith·(−1)^iy)."""
    Nx = Ny = L
    N = Nx * Ny
    XX, YY = _grid(L)
    H = np.zeros((N, N), dtype=np.complex128)
    rows = np.repeat(np.arange(Ny), Nx - 1)
    cols = np.tile(np.arange(Nx - 1), Ny)
    i_from = rows * Nx + cols
    i_to = i_from + 1
    phi_x = 2.0 * np.pi * (alpha * (rows + 1.0)
                           + dith * ((rows + 1.0) % 2 * 2.0 - 1.0))
    H[i_from, i_to] = -T_HOP * np.exp(1j * phi_x)
    H[i_to, i_from] = -T_HOP * np.exp(-1j * phi_x)
    iy_pairs = np.arange(Ny - 1)
    cols_v = np.tile(np.arange(Nx), iy_pairs.size)
    rows_v = np.repeat(iy_pairs, Nx)
    j_from = rows_v * Nx + cols_v
    j_to = j_from + Nx
    phi_y = vortex_phi_field(vortices, XX, YY, j_from, j_to)
    H[j_from, j_to] = -T_HOP * np.exp(1j * phi_y)
    H[j_to, j_from] = -T_HOP * np.exp(-1j * phi_y)
    if W > 0:
        diag = np.zeros(N)
        for (vx, vy, qk) in vortices:
            r2 = (XX - vx) ** 2 + (YY - vy) ** 2
            diag += qk * W / (r2 / N + 1.0)
        H[np.arange(N), np.arange(N)] = diag
    return H


def _protocol_H(L, vortices, alpha, W):
    """Протокольный H v1 (открытые границы) — общий каркас."""
    Nx = Ny = L
    N = Nx * Ny
    XX, YY = _grid(L)
    H = np.zeros((N, N), dtype=np.complex128)
    rows = np.repeat(np.arange(Ny), Nx - 1)
    cols = np.tile(np.arange(Nx - 1), Ny)
    i_from = rows * Nx + cols
    i_to = i_from + 1
    phi_x = 2.0 * np.pi * alpha * (rows + 1.0)
    H[i_from, i_to] = -T_HOP * np.exp(1j * phi_x)
    H[i_to, i_from] = -T_HOP * np.exp(-1j * phi_x)
    iy_pairs = np.arange(Ny - 1)
    cols_v = np.tile(np.arange(Nx), iy_pairs.size)
    rows_v = np.repeat(iy_pairs, Nx)
    j_from = rows_v * Nx + cols_v
    j_to = j_from + Nx
    phi_y = vortex_phi_field(vortices, XX, YY, j_from, j_to)
    H[j_from, j_to] = -T_HOP * np.exp(1j * phi_y)
    H[j_to, j_from] = -T_HOP * np.exp(-1j * phi_y)
    if W > 0:
        diag = np.zeros(N)
        for (vx, vy, qk) in vortices:
            r2 = (XX - vx) ** 2 + (YY - vy) ** 2
            diag += qk * W / (r2 / N + 1.0)
        H[np.arange(N), np.arange(N)] = diag
    return H


def family_gates():
    """30 затворов: 5 семейств × 6 вариантов (детерминизм сидов)."""
    G = []
    L = 24
    for Nv in (8, 16, 32):
        for W in (0.0, 0.5):
            vrng = np.random.default_rng(BASE_SEED + HARDCORE_OFFSET)
            v1 = random_vortex_configuration(Nv, L, L, 1.0, vrng, "protocol")
            G.append((f"BF1_imagx_Nv{Nv}_W{W}",
                      lambda L=L, v=v1, W=W: build_BF1(L, v, 0.5, W)))
            G.append((f"BF2_golden_Nv{Nv}_W{W}",
                      lambda L=L, Nv=Nv, W=W: build_BF2(L, 0.5, Nv, 1.0, W)))
    for seed in (11, 12):
        for n_d in (6, 8):
            v3 = dimer_vortices(L, n_d, 1.0, seed)
            G.append((f"BF3_dimers_d{n_d}_s{seed}",
                      lambda L=L, v=v3: _protocol_H(L, v, 0.5, 0.0)))
    for Nv in (16, 32):
        vrng = np.random.default_rng(BASE_SEED + HARDCORE_OFFSET)
        v4 = random_vortex_configuration(Nv, L, L, 1.0, vrng, "protocol")
        G.append((f"BF4_plaw2_Nv{Nv}",
                  lambda L=L, v=v4: build_BF4(L, v, 0.5, 0.35, 0.0)))
    for dith in (0.01, 0.02):
        vrng = np.random.default_rng(BASE_SEED + HARDCORE_OFFSET)
        v5 = random_vortex_configuration(16, L, L, 1.0, vrng, "protocol")
        G.append((f"BF5_dither{dith}",
                  lambda L=L, v=v5, d=dith: build_BF5(L, v, 0.5, d, 0.0)))
    return G
