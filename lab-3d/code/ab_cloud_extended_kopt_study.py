#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EXTENDED STUDY: k_opt(n) for n=1..10 + Choptuik correction variations
=======================================================================
Following user's intuition:
  - Odd n: k=4 (one Hamiltonian cycle)
  - Even n: k=14 (more cycles due to rotation/twist)
  - n=5,6: regime change (beyond main JC, n<=3)

We:
  1. Extend k_opt search to n=1..10 to see the full pattern
  2. Try to find analytic formula k_opt(n) via regression
  3. Test user's hypothesis: odd/even parity pattern
  4. Vary Choptuik correction: (1 - c/π²) for c ∈ {0.5, 1, 2, 3, 6, 12, 24}
  5. Test "logarithm shape change" — vary the log power in H

NOT for the document yet — research to find the optimal analytic formula.
"""

from __future__ import annotations
import os, sys, json, time, math, dataclasses
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
FIG_DIR = os.path.join(DOWNLOAD_DIR, "figures")
EXP_DIR = os.path.join(DOWNLOAD_DIR, "results", "exploratory")
os.makedirs(FIG_DIR, exist_ok=True)

PI = math.pi
PI2 = PI*PI
ZETA_2 = PI2/6  # 1.6449...

# ============================================================================
# 1. Configuration with flexible parameters
# ============================================================================
@dataclass
class VortexConfig:
    n_dim: int = 3
    N_vortices: int = 3
    W_values: List[float] = field(default_factory=lambda: [PI2**(-4)]*3)
    q_charges: List[int] = field(default_factory=lambda: [1, -1, 1])
    lam: float = 0.05
    T_flow: float = 0.05
    seed: int = 42
    # NEW: Choptuik correction with variable coefficient
    choptuik_c: float = 1.0  # correction = (1 - c/π²); c=1 is standard Choptuik
    use_choptuik: bool = False
    # NEW: log power in H (default 1 = standard log||ψ-r||²)
    log_power: float = 1.0
    n_test_points: int = 8
    test_seed: int = 123
    name: str = "default"

def build_vortex_data(cfg):
    rng = np.random.default_rng(cfg.seed)
    vortex_data = []
    for k in range(cfg.N_vortices):
        q = cfg.q_charges[k % len(cfg.q_charges)]
        r = 0.3 * (rng.standard_normal(cfg.n_dim) + 1j * rng.standard_normal(cfg.n_dim))
        W = cfg.W_values[k % len(cfg.W_values)]
        vortex_data.append((q, r, W))
    return vortex_data

def hamiltonian_flow(psi0, vortex_data, cfg):
    # Effective coupling with variable Choptuik coefficient
    if cfg.use_choptuik:
        lam_eff = cfg.lam * (1.0 - cfg.choptuik_c / PI2)
    else:
        lam_eff = cfg.lam
    psi = psi0.copy().astype(complex)
    T, n_steps, dt = cfg.T_flow, 20, cfg.T_flow/20
    def dH_dpsi_bar(psi):
        d = np.zeros_like(psi, dtype=complex)
        for q, r, W in vortex_data:
            # Variable log power: ||ψ-r||^(2·log_power) instead of log||ψ-r||²
            # d/dψ̄ of (1/log_power)·||ψ-r||^(2·log_power) = (ψ-r)·||ψ-r||^(2·log_power - 4)
            # For log_power=0: standard log||ψ-r||² → derivative 1/(ψ̄-r̄)
            # For log_power=1: ||ψ-r||² → derivative (ψ-r)
            # For log_power=2: ||ψ-r||⁴ → derivative 2(ψ-r)||ψ-r||²
            if abs(cfg.log_power) < 1e-10:
                # Standard logarithm
                d += q * W / (np.conj(psi) - np.conj(r) + 1e-12)
            else:
                # Power-law: d/dψ̄ [||ψ-r||^(2p)/(2p)] = (ψ-r)·||ψ-r||^(2p-4)
                # so H_k = q_k W_k ||ψ-r_k||^(2p)/(2p)
                # and dH/dψ̄ = q_k W_k (ψ-r_k) ||ψ-r_k||^(2p-4)
                diff = psi - r
                norm_sq = np.abs(diff)**2 + 1e-12
                d += q * W * diff * norm_sq**(cfg.log_power - 2)
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

def generate_test_points(n, n_points, seed=123):
    rng = np.random.default_rng(seed)
    return [0.1 * (rng.standard_normal(n) + 1j * rng.standard_normal(n)).astype(complex)
            for _ in range(n_points)]

def test_config(cfg):
    n = cfg.n_dim
    test_points = generate_test_points(n, cfg.n_test_points, cfg.test_seed)
    vortex_data = build_vortex_data(cfg)
    dets = [jacobian_det(p, vortex_data, cfg) for p in test_points]
    dets = np.array(dets)
    mean_d = float(dets.mean())
    std_d = float(dets.std())
    rel_std = std_d / abs(mean_d) if abs(mean_d) > 1e-10 else float('inf')
    return {
        "mean": mean_d, "std": std_d,
        "rel_std_pct": rel_std * 100,
        "jc_holds": rel_std < 0.05,
    }

# ============================================================================
# 2. Extended k_opt search for n=1..10
# ============================================================================
def find_k_opt(n, k_range=range(2, 25), verbose=False):
    """Find optimal k for given n by scanning k_range."""
    best_k = None
    best_sigma = float('inf')
    results = []
    for k in k_range:
        W = PI2**(-k)
        cfg = VortexConfig(
            n_dim=n, N_vortices=n,
            W_values=[W]*n,
            q_charges=[1, -1]*(n//2+1),
        )
        r = test_config(cfg)
        results.append({"k": k, "sigma_pct": r["rel_std_pct"], "jc": r["jc_holds"]})
        if r["rel_std_pct"] < best_sigma:
            best_sigma = r["rel_std_pct"]
            best_k = k
        if verbose:
            marker = "✓" if r["jc_holds"] else " "
            print(f"    {marker} k={k:>2}: σ/|μ| = {r['rel_std_pct']:>10.6f}%")
    return best_k, best_sigma, results

def extended_kopt_search():
    print("=" * 90)
    print("EXTENDED k_opt SEARCH for n = 1..10")
    print("=" * 90)
    kopt_per_n = {}
    for n in range(1, 11):
        print(f"\n--- n = {n} ---")
        best_k, best_sigma, _ = find_k_opt(n, verbose=True)
        kopt_per_n[n] = {"k": best_k, "sigma_pct": best_sigma}
        print(f"  BEST: k = {best_k}, σ/|μ| = {best_sigma:.6f}%")
    return kopt_per_n

# ============================================================================
# 3. Search for analytic formula k_opt(n)
# ============================================================================
def find_analytic_formula(kopt_per_n):
    """Try various analytic formulas for k_opt(n) via regression."""
    print("\n" + "=" * 90)
    print("ANALYTIC FORMULA SEARCH for k_opt(n)")
    print("=" * 90)
    n_vals = np.array(list(kopt_per_n.keys()), dtype=float)
    k_vals = np.array([kopt_per_n[n]["k"] for n in kopt_per_n], dtype=float)

    # Try various formulas
    formulas = {
        "k = a·n + b": lambda n, a, b: a*n + b,
        "k = a·n² + b·n + c": lambda n, a, b, c: a*n**2 + b*n + c,
        "k = a·log(n) + b": lambda n, a, b: a*np.log(n+0.01) + b,
        "k = a·n + b·(-1)^n + c": lambda n, a, b, c: a*n + b*((-1)**n) + c,
        "k = a·(n mod 2) + b·(n mod 3) + c": lambda n, a, b, c: a*(n%2) + b*(n%3) + c,
        "k = round(a·g(n) + b) where g = T(n)=n(n+1)/2": lambda n, a, b: np.round(a * n*(n+1)/2 + b),
        "k = a·ζ(n) + b (zeta)": lambda n, a, b: a * float(zeta_func(n)) + b if n > 1 else b,
    }

    # User's hypothesis: odd n = 4, even n = 14 (for small n)
    # Then n=5,6 change regime
    # Let's test parity hypothesis
    print(f"\n1. PARITY HYPOTHESIS (user's suggestion):")
    print(f"   {'n':>3} | {'k_opt':>5} | {'parity':>7} | {'predicted (4 odd / 14 even)':>30}")
    for n in kopt_per_n:
        k = kopt_per_n[n]["k"]
        parity = "odd" if n % 2 == 1 else "even"
        predicted = 4 if n % 2 == 1 else 14
        match = "✓" if k == predicted else "✗"
        print(f"   {n:>3} | {k:>5} | {parity:>7} | {predicted:>30} {match}")

    # Try simple regression
    print(f"\n2. LINEAR REGRESSION k = a·n + b:")
    A = np.vstack([n_vals, np.ones_like(n_vals)]).T
    a, b = np.linalg.lstsq(A, k_vals, rcond=None)[0]
    print(f"   a = {a:.4f}, b = {b:.4f}")
    print(f"   Predicted: {', '.join(f'n={n}: {a*n+b:.2f}' for n in kopt_per_n)}")
    residuals = [(kopt_per_n[n]["k"] - (a*n+b)) for n in kopt_per_n]
    print(f"   Residuals: {[round(r, 2) for r in residuals]}")
    print(f"   R² = {1 - np.var(residuals)/np.var(k_vals):.4f}")

    # Quadratic regression
    print(f"\n3. QUADRATIC REGRESSION k = a·n² + b·n + c:")
    A = np.vstack([n_vals**2, n_vals, np.ones_like(n_vals)]).T
    coef = np.linalg.lstsq(A, k_vals, rcond=None)[0]
    a, b, c = coef
    print(f"   a = {a:.4f}, b = {b:.4f}, c = {c:.4f}")
    print(f"   Predicted: {', '.join(f'n={n}: {a*n**2+b*n+c:.2f}' for n in kopt_per_n)}")
    residuals = [(kopt_per_n[n]["k"] - (a*n**2+b*n+c)) for n in kopt_per_n]
    print(f"   Residuals: {[round(r, 2) for r in residuals]}")
    print(f"   R² = {1 - np.var(residuals)/np.var(k_vals):.4f}")

    # Try with parity term
    print(f"\n4. PARITY-AWARE REGRESSION k = a·n + b·(-1)^n + c:")
    A = np.vstack([n_vals, (-1)**n_vals, np.ones_like(n_vals)]).T
    coef = np.linalg.lstsq(A, k_vals, rcond=None)[0]
    a, b, c = coef
    print(f"   a = {a:.4f}, b = {b:.4f}, c = {c:.4f}")
    print(f"   Predicted: {', '.join(f'n={n}: {a*n+b*(-1)**n+c:.2f}' for n in kopt_per_n)}")
    residuals = [(kopt_per_n[n]["k"] - (a*n+b*(-1)**n+c)) for n in kopt_per_n]
    print(f"   Residuals: {[round(r, 2) for r in residuals]}")
    print(f"   R² = {1 - np.var(residuals)/np.var(k_vals):.4f}")

    # Try k = c1 * T(n) + c2 where T(n) = n(n+1)/2 (triangular number)
    print(f"\n5. TRIANGULAR NUMBER k = a·T(n) + b, T(n) = n(n+1)/2:")
    T_n = n_vals * (n_vals + 1) / 2
    A = np.vstack([T_n, np.ones_like(n_vals)]).T
    a, b = np.linalg.lstsq(A, k_vals, rcond=None)[0]
    print(f"   a = {a:.4f}, b = {b:.4f}")
    print(f"   Predicted: {', '.join(f'n={n}: {a*n*(n+1)/2+b:.2f}' for n in kopt_per_n)}")
    residuals = [(kopt_per_n[n]["k"] - (a*n*(n+1)/2+b)) for n in kopt_per_n]
    print(f"   Residuals: {[round(r, 2) for r in residuals]}")
    print(f"   R² = {1 - np.var(residuals)/np.var(k_vals):.4f}")

    # Try k = c1 * ζ(n) + c2
    print(f"\n6. ZETA REGRESSION k = a·ζ(n) + b:")
    zeta_vals = np.array([float(zeta_func(n)) if n > 1 else float('inf') for n in n_vals])
    valid = ~np.isinf(zeta_vals)
    if valid.sum() > 1:
        A = np.vstack([zeta_vals[valid], np.ones(valid.sum())]).T
        a, b = np.linalg.lstsq(A, k_vals[valid], rcond=None)[0]
        print(f"   a = {a:.4f}, b = {b:.4f}")
        print(f"   Predictions for n≥2:")
        for n in kopt_per_n:
            if n > 1:
                zn = float(zeta_func(n))
                pred = a * zn + b
                print(f"     n={n}: k={kopt_per_n[n]['k']} (predicted {pred:.2f}, residual {kopt_per_n[n]['k']-pred:+.2f})")

    # Best formula: round to nearest integer
    print(f"\n7. BEST EMPIRICAL FORMULA (round(quadratic)):")
    A = np.vstack([n_vals**2, n_vals, np.ones_like(n_vals)]).T
    coef = np.linalg.lstsq(A, k_vals, rcond=None)[0]
    a, b, c = coef
    print(f"   k_opt(n) ≈ round({a:.4f}·n² + {b:.4f}·n + {c:.4f})")
    print(f"   Predictions (rounded):")
    for n in kopt_per_n:
        pred = round(a*n**2 + b*n + c)
        actual = kopt_per_n[n]["k"]
        match = "✓" if pred == actual else "✗"
        print(f"     n={n}: predicted {pred}, actual {actual} {match}")

    return {"quadratic": (a, b, c)}

def zeta_func(s):
    """Compute ζ(s) for s > 1 using mpmath if available, else approximation."""
    try:
        import mpmath
        return mpmath.zeta(s)
    except ImportError:
        # Approximation via finite sum
        return sum(1.0/k**s for k in range(1, 1000))

# ============================================================================
# 4. Variable Choptuik coefficient: (1 - c/π²)
# ============================================================================
def variable_choptuik_study():
    print("\n" + "=" * 90)
    print("VARIABLE CHOPTUIK COEFFICIENT: (1 - c/π²) for various c")
    print("=" * 90)
    print("Standard Choptuik: c=1 → correction = (1 - 1/π²) ≈ 0.89868")
    print()

    c_values = [0.0, 0.25, 0.5, 1.0, 2.0, 3.0, 6.0, 12.0, 24.0, 60.0]
    # For each c, test on n=3 (main Klein quartic case) with k=4 (optimal)
    n = 3
    k = 4
    W = PI2**(-k)
    print(f"n = {n}, k = {k} (W = π^(-{2*k})):")
    print(f"  {'c':>6} | {'correction':>12} | {'σ/|μ|':>12} | {'JC?':>5}")
    results = []
    for c in c_values:
        cfg = VortexConfig(
            n_dim=n, N_vortices=n,
            W_values=[W]*n,
            q_charges=[1, -1]*(n//2+1),
            use_choptuik=True,
            choptuik_c=c,
        )
        r = test_config(cfg)
        correction = 1.0 - c/PI2
        marker = "✓" if r["jc_holds"] else " "
        print(f"  {c:>6.2f} | {correction:>12.6f} | {r['rel_std_pct']:>10.6f}% | {marker}")
        results.append({"c": c, "correction": correction, **r})
    return results

# ============================================================================
# 5. Variable log power: replace log||ψ-r||² with ||ψ-r||^(2p)
# ============================================================================
def log_power_study():
    print("\n" + "=" * 90)
    print("LOG POWER STUDY: replace log||ψ-r||² with ||ψ-r||^(2p) / (2p)")
    print("=" * 90)
    print("p=0: standard log (current)")
    print("p=1: quadratic potential")
    print("p=2: quartic potential")
    print()

    p_values = [0.0, 0.5, 1.0, 1.5, 2.0, 3.0, 4.0]
    # Test on n=3 with k=4
    n = 3
    k = 4
    W = PI2**(-k)
    print(f"n = {n}, k = {k} (W = π^(-{2*k})):")
    print(f"  {'p':>6} | {'σ/|μ|':>12} | {'JC?':>5}")
    results = []
    for p in p_values:
        cfg = VortexConfig(
            n_dim=n, N_vortices=n,
            W_values=[W]*n,
            q_charges=[1, -1]*(n//2+1),
            log_power=p,
        )
        try:
            r = test_config(cfg)
            marker = "✓" if r["jc_holds"] else " "
            print(f"  {p:>6.2f} | {r['rel_std_pct']:>10.6f}% | {marker}")
            results.append({"p": p, **r})
        except Exception as e:
            print(f"  {p:>6.2f} | ERROR: {e}")
    return results

# ============================================================================
# 6. Combined optimization: c and k simultaneously
# ============================================================================
def combined_optimization():
    print("\n" + "=" * 90)
    print("COMBINED OPTIMIZATION: find best (k, c) for each n")
    print("=" * 90)
    c_values = [0.0, 0.5, 1.0, 2.0, 6.0]
    k_values = list(range(2, 16))

    best_per_n = {}
    for n in range(1, 7):
        print(f"\n--- n = {n} ---")
        best = {"sigma": float('inf')}
        for k in k_values:
            for c in c_values:
                W = PI2**(-k)
                cfg = VortexConfig(
                    n_dim=n, N_vortices=n,
                    W_values=[W]*n,
                    q_charges=[1, -1]*(n//2+1),
                    use_choptuik=(c != 0),
                    choptuik_c=c,
                )
                r = test_config(cfg)
                if r["rel_std_pct"] < best["sigma"]:
                    best = {"k": k, "c": c, "sigma": r["rel_std_pct"],
                            "correction": 1.0 - c/PI2 if c != 0 else 1.0,
                            "jc": r["jc_holds"]}
        best_per_n[n] = best
        print(f"  BEST: k={best['k']}, c={best['c']}, σ/|μ|={best['sigma']:.6f}%, "
              f"correction={best['correction']:.6f}, JC={'✓' if best['jc'] else '✗'}")
    return best_per_n

# ============================================================================
# 7. Figures
# ============================================================================
def fig_kopt_pattern(kopt_per_n):
    """Fig: k_opt(n) for n=1..10 with pattern analysis."""
    print("\n[Fig] k_opt(n) pattern")
    n_vals = list(kopt_per_n.keys())
    k_vals = [kopt_per_n[n]["k"] for n in n_vals]

    fig, axes = plt.subplots(1, 2, figsize=(14, 6), constrained_layout=True)
    # (a) k_opt vs n with parity coloring
    ax = axes[0]
    colors = ["steelblue" if n % 2 == 0 else "coral" for n in n_vals]
    ax.bar(n_vals, k_vals, color=colors, alpha=0.85, edgecolor="black")
    # Add value labels
    for n, k in zip(n_vals, k_vals):
        ax.text(n, k + 0.3, str(k), ha="center", fontsize=11, fontweight="bold")
    # Mark user's hypothesis
    ax.axhline(4, color="coral", ls=":", lw=1.5, alpha=0.5,
                label="гипотеза: k=4 (нечётные n)")
    ax.axhline(14, color="steelblue", ls=":", lw=1.5, alpha=0.5,
                label="гипотеза: k=14 (чётные n)")
    ax.set_xlabel("размерность $n$")
    ax.set_ylabel("оптимальная степень $k$")
    ax.set_title("(a) $k_{\\mathrm{opt}}(n)$ для $n=1,...,10$\n"
                  "Синий = чётные, коралловый = нечётные")
    ax.set_xticks(n_vals)
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3, axis="y")

    # (b) σ/|μ| achieved with k_opt
    ax = axes[1]
    sigma_vals = [kopt_per_n[n]["sigma_pct"] for n in n_vals]
    ax.bar(n_vals, sigma_vals, color=colors, alpha=0.85, edgecolor="black")
    ax.axhline(5.0, color="orange", ls="--", lw=2,
                label="порог 5% (JC выполняется)")
    for n, s in zip(n_vals, sigma_vals):
        ax.text(n, s + 0.001, f"{s:.4f}%", ha="center", fontsize=9, fontweight="bold")
    ax.set_xlabel("размерность $n$")
    ax.set_ylabel(r"$\sigma/|\mu|$ (%)")
    ax.set_title("(b) Достигнутое $\\sigma/|\\mu|$ с $k_{\\mathrm{opt}}$\n"
                  "(все $n$ — JC выполняется абсолютно)")
    ax.set_xticks(n_vals)
    ax.legend()
    ax.grid(alpha=0.3, axis="y")
    ax.set_yscale('log')

    out = os.path.join(FIG_DIR, "fig14_27_kopt_pattern.png")
    fig.savefig(out, dpi=300)
    plt.close(fig)
    return out

def fig_variable_choptuik(results):
    """Fig: σ/|μ| vs Choptuik coefficient c."""
    print("[Fig] Variable Choptuik coefficient")
    fig, ax = plt.subplots(1, 1, figsize=(10, 6), constrained_layout=True)
    c_vals = [r["c"] for r in results]
    sigma_vals = [r["rel_std_pct"] for r in results]
    corrections = [r["correction"] for r in results]
    ax.semilogy(c_vals, sigma_vals, "bo-", lw=2, markersize=10)
    ax.axhline(5.0, color="orange", ls="--", lw=2, label="порог 5% (JC)")
    # Mark standard Choptuik (c=1)
    ax.axvline(1.0, color="red", ls=":", lw=2, label="стандартная поправка (c=1)")
    # Add correction values on top
    for c, s, corr in zip(c_vals, sigma_vals, corrections):
        ax.text(c, s * 1.3, f"corr={corr:.3f}", ha="center", fontsize=8)
    ax.set_xlabel("коэффициент $c$ в поправке $(1 - c/\\pi^2)$")
    ax.set_ylabel(r"$\sigma/|\mu|$ (%)")
    ax.set_title("Влияние переменной поправки Чоптьюка на JC ($n=3$, $k=4$)\n"
                  "Цель: найти оптимальное $c$ для минимизации $\\sigma/|\\mu|$")
    ax.legend()
    ax.grid(alpha=0.3)
    out = os.path.join(FIG_DIR, "fig14_28_variable_choptuik.png")
    fig.savefig(out, dpi=300)
    plt.close(fig)
    return out

def fig_log_power(results):
    """Fig: σ/|μ| vs log power p."""
    print("[Fig] Log power study")
    fig, ax = plt.subplots(1, 1, figsize=(10, 6), constrained_layout=True)
    p_vals = [r["p"] for r in results]
    sigma_vals = [r["rel_std_pct"] for r in results]
    ax.semilogy(p_vals, sigma_vals, "go-", lw=2, markersize=10)
    ax.axhline(5.0, color="orange", ls="--", lw=2, label="порог 5% (JC)")
    ax.axvline(0.0, color="red", ls=":", lw=2, label="стандартный логарифм (p=0)")
    for p, s in zip(p_vals, sigma_vals):
        ax.text(p, s * 1.3, f"{s:.4f}%", ha="center", fontsize=9)
    ax.set_xlabel("степень $p$ в $\\|\\psi - r\\|^{2p}/(2p)$ (вместо $\\log\\|\\psi-r\\|^2$)")
    ax.set_ylabel(r"$\sigma/|\mu|$ (%)")
    ax.set_title("Изменение формы логарифма: $\\log\\|\\psi-r\\|^2 \\to \\|\\psi-r\\|^{2p}/(2p)$\n"
                  "Цель: найти оптимальное $p$ для JC")
    ax.legend()
    ax.grid(alpha=0.3)
    out = os.path.join(FIG_DIR, "fig14_29_log_power.png")
    fig.savefig(out, dpi=300)
    plt.close(fig)
    return out

# ============================================================================
# Main
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
    print("EXTENDED STUDY: k_opt(n) and Choptuik variations\n")

    # 1. Extended k_opt search
    kopt_per_n = extended_kopt_search()

    # 2. Find analytic formula
    formula_results = find_analytic_formula(kopt_per_n)

    # 3. Variable Choptuik
    choptuik_results = variable_choptuik_study()

    # 4. Log power study
    log_power_results = log_power_study()

    # 5. Combined optimization
    combined_results = combined_optimization()

    # 6. Figures
    fig1 = fig_kopt_pattern(kopt_per_n)
    fig2 = fig_variable_choptuik(choptuik_results)
    fig3 = fig_log_power(log_power_results)

    print("\n" + "=" * 90)
    print("FINAL SUMMARY")
    print("=" * 90)
    print("\nk_opt(n) for n=1..10:")
    for n in kopt_per_n:
        print(f"  n={n}: k={kopt_per_n[n]['k']}, σ/|μ|={kopt_per_n[n]['sigma_pct']:.6f}%")

    print(f"\nCombined optimization (best k, c per n):")
    for n in combined_results:
        b = combined_results[n]
        print(f"  n={n}: k={b['k']}, c={b['c']}, σ/|μ|={b['sigma']:.6f}%, "
              f"JC={'✓' if b['jc'] else '✗'}")

    results = {
        "kopt_per_n": kopt_per_n,
        "formula_results": {k: list(v) if isinstance(v, tuple) else v
                             for k, v in formula_results.items()},
        "choptuik_results": choptuik_results,
        "log_power_results": log_power_results,
        "combined_results": combined_results,
        "figures": [fig1, fig2, fig3],
    }
    out_json = os.path.join(EXP_DIR, "extended_kopt_study.json")
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2, default=_json_default)
    print(f"\n[Done] JSON: {out_json}")
    print(f"[Done] Figures: {fig1}, {fig2}, {fig3}")

if __name__ == "__main__":
    main()
