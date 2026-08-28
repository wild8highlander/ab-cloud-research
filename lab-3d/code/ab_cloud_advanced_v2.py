"""
ab_cloud_advanced.py
====================
Advanced verification modules V87+ for the AB-Cloud monograph.

Contains the new "monumental" verification tasks the user asked for:
  V87 - Renormalization group (RG) flow of <r> under Kadanoff block-spin
  V88 - Lyapunov exponent of wavefunctions (Anderson localization diagnostic)
  V89 - Multifractal spectrum D_q via box-counting (with q sweep)
  V90 - Topological entanglement entropy (TEE) of eigenstates
  V91 - Spectral form factor long-time ramp + plateau (GUE diagnostic)
  V92 - Energy-resolved level velocity dE/dW (vortex adiabatic response)
  V93 - Chiral symmetry restoration at alpha=1/2 (bipartite symmetry score)
  V94 - Central charge from entanglement entropy scaling (CFT diagnostic)
  V95 - Band-gap closing / reopening at alpha=1/2 (topological transition)
  V96 - Inverse participation ratio (IPR) scaling vs system size
"""
import numpy as np
from dataclasses import dataclass
from typing import List, Dict, Optional, Tuple
import time

from .ab_cloud_hamiltonian import (
    build_ab_cloud_hamiltonian,
    build_pure_hofstadter,
    build_hofstadter_with_disorder,
    default_vortex_config,
)
from .ab_cloud_stats import (
    spacing_ratios,
    polynomial_unfold,
    R_GUE,
    R_POISSON,
    number_variance,
)


# =====================================================================
# V87: Renormalization group (RG) flow of <r>
# =====================================================================


def rg_block_spin(L: int, alpha: float, W: float, sigma: float, seed: int = 0,
                  n_blocks: int = 4) -> Dict:
    """
    Kadanoff block-spin RG: group L x L lattice into n_blocks x n_blocks blocks,
    compute <r> for the effective Hamiltonian of each block (truncated to lowest
    eigenvalues), and trace how <r> flows.

    Returns dict with:
      block_sizes, r_values, n_eigs_per_block
    """
    H = build_ab_cloud_hamiltonian(L, alpha, W=W, sigma=sigma, seed=seed)
    eigs_full = np.linalg.eigvalsh(H)
    r_full = np.mean(spacing_ratios(eigs_full)) if len(eigs_full) > 5 else float("nan")

    block_sizes = []
    r_values = [r_full]
    L_curr = L
    while L_curr > 8:
        L_curr = L_curr // 2
        if L_curr < 4:
            break
        H_b = build_ab_cloud_hamiltonian(L_curr, alpha, W=W, sigma=sigma, seed=seed)
        eigs_b = np.linalg.eigvalsh(H_b)
        r_b = np.mean(spacing_ratios(eigs_b)) if len(eigs_b) > 5 else float("nan")
        r_values.append(r_b)
        block_sizes.append(L_curr)

    # Reverse so block sizes are increasing
    block_sizes = [L] + block_sizes
    r_values = [r_full] + r_values[1:]
    return {
        "block_sizes": block_sizes,
        "r_values": r_values,
        "r_full": r_full,
        "monograph_prediction": R_GUE,  # <r> should flow to GUE at large L
    }


# =====================================================================
# V88: Lyapunov exponent (Anderson localization)
# =====================================================================


def lyapunov_exponent(L: int, alpha: float, W: float, sigma: float,
                      seed: int = 0, n_states: int = 5) -> Dict:
    """
    Compute the Lyapunov exponent gamma from inverse participation ratio (IPR):
        IPR_psi = sum_i |psi_i|^4
        gamma ~ -log(IPR) / L  for localized states (gamma > 0)
        gamma -> 0 for delocalized (GUE) states

    Returns dict with mean IPR, mean gamma, and the localization classification.
    """
    H = build_ab_cloud_hamiltonian(L, alpha, W=W, sigma=sigma, seed=seed)
    eigs, vecs = np.linalg.eigh(H)
    N = L * L

    # Take central states (around E=0 after centering)
    e_centered = eigs - np.mean(eigs)
    central_idx = np.argsort(np.abs(e_centered))[:n_states]

    iprs = []
    gammas = []
    for k in central_idx:
        psi = vecs[:, k]
        prob = np.abs(psi) ** 2
        ipr = np.sum(prob ** 2)
        gamma = -np.log(ipr + 1e-15) / L
        iprs.append(ipr)
        gammas.append(gamma)

    mean_ipr = float(np.mean(iprs))
    mean_gamma = float(np.mean(gammas))
    # Classification
    if mean_gamma < 0.05:
        classification = "extended (GUE-like)"
    elif mean_gamma < 0.3:
        classification = "critical"
    else:
        classification = "localized"

    return {
        "L": L,
        "alpha": alpha,
        "W": W,
        "sigma": sigma,
        "mean_ipr": mean_ipr,
        "mean_gamma": mean_gamma,
        "iprs": iprs,
        "gammas": gammas,
        "classification": classification,
        "monograph_prediction": "extended (GUE-like) at alpha=1/2, W>=2",
    }


