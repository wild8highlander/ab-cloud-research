"""
examples/large_matrix_demo.py
==============================
Demonstration of large-matrix AB-Cloud verification (L=70, 84).

Shows:
1. Building L=70 and L=84 Hamiltonians (monumental matrices)
2. Computing <r> at the optimal point
3. Comparing with GUE reference
4. Generating Hofstadter butterfly
5. Computing spectral form factor K(t)
"""
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from python.ab_cloud_hamiltonian import build_ab_cloud_hamiltonian, build_pure_hofstadter
from python.ab_cloud_stats import (
    spacing_ratios, mean_spacing_ratio, polynomial_unfold,
    spectral_form_factor, R_GUE, R_POISSON,
)
from python.ab_cloud_plots import (
    plot_hofstadter_butterfly, plot_spectral_form_factor_long,
)
import numpy as np


def main():
    print("=" * 60)
    print("AB-Cloud Monumental — Large Matrix Demo")
    print("=" * 60)

    # 1. L=70 verification
    print("\n1. L=70 verification at alpha=1/2, W=2...")
    t0 = time.time()
    H = build_ab_cloud_hamiltonian(L=70, alpha=0.5, W=2.0, sigma=0.5, seed=0)
    eigs = np.linalg.eigvalsh(H)
    elapsed = time.time() - t0
    print(f"   Build + eig: {elapsed:.1f}s")

    e0, e1 = np.percentile(eigs, [35, 65])
    central = eigs[(eigs >= e0) & (eigs <= e1)]
    r = spacing_ratios(central)
    mr = float(np.mean(r))
    print(f"   <r> = {mr:.4f}  (GUE = {R_GUE})")

    # 2. L=84 verification
    print("\n2. L=84 verification at alpha=1/2, W=2...")
    t0 = time.time()
    H = build_ab_cloud_hamiltonian(L=84, alpha=0.5, W=2.0, sigma=0.5, seed=0)
    eigs = np.linalg.eigvalsh(H)
    elapsed = time.time() - t0
    print(f"   Build + eig: {elapsed:.1f}s")

    e0, e1 = np.percentile(eigs, [35, 65])
    central = eigs[(eigs >= e0) & (eigs <= e1)]
    r = spacing_ratios(central)
    mr = float(np.mean(r))
    print(f"   <r> = {mr:.4f}  (GUE = {R_GUE})")

    # 3. Hofstadter butterfly
    print("\n3. Generating Hofstadter butterfly (L=50, 100 alpha values)...")
    path = plot_hofstadter_butterfly(L=50, n_alpha=100, name="large_demo_butterfly")
    print(f"   Saved: {path}")

    # 4. Spectral form factor at L=56
    print("\n4. Spectral form factor at L=56, alpha=1/2...")
    H = build_ab_cloud_hamiltonian(L=56, alpha=0.5, W=2.0, sigma=0.5, seed=0)
    eigs = np.linalg.eigvalsh(H)
    xi = polynomial_unfold(eigs)
    ts, K = spectral_form_factor(xi, t_max=10, n_t=80)
    print(f"   K(t=0.5) = {K[5]:.4f}  (GUE ~ 0.5)")
    print(f"   K(t=2.0) = {K[40]:.4f}  (GUE plateau ~ 1)")

    print("\n" + "=" * 60)
    print("Done!")
    print("=" * 60)


if __name__ == "__main__":
    main()
