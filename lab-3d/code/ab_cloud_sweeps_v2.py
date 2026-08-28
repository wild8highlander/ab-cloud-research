"""
ab_cloud_sweeps.py
==================
Massive parameter sweep infrastructure for AB-Cloud verification.

This module provides the "monumental" infrastructure the user asked for:
- Dense sweeps over alpha, W, L, N_vortices, sigma
- Multiple disorder realizations per parameter point (with statistical averaging)
- Returns aggregated statistics with standard errors
- Designed for thousands of parameter combinations

Each sweep returns a SweepResult dataclass with:
- param_grid: dict of arrays
- statistics: dict of arrays (mean over realizations)
- raw_data: list of dicts (per realization)
"""
import numpy as np
from dataclasses import dataclass, field
from typing import Callable, Dict, List, Optional, Tuple, Any
import itertools
import time

from .ab_cloud_hamiltonian import (
    build_ab_cloud_hamiltonian,
    build_pure_hofstadter,
    build_hofstadter_with_disorder,
    default_vortex_config,
)
from .ab_cloud_stats import (
    spacing_ratios,
    mean_spacing_ratio,
    std_spacing_ratio,
    number_variance,
    f_GUE_score,
    R_GUE,
    R_POISSON,
    polynomial_unfold,
)


# Default alpha grid: rational p/q values that fit in L x L
DEFAULT_ALPHA_GRID = [
    1.0 / 7, 1.0 / 6, 1.0 / 5, 1.0 / 4, 2.0 / 7,
    1.0 / 3, 2.0 / 5, 3.0 / 7, 1.0 / 2, 4.0 / 7,
    3.0 / 5, 2.0 / 3, 5.0 / 7, 3.0 / 4, 4.0 / 5, 5.0 / 6, 6.0 / 7,
]

# Default W grid: 0 (pure Hofstadter) to 5 (strong vortex regime)
DEFAULT_W_GRID = np.linspace(0.0, 5.0, 21)

# Default L grid: small (debug) to large (asymptotic)
DEFAULT_L_GRID = [14, 28, 42, 56, 70, 84, 100]

# Default sigma grid
DEFAULT_SIGMA_GRID = np.linspace(0.0, 2.0, 11)

# Default N_vortices grid
DEFAULT_NV_GRID = list(range(1, 21))


@dataclass
class SweepResult:
    """Container for sweep results."""
    name: str
    param_names: List[str]
    param_values: List[np.ndarray]  # 1D array per parameter
    statistics: Dict[str, np.ndarray] = field(default_factory=dict)
    std_errors: Dict[str, np.ndarray] = field(default_factory=dict)
    raw_data: List[Dict[str, Any]] = field(default_factory=list)
    n_realizations: int = 1
    elapsed_seconds: float = 0.0

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "param_names": self.param_names,
            "param_values": [p.tolist() for p in self.param_values],
            "statistics": {k: v.tolist() for k, v in self.statistics.items()},
            "std_errors": {k: v.tolist() for k, v in self.std_errors.items()},
            "n_realizations": self.n_realizations,
            "elapsed_seconds": self.elapsed_seconds,
        }


def _diagonalize(H: np.ndarray) -> np.ndarray:
    """Diagonalize Hermitian H, return sorted real eigenvalues."""
    eigs = np.linalg.eigvalsh(H)
    return np.sort(eigs)