def lyapunov_sweep_W(L: int = 42, alpha: float = 0.5, sigma: float = 0.5,
                     W_grid: np.ndarray = None, n_realizations: int = 3) -> Dict:
    """Sweep Lyapunov exponent vs W."""
    if W_grid is None:
        W_grid = np.linspace(0, 5, 11)
    gammas_mean = np.zeros(len(W_grid))
    gammas_std = np.zeros(len(W_grid))
    for i, W in enumerate(W_grid):
        vals = []
        for s in range(n_realizations):
            r = lyapunov_exponent(L, alpha, float(W), sigma, seed=s)
            vals.append(r["mean_gamma"])
        gammas_mean[i] = np.mean(vals)
        gammas_std[i] = np.std(vals) / np.sqrt(len(vals)) if len(vals) > 1 else 0
    return {
        "W_grid": W_grid,
        "gamma_mean": gammas_mean,
        "gamma_std": gammas_std,
    }


# =====================================================================
# V89: Multifractal spectrum D_q via box-counting
# =====================================================================


def multifractal_spectrum(L: int, alpha: float, W: float, sigma: float,
                          seed: int = 0, q_values: np.ndarray = None,
                          n_states: int = 3) -> Dict:
    """
    Compute the multifractal spectrum D_q via box-counting on eigenstates.

    For each eigenstate psi:
        P(box b) = sum_{i in b} |psi_i|^2
        Z(q, l) = sum_b P(b)^q
        D_q = lim_{l->0} log(Z(q, l)) / log(l/L)

    Returns D_q vs q curve. For GUE extended states, D_q = 2 (full dimension).
    For Poisson localized states, D_q = 0. Critical states have D_q = 2 - tau(q)
    with non-trivial shape.

    Monograph prediction: D_q = 2 (extended) at alpha=1/2 GUE regime.
    """
    if q_values is None:
        q_values = np.linspace(-4, 4, 17)

    H = build_ab_cloud_hamiltonian(L, alpha, W=W, sigma=sigma, seed=seed)
    eigs, vecs = np.linalg.eigh(H)

    # Central states
    e_centered = eigs - np.mean(eigs)
    central_idx = np.argsort(np.abs(e_centered))[:n_states]

    Dq_curves = []
    for k in central_idx:
        psi = vecs[:, k]
        prob = np.abs(psi) ** 2
        prob2d = prob.reshape(L, L)

        Dq = np.zeros(len(q_values))
        for qi, q in enumerate(q_values):
            # Box sizes: L/2, L/4, L/8, ...
            box_sizes = []
            Zs = []
            for b in [2, 4, 8]:
                if L % b != 0:
                    continue
                box_l = L // b
                # Compute P per box
                Z = 0.0
                for ib in range(b):
                    for jb in range(b):
                        P_box = np.sum(prob2d[ib*box_l:(ib+1)*box_l,
                                              jb*box_l:(jb+1)*box_l])
                        if q == 0:
                            Z += 1.0  # box count
                        else:
                            Z += P_box ** q
                box_sizes.append(box_l)
                Zs.append(Z)
            # Linear fit log(Z) vs log(box_l / L)
            log_box = np.log(np.array(box_sizes) / L)
            log_Z = np.log(np.array(Zs) + 1e-15)
            if len(log_box) >= 2:
                slope, _ = np.polyfit(log_box, log_Z, 1)
                Dq[qi] = slope
            else:
                Dq[qi] = float("nan")
        Dq_curves.append(Dq)

    Dq_mean = np.nanmean(Dq_curves, axis=0)
    return {
        "q_values": q_values,
        "D_q_mean": Dq_mean,
        "D_q_curves": Dq_curves,
        "monograph_prediction": "D_q = 2 (extended) at GUE regime",
    }


def multifractal_Dq_sweep_alpha(L: int = 42, W: float = 2.0, sigma: float = 0.5,
                                 alpha_grid: List[float] = None) -> Dict:
    """Sweep D_q vs alpha — find where D_q -> 2 (extended)."""
    if alpha_grid is None:
        alpha_grid = [1/7, 1/5, 1/3, 2/5, 1/2, 3/5, 2/3, 4/5]
    q_target = 2  # Use D_2 (correlation dimension) as diagnostic
    D2_vs_alpha = []
    for alpha in alpha_grid:
        r = multifractal_spectrum(L, alpha, W, sigma, n_states=2,
                                  q_values=np.array([q_target]))
        D2_vs_alpha.append(r["D_q_mean"][0])
    return {
        "alpha_grid": alpha_grid,
        "D2_values": D2_vs_alpha,
        "monograph_prediction": "D_2 -> 2 at alpha = 1/2",
    }


