"""
ab_cloud_sweeps.py
==================
Dense parameter-sweep infrastructure for the AB-cloud verification suite.

This module provides vectorised helpers for performing parameter sweeps
across many values of:
    - α  (flux per plaquette)
    - W  (vortex/disorder strength)
    - L  (linear lattice size)
    - N_v (number of vortices)
    - L_statistic  (window size for Σ², Δ₃)
    - s  (pair correlation argument)
    - τ  (form factor argument)
    - σ  (scaling parameter)
    - N_ζ  (number of Riemann zeros)

Every sweep returns a dict of arrays suitable for plotting and χ²/KS tests.

Designed for the EXTENDED verification suite (V38–V80): the goal is to give
each verification a dense grid of values (not just 1–2 points) so that we
can confirm the monograph claims across the entire parameter space.
"""
from __future__ import annotations

import os
import sys
import numpy as np
import time
from typing import Callable

# allow both `from python.ab_cloud_sweeps import ...` and `from ab_cloud_sweeps import ...`
_THIS = os.path.dirname(os.path.abspath(__file__))
if _THIS not in sys.path:
    sys.path.insert(0, _THIS)

from ab_cloud_hamiltonian import (
    build_ab_cloud_hamiltonian, build_pure_hofstadter,
    build_random_anderson, build_random_gue, VortexConfig,
)
from ab_cloud_stats import (
    mean_level_spacing_ratio, spacings_from_levels,
    sigma2_statistic, delta3_statistic,
    sigma2_GUE_exact, delta3_GUE_exact,
    f_gue_two_sided, R2_empirical, R2_GUE, R2_Poisson,
    chi_square_uniform, ks_against_wigner_dyson,
    wigner_dyson_pdf,
)


# ============================================================
# 1.  α-sweep: ⟨r⟩ vs α  (find GUE-optimal flux)
# ============================================================
def sweep_r_vs_alpha(alphas: np.ndarray, L: int = 18, W: float = 0.5,
                     N_v: int = 5, seeds: list[int] = None) -> dict:
    """Compute ⟨r⟩(α) for each α in `alphas`, averaged over seeds."""
    if seeds is None:
        seeds = [1, 2, 3]
    r_mean = np.zeros_like(alphas)
    r_err = np.zeros_like(alphas)
    for i, alpha in enumerate(alphas):
        samples = []
        for s in seeds:
            cfg = VortexConfig(Lx=L, Ly=L, N_v=N_v, W=W, alpha=float(alpha), seed=s)
            H, _ = build_ab_cloud_hamiltonian(cfg)
            ev = np.linalg.eigvalsh(H)
            sp = spacings_from_levels(ev)
            r, _ = mean_level_spacing_ratio(sp)
            samples.append(r)
        r_mean[i] = np.mean(samples)
        r_err[i] = np.std(samples) / np.sqrt(len(samples))
    return {"alphas": alphas, "r_mean": r_mean, "r_err": r_err,
            "L": L, "W": W, "N_v": N_v, "seeds": seeds}


# ============================================================
# 2.  L-sweep: ⟨r⟩(L)  (finite-size scaling)
# ============================================================
def sweep_r_vs_L(Ls: list[int], alpha: float = 1.0/7.0, W: float = 0.5,
                 N_v: int = 5, seeds: list[int] = None) -> dict:
    """Compute ⟨r⟩(L) at fixed α, W, N_v."""
    if seeds is None:
        seeds = [1, 2, 3]
    r_mean = np.zeros(len(Ls))
    r_err = np.zeros(len(Ls))
    for i, L in enumerate(Ls):
        samples = []
        for s in seeds:
            cfg = VortexConfig(Lx=L, Ly=L, N_v=N_v, W=W, alpha=alpha, seed=s)
            H, _ = build_ab_cloud_hamiltonian(cfg)
            ev = np.linalg.eigvalsh(H)
            sp = spacings_from_levels(ev)
            r, _ = mean_level_spacing_ratio(sp)
            samples.append(r)
        r_mean[i] = np.mean(samples)
        r_err[i] = np.std(samples) / np.sqrt(len(samples))
    return {"Ls": np.array(Ls), "r_mean": r_mean, "r_err": r_err,
            "alpha": alpha, "W": W, "N_v": N_v, "seeds": seeds}