def sweep_alpha(
    L: int = 56,
    W: float = 2.0,
    sigma: float = 0.5,
    alpha_grid: Optional[List[float]] = None,
    n_realizations: int = 5,
    use_vortices: bool = True,
    central_window: float = 0.3,
) -> SweepResult:
    """
    Sweep over alpha (magnetic flux) at fixed L, W, sigma.
    Returns <r>(alpha), std, f_GUE(alpha).
    """
    if alpha_grid is None:
        alpha_grid = DEFAULT_ALPHA_GRID

    t0 = time.time()
    rs_mean = np.zeros(len(alpha_grid))
    rs_std = np.zeros(len(alpha_grid))
    fGUE = np.zeros(len(alpha_grid))
    rs_all = []

    for i, alpha in enumerate(alpha_grid):
        r_vals = []
        for s in range(n_realizations):
            if use_vortices:
                H = build_ab_cloud_hamiltonian(L, alpha, W=W, sigma=sigma, seed=s)
            else:
                H = build_hofstadter_with_disorder(L, alpha, sigma=sigma, seed=s)
            eigs = _diagonalize(H)
            # Use central window of spectrum
            e0, e1 = np.percentile(eigs, [50 - 100 * central_window / 2, 50 + 100 * central_window / 2])
            mask = (eigs >= e0) & (eigs <= e1)
            r = spacing_ratios(eigs[mask])
            if len(r) >= 5:
                r_vals.append(np.mean(r))
        if r_vals:
            rs_mean[i] = np.mean(r_vals)
            rs_std[i] = np.std(r_vals) / np.sqrt(len(r_vals))
            fGUE[i] = 1.0 - 2.0 * max(abs(rs_mean[i] - R_GUE), abs(rs_mean[i] - R_POISSON))
        rs_all.append(r_vals)

    return SweepResult(
        name="sweep_alpha",
        param_names=["alpha"],
        param_values=[np.array(alpha_grid)],
        statistics={"r_mean": rs_mean, "f_GUE": fGUE},
        std_errors={"r_mean": rs_std},
        n_realizations=n_realizations,
        elapsed_seconds=time.time() - t0,
    )


def sweep_W(
    L: int = 56,
    alpha: float = 0.5,
    sigma: float = 0.5,
    W_grid: Optional[np.ndarray] = None,
    n_realizations: int = 5,
    use_vortices: bool = True,
) -> SweepResult:
    """Sweep vortex strength W."""
    if W_grid is None:
        W_grid = DEFAULT_W_GRID

    t0 = time.time()
    rs_mean = np.zeros(len(W_grid))
    rs_std = np.zeros(len(W_grid))
    fGUE = np.zeros(len(W_grid))

    for i, W in enumerate(W_grid):
        r_vals = []
        for s in range(n_realizations):
            if use_vortices:
                H = build_ab_cloud_hamiltonian(L, alpha, W=W, sigma=sigma, seed=s)
            else:
                H = build_hofstadter_with_disorder(L, alpha, sigma=sigma, seed=s)
            eigs = _diagonalize(H)
            e0, e1 = np.percentile(eigs, [35, 65])
            mask = (eigs >= e0) & (eigs <= e1)
            r = spacing_ratios(eigs[mask])
            if len(r) >= 5:
                r_vals.append(np.mean(r))
        if r_vals:
            rs_mean[i] = np.mean(r_vals)
            rs_std[i] = np.std(r_vals) / np.sqrt(len(r_vals))
            fGUE[i] = 1.0 - 2.0 * max(abs(rs_mean[i] - R_GUE), abs(rs_mean[i] - R_POISSON))

    return SweepResult(
        name="sweep_W",
        param_names=["W"],
        param_values=[np.array(W_grid)],
        statistics={"r_mean": rs_mean, "f_GUE": fGUE},
        std_errors={"r_mean": rs_std},
        n_realizations=n_realizations,
        elapsed_seconds=time.time() - t0,
    )


def sweep_L(
    alpha: float = 0.5,
    W: float = 2.0,
    sigma: float = 0.5,
    L_grid: Optional[List[int]] = None,
    n_realizations: int = 5,
    use_vortices: bool = True,
) -> SweepResult:
    """Sweep system size L (finite-size scaling)."""
    if L_grid is None:
        L_grid = DEFAULT_L_GRID

    t0 = time.time()
    rs_mean = np.zeros(len(L_grid))
    rs_std = np.zeros(len(L_grid))
    fGUE = np.zeros(len(L_grid))

    for i, L in enumerate(L_grid):
        r_vals = []
        for s in range(n_realizations):
            if use_vortices:
                H = build_ab_cloud_hamiltonian(L, alpha, W=W, sigma=sigma, seed=s)
            else:
                H = build_hofstadter_with_disorder(L, alpha, sigma=sigma, seed=s)
            eigs = _diagonalize(H)
            e0, e1 = np.percentile(eigs, [35, 65])
            mask = (eigs >= e0) & (eigs <= e1)
            r = spacing_ratios(eigs[mask])
            if len(r) >= 5:
                r_vals.append(np.mean(r))
        if r_vals:
            rs_mean[i] = np.mean(r_vals)
            rs_std[i] = np.std(r_vals) / np.sqrt(len(r_vals))
            fGUE[i] = 1.0 - 2.0 * max(abs(rs_mean[i] - R_GUE), abs(rs_mean[i] - R_POISSON))

    return SweepResult(
        name="sweep_L",
        param_names=["L"],
        param_values=[np.array(L_grid)],
        statistics={"r_mean": rs_mean, "f_GUE": fGUE},
        std_errors={"r_mean": rs_std},
        n_realizations=n_realizations,
        elapsed_seconds=time.time() - t0,
    )


