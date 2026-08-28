"""
run_experiments.py — Runs all 15 KdV experiments with the b-correction
and generates the 25+ professional figures (English labels) for the
report (chapter 16 of the monograph).

Output:
    /home/z/my-project/download/figures/*.png     (45 figures)
    /home/z/my-project/download/results.json      (numerical results)

Experiments:
    E1   Single soliton, baseline (no b)
    E2   Single soliton + M1 (spectral b-shift)
    E3   Single soliton + M2 (Rodrigues in (u, u_x))
    E4   Single soliton + M3 (modified nonlinearity)
    E5   Two-soliton collision, no b
    E6   Two-soliton collision + 3 b-mechanisms
    E7   Three-soliton interaction
    E8   mKdV (modified KdV) baseline + b
    E9   5-model comparison (true KdV + 4 b-modifications)
    E10  Systematic scan: 12 rotation angles θ_b
    E11  Dispersion relation measurement
    E12  Long-time evolution (T=50)
    E13  Perturbed initial conditions
    E14  Statistics over 50 random ICs
    E15  Universality check (Theorem 13.1)
"""
from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.colors import LinearSegmentedColormap

# Font setup
for fp in [
    "/usr/share/fonts/truetype/english/Tinos-Regular.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
]:
    if os.path.exists(fp):
        try:
            fm.fontManager.addfont(fp)
        except Exception:
            pass

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Tinos", "DejaVu Serif", "Liberation Serif"],
    "font.size": 11,
    "axes.titlesize": 12,
    "axes.labelsize": 11,
    "axes.grid": True,
    "grid.alpha": 0.3,
    "grid.linestyle": "--",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "figure.dpi": 110,
    "savefig.dpi": 160,
    "savefig.bbox": "standard",
    "legend.frameon": False,
})

# Local imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kdv_core import (
    B_UNIVERSAL, THETA_B, make_grid, dealias_mask,
    single_soliton, two_solitons, three_solitons,
    invariants, MODELS, integrate, apply_M1_spectral, apply_M2_rodrigues,
    hilbert_fft, two_soliton_phase_shifts, sech2,
)
import monograph_constants as mc

# ------------------------------------------------------------------
# Output directories
# ------------------------------------------------------------------
FIG_DIR = Path("/home/z/my-project/download/figures")
FIG_DIR.mkdir(parents=True, exist_ok=True)
RESULTS_PATH = Path("/home/z/my-project/download/results.json")

# Color palette (publication-quality, color-blind safe)
PALETTE = {
    "true_kdv":   "#1f77b4",   # blue
    "b_rotation": "#d62728",   # red
    "b_brake":    "#2ca02c",   # green
    "b_linear":   "#ff7f0e",   # orange
    "b_les":      "#9467bd",   # purple
    "b_modified": "#8c564b",   # brown
    "M1":         "#d62728",
    "M2":         "#2ca02c",
    "M3":         "#9467bd",
    "b":          "#d62728",
    "no_b":       "#1f77b4",
}

RESULTS = {}


def save_fig(name: str, fig=None):
    """Save figure to FIG_DIR with consistent naming."""
    path = FIG_DIR / f"{name}.png"
    if fig is None:
        fig = plt.gcf()
    fig.savefig(path, dpi=160, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"    [fig] {path.name}")
    return str(path)


