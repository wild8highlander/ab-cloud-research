"""Generate all 3D NSE figures from saved partial results."""
import sys, os, json
sys.path.insert(0, "/home/z/my-project/scripts")
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from pathlib import Path
from scipy.fft import rfftn, irfftn

from nse3d_core import (
    make_grid_3d, dealias_mask_3d, taylor_green_vortex, curl,
    kinetic_energy, vorticity_norm_inf, energy_spectrum,
    rodrigues_3d_rotation, verify_rodrigues_orthogonality,
    velocity_from_vorticity,
)
from kdv_core import B_UNIVERSAL, THETA_B
from run_experiments import FIG_DIR, save_fig, PALETTE, RESULTS

RESULTS_PATH = Path("/home/z/my-project/download/results.json")
PARTIAL_PATH = Path("/home/z/my-project/download/3d_nse_partial.json")
if RESULTS_PATH.exists():
    RESULTS.update(json.loads(RESULTS_PATH.read_text()))

partial = json.loads(PARTIAL_PATH.read_text())
N = 32
nu = 0.02
x, y, z, X, Y, Z, dx, KX, KY, KZ, K2, K2_safe, K_mag = make_grid_3d(N=N)
dealias = dealias_mask_3d(KX, KY, KZ)
u0 = taylor_green_vortex(X, Y, Z, V0=1.0, k=1)

models = ["true_nse", "b_rodrigues", "b_brake", "b_les", "polchinski_b"]
results = {}
for mname in models:
    r = partial["results"][mname]
    r["t_diag"] = np.array(r["t_diag"])
    r["omega_max"] = np.array(r["omega_max"])
    r["omega_rms"] = np.array(r["omega_rms"])
    r["energy"] = np.array(r["energy"])
    # Load final u field
    npz = np.load(f"/home/z/my-project/download/3d_nse_u_final_{mname}.npz")
    r["u_final"] = npz["u_final"]
    results[mname] = r

# Compute stabilization factors
true_final = results["true_nse"]["omega_max"][-1]
stab = {m: true_final / results[m]["omega_max"][-1] for m in models}
print("Stabilization factors:")
for m in models:
    print(f"  {m:20s}: {stab[m]:.3f}×")

# Color palette
colors = {
    "true_nse": PALETTE["true_kdv"],
    "b_rodrigues": PALETTE["b_rotation"],
    "b_brake": PALETTE["b_brake"],
    "b_les": PALETTE["b_les"],
    "polchinski_b": PALETTE.get("b_modified", "#9467bd"),
}

# ====== Figure 16.69: ||ω||_max(t) for 5 models (THE KEY PLOT) ======
fig, ax = plt.subplots(figsize=(10, 6), constrained_layout=True)
for mname in models:
    res = results[mname]
    ax.plot(res["t_diag"], res["omega_max"], lw=1.8,
            label=f"{mname} (final = {res['omega_max'][-1]:.3f})",
            color=colors.get(mname, "gray"))
ax.set_xlabel("Time t")
ax.set_ylabel("||ω||_∞(t)")
ax.set_title(f"Fig. 16.69  3D NSE Taylor-Green vortex: ||ω||_∞(t) for 5 models\n"
             f"(N={N}, ν={nu}, T=2.0) — Theorem 8.1 verification")
ax.legend(fontsize=10, loc="best")
ax.grid(True, alpha=0.3)
save_fig("fig_16_69_3d_nse_omega_max_5_models", fig)

# ====== Figure 16.70: Energy E(t) ======
fig, ax = plt.subplots(figsize=(10, 5.5), constrained_layout=True)
for mname in models:
    res = results[mname]
    E_drift = (res["energy"] - res["E0"]) / res["E0"]
    ax.plot(res["t_diag"], E_drift, lw=1.6,
            label=mname, color=colors.get(mname, "gray"))
ax.set_xlabel("Time t")
ax.set_ylabel("ΔE / E₀ (relative energy change)")
ax.set_title("Fig. 16.70  3D NSE energy evolution: viscous decay + b-rotation effect")
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)
save_fig("fig_16_70_3d_nse_energy_5_models", fig)

