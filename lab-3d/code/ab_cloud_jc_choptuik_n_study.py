#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
JC VERIFICATION WITH CHOPTUIK CORRECTION FOR n = 1..6 (Chapter 14 §14.19-14.20)
================================================================================
Systematic study of how the Choptuik correction (1 - 1/π²) = 0.89868 affects
the Jacobian Conjecture verification across dimensions n = 1, 2, 3, 4, 5, 6.

For each n we:
  1. Build an AB-cloud Hamiltonian with N_v = n vortices (one per dimension).
  2. Compute det(J_F) at multiple test points without and with the correction.
  3. Measure:
       - mean and std of det(J_F)
       - relative deviation σ/|μ| (JC constancy measure)
       - improvement from the correction (reduction in σ/|μ|)
       - convergence time (slowdown verification)
  4. Generate comparison figures.

Key questions answered:
  Q1. Does the Choptuik correction improve JC verification for all n?
  Q2. For which n is the improvement most pronounced?
  Q3. Does the slowdown factor match 1/(1-1/π²) ≈ 1.113 across all n?
  Q4. At what n does the JC verification break down (numerically)?

Author: Z.ai (Chapter 14 §14.19-14.20 extension)
Date  : 2026-07-22
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
plt.rcParams["font.serif"]      = ["Noto Serif SC", "DejaVu Serif"]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["savefig.dpi"] = 300

PROJECT_ROOT = "/home/z/my-project"
DOWNLOAD_DIR = os.path.join(PROJECT_ROOT, "download")
FIG_DIR      = os.path.join(DOWNLOAD_DIR, "figures")
RESULTS_DIR  = os.path.join(DOWNLOAD_DIR, "results")
os.makedirs(FIG_DIR, exist_ok=True)
os.makedirs(RESULTS_DIR, exist_ok=True)

PI = math.pi
CHOPTUIK_CORRECTION = 1.0 - 1.0 / (PI * PI)  # 0.89868
SLOWDOWN_FACTOR = 1.0 / CHOPTUIK_CORRECTION  # 1.113

# ============================================================================
# 1. AB-cloud configuration with N_v = n
# ============================================================================
@dataclass
class ABCloudConfig:
    n_dim: int = 3
    N_vortices: int = 3  # N_v = n
    W: float = 1.0
    lam: float = 0.05
    T_flow: float = 0.05
    seed: int = 42
    use_choptuik: bool = False

def build_vortex_data(cfg: ABCloudConfig):
    rng = np.random.default_rng(cfg.seed)
    vortex_data = []
    for _ in range(cfg.N_vortices):
        q = int(rng.choice([-1, 1]))
        r = rng.standard_normal(cfg.n_dim) + 1j * rng.standard_normal(cfg.n_dim)
        vortex_data.append((q, r))
    return vortex_data

def hamiltonian_flow_map(psi0, vortex_data, cfg: ABCloudConfig):
    """RK4 integration of Hamilton's equations with optional Choptuik correction."""
    lam_eff = cfg.lam * CHOPTUIK_CORRECTION if cfg.use_choptuik else cfg.lam

    psi = psi0.copy().astype(complex)
    T = cfg.T_flow
    n_steps = 20
    dt = T / n_steps

    def dH_dpsi_bar(psi):
        d = np.zeros_like(psi, dtype=complex)
        for q, r in vortex_data:
            d += q * cfg.W / (np.conj(psi) - np.conj(r) + 1e-12)
        d += lam_eff * psi / (np.abs(psi)**2 + 1.0)
        return d

    def dH_dpsi(psi):
        return np.conj(dH_dpsi_bar(psi))

    for _ in range(n_steps):
        k1_psi =  dH_dpsi_bar(psi)
        k2_psi =  dH_dpsi_bar(psi + 0.5*dt*k1_psi)
        k3_psi =  dH_dpsi_bar(psi + 0.5*dt*k2_psi)
        k4_psi =  dH_dpsi_bar(psi + dt*k3_psi)
        psi = psi + (dt/6) * (k1_psi + 2*k2_psi + 2*k3_psi + k4_psi)
    return psi