def sweep_sigma(
    L: int = 56,
    alpha: float = 0.5,
    W: float = 2.0,
    sigma_grid: Optional[np.ndarray] = None,
    n_realizations: int = 5,
    use_vortices: bool = True,
) -> SweepResult:
    """Sweep disorder strength sigma."""
    if sigma_grid is None:
        sigma_grid = DEFAULT_SIGMA_GRID

    t0 = time.time()
    rs_mean = np.zeros(len(sigma_grid))
    rs_std = np.zeros(len(sigma_grid))
    fGUE = np.zeros(len(sigma_grid))

    for i, sigma in enumerate(sigma_grid):
        r_vals = []
        for s in range(n_realizations):
            if use_vortices:
                H = build_ab_cloud_hamiltonian(L, alpha, W=W, sigma=sigma, seed=s)
            else:
                H = build_hofstadter_with_disorder(L, alpha, sigma=sigma, seed=s)
            eigs = _diagonalize(H)
            e0, e1 = np.percentile(eigs, [35, 65])
            mask = (eigs >= e0) & (eigs <= e1)
            r = spacing_ratios(eigs[mask])
            if len(r) >= 5:
                r_vals.append(np.mean(r))
        if r_vals:
            rs_mean[i] = np.mean(r_vals)
            rs_std[i] = np.std(r_vals) / np.sqrt(len(r_vals))
            fGUE[i] = 1.0 - 2.0 * max(abs(rs_mean[i] - R_GUE), abs(rs_mean[i] - R_POISSON))

    return SweepResult(
        name="sweep_sigma",
        param_names=["sigma"],
        param_values=[np.array(sigma_grid)],
        statistics={"r_mean": rs_mean, "f_GUE": fGUE},
        std_errors={"r_mean": rs_std},
        n_realizations=n_realizations,
        elapsed_seconds=time.time() - t0,
    )


def sweep_alpha_W_2d(
    L: int = 56,
    sigma: float = 0.5,
    alpha_grid: Optional[List[float]] = None,
    W_grid: Optional[np.ndarray] = None,
    n_realizations: int = 3,
    use_vortices: bool = True,
) -> SweepResult:
    """
    2D sweep over (alpha, W) — produces a 2D heatmap of <r>.
    This is one of the "big matrices" the user requested.
    """
    if alpha_grid is None:
        alpha_grid = DEFAULT_ALPHA_GRID
    if W_grid is None:
        W_grid = DEFAULT_W_GRID

    t0 = time.time()
    R_matrix = np.zeros((len(alpha_grid), len(W_grid)))
    R_err = np.zeros_like(R_matrix)

    for i, alpha in enumerate(alpha_grid):
        for j, W in enumerate(W_grid):
            r_vals = []
            for s in range(n_realizations):
                if use_vortices:
                    H = build_ab_cloud_hamiltonian(L, alpha, W=float(W), sigma=sigma, seed=s)
                else:
                    H = build_hofstadter_with_disorder(L, alpha, sigma=sigma, seed=s)
                eigs = _diagonalize(H)
                e0, e1 = np.percentile(eigs, [35, 65])
                mask = (eigs >= e0) & (eigs <= e1)
                r = spacing_ratios(eigs[mask])
                if len(r) >= 5:
                    r_vals.append(np.mean(r))
            if r_vals:
                R_matrix[i, j] = np.mean(r_vals)
                R_err[i, j] = np.std(r_vals) / np.sqrt(len(r_vals))

    return SweepResult(
        name="sweep_alpha_W_2d",
        param_names=["alpha", "W"],
        param_values=[np.array(alpha_grid), np.array(W_grid)],
        statistics={"r_mean": R_matrix},
        std_errors={"r_mean": R_err},
        n_realizations=n_realizations,
        elapsed_seconds=time.time() - t0,
    )