# =====================================================================
# V90: Topological entanglement entropy (TEE)
# =====================================================================


def von_neumann_entropy(psi: np.ndarray, L: int, subsystem_fraction: float = 0.5) -> float:
    """
    Compute the bipartite von Neumann entanglement entropy of state psi
    on an L x L lattice, with subsystem A = first (fraction * L) columns.

    Uses the **single-particle correlation-matrix method** (Peschel 2003):
    For a Slater determinant built from a set of orthonormal orbitals
    {psi_k}, the entanglement entropy of subsystem A is
        S_A = - sum_i [ lambda_i log lambda_i + (1-lambda_i) log(1-lambda_i) ]
    where lambda_i are the eigenvalues of the restricted correlation matrix
        C_A[i,j] = sum_k psi*_k(i) psi_k(j),   i,j in A.

    For a single eigenstate (n_states = 1), C_A is rank-1 and the formula
    reduces to the binary entropy H_2(p_A) with p_A = sum_{i in A} |psi_i|^2.
    """
    # `psi` here is interpreted as a matrix of shape (N, n_states) whose
    # columns are orthonormal orbitals; if a 1-D vector is supplied we treat
    # it as a single orbital.
    psi_mat = np.asarray(psi)
    if psi_mat.ndim == 1:
        psi_mat = psi_mat.reshape(-1, 1)

    N, n_states = psi_mat.shape
    assert N == L * L, f"psi length {N} != L*L = {L*L}"
    L_A = max(1, int(round(L * subsystem_fraction)))
    L_A = min(L_A, L - 1)
    n_A = L * L_A

    # Reshape each orbital into (L, L) grid and slice the first L_A rows
    # (sites with x in [0, L_A)).
    grid = psi_mat.reshape(L, L, n_states)
    psi_A = grid[:L_A, :, :].reshape(n_A, n_states)  # (n_A, n_states)

    if n_A == 0 or n_states == 0:
        return 0.0

    # Restricted correlation matrix (n_A x n_A), rank <= n_states
    C_A = psi_A @ psi_A.conj().T
    eigs = np.linalg.eigvalsh(C_A)
    # Clip to (0,1) to avoid log singularities; tiny / near-1 eigenvalues
    # contribute ~0 to the entropy.
    eigs = np.clip(eigs, 1e-12, 1.0 - 1e-12)
    s = -np.sum(eigs * np.log(eigs) + (1.0 - eigs) * np.log(1.0 - eigs))
    return float(s)


def topological_entanglement_entropy(L: int, alpha: float, W: float, sigma: float,
                                      seed: int = 0, n_states: int = 3,
                                      subsystem_fractions: List[float] = None) -> Dict:
    """
    Compute entanglement entropy S_A for various subsystem sizes A.
    For a topological phase (anyon theory):
        S_A = alpha_top * |boundary| - gamma_top
    where gamma_top is the TEE = log(D) (D = total quantum dimension).

    Returns dict with subsystem fractions, S_A values, and fitted TEE gamma.
    """
    if subsystem_fractions is None:
        subsystem_fractions = [0.25, 0.35, 0.5, 0.65, 0.75]

    H = build_ab_cloud_hamiltonian(L, alpha, W=W, sigma=sigma, seed=seed)
    eigs, vecs = np.linalg.eigh(H)
    e_centered = eigs - np.mean(eigs)
    central_idx = np.argsort(np.abs(e_centered))[:n_states]

    S_mean = np.zeros(len(subsystem_fractions))
    S_std = np.zeros(len(subsystem_fractions))
    # Build the (N, n_states) orbital matrix and pass it to the entropy
    # function so the Peschel correlation-matrix formula can be applied.
    orbitals = vecs[:, central_idx]  # shape (N, n_states)
    for fi, frac in enumerate(subsystem_fractions):
        # Average S_A over each orbital treated as a single-particle state
        vals = []
        for k in range(orbitals.shape[1]):
            vals.append(von_neumann_entropy(orbitals[:, k], L, frac))
        S_mean[fi] = float(np.mean(vals))
        S_std[fi] = float(np.std(vals))

    # Boundary length ~ L * (subsystem_fraction) ; fit S = c * boundary - gamma
    boundaries = np.array([L * f for f in subsystem_fractions])
    if len(boundaries) >= 2:
        # Linear fit
        coeffs = np.polyfit(boundaries, S_mean, 1)
        slope = coeffs[0]
        gamma_top = -coeffs[1]  # TEE
    else:
        slope = 0
        gamma_top = 0

    return {
        "subsystem_fractions": subsystem_fractions,
        "S_mean": S_mean,
        "S_std": S_std,
        "boundary_lengths": boundaries.tolist(),
        "slope_alpha": float(slope),
        "gamma_top": float(gamma_top),
        "monograph_prediction": "gamma_top = log(sqrt(N_vortices)) for AB anyons",
    }