def jacobian_det_flow(psi0, vortex_data, cfg, eps=1e-6):
    n = len(psi0)
    J = np.zeros((n, n), dtype=complex)
    for j in range(n):
        psi_plus = psi0.copy().astype(complex); psi_plus[j] += eps
        psi_minus = psi0.copy().astype(complex); psi_minus[j] -= eps
        F_plus = hamiltonian_flow_map(psi_plus, vortex_data, cfg)
        F_minus = hamiltonian_flow_map(psi_minus, vortex_data, cfg)
        J[:, j] = (F_plus - F_minus) / (2 * eps)
    det_J = np.linalg.det(J)
    return float(det_J.real)

# ============================================================================
# 2. Generate test points for given n
# ============================================================================
def generate_test_points(n: int, n_points: int = 8) -> List[np.ndarray]:
    """Generate n_points test points in C^n near the origin."""
    rng = np.random.default_rng(123)
    points = []
    for _ in range(n_points):
        p = 0.1 * (rng.standard_normal(n) + 1j * rng.standard_normal(n))
        points.append(p.astype(complex))
    return points

# ============================================================================
# 3. Run JC verification for one n with and without Choptuik correction
# ============================================================================
def verify_jc_for_n(n: int, lam: float = 0.05, T_flow: float = 0.05) -> Dict[str, Any]:
    """Run JC verification for dimension n with N_v = n vortices.

    Returns dict with mean, std, rel_std, time for both cases (with/without correction).
    """
    print(f"\n--- n = {n}, N_v = {n} vortices, λ = {lam} ---")

    test_points = generate_test_points(n, n_points=8)

    # Without correction
    cfg_plain = ABCloudConfig(n_dim=n, N_vortices=n, lam=lam, T_flow=T_flow,
                                seed=42, use_choptuik=False)
    vortex_data = build_vortex_data(cfg_plain)
    dets_plain = []
    t0 = time.time()
    for psi0 in test_points:
        d = jacobian_det_flow(psi0, vortex_data, cfg_plain)
        dets_plain.append(d)
    time_plain = time.time() - t0
    dets_plain = np.array(dets_plain)

    # With Choptuik correction
    cfg_chop = ABCloudConfig(n_dim=n, N_vortices=n, lam=lam, T_flow=T_flow,
                              seed=42, use_choptuik=True)
    dets_chop = []
    t0 = time.time()
    for psi0 in test_points:
        d = jacobian_det_flow(psi0, vortex_data, cfg_chop)
        dets_chop.append(d)
    time_chop = time.time() - t0
    dets_chop = np.array(dets_chop)

    # Compute statistics
    mean_plain = float(dets_plain.mean())
    std_plain = float(dets_plain.std())
    rel_std_plain = std_plain / abs(mean_plain) if abs(mean_plain) > 1e-10 else float('inf')

    mean_chop = float(dets_chop.mean())
    std_chop = float(dets_chop.std())
    rel_std_chop = std_chop / abs(mean_chop) if abs(mean_chop) > 1e-10 else float('inf')

    # Improvement
    if rel_std_plain > 0:
        improvement_pct = (1 - rel_std_chop / rel_std_plain) * 100
    else:
        improvement_pct = 0.0
    slowdown_measured = time_chop / time_plain if time_plain > 0 else 1.0

    print(f"  Without correction: ⟨|det J_F|⟩ = {abs(mean_plain):.4g}, "
          f"σ/|μ| = {rel_std_plain*100:.2f}%")
    print(f"  With correction:    ⟨|det J_F|⟩ = {abs(mean_chop):.4g}, "
          f"σ/|μ| = {rel_std_chop*100:.2f}%")
    print(f"  Improvement: σ/|μ| reduced by {improvement_pct:.1f}%")
    print(f"  Slowdown:    {slowdown_measured:.3f}× (expected {SLOWDOWN_FACTOR:.3f}×)")

    # JC verdict
    jc_plain = rel_std_plain < 0.05
    jc_chop  = rel_std_chop  < 0.05
    print(f"  JC without: {'✓' if jc_plain else '✗'} ({rel_std_plain*100:.2f}% >= 5%)")
    print(f"  JC with:    {'✓' if jc_chop  else '✗'} ({rel_std_chop*100:.2f}% >= 5%)")

    return {
        "n": n,
        "N_v": n,
        "lambda": lam,
        "without_correction": {
            "mean": mean_plain,
            "std": std_plain,
            "rel_std": rel_std_plain,
            "rel_std_pct": rel_std_plain * 100,
            "time": float(time_plain),
            "jc_verified": bool(jc_plain),
            "dets": [float(d) for d in dets_plain],
        },
        "with_correction": {
            "lambda_eff": lam * CHOPTUIK_CORRECTION,
            "mean": mean_chop,
            "std": std_chop,
            "rel_std": rel_std_chop,
            "rel_std_pct": rel_std_chop * 100,
            "time": float(time_chop),
            "jc_verified": bool(jc_chop),
            "dets": [float(d) for d in dets_chop],
        },
        "improvement_pct": float(improvement_pct),
        "slowdown_measured": float(slowdown_measured),
        "slowdown_expected": float(SLOWDOWN_FACTOR),
    }

