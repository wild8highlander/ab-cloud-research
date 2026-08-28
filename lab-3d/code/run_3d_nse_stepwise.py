"""Run 3D NSE experiments one model at a time, saving partial results."""
import sys, os, json, time, gc
sys.path.insert(0, "/home/z/my-project/scripts")
import numpy as np
from pathlib import Path

from nse3d_core import (
    make_grid_3d, dealias_mask_3d, taylor_green_vortex, curl,
    integrate_3d_nse, kinetic_energy, vorticity_norm_inf,
)
from scipy.fft import rfftn, irfftn

RESULTS_PATH = Path("/home/z/my-project/download/results.json")
PARTIAL_PATH = Path("/home/z/my-project/download/3d_nse_partial.json")

# Load existing
if PARTIAL_PATH.exists():
    partial = json.loads(PARTIAL_PATH.read_text())
else:
    partial = {"models_done": [], "results": {}}

N = 32
nu = 0.02
x, y, z, X, Y, Z, dx, KX, KY, KZ, K2, K2_safe, K_mag = make_grid_3d(N=N)
dealias = dealias_mask_3d(KX, KY, KZ)
u0 = taylor_green_vortex(X, Y, Z, V0=1.0, k=1)
print(f"Grid: N={N}, nu={nu}", flush=True)

models_to_run = ["true_nse", "b_rodrigues", "b_brake", "b_les", "polchinski_b"]

for mname in models_to_run:
    if mname in partial["models_done"]:
        print(f"[{mname}] already done, skipping", flush=True)
        continue
    print(f"\n[{mname}] T=2.0 ...", flush=True)
    t0 = time.time()
    res = integrate_3d_nse(u0, t_final=2.0, dt=0.008, model_name=mname,
                             X=X, Y=Y, Z=Z, dx=dx, KX=KX, KY=KY, KZ=KZ,
                             K2_safe=K2_safe, dealias=dealias, nu=nu,
                             save_every=10000, diagnose_every=25, verbose=True)
    elapsed = time.time() - t0
    print(f"Elapsed: {elapsed:.1f}s, ||ω||_max(T)={res['omega_max'][-1]:.4f}", flush=True)

    # Save final u field separately as npz
    u_final = res["u_save"][-1].copy()
    np.savez_compressed(f"/home/z/my-project/download/3d_nse_u_final_{mname}.npz",
                         u_final=u_final)
    # Save diagnostics to partial
    partial["results"][mname] = {
        "label": res["label"],
        "t_diag": res["t_diag"].tolist(),
        "omega_max": res["omega_max"].tolist(),
        "omega_rms": res["omega_rms"].tolist(),
        "energy": res["energy"].tolist(),
        "E0": res["E0"], "W0": res["W0"],
    }
    partial["models_done"].append(mname)
    PARTIAL_PATH.write_text(json.dumps(partial, indent=2))
    print(f"Saved partial results for {mname}", flush=True)
    gc.collect()

print("\nAll 5 models complete!", flush=True)
print(f"Results in {PARTIAL_PATH}", flush=True)