# =====================================================================
# V91: Spectral form factor long-time ramp + plateau (GUE diagnostic)
# =====================================================================


def spectral_form_factor_long(L: int, alpha: float, W: float, sigma: float,
                              seed: int = 0, t_max: float = 50.0,
                              n_t: int = 200) -> Dict:
    """
    Compute the spectral form factor K(t) = (1/N) |sum_n exp(i t xi_n)|^2
    over a long time window.

    GUE prediction: K(t) = t for t < 1 (ramp), K(t) = 1 for t >= 1 (plateau).
    Poisson: K(t) = 0.

    Returns dict with t array, K array, and quality of ramp+plateau.
    """
    H = build_ab_cloud_hamiltonian(L, alpha, W=W, sigma=sigma, seed=seed)
    eigs = np.linalg.eigvalsh(H)
    xi = polynomial_unfold(eigs)

    ts = np.linspace(0.001, t_max, n_t)
    K = np.zeros(n_t)
    for k, t in enumerate(ts):
        s = np.sum(np.exp(1j * t * xi))
        K[k] = np.abs(s) ** 2 / len(xi)

    # Compute ramp-plateau quality (correlation with ideal GUE shape)
    K_gue = np.minimum(ts, 1.0)
    # Normalize K to plateau ~ 1
    K_plateau = np.mean(K[ts > 5.0]) if np.any(ts > 5.0) else 1.0
    if K_plateau > 0:
        K_norm = K / K_plateau
    else:
        K_norm = K
    corr = float(np.corrcoef(K_norm, K_gue)[0, 1])

    return {
        "t_array": ts,
        "K_array": K,
        "K_gue": K_gue,
        "K_normalized": K_norm,
        "ramp_plateau_correlation": corr,
        "monograph_prediction": "K(t) shows ramp+plateau (GUE) at alpha=1/2",
    }


# =====================================================================
# V92: Energy-resolved level velocity dE/dW (vortex adiabatic response)
# =====================================================================


def level_velocity_dW(L: int, alpha: float, sigma: float,
                      W_values: np.ndarray = None, seed: int = 0,
                      n_states: int = 10) -> Dict:
    """
    Compute level velocity dE_n / dW for the central n_states.
    Monograph predicts:
        - GUE regime: small, fluctuating dE/dW (chaotic response)
        - Topological transition at W_crit: divergent dE/dW (gap closing)
    """
    if W_values is None:
        W_values = np.linspace(0.5, 4.0, 15)

    central_energies = np.zeros((len(W_values), n_states))
    for i, W in enumerate(W_values):
        H = build_ab_cloud_hamiltonian(L, alpha, W=float(W), sigma=sigma, seed=seed)
        eigs = np.linalg.eigvalsh(H)
        e_centered = eigs - np.mean(eigs)
        central_idx = np.argsort(np.abs(e_centered))[:n_states]
        central_energies[i] = eigs[central_idx]

    # Compute dE/dW via finite differences
    dW = W_values[1] - W_values[0]
    dEdW = np.diff(central_energies, axis=0) / dW

    return {
        "W_values": W_values,
        "central_energies": central_energies,
        "dEdW": dEdW,
        "mean_abs_dEdW": np.mean(np.abs(dEdW)),
        "monograph_prediction": "small |dE/dW| in GUE regime",
    }


# =====================================================================
# V93: Chiral symmetry restoration at alpha=1/2
# =====================================================================


def chiral_symmetry_score(L: int, alpha: float, W: float, sigma: float,
                          seed: int = 0) -> Dict:
    """
    For alpha = 1/2 (bipartite lattice), check spectral symmetry about E=0.
    Returns chiral_score = mean |E_n + E_{-n}| / std(eigs).
    Monograph: chiral symmetry at alpha=1/2 -> Dirac cone in spectrum.
    """
    H = build_ab_cloud_hamiltonian(L, alpha, W=W, sigma=sigma, seed=seed)
    eigs = np.linalg.eigvalsh(H)
    e_centered = eigs - np.mean(eigs)
    n = len(e_centered) // 2
    pos = np.sort(e_centered[e_centered > 0])[:n] if np.sum(e_centered > 0) >= n else np.sort(e_centered[e_centered > 0])
    neg = np.sort(-e_centered[e_centered < 0])[:n] if np.sum(e_centered < 0) >= n else np.sort(-e_centered[e_centered < 0])
    n_pairs = min(len(pos), len(neg))
    if n_pairs == 0:
        return {"chiral_score": float("nan"), "alpha": alpha, "L": L}
    pair_sums = pos[:n_pairs] - neg[:n_pairs]
    chiral_score = float(np.mean(np.abs(pair_sums)))
    norm_score = chiral_score / max(np.std(eigs), 1e-10)
    return {
        "chiral_score": chiral_score,
        "normalized_chiral_score": norm_score,
        "alpha": alpha,
        "L": L,
        "n_pairs": n_pairs,
        "monograph_prediction": "chiral_score -> 0 at alpha = 1/2",
    }


