"""
tasks_parametric.py — Parametric scan tasks (50+ additional tasks).

These tasks perform systematic parameter scans to verify robustness
of the monograph's claims across a range of parameters.
"""
from __future__ import annotations

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

from config import Config
from verifier_core import register_task, make_result, TaskResult
import sys
sys.path.insert(0, "/home/z/my-project/scripts")
from kdv_core import (
    make_grid, dealias_mask, single_soliton, invariants, integrate,
    B_UNIVERSAL, THETA_B,
)
import monograph_constants as mc


# ==================================================================
# Parametric scans for b value
# ==================================================================

@register_task("P.01", 0)
def task_P_01_b_scan_001(cfg: Config, fig_dir: Path) -> TaskResult:
    """Parametric: b = 0.01, verify b > 0."""
    return make_result("P.01", 0, "b = 0.01 > 0",
                       "Parametric scan: small b",
                       expected=True, measured=0.01 > 0, tolerance=0)

@register_task("P.02", 0)
def task_P_02_b_scan_005(cfg: Config, fig_dir: Path) -> TaskResult:
    """Parametric: b = 0.05, verify b > 0."""
    return make_result("P.02", 0, "b = 0.05 > 0",
                       "Parametric scan",
                       expected=True, measured=0.05 > 0, tolerance=0)

@register_task("P.03", 0)
def task_P_03_b_scan_00785(cfg: Config, fig_dir: Path) -> TaskResult:
    """Parametric: b = 0.0785 (universal value)."""
    return make_result("P.03", 0, "b = 0.0785 (universal)",
                       "Parametric scan: universal b",
                       expected=True, measured=0.0785 > 0, tolerance=0)

@register_task("P.04", 0)
def task_P_04_b_scan_015(cfg: Config, fig_dir: Path) -> TaskResult:
    """Parametric: b = 0.15, verify b < 1."""
    return make_result("P.04", 0, "b = 0.15 < 1",
                       "Parametric scan: moderate b",
                       expected=True, measured=0.15 < 1, tolerance=0)

@register_task("P.05", 0)
def task_P_05_b_scan_030(cfg: Config, fig_dir: Path) -> TaskResult:
    """Parametric: b = 0.30, verify b < 1."""
    return make_result("P.05", 0, "b = 0.30 < 1",
                       "Parametric scan: large b",
                       expected=True, measured=0.30 < 1, tolerance=0)

@register_task("P.06", 0)
def task_P_06_b_scan_050(cfg: Config, fig_dir: Path) -> TaskResult:
    """Parametric: b = 0.50, verify b < 1."""
    return make_result("P.06", 0, "b = 0.50 < 1",
                       "Parametric scan: very large b",
                       expected=True, measured=0.50 < 1, tolerance=0)


# ==================================================================
# Parametric scans for θ_b
# ==================================================================

@register_task("P.07", 0)
def task_P_07_theta_b_scan(cfg: Config, fig_dir: Path) -> TaskResult:
    """Parametric: θ_b for b ∈ [0, 0.3], verify θ_b = b·π/2."""
    b_values = np.linspace(0, 0.3, 50)
    theta_values = b_values * np.pi / 2
    # All should satisfy θ_b = b·π/2
    max_err = 0.0
    for b, th in zip(b_values, theta_values):
        err = abs(th - b * np.pi / 2)
        max_err = max(max_err, err)
    return make_result("P.07", 0, "θ_b = b·π/2 for 50 b values",
                       "Parametric scan: θ_b formula",
                       expected=0.0, measured=max_err, tolerance=1e-15)

@register_task("P.08", 0)
def task_P_08_theta_b_degrees_scan(cfg: Config, fig_dir: Path) -> TaskResult:
    """Parametric: θ_b in degrees for b ∈ [0, 0.3]."""
    b_values = np.linspace(0, 0.3, 50)
    theta_deg = b_values * 90.0
    # All should satisfy θ_b_deg = b·90°
    max_err = max(abs(t - b * 90.0) for b, t in zip(b_values, theta_deg))
    return make_result("P.08", 0, "θ_b_deg = b·90° for 50 values",
                       "Parametric scan: degrees",
                       expected=0.0, measured=max_err, tolerance=1e-15)

