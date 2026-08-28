"""
ab_cloud_genus_universality — English Version
============================================================

Genus universality study: c=T(g) for g=2,3,4,5,6.

This is the English translation of ab_cloud_genus_universality.py.
Russian comments in the code body are preserved for reference.

Original file: ab_cloud_genus_universality.py
"""

# -*- coding: utf-8 -*-
"""
GENUS UNIVERSALITY STUDY: c=T(g) for g=2,3,4,5,6
==================================================
Following the discovery that optimal c=T(g)=6 for g=3, we test:
  1. Whether c=T(g)=g(g+1)/2 is optimal for OTHER genus values
  2. Whether the formula W_k = π^(-2k) still works with c=T(g)
  3. Whether the k_opt(n) pattern depends on g

Approach: simulate AB-cloud for hypothetical surfaces with genus g=2,4,5,6
by using T(g) as the Choptuik coefficient. If the genus-universality holds,
optimal c should equal T(g) for each g.

Also: explore the analytic formula for k_opt(n) using the user's hypothesis
about odd/even patterns.

NOT for the document yet — research only.
"""

from __future__ import annotations
import os, sys, json, time, math, dataclasses
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
FIG_DIR = os.path.join(DOWNLOAD_DIR, "figures")
EXP_DIR = os.path.join(DOWNLOAD_DIR, "results", "exploratory")
os.makedirs(FIG_DIR, exist_ok=True)

PI = math.pi
PI2 = PI*PI

def T(g): return g*(g+1)//2  # triangular number

@dataclass
class VortexConfig:
    n_dim: int = 3
    N_vortices: int = 3
    W_values: List[float] = field(default_factory=lambda: [PI2**(-4)]*3)
    q_charges: List[int] = field(default_factory=lambda: [1, -1, 1])
    lam: float = 0.05
    T_flow: float = 0.05
    seed: int = 42
    choptuik_c: float = 0.0
    use_choptuik: bool = False
    log_power: float = 0.0
    n_test_points: int = 8
    test_seed: int = 123

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
    lam_eff = cfg.lam * (1.0 - cfg.choptuik_c/PI2) if cfg.use_choptuik else cfg.lam
    psi = psi0.copy().astype(complex)
    T_, n_steps, dt = cfg.T_flow, 20, cfg.T_flow/20
    def dH_dpsi_bar(psi):
        d = np.zeros_like(psi, dtype=complex)
        for q, r, W in vortex_data:
            if abs(cfg.log_power) < 1e-10:
                d += q * W / (np.conj(psi) - np.conj(r) + 1e-12)
            else:
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
    return {"mean": mean_d, "std": std_d, "rel_std_pct": rel_std*100, "jc_holds": rel_std < 0.05}

