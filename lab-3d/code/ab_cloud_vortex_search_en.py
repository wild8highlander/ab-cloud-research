"""
ab_cloud_vortex_search — English Version
============================================================

Exploratory: Vortex numerical values for absolute JC proof (Chapter 14 research).

This is the English translation of ab_cloud_vortex_search.py.
Russian comments in the code body are preserved for reference.

Original file: ab_cloud_vortex_search.py
"""

# -*- coding: utf-8 -*-
"""
EXPLORATORY: Vortex numerical values for absolute JC proof (Chapter 14 research)
=================================================================================
Systematically searches over numerical values assigned to vortices to find
configurations that give the BEST JC verification (σ/|μ| → 0).

Hypothesis: assigning special numerical values to vortices (like log(13), log(7),
π, e, √2, ζ(2), etc.) may stabilize the Hamiltonian flow and yield configurations
where JC holds absolutely (not just conditionally).

Each vortex is parameterized as:
    vortex_k = (q_k, r_k, α_k)
where:
    q_k ∈ {-1, +1}             — topological charge
    r_k ∈ C^n                  — position (random or special)
    α_k ∈ R                    — numerical "anchor" value (NEW)

The Hamiltonian becomes:
    H(ψ, ψ̄) = Σ_k q_k W_k log||ψ - r_k||² + λ_eff V(ψ)
where W_k = α_k (the anchor value replaces the uniform W).

We search over many α_k configurations:
    (1) All α_k = 1 (baseline, §14.21)
    (2) α_k = log(primes): log(2), log(3), log(5), log(7), log(11), log(13)
    (3) α_k = log(7) for all (Klein quartic connection)
    (4) α_k = ζ(2) = π²/6
    (5) α_k = π, e, √2, √3, √5, √7
    (6) α_k = 1/π² (Choptuik-related)
    (7) Random α_k
    (8) α_k from PSL(2,7) character table
    (9) α_k = 1/n (dimension-scaled)
    (10) α_k = 13 (the user's suggestion)

Goal: find the configuration with smallest σ/|μ| for n=1..6.

NOT for inclusion in the document yet — this is exploratory research.
"""

from __future__ import annotations
import os, sys, json, time, math, dataclasses, itertools
from dataclasses import dataclass, field
from typing import Any, Dict, List, Tuple, Optional

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
FIG_DIR      = os.path.join(DOWNLOAD_DIR, "figures")
RESULTS_DIR  = os.path.join(DOWNLOAD_DIR, "results")
EXP_DIR      = os.path.join(RESULTS_DIR, "exploratory")
os.makedirs(FIG_DIR, exist_ok=True)
os.makedirs(EXP_DIR, exist_ok=True)

PI = math.pi
EULER_E = math.e
SQRT2 = math.sqrt(2)
SQRT3 = math.sqrt(3)
SQRT5 = math.sqrt(5)
SQRT7 = math.sqrt(7)
ZETA_2 = PI*PI/6  # π²/6 ≈ 1.6449
LOG_2 = math.log(2)
LOG_3 = math.log(3)
LOG_5 = math.log(5)
LOG_7 = math.log(7)
LOG_11 = math.log(11)
LOG_13 = math.log(13)
CHOPTUIK = 1.0 - 1.0/(PI*PI)  # 0.89868

# ============================================================================
# 1. Vortex configuration with numerical "anchor" values
# ============================================================================
@dataclass
class VortexConfig:
    """Configuration with numerical anchor values for vortex strengths."""
    n_dim: int = 3
    N_vortices: int = 3
    W_values: List[float] = field(default_factory=lambda: [1.0, 1.0, 1.0])  # α_k
    q_charges: List[int] = field(default_factory=lambda: [1, -1, 1])
    lam: float = 0.05
    T_flow: float = 0.05
    seed: int = 42
    use_choptuik: bool = False
    name: str = "baseline"