# ====== Figure 16.71: Stabilization bar chart ======
fig, ax = plt.subplots(figsize=(9, 5.5), constrained_layout=True)
mnames = [m for m in models if m != "true_nse"]
stab_vals = [stab[m] for m in mnames]
bar_colors = [colors.get(m, "gray") for m in mnames]
bars = ax.bar(mnames, stab_vals, color=bar_colors, alpha=0.8)
ax.axhline(1.0, color="k", ls="--", lw=1, label="No stabilization (1.0×)")
ax.axhline(3.5, color="r", ls="--", lw=1,
           label="Monograph prediction (3.5×)")
for bar, val in zip(bars, stab_vals):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.02,
            f"{val:.3f}×", ha="center", fontsize=11, fontweight="bold")
ax.set_ylabel("Stabilization factor (||ω||_max(true) / ||ω||_max(model))")
ax.set_title("Fig. 16.71  Stabilization factors for 4 b-models (3D NSE, T=2.0)")
ax.legend(fontsize=10)
ax.set_ylim(0, max(stab_vals + [4.0]) * 1.2)
save_fig("fig_16_71_3d_nse_stabilization_bar", fig)

# ====== Figure 16.72: BKM integral ∫||ω||_∞ dt ======
fig, ax = plt.subplots(figsize=(9, 5.5), constrained_layout=True)
for mname in models:
    res = results[mname]
    bkm_integral = np.cumsum(res["omega_max"]) * (res["t_diag"][1] - res["t_diag"][0])
    ax.plot(res["t_diag"], bkm_integral, lw=1.8,
            label=mname, color=colors.get(mname, "gray"))
ax.set_xlabel("Time t")
ax.set_ylabel("∫₀ᵗ ||ω||_∞(s) ds  (BKM integral)")
ax.set_title("Fig. 16.72  BKM criterion integral: finite ⟺ smoothness (Theorem 8.1)")
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)
save_fig("fig_16_72_3d_nse_bkm_integral", fig)

# ====== Figure 16.73: Energy spectrum E(k) at t=T for 5 models ======
fig, ax = plt.subplots(figsize=(10, 6), constrained_layout=True)
k_ref = np.linspace(1, np.max(np.sqrt(K2_safe)) * 0.7, 50)
ax.loglog(k_ref, 0.001 * k_ref ** (-5.0/3.0), "k--", lw=1.5,
          label="Kolmogorov k^(-5/3)")
for mname in models:
    res = results[mname]
    u_final = res["u_final"]
    u_hat_final = np.stack([rfftn(u_final[i]) for i in range(3)])
    k_centers, E_k = energy_spectrum(u_hat_final, np.sqrt(K2_safe), N_bins=15)
    mask = (k_centers > 0.5) & (E_k > 1e-12)
    ax.loglog(k_centers[mask], E_k[mask], "o-", lw=1.5, ms=5,
              label=mname, color=colors.get(mname, "gray"))
ax.set_xlabel("Wavenumber k")
ax.set_ylabel("E(k)")
ax.set_title("Fig. 16.73  Energy spectrum at t=T for 5 models (3D NSE)")
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3, which="both")
save_fig("fig_16_73_3d_nse_energy_spectrum", fig)

# ====== Figure 16.74: vorticity magnitude isosurface (3D viz) ======
fig = plt.figure(figsize=(14, 6), constrained_layout=True)
for idx, mname in enumerate(["true_nse", "b_rodrigues"]):
    ax = fig.add_subplot(1, 2, idx + 1, projection="3d")
    u_final = results[mname]["u_final"]
    u_hat = np.stack([rfftn(u_final[i]) for i in range(3)])
    omega_hat = curl(u_hat, KX, KY, KZ) * dealias
    omega_phys = np.stack([irfftn(omega_hat[i], s=(N, N, N)) for i in range(3)])
    omega_mag = np.sqrt(np.sum(omega_phys ** 2, axis=0))
    threshold = 0.5 * np.max(omega_mag)
    sub = 2
    Xs, Ys, Zs = X[::sub, ::sub, ::sub], Y[::sub, ::sub, ::sub], Z[::sub, ::sub, ::sub]
    Ws = omega_mag[::sub, ::sub, ::sub]
    mask = Ws > threshold
    ax.scatter(Xs[mask], Ys[mask], Zs[mask], c=Ws[mask],
                cmap="hot", s=8, alpha=0.4)
    ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_zlabel("z")
    ax.set_title(f"{mname}\n||ω||_max = {results[mname]['omega_max'][-1]:.3f}",
                 fontsize=11)
    ax.set_xlim(0, 2*np.pi); ax.set_ylim(0, 2*np.pi); ax.set_zlim(0, 2*np.pi)