# ============================================================
# 3.  W-sweep: ⟨r⟩(W)  (Anderson transition)
# ============================================================
def sweep_r_vs_W(Ws: np.ndarray, alpha: float = 1.0/7.0, L: int = 14,
                 N_v: int = 5, seeds: list[int] = None) -> dict:
    """Compute ⟨r⟩(W) at fixed α, L, N_v."""
    if seeds is None:
        seeds = [1, 2]
    r_mean = np.zeros_like(Ws)
    r_err = np.zeros_like(Ws)
    for i, W in enumerate(Ws):
        samples = []
        for s in seeds:
            cfg = VortexConfig(Lx=L, Ly=L, N_v=N_v, W=float(W), alpha=alpha, seed=s)
            H, _ = build_ab_cloud_hamiltonian(cfg)
            ev = np.linalg.eigvalsh(H)
            sp = spacings_from_levels(ev)
            r, _ = mean_level_spacing_ratio(sp)
            samples.append(r)
        r_mean[i] = np.mean(samples)
        r_err[i] = np.std(samples) / np.sqrt(len(samples))
    return {"Ws": Ws, "r_mean": r_mean, "r_err": r_err,
            "alpha": alpha, "L": L, "N_v": N_v, "seeds": seeds}


# ============================================================
# 4.  N_v-sweep: ⟨r⟩(N_v)  (vortex density effect)
# ============================================================
def sweep_r_vs_Nv(Nvs: list[int], alpha: float = 1.0/7.0, L: int = 14,
                  W: float = 0.5, seeds: list[int] = None) -> dict:
    """Compute ⟨r⟩(N_v) at fixed α, L, W."""
    if seeds is None:
        seeds = [1, 2]
    r_mean = np.zeros(len(Nvs))
    r_err = np.zeros(len(Nvs))
    for i, N_v in enumerate(Nvs):
        samples = []
        for s in seeds:
            cfg = VortexConfig(Lx=L, Ly=L, N_v=int(N_v), W=W, alpha=alpha, seed=s)
            H, _ = build_ab_cloud_hamiltonian(cfg)
            ev = np.linalg.eigvalsh(H)
            sp = spacings_from_levels(ev)
            r, _ = mean_level_spacing_ratio(sp)
            samples.append(r)
        r_mean[i] = np.mean(samples)
        r_err[i] = np.std(samples) / np.sqrt(len(samples))
    return {"Nvs": np.array(Nvs), "r_mean": r_mean, "r_err": r_err,
            "alpha": alpha, "L": L, "W": W, "seeds": seeds}


# ============================================================
# 5.  Σ²(L) dense sweep on ζ-zeros
# ============================================================
def sweep_sigma2(unfolded: np.ndarray, L_grid: np.ndarray) -> dict:
    """Σ²_data(L), Σ²_GUE_exact(L), Σ²_Poisson(L)=L, and f_GUE(L)."""
    s2_data = np.array([sigma2_statistic(unfolded, float(L)) for L in L_grid])
    s2_gue = np.array([sigma2_GUE_exact(float(L)) for L in L_grid])
    s2_pois = L_grid.copy()
    f_gue = np.array([f_gue_two_sided(d, p, g)
                      for d, p, g in zip(s2_data, s2_pois, s2_gue)])
    return {"L": L_grid, "data": s2_data, "GUE": s2_gue,
            "Poisson": s2_pois, "f_GUE": f_gue}


# ============================================================
# 6.  Δ₃(L) dense sweep on ζ-zeros
# ============================================================
def sweep_delta3(unfolded: np.ndarray, L_grid: np.ndarray) -> dict:
    """Δ₃_data(L), Δ₃_GUE_exact(L), Δ₃_Poisson(L)=L/15, and f_GUE(L)."""
    d3_data = np.array([delta3_statistic(unfolded, float(L)) for L in L_grid])
    d3_gue = np.array([delta3_GUE_exact(float(L)) for L in L_grid])
    d3_pois = L_grid / 15.0
    f_gue = np.array([f_gue_two_sided(d, p, g)
                      for d, p, g in zip(d3_data, d3_pois, d3_gue)])
    return {"L": L_grid, "data": d3_data, "GUE": d3_gue,
            "Poisson": d3_pois, "f_GUE": f_gue}