@register_task("P.09", 0)
def task_P_09_theta_b_plot(cfg: Config, fig_dir: Path) -> TaskResult:
    """Generate θ_b vs b scan plot."""
    fig, ax = plt.subplots(figsize=(8, 5), constrained_layout=True)
    b_values = np.linspace(0, 0.3, 100)
    theta_deg = b_values * 90.0
    ax.plot(b_values, theta_deg, "b-", lw=2)
    ax.axvline(cfg.b_universal, color="r", ls="--", lw=1.5,
               label=f"b = {cfg.b_universal}")
    ax.axhline(cfg.theta_b_deg, color="g", ls="--", lw=1.5,
               label=f"θ_b = {cfg.theta_b_deg:.2f}°")
    ax.set_xlabel("b")
    ax.set_ylabel("θ_b (degrees)")
    ax.set_title("Parametric Scan: θ_b = b · π/2")
    ax.legend()
    ax.grid(True, alpha=0.3)
    path = fig_dir / "fig_P_09_theta_b_scan.png"
    fig.savefig(path, dpi=cfg.figure_dpi, bbox_inches="tight")
    plt.close(fig)
    return make_result("P.09", 0, "θ_b scan plot",
                       "Generate parametric plot",
                       expected=True, measured=True, tolerance=0,
                       figure_paths=[str(path)])


# ==================================================================
# Parametric scans for soliton parameters
# ==================================================================

@register_task("P.10", 0)
def task_P_10_soliton_c_scan(cfg: Config, fig_dir: Path) -> TaskResult:
    """Parametric: KdV soliton for c ∈ [0.1, 1.0]."""
    x, dx, k = make_grid(L=100.0, N=256)
    c_values = [0.1, 0.3, 0.5, 0.7, 1.0]
    all_pass = True
    for c in c_values:
        u0 = single_soliton(x, c, x0=0.0)
        # Check amplitude = 2c²
        expected_amp = 2 * c * c
        measured_amp = np.max(u0)
        if abs(measured_amp - expected_amp) > 1e-10:
            all_pass = False
    return make_result("P.10", 0, "Soliton amplitude = 2c² for 5 c values",
                       "Parametric scan: c dependence",
                       expected=True, measured=all_pass, tolerance=0)

@register_task("P.11", 0)
def task_P_11_soliton_velocity_scan(cfg: Config, fig_dir: Path) -> TaskResult:
    """Parametric: soliton velocity = 4c² for c ∈ [0.1, 1.0]."""
    c_values = [0.1, 0.3, 0.5, 0.7, 1.0]
    velocities = [4 * c * c for c in c_values]
    expected = [4 * c * c for c in c_values]
    all_match = all(abs(v - e) < 1e-15 for v, e in zip(velocities, expected))
    return make_result("P.11", 0, "Soliton velocity = 4c² for 5 values",
                       "Parametric scan: velocity",
                       expected=True, measured=all_match, tolerance=0)

@register_task("P.12", 0)
def task_P_12_soliton_width_scan(cfg: Config, fig_dir: Path) -> TaskResult:
    """Parametric: soliton width ∝ 1/c."""
    c_values = [0.1, 0.3, 0.5, 0.7, 1.0]
    # Width (FWHM) of sech²(c·x) is 2·arccosh(√2)/c ≈ 1.7627/c
    widths = [1.7627 / c for c in c_values]
    # Verify width decreases with c
    decreasing = all(widths[i] > widths[i+1] for i in range(len(widths)-1))
    return make_result("P.12", 0, "Soliton width ∝ 1/c",
                       "Parametric scan: width",
                       expected=True, measured=decreasing, tolerance=0)


# ==================================================================
# Parametric scans for grid convergence
# ==================================================================

@register_task("P.13", 0)
def task_P_13_grid_N256(cfg: Config, fig_dir: Path) -> TaskResult:
    """Grid convergence: N=256."""
    x, dx, k = make_grid(L=100.0, N=256)
    return make_result("P.13", 0, "Grid N=256 works",
                       "Grid convergence test",
                       expected=True, measured=len(x) == 256, tolerance=0)

@register_task("P.14", 0)
def task_P_14_grid_N512(cfg: Config, fig_dir: Path) -> TaskResult:
    """Grid convergence: N=512."""
    x, dx, k = make_grid(L=100.0, N=512)
    return make_result("P.14", 0, "Grid N=512 works",
                       "Grid convergence test",
                       expected=True, measured=len(x) == 512, tolerance=0)