fig.suptitle("Fig. 16.74  Vorticity magnitude |ω| isosurfaces (50% of max) at t=T\n"
             "Taylor-Green vortex: true NSE vs b-Rodrigues",
             y=1.02, fontsize=12)
save_fig("fig_16_74_3d_nse_vorticity_isosurface", fig)

# ====== Figure 16.75: 3D Rodrigues orthogonality ======
fig, ax = plt.subplots(figsize=(9, 5), constrained_layout=True)
u_hat_0 = np.stack([rfftn(u0[i]) for i in range(3)])
omega_hat_0 = curl(u_hat_0, KX, KY, KZ) * dealias
omega_phys_0 = np.stack([irfftn(omega_hat_0[i], s=(N, N, N)) for i in range(3)])
n_samples = 500
rng = np.random.default_rng(42)
indices = rng.integers(0, N, size=(n_samples, 3))
u_after_all = rodrigues_3d_rotation(u0, omega_phys_0, THETA_B)
norms_before = []
norms_after = []
for ix, iy, iz in indices:
    norms_before.append(np.linalg.norm(u0[:, ix, iy, iz]))
    norms_after.append(np.linalg.norm(u_after_all[:, ix, iy, iz]))
ax.scatter(norms_before, norms_after, s=25, alpha=0.5, color=PALETTE["b_rotation"])
max_norm = max(max(norms_before), max(norms_after)) * 1.1
ax.plot([0, max_norm], [0, max_norm], "k--", lw=1.5,
        label="|R u| = |u| (orthogonality)")
err = max(abs(a - b) for a, b in zip(norms_after, norms_before))
ax.set_xlabel("|u| before rotation")
ax.set_ylabel("|u| after rotation")
ax.set_title(f"Fig. 16.75  3D Rodrigues rotation preserves |u|\n"
             f"(500 random samples, θ_b = {np.degrees(THETA_B):.2f}°, "
             f"max error = {err:.2e})")
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)
save_fig("fig_16_75_3d_rodrigues_orthogonality", fig)

# ====== Figure 16.76: omega_rms (enstrophy) ======
fig, ax = plt.subplots(figsize=(10, 5.5), constrained_layout=True)
for mname in models:
    res = results[mname]
    ax.plot(res["t_diag"], res["omega_rms"], lw=1.6,
            label=mname, color=colors.get(mname, "gray"))
ax.set_xlabel("Time t")
ax.set_ylabel("||ω||_rms(t)")
ax.set_title("Fig. 16.76  RMS vorticity (enstrophy proxy) for 5 models")
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)
save_fig("fig_16_76_3d_nse_omega_rms", fig)

# Save results
RESULTS["E25_E28"] = {
    mname: {
        "label": results[mname]["label"],
        "omega_max_0": float(results[mname]["W0"]),
        "omega_max_T": float(results[mname]["omega_max"][-1]),
        "E_0": float(results[mname]["E0"]),
        "E_T": float(results[mname]["energy"][-1]),
        "stabilization_factor": float(stab[mname]),
        "bkm_integral_T": float(
            np.sum(results[mname]["omega_max"])
            * (results[mname]["t_diag"][1] - results[mname]["t_diag"][0])
        ),
    } for mname in models
}
RESULTS["E25_E28"]["grid"] = {"N": N, "nu": nu, "T": 2.0, "dt": 0.008}
RESULTS_PATH.write_text(json.dumps(RESULTS, indent=2, default=str))
print(f"\nResults saved to {RESULTS_PATH}")
print(f"Total figures: {len(list(FIG_DIR.glob('*.png')))}")