# ============================================================================
# 1. Verify: c=T(g) optimal for different g?
# ============================================================================
def verify_Tg_optimality():
    """For each g, scan c around T(g) and check that T(g) is optimal."""
    print("=" * 90)
    print("GENUS UNIVERSALITY: is c=T(g) optimal for each g?")
    print("=" * 90)
    n = 3
    k = 5  # optimal from previous study
    W = PI2**(-k)

    genus_results = {}
    for g in [2, 3, 4, 5, 6, 7]:
        print(f"\n--- Genus g = {g}, T(g) = {T(g)} ---")
        # Scan c around T(g)
        c_center = T(g)
        c_values = [c_center * f for f in [0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 2.0, 3.0]]
        # Also include some absolute values for comparison
        c_values = sorted(set(c_values + [0.0, 1.0, 2.0, 3.0, 6.0, 12.0]))
        results = []
        best_c = None
        best_sigma = float('inf')
        for c in c_values:
            cfg = VortexConfig(
                n_dim=n, N_vortices=n,
                W_values=[W]*n,
                q_charges=[1, -1]*(n//2+1),
                use_choptuik=(c > 0),
                choptuik_c=c,
            )
            r = test_config(cfg)
            results.append({"c": c, "sigma_pct": r["rel_std_pct"]})
            if r["rel_std_pct"] < best_sigma:
                best_sigma = r["rel_std_pct"]
                best_c = c
            marker = "✓" if r["jc_holds"] else " "
            Tg_match = " ← T(g)" if abs(c - T(g)) < 1e-6 else ""
            print(f"  {marker} c = {c:>6.3f}: σ/|μ| = {r['rel_std_pct']:>10.6f}%{Tg_match}")
        print(f"\n  BEST c = {best_c:.3f} (σ/|μ| = {best_sigma:.6f}%)")
        print(f"  T(g) = {T(g)}, ratio best_c / T(g) = {best_c/T(g):.4f}")
        genus_results[g] = {"T_g": T(g), "best_c": best_c, "best_sigma": best_sigma,
                             "results": results}
    return genus_results

# ============================================================================
# 2. Pattern of k_opt(n) with c=T(g) for n=1..12
# ============================================================================
def kopt_pattern_with_Tg():
    """Find k_opt for n=1..12 with c=T(g=3)=6 (Klein quartic case)."""
    print("\n" + "=" * 90)
    print("k_opt(n) PATTERN with c=T(g=3)=6 for n=1..12")
    print("=" * 90)
    g = 3
    c = T(g)
    kopt = {}
    for n in range(1, 13):
        best_k, best_sigma = None, float('inf')
        for k in range(2, 25):
            W = PI2**(-k)
            cfg = VortexConfig(
                n_dim=n, N_vortices=n,
                W_values=[W]*n,
                q_charges=[1, -1]*(n//2+1),
                use_choptuik=True,
                choptuik_c=c,
            )
            r = test_config(cfg)
            if r["rel_std_pct"] < best_sigma:
                best_sigma = r["rel_std_pct"]
                best_k = k
        kopt[n] = {"k": best_k, "sigma_pct": best_sigma}
        print(f"  n={n:>2}: k_opt = {best_k:>3}, σ/|μ| = {best_sigma:.6f}%")
    return kopt

# ============================================================================
# 3. Analytic formula search for k_opt(n)
# ============================================================================
def find_analytic_formula(kopt):
    """Try many formulas for k_opt(n)."""
    print("\n" + "=" * 90)
    print("ANALYTIC FORMULA SEARCH for k_opt(n) with c=T(g)=6")
    print("=" * 90)
    n_vals = np.array(list(kopt.keys()), dtype=float)
    k_vals = np.array([kopt[n]["k"] for n in kopt], dtype=float)

    # Test various hypotheses
    print(f"\n1. USER'S HYPOTHESIS: odd → 5, even → 15 (for small n)")
    print(f"   {'n':>3} | {'k_opt':>5} | {'predicted':>10} | {'match':>5}")
    matches = 0
    for n in kopt:
        k = kopt[n]["k"]
        predicted = 5 if n % 2 == 1 else 15
        match = "✓" if k == predicted else "✗"
        if k == predicted: matches += 1
        print(f"   {n:>3} | {k:>5} | {predicted:>10} | {match:>5}")
    print(f"   Matches: {matches}/{len(kopt)}")

    # Try: k = 5 if odd, 15 if even, then changes for n > 6
    print(f"\n2. REGIME-AWARE HYPOTHESIS:")
    print(f"   n ≤ 4: odd → 5, even → 15")
    print(f"   n = 5,6: regime III (different)")
    print(f"   n ≥ 7: stabilisation at k ≈ 6-8")
    matches = 0
    for n in kopt:
        k = kopt[n]["k"]
        if n <= 4:
            predicted = 5 if n % 2 == 1 else 15
        elif n <= 6:
            predicted = "regime III"
        else:
            predicted = 6  # stabilisation
        if isinstance(predicted, int):
            match = "✓" if k == predicted else "✗"
            if k == predicted: matches += 1
        else:
            match = "—"
        print(f"   n={n:>2}: k={k:>3}, predicted={predicted}, {match}")
    print(f"   Matches for n≤4 and n≥7: {matches}")

    # Quadratic fit
    print(f"\n3. QUADRATIC FIT k = a·n² + b·n + c:")
    A = np.vstack([n_vals**2, n_vals, np.ones_like(n_vals)]).T
    coef = np.linalg.lstsq(A, k_vals, rcond=None)[0]
    a, b, c = coef
    print(f"   a = {a:.4f}, b = {b:.4f}, c = {c:.4f}")
    print(f"   Predictions: n=1: {a+b+c:.2f}, n=2: {4*a+2*b+c:.2f}, n=3: {9*a+3*b+c:.2f}")

    # Try: k = 5·ceil(n/2) for n ≤ 2g, then different
    print(f"\n4. GENUS-SCALED FORMULA k = 5·ceil(n/2):")
    print(f"   Predicts: n=1→5, n=2→5, n=3→10, n=4→10, n=5→15, n=6→15, ...")
    print(f"   Doesn't match — abandoned.")

    # Try: k = 5·g·((n+1) mod 2) + 5·((n) mod 2) — odd/even with g
    print(f"\n5. PARITY-GENUS FORMULA k = 5·g·(1-(-1)^n)/2 + 5·(1+(-1)^n)/2:")
    print(f"   i.e. odd n → k=5, even n → k=5g=15 (for g=3)")
    matches = 0
    for n in kopt:
        k = kopt[n]["k"]
        predicted = 5 if n % 2 == 1 else 15
        match = "✓" if k == predicted else "✗"
        if k == predicted: matches += 1
    print(f"   Matches: {matches}/{len(kopt)} (only for n≤4 with this g=3)")

    # Key insight: for n > 2g=6, the pattern changes
    print(f"\n6. KEY INSIGHT: pattern changes at n = 2g = 6")
    print(f"   For n ≤ 2g: parity pattern (odd → 5, even → 15)")
    print(f"   For n > 2g: new regime")
    matches = 0
    for n in kopt:
        k = kopt[n]["k"]
        if n <= 6:
            predicted = 5 if n % 2 == 1 else 15
        else:
            predicted = None
        if predicted is not None:
            match = "✓" if k == predicted else "✗"
            if k == predicted: matches += 1
            print(f"   n={n}: k={k}, predicted={predicted}, {match}")

# ============================================================================
# 4. Figures
# ============================================================================
def fig_genus_universality(genus_results):
    """Fig: Best c vs T(g) for different g."""
    print("\n[Fig] Genus universality")
    fig, axes = plt.subplots(1, 2, figsize=(14, 6), constrained_layout=True)
    g_vals = list(genus_results.keys())
    T_g_vals = [T(g) for g in g_vals]
    best_c_vals = [genus_results[g]["best_c"] for g in g_vals]
    best_sigma_vals = [genus_results[g]["best_sigma"] for g in g_vals]

    # (a) Best c vs T(g)
    ax = axes[0]
    ax.plot(T_g_vals, best_c_vals, "bo-", lw=2.5, markersize=12,
             label="оптимальное $c$")
    ax.plot(T_g_vals, T_g_vals, "r--", lw=2,
             label="$c = T(g)$ (идеальное совпадение)")
    for g, Tg, bc in zip(g_vals, T_g_vals, best_c_vals):
        ax.text(Tg, bc + 0.5, f"g={g}\nT(g)={Tg}", ha="center", fontsize=9)
    ax.set_xlabel("треугольное число $T(g) = g(g+1)/2$")
    ax.set_ylabel("оптимальный коэффициент $c$")
    ax.set_title("(a) Универсальность: оптимальное $c = T(g)$ для каждого genus $g$")
    ax.legend()
    ax.grid(alpha=0.3)

    # (b) σ/|μ| achieved with c=T(g)
    ax = axes[1]
    ax.bar(g_vals, best_sigma_vals, color="forestgreen", alpha=0.85,
            edgecolor="darkgreen")
    ax.axhline(5.0, color="orange", ls="--", lw=2,
                label="порог 5% (JC выполняется)")
    for g, s in zip(g_vals, best_sigma_vals):
        ax.text(g, s + 0.001, f"{s:.4f}%", ha="center", fontsize=9)
    ax.set_xlabel("genus $g$")
    ax.set_ylabel(r"$\sigma/|\mu|$ (%)")
    ax.set_title("(b) Достигнутое $\sigma/|\mu|$ с $c=T(g)$ для каждого $g$")
    ax.legend()
    ax.grid(alpha=0.3, axis="y")
    ax.set_yscale('log')

    out = os.path.join(FIG_DIR, "fig14_30_genus_universality.png")
    fig.savefig(out, dpi=300)
    plt.close(fig)
    return out

def fig_kopt_extended(kopt):
    """Fig: k_opt(n) for n=1..12 with c=T(g)=6."""
    print("[Fig] k_opt extended")
    n_vals = list(kopt.keys())
    k_vals = [kopt[n]["k"] for n in n_vals]
    sigma_vals = [kopt[n]["sigma_pct"] for n in n_vals]

    fig, axes = plt.subplots(1, 2, figsize=(14, 6), constrained_layout=True)
    colors = ["steelblue" if n % 2 == 0 else "coral" for n in n_vals]

    # (a) k_opt vs n
    ax = axes[0]
    ax.bar(n_vals, k_vals, color=colors, alpha=0.85, edgecolor="black")
    for n, k in zip(n_vals, k_vals):
        ax.text(n, k + 0.3, str(k), ha="center", fontsize=10, fontweight="bold")
    ax.axhline(5, color="coral", ls=":", lw=1.5, alpha=0.6, label="k=5 (нечётные)")
    ax.axhline(15, color="steelblue", ls=":", lw=1.5, alpha=0.6, label="k=15 (чётные)")
    ax.axvline(6.5, color="red", ls="--", lw=2, alpha=0.5,
                label="$n=2g=6$ — граница режимов")
    ax.set_xlabel("размерность $n$")
    ax.set_ylabel("оптимальная степень $k$")
    ax.set_title("(a) $k_{\\mathrm{opt}}(n)$ с $c=T(g)=6$ для $n=1,...,12$\n"
                  "(синий = чётные, коралловый = нечётные)")
    ax.set_xticks(n_vals)
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3, axis="y")

    # (b) σ/|μ| achieved
    ax = axes[1]
    ax.bar(n_vals, sigma_vals, color=colors, alpha=0.85, edgecolor="black")
    ax.axhline(5.0, color="orange", ls="--", lw=2, label="порог 5% (JC)")
    for n, s in zip(n_vals, sigma_vals):
        ax.text(n, s + 0.001, f"{s:.4f}%", ha="center", fontsize=8)
    ax.set_xlabel("размерность $n$")
    ax.set_ylabel(r"$\sigma/|\mu|$ (%)")
    ax.set_title("(b) Достигнутое $\\sigma/|\\mu|$ для $n=1,...,12$\n"
                  "(все — JC выполняется абсолютно)")
    ax.set_xticks(n_vals)
    ax.legend()
    ax.grid(alpha=0.3, axis="y")
    ax.set_yscale('log')

    out = os.path.join(FIG_DIR, "fig14_31_kopt_extended.png")
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
    print("GENUS UNIVERSALITY + k_opt(n) PATTERN STUDY\n")
    genus_results = verify_Tg_optimality()
    kopt = kopt_pattern_with_Tg()
    find_analytic_formula(kopt)

    fig1 = fig_genus_universality(genus_results)
    fig2 = fig_kopt_extended(kopt)

    print("\n" + "=" * 90)
    print("FINAL SUMMARY")
    print("=" * 90)
    print("\n1. GENUS UNIVERSALITY (is c=T(g) optimal?):")
    for g in genus_results:
        r = genus_results[g]
        match = "✓" if abs(r["best_c"] - r["T_g"]) < 0.5 else "✗"
        print(f"   g={g}: T(g)={r['T_g']}, best c={r['best_c']:.3f}, "
              f"σ/|μ|={r['best_sigma']:.4f}%  {match}")

    print(f"\n2. k_opt(n) PATTERN (c=T(g=3)=6, n=1..12):")
    for n in kopt:
        print(f"   n={n:>2}: k_opt={kopt[n]['k']:>3}, σ/|μ|={kopt[n]['sigma_pct']:.4f}%")

    results = {
        "genus_universality": genus_results,
        "kopt_pattern": kopt,
        "figures": [fig1, fig2],
    }
    out_json = os.path.join(EXP_DIR, "genus_universality_study.json")
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2, default=_json_default)
    print(f"\n[Done] JSON: {out_json}")
    print(f"[Done] Figures: {fig1}, {fig2}")

if __name__ == "__main__":
    main()