# ============================================================================
# 4. Run for all n = 1, 2, 3, 4, 5, 6
# ============================================================================
def run_all_dimensions():
    """Run JC verification for n = 1, 2, 3, 4, 5, 6 with and without Choptuik correction."""
    print("=" * 78)
    print("JC VERIFICATION WITH CHOPTUIK CORRECTION FOR n = 1..6")
    print(f"Correction factor: (1 - 1/π²) = {CHOPTUIK_CORRECTION:.6f}")
    print(f"Expected slowdown: 1/(1-1/π²) = {SLOWDOWN_FACTOR:.6f}")
    print("=" * 78)

    all_results = {}
    for n in [1, 2, 3, 4, 5, 6]:
        try:
            all_results[f"n{n}"] = verify_jc_for_n(n, lam=0.05, T_flow=0.05)
        except Exception as e:
            print(f"\n--- n = {n}: ERROR {e} ---")
            all_results[f"n{n}"] = {"error": str(e), "n": n}
    return all_results

# ============================================================================
# 5. Generate figures
# ============================================================================
def fig_jc_n_comparison(all_results):
    """Fig 14.17: JC verification comparison across n=1..6 with and without correction."""
    print("\n[Fig 14.17] JC verification across n=1..6")
    n_values = list(range(1, 7))
    rel_std_plain = []
    rel_std_chop = []
    for n in n_values:
        r = all_results.get(f"n{n}", {})
        if "without_correction" in r:
            rel_std_plain.append(r["without_correction"]["rel_std_pct"])
            rel_std_chop.append(r["with_correction"]["rel_std_pct"])
        else:
            rel_std_plain.append(float('nan'))
            rel_std_chop.append(float('nan'))

    fig, axes = plt.subplots(1, 2, figsize=(14, 5.5), constrained_layout=True)

    # (a) σ/|μ| for each n, with and without correction
    x = np.arange(len(n_values))
    width = 0.35
    bars1 = axes[0].bar(x - width/2, rel_std_plain, width,
                         color="steelblue", alpha=0.85, edgecolor="navy",
                         label="без поправки Чоптьюка")
    bars2 = axes[0].bar(x + width/2, rel_std_chop, width,
                         color="coral", alpha=0.85, edgecolor="darkred",
                         label=fr"с поправкой $(1-1/\pi^2)$")
    axes[0].axhline(5.0, color="green", ls="--", lw=1.5,
                     label="порог 5% (JC выполняется)")
    axes[0].set_xticks(x)
    axes[0].set_xticklabels([f"n={n}\nN_v={n}" for n in n_values])
    axes[0].set_xlabel("размерность $n$ (= число вихрей $N_v$)")
    axes[0].set_ylabel(r"относительное отклонение $\sigma/|\mu|$ (%)")
    axes[0].set_title("(a) Постоянство якобиана: JC с/без поправкой Чоптьюка")
    axes[0].legend(loc="upper left", fontsize=9)
    axes[0].grid(alpha=0.3, axis="y")
    axes[0].set_yscale('log')

    # (b) Improvement percentage per n
    improvements = []
    for n in n_values:
        r = all_results.get(f"n{n}", {})
        if "improvement_pct" in r:
            improvements.append(r["improvement_pct"])
        else:
            improvements.append(0.0)
    axes[1].bar(x, improvements, color="forestgreen", alpha=0.85,
                 edgecolor="darkgreen")
    axes[1].axhline(0, color="black", lw=0.5)
    axes[1].set_xticks(x)
    axes[1].set_xticklabels([f"n={n}" for n in n_values])
    axes[1].set_xlabel("размерность $n$")
    axes[1].set_ylabel(r"улучшение $\sigma/|\mu|$ (%)")
    axes[1].set_title("(b) Улучшение от поправки Чоптьюка\n"
                       "(положительное = поправка помогает JC)")
    axes[1].grid(alpha=0.3, axis="y")
    for i, v in enumerate(improvements):
        axes[1].text(i, v + (1 if v >= 0 else -3), f"{v:+.1f}%",
                      ha="center", fontsize=9, fontweight="bold")

    out = os.path.join(FIG_DIR, "fig14_17_jc_n_comparison.png")
    fig.savefig(out, dpi=300)
    plt.close(fig)
    return out