# ============================================================
# 7.  R₂(s) dense sweep
# ============================================================
def sweep_R2(unfolded: np.ndarray, s_grid: np.ndarray, ds: float = 0.05) -> dict:
    """R₂_data(s), R₂_GUE(s), R₂_Poisson(s)=1, and KS-like deviation."""
    R2_data = R2_empirical(unfolded, s_grid, ds=ds)
    R2_gue = R2_GUE(s_grid)
    R2_pois = R2_Poisson(s_grid)
    dev = np.abs(R2_data - R2_gue)
    return {"s": s_grid, "data": R2_data, "GUE": R2_gue,
            "Poisson": R2_pois, "deviation": dev,
            "max_dev": float(np.max(dev)), "mean_dev": float(np.mean(dev))}


# ============================================================
# 8.  Spectral form factor K(τ) sweep
# ============================================================
def spectral_form_factor(unfolded: np.ndarray, tau_grid: np.ndarray,
                         averaging_window: float = 0.05) -> dict:
    """
    Spectral form factor K(τ) = (1/N) |Σ_n exp(i τ x_n)|².
    Smoothed by averaging over a small window around each τ.
    """
    N = len(unfolded)
    K = np.zeros_like(tau_grid)
    for i, tau in enumerate(tau_grid):
        # averaging over [tau - w/2, tau + w/2]
        sub_taus = np.linspace(tau - averaging_window/2,
                               tau + averaging_window/2, 5)
        ks = []
        for t in sub_taus:
            phase = np.exp(1j * t * unfolded)
            K_raw = np.abs(np.sum(phase))**2 / N
            ks.append(K_raw)
        K[i] = np.mean(ks)
    # GUE prediction: K(τ) = τ for τ<1, =1 for τ≥1
    K_gue = np.minimum(tau_grid, 1.0)
    return {"tau": tau_grid, "data": K, "GUE": K_gue}


# ============================================================
# 9.  σ-scan (scaling parameter) dense
# ============================================================
def sweep_sigma_scan(spacings: np.ndarray, sigmas: np.ndarray) -> dict:
    """For each σ, compute KS(spacings/σ || Wigner-Dyson)."""
    ks_vals = np.zeros_like(sigmas)
    p_vals = np.zeros_like(sigmas)
    for i, sigma in enumerate(sigmas):
        if sigma <= 0:
            ks_vals[i] = np.nan
            p_vals[i] = np.nan
            continue
        scaled = spacings / sigma
        d, p = ks_against_wigner_dyson(scaled)
        ks_vals[i] = d
        p_vals[i] = p
    sigma_star = sigmas[np.nanargmin(ks_vals)]
    return {"sigmas": sigmas, "ks": ks_vals, "pvals": p_vals,
            "sigma_star": float(sigma_star)}


# ============================================================
# 10.  ⟨r⟩_ζ finite-N scaling
# ============================================================
def sweep_r_zeta_vs_N(Ns: list[int], zeta_zeros_full: np.ndarray) -> dict:
    """For each N, compute ⟨r⟩ on the first N ζ-zeros."""
    from ab_cloud_zeta import unfold_rvm
    r_vals = np.zeros(len(Ns))
    r_errs = np.zeros(len(Ns))
    mean_spacings = np.zeros(len(Ns))
    for i, N in enumerate(Ns):
        zs = zeta_zeros_full[:N]
        unfolded = unfold_rvm(zs)
        sp = np.diff(unfolded)
        sp = sp[sp > 0]
        mean_spacings[i] = np.mean(sp)
        r, err = mean_level_spacing_ratio(sp)
        r_vals[i] = r
        r_errs[i] = err
    return {"Ns": np.array(Ns), "r": r_vals, "r_err": r_errs,
            "mean_spacings": mean_spacings}


# ============================================================
# 11.  Hofstadter butterfly spectrum (dense α sweep)
# ============================================================
def sweep_hofstadter_spectrum(alphas: np.ndarray, L: int = 12,
                              W: float = 0.0) -> dict:
    """For each α, build pure Hofstadter and store sorted eigenvalues."""
    all_evs = []
    for a in alphas:
        H = build_pure_hofstadter(L, L, alpha=float(a), seed=0)
        ev = np.sort(np.linalg.eigvalsh(H))
        all_evs.append(ev)
    return {"alphas": alphas, "eigenvalues": all_evs, "L": L}