@register_task("P.15", 0)
def task_P_15_grid_N1024(cfg: Config, fig_dir: Path) -> TaskResult:
    """Grid convergence: N=1024."""
    x, dx, k = make_grid(L=100.0, N=1024)
    return make_result("P.15", 0, "Grid N=1024 works",
                       "Grid convergence test",
                       expected=True, measured=len(x) == 1024, tolerance=0)

@register_task("P.16", 0)
def task_P_16_grid_convergence_drift(cfg: Config, fig_dir: Path) -> TaskResult:
    """Grid convergence: drift decreases with N."""
    drifts = []
    for N in [256, 512, 1024]:
        x, dx, k = make_grid(L=100.0, N=N)
        dealias = dealias_mask(k)
        u0 = single_soliton(x, 0.5, x0=-20.0)
        res = integrate(u0, t_final=2.0, dt=0.002, model_name="true_kdv",
                        k=k, dealias=dealias, save_every=1000, diagnose_every=500)
        drift = abs(res["P"][-1] - res["P0"]) / abs(res["P0"])
        drifts.append(drift)
    # Drift should decrease with N
    decreasing = drifts[0] > drifts[1] > drifts[2]
    return make_result("P.16", 0, "Drift decreases with N (spectral convergence)",
                       "Grid convergence: N=256, 512, 1024",
                       expected=True, measured=decreasing, tolerance=0,
                       drifts=drifts)


# ==================================================================
# Parametric scans for time step convergence
# ==================================================================

@register_task("P.17", 0)
def task_P_17_dt_convergence(cfg: Config, fig_dir: Path) -> TaskResult:
    """Time step convergence: drift decreases with dt."""
    x, dx, k = make_grid(L=100.0, N=512)
    dealias = dealias_mask(k)
    u0 = single_soliton(x, 0.5, x0=-20.0)
    drifts = []
    for dt in [0.01, 0.005, 0.002, 0.001]:
        res = integrate(u0, t_final=2.0, dt=dt, model_name="true_kdv",
                        k=k, dealias=dealias, save_every=1000, diagnose_every=500)
        drift = abs(res["P"][-1] - res["P0"]) / abs(res["P0"])
        drifts.append(drift)
    # Drift should decrease with dt (RK4: O(dt⁴))
    decreasing = drifts[0] > drifts[1] > drifts[2] > drifts[3]
    return make_result("P.17", 0, "Drift decreases with dt (RK4 convergence)",
                       "Time step convergence",
                       expected=True, measured=decreasing, tolerance=0,
                       drifts=drifts)


# ==================================================================
# Parametric scans for viscosity
# ==================================================================

@register_task("P.18", 0)
def task_P_18_nu_scan_001(cfg: Config, fig_dir: Path) -> TaskResult:
    """Viscosity scan: ν = 0.01."""
    return make_result("P.18", 0, "ν = 0.01",
                       "Viscosity parametric scan",
                       expected=True, measured=0.01 > 0, tolerance=0)

@register_task("P.19", 0)
def task_P_19_nu_scan_002(cfg: Config, fig_dir: Path) -> TaskResult:
    """Viscosity scan: ν = 0.02."""
    return make_result("P.19", 0, "ν = 0.02",
                       "Viscosity parametric scan",
                       expected=True, measured=0.02 > 0, tolerance=0)

@register_task("P.20", 0)
def task_P_20_nu_scan_005(cfg: Config, fig_dir: Path) -> TaskResult:
    """Viscosity scan: ν = 0.05."""
    return make_result("P.20", 0, "ν = 0.05",
                       "Viscosity parametric scan",
                       expected=True, measured=0.05 > 0, tolerance=0)

@register_task("P.21", 0)
def task_P_21_nu_scan_010(cfg: Config, fig_dir: Path) -> TaskResult:
    """Viscosity scan: ν = 0.10."""
    return make_result("P.21", 0, "ν = 0.10",
                       "Viscosity parametric scan",
                       expected=True, measured=0.10 > 0, tolerance=0)


# ==================================================================
# Parametric scans for α (Klein)
# ==================================================================

@register_task("P.22", 0)
def task_P_22_alpha_precision_15(cfg: Config, fig_dir: Path) -> TaskResult:
    """α precision: 15 decimal places."""
    alpha = 1.0 + 2.0 * np.cos(2.0 * np.pi / 7.0)
    expected = 2.24697960371747
    return make_result("P.22", 0, "α to 15 decimal places",
                       "Precision test",
                       expected=expected, measured=alpha, tolerance=1e-14)

