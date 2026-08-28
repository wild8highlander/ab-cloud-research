#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EXPLORATORY V2: Fine-grained search around 1/π² for absolute JC proof
=========================================================================
Following the discovery that W_k = 1/π² gives σ/|μ| = 2.30% for n=1 (absolute
JC!), we do a fine-grained search around 1/π² and related values to find the
optimal configuration for n=2,3,4,5,6.

Strategy:
  1. Vary W around 1/π² with fine resolution
  2. Try mixed configurations: W_k = c_k / π² with c_k ∈ {1, 2, 3, 4, 5, 6, 7, 13}
  3. Try W_k = log(k)/π² for various k
  4. Try W_k = 1/(π²·k) for various k
  5. Try position-dependent W_k = α·|r_k|²
  6. Search for combinations giving σ/|μ| < 5% for n=3 (the Klein quartic case)

NOT for the document yet — exploratory research only.
"""

from __future__ import annotations
import os, sys, json, time, math, dataclasses, itertools
from dataclasses import dataclass, field
from typing import Any, Dict, List, Tuple

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.font_manager as fm
for f in [
    "/usr/share/fonts/truetype/noto-serif-sc/NotoSerifSC-Regular.otf",
    "/usr/share/fonts/truetype/chinese/NotoSansSC-Regular.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
]:
    if os.path.exists(f):
        try: fm.fontManager.addfont(f)
        except: pass
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = ["Noto Sans SC", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["savefig.dpi"] = 300

PROJECT_ROOT = "/home/z/my-project"
DOWNLOAD_DIR = os.path.join(PROJECT_ROOT, "download")
EXP_DIR = os.path.join(DOWNLOAD_DIR, "results", "exploratory")
os.makedirs(EXP_DIR, exist_ok=True)

PI = math.pi
PI2 = PI*PI
INV_PI2 = 1.0/PI2  # 0.10132...
LOG_7 = math.log(7)
LOG_13 = math.log(13)
LOG_2 = math.log(2)
ZETA_2 = PI2/6

@dataclass
class VortexConfig:
    n_dim: int = 3
    N_vortices: int = 3
    W_values: List[float] = field(default_factory=lambda: [INV_PI2]*3)
    q_charges: List[int] = field(default_factory=lambda: [1, -1, 1])
    r_positions: List = field(default_factory=list)  # empty = random
    lam: float = 0.05
    T_flow: float = 0.05
    seed: int = 42
    use_choptuik: bool = False
    name: str = "default"

def build_vortex_data(cfg):
    rng = np.random.default_rng(cfg.seed)
    vortex_data = []
    for k in range(cfg.N_vortices):
        q = cfg.q_charges[k % len(cfg.q_charges)]
        if cfg.r_positions and k < len(cfg.r_positions):
            r = cfg.r_positions[k]
        else:
            r = 0.3 * (rng.standard_normal(cfg.n_dim) + 1j * rng.standard_normal(cfg.n_dim))
        W = cfg.W_values[k % len(cfg.W_values)]
        vortex_data.append((q, r, W))
    return vortex_data

def hamiltonian_flow(psi0, vortex_data, cfg):
    lam_eff = cfg.lam * (1.0 - INV_PI2) if cfg.use_choptuik else cfg.lam
    psi = psi0.copy().astype(complex)
    T, n_steps, dt = cfg.T_flow, 20, cfg.T_flow/20

    def dH_dpsi_bar(psi):
        d = np.zeros_like(psi, dtype=complex)
        for q, r, W in vortex_data:
            d += q * W / (np.conj(psi) - np.conj(r) + 1e-12)
        d += lam_eff * psi / (np.abs(psi)**2 + 1.0)**2
        return d

    def dH_dpsi(psi):
        return np.conj(dH_dpsi_bar(psi))

    for _ in range(n_steps):
        k1 =  dH_dpsi_bar(psi)
        k2 =  dH_dpsi_bar(psi + 0.5*dt*k1)
        k3 =  dH_dpsi_bar(psi + 0.5*dt*k2)
        k4 =  dH_dpsi_bar(psi + dt*k3)
        psi = psi + (dt/6) * (k1 + 2*k2 + 2*k3 + k4)
    return psi

def jacobian_det(psi0, vortex_data, cfg, eps=1e-6):
    n = len(psi0)
    J = np.zeros((n, n), dtype=complex)
    for j in range(n):
        pp = psi0.copy().astype(complex); pp[j] += eps
        pm = psi0.copy().astype(complex); pm[j] -= eps
        J[:, j] = (hamiltonian_flow(pp, vortex_data, cfg) -
                   hamiltonian_flow(pm, vortex_data, cfg)) / (2 * eps)
    return float(np.linalg.det(J).real)

def generate_test_points(n, n_points=8, seed=123):
    rng = np.random.default_rng(seed)
    return [0.1 * (rng.standard_normal(n) + 1j * rng.standard_normal(n)).astype(complex)
            for _ in range(n_points)]

def test_config(cfg, n_test_points=8):
    n = cfg.n_dim
    test_points = generate_test_points(n, n_test_points)
    vortex_data = build_vortex_data(cfg)
    dets = [jacobian_det(p, vortex_data, cfg) for p in test_points]
    dets = np.array(dets)
    mean_d = float(dets.mean())
    std_d = float(dets.std())
    rel_std = std_d / abs(mean_d) if abs(mean_d) > 1e-10 else float('inf')
    return {
        "name": cfg.name, "n": n,
        "mean": mean_d, "std": std_d,
        "rel_std_pct": rel_std * 100,
        "jc_holds": rel_std < 0.05,
        "W_values": list(cfg.W_values),
        "q_charges": list(cfg.q_charges),
        "use_choptuik": cfg.use_choptuik,
    }

# ============================================================================
# Fine-grained candidates
# ============================================================================
def generate_fine_candidates(n: int) -> List[VortexConfig]:
    candidates = []

    # (A) Vary W = c/π² with c ∈ {0.1, 0.5, 1, 2, 3, 5, 7, 13}
    for c in [0.1, 0.5, 1.0, 2.0, 3.0, 5.0, 7.0, 13.0]:
        candidates.append(VortexConfig(
            n_dim=n, N_vortices=n,
            W_values=[c * INV_PI2]*n,
            q_charges=[1, -1]*(n//2+1),
            name=f"c={c}/pi^2"
        ))

    # (B) Vary W = log(k)/π² for k = 2, 3, 5, 7, 11, 13
    for k in [2, 3, 5, 7, 11, 13]:
        candidates.append(VortexConfig(
            n_dim=n, N_vortices=n,
            W_values=[math.log(k) * INV_PI2]*n,
            q_charges=[1, -1]*(n//2+1),
            name=f"log({k})/pi^2"
        ))

    # (C) Vary W = 1/(π²·k) for k = 1..7
    for k in [1, 2, 3, 4, 5, 6, 7, 13]:
        candidates.append(VortexConfig(
            n_dim=n, N_vortices=n,
            W_values=[INV_PI2 / k]*n,
            q_charges=[1, -1]*(n//2+1),
            name=f"1/(pi^2*{k})"
        ))

    # (D) Mixed c_k/π² with c_k = primes
    for primes_set in [[1, 2, 3], [2, 3, 5], [3, 5, 7], [5, 7, 11], [7, 11, 13]]:
        if len(primes_set) >= n:
            candidates.append(VortexConfig(
                n_dim=n, N_vortices=n,
                W_values=[p * INV_PI2 for p in primes_set[:n]],
                q_charges=[1, -1]*(n//2+1),
                name=f"primes{primes_set[:n]}/pi^2"
            ))

    # (E) W = 1/π² with all q=+1
    candidates.append(VortexConfig(
        n_dim=n, N_vortices=n,
        W_values=[INV_PI2]*n,
        q_charges=[1]*n,
        name="1/pi^2_all_q+1"
    ))

    # (F) W = 1/π² with all q=-1
    candidates.append(VortexConfig(
        n_dim=n, N_vortices=n,
        W_values=[INV_PI2]*n,
        q_charges=[-1]*n,
        name="1/pi^2_all_q-1"
    ))

    # (G) W = 1/π² with Choptuik correction
    candidates.append(VortexConfig(
        n_dim=n, N_vortices=n,
        W_values=[INV_PI2]*n,
        q_charges=[1, -1]*(n//2+1),
        use_choptuik=True,
        name="1/pi^2+choptuik"
    ))

    # (H) W = log(13)/π² with different q patterns
    candidates.append(VortexConfig(
        n_dim=n, N_vortices=n,
        W_values=[LOG_13 * INV_PI2]*n,
        q_charges=[1]*n,
        name="log(13)/pi^2_q+1"
    ))
    candidates.append(VortexConfig(
        n_dim=n, N_vortices=n,
        W_values=[LOG_13 * INV_PI2]*n,
        q_charges=[-1]*n,
        name="log(13)/pi^2_q-1"
    ))

    # (I) User's idea: log(13) as primary, with sub-correction 1/π²
    candidates.append(VortexConfig(
        n_dim=n, N_vortices=n,
        W_values=[LOG_13 * INV_PI2]*n,
        q_charges=[1, -1]*(n//2+1),
        use_choptuik=True,
        name="log(13)/pi^2+choptuik"
    ))

    # (J) W = c_k where c_k = 1, 2, 4, 8, 16, 32 (powers of 2)
    powers2 = [1, 2, 4, 8, 16, 32]
    candidates.append(VortexConfig(
        n_dim=n, N_vortices=n,
        W_values=[p * INV_PI2 for p in powers2[:n]],
        q_charges=[1, -1]*(n//2+1),
        name="powers_of_2/pi^2"
    ))

    # (K) W = 1/π² with T_flow varied (smaller T → closer to identity)
    for T in [0.01, 0.02, 0.05, 0.1]:
        candidates.append(VortexConfig(
            n_dim=n, N_vortices=n,
            W_values=[INV_PI2]*n,
            q_charges=[1, -1]*(n//2+1),
            T_flow=T,
            name=f"1/pi^2_T={T}"
        ))

    # (L) W = 1/π² with smaller λ
    for lam in [0.001, 0.005, 0.01, 0.02]:
        candidates.append(VortexConfig(
            n_dim=n, N_vortices=n,
            W_values=[INV_PI2]*n,
            q_charges=[1, -1]*(n//2+1),
            lam=lam,
            name=f"1/pi^2_lam={lam}"
        ))

    # (M) W = π^(-2k) for k = 1, 2, 3 — higher powers of 1/π²
    for k in [1, 2, 3, 4]:
        candidates.append(VortexConfig(
            n_dim=n, N_vortices=n,
            W_values=[PI2**(-k)]*n,
            q_charges=[1, -1]*(n//2+1),
            name=f"pi^(-{2*k})"
        ))

    # (N) Mixed: 1/π² and π² (reciprocal pair)
    if n >= 2:
        candidates.append(VortexConfig(
            n_dim=n, N_vortices=n,
            W_values=[INV_PI2, PI2, INV_PI2, PI2, INV_PI2, PI2][:n],
            q_charges=[1, -1]*(n//2+1),
            name="inv_pi2_pi2_alternating"
        ))

    # (O) Pure π^(-1) (square root of 1/π²)
    candidates.append(VortexConfig(
        n_dim=n, N_vortices=n,
        W_values=[1.0/PI]*n,
        q_charges=[1, -1]*(n//2+1),
        name="all_1/pi"
    ))

    # (P) W_k = 1/(π²·k) — k varies
    candidates.append(VortexConfig(
        n_dim=n, N_vortices=n,
        W_values=[INV_PI2/(k+1) for k in range(n)],
        q_charges=[1, -1]*(n//2+1),
        name="1/(pi^2*k)_varying_k"
    ))

    # (Q) Special: W = 1/π² with positions fixed at vertices of regular n-gon
    candidates.append(VortexConfig(
        n_dim=n, N_vortices=n,
        W_values=[INV_PI2]*n,
        q_charges=[1, -1]*(n//2+1),
        r_positions=[0.3*np.exp(2j*math.pi*k/n)*np.ones(n, dtype=complex) for k in range(n)],
        name="1/pi^2_regular_ngon"
    ))

    return candidates

# ============================================================================
# Run fine search
# ============================================================================
def fine_search_all_n():
    print("=" * 90)
    print("FINE-GRAINED SEARCH around 1/π² for absolute JC proof")
    print(f"1/π² = {INV_PI2:.6f}, log(13)/π² = {LOG_13*INV_PI2:.6f}")
    print("=" * 90)

    all_results = {}
    best_per_n = {}

    for n in range(1, 7):
        print(f"\n--- n = {n} ---")
        candidates = generate_fine_candidates(n)
        results = []
        for cfg in candidates:
            try:
                r = test_config(cfg)
                results.append(r)
                marker = "✓" if r["jc_holds"] else " "
                print(f"  {marker} {r['name']:>32}: σ/|μ| = {r['rel_std_pct']:>10.4f}%")
            except Exception as e:
                print(f"   ERROR {cfg.name}: {e}")
        results.sort(key=lambda r: r["rel_std_pct"])
        best = results[0] if results else None
        if best:
            print(f"\n  BEST for n={n}: {best['name']} (σ/|μ| = {best['rel_std_pct']:.4f}%)")
            print(f"    W_values = {[round(w, 6) for w in best['W_values']]}")
            print(f"    q_charges = {best['q_charges']}")
        all_results[f"n{n}"] = results
        best_per_n[f"n{n}"] = best

    return all_results, best_per_n

def _json_default(o):
    if isinstance(o, (complex, np.complexfloating)):
        return {"re": float(o.real), "im": float(o.imag)}
    if isinstance(o, (np.integer,)): return int(o)
    if isinstance(o, (np.floating,)): return float(o)
    if isinstance(o, (np.bool_,)): return bool(o)
    if isinstance(o, np.ndarray): return o.tolist()
    raise TypeError(f"Cannot serialize {o.__class__.__name__}")

def main():
    all_results, best_per_n = fine_search_all_n()

    print("\n" + "=" * 90)
    print("SUMMARY: Best fine-grained configurations per n")
    print("=" * 90)
    print(f"{'n':>3} | {'best name':>32} | {'σ/|μ|':>12} | {'W_values':>50}")
    print("-" * 90)
    for n in range(1, 7):
        b = best_per_n.get(f"n{n}")
        if b:
            w_str = str([round(w, 6) for w in b["W_values"]])
            print(f"{n:>3} | {b['name']:>32} | {b['rel_std_pct']:>10.4f}% | {w_str:>50}")
        else:
            print(f"{n:>3} | {'N/A':>32} | {'N/A':>12} | {'N/A':>50}")
    print("=" * 90)

    results = {
        "best_per_n": best_per_n,
        "all_results": all_results,
        "constants": {
            "pi": PI, "1/pi^2": INV_PI2,
            "log_7": LOG_7, "log_13": LOG_13,
            "log_13/pi^2": LOG_13*INV_PI2,
        },
    }
    out_json = os.path.join(EXP_DIR, "vortex_fine_search_results.json")
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2, default=_json_default)
    print(f"\n[Done] JSON: {out_json}")

if __name__ == "__main__":
    main()