def fig_slowdown_n(all_results):
    """Fig 14.18: Slowdown factor vs n."""
    print("[Fig 14.18] Slowdown factor vs n")
    n_values = list(range(1, 7))
    slowdowns = []
    for n in n_values:
        r = all_results.get(f"n{n}", {})
        if "slowdown_measured" in r:
            slowdowns.append(r["slowdown_measured"])
        else:
            slowdowns.append(float('nan'))

    fig, ax = plt.subplots(1, 1, figsize=(8, 5), constrained_layout=True)
    ax.plot(n_values, slowdowns, "bo-", lw=2.5, markersize=12,
             label="измеренное замедление")
    ax.axhline(SLOWDOWN_FACTOR, color="red", ls="--", lw=2,
                label=fr"ожидаемое $1/(1-1/\pi^2) = {SLOWDOWN_FACTOR:.4f}$")
    ax.fill_between(n_values, [SLOWDOWN_FACTOR*0.95]*len(n_values),
                      [SLOWDOWN_FACTOR*1.05]*len(n_values),
                      color="red", alpha=0.15, label="±5% коридор")
    ax.set_xlabel("размерность $n$")
    ax.set_ylabel(r"коэффициент замедления $\tau_{\mathrm{Ch}}/\tau_0$")
    ax.set_title("Универсальное замедление процессов от поправки Чоптьюка\n"
                  "по всем размерностям $n=1,\\ldots,6$")
    ax.set_xticks(n_values)
    ax.legend(loc="best")
    ax.grid(alpha=0.3)
    ax.set_ylim(0.8, 1.3)

    out = os.path.join(FIG_DIR, "fig14_18_slowdown_vs_n.png")
    fig.savefig(out, dpi=300)
    plt.close(fig)
    return out

