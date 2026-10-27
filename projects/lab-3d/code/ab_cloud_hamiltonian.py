"""
ab_cloud_hamiltonian.py
=======================
Real AB-cloud Hamiltonian with topological vortices.

CRITICAL FIX vs v17:
--------------------
v17 used build_H with V = W*(rand()-0.5) (uniform diagonal disorder) and a
single Peierls phase 2*pi*phi*(i-1) in x-direction only.  That is the standard
Hofstadter model with diagonal disorder, NOT the AB-cloud of the monograph.

Here we implement the actual monograph Hamiltonian:

    H_{ij} = -t_x e^{i A_x(r_i)} δ_{j,i+x̂}
             -t_y e^{i A_y(r_i)} δ_{j,i+ŷ}
             + V_i δ_{ij}

with

    A_x(r_i) = 2*pi*alpha*(j-1) + sum_k q_k * arg(r_i - r_k)
    A_y(r_i) =             0     + sum_k q_k * arg(r_i - r_k)

    V_i      = sum_k q_k * W / (|r_i - r_k|^2 * N + 1)  +  eps_i

where {r_k} are N_v vortex positions chosen uniformly on the torus,
q_k = ±1 are vortex charges, and eps_i ~ Uniform(-eps_w, eps_w) is a
small on-site noise.  This is the "Coulomb-vortex + AB-phase" form
described in monograph section 2.3.

All RNG state is LOCAL (numpy.random.Generator), never global.
"""
from __future__ import annotations

import numpy as np
from dataclasses import dataclass


@dataclass
class VortexConfig:
    """Configuration of an AB-cloud sample."""
    Lx: int
    Ly: int
    N_v: int                 # number of vortices
    W: float = 1.0           # vortex potential strength
    eps_w: float = 0.0       # on-site uniform noise amplitude
    tx: float = 1.0
    ty: float = 1.0
    alpha: float = 0.5       # background flux per plaquette (= 1/2 for Dirac cone)
    seed: int = 0
    vortex_charges: str = "random"   # "random" or "alternating"


def _vortex_positions(rng: np.random.Generator, N_v: int, Lx: int, Ly: int):
    """Uniformly place N_v vortices on the (Lx,Ly) torus, coordinates in [0,Lx)x[0,Ly)."""
    xs = rng.uniform(0.0, Lx, size=N_v)
    ys = rng.uniform(0.0, Ly, size=N_v)
    return np.stack([xs, ys], axis=1)   # shape (N_v, 2)


def _vortex_charges(rng: np.random.Generator, N_v: int, mode: str):
    if mode == "random":
        return rng.choice([-1.0, 1.0], size=N_v)
    elif mode == "alternating":
        return np.array([1.0 if k % 2 == 0 else -1.0 for k in range(N_v)])
    else:
        raise ValueError(f"unknown vortex_charges mode: {mode}")


def _torus_diff(r_i: np.ndarray, r_k: np.ndarray, Lx: int, Ly: int):
    """Minimum-image convention on a 2-torus."""
    d = r_i - r_k
    d[0] -= Lx * np.round(d[0] / Lx)
    d[1] -= Ly * np.round(d[1] / Ly)
    return d


