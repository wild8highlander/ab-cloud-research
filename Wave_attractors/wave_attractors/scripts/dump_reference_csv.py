#!/usr/bin/env python3
"""
dump_reference_csv.py — Export the launch states of the cross-verification
set (identical to rays_python.json) as a plain CSV consumed by the Julia
port (scripts/julia/wave_attractors.jl).
"""

import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ray_billiard import Medium, chamber_hexagon_asym, chirality_index, \
    propagate_ray

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.normpath(os.path.join(HERE, "..", "data"))

ETA = 100.0


def main() -> None:
    n_rays = 12
    med = Medium("hyperbolic", eta=ETA)
    ch = chamber_hexagon_asym(s_left=0.03, s_right=0.06, y_v=0.35)
    rows = [("ray", "p0x", "p0y", "k0x", "k0y")]
    rays = []
    SHORT_HORIZON = 100
    short_rows = [("ray", "bounce", "x", "y")]
    for ir in range(n_rays):
        rng = np.random.default_rng(7000 + ir)
        p0 = np.array([0.25 + 0.5 * rng.uniform(), 0.85])
        kx = rng.uniform(-1.5, 1.5)
        ky = math.sqrt(1.0 + kx * kx / ETA)
        k0 = np.array([kx, -ky])
        rows.append((ir, f"{p0[0]:.16e}", f"{p0[1]:.16e}",
                     f"{k0[0]:.16e}", f"{k0[1]:.16e}"))
        res = propagate_ray(ch, med, p0, k0, 1.0, max_bounces=1600,
                            loop_tol=1e-7, loop_window=100)
        rays.append(res)
        for b in range(min(SHORT_HORIZON, len(res.bounce_points) - 1)):
            short_rows.append((ir, b,
                               f"{res.bounce_points[b + 1, 0]:.16e}",
                               f"{res.bounce_points[b + 1, 1]:.16e}"))

    with open(os.path.join(DATA, "rays_reference.csv"), "w") as f:
        for r in rows:
            f.write(",".join(str(x) for x in r) + "\n")
    with open(os.path.join(DATA, "rays_short_python.csv"), "w") as f:
        for r in short_rows:
            f.write(",".join(str(x) for x in r) + "\n")

    # Python-side results in the same schema as rays_julia.csv
    with open(os.path.join(DATA, "rays_python_summary.csv"), "w") as f:
        f.write("ray,n_bounces,period,loop_found,chirality,final_kx,final_ky\n")
        for ir, res in enumerate(rays):
            loop_found = res.closed_loop is not None
            chi = chirality_index(res.closed_loop) if loop_found else 0.0
            per = res.period if loop_found else 0
            kf = res.k_history[-1]
            f.write(f"{ir},{len(res.edges)},{per},"
                    f"{1 if loop_found else 0},{chi:.16e},"
                    f"{kf[0]:.16e},{kf[1]:.16e}\n")
    print(f"wrote rays_reference.csv and rays_python_summary.csv "
          f"({n_rays} rays)")


import math  # noqa: E402  (kept at bottom to mirror run_experiments style)

if __name__ == "__main__":
    main()
