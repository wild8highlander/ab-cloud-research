"""Quick re-run of E6, E9, E10, E12 to save numerical summary data."""
import sys, os, json, time
sys.path.insert(0, "/home/z/my-project/scripts")
import numpy as np
from pathlib import Path

from kdv_core import (
    THETA_B, make_grid, dealias_mask, single_soliton, two_solitons,
    invariants, MODELS, integrate, apply_M2_rodrigues,
    two_soliton_phase_shifts, ifrk4_step, _nonlinear_term_true,
)
from scipy.fft import fft, ifft
from run_experiments import RESULTS, RESULTS_PATH

# E9 — 7-model comparison summary (T=15)
def rerun_E9():
    print("\n[Rerun E9] 7-model comparison, T=15 ...")
    x, dx, k = make_grid(L=120.0, N=512)
    dealias = dealias_mask(k)
    c = 0.6
    u0 = single_soliton(x, c, x0=-30.0)
    summary = {}
    for mname in ["true_kdv", "b_rotation", "b_rodrigues", "b_modified",
                  "b_brake", "b_linear", "b_les"]:
        t0 = time.time()
        res = integrate(u0, t_final=15.0, dt=0.002, model_name=mname,
                        k=k, dealias=dealias, save_every=2000,
                        diagnose_every=2000, verbose=False)
        elapsed = time.time() - t0
        summary[mname] = {
            "label": res["label"],
            "max_u": float(np.max(res["umax"])),
            "drift_M": float(abs(res["M"][-1] - res["M0"]) / abs(res["M0"])),
            "drift_P": float(abs(res["P"][-1] - res["P0"]) / abs(res["P0"])),
            "drift_E": float(abs(res["E"][-1] - res["E0"]) / abs(res["E0"])),
            "dissipation": bool(MODELS[mname][3]),
            "elapsed_s": float(elapsed),
        }
        print(f"  {mname:14s}  max={summary[mname]['max_u']:.4f}  "
              f"drift_E={summary[mname]['drift_E']:.2e}")
    RESULTS["E9"] = summary

# E6 — collision with b, summary
def rerun_E6():
    print("\n[Rerun E6] 2-soliton collision with M1/M2/M3 ...")
    x, dx, k = make_grid(L=120.0, N=512)
    dealias = dealias_mask(k)
    c1, c2 = 0.8, 0.4
    u0 = two_solitons(x, c1, c2, x1=-30.0, x2=10.0)
    summary = {}
    for mech, model_key in [("M1", "b_rotation"), ("M2", "b_rodrigues"),
                             ("M3", "b_modified")]:
        res = integrate(u0, t_final=30.0, dt=0.002, model_name=model_key,
                        k=k, dealias=dealias, save_every=2000,
                        diagnose_every=2000, verbose=False)
        summary[mech] = {
            "max_u": float(np.max(res["umax"])),
            "drift_E": float(abs(res["E"][-1] - res["E0"]) / abs(res["E0"])),
        }
        print(f"  {mech}  max={summary[mech]['max_u']:.4f}  "
              f"drift_E={summary[mech]['drift_E']:.2e}")
    # Baseline
    res_base = integrate(u0, t_final=30.0, dt=0.002, model_name="true_kdv",
                         k=k, dealias=dealias, save_every=2000,
                         diagnose_every=2000, verbose=False)
    summary["baseline"] = {
        "max_u": float(np.max(res_base["umax"])),
        "drift_E": float(abs(res_base["E"][-1] - res_base["E0"]) / abs(res_base["E0"])),
    }
    print(f"  baseline  max={summary['baseline']['max_u']:.4f}  "
          f"drift_E={summary['baseline']['drift_E']:.2e}")
    RESULTS["E6"] = summary

# E10 — angle scan summary
def rerun_E10():
    print("\n[Rerun E10] 12-angle scan ...")
    x, dx, k = make_grid(L=100.0, N=256)
    dealias = dealias_mask(k)
    c = 0.5
    u0 = single_soliton(x, c, x0=-20.0)
    angle_multipliers = [0, 0.5, 1, 2, 3, 4, 6, 8, 12, 16, 24, 32]
    drift_M_list, drift_P_list, drift_E_list, form_drift_list = [], [], [], []
    t_final = 10.0
    dt = 0.002
    n_steps = int(t_final / dt)
    M0, P0, E0 = invariants(u0, dx, k)
    x_final_expected = -20 + 4 * c * c * t_final
    u_sol = single_soliton(x, c, x0=x_final_expected)

    for mult in angle_multipliers:
        theta_eff = mult * THETA_B
        per_step = dt * theta_eff
        u = u0.copy()
        for step in range(1, n_steps + 1):
            t_now = (step - 1) * dt
            u = ifrk4_step(u, dt, t_now, _nonlinear_term_true,
                           k, dealias, 1.0, theta_eff)
            u = apply_M2_rodrigues(u, per_step, k)
            u = np.real(ifft(fft(u) * dealias))
        M_f, P_f, E_f = invariants(u, dx, k)
        fd = np.linalg.norm(u - u_sol) / np.linalg.norm(u_sol)
        drift_M_list.append(float(abs(M_f - M0) / abs(M0)))
        drift_P_list.append(float(abs(P_f - P0) / abs(P0)))
        drift_E_list.append(float(abs(E_f - E0) / abs(E0)))
        form_drift_list.append(float(fd))
    RESULTS["E10"] = {
        "angle_multipliers": angle_multipliers,
        "angles_deg": [float(np.degrees(m * THETA_B)) for m in angle_multipliers],
        "drift_M": drift_M_list,
        "drift_P": drift_P_list,
        "drift_E": drift_E_list,
        "form_drift": form_drift_list,
    }
    print(f"  Done. min form_drift at mult="
          f"{angle_multipliers[np.argmin(form_drift_list)]}")

# E12 — long-time summary
def rerun_E12():
    print("\n[Rerun E12] Long-time T=50, 5 models ...")
    x, dx, k = make_grid(L=150.0, N=512)
    dealias = dealias_mask(k)
    c = 0.5
    u0 = single_soliton(x, c, x0=-60.0)
    summary = {}
    for mname in ["true_kdv", "b_rodrigues", "b_brake", "b_linear", "b_les"]:
        t0 = time.time()
        res = integrate(u0, t_final=50.0, dt=0.002, model_name=mname,
                        k=k, dealias=dealias, save_every=5000,
                        diagnose_every=5000, verbose=False)
        elapsed = time.time() - t0
        summary[mname] = {
            "max_u": float(np.max(res["umax"])),
            "drift_M": float(abs(res["M"][-1] - res["M0"]) / abs(res["M0"])),
            "drift_P": float(abs(res["P"][-1] - res["P0"]) / abs(res["P0"])),
            "drift_E": float(abs(res["E"][-1] - res["E0"]) / abs(res["E0"])),
            "elapsed_s": float(elapsed),
        }
        print(f"  {mname:14s}  max={summary[mname]['max_u']:.4f}  "
              f"drift_E={summary[mname]['drift_E']:.2e}")
    RESULTS["E12"] = summary

if __name__ == "__main__":
    rerun_E9()
    rerun_E6()
    rerun_E10()
    rerun_E12()
    RESULTS_PATH.write_text(json.dumps(RESULTS, indent=2, default=str))
    print(f"\nAll results saved to {RESULTS_PATH}")