# ==================================================================
# EXPERIMENT E1 — single soliton baseline
# ==================================================================
def exp_E1_baseline():
    print("\n[E1] Single soliton, baseline (no b), T=20 ...")
    x, dx, k = make_grid(L=100.0, N=1024)
    dealias = dealias_mask(k)
    c = 0.5
    u0 = single_soliton(x, c, x0=-20.0)

    t0 = time.time()
    res = integrate(u0, t_final=20.0, dt=0.002,
                    model_name="true_kdv", k=k, dealias=dealias,
                    save_every=200, diagnose_every=100, verbose=False)
    print(f"    elapsed: {time.time()-t0:.1f}s, "
          f"final t={res['t_save'][-1]:.2f}, "
          f"max||u||={np.max(res['umax']):.4f}")

    # Figure 16.3: space-time heatmap
    fig, ax = plt.subplots(figsize=(8, 5), constrained_layout=True)
    T_save = res["t_save"]
    U = res["u_save"]
    # Compute peak position over time
    peak_idx = np.argmax(U, axis=1)
    peak_x = x[peak_idx]
    # Unwrap peak position for periodicity
    peak_x_unwrap = np.copy(peak_x)
    for i in range(1, len(peak_x_unwrap)):
        if peak_x_unwrap[i] - peak_x_unwrap[i-1] > 50:
            peak_x_unwrap[i:] -= 100
        elif peak_x_unwrap[i] - peak_x_unwrap[i-1] < -50:
            peak_x_unwrap[i:] += 100
    ax.plot(T_save, peak_x_unwrap, "b-", lw=2, label="soliton peak")
    ax.plot(T_save, 4*c*c*T_save - 20, "k--", lw=1, label="expected: 4c²t − 20")
    ax.set_xlabel("Time t")
    ax.set_ylabel("Peak position x")
    ax.set_title(f"Fig. 16.3  Single soliton trajectory (c={c}, true KdV)")
    ax.legend()
    save_fig("fig_16_03_soliton_trajectory", fig)

    # Figure 16.4: invariants
    fig, axes = plt.subplots(1, 3, figsize=(12, 3.5), constrained_layout=True)
    for ax, inv, name, val0 in zip(
        axes, [res["M"], res["P"], res["E"]],
        ["Mass M = ∫u dx", "Momentum P = ∫u² dx", "Energy E = ∫(u_x² − u³) dx"],
        [res["M0"], res["P0"], res["E0"]]):
        drift = (inv - val0) / abs(val0) if val0 != 0 else inv - val0
        ax.semilogy(res["t_diag"], np.abs(drift) + 1e-18, "b-", lw=1.5)
        ax.set_xlabel("Time t")
        ax.set_ylabel(f"|Δ{name.split('=')[0].strip()}| / |{name.split('=')[0].strip()}₀|")
        ax.set_title(name)
        ax.axhline(1e-10, color="k", ls=":", lw=0.8, label="1e-10")
        ax.legend()
    fig.suptitle("Fig. 16.4  Invariant conservation (true KdV, baseline)", y=1.02)
    save_fig("fig_16_04_invariants_baseline", fig)

    RESULTS["E1"] = {
        "max_u": float(np.max(res["umax"])),
        "drift_M": float(abs(res["M"][-1] - res["M0"]) / abs(res["M0"])),
        "drift_P": float(abs(res["P"][-1] - res["P0"]) / abs(res["P0"])),
        "drift_E": float(abs(res["E"][-1] - res["E0"]) / abs(res["E0"])),
        "peak_velocity": float((peak_x_unwrap[-1] - peak_x_unwrap[0]) / T_save[-1]),
        "expected_velocity": float(4 * c * c),
    }
    return res