# ============================================================
# 12.  p(s) histogram on multiple α
# ============================================================
def sweep_spacing_pdf(alphas: list[float], L: int = 18, W: float = 0.5,
                      N_v: int = 5, bins: np.ndarray = None) -> dict:
    """For each α, compute the spacing histogram and return PDFs."""
    if bins is None:
        bins = np.linspace(0.0, 4.0, 41)
    centers = 0.5 * (bins[:-1] + bins[1:])
    pdfs = {}
    for alpha in alphas:
        all_sp = []
        for seed in [1, 2, 3]:
            cfg = VortexConfig(Lx=L, Ly=L, N_v=N_v, W=W, alpha=alpha, seed=seed)
            H, _ = build_ab_cloud_hamiltonian(cfg)
            ev = np.linalg.eigvalsh(H)
            sp = spacings_from_levels(ev)
            sp = sp / np.mean(sp)
            all_sp.append(sp)
        all_sp = np.concatenate(all_sp)
        counts, _ = np.histogram(all_sp, bins=bins, density=True)
        pdfs[f"alpha={alpha:.4f}"] = counts
    return {"centers": centers, "pdfs": pdfs, "alphas": alphas,
            "wigner_dyson": wigner_dyson_pdf(centers)}


# ============================================================
# 13.  Moment of spacings <s^q>
# ============================================================
def spacing_moments(spacings: np.ndarray, qs: list[int]) -> dict:
    """Compute <s^q> for q in `qs`.  GUE values: <s^q> = Γ(q+3/2)·(π/4)^(q+3/2)·..."""
    moments = np.array([np.mean(spacings**q) for q in qs])
    # GUE Wigner-Dyson surmise moments: <s^q> = (π/4)^(3/2) * Γ(q+3/2) (normalized so mean=1)
    from scipy.special import gamma as gamma_func
    # mean of Wigner-Dyson surmise (32/π²)s² exp(-4s²/π) is 3π/16
    # so to normalize to mean=1, divide by 3π/16
    gue_moments = np.array([
        gamma_func(q + 1.5) * (np.pi/4)**1.5 / ((3*np.pi/16)**q) / gamma_func(1.5) * (np.pi/4)**1.5
        for q in qs
    ])
    # simpler: just compute numerically
    s_grid = np.linspace(0.001, 10, 10000)
    pdf = wigner_dyson_pdf(s_grid)
    pdf = pdf / np.trapz(pdf, s_grid)
    mean_wd = np.trapz(s_grid * pdf, s_grid)
    gue_moments = np.array([np.trapz((s_grid/mean_wd)**q * pdf, s_grid) for q in qs])
    return {"qs": np.array(qs), "data": moments, "GUE": gue_moments}


# ============================================================
# 14.  χ² heat-map: (α, W) plane
# ============================================================
def sweep_chi2_alpha_W(alphas: np.ndarray, Ws: np.ndarray, L: int = 12,
                       N_v: int = 5, n_bins: int = 10) -> dict:
    """Compute χ²(spacings vs Wigner-Dyson) on a grid of (α, W)."""
    chi2_grid = np.zeros((len(alphas), len(Ws)))
    for i, alpha in enumerate(alphas):
        for j, W in enumerate(Ws):
            all_sp = []
            for seed in [1, 2]:
                cfg = VortexConfig(Lx=L, Ly=L, N_v=N_v, W=float(W),
                                   alpha=float(alpha), seed=seed)
                H, _ = build_ab_cloud_hamiltonian(cfg)
                ev = np.linalg.eigvalsh(H)
                sp = spacings_from_levels(ev)
                sp = sp / np.mean(sp)
                all_sp.append(sp)
            all_sp = np.concatenate(all_sp)
            chi2, df = chi_square_uniform(all_sp, s_max=3.0, n_bins=n_bins)
            chi2_grid[i, j] = chi2 / max(df, 1)
    return {"alphas": alphas, "Ws": Ws, "chi2_per_df": chi2_grid}


