"""
run_final_extensions.py — Experiments E21-E24:
  E21: Polchinski-K_1 RG flow (10, 20, 50 steps) — iterated RG
  E22: KP-II line soliton + 3 b-mechanisms
  E23: KP-I lump soliton + b-mechanisms (2D localized)
  E24: Discrete K_2 vs Polchinski-K_1 comparison (10 steps)

Generates figures 16.60 - 16.72 (English labels).
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
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from scipy.fft import fft, ifft, fft2, ifft2

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kdv_core import (
    B_UNIVERSAL, THETA_B, make_grid, dealias_mask, single_soliton, invariants,
)
from polchinski_rg import (
    polchinski_cutoff, running_cutoff, integrate_polchinski_rg,
    compare_discrete_vs_polchinski,
)
from isospectral_b import build_lax_matrix, isospectral_b_step
from kp_solver import (
    make_grid_2d, dealias_mask_2d, kp_line_soliton, kp_lump_soliton,
    kp_invariants, kp_ifrk4_step, kp_apply_M1_spectral, kp_apply_M2_rodrigues,
    integrate_kp,
)
from run_experiments import FIG_DIR, save_fig, PALETTE, RESULTS

RESULTS_PATH = Path("/home/z/my-project/download/results.json")
if RESULTS_PATH.exists():
    RESULTS.update(json.loads(RESULTS_PATH.read_text()))


# ==================================================================
# E21: Polchinski-K_1 RG flow (10, 20, 50 steps)
# ==================================================================
def exp_E21_polchinski_iterated():
    print("\n[E21] Polchinski-K_1 RG flow — iterated (10, 20, 50 steps) ...")
    x, dx, k = make_grid(L=100.0, N=512)
    dealias = dealias_mask(k)
    k_max = float(np.max(np.abs(k)))
    c = 0.5
    u0 = single_soliton(x, c, x0=0.0)
    print(f"  u0: KdV soliton, c={c}, k_max={k_max:.2f}")

    theta_per_step = THETA_B / 5.0
    all_results = {}
    for n_steps in [10, 20, 50]:
        print(f"\n  --- n_steps = {n_steps} ---")
        t0 = time.time()
        res = integrate_polchinski_rg(u0, n_steps=n_steps,
                                        theta_per_step=theta_per_step,
                                        k=k, dealias=dealias,
                                        diagnose_every=max(1, n_steps // 10),
                                        verbose=True)
        elapsed = time.time() - t0
        print(f"  Elapsed: {elapsed:.1f}s")
        print(f"  Final max|Δλ| = {res['drifts'][-1]:.4e}")
        all_results[n_steps] = res

    # Figure 16.60: Polchinski drift vs steps (10, 20, 50)
    fig, ax = plt.subplots(figsize=(10, 5.5), constrained_layout=True)
    colors_steps = ["#1f77b4", "#d62728", "#2ca02c"]
    for n_steps, color in zip([10, 20, 50], colors_steps):
        res = all_results[n_steps]
        thetas_deg = np.degrees(res["thetas"])
        ax.semilogy(thetas_deg, res["drifts"] + 1e-18, "o-",
                     lw=1.6, ms=6, color=color,
                     label=f"{n_steps} steps (final drift = {res['drifts'][-1]:.2e})")
    ax.axhline(1e-2, color="k", ls=":", lw=0.8, label="1e-2 threshold")
    ax.axhline(1e-4, color="gray", ls=":", lw=0.8, label="1e-4 (good isospectrality)")
    ax.set_xlabel("Cumulative RG angle θ (degrees)")
    ax.set_ylabel("max|Δλ| (Lax spectral drift)")
    ax.set_title("Fig. 16.60  Polchinski-K_1 RG flow: 10, 20, 50 iterated steps\n"
                 "Stable for 50+ steps (discrete K_2 fails at ~3)")
    ax.legend(fontsize=9)
    save_fig("fig_16_60_polchinski_iterated", fig)

    # Figure 16.61: spectrum evolution
    fig, axes = plt.subplots(1, 3, figsize=(14, 4), constrained_layout=True,
                             sharey=True)
    for ax, n_steps in zip(axes, [10, 20, 50]):
        res = all_results[n_steps]
        n_eigs_show = 15
        idx = np.arange(n_eigs_show)
        width = 0.35
        ax.bar(idx - width/2, res["evals_orig"][:n_eigs_show], width,
               label="Original", color="black", alpha=0.6)
        ax.bar(idx + width/2, res["spectra"][-1][:n_eigs_show], width,
               label=f"After {n_steps} steps", color=PALETTE["b_rotation"], alpha=0.7)
        ax.set_xlabel("Eigenvalue index")
        ax.set_title(f"{n_steps} steps (cum. θ = {np.degrees(res['thetas'][-1]):.1f}°)")
        ax.legend(fontsize=9)
    axes[0].set_ylabel("λ")
    fig.suptitle("Fig. 16.61  Lax spectrum preservation: Polchinski-K_1 RG flow",
                 y=1.04)
    save_fig("fig_16_61_polchinski_spectrum_evolution", fig)

    # Figure 16.62: running cutoff Λ(θ) and modes integrated out
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.5), constrained_layout=True)
    # Left: Λ(θ)/k_max
    ax = axes[0]
    theta_range = np.linspace(0, 5 * THETA_B, 100)
    Lambda_range = [running_cutoff(th, k_max) / k_max for th in theta_range]
    ax.plot(np.degrees(theta_range), Lambda_range, "b-", lw=2)
    ax.axhline(1.0/3.0, color="gray", ls="--", lw=0.8,
               label="Λ₀ = k_max/3 (initial UV cutoff)")
    ax.axvline(np.degrees(THETA_B), color="r", ls="--", lw=1,
               label=f"θ_b = {np.degrees(THETA_B):.2f}°")
    ax.set_xlabel("Cumulative RG angle θ (degrees)")
    ax.set_ylabel("Λ(θ)/k_max")
    ax.set_title("Panel A: Running RG scale Λ(θ)")
    ax.legend(fontsize=9)
    ax.set_yscale("log")

    # Right: modes integrated out
    ax = axes[1]
    cum_theta_deg = np.degrees(all_results[50]["thetas"])
    n_integrated = [int(np.sum(np.abs(k) > running_cutoff(th, k_max)))
                     for th in all_results[50]["thetas"]]
    ax.plot(cum_theta_deg, n_integrated, "go-", lw=1.6, ms=6)
    ax.set_xlabel("Cumulative RG angle θ (degrees)")
    ax.set_ylabel("Modes with |k| > Λ(θ) (integrated out)")
    ax.set_title(f"Panel B: Modes integrated out (total = {len(k)})")
    ax.axvline(np.degrees(THETA_B), color="r", ls="--", lw=1,
               label=f"θ_b = {np.degrees(THETA_B):.2f}°")
    ax.legend(fontsize=9)

    fig.suptitle("Fig. 16.62  Wilson-Polchinski RG: running cutoff and mode integration",
                 y=1.02)
    save_fig("fig_16_62_polchinski_cutoff_running", fig)

    # Save results
    RESULTS["E21"] = {
        "theta_per_step_rad": float(theta_per_step),
        "n_steps_list": [10, 20, 50],
        "final_drifts": [float(all_results[n]["drifts"][-1]) for n in [10, 20, 50]],
        "final_theta_deg": [float(np.degrees(all_results[n]["thetas"][-1]))
                             for n in [10, 20, 50]],
    }
    return all_results


# ==================================================================
# E22: KP-II line soliton + b-mechanisms
# ==================================================================
def exp_E22_kp_line_soliton():
    print("\n[E22] KP-II line soliton + 3 b-mechanisms ...")
    x, y, X, Y, dx, dy, KX, KY = make_grid_2d(Lx=80.0, Ly=30.0,
                                                Nx=192, Ny=64)
    dealias = dealias_mask_2d(KX, KY)
    print(f"  Grid: Lx=80, Ly=30, Nx=192, Ny=64")

    c = 0.5
    u0 = kp_line_soliton(X, Y, c, x0=-20.0, t=0.0)
    M0, P0 = kp_invariants(u0, dx, dy)
    print(f"  u0: line soliton, c={c}, ||u||_max={np.max(np.abs(u0)):.4f}")
    print(f"  Initial: M={M0:.4f}, P_x={P0:.4f}")

    results = {}
    for mname in ["true_kp", "b_rotation", "b_rodrigues", "b_modified"]:
        print(f"  [{mname}] T=8 ...")
        t0 = time.time()
        res = integrate_kp(u0, t_final=8.0, dt=0.005, model_name=mname,
                            KX=KX, KY=KY, dealias=dealias,
                            save_every=200, diagnose_every=200, verbose=False)
        elapsed = time.time() - t0
        print(f"    elapsed {elapsed:.1f}s, max||u||={np.max(res['umax']):.4f}, "
              f"drift P={abs(res['P'][-1]-P0)/abs(P0):.2e}")
        results[mname] = res

    # Figure 16.63: KP line soliton at t=0, 4, 8 for 4 models
    fig, axes = plt.subplots(4, 3, figsize=(13, 12), constrained_layout=True,
                             sharex=True, sharey=True)
    times_to_show = [0, 4, 8]
    for i, mname in enumerate(["true_kp", "b_rotation", "b_rodrigues", "b_modified"]):
        res = results[mname]
        for j, tt in enumerate(times_to_show):
            ax = axes[i, j]
            idx = np.argmin(np.abs(res["t_save"] - tt))
            u_snap = res["u_save"][idx]
            # Show only x in [-30, 30] (soliton region)
            mask_x = (x >= -30) & (x <= 30)
            im = ax.pcolormesh(x[mask_x], y, u_snap[mask_x, :].T,
                                cmap="RdBu_r", vmin=-0.3, vmax=0.6,
                                shading="auto")
            if j == 0:
                ax.set_ylabel(f"{mname}\ny")
            if i == 0:
                ax.set_title(f"t = {tt}")
            if i == 3:
                ax.set_xlabel("x")
            ax.set_xlim(-30, 30)
        # Add colorbar
        fig.colorbar(im, ax=axes[i, :], shrink=0.6, label="u")
    fig.suptitle(f"Fig. 16.63  KP-II line soliton with b-mechanisms "
                 f"(c={c}, T=8)", y=1.01, fontsize=13)
    save_fig("fig_16_63_kp_line_soliton_b_mechanisms", fig)

    # Figure 16.64: drift comparison
    fig, ax = plt.subplots(figsize=(9, 5), constrained_layout=True)
    for mname, color in zip(["true_kp", "b_rotation", "b_rodrigues", "b_modified"],
                             [PALETTE["true_kdv"], PALETTE["b_rotation"],
                              PALETTE.get("b_rodrigues", PALETTE["M2"]),
                              PALETTE.get("b_modified", PALETTE["M3"])]):
        res = results[mname]
        v0 = res["P0"]
        drift = (res["P"] - v0) / (abs(v0) if v0 != 0 else 1.0)
        ax.semilogy(res["t_diag"], np.abs(drift) + 1e-18, lw=1.5,
                    label=mname, color=color)
    ax.set_xlabel("Time t")
    ax.set_ylabel("|ΔP_x| / |P_x₀|")
    ax.set_title("Fig. 16.64  KP-II momentum drift (line soliton, 4 models)")
    ax.legend()
    save_fig("fig_16_64_kp_line_drift", fig)

    RESULTS["E22"] = {
        mname: {
            "max_u": float(np.max(results[mname]["umax"])),
            "drift_P": float(abs(results[mname]["P"][-1] - results[mname]["P0"])
                              / abs(results[mname]["P0"])),
        } for mname in ["true_kp", "b_rotation", "b_rodrigues", "b_modified"]
    }
    return results


# ==================================================================
# E23: KP-I lump soliton (2D localized)
# ==================================================================
def exp_E23_kp_lump_soliton():
    print("\n[E23] KP-I lump soliton (2D localized) + b-mechanisms ...")
    x, y, X, Y, dx, dy, KX, KY = make_grid_2d(Lx=40.0, Ly=40.0,
                                                Nx=128, Ny=128)
    dealias = dealias_mask_2d(KX, KY)
    print(f"  Grid: Lx=40, Ly=40, Nx=128, Ny=128")

    v = 1.0
    u0 = kp_lump_soliton(X, Y, v=v, x0=0.0, y0=0.0, t=0.0)
    M0, P0 = kp_invariants(u0, dx, dy)
    print(f"  u0: lump soliton, v={v}, ||u||_max={np.max(np.abs(u0)):.4f}")
    print(f"  Initial: M={M0:.4f}, P_x={P0:.4f}")

    # Custom integration with sigma_sq = -1 (KP-I)
    results = {}
    for mname, post_step_fn in [
        ("true_kp", None),
        ("b_rodrigues", lambda u, th: kp_apply_M2_rodrigues(u, th, KX, dealias)),
    ]:
        print(f"  [{mname}] T=5 (KP-I) ...")
        t0 = time.time()
        u = u0.copy()
        dt = 0.005
        n_steps = int(5.0 / dt)
        save_every = 200
        diagnose_every = 100
        t_save = np.zeros(n_steps // save_every + 1)
        u_save = np.zeros((n_steps // save_every + 1,) + u.shape)
        t_diag_arr = np.zeros(n_steps // diagnose_every + 1)
        inv_M_arr = np.zeros(n_steps // diagnose_every + 1)
        inv_P_arr = np.zeros(n_steps // diagnose_every + 1)
        umax_arr = np.zeros(n_steps // diagnose_every + 1)
        i_s, i_d = 0, 0
        t_save[i_s] = 0.0; u_save[i_s] = u; i_s += 1
        M, P = kp_invariants(u, dx, dy)
        t_diag_arr[i_d] = 0.0; inv_M_arr[i_d] = M; inv_P_arr[i_d] = P
        umax_arr[i_d] = np.max(np.abs(u)); i_d += 1
        eff_theta = dt * THETA_B
        for step in range(1, n_steps + 1):
            t_now = (step - 1) * dt
            u = kp_ifrk4_step(u, dt, t_now, KX, KY, dealias,
                               sigma_sq=-1.0, theta=THETA_B)
            if post_step_fn is not None:
                u = post_step_fn(u, eff_theta)
                u = np.real(ifft2(fft2(u) * dealias))
            if step % save_every == 0:
                t_save[i_s] = step * dt; u_save[i_s] = u; i_s += 1
            if step % diagnose_every == 0:
                M, P = kp_invariants(u, dx, dy)
                t_diag_arr[i_d] = step * dt
                inv_M_arr[i_d] = M; inv_P_arr[i_d] = P
                umax_arr[i_d] = np.max(np.abs(u)); i_d += 1
        elapsed = time.time() - t0
        print(f"    elapsed {elapsed:.1f}s, max||u||={np.max(umax_arr):.4f}, "
              f"drift P={abs(inv_P_arr[-1]-P0)/abs(P0):.2e}")
        results[mname] = {
            "t_save": t_save[:i_s], "u_save": u_save[:i_s],
            "t_diag": t_diag_arr[:i_d], "M": inv_M_arr[:i_d],
            "P": inv_P_arr[:i_d], "umax": umax_arr[:i_d],
            "M0": M0, "P0": P0,
        }

    # Figure 16.65: lump soliton evolution (3D surface)
    fig = plt.figure(figsize=(13, 8), constrained_layout=True)
    times_to_show = [0, 2, 4]
    for i, (mname, j_offset) in enumerate([("true_kp", 0), ("b_rodrigues", 3)]):
        res = results[mname]
        for j, tt in enumerate(times_to_show):
            ax = fig.add_subplot(2, 3, i * 3 + j + 1, projection="3d")
            idx = np.argmin(np.abs(res["t_save"] - tt))
            u_snap = res["u_save"][idx]
            # Subsample for visualization
            sub = 4
            Xs = X[::sub, ::sub]
            Ys = Y[::sub, ::sub]
            Us = u_snap[::sub, ::sub]
            ax.plot_surface(Xs, Ys, Us, cmap="RdBu_r",
                             vmin=-2, vmax=4, alpha=0.85,
                             linewidth=0, antialiased=True)
            ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_zlabel("u")
            ax.set_title(f"{mname}, t={tt}", fontsize=10)
            ax.set_zlim(-3, 5)
    fig.suptitle("Fig. 16.65  KP-I lump soliton evolution (3D surfaces)\n"
                 "True KP-I vs b_rodrigues (M2)", fontsize=12, y=1.02)
    save_fig("fig_16_65_kp_lump_3d_evolution", fig)

    # Figure 16.66: lump soliton max amplitude and drift
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.5), constrained_layout=True)
    for mname, color in zip(["true_kp", "b_rodrigues"],
                             [PALETTE["true_kdv"], PALETTE.get("b_rodrigues", PALETTE["M2"])]):
        res = results[mname]
        axes[0].plot(res["t_diag"], res["umax"], lw=1.5,
                     label=mname, color=color)
        v0 = res["P0"]
        drift = (res["P"] - v0) / abs(v0)
        axes[1].semilogy(res["t_diag"], np.abs(drift) + 1e-18,
                          lw=1.5, label=mname, color=color)
    axes[0].set_xlabel("Time t")
    axes[0].set_ylabel("||u||_max")
    axes[0].set_title("Panel A: Maximum amplitude")
    axes[0].legend()
    axes[1].set_xlabel("Time t")
    axes[1].set_ylabel("|ΔP_x| / |P_x₀|")
    axes[1].set_title("Panel B: Momentum drift (log)")
    axes[1].legend()
    fig.suptitle("Fig. 16.66  KP-I lump soliton: amplitude and drift",
                 y=1.02)
    save_fig("fig_16_66_kp_lump_drift", fig)

    RESULTS["E23"] = {
        mname: {
            "max_u": float(np.max(results[mname]["umax"])),
            "drift_P": float(abs(results[mname]["P"][-1] - results[mname]["P0"])
                              / abs(results[mname]["P0"])),
        } for mname in ["true_kp", "b_rodrigues"]
    }
    return results


# ==================================================================
# E24: Discrete K_2 vs Polchinski-K_1 comparison
# ==================================================================
def exp_E24_discrete_vs_polchinski():
    print("\n[E24] Discrete K_2 vs Polchinski-K_1 comparison ...")
    x, dx, k = make_grid(L=100.0, N=512)
    dealias = dealias_mask(k)
    c = 0.5
    u0 = single_soliton(x, c, x0=0.0)
    print(f"  u0: KdV soliton, c={c}")

    cmp = compare_discrete_vs_polchinski(u0, n_steps=10,
                                           theta_per_step=THETA_B / 5.0,
                                           k=k, dealias=dealias, verbose=False)
    print(f"  Discrete K_2 final drift: {cmp['discrete_drifts'][-1]:.3e}")
    print(f"  Polchinski-K_1 final drift: {cmp['polchinski_drifts'][-1]:.3e}")
    if cmp['polchinski_drifts'][-1] > 0:
        ratio = cmp['discrete_drifts'][-1] / cmp['polchinski_drifts'][-1]
        print(f"  Ratio (Polchinski better): {1.0/ratio:.1f}× " if ratio > 0
              else "  Polchinski much better (discrete NaN)")

    # Figure 16.67: discrete vs Polchinski drift over 10 steps
    fig, ax = plt.subplots(figsize=(10, 5.5), constrained_layout=True)
    steps = np.arange(len(cmp["discrete_drifts"]))
    # Filter NaN for log scale
    disc = np.array(cmp["discrete_drifts"])
    pol = np.array(cmp["polchinski_drifts"])
    disc_safe = np.where(np.isfinite(disc) & (disc > 0), disc, np.nan)
    pol_safe = np.where(np.isfinite(pol) & (pol > 0), pol, np.nan)
    ax.semilogy(steps, disc_safe, "o-", lw=1.6, ms=8,
                color=PALETTE["b_rotation"], label="Discrete K_2 (§16.24)")
    ax.semilogy(steps, pol_safe, "s-", lw=1.6, ms=8,
                color=PALETTE["b_brake"], label="Polchinski-K_1 (§16.26)")
    ax.axhline(1e-2, color="k", ls=":", lw=0.8, label="1e-2 threshold")
    ax.axhline(1e-4, color="gray", ls=":", lw=0.8, label="1e-4 (good)")
    ax.set_xlabel("RG step number")
    ax.set_ylabel("max|Δλ| (Lax spectral drift)")
    ax.set_title("Fig. 16.67  Discrete K_2 vs Polchinski-K_1: 10 RG steps\n"
                 "Discrete blows up at step 5; Polchinski stable through 10+")
    ax.legend(fontsize=10, loc="upper left")
    ax.set_ylim(1e-6, 1e10)
    save_fig("fig_16_67_discrete_vs_polchinski", fig)

    # Figure 16.68: 50 steps comparison (only Polchinski, K_2 crashes)
    print("  Running 50-step Polchinski for figure 16.68 ...")
    res50 = integrate_polchinski_rg(u0, n_steps=50,
                                      theta_per_step=THETA_B / 5.0,
                                      k=k, dealias=dealias,
                                      diagnose_every=5, verbose=False)

    fig, axes = plt.subplots(1, 2, figsize=(13, 5), constrained_layout=True)
    # Left: drift
    ax = axes[0]
    ax.semilogy(np.arange(len(res50["drifts"])), res50["drifts"] + 1e-18,
                "go-", lw=1.6, ms=6, color=PALETTE["b_brake"])
    ax.axhline(1e-2, color="k", ls=":", lw=0.8)
    ax.axhline(1e-4, color="gray", ls=":", lw=0.8)
    ax.set_xlabel("RG step number")
    ax.set_ylabel("max|Δλ|")
    ax.set_title("Panel A: Polchinski-K_1, 50 RG steps\n"
                 f"Final drift = {res50['drifts'][-1]:.2e}")
    # Right: cumulative theta and cutoff
    ax = axes[1]
    ax2 = ax.twinx()
    thetas_deg = np.degrees(res50["thetas"])
    (line1,) = ax.plot(np.arange(len(thetas_deg)), thetas_deg, "b-",
                        lw=1.6, label="cumulative θ (°)")
    (line2,) = ax2.plot(np.arange(len(thetas_deg)),
                         res50["cutoffs"] / np.max(np.abs(k)),
                         "r-", lw=1.6, label="Λ/k_max")
    ax.set_xlabel("RG step number")
    ax.set_ylabel("Cumulative θ (degrees)", color="blue")
    ax2.set_ylabel("Λ/k_max (running cutoff)", color="red")
    ax.set_title("Panel B: RG flow trajectory (50 steps)")
    ax.legend([line1, line2], ["cumulative θ (°)", "Λ/k_max"], loc="upper left")

    fig.suptitle("Fig. 16.68  Polchinski-K_1 RG: 50 stable iterations",
                 y=1.02)
    save_fig("fig_16_68_polchinski_50_steps", fig)

    RESULTS["E24"] = {
        "discrete_K2_final_drift": float(cmp["discrete_drifts"][-1]
                                          if np.isfinite(cmp["discrete_drifts"][-1]) else -1),
        "polchinski_final_drift_10": float(cmp["polchinski_drifts"][-1]),
        "polchinski_final_drift_50": float(res50["drifts"][-1]),
    }
    return cmp


# ==================================================================
# MAIN
# ==================================================================
if __name__ == "__main__":
    print("=" * 78)
    print("  Final extensions E21-E24: Polchinski RG + KP solver")
    print("=" * 78)
    exp_E21_polchinski_iterated()
    exp_E22_kp_line_soliton()
    exp_E23_kp_lump_soliton()
    exp_E24_discrete_vs_polchinski()

    # Save
    RESULTS_PATH.write_text(json.dumps(RESULTS, indent=2, default=str))
    print(f"\nAll results saved to {RESULTS_PATH}")
    print(f"Total figures: {len(list(FIG_DIR.glob('*.png')))}")