# ==================================================================
# EXPERIMENTS E2-E4 — single soliton with 3 b-mechanisms
# ==================================================================
def exp_E2_E4_three_mechanisms():
    print("\n[E2-E4] Single soliton with M1/M2/M3 b-mechanisms ...")
    x, dx, k = make_grid(L=100.0, N=1024)
    dealias = dealias_mask(k)
    c = 0.5
    u0 = single_soliton(x, c, x0=-20.0)

    # All three b-mechanisms are now proper models in kdv_core.MODELS
    # M1 = b_rotation  (post-step spectral phase shift)
    # M2 = b_rodrigues (post-step Rodrigues in (u, u_x))
    # M3 = b_modified  (in-RHS modified nonlinearity)
    model_map = {"M1": "b_rotation", "M2": "b_rodrigues", "M3": "b_modified"}
    results = {}
    for mech_name, model_key in model_map.items():
        print(f"  [{mech_name}] integrating {model_key} to T=20 ...")
        t0 = time.time()
        res = integrate(u0, t_final=20.0, dt=0.002,
                        model_name=model_key, k=k, dealias=dealias,
                        save_every=200, diagnose_every=100, verbose=False)
        print(f"    elapsed {time.time()-t0:.1f}s, "
              f"max||u||={np.max(res['umax']):.4f}, "
              f"drift E={abs(res['E'][-1]-res['E0'])/abs(res['E0']):.2e}")
        results[mech_name] = res

    # Figure 16.5: 3 panels showing soliton at t=0,10,20 for each mechanism
    fig, axes = plt.subplots(1, 3, figsize=(13, 3.8), constrained_layout=True,
                             sharey=True)
    times_to_show = [0.0, 10.0, 20.0]
    for ax, mech_name in zip(axes, ["M1", "M2", "M3"]):
        res = results[mech_name]
        for t_target in times_to_show:
            idx = np.argmin(np.abs(res["t_save"] - t_target))
            ax.plot(x, res["u_save"][idx], lw=1.7,
                    label=f"t={res['t_save'][idx]:.1f}")
        ax.set_xlabel("x")
        ax.set_title(f"{mech_name}: {res['label']}")
        ax.set_ylim(-0.3, 0.7)
        ax.legend(loc="upper right")
    axes[0].set_ylabel("u(x, t)")
    fig.suptitle("Fig. 16.5  Single soliton with three b-mechanisms "
                 f"(θ_b = {np.degrees(THETA_B):.2f}°)", y=1.03)
    save_fig("fig_16_05_three_mechanisms_soliton", fig)

    # Figure 16.6: invariant drift comparison
    fig, axes = plt.subplots(1, 3, figsize=(13, 3.5), constrained_layout=True)
    for ax, inv_name, inv_key, val_key in zip(
        axes, ["Mass M", "Momentum P", "Energy E"],
        ["M", "P", "E"], ["M0", "P0", "E0"]):
        for mech_name, color in zip(["M1", "M2", "M3"],
                                     [PALETTE["M1"], PALETTE["M2"], PALETTE["M3"]]):
            res = results[mech_name]
            v0 = res[val_key]
            drift = (res[inv_key] - v0) / (abs(v0) if v0 != 0 else 1.0)
            ax.semilogy(res["t_diag"], np.abs(drift) + 1e-18,
                        color=color, lw=1.5, label=mech_name)
        ax.set_xlabel("Time t")
        ax.set_ylabel(f"|Δ{inv_name}| / |{inv_name}₀|")
        ax.set_title(inv_name)
        ax.legend()
    fig.suptitle("Fig. 16.6  Invariant drift for three b-mechanisms", y=1.02)
    save_fig("fig_16_06_invariants_three_mechanisms", fig)

    # Figure 16.7: soliton peak displacement vs time (phase shift measurement)
    fig, ax = plt.subplots(figsize=(8, 4.5), constrained_layout=True)
    for mech_name, color in zip(["M1", "M2", "M3"],
                                 [PALETTE["M1"], PALETTE["M2"], PALETTE["M3"]]):
        res = results[mech_name]
        peak_idx = np.argmax(res["u_save"], axis=1)
        peak_x = x[peak_idx]
        # Unwrap
        for i in range(1, len(peak_x)):
            if peak_x[i] - peak_x[i-1] > 50:
                peak_x[i:] -= 100
            elif peak_x[i] - peak_x[i-1] < -50:
                peak_x[i:] += 100
        # Reference: expected trajectory without b = 4c²·t - 20
        expected = 4 * c * c * res["t_save"] - 20
        shift = peak_x - expected
        ax.plot(res["t_save"], shift, color=color, lw=1.5, label=mech_name)
    ax.axhline(0, color="k", ls="-", lw=0.5)
    ax.set_xlabel("Time t")
    ax.set_ylabel("Peak position shift Δx(t) = x_peak − 4c²t")
    ax.set_title("Fig. 16.7  Phase shift induced by b-rotation")
    ax.legend()
    save_fig("fig_16_07_phase_shift_three_mechanisms", fig)

    RESULTS["E2_E4"] = {
        mech: {
            "max_u": float(np.max(results[mech]["umax"])),
            "drift_M": float(abs(results[mech]["M"][-1] - results[mech]["M0"])
                              / abs(results[mech]["M0"])),
            "drift_P": float(abs(results[mech]["P"][-1] - results[mech]["P0"])
                              / abs(results[mech]["P0"])),
            "drift_E": float(abs(results[mech]["E"][-1] - results[mech]["E0"])
                              / abs(results[mech]["E0"])),
        } for mech in ["M1", "M2", "M3"]
    }
    return results