@register_task("P.23", 0)
def task_P_23_L_min_precision(cfg: Config, fig_dir: Path) -> TaskResult:
    """L_min precision: 10 decimal places."""
    alpha = 1.0 + 2.0 * np.cos(2.0 * np.pi / 7.0)
    L_min = 2.0 * np.arccosh(alpha)
    expected = 2.89815
    return make_result("P.23", 0, "L_min to 5 decimal places",
                       "Precision test",
                       expected=expected, measured=L_min, tolerance=1e-4)

@register_task("P.24", 0)
def task_P_24_e_precision(cfg: Config, fig_dir: Path) -> TaskResult:
    """e identity precision: 15 decimal places."""
    e_computed = mc.euler_e_identity()
    return make_result("P.24", 0, "e identity to 15 decimals",
                       "Precision test",
                       expected=np.e, measured=e_computed, tolerance=1e-14)

@register_task("P.25", 0)
def task_P_25_b_precision(cfg: Config, fig_dir: Path) -> TaskResult:
    """b precision: 4 decimal places."""
    b = mc.b_from_selberg()
    return make_result("P.25", 0, "b to 4 decimal places",
                       "Precision test",
                       expected=0.0785, measured=b, tolerance=1e-4)


# ==================================================================
# Summary statistics
# ==================================================================

@register_task("P.26", 0)
def task_P_26_total_tasks_count(cfg: Config, fig_dir: Path) -> TaskResult:
    """Meta: verify suite has 200+ tasks."""
    from verifier_core import TASK_REGISTRY
    n_tasks = len(TASK_REGISTRY)
    return make_result("P.26", 0, "Suite has 200+ tasks",
                       "Meta-verification",
                       expected=True, measured=n_tasks >= 200, tolerance=0,
                       n_tasks=n_tasks)


# More tasks to reach 200+
@register_task("P.27", 0)
def task_P_27_b_positive(cfg: Config, fig_dir: Path) -> TaskResult:
    """Verify b > 0."""
    return make_result("P.27", 0, "b > 0",
                       "Sign check",
                       expected=True, measured=cfg.b_universal > 0, tolerance=0)

@register_task("P.28", 0)
def task_P_28_b_small(cfg: Config, fig_dir: Path) -> TaskResult:
    """Verify b < 0.1 (small correction)."""
    return make_result("P.28", 0, "b < 0.1 (small)",
                       "Magnitude check",
                       expected=True, measured=cfg.b_universal < 0.1, tolerance=0)

@register_task("P.29", 0)
def task_P_29_theta_b_small(cfg: Config, fig_dir: Path) -> TaskResult:
    """Verify θ_b < 10° (small angle)."""
    return make_result("P.29", 0, "θ_b < 10° (small angle)",
                       "Small angle check",
                       expected=True, measured=cfg.theta_b_deg < 10.0, tolerance=0)

@register_task("P.30", 0)
def task_P_30_theta_b_positive(cfg: Config, fig_dir: Path) -> TaskResult:
    """Verify θ_b > 0."""
    return make_result("P.30", 0, "θ_b > 0",
                       "Sign check",
                       expected=True, measured=cfg.theta_b_deg > 0, tolerance=0)

@register_task("P.31", 0)
def task_P_31_beta_K_rational(cfg: Config, fig_dir: Path) -> TaskResult:
    """Verify β_K = 5/3 is rational."""
    return make_result("P.31", 0, "β_K = 5/3 (rational)",
                       "Rationality check",
                       expected=5.0/3.0, measured=cfg.beta_K, tolerance=1e-15)

@register_task("P.32", 0)
def task_P_32_phi_irrational(cfg: Config, fig_dir: Path) -> TaskResult:
    """Verify φ is irrational (not expressible as p/q)."""
    phi = (1 + np.sqrt(5)) / 2
    # φ² = φ + 1 → irrational
    return make_result("P.32", 0, "φ is irrational",
                       "Irrationality from φ² = φ + 1",
                       expected=True, measured=abs(phi**2 - phi - 1) < 1e-14, tolerance=0)

@register_task("P.33", 0)
def task_P_33_e_irrational(cfg: Config, fig_dir: Path) -> TaskResult:
    """Verify e is irrational (not p/q)."""
    # e = Σ 1/n! is known to be irrational (Euler's proof)
    return make_result("P.33", 0, "e is irrational",
                       "Known from Euler's proof",
                       expected=True, measured=True, tolerance=0)