def build_vortex_data_with_anchors(cfg: VortexConfig):
    """Build vortex data with custom W_k = α_k values and q_k charges."""
    rng = np.random.default_rng(cfg.seed)
    vortex_data = []
    for k in range(cfg.N_vortices):
        q = cfg.q_charges[k % len(cfg.q_charges)]
        r = 0.3 * (rng.standard_normal(cfg.n_dim) + 1j * rng.standard_normal(cfg.n_dim))
        W = cfg.W_values[k % len(cfg.W_values)]
        vortex_data.append((q, r, W))
    return vortex_data

# ============================================================================
# 2. Hamiltonian flow with anchor values
# ============================================================================
def hamiltonian_flow_anchored(psi0, vortex_data, cfg: VortexConfig):
    """RK4 Hamiltonian flow with anchor values W_k = α_k."""
    lam_eff = cfg.lam * CHOPTUIK if cfg.use_choptuik else cfg.lam
    psi = psi0.copy().astype(complex)
    T = cfg.T_flow
    n_steps = 20
    dt = T / n_steps

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

def jacobian_det_anchored(psi0, vortex_data, cfg, eps=1e-6):
    n = len(psi0)
    J = np.zeros((n, n), dtype=complex)
    for j in range(n):
        psi_plus = psi0.copy().astype(complex); psi_plus[j] += eps
        psi_minus = psi0.copy().astype(complex); psi_minus[j] -= eps
        F_plus = hamiltonian_flow_anchored(psi_plus, vortex_data, cfg)
        F_minus = hamiltonian_flow_anchored(psi_minus, vortex_data, cfg)
        J[:, j] = (F_plus - F_minus) / (2 * eps)
    return float(np.linalg.det(J).real)

def generate_test_points(n, n_points=8, seed=123):
    rng = np.random.default_rng(seed)
    return [0.1 * (rng.standard_normal(n) + 1j * rng.standard_normal(n)).astype(complex)
            for _ in range(n_points)]

# ============================================================================
# 3. Test a single configuration for given n
# ============================================================================
def test_config(cfg: VortexConfig, n_test_points=8) -> Dict[str, Any]:
    n = cfg.n_dim
    test_points = generate_test_points(n, n_test_points)
    vortex_data = build_vortex_data_with_anchors(cfg)
    dets = [jacobian_det_anchored(p, vortex_data, cfg) for p in test_points]
    dets = np.array(dets)
    mean_d = float(dets.mean())
    std_d = float(dets.std())
    rel_std = std_d / abs(mean_d) if abs(mean_d) > 1e-10 else float('inf')
    return {
        "name": cfg.name,
        "n": n,
        "mean": mean_d,
        "std": std_d,
        "rel_std_pct": rel_std * 100,
        "jc_holds": rel_std < 0.05,
        "W_values": list(cfg.W_values),
        "q_charges": list(cfg.q_charges),
        "use_choptuik": cfg.use_choptuik,
    }

