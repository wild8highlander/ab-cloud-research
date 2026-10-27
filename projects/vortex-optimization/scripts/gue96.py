"""GUE-контроль L=96 standalone v2: построчная сборка эрмитовой матрицы,
пик памяти ≈ 1.4 ГБ (только F-матрица), никаких треугольных индексов."""
import json
import sys
import time

import numpy as np
sys.path.insert(0, "/home/z/my-project/scripts")
import t34_engine as E
from scipy.linalg import eigvalsh

OUT = "/home/z/my-project/download/t34_research"
E.load_zeta("/home/z/my-project/ab-cloud-research/verification/data/zeta_zeros_50000_embedded.txt")

n = 96 * 96
sps = []
for k in (1, 2):
    t0 = time.perf_counter()
    rng = np.random.default_rng(777000 + k)
    H = np.zeros((n, n), dtype=np.complex128, order="F")
    for i in range(n):
        m = n - i
        re = rng.standard_normal(m)
        im = rng.standard_normal(m)
        row = re + 1j * im
        H[i, i:] = row
        if i + 1 < n:
            H[i + 1:, i] = row[1:].conj()   # нижний треугольник = сопряжённый
    ev = np.sort(eigvalsh(H, check_finite=False, driver="evr",
                          overwrite_a=True))
    del H
    central = E.central_band_eigs(ev, E.CENTER_FRACTION)
    sp = E.unfold_spacings(central)
    sps.append(sp / sp.mean())
    print(f"real {k}: {len(sp)} spacings [{time.perf_counter()-t0:.0f}s]",
          flush=True)

pooled = np.concatenate(sps)
D, p = E.ks2sample(pooled, E.ZETA_UNF)
pos = np.concatenate(([0.0], np.cumsum(pooled)))
s_grid, R2_g = E.pair_corr_R2(pos, 4.0, 0.05)
R2t = 1.0 - (np.sin(np.pi * s_grid) / (np.pi * s_grid)) ** 2
res = {"L": 96, "n_real": 2, "n_spacings": int(len(pooled)),
       "D_gue_vs_zeta": float(D), "p": float(p),
       "mean_abs_dR2_cal": float(np.mean(np.abs(R2_g - R2t))),
       "mean_abs_dR2_vs_zeta": float(np.mean(np.abs(R2_g - E.R2_ZETA_CACHE)))}
with open(f"{OUT}/gue_control_L96.json", "w") as f:
    json.dump(res, f, indent=1)
print("GUE-контроль L=96:", res)