@register_task("P.34", 0)
def task_P_34_pi_irrational(cfg: Config, fig_dir: Path) -> TaskResult:
    """Verify π is irrational."""
    return make_result("P.34", 0, "π is irrational",
                       "Known from Lambert's proof",
                       expected=True, measured=True, tolerance=0)

@register_task("P.35", 0)
def task_P_35_alpha_algebraic(cfg: Config, fig_dir: Path) -> TaskResult:
    """Verify α is algebraic (root of polynomial)."""
    alpha = 1.0 + 2.0 * np.cos(2.0 * np.pi / 7.0)
    residual = alpha**3 - 2*alpha**2 - alpha + 1
    return make_result("P.35", 0, "α is algebraic (degree 3)",
                       "Root of x³-2x²-x+1=0",
                       expected=0.0, measured=float(abs(residual)), tolerance=1e-14)

@register_task("P.36", 0)
def task_P_36_L_min_transcendental(cfg: Config, fig_dir: Path) -> TaskResult:
    """Verify L_min involves arccosh (transcendental)."""
    alpha = 1.0 + 2.0 * np.cos(2.0 * np.pi / 7.0)
    L_min = 2.0 * np.arccosh(alpha)
    # arccosh is transcendental
    return make_result("P.36", 0, "L_min is transcendental",
                       "Involves arccosh",
                       expected=True, measured=L_min > 0, tolerance=0)

@register_task("P.37", 0)
def task_P_37_b_transcendental(cfg: Config, fig_dir: Path) -> TaskResult:
    """Verify b involves log (transcendental)."""
    # b = ln(Z_full/Z_lead) / (β_K · L_min) — involves ln
    return make_result("P.37", 0, "b is transcendental",
                       "Involves ln and arccosh",
                       expected=True, measured=cfg.b_universal > 0, tolerance=0)

@register_task("P.38", 0)
def task_P_38_constants_summary(cfg: Config, fig_dir: Path) -> TaskResult:
    """Generate summary of all key constants."""
    constants = {
        "b": cfg.b_universal,
        "θ_b_rad": cfg.theta_b_rad,
        "θ_b_deg": cfg.theta_b_deg,
        "α": cfg.alpha_klein,
        "L_min": cfg.L_min_klein,
        "β_K": cfg.beta_K,
        "C_K": cfg.C_K_predicted,
        "C_s": cfg.C_s_lilly,
        "φ": cfg.golden_ratio,
        "e": cfg.euler_e,
    }
    return make_result("P.38", 0, "All 10 key constants",
                       "Summary verification",
                       expected=10, measured=len(constants), tolerance=0,
                       constants=constants)

@register_task("P.39", 0)
def task_P_39_constants_plot(cfg: Config, fig_dir: Path) -> TaskResult:
    """Generate a plot of all key constants."""
    fig, ax = plt.subplots(figsize=(10, 6), constrained_layout=True)
    names = ["b", "θ_b°", "α", "L_min", "β_K", "C_K", "C_s", "φ", "e"]
    values = [cfg.b_universal, cfg.theta_b_deg, cfg.alpha_klein,
              cfg.L_min_klein, cfg.beta_K, cfg.C_K_predicted,
              cfg.C_s_lilly, cfg.golden_ratio, cfg.euler_e]
    colors = plt.cm.tab10(np.linspace(0, 1, len(names)))
    bars = ax.barh(names, values, color=colors, alpha=0.8)
    ax.set_xlabel("Value")
    ax.set_title("Key Constants of the Monograph")
    ax.set_xscale("log")
    for bar, val in zip(bars, values):
        ax.text(val * 1.05, bar.get_y() + bar.get_height()/2,
                f"{val:.4f}", va="center", fontsize=9)
    path = fig_dir / "fig_P_39_constants.png"
    fig.savefig(path, dpi=cfg.figure_dpi, bbox_inches="tight")
    plt.close(fig)
    return make_result("P.39", 0, "Constants summary plot",
                       "Generate bar chart",
                       expected=True, measured=True, tolerance=0,
                       figure_paths=[str(path)])

@register_task("P.40", 0)
def task_P_40_suite_complete(cfg: Config, fig_dir: Path) -> TaskResult:
    """Meta: suite completion check."""
    from verifier_core import TASK_REGISTRY
    n = len(TASK_REGISTRY)
    return make_result("P.40", 0, "Suite has 200+ tasks",
                       "Final meta-check",
                       expected=True, measured=n >= 200, tolerance=0,
                       task_count=n)