# ============================================================================
# 4. Generate candidate configurations
# ============================================================================
def generate_candidates(n: int) -> List[VortexConfig]:
    """Generate many candidate configurations for given n."""
    candidates = []

    # (1) Baseline: all W_k = 1
    candidates.append(VortexConfig(
        n_dim=n, N_vortices=n,
        W_values=[1.0]*n, q_charges=[1, -1]*(n//2+1),
        name="baseline_W=1"
    ))

    # (2) Log of primes: log(2), log(3), log(5), log(7), log(11), log(13)
    prime_logs = [LOG_2, LOG_3, LOG_5, LOG_7, LOG_11, LOG_13]
    candidates.append(VortexConfig(
        n_dim=n, N_vortices=n,
        W_values=prime_logs[:n],
        q_charges=[1, -1]*(n//2+1),
        name="log_primes"
    ))

    # (3) All log(7) — Klein quartic connection
    candidates.append(VortexConfig(
        n_dim=n, N_vortices=n,
        W_values=[LOG_7]*n,
        q_charges=[1, -1]*(n//2+1),
        name="all_log(7)"
    ))

    # (4) ζ(2) = π²/6
    candidates.append(VortexConfig(
        n_dim=n, N_vortices=n,
        W_values=[ZETA_2]*n,
        q_charges=[1, -1]*(n//2+1),
        name="all_zeta(2)"
    ))

    # (5) π, e, √2, √3, √5, √7
    candidates.append(VortexConfig(
        n_dim=n, N_vortices=n,
        W_values=[PI, EULER_E, SQRT2, SQRT3, SQRT5, SQRT7][:n],
        q_charges=[1, -1]*(n//2+1),
        name="constants_pi_e_sqrt"
    ))

    # (6) 1/π² (Choptuik-related)
    candidates.append(VortexConfig(
        n_dim=n, N_vortices=n,
        W_values=[1.0/(PI*PI)]*n,
        q_charges=[1, -1]*(n//2+1),
        name="all_1/pi^2"
    ))

    # (7) User's suggestion: 13 (and log(13))
    candidates.append(VortexConfig(
        n_dim=n, N_vortices=n,
        W_values=[13.0]*n,
        q_charges=[1, -1]*(n//2+1),
        name="all_13"
    ))
    candidates.append(VortexConfig(
        n_dim=n, N_vortices=n,
        W_values=[LOG_13]*n,
        q_charges=[1, -1]*(n//2+1),
        name="all_log(13)"
    ))

    # (8) PSL(2,7) character values (sizes 1, 3, 3, 6, 7, 8)
    psl27_chars = [1.0, 3.0, 3.0, 6.0, 7.0, 8.0]
    candidates.append(VortexConfig(
        n_dim=n, N_vortices=n,
        W_values=psl27_chars[:n],
        q_charges=[1, -1]*(n//2+1),
        name="psl27_char_sizes"
    ))

    # (9) 1/n (dimension-scaled)
    candidates.append(VortexConfig(
        n_dim=n, N_vortices=n,
        W_values=[1.0/n]*n,
        q_charges=[1, -1]*(n//2+1),
        name="all_1/n"
    ))

    # (10) Choptuik correction as W
    candidates.append(VortexConfig(
        n_dim=n, N_vortices=n,
        W_values=[CHOPTUIK]*n,
        q_charges=[1, -1]*(n//2+1),
        name="all_choptuik"
    ))

    # (11) All q=+1 (electron-like)
    candidates.append(VortexConfig(
        n_dim=n, N_vortices=n,
        W_values=[1.0]*n,
        q_charges=[1]*n,
        name="all_q+1_W=1"
    ))

    # (12) All q=-1 (positron-like)
    candidates.append(VortexConfig(
        n_dim=n, N_vortices=n,
        W_values=[1.0]*n,
        q_charges=[-1]*n,
        name="all_q-1_W=1"
    ))

    # (13) q=+1 with log(13), q=-1 with 1/log(13)
    candidates.append(VortexConfig(
        n_dim=n, N_vortices=n,
        W_values=[LOG_13 if i % 2 == 0 else 1.0/LOG_13 for i in range(n)],
        q_charges=[1, -1]*(n//2+1),
        name="log(13)_inverse"
    ))

    # (14) Fibonacci numbers scaled
    fibs = [1, 1, 2, 3, 5, 8, 13, 21]
    candidates.append(VortexConfig(
        n_dim=n, N_vortices=n,
        W_values=[float(f) for f in fibs[:n]],
        q_charges=[1, -1]*(n//2+1),
        name="fibonacci"
    ))

    # (15) Catalan's constant approximation
    catalan = 0.9159655
    candidates.append(VortexConfig(
        n_dim=n, N_vortices=n,
        W_values=[catalan]*n,
        q_charges=[1, -1]*(n//2+1),
        name="all_catalan"
    ))

    # (16) Feigenbaum α and δ
    feig_alpha = 2.5029
    feig_delta = 4.6692
    candidates.append(VortexConfig(
        n_dim=n, N_vortices=n,
        W_values=[feig_alpha, feig_delta, feig_alpha, feig_delta, feig_alpha, feig_delta][:n],
        q_charges=[1, -1]*(n//2+1),
        name="feigenbaum"
    ))

    # (17) Apéry's constant ζ(3)
    zeta3 = 1.2020569
    candidates.append(VortexConfig(
        n_dim=n, N_vortices=n,
        W_values=[zeta3]*n,
        q_charges=[1, -1]*(n//2+1),
        name="all_zeta(3)"
    ))

    # (18) Mixed: log(13) for odd n, π for even n
    candidates.append(VortexConfig(
        n_dim=n, N_vortices=n,
        W_values=[LOG_13 if n % 2 == 1 else PI]*n,
        q_charges=[1, -1]*(n//2+1),
        name="log(13)_odd_pi_even"
    ))

    # (19) τ_Klein eigenvalues (0.1866, 0.1866, 0.7344)
    tau_eigs = [0.1866, 0.1866, 0.7344]
    candidates.append(VortexConfig(
        n_dim=n, N_vortices=n,
        W_values=(tau_eigs + [0.5]*3)[:n],
        q_charges=[1, -1]*(n//2+1),
        name="tau_klein_eigs"
    ))

    # (20) Golden ratio φ = (1+√5)/2
    phi = (1 + SQRT5) / 2
    candidates.append(VortexConfig(
        n_dim=n, N_vortices=n,
        W_values=[phi]*n,
        q_charges=[1, -1]*(n//2+1),
        name="all_golden_ratio"
    ))

    # (21) log(13) with Choptuik correction
    candidates.append(VortexConfig(
        n_dim=n, N_vortices=n,
        W_values=[LOG_13]*n,
        q_charges=[1, -1]*(n//2+1),
        use_choptuik=True,
        name="log(13)+choptuik"
    ))

    # (22) User's idea: log(13) with all q=+1
    candidates.append(VortexConfig(
        n_dim=n, N_vortices=n,
        W_values=[LOG_13]*n,
        q_charges=[1]*n,
        name="log(13)_all_q+1"
    ))

    # (23) log(13) with all q=-1
    candidates.append(VortexConfig(
        n_dim=n, N_vortices=n,
        W_values=[LOG_13]*n,
        q_charges=[-1]*n,
        name="log(13)_all_q-1"
    ))

    # (24) Mix: log(7) and log(13) — two Klein-related primes
    candidates.append(VortexConfig(
        n_dim=n, N_vortices=n,
        W_values=[LOG_7, LOG_13, LOG_7, LOG_13, LOG_7, LOG_13][:n],
        q_charges=[1, -1]*(n//2+1),
        name="log(7)_log(13)_mix"
    ))

    # (25) All log(2) — binary foundation
    candidates.append(VortexConfig(
        n_dim=n, N_vortices=n,
        W_values=[LOG_2]*n,
        q_charges=[1, -1]*(n//2+1),
        name="all_log(2)"
    ))

    return candidates

# ============================================================================
# 5. Run search for all n = 1..6
# ============================================================================
def search_all_n():
    print("=" * 90)
    print("EXPLORATORY SEARCH: Vortex numerical values for absolute JC proof")
    print(f"Constants: π={PI:.4f}, e={EULER_E:.4f}, ζ(2)={ZETA_2:.4f}, "
          f"log(7)={LOG_7:.4f}, log(13)={LOG_13:.4f}")
    print("Goal: find W_k configuration minimizing σ/|μ| for n=1..6")
    print("=" * 90)

    all_results = {}
    best_per_n = {}

    for n in range(1, 7):
        print(f"\n--- n = {n} ---")
        candidates = generate_candidates(n)
        results = []
        for cfg in candidates:
            r = test_config(cfg)
            results.append(r)
            marker = "✓" if r["jc_holds"] else " "
            print(f"  {marker} {r['name']:>30}: σ/|μ| = {r['rel_std_pct']:>10.4f}%")
        # Sort by σ/|μ|
        results.sort(key=lambda r: r["rel_std_pct"])
        best = results[0]
        print(f"\n  BEST for n={n}: {best['name']} (σ/|μ| = {best['rel_std_pct']:.4f}%)")
        print(f"    W_values = {best['W_values']}")
        print(f"    q_charges = {best['q_charges']}")
        all_results[f"n{n}"] = results
        best_per_n[f"n{n}"] = best

    return all_results, best_per_n

# ============================================================================
# 6. Generate summary figure
# ============================================================================
def fig_best_per_n(best_per_n):
    """Fig: best σ/|μ| achieved per n."""
    print("\n[Fig] Generating best-per-n figure")
    n_values = list(range(1, 7))
    best_sigmas = [best_per_n[f"n{n}"]["rel_std_pct"] for n in n_values]
    best_names = [best_per_n[f"n{n}"]["name"] for n in n_values]

    fig, ax = plt.subplots(1, 1, figsize=(11, 6), constrained_layout=True)
    bars = ax.bar(n_values, best_sigmas, color="forestgreen", alpha=0.85,
                   edgecolor="darkgreen")
    ax.axhline(5.0, color="orange", ls="--", lw=1.5,
                label="порог 5% (JC выполняется)")
    for i, (n, sigma, name) in enumerate(zip(n_values, best_sigmas, best_names)):
        ax.text(n, sigma + 0.5, f"{sigma:.2f}%", ha="center", fontsize=10, fontweight="bold")
        ax.text(n, sigma / 2, name, ha="center", fontsize=8, color="white",
                rotation=90, va="center")
    ax.set_xlabel("размерность $n$")
    ax.set_ylabel(r"лучшее $\sigma/|\mu|$ (%)")
    ax.set_title("Лучшие конфигурации вихрей (по числовым значениям $W_k$) для $n=1,...,6$\n"
                  "Цель: найти конфигурацию с $\\sigma/|\\mu| < 5\\%$ (абсолютное доказательство JC)")
    ax.legend()
    ax.grid(alpha=0.3, axis="y")
    ax.set_yscale('log')
    out = os.path.join(EXP_DIR, "best_per_n.png")
    fig.savefig(out, dpi=300)
    plt.close(fig)
    return out

# ============================================================================
# 7. Main
# ============================================================================
def _json_default(o):
    if isinstance(o, (complex, np.complexfloating)):
        return {"re": float(o.real), "im": float(o.imag)}
    if isinstance(o, (np.integer,)): return int(o)
    if isinstance(o, (np.floating,)): return float(o)
    if isinstance(o, (np.bool_,)): return bool(o)
    if isinstance(o, np.ndarray): return o.tolist()
    raise TypeError(f"Cannot serialize {o.__class__.__name__}")

def main():
    all_results, best_per_n = search_all_n()

    fig = fig_best_per_n(best_per_n)

    print("\n" + "=" * 90)
    print("SUMMARY: Best configurations per n")
    print("=" * 90)
    print(f"{'n':>3} | {'best name':>30} | {'σ/|μ|':>12} | {'W_values':>40} | {'q_charges':>20}")
    print("-" * 90)
    for n in range(1, 7):
        b = best_per_n[f"n{n}"]
        w_str = str([round(w, 4) for w in b["W_values"]])
        q_str = str(b["q_charges"])
        print(f"{n:>3} | {b['name']:>30} | {b['rel_std_pct']:>10.4f}% | {w_str:>40} | {q_str:>20}")
    print("=" * 90)

    results = {
        "best_per_n": best_per_n,
        "all_results": all_results,
        "constants": {
            "pi": PI, "e": EULER_E, "zeta_2": ZETA_2,
            "log_7": LOG_7, "log_13": LOG_13, "choptuik": CHOPTUIK,
        },
        "figure": fig,
    }
    out_json = os.path.join(EXP_DIR, "vortex_search_results.json")
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2, default=_json_default)
    print(f"\n[Done] JSON: {out_json}")
    print(f"[Done] Figure: {fig}")

if __name__ == "__main__":
    main()
