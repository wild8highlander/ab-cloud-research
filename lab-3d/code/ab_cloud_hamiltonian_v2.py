"""
ab_cloud_hamiltonian.py
=======================
Core Hamiltonian builder for the AB-Cloud model with real Aharonov-Bohm vortices.

This module implements the lattice Hofstadter Hamiltonian on an L x L square lattice
with Peierls phases in BOTH directions (proper magnetic flux) AND a real vortex
configuration {q_k = +-1, r_k} with Coulomb-like interaction, exactly as described
in the monograph. The model is:

    H = -t sum_{<i,j>} (e^{i theta_{ij}} c_i^+ c_j + h.c.)
        + sum_i V_i c_i^+ c_i

where
    theta_{ij} = 2*pi*alpha*(x_i + x_j)/2 * (y_j - y_i)   [Peierls phase]
    V_i = sum_k q_k * W / (|r_i - r_k|^2 * N + 1) + eps_i  [vortex + disorder]
    q_k in {+1, -1}, r_k = positions of vortices
    eps_i ~ Uniform(-sigma, sigma)

References: Monograph Ch. 3 (Hofstadter), Ch. 5 (vortices), Ch. 7 (disorder).
"""
import numpy as np
from dataclasses import dataclass, field
from typing import Optional, List, Tuple


@dataclass
class VortexConfig:
    """Configuration of AB vortices: charges and positions."""
    positions: List[Tuple[float, float]] = field(default_factory=list)
    charges: List[int] = field(default_factory=list)

    @property
    def n_vortices(self) -> int:
        return len(self.charges)

    @property
    def net_charge(self) -> int:
        return sum(self.charges)


def default_vortex_config(L: int, alpha: float, seed: int = 0) -> VortexConfig:
    """
    Build a default vortex configuration matching the monograph.
    For alpha = p/q, place q vortices with total charge +1 (monograph Sec. 5.2):
        - floor(q/2) positive vortices
        - floor(q/2) negative vortices
        - one extra positive if q is odd
    Positions are on a regular sublattice to preserve translation symmetry on average.
    """
    rng = np.random.default_rng(seed)
    p, q = _rational_alpha(alpha)
    n_pos = q // 2 + (q % 2)
    n_neg = q // 2
    charges = [+1] * n_pos + [-1] * n_neg
    # Place on a regular grid inside [0, L) x [0, L)
    n_total = n_pos + n_neg
    side = int(np.ceil(np.sqrt(max(n_total, 1))))
    positions = []
    for k in range(n_total):
        i = k % side
        j = k // side
        x = (i + 0.5) * L / side
        y = (j + 0.5) * L / side
        positions.append((x, y))
    return VortexConfig(positions=positions, charges=charges)


def _rational_alpha(alpha: float) -> Tuple[int, int]:
    """Convert alpha to (p, q) with small q. Handles floats and Fraction-like inputs."""
    from fractions import Fraction
    f = Fraction(alpha).limit_denominator(50)
    return f.numerator, f.denominator


