"""Sanity-тест порта: эрмитовость, поток ячейки, KS-согласование, развёртка."""
import numpy as np
import sys
sys.path.insert(0, "/home/z/my-project/scripts")
import t34_engine as E
from t34_engine import (build_ab_cloud_hamiltonian, random_vortex_configuration,
                        ks2sample, unfold_spacings, central_band_eigs,
                        normalized_spacings, load_zeta, run_config, gue_control)

from scipy.linalg import eigvalsh
from scipy.stats import ks_2samp

rng = np.random.default_rng(5)

# 1) Эрмитовость и поток ячейки без вихрей (α=1/4, торус α·Ny=3∈ℤ)
L = 12
vort = []
dis = np.random.default_rng(0)
H = build_ab_cloud_hamiltonian(L, L, vort, 0.25, 1.0, 0.0, "torus", dis)
herm = np.max(np.abs(H - H.conj().T))
print(f"1) herm defect (no vortex): {herm:.2e}")

def plaquette_flux(H, L):
    def idx(x, y): return (x % L) * L + (y % L)
    F = np.zeros((L, L))
    for x in range(L):
        for y in range(L):
            i, j = idx(x, y), idx(x + 1, y)
            k, l = idx(x + 1, y + 1), idx(x, y + 1)
            P = H[i, j] * H[j, k] * np.conj(H[l, k]) * np.conj(H[i, l])
            F[x, y] = np.angle(P) / (2 * np.pi)
    return F

F = plaquette_flux(H, L)
print(f"   plaquette flux (torus α=1/4): min {F.min():.6f} max {F.max():.6f} (ожидание ±0.25)")
H = build_ab_cloud_hamiltonian(L, L, vort, 0.3, 1.0, 0.0, "open", dis)
F = plaquette_flux(H, L)
print(f"   open α=0.3: flux min {F.min():.6f} max {F.max():.6f} (ожидание ±0.3)")

# 2) Вихрь: monumental smooth gauge — поток локализован у вихря, интеграл = q
vort = [(6.5, 6.5, 1.0)]           # центр ячейки F[5,5] (0-based)
H2 = build_ab_cloud_hamiltonian(L, L, vort, 0.0, 1.0, 0.0, "open", dis)
F2 = plaquette_flux(H2, L)
kmax = np.unravel_index(np.argmax(np.abs(F2)), F2.shape)
print(f"2) vortex q=1: |flux| max {np.abs(F2).max():.4f} at {kmax} (vortex cell [5,5]), "
      f"sum(|F|) near vortex {np.abs(F2[4:8, 4:8]).sum():.4f}, far {np.abs(F2[0:3, 0:3]).max():.4f}")
# monumental: поток РАСПРЕДЕЛён по соседним ячейкам (докстринг модели),
# интеграл по окрестности вихря → ±q (Byers-Yang); вдали от вихря ≈ 0

# 3) KS vs scipy
x = rng.normal(0, 1, 3000); y = rng.normal(0.1, 1, 2000)
D1, p1 = ks2sample(x, y)
r = ks_2samp(x, y, method="asymp")
print(f"3) ks2sample D={D1:.5f} p={p1:.5f} | scipy D={r.statistic:.5f} p={r.pvalue:.5f}")
assert abs(D1 - r.statistic) < 1e-12, "KS D mismatch!"

# 4) ζ-развёртка
zs = load_zeta("/home/z/my-project/ab-cloud-research/verification/data/zeta_zeros_50000_embedded.txt")
print(f"4) ζ: {len(zs)} zeros; unfolded {len(E.ZETA_UNF)} spacings, mean={E.ZETA_UNF.mean():.6f}")

# 5) Полный прогон маленькой конфигурации (L=24, Nv=2, q=1)
res = run_config(2, 1.0, 1.0, 0.5, 24, "open", n_real=3)
print(f"5) L=24 Nv=2 q=1 W=1: D={res['D_pooled']:.4f} p={res['p_pooled']:.3g} "
      f"⟨r⟩={res['r_mean']:.4f} n_sp={res['n_spacings']} "
      f"dR2={res['mean_abs_dR2']:.4f} dGUE={res['d_GUE']:.4f} dPois={res['d_Pois']:.4f} "
      f"[{res['runtime_s']:.1f}s]")

# 6) GUE-контроль
ctl = gue_control(24, n_real=2)
print(f"6) GUE control L=24: D={ctl['D_gue_vs_zeta']:.4f} "
      f"R2cal={ctl['mean_abs_dR2_cal']:.4f} R2vsζ={ctl['mean_abs_dR2_vs_zeta']:.4f}")
