"""
examples/quick_start.py
========================
Quick start example for the AB-Cloud monumental verification codebase.

Shows how to:
1. Build the AB-Cloud Hamiltonian with real vortices
2. Diagonalize and compute GUE statistics
3. Run a parameter sweep
4. Generate a plot
"""
import sys
from pathlib import Path

# Make the lab-3d package importable (code/ is the package; its modules
# use relative imports, so they must be imported as code.<module>)
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from code.ab_cloud_hamiltonian_v2 import build_ab_cloud_hamiltonian, default_vortex_config
from code.ab_cloud_stats_v2 import spacing_ratios, mean_spacing_ratio, R_GUE
from code.ab_cloud_sweeps_v2 import sweep_alpha, DEFAULT_ALPHA_GRID
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    print("=" * 60)
    print("AB-Cloud Monumental — Quick Start Example")
    print("=" * 60)

    # 1. Build the Hamiltonian at the monograph's optimal point
    print("\n1. Building AB-Cloud Hamiltonian at alpha=1/2, W=2, L=56...")
    L, alpha, W, sigma = 56, 0.5, 2.0, 0.5
    cfg = default_vortex_config(L, alpha, seed=0)
    print(f"   Vortex config: {cfg.n_vortices} vortices, "
          f"charges={cfg.charges}, positions={cfg.positions}")

    H = build_ab_cloud_hamiltonian(L, alpha, W=W, sigma=sigma, seed=0)
    print(f"   H shape: {H.shape}, Hermitian: {np.allclose(H, H.conj().T)}")

    # 2. Diagonalize and compute central <r>
    print("\n2. Diagonalizing...")
    eigs = np.linalg.eigvalsh(H)
    print(f"   Eigenvalues: n={len(eigs)}, min={eigs.min():.4f}, max={eigs.max():.4f}")

    # Central window
    e0, e1 = np.percentile(eigs, [35, 65])
    central = eigs[(eigs >= e0) & (eigs <= e1)]
    r = spacing_ratios(central)
    mr = float(np.mean(r))
    print(f"   Central <r> = {mr:.4f}")
    print(f"   GUE reference: {R_GUE}")
    print(f"   Passes GUE (within 0.05): {abs(mr - R_GUE) < 0.05}")

    # 3. Run a small sweep over alpha
    print("\n3. Running alpha sweep (L=42, n_realizations=2)...")
    res = sweep_alpha(L=42, W=2.0, sigma=0.5, n_realizations=2,
                      alpha_grid=DEFAULT_ALPHA_GRID[:8])  # First 8 alphas only
    print(f"   Sweep took {res.elapsed_seconds:.1f}s")
    print(f"   <r> vs alpha:")
    for a, r in zip(res.param_values[0], res.statistics["r_mean"]):
        print(f"     alpha={a:.4f}  <r>={r:.4f}")

    # 4. Generate plot (inline matplotlib; figures land in code/figs/)
    print("\n4. Generating plot...")
    outdir = Path(__file__).resolve().parent / "figs"
    outdir.mkdir(exist_ok=True)
    fig, ax = plt.subplots(figsize=(7.0, 4.2))
    ax.errorbar(res.param_values[0], res.statistics["r_mean"],
                yerr=res.std_errors.get("r_mean"), fmt="o-", capsize=3,
                color="#0E7C86", label="AB-Cloud $\\langle r\\rangle$")
    ax.axhline(R_GUE, color="k", ls="--", lw=1.0, label="GUE 0.5996")
    ax.set_xlabel(r"$\alpha$ (flux per plaquette)")
    ax.set_ylabel(r"$\langle r \rangle$")
    ax.set_title("AB-Cloud quick start: alpha sweep")
    ax.legend()
    fig.tight_layout()
    plot_path = outdir / "quick_start_sweep_alpha.png"
    fig.savefig(plot_path, dpi=150)
    plt.close(fig)
    print(f"   Saved: {plot_path}")

    print("\n" + "=" * 60)
    print("Done! See code/figs/ for the generated figure.")
    print("=" * 60)


if __name__ == "__main__":
    main()
