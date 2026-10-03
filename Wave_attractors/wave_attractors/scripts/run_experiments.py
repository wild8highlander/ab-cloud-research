#!/usr/bin/env python3
"""
run_experiments.py — Experimental programme of study W1
(Hyperbolic wave attractors, numerical reproduction).

Experiments
-----------
E1  Wavelength cascade     : |k| growth at slope reflections and geometric
                             convergence of rays onto the attractor loop.
E2  Material control       : hyperbolic vs isotropic medium in the same
                             chamber — attractor vs no attractor.
E3  Chirality              : chamber vs its mirror image — the sense of
                             circulation of the attractor loop flips.
E4  Frequency independence : ray map is omega-independent by construction;
                             the wave-level counterpart is tested by
                             wave_helmholtz.py (see report Section 6).
E5  Attractor phase diagram: fraction of rays converging to closed loops /
                             runaway cascades / regular channels across the
                             (slope s, vertical-wall extent y_v) plane —
                             the "attractor phase transitions" of the
                             reference study.

Outputs: data/*.csv and data/*.json (consumed by make_figures.py and
verify_cross.py).

Usage:
    python3 run_experiments.py           # full protocol
    python3 run_experiments.py --quick   # reduced protocol (CI)
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ray_billiard import (Chamber, Medium, chirality_index, chamber_hexagon,
                          chamber_hexagon_asym, distance_to_loop, propagate_ray)

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.normpath(os.path.join(HERE, "..", "data"))
os.makedirs(DATA, exist_ok=True)

ETA = 100.0
HYP = Medium("hyperbolic", eta=ETA)
ISO = Medium("isotropic")

# reference chamber: hexagon with shallow bottom-corner slopes
# (asymmetric: s_left != s_right selects a genuine mirror pair for E3)
S_LEFT = 0.03
S_RIGHT = 0.06
Y_V = 0.35          # vertical-wall lower end; slopes span y in [0, Y_V]
CH = chamber_hexagon_asym(s_left=S_LEFT, s_right=S_RIGHT, y_v=Y_V)
CH_MIR = None       # mirror built around the chamber centre (see below)


def mirrored(ch: Chamber) -> Chamber:
    v = ch.vertices.copy()
    xc = 0.5 * (v[:, 0].min() + v[:, 0].max())
    v[:, 0] = 2.0 * xc - v[:, 0]
    return Chamber(vertices=v[::-1], name=ch.name + "_mirrored")


CH_MIR = mirrored(CH)

SLOPE_EDGES = (2, 4)   # hexagon wall indices of the two shallow slopes


def launch_rng(seed: int) -> np.random.Generator:
    return np.random.default_rng(seed)


def sample_ray(rng: np.random.Generator, med: Medium) -> tuple[np.ndarray, np.ndarray]:
    p0 = np.array([0.25 + 0.5 * rng.uniform(), 0.85])
    kx = rng.uniform(-1.5, 1.5)
    if med.kind == "hyperbolic":
        ky = math.sqrt(1.0 + kx * kx / med.eta)
    else:
        ky = math.sqrt(max(1e-6, 1.0 - 0.3 * kx * kx))
    k0 = np.array([kx, -ky])          # launched downward
    return p0, k0


def has_attractor_loop(res, min_walls: int = 4) -> bool:
    if res.closed_loop is None:
        return False
    m = res.period
    return len(set(res.edges[-m:])) >= min_walls


# ----------------------------------------------------------------------------
# E1 — cascade
# ----------------------------------------------------------------------------
def e1_cascade(n_rays: int, max_bounces: int) -> dict:
    """|k| growth at slope reflections + geometric convergence to the loop.

    The wavelength cascade lives in the TRANSIENT (approach) phase: early
    slope reflections grow |k| geometrically; at the locked attractor the
    slope map has reached its fixed point and the ratio saturates at 1.
    We therefore report transient (bounce < TRANSIENT_BOUNCES) and steady
    statistics separately.
    """
    t0 = time.time()
    TRANSIENT_BOUNCES = 300
    rows = []          # per slope-hit records
    conv_rows = []     # per-ray convergence summaries
    ref_res = None

    for ir in range(n_rays):
        rng = launch_rng(1000 + ir)
        p0, k0 = sample_ray(rng, HYP)
        res = propagate_ray(CH, HYP, p0, k0, 1.0, max_bounces=max_bounces,
                            loop_tol=1e-7, loop_window=100)
        if ir == 0:
            ref_res = res
        kh = res.k_history
        for i, e in enumerate(res.edges):
            if e in SLOPE_EDGES and i > 0 and i + 1 < len(kh):
                kb = np.hypot(*kh[i])
                ka = np.hypot(*kh[i + 1])
                rows.append((ir, i, e, kb, ka, ka / kb,
                             "transient" if i < TRANSIENT_BOUNCES else "steady"))
        if has_attractor_loop(res):
            loop = res.closed_loop
            n = len(res.bounce_points)
            d = np.array([distance_to_loop(p, loop)
                          for p in res.bounce_points[: n - res.period]])
            idx = np.arange(len(d))
            mask = d > 1e-12
            if mask.sum() > 12:
                coef = np.polyfit(idx[mask], np.log(d[mask]), 1)
                q = math.exp(coef[0])
                conv_rows.append((ir, res.period, q, float(d[mask].max()),
                                  float(d[mask].min())))
        else:
            conv_rows.append((ir, 0, float("nan"), float("nan"), float("nan")))

    with open(os.path.join(DATA, "E1_cascade_slope_hits.csv"), "w",
              newline="") as f:
        w = csv.writer(f)
        w.writerow(["ray", "bounce", "edge", "k_before", "k_after", "ratio",
                    "phase"])
        w.writerows(rows)
    with open(os.path.join(DATA, "E1_convergence.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["ray", "period", "q_fit", "d_max", "d_min"])
        w.writerows(conv_rows)

    ratios_tr = np.array([r[5] for r in rows if r[6] == "transient"])
    ratios_st = np.array([r[5] for r in rows if r[6] == "steady"])
    qs = np.array([c[2] for c in conv_rows if np.isfinite(c[2])])
    out = {
        "n_rays": n_rays,
        "n_slope_hits_transient": int(len(ratios_tr)),
        "ratio_transient_mean": (float(ratios_tr.mean())
                                 if len(ratios_tr) else None),
        "ratio_transient_max": (float(ratios_tr.max())
                                if len(ratios_tr) else None),
        "ratio_steady_mean": (float(ratios_st.mean())
                              if len(ratios_st) else None),
        "q_fit_median": float(np.median(qs)) if len(qs) else None,
        "n_converged": len(qs),
        "ref_period": ref_res.period if ref_res else 0,
        "runtime_s": round(time.time() - t0, 2),
    }
    with open(os.path.join(DATA, "E1_summary.json"), "w") as f:
        json.dump(out, f, indent=2)
    return out


# ----------------------------------------------------------------------------
# E2 — material control
# ----------------------------------------------------------------------------
def e2_control(n_rays: int, max_bounces: int) -> dict:
    """Attractor convergence: hyperbolic vs isotropic, same chamber."""
    t0 = time.time()
    rows = []
    summary = {}
    for label, med in (("hyperbolic", HYP), ("isotropic", ISO)):
        n_loop = 0
        occ = []
        for ir in range(n_rays):
            rng = launch_rng(2000 + ir)
            p0, k0 = sample_ray(rng, med)
            res = propagate_ray(CH, med, p0, k0, 1.0, max_bounces=max_bounces,
                                loop_tol=1e-7, loop_window=100)
            hit = 1 if has_attractor_loop(res) else 0
            n_loop += hit
            rows.append((label, ir, hit, res.period))
            # occupation: fraction of the last 200 bounces close to the ray's
            # own loop (hyperbolic) — for isotropic we measure loop closure
            # frequency as well; the contrast is the physics.
        summary[label] = {
            "n_rays": n_rays,
            "n_attractor": n_loop,
            "fraction": n_loop / n_rays,
        }
    with open(os.path.join(DATA, "E2_control.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["medium", "ray", "loop_found", "period"])
        w.writerows(rows)
    summary["runtime_s"] = round(time.time() - t0, 2)
    with open(os.path.join(DATA, "E2_summary.json"), "w") as f:
        json.dump(summary, f, indent=2)
    return summary


# ----------------------------------------------------------------------------
# E3 — chirality
# ----------------------------------------------------------------------------
def mirror_ic(p0: np.ndarray, k0: np.ndarray,
              xc: float) -> tuple[np.ndarray, np.ndarray]:
    """Mirror an initial condition across the vertical line x = xc."""
    pm = p0.copy()
    pm[0] = 2.0 * xc - pm[0]
    km = k0.copy()
    km[0] = -km[0]
    return pm, km


def e3_chirality(n_rays: int, max_bounces: int) -> dict:
    """Chirality of the attractor loops.

    Two tests:
    (1) deterministic mirror test — the mirror-image chamber with the
        mirror-image initial condition hosts the mirror-image loop, whose
        chirality index is exactly the opposite of the original one;
    (2) basin census — across many launched rays the two circulation
        senses +/- C coexist (spontaneous selection of the winding sense
        by the initial condition); the census is mirror-symmetric.
    """
    t0 = time.time()
    v = CH.vertices
    xc = 0.5 * (v[:, 0].min() + v[:, 0].max())
    ch_m = CH_MIR

    rows = []
    mirror_ok = 0
    n_pairs = 0
    hausdorff = []
    census = []
    for ir in range(n_rays):
        rng = launch_rng(3000 + ir)
        p0, k0 = sample_ray(rng, HYP)
        res = propagate_ray(CH, HYP, p0, k0, 1.0, max_bounces=max_bounces,
                            loop_tol=1e-7, loop_window=100)
        if not has_attractor_loop(res):
            census.append((ir, None, 0))
            continue
        c = chirality_index(res.closed_loop)
        census.append((ir, c, res.period))
        # deterministic mirror pair
        pm, km = mirror_ic(p0, k0, xc)
        res_m = propagate_ray(ch_m, HYP, pm, km, 1.0, max_bounces=max_bounces,
                              loop_tol=1e-7, loop_window=100)
        if has_attractor_loop(res_m):
            c_m = chirality_index(res_m.closed_loop)
            n_pairs += 1
            # geometric identity: mirror(loop) == loop_mirrored
            vmm = res_m.closed_loop.copy()
            vmm[:, 0] = 2.0 * xc - vmm[:, 0]
            # Hausdorff distance (symmetric, via point-to-polyline distance)
            d1 = max(distance_to_loop(p, res.closed_loop) for p in vmm)
            d2 = max(distance_to_loop(p, vmm) for p in res.closed_loop)
            hd = max(d1, d2)
            hausdorff.append(hd)
            rows.append((ir, c, c_m, float(hd)))

    cs = np.array([c for _, c, _ in census if c is not None])
    c_pairs = np.array([r[1] for r in rows])
    c_pairs_m = np.array([r[2] for r in rows])
    out = {
        "n_rays": n_rays,
        "n_loops_census": int(len(cs)),
        "census_mean": float(cs.mean()) if len(cs) else None,
        "census_std": float(cs.std()) if len(cs) else None,
        "n_mirror_pairs": n_pairs,
        "mirror_chirality_flip": bool(np.all(np.sign(c_pairs) !=
                                             np.sign(c_pairs_m))) if n_pairs else False,
        "mirror_chirality_sum_max": (float(np.max(np.abs(c_pairs + c_pairs_m)))
                                     if n_pairs else None),
        "mirror_hausdorff_max": float(np.max(hausdorff)) if hausdorff else None,
    }
    with open(os.path.join(DATA, "E3_chirality.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["ray", "chirality_original", "chirality_mirrored",
                    "hausdorff_mirror_loop"])
        w.writerows(rows)
    out["runtime_s"] = round(time.time() - t0, 2)
    with open(os.path.join(DATA, "E3_summary.json"), "w") as f:
        json.dump(out, f, indent=2)
    return out


# ----------------------------------------------------------------------------
# E5 — attractor phase diagram
# ----------------------------------------------------------------------------
def e5_phase_diagram(n_rays: int, max_bounces: int) -> dict:
    t0 = time.time()
    s_values = [0.02, 0.03, 0.05, 0.08, 0.12]
    yv_values = [0.15, 0.25, 0.35, 0.50, 0.65]
    grid = []
    for s in s_values:
        for yv in yv_values:
            ch = chamber_hexagon(s=s, y_v=yv)
            n_loop = n_corner = 0
            for ir in range(n_rays):
                rng = launch_rng(5000 + ir)
                p0, k0 = sample_ray(rng, HYP)
                try:
                    res = propagate_ray(ch, HYP, p0, k0, 1.0,
                                        max_bounces=max_bounces,
                                        loop_tol=1e-7, loop_window=100)
                except RuntimeError:
                    n_corner += 1
                    continue
                if has_attractor_loop(res):
                    n_loop += 1
            grid.append((s, yv, n_loop, n_corner, n_rays - n_loop - n_corner))
            print(f"  E5 s={s:.2f} y_v={yv:.2f}: loop={n_loop} "
                  f"corner={n_corner} chan={n_rays - n_loop - n_corner}",
                  flush=True)
    with open(os.path.join(DATA, "E5_phase_diagram.csv"), "w",
              newline="") as f:
        w = csv.writer(f)
        w.writerow(["s_slope", "y_v", "n_loop", "n_corner", "n_channel"])
        w.writerows(grid)
    out = {"s_values": s_values, "yv_values": yv_values,
           "n_rays": n_rays, "runtime_s": round(time.time() - t0, 2)}
    with open(os.path.join(DATA, "E5_summary.json"), "w") as f:
        json.dump(out, f, indent=2)
    return out


# ----------------------------------------------------------------------------
# Cross-verification dataset (Python reference for the Julia port)
# ----------------------------------------------------------------------------
def dump_cross_reference(n_rays: int, max_bounces: int) -> dict:
    """Reference dataset consumed by verify_cross.py (Python vs Julia)."""
    t0 = time.time()
    rays = []
    for ir in range(n_rays):
        rng = launch_rng(7000 + ir)
        p0, k0 = sample_ray(rng, HYP)
        res = propagate_ray(CH, HYP, p0, k0, 1.0, max_bounces=max_bounces,
                            loop_tol=1e-7, loop_window=100)
        rec = {
            "ray": ir,
            "p0": p0.tolist(),
            "k0": k0.tolist(),
            "n_bounces": int(len(res.edges)),
            "final_k": res.k_history[-1].tolist(),
            "period": int(res.period),
            "loop_found": bool(res.closed_loop is not None),
            "chirality": (chirality_index(res.closed_loop)
                          if res.closed_loop is not None else None),
            "last_loop_points": (res.closed_loop.tolist()
                                 if res.closed_loop is not None else None),
            "crashed": False,
        }
        rays.append(rec)
    out = {
        "eta": ETA,
        "chamber": {"name": CH.name,
                    "vertices": CH.vertices.tolist()},
        "protocol": {"n_rays": n_rays, "max_bounces": max_bounces,
                     "loop_tol": 1e-7, "loop_window": 100},
        "rays": rays,
        "runtime_s": round(time.time() - t0, 2),
    }
    with open(os.path.join(DATA, "rays_python.json"), "w") as f:
        json.dump(out, f, indent=1)
    return {"n_rays": n_rays}


# ----------------------------------------------------------------------------
def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--quick", action="store_true",
                    help="reduced protocol for CI")
    args = ap.parse_args()

    if args.quick:
        n_rays, max_bounces, n_phase = 8, 800, 4
    else:
        n_rays, max_bounces, n_phase = 24, 1600, 6

    print(f"[W1] protocol: n_rays={n_rays}, max_bounces={max_bounces}",
          flush=True)
    print("[W1] E1 cascade...", flush=True)
    r1 = e1_cascade(n_rays, max_bounces)
    print("     ", json.dumps(r1), flush=True)
    print("[W1] E2 control...", flush=True)
    r2 = e2_control(n_rays, max_bounces)
    print("     ", json.dumps(r2), flush=True)
    print("[W1] E3 chirality...", flush=True)
    r3 = e3_chirality(n_rays, max_bounces)
    print("     ", json.dumps(r3), flush=True)
    print("[W1] E5 phase diagram...", flush=True)
    r5 = e5_phase_diagram(n_phase, max_bounces)
    print("     ", json.dumps(r5), flush=True)
    print("[W1] cross-reference dump...", flush=True)
    r4 = dump_cross_reference(min(n_rays, 12), max_bounces)
    print("     ", json.dumps(r4), flush=True)
    print("[W1] all experiments done.", flush=True)


if __name__ == "__main__":
    main()