# ============================================================
# 15.  IDOS (integrated density of states) sweep
# ============================================================
def idos_spectrum(alpha: float, L: int = 14, W: float = 0.0, N_v: int = 0) -> dict:
    """Compute IDOS: cumulative count vs energy."""
    if N_v > 0:
        cfg = VortexConfig(Lx=L, Ly=L, N_v=N_v, W=W, alpha=alpha, seed=1)
        H, _ = build_ab_cloud_hamiltonian(cfg)
    else:
        H = build_pure_hofstadter(L, L, alpha=alpha, seed=0)
    ev = np.sort(np.linalg.eigvalsh(H))
    N = len(ev)
    idos = np.arange(1, N + 1) / N
    return {"E": ev, "IDOS": idos, "alpha": alpha, "L": L, "W": W, "N_v": N_v}


# ============================================================
# 16.  Band gap analysis for α = p/q
# ============================================================
def band_gaps_alpha_pq(pq_pairs: list[tuple[int, int]], L: int = 14) -> dict:
    """For each (p,q), compute α=p/q spectrum and detect q sub-bands + gaps."""
    results = {}
    for p, q in pq_pairs:
        alpha = p / q
        H = build_pure_hofstadter(L, L, alpha=alpha, seed=0)
        ev = np.sort(np.linalg.eigvalsh(H))
        # detect gaps: spacings > 5× median
        sp = np.diff(ev)
        median_sp = np.median(sp)
        gap_idx = np.where(sp > 5 * median_sp)[0]
        gaps = [(ev[i], ev[i+1], ev[i+1] - ev[i]) for i in gap_idx]
        n_bands = len(gaps) + 1
        results[f"α={p}/{q}"] = {"eigenvalues": ev, "gaps": gaps,
                                  "n_bands_detected": n_bands,
                                  "n_bands_expected": q}
    return results


# ============================================================
# 17.  Dirac cone dispersion E(k_x) at α=1/2
# ============================================================
def dirac_dispersion(L: int = 16, n_k: int = 50) -> dict:
    """
    For α=1/2 pure Hofstadter on L×L lattice, sweep k_x in [-π, π] and
    record the central 4 eigenvalues.  Verify linear dispersion near k=0.
    """
    kxs = np.linspace(-np.pi, np.pi, n_k)
    central_evs = np.zeros((n_k, 4))
    for i, kx in enumerate(kxs):
        # build Hofstadter with twisted BC in x (kx)
        N = L * L
        H = np.zeros((N, N), dtype=complex)
        alpha = 0.5
        for ix in range(L):
            for j in range(L):
                idx = ix * L + j
                ix2 = (ix + 1) % L
                # x-hopping: include twist kx on the wrap-around bond
                tx = -1.0 if ix < L - 1 else -np.exp(1j * kx)
                H[idx, ix2 * L + j] += tx
                H[ix2 * L + j, idx] += np.conj(tx)
                j2 = (j + 1) % L
                phase = 2 * np.pi * alpha * ix
                H[idx, ix * L + j2] += -np.exp(1j * phase)
                H[ix * L + j2, idx] += -np.exp(-1j * phase)
        H = 0.5 * (H + H.conj().T)
        ev = np.sort(np.linalg.eigvalsh(H))
        central_evs[i] = ev[L*L//2 - 2 : L*L//2 + 2]
    return {"kxs": kxs, "central_evs": central_evs, "L": L}


# ============================================================
# 18.  Bootstrap confidence interval for Σ²(L)
# ============================================================
def bootstrap_sigma2(unfolded: np.ndarray, L: float, n_boot: int = 100,
                     seed: int = 0) -> tuple[float, float]:
    """Bootstrap std-dev of Σ²(L)."""
    rng = np.random.default_rng(seed)
    N = len(unfolded)
    vals = []
    for _ in range(n_boot):
        idx = rng.integers(0, N, size=N)
        u_boot = unfolded[idx]
        u_boot = np.sort(u_boot)
        vals.append(sigma2_statistic(u_boot, L))
    return float(np.std(vals))


# ============================================================
# 19.  Bootstrap confidence interval for Δ₃(L)
# ============================================================
def bootstrap_delta3(unfolded: np.ndarray, L: float, n_boot: int = 100,
                     seed: int = 0) -> tuple[float, float]:
    """Bootstrap std-dev of Δ₃(L)."""
    rng = np.random.default_rng(seed)
    N = len(unfolded)
    vals = []
    for _ in range(n_boot):
        idx = rng.integers(0, N, size=N)
        u_boot = np.sort(unfolded[idx])
        vals.append(delta3_statistic(u_boot, L))
    return float(np.std(vals))