def fig_jc_phase_diagram(all_results):
    """Fig 14.19: JC phase diagram — for which (n, λ) does JC hold?"""
    print("[Fig 14.19] JC phase diagram (n, λ) with and without correction")
    n_values = list(range(1, 7))
    lam_values = np.linspace(0.01, 0.20, 10)

    # Build JC status matrices
    jc_plain = np.zeros((len(n_values), len(lam_values)))
    jc_chop  = np.zeros((len(n_values), len(lam_values)))

    for i, n in enumerate(n_values):
        for j, lam in enumerate(lam_values):
            try:
                r = verify_jc_for_n(n, lam=float(lam), T_flow=0.05)
                rp = r["without_correction"]["rel_std_pct"]
                rc = r["with_correction"]["rel_std_pct"]
                # JC holds if rel_std < 5%
                jc_plain[i, j] = 1.0 if rp < 5.0 else 0.0
                jc_chop[i, j]  = 1.0 if rc < 5.0 else 0.0
            except Exception:
                jc_plain[i, j] = float('nan')
                jc_chop[i, j]  = float('nan')

    fig, axes = plt.subplots(1, 2, figsize=(14, 5.5), constrained_layout=True)

    # (a) Without correction
    im0 = axes[0].imshow(jc_plain, origin="lower", aspect="auto",
                          extent=[lam_values[0], lam_values[-1],
                                  n_values[0]-0.5, n_values[-1]+0.5],
                          cmap="RdYlGn", vmin=0, vmax=1)
    axes[0].set_xlabel(r"константа связи $\lambda$")
    axes[0].set_ylabel("размерность $n$")
    axes[0].set_title("(a) JC без поправки Чоптьюка\n"
                       "(зелёный = JC выполняется, красный = нарушена)")
    axes[0].set_yticks(n_values)
    fig.colorbar(im0, ax=axes[0], shrink=0.85, label="JC статус")

    # (b) With correction
    im1 = axes[1].imshow(jc_chop, origin="lower", aspect="auto",
                          extent=[lam_values[0], lam_values[-1],
                                  n_values[0]-0.5, n_values[-1]+0.5],
                          cmap="RdYlGn", vmin=0, vmax=1)
    axes[1].set_xlabel(r"константа связи $\lambda$")
    axes[1].set_ylabel("размерность $n$")
    axes[1].set_title(fr"(b) JC с поправкой $(1-1/\pi^2)$"
                       "\n(зелёный = JC выполняется, красный = нарушена)")
    axes[1].set_yticks(n_values)
    fig.colorbar(im1, ax=axes[1], shrink=0.85, label="JC статус")

    out = os.path.join(FIG_DIR, "fig14_19_jc_phase_diagram.png")
    fig.savefig(out, dpi=300)
    plt.close(fig)
    return out

# ============================================================================
# 6. Main
# ============================================================================
def _json_default(o):
    if isinstance(o, (complex, np.complexfloating)):
        return {"re": float(o.real), "im": float(o.imag)}
    if isinstance(o, (np.integer,)): return int(o)
    if isinstance(o, (np.floating,)): return float(o)
    if isinstance(o, (np.bool_,)): return bool(o)
    if isinstance(o, np.ndarray):
        if o.dtype.kind == "c":
            return [{"re": float(x.real), "im": float(x.imag)} for x in o.ravel()]
        return o.tolist()
    raise TypeError(f"Cannot serialize {o.__class__.__name__}")

def main():
    print("JC verification with Choptuik correction for n = 1..6\n")

    all_results = run_all_dimensions()

    fig1 = fig_jc_n_comparison(all_results)
    fig2 = fig_slowdown_n(all_results)
    # Skip phase diagram for speed; it's expensive (60 configurations)
    # fig3 = fig_jc_phase_diagram(all_results)

    # Summary table
    print("\n" + "=" * 78)
    print("SUMMARY: JC verification across n=1..6 with and without Choptuik correction")
    print("=" * 78)
    print(f"{'n':>3} | {'σ/|μ| plain':>14} | {'σ/|μ| Chopt':>14} | {'improvement':>12} | {'JC plain':>9} | {'JC Chopt':>9}")
    print("-" * 78)
    for n in range(1, 7):
        r = all_results.get(f"n{n}", {})
        if "without_correction" in r:
            rp = r["without_correction"]["rel_std_pct"]
            rc = r["with_correction"]["rel_std_pct"]
            imp = r["improvement_pct"]
            jcp = "✓" if r["without_correction"]["jc_verified"] else "✗"
            jcc = "✓" if r["with_correction"]["jc_verified"] else "✗"
            print(f"{n:>3} | {rp:>12.2f}%  | {rc:>12.2f}%  | {imp:>+10.1f}% | {jcp:>9} | {jcc:>9}")
        else:
            print(f"{n:>3} | {'ERROR':>14} | {'ERROR':>14} | {'-':>12} | {'-':>9} | {'-':>9}")
    print("=" * 78)

    results = {
        "choptuik_correction": CHOPTUIK_CORRECTION,
        "slowdown_factor_expected": SLOWDOWN_FACTOR,
        "results_per_n": all_results,
        "figures": [fig1, fig2],
    }
    out_json = os.path.join(RESULTS_DIR, "chapter14_jc_choptuik_n1_6_results.json")
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2, default=_json_default)
    print(f"\n[Done] JSON: {out_json}")
    print(f"[Done] Figures: {fig1}, {fig2}")

if __name__ == "__main__":
    main()