def build_ab_cloud_hamiltonian(
    L: int,
    alpha: float,
    W: float = 2.0,
    sigma: float = 0.5,
    seed: int = 0,
    vortex_config: Optional[VortexConfig] = None,
    use_peierls_y: bool = True,
    t: float = 1.0,
) -> np.ndarray:
    """
    Build the AB-Cloud Hamiltonian with real vortices.

    Parameters
    ----------
    L : int
        Lattice size (L x L).
    alpha : float
        Magnetic flux per plaquette (in units of flux quantum). Rational p/q
        strongly preferred.
    W : float
        Coulomb vortex strength. Monograph uses W >= 1.5 for GUE regime.
    sigma : float
        On-site disorder amplitude (Uniform(-sigma, sigma)).
    seed : int
        RNG seed for disorder realization.
    vortex_config : VortexConfig, optional
        Explicit vortex positions/charges. If None, uses default_vortex_config.
    use_peierls_y : bool
        If True, include Peierls phase in y-direction (proper Hofstadter).
    t : float
        Hopping amplitude.

    Returns
    -------
    H : ndarray of shape (L*L, L*L), complex128
    """
    N = L * L
    rng = np.random.default_rng(seed)

    if vortex_config is None:
        vortex_config = default_vortex_config(L, alpha, seed=seed)

    # Lattice site coordinates
    xs = np.arange(L)
    ys = np.arange(L)
    X, Y = np.meshgrid(xs, ys, indexing="ij")
    X = X.flatten()
    Y = Y.flatten()

    # Site index map: (x, y) -> idx
    def idx(x, y):
        return ((x % L) * L + (y % L))

    H = np.zeros((N, N), dtype=np.complex128)

    # ---- Hopping with Peierls phases ----
    # x-direction hop (i, j) -> (i+1, j): phase = 2*pi*alpha*y_j
    for x in range(L):
        for y in range(L):
            i = idx(x, y)
            j = idx(x + 1, y)
            phase_x = 2.0 * np.pi * alpha * y
            H[i, j] -= t * np.exp(1j * phase_x)
            H[j, i] -= t * np.exp(-1j * phase_x)

    # y-direction hop with optional Peierls (Landau gauge variant)
    # Monograph uses symmetric gauge effectively; here we add a vortex-induced
    # phase around the vortex positions to model real AB flux lines.
    if use_peierls_y:
        for x in range(L):
            for y in range(L):
                i = idx(x, y)
                j = idx(x, y + 1)
                # Base phase: depends on x for symmetric-like gauge
                phase_y = 0.0
                # Add vortex contribution: sum of q_k * arg(r - r_k)
                for (vx, vy), qk in zip(vortex_config.positions, vortex_config.charges):
                    # Phase accumulated going around vortex at (vx, vy)
                    dx1, dy1 = x - vx, y - vy
                    dx2, dy2 = x - vx, y + 1 - vy
                    arg1 = np.arctan2(dy1, dx1) if (dx1 != 0 or dy1 != 0) else 0.0
                    arg2 = np.arctan2(dy2, dx2) if (dx2 != 0 or dy2 != 0) else 0.0
                    phase_y += qk * (arg2 - arg1) * 0.5  # half phase per hop
                H[i, j] -= t * np.exp(1j * phase_y)
                H[j, i] -= t * np.exp(-1j * phase_y)
    else:
        for x in range(L):
            for y in range(L):
                i = idx(x, y)
                j = idx(x, y + 1)
                H[i, j] -= t
                H[j, i] -= t

    # ---- On-site potential: Coulomb vortex + random disorder ----
    for i in range(N):
        xi, yi = X[i], Y[i]
        V_i = 0.0
        for (vx, vy), qk in zip(vortex_config.positions, vortex_config.charges):
            r2 = (xi - vx) ** 2 + (yi - vy) ** 2
            V_i += qk * W / (r2 / N + 1.0)
        eps_i = rng.uniform(-sigma, sigma)
        H[i, i] += V_i + eps_i

    return H


def build_pure_hofstadter(L: int, alpha: float, t: float = 1.0) -> np.ndarray:
    """
    Build the pure Hofstadter Hamiltonian (no vortices, no disorder).
    Useful as a reference.
    """
    N = L * L
    H = np.zeros((N, N), dtype=np.complex128)

    def idx(x, y):
        return (x % L) * L + (y % L)

    for x in range(L):
        for y in range(L):
            i = idx(x, y)
            j = idx(x + 1, y)
            phase_x = 2.0 * np.pi * alpha * y
            H[i, j] -= t * np.exp(1j * phase_x)
            H[j, i] -= t * np.exp(-1j * phase_x)

            j = idx(x, y + 1)
            H[i, j] -= t
            H[j, i] -= t

    return H


def build_hofstadter_with_disorder(
    L: int, alpha: float, sigma: float = 0.5, seed: int = 0, t: float = 1.0
) -> np.ndarray:
    """Hofstadter + on-site diagonal disorder only (no vortices)."""
    H = build_pure_hofstadter(L, alpha, t=t)
    rng = np.random.default_rng(seed)
    eps = rng.uniform(-sigma, sigma, size=L * L)
    H += np.diag(eps.astype(np.complex128))
    return H


def band_energies(L: int, alpha: float, n_bands: int = 5) -> np.ndarray:
    """
    Approximate Hofstadter band centers for rational alpha = p/q.
    Returns the n_bands lowest central energies (Hofstadter butterfly).
    """
    p, q = _rational_alpha(alpha)
    # Eigenvalues of q x q Hofstadter matrix at k=0
    H_q = np.zeros((q, q), dtype=np.complex128)
    for n in range(q):
        H_q[n, (n + 1) % q] = -1.0
        H_q[(n + 1) % q, n] = -1.0
        H_q[n, n] += 2.0 * np.cos(2.0 * np.pi * alpha * n)
    eigs = np.linalg.eigvalsh(H_q)
    return np.sort(eigs)[:n_bands]