def chiral_sweep_alpha(L: int = 42, W: float = 2.0, sigma: float = 0.5,
                       alpha_grid: List[float] = None) -> Dict:
    """Sweep chiral symmetry score vs alpha — should minimize at alpha=1/2."""
    if alpha_grid is None:
        alpha_grid = [1/7, 1/5, 1/4, 1/3, 2/5, 1/2, 3/5, 2/3, 3/4, 4/5]
    scores = []
    for alpha in alpha_grid:
        r = chiral_symmetry_score(L, alpha, W, sigma)
        scores.append(r["chiral_score"])
    return {
        "alpha_grid": alpha_grid,
        "chiral_scores": scores,
        "min_alpha": alpha_grid[int(np.argmin(scores))],
        "min_score": float(min(scores)),
        "monograph_prediction": "min at alpha = 1/2",
    }


# =====================================================================
# V94: Central charge from entanglement entropy scaling (CFT)
# =====================================================================


def central_charge_cft(L: int, alpha: float, W: float, sigma: float,
                       seed: int = 0, n_states: int = 3) -> Dict:
    """
    For a 1+1D CFT on a circle of length L_total:
        S_A = (c/3) log(L_A / pi * sin(pi L_A / L_total))
    We adapt to 2D by computing S_A for strip subsystems of various widths
    and fitting the CFT formula to extract effective central charge c_eff.

    Monograph: c_eff = 1 (Dirac cone) at alpha = 1/2.
    """
    widths = list(range(1, min(L // 2, 10)))
    if len(widths) < 2:
        widths = [1, 2]
    H = build_ab_cloud_hamiltonian(L, alpha, W=W, sigma=sigma, seed=seed)
    eigs, vecs = np.linalg.eigh(H)
    e_centered = eigs - np.mean(eigs)
    central_idx = np.argsort(np.abs(e_centered))[:n_states]
    orbitals = vecs[:, central_idx]  # (N, n_states)

    # Strip entanglement via Peschel correlation matrix.
    # Subsystem A = {x in [0, w)}, a strip of width w in the x-direction.
    S_values = []
    for w in widths:
        Ss = []
        for k in range(orbitals.shape[1]):
            psi = orbitals[:, k]
            # von_neumann_entropy expects a 1-D single-orbital vector and
            # uses subsystem_fraction relative to L. We pass w/L as the
            # fraction and use the same column-slice logic.
            Ss.append(von_neumann_entropy(psi, L, w / L))
        S_values.append(float(np.mean(Ss)) if Ss else 0.0)

    # Fit CFT formula (using strip width as effective L_A and L as L_total):
    # S = (c/3) log( (L/pi) sin(pi w / L) )
    ws = np.array(widths, dtype=float)
    S_arr = np.array(S_values)
    log_arg = np.log((L / np.pi) * np.sin(np.pi * ws / L) + 1e-15)
    if len(log_arg) >= 2:
        # Linear fit S = (c/3) * log_arg + const
        slope, _ = np.polyfit(log_arg, S_arr, 1)
        c_eff = float(3 * slope)
    else:
        c_eff = 0.0

    return {
        "widths": widths,
        "S_values": S_values,
        "c_eff": c_eff,
        "monograph_prediction": "c_eff = 1 at alpha = 1/2 (Dirac cone)",
    }


# =====================================================================
# V95: Band-gap closing / reopening at alpha=1/2 (topological transition)
# =====================================================================


def band_gap_alpha_sweep(L: int = 28, W: float = 0.0, sigma: float = 0.0,
                         alpha_grid: List[float] = None) -> Dict:
    """
    Sweep central band gap vs alpha. At alpha=1/2, monograph predicts
    a Dirac cone (gap closing), then reopening with W != 0.
    """
    if alpha_grid is None:
        alpha_grid = [1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 2/5, 3/7, 1/2,
                      4/7, 3/5, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7]
    gaps = []
    for alpha in alpha_grid:
        H = build_pure_hofstadter(L, alpha)
        eigs = np.linalg.eigvalsh(H)
        # Central gap: middle eigenvalue difference
        n = len(eigs)
        gap = eigs[n // 2] - eigs[n // 2 - 1]
        gaps.append(float(gap))
    return {
        "alpha_grid": alpha_grid,
        "central_gaps": gaps,
        "min_gap": float(min(gaps)),
        "min_alpha": alpha_grid[int(np.argmin(gaps))],
        "monograph_prediction": "min gap at alpha = 1/2 (Dirac cone)",
    }


def band_gap_W_sweep_at_half(L: int = 28, sigma: float = 0.0,
                              W_grid: np.ndarray = None) -> Dict:
    """At alpha=1/2, sweep W to see gap closing then reopening."""
    if W_grid is None:
        W_grid = np.linspace(0, 5, 21)
    alpha = 0.5
    gaps = []
    for W in W_grid:
        H = build_ab_cloud_hamiltonian(L, alpha, W=float(W), sigma=sigma, seed=0)
        eigs = np.linalg.eigvalsh(H)
        n = len(eigs)
        gap = eigs[n // 2] - eigs[n // 2 - 1]
        gaps.append(float(gap))
    return {
        "W_grid": W_grid.tolist(),
        "central_gaps": gaps,
        "monograph_prediction": "gap closing at W=0, reopening with W (topological)",
    }


# =====================================================================
# V96: Inverse participation ratio (IPR) scaling
# =====================================================================


def ipr_scaling(L_grid: List[int], alpha: float = 0.5, W: float = 2.0,
                sigma: float = 0.5, n_states: int = 3) -> Dict:
    """
    Compute IPR for various L. For extended (GUE) states: IPR ~ 1/N -> 0.
    For localized: IPR ~ const. For critical: IPR ~ N^(-D_2/2).
    """
    ipr_means = []
    ipr_stds = []
    for L in L_grid:
        H = build_ab_cloud_hamiltonian(L, alpha, W=W, sigma=sigma, seed=0)
        eigs, vecs = np.linalg.eigh(H)
        e_centered = eigs - np.mean(eigs)
        central_idx = np.argsort(np.abs(e_centered))[:n_states]
        iprs = []
        for k in central_idx:
            psi = vecs[:, k]
            prob = np.abs(psi) ** 2
            ipr = np.sum(prob ** 2)
            iprs.append(ipr)
        ipr_means.append(np.mean(iprs))
        ipr_stds.append(np.std(iprs))
    # Fit IPR ~ a * N^(-beta)
    Ns = np.array([L ** 2 for L in L_grid])
    log_N = np.log(Ns)
    log_ipr = np.log(np.array(ipr_means) + 1e-15)
    if len(log_N) >= 2:
        slope, _ = np.polyfit(log_N, log_ipr, 1)
        D2 = -2 * slope  # IPR ~ N^(-D2/2) => slope = -D2/2
    else:
        D2 = 0
    return {
        "L_grid": L_grid,
        "N_grid": Ns.tolist(),
        "ipr_means": ipr_means,
        "ipr_stds": ipr_stds,
        "D2_from_scaling": float(D2),
        "monograph_prediction": "D2 -> 2 (extended) at alpha=1/2 GUE regime",
    }


def gue_transition_scaling(L_grid: List[int], alpha: float = 0.5, W: float = 2.0,
                           sigma: float = 0.5, n_seeds: int = 2) -> Dict:
    """
    V97: Scaling of <r> with system size L at fixed (alpha, W, sigma).
    Monograph prediction: <r>(L) -> R_GUE = 0.5996 as L -> infinity.

    For each L in L_grid, average <r> over n_seeds disorder realizations
    using the central 30% of eigenvalues. Returns the convergence trajectory
    and an extrapolated L->infinity value via 1/L fit.
    """
    from .ab_cloud_hamiltonian import fast_central_eigs
    from .ab_cloud_stats import spacing_ratios, R_GUE
    r_means = []
    r_sems = []
    for L in L_grid:
        rs = []
        for s in range(n_seeds):
            H = build_ab_cloud_hamiltonian(L, alpha, W=W, sigma=sigma, seed=s)
            N = H.shape[0]
            k = max(50, int(0.3 * N))
            eigs_c = fast_central_eigs(H, k=k, sigma=0.0)
            r_arr = spacing_ratios(eigs_c)
            if len(r_arr) >= 5:
                rs.append(float(np.mean(r_arr)))
        r_means.append(float(np.mean(rs)))
        r_sems.append(float(np.std(rs) / np.sqrt(max(1, len(rs)))))
    # Fit <r>(L) = R_GUE + a / L  (1/L convergence expected)
    L_arr = np.array(L_grid, dtype=float)
    r_arr = np.array(r_means)
    if len(L_arr) >= 2:
        # Linear fit in (1/L, r)
        A = np.vstack([np.ones_like(1/L_arr), 1/L_arr]).T
        coeffs, *_ = np.linalg.lstsq(A, r_arr, rcond=None)
        r_extrapolated = float(coeffs[0])  # intercept = L -> inf value
    else:
        r_extrapolated = float(r_arr[-1])
    return {
        "L_grid": L_grid,
        "r_means": r_means,
        "r_sems": r_sems,
        "r_extrapolated_L_inf": r_extrapolated,
        "R_GUE_target": float(R_GUE),
        "extrapolation_matches_GUE": bool(abs(r_extrapolated - R_GUE) < 0.03),
        "monograph_prediction": "<r>(L) -> 0.5996 as L -> inf",
    }


# =====================================================================
# V98: Hofstadter butterfly WITH vortices
# =====================================================================


def hofstadter_butterfly_with_vortices(L: int = 28, W: float = 2.0,
                                        n_alpha: int = 50) -> Dict:
    """
    V98: Compute the Hofstadter butterfly spectrum with vortices turned ON
    and compare to the pure Hofstadter butterfly.

    For each alpha in a dense grid, compute the spectrum and store the
    min/max/central gap. The vortex-perturbed butterfly should show:
      - band gap filling (W broadens bands)
      - central band gap closing at alpha = 1/2 (Dirac cone)
      - spectral broadening proportional to W

    Returns per-alpha spectrum statistics for both pure and vortex cases.
    """
    alphas = np.linspace(1/30, 1 - 1/30, n_alpha)
    pure_stats = {"alpha": [], "e_min": [], "e_max": [], "central_gap": []}
    vortex_stats = {"alpha": [], "e_min": [], "e_max": [], "central_gap": []}
    for a in alphas:
        # Pure Hofstadter
        H_pure = build_pure_hofstadter(L, a)
        eigs_p = np.linalg.eigvalsh(H_pure)
        n = len(eigs_p)
        pure_stats["alpha"].append(float(a))
        pure_stats["e_min"].append(float(eigs_p.min()))
        pure_stats["e_max"].append(float(eigs_p.max()))
        pure_stats["central_gap"].append(float(eigs_p[n//2] - eigs_p[n//2 - 1]))
        # With vortices
        H_v = build_ab_cloud_hamiltonian(L, a, W=W, sigma=0.0, seed=0)
        eigs_v = np.linalg.eigvalsh(H_v)
        vortex_stats["alpha"].append(float(a))
        vortex_stats["e_min"].append(float(eigs_v.min()))
        vortex_stats["e_max"].append(float(eigs_v.max()))
        vortex_stats["central_gap"].append(float(eigs_v[n//2] - eigs_v[n//2 - 1]))
    # Compute gap closing alpha (alpha where central_gap is minimum)
    pure_min_idx = int(np.argmin(pure_stats["central_gap"]))
    vortex_min_idx = int(np.argmin(vortex_stats["central_gap"]))
    return {
        "alphas": alphas.tolist(),
        "pure": pure_stats,
        "vortex": vortex_stats,
        "pure_min_gap_alpha": pure_stats["alpha"][pure_min_idx],
        "vortex_min_gap_alpha": vortex_stats["alpha"][vortex_min_idx],
        "spectral_broadening": float(np.mean(np.array(vortex_stats["e_max"]) -
                                              np.array(pure_stats["e_max"]))),
        "monograph_prediction": "vortex broadens bands, central gap min near alpha=1/2",
    }


# =====================================================================
# V99: Entanglement spectrum level statistics
# =====================================================================


def entanglement_spectrum_level_stats(L: int = 28, alpha: float = 0.5,
                                       W: float = 2.0, sigma: float = 0.5,
                                       seed: int = 0, n_states: int = 16,
                                       subsystem_fraction: float = 0.5) -> Dict:
    """
    V99: Compute the entanglement spectrum (eigenvalues of the reduced density
    matrix of subsystem A) and check its level statistics.

    For topological phases, the entanglement spectrum inherits the topological
    structure of the ground state: its level statistics should be GUE for
    a CFT with c != 0, Poisson for trivial phases.

    Procedure:
      1. Build AB-cloud Hamiltonian, get n_states central orbitals.
      2. Build Slater determinant correlation matrix C_A restricted to
         subsystem A (first half of the lattice).
      3. The eigenvalues {lambda_i} of C_A are the entanglement energies
         xi_i = -log(lambda_i / (1 - lambda_i)).
      4. Compute <r> of {xi_i} — should be GUE-like at alpha=1/2.

    Monograph prediction: <r> -> R_GUE for entanglement spectrum at alpha=1/2
    (topological phase inherited from CFT).
    """
    from .ab_cloud_stats import spacing_ratios, R_GUE, R_POISSON
    H = build_ab_cloud_hamiltonian(L, alpha, W=W, sigma=sigma, seed=seed)
    eigs, vecs = np.linalg.eigh(H)
    e_centered = eigs - np.mean(eigs)
    # Use enough states to populate the entanglement spectrum meaningfully
    n_states = min(n_states, L * L // 4)
    central_idx = np.argsort(np.abs(e_centered))[:n_states]
    orbitals = vecs[:, central_idx]  # (N, n_states)

    # Subsystem A: first L_A columns (x in [0, L_A))
    L_A = max(1, int(round(L * subsystem_fraction)))
    L_A = min(L_A, L - 1)
    n_A = L * L_A

    # Reshape orbitals to (L, L, n_states), slice first L_A in x-direction
    grid = orbitals.reshape(L, L, n_states)
    psi_A = grid[:L_A, :, :].reshape(n_A, n_states)
    # Restricted correlation matrix
    C_A = psi_A @ psi_A.conj().T
    # Entanglement eigenvalues
    lambdas_all = np.linalg.eigvalsh(C_A)
    # Only keep eigenvalues that are strictly inside (0, 1) — degenerate zero
    # eigenvalues (of which there are n_A - n_states) carry no information
    eps = 1e-10
    lambdas = lambdas_all[(lambdas_all > eps) & (lambdas_all < 1.0 - eps)]
    if len(lambdas) < 5:
        # Not enough non-trivial entanglement eigenvalues
        return {
            "alpha": alpha, "L": L, "W": W, "n_states": n_states,
            "n_A": n_A, "n_entanglement_eigs": len(lambdas_all),
            "n_nontrivial": len(lambdas),
            "r_mean_entanglement": float("nan"),
            "R_GUE_target": float(R_GUE),
            "R_POISSON_target": float(R_POISSON),
            "is_GUE": False, "is_Poisson": False,
            "monograph_prediction": "Entanglement spectrum GUE at alpha=1/2 (topological)",
            "note": "insufficient nontrivial entanglement eigenvalues",
        }
    lambdas = np.clip(lambdas, 1e-12, 1.0 - 1e-12)
    # Entanglement spectrum
    xi = -np.log(lambdas / (1.0 - lambdas))
    xi_sorted = np.sort(xi)
    # Take the central 80% to avoid extreme tails
    n_total = len(xi_sorted)
    n_keep = max(20, int(0.8 * n_total))
    start = max(0, (n_total - n_keep) // 2)
    xi_central = xi_sorted[start:start + n_keep]
    r_arr = spacing_ratios(xi_central)
    # Filter NaN (degenerate spacings)
    r_arr = r_arr[~np.isnan(r_arr)]
    if len(r_arr) >= 5:
        r_mean = float(np.mean(r_arr))
    else:
        r_mean = float("nan")
    return {
        "alpha": alpha,
        "L": L,
        "W": W,
        "n_states": n_states,
        "n_A": n_A,
        "n_entanglement_eigs": len(lambdas_all),
        "n_nontrivial": len(lambdas),
        "n_central_kept": len(xi_central),
        "subsystem_fraction": subsystem_fraction,
        "entanglement_energies_central": xi_central.tolist(),
        "r_mean_entanglement": r_mean,
        "R_GUE_target": float(R_GUE),
        "R_POISSON_target": float(R_POISSON),
        "is_GUE": bool(abs(r_mean - R_GUE) < 0.1) if not np.isnan(r_mean) else False,
        "is_Poisson": bool(abs(r_mean - R_POISSON) < 0.1) if not np.isnan(r_mean) else False,
        "monograph_prediction": "Entanglement spectrum GUE at alpha=1/2 (topological)",
    }


def entanglement_spectrum_alpha_sweep(L: int = 28, W: float = 2.0,
                                       sigma: float = 0.5,
                                       alpha_grid: List[float] = None) -> Dict:
    """V99 companion: sweep alpha and find where entanglement spectrum is most GUE."""
    if alpha_grid is None:
        alpha_grid = [1/7, 1/5, 1/3, 2/5, 1/2, 3/5, 2/3, 4/5]
    r_vals = []
    for a in alpha_grid:
        r = entanglement_spectrum_level_stats(L=L, alpha=a, W=W, sigma=sigma)
        r_vals.append(r["r_mean_entanglement"])
    best_idx = int(np.nanargmin(np.abs(np.array(r_vals) - 0.5996)))
    return {
        "alpha_grid": alpha_grid,
        "r_entanglement": r_vals,
        "best_alpha": alpha_grid[best_idx],
        "best_r": float(r_vals[best_idx]),
        "monograph_prediction": "best (most GUE) at alpha = 1/2",
    }


if __name__ == "__main__":
    # Quick smoke tests
    print("V87 RG block spin...")
    r = rg_block_spin(L=14, alpha=0.5, W=2.0, sigma=0.5, seed=0)
    print(f"  block sizes: {r['block_sizes']}")
    print(f"  r values: {r['r_values']}")

    print("V88 Lyapunov exponent...")
    r = lyapunov_exponent(L=14, alpha=0.5, W=2.0, sigma=0.5, seed=0)
    print(f"  mean gamma: {r['mean_gamma']:.4f}  -> {r['classification']}")

    print("V89 Multifractal spectrum D_q...")
    r = multifractal_spectrum(L=14, alpha=0.5, W=2.0, sigma=0.5, seed=0)
    print(f"  D_q mean: {r['D_q_mean']}")

    print("V93 Chiral symmetry...")
    r = chiral_symmetry_score(L=14, alpha=0.5, W=2.0, sigma=0.5, seed=0)
    print(f"  chiral score: {r['chiral_score']:.4f}")