# ==================================================================
# EXPERIMENT E5 — two-soliton collision (baseline, no b)
# ==================================================================
def exp_E5_two_soliton_baseline():
    print("\n[E5] Two-soliton collision (no b) ...")
    x, dx, k = make_grid(L=120.0, N=1024)
    dealias = dealias_mask(k)
    c1, c2 = 0.8, 0.4   # c1 > c2: faster soliton starts LEFT, catches up
    u0 = two_solitons(x, c1, c2, x1=-30.0, x2=10.0)

    t0 = time.time()
    res = integrate(u0, t_final=30.0, dt=0.002,
                    model_name="true_kdv", k=k, dealias=dealias,
                    save_every=150, diagnose_every=100, verbose=False)
    print(f"    elapsed {time.time()-t0:.1f}s, "
          f"max||u||={np.max(res['umax']):.4f}, "
          f"drift E={abs(res['E'][-1]-res['E0'])/abs(res['E0']):.2e}")

    # Figure 16.8: 6-panel evolution
    fig, axes = plt.subplots(2, 3, figsize=(13, 6), constrained_layout=True,
                             sharex=True, sharey=True)
    times_to_show = [0, 6, 12, 18, 24, 30]
    for ax, tt in zip(axes.flat, times_to_show):
        idx = np.argmin(np.abs(res["t_save"] - tt))
        ax.plot(x, res["u_save"][idx], "b-", lw=1.6)
        ax.set_title(f"t = {res['t_save'][idx]:.1f}")
        ax.set_xlabel("x")
        ax.set_ylim(-0.2, 1.6)
    axes[0, 0].set_ylabel("u(x,t)")
    axes[1, 0].set_ylabel("u(x,t)")
    fig.suptitle(f"Fig. 16.8  Two-soliton collision (c₁={c1}, c₂={c2}, true KdV)",
                 y=1.02)
    save_fig("fig_16_08_two_soliton_collision", fig)

    # Figure 16.9: invariants during collision
    fig, axes = plt.subplots(1, 3, figsize=(12, 3.5), constrained_layout=True)
    for ax, inv, name, v0 in zip(
        axes, [res["M"], res["P"], res["E"]],
        ["M", "P", "E"], [res["M0"], res["P0"], res["E0"]]):
        drift = (inv - v0) / (abs(v0) if v0 != 0 else 1.0)
        ax.semilogy(res["t_diag"], np.abs(drift) + 1e-18, "b-", lw=1.5)
        ax.set_xlabel("Time t")
        ax.set_ylabel(f"|Δ{name}|/|{name}₀|")
        ax.set_title(name)
    fig.suptitle("Fig. 16.9  Invariants during two-soliton collision", y=1.02)
    save_fig("fig_16_09_invariants_collision", fig)

    # Figure 16.10: trajectory + analytical phase shift
    fig, ax = plt.subplots(figsize=(8, 5), constrained_layout=True)
    # Track two peaks (need to split the domain)
    peak_list_over_time = []
    for u_snapshot in res["u_save"][::3]:  # subsample for speed
        # Find local maxima above 0.05 threshold
        from scipy.signal import find_peaks
        peaks, _ = find_peaks(u_snapshot, height=0.05, distance=50)
        peak_list_over_time.append(x[peaks])
    # Plot trajectories of the two largest peaks at each time
    times_sub = res["t_save"][::3]
    fast_traj = []
    slow_traj = []
    for plist, tt in zip(peak_list_over_time, times_sub):
        if len(plist) >= 2:
            # Sort by amplitude? Easier: sort by current position
            # Fast soliton (originally at -30) moves faster to the right
            # After collision: fast soliton ends up further right
            # Use peak amplitude: fast soliton has higher amplitude (2c₁² = 1.28)
            # Slow soliton has amplitude 2c₂² = 0.32
            # We can distinguish by amplitude
            u_at_peaks = [u_snapshot[np.argmin(np.abs(x - p))] for p in plist]
            # Just take both peaks and sort by position
            sorted_p = sorted(plist)
            slow_traj.append(sorted_p[0])
            fast_traj.append(sorted_p[-1])
        elif len(plist) == 1:
            fast_traj.append(plist[0])
            slow_traj.append(np.nan)
        else:
            fast_traj.append(np.nan)
            slow_traj.append(np.nan)

    ax.plot(times_sub, fast_traj, "r-o", ms=3, lw=1.5, label="fast soliton (c₁)")
    ax.plot(times_sub, slow_traj, "b-s", ms=3, lw=1.5, label="slow soliton (c₂)")
    # Analytical expected positions
    # Before collision: x_fast = -30 + 4c₁²·t, x_slow = 10 + 4c₂²·t
    # After collision (approx t > 15): x_fast = -30 + 4c₁²·t + Δx₁
    #                                  x_slow = 10 + 4c₂²·t + Δx₂
    dx1, dx2 = two_soliton_phase_shifts(c1, c2)
    print(f"    analytical phase shifts: Δx₁={dx1:.4f}, Δx₂={dx2:.4f}")
    t_pre = np.linspace(0, 12, 50)
    t_post = np.linspace(15, 30, 50)
    ax.plot(t_pre, -30 + 4*c1**2*t_pre, "r--", lw=0.8, alpha=0.5)
    ax.plot(t_pre, 10 + 4*c2**2*t_pre, "b--", lw=0.8, alpha=0.5)
    ax.plot(t_post, -30 + 4*c1**2*t_post + dx1, "r--", lw=0.8, alpha=0.5,
            label=f"analytical post-collision (Δx₁={dx1:.2f})")
    ax.plot(t_post, 10 + 4*c2**2*t_post + dx2, "b--", lw=0.8, alpha=0.5,
            label=f"analytical post-collision (Δx₂={dx2:.2f})")
    ax.set_xlabel("Time t")
    ax.set_ylabel("Soliton position x")
    ax.set_title("Fig. 16.10  Soliton trajectories and Lax phase shifts")
    ax.legend(loc="upper left", fontsize=9)
    save_fig("fig_16_10_soliton_trajectories_phaseshift", fig)

    RESULTS["E5"] = {
        "c1": c1, "c2": c2,
        "phase_shift_fast_predicted": float(dx1),
        "phase_shift_slow_predicted": float(dx2),
        "drift_E": float(abs(res["E"][-1] - res["E0"]) / abs(res["E0"])),
    }
    return res


if __name__ == "__main__":
    print("=" * 78)
    print("  KdV + b-correction experiments — chapter 16 of the monograph")
    print("=" * 78)
    exp_E1_baseline()
    exp_E2_E4_three_mechanisms()
    exp_E5_two_soliton_baseline()

    # Save partial results
    RESULTS_PATH.write_text(json.dumps(RESULTS, indent=2, default=str))
    print(f"\nPartial results saved to {RESULTS_PATH}")
    print(f"Figures saved to {FIG_DIR}")