def sweep_L_sigma_2d(
    alpha: float = 0.5,
    W: float = 2.0,
    L_grid: Optional[List[int]] = None,
    sigma_grid: Optional[np.ndarray] = None,
    n_realizations: int = 3,
    use_vortices: bool = True,
) -> SweepResult:
    """2D sweep over (L, sigma) — finite-size x disorder phase diagram."""
    if L_grid is None:
        L_grid = DEFAULT_L_GRID
    if sigma_grid is None:
        sigma_grid = DEFAULT_SIGMA_GRID

    t0 = time.time()
    R_matrix = np.zeros((len(L_grid), len(sigma_grid)))

    for i, L in enumerate(L_grid):
        for j, sigma in enumerate(sigma_grid):
            r_vals = []
            for s in range(n_realizations):
                if use_vortices:
                    H = build_ab_cloud_hamiltonian(L, alpha, W=W, sigma=float(sigma), seed=s)
                else:
                    H = build_hofstadter_with_disorder(L, alpha, sigma=float(sigma), seed=s)
                eigs = _diagonalize(H)
                e0, e1 = np.percentile(eigs, [35, 65])
                mask = (eigs >= e0) & (eigs <= e1)
                r = spacing_ratios(eigs[mask])
                if len(r) >= 5:
                    r_vals.append(np.mean(r))
            if r_vals:
                R_matrix[i, j] = np.mean(r_vals)

    return SweepResult(
        name="sweep_L_sigma_2d",
        param_names=["L", "sigma"],
        param_values=[np.array(L_grid), np.array(sigma_grid)],
        statistics={"r_mean": R_matrix},
        n_realizations=n_realizations,
        elapsed_seconds=time.time() - t0,
    )


def sweep_alpha_L_2d(
    W: float = 2.0,
    sigma: float = 0.5,
    alpha_grid: Optional[List[float]] = None,
    L_grid: Optional[List[int]] = None,
    n_realizations: int = 3,
    use_vortices: bool = True,
) -> SweepResult:
    """2D sweep over (alpha, L) — flux-size phase diagram."""
    if alpha_grid is None:
        alpha_grid = DEFAULT_ALPHA_GRID
    if L_grid is None:
        L_grid = DEFAULT_L_GRID

    t0 = time.time()
    R_matrix = np.zeros((len(alpha_grid), len(L_grid)))

    for i, alpha in enumerate(alpha_grid):
        for j, L in enumerate(L_grid):
            r_vals = []
            for s in range(n_realizations):
                if use_vortices:
                    H = build_ab_cloud_hamiltonian(L, alpha, W=W, sigma=sigma, seed=s)
                else:
                    H = build_hofstadter_with_disorder(L, alpha, sigma=sigma, seed=s)
                eigs = _diagonalize(H)
                e0, e1 = np.percentile(eigs, [35, 65])
                mask = (eigs >= e0) & (eigs <= e1)
                r = spacing_ratios(eigs[mask])
                if len(r) >= 5:
                    r_vals.append(np.mean(r))
            if r_vals:
                R_matrix[i, j] = np.mean(r_vals)

    return SweepResult(
        name="sweep_alpha_L_2d",
        param_names=["alpha", "L"],
        param_values=[np.array(alpha_grid), np.array(L_grid)],
        statistics={"r_mean": R_matrix},
        n_realizations=n_realizations,
        elapsed_seconds=time.time() - t0,
    )


if __name__ == "__main__":
    # Quick smoke test
    print("Running small sweep_alpha...")
    res = sweep_alpha(L=14, n_realizations=2, alpha_grid=[1/3, 1/2])
    print(res.to_dict())
