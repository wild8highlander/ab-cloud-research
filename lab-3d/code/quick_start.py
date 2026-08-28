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

# Make package importable
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from python.ab_cloud_hamiltonian import build_ab_cloud_hamiltonian, default_vortex_config
from python.ab_cloud_stats import spacing_ratios, mean_spacing_ratio, R_GUE
from python.ab_cloud_sweeps import sweep_alpha, DEFAULT_ALPHA_GRID
from python.ab_cloud_plots import plot_sweep_alpha
import numpy as np


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

    # 4. Generate plot
    print("\n4. Generating plot...")
    plot_path = plot_sweep_alpha(res, name="quick_start_sweep_alpha")
    print(f"   Saved: {plot_path}")

    print("\n" + "=" * 60)
    print("Done! See results/plots/ for the generated figure.")
    print("=" * 60)


if __name__ == "__main__":
    main()