def build_ab_cloud_hamiltonian(cfg: VortexConfig) -> tuple[np.ndarray, np.ndarray]:
    """
    Build the AB-cloud Hamiltonian as a dense complex Hermitian matrix.

    Returns
    -------
    H : (N,N) complex Hermitian ndarray
    positions : (N_v, 2) float ndarray  (for diagnostics)
    """
    Lx, Ly = cfg.Lx, cfg.Ly
    N = Lx * Ly
    rng = np.random.default_rng(cfg.seed)

    # --- vortex placement ---
    r_vortex = _vortex_positions(rng, cfg.N_v, Lx, Ly)
    q_vortex = _vortex_charges(rng, cfg.N_v, cfg.vortex_charges)

    H = np.zeros((N, N), dtype=complex)
    on_site = np.zeros(N, dtype=float)

    # --- build site positions and vortex potentials ---
    for i in range(Lx):
        for j in range(Ly):
            idx = i * Ly + j
            r_i = np.array([float(i), float(j)])
            # Coulomb-like vortex potential V_i
            V = 0.0
            for k in range(cfg.N_v):
                d = _torus_diff(r_i.copy(), r_vortex[k], Lx, Ly)
                dist2 = d[0]*d[0] + d[1]*d[1] + 1e-12
                V += q_vortex[k] * cfg.W / (dist2 * N + 1.0)
            # small on-site noise
            if cfg.eps_w > 0:
                V += cfg.eps_w * (rng.uniform(-1.0, 1.0))
            on_site[idx] = V          # on-site = vortex potential only (no +4 shift)
            H[idx, idx] = on_site[idx]

    # --- hopping with Peierls phase = background flux + vortex contributions ---
    for i in range(Lx):
        for j in range(Ly):
            idx = i * Ly + j
            r_i = np.array([float(i), float(j)])

            # x-hopping (i,j) -> (i+1,j)
            i2 = (i + 1) % Lx
            idx_r = i2 * Ly + j
            # background phase (Landau gauge A = (0, 2π α x))  — phase on y-hop
            # but we use symmetric gauge:  phase_x = 0, phase_y = 2π α i
            phase_x = 0.0
            # vortex contributions to x-hopping phase = line integral along edge
            for k in range(cfg.N_v):
                d = _torus_diff(r_i.copy(), r_vortex[k], Lx, Ly)
                # arg of complex (dx + i dy)
                phase_x += q_vortex[k] * np.arctan2(d[1], d[0] + 0.5) \
                                      - q_vortex[k] * np.arctan2(d[1], d[0] - 0.5)
            H[idx, idx_r] += -cfg.tx * np.exp(1j * phase_x)
            H[idx_r, idx] += -cfg.tx * np.exp(-1j * phase_x)

            # y-hopping (i,j) -> (i,j+1)  with Landau-gauge background phase 2π α i
            j2 = (j + 1) % Ly
            idx_u = i * Ly + j2
            phase_y = 2.0 * np.pi * cfg.alpha * i
            for k in range(cfg.N_v):
                d = _torus_diff(r_i.copy(), r_vortex[k], Lx, Ly)
                phase_y += q_vortex[k] * np.arctan2(d[1] + 0.5, d[0]) \
                                     - q_vortex[k] * np.arctan2(d[1] - 0.5, d[0])
            H[idx, idx_u] += -cfg.ty * np.exp(1j * phase_y)
            H[idx_u, idx] += -cfg.ty * np.exp(-1j * phase_y)

    # symmetrize to kill tiny non-Hermitian numerical noise
    H = 0.5 * (H + H.conj().T)
    return H, r_vortex


def build_pure_hofstadter(Lx: int, Ly: int, alpha: float, seed: int = 0) -> np.ndarray:
    """
    Standard Hofstadter model WITHOUT vortices, WITHOUT disorder.
    On-site energy = 0 (so spectrum is symmetric around 0 for α=1/2 due to
    bipartite chiral symmetry).  v17 used 4.0 on-site (coordination number),
    which shifted the Dirac point to E=4 — visually equivalent but obscures
    the E → −E symmetry test.
    """
    rng = np.random.default_rng(seed)
    N = Lx * Ly
    H = np.zeros((N, N), dtype=complex)
    for i in range(Lx):
        for j in range(Ly):
            idx = i * Ly + j
            # on-site = 0  (was 4.0 in v17)
            i2 = (i + 1) % Lx
            H[idx, i2 * Ly + j] += -1.0
            j2 = (j + 1) % Ly
            phase = 2.0 * np.pi * alpha * i
            H[idx, i * Ly + j2] += -np.exp(1j * phase)
            H[i * Ly + j2, idx] += -np.exp(-1j * phase)
    return 0.5 * (H + H.conj().T)


def build_random_anderson(L: int, W: float, seed: int = 0) -> np.ndarray:
    """
    Generic 2D Anderson model on L×L square lattice with uniform diagonal
    disorder in [-W/2, W/2].  Used as the 'null hypothesis' in V19 comparison:
    if ⟨r⟩_AB(L) ≈ ⟨r⟩_Anderson(L), then AB-cloud is just another disordered
    Hermitian matrix, not a special universal class.
    """
    rng = np.random.default_rng(seed)
    N = L * L
    H = np.zeros((N, N), dtype=complex)
    on_site = W * (rng.uniform(-0.5, 0.5, size=N))   # no +4 shift
    np.fill_diagonal(H, on_site)
    for i in range(L):
        for j in range(L):
            idx = i * L + j
            i2 = (i + 1) % L
            j2 = (j + 1) % L
            H[idx, i2 * L + j] += -1.0
            H[idx, i * L + j2] += -1.0
    return 0.5 * (H + H.conj().T)


def build_random_gue(N: int, seed: int = 0) -> np.ndarray:
    """
    Draw a fresh N×N matrix from GUE:  H = (G + G†)/√(2N) where G has i.i.d.
    complex Gaussian entries.  Used as the literal GUE reference for ⟨r⟩, Σ², Δ₃.
    """
    rng = np.random.default_rng(seed)
    G = (rng.standard_normal((N, N)) + 1j * rng.standard_normal((N, N))) / np.sqrt(2.0)
    H = (G + G.conj().T) / np.sqrt(2 * N)
    return H