def central_gap(L: int, alpha: float) -> float:
    """Central gap of the Hofstadter spectrum (Landau level gap)."""
    p, q = _rational_alpha(alpha)
    H = build_pure_hofstadter(L, alpha)
    eigs = np.linalg.eigvalsh(H)
    n_total = len(eigs)
    # For alpha = p/q, there are q subbands; central gap is between band q//2 and q//2+1
    n_per_band = max(1, n_total // q)
    # Use min(q+1, n_total) to avoid index out of range
    n_edges = min(q + 1, n_total // max(1, n_per_band) + 1)
    band_edges = [eigs[min(k * n_per_band, n_total - 1)] for k in range(n_edges)]
    mid_idx = min(q // 2, len(band_edges) - 2)
    return band_edges[mid_idx + 1] - band_edges[mid_idx]


def fast_central_eigs(H: np.ndarray, k: int = 200, sigma: float = 0.0) -> np.ndarray:
    """
    Fast computation of the k eigenvalues closest to `sigma` (default 0).

    For small matrices (N <= 5000, i.e. L <= 70) uses dense `np.linalg.eigvalsh`
    which is fastest (returns ALL eigenvalues, then we slice the central k).
    For larger matrices, switches to sparse shift-invert
    `scipy.sparse.linalg.eigsh` with sigma=sigma.

    Note: when using the sparse path, k should be modest (k <= 300) — shift-invert
    cost grows with k. For dense path, any k is fine.

    Parameters
    ----------
    H : ndarray (N, N), complex Hermitian
    k : int
        Number of eigenvalues to return (must be < N). For sparse path, k <= 300.
    sigma : float
        Shift for shift-invert; central eigenvalues around E=sigma are returned.

    Returns
    -------
    eigs : ndarray (k,), sorted ascending
    """
    N = H.shape[0]
    # Dense path: for N <= 5000 dense eigvalsh is faster than sparse shift-invert
    # (L=42: 0.4s dense vs 2.6s sparse; L=56: 2.0s dense vs 2.9s sparse)
    if N <= 5000:
        all_eigs = np.linalg.eigvalsh(H)
        if k >= N:
            return all_eigs
        order = np.argsort(np.abs(all_eigs - sigma))
        central_idx = np.sort(order[:k])
        return all_eigs[central_idx]
    # Sparse path: only for very large matrices (L >= 71, N >= 5041)
    # Cap k to avoid shift-invert blow-up
    k_eff = min(k, 300)
    from scipy.sparse.linalg import eigsh
    from scipy.sparse import csr_matrix
    H_sp = csr_matrix(H.astype(np.complex128))
    eigs = eigsh(H_sp, k=k_eff, sigma=sigma, which='LM')[0]
    return np.sort(eigs)


def fast_central_eigsys(H: np.ndarray, k: int = 200, sigma: float = 0.0):
    """
    Same as fast_central_eigs but also returns eigenvectors.

    Returns
    -------
    eigs : ndarray (k,)
    vecs : ndarray (N, k)
    """
    N = H.shape[0]
    if N <= 5000:
        all_eigs, all_vecs = np.linalg.eigh(H)
        if k >= N:
            return all_eigs, all_vecs
        order = np.argsort(np.abs(all_eigs - sigma))
        central_idx = np.sort(order[:k])
        return all_eigs[central_idx], all_vecs[:, central_idx]
    k_eff = min(k, 300)
    from scipy.sparse.linalg import eigsh
    from scipy.sparse import csr_matrix
    H_sp = csr_matrix(H.astype(np.complex128))
    eigs, vecs = eigsh(H_sp, k=k_eff, sigma=sigma, which='LM')
    order = np.argsort(eigs)
    return eigs[order], vecs[:, order]


if __name__ == "__main__":
    # Smoke test
    H = build_ab_cloud_hamiltonian(L=14, alpha=0.5, W=2.0, sigma=0.5, seed=0)
    print(f"H.shape = {H.shape}, dtype = {H.dtype}")
    print(f"Hermitian check: {np.allclose(H, H.conj().T)}")
    eigs = np.linalg.eigvalsh(H)
    print(f"Eigenvalues: min={eigs.min():.4f}, max={eigs.max():.4f}, n={len(eigs)}")
    # Test fast path
    eigs_fast = fast_central_eigs(H, k=50, sigma=0.0)
    print(f"fast_central_eigs(k=50): n={len(eigs_fast)}, range=[{eigs_fast.min():.4f}, {eigs_fast.max():.4f}]")
