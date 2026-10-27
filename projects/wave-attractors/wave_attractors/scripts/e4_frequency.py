#!/usr/bin/env python3
"""
e4_frequency.py — Frequency independence of the attractor (E4).

E4a (rigorous): the normalised ray map is exactly frequency-invariant.
    Propagating the SAME chamber with K = 1 and K = 7 and comparing the
    normalised trajectories (k/K) gives machine-precision agreement, hence
    the attractor route geometry does not depend on the drive frequency.

E4c (geometric acoustics): the high-frequency energy density of a broad
    ensemble of rays concentrates onto the closed attractor route. We
    accumulate a 2-D histogram of ray path lengths (the ray-density proxy
    for the time-averaged wave energy density, cf. internal-wave attractor
    visualisations of Maas & Lam) and report the route-corridor contrast.

Outputs:
    data/E4_frequency_invariance.json
    data/E4_ray_density.npz
"""

from __future__ import annotations

import json
import math
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ray_billiard import Medium, chamber_hexagon_asym, distance_to_loop, \
    propagate_ray

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))
DATA = os.path.join(ROOT, "data")
os.makedirs(DATA, exist_ok=True)

S_LEFT, S_RIGHT, Y_V = 0.03, 0.06, 0.35


def run_chamber(med: Medium, seed0: int, n_rays: int, max_bounces: int):
    ch = chamber_hexagon_asym(s_left=S_LEFT, s_right=S_RIGHT, y_v=Y_V)
    loops = []
    for ir in range(n_rays):
        rng = np.random.default_rng(seed0 + ir)
        p0 = np.array([0.25 + 0.5 * rng.uniform(), 0.85])
        kx = rng.uniform(-1.5, 1.5)
        ky = math.sqrt(1.0 + kx * kx / med.eta) if med.kind == "hyperbolic" \
            else math.sqrt(max(1e-6, 1.0 - 0.3 * kx * kx))
        res = propagate_ray(ch, med, p0, np.array([kx, -ky]),
                            1.0 if med.kind == "hyperbolic" else 1.0,
                            max_bounces=max_bounces, loop_tol=1e-7,
                            loop_window=100)
        loops.append(res)
    return ch, loops


def main() -> None:
    t0 = time.time()
    eta = 9.0
    med = Medium("hyperbolic", eta=eta)

    # ---- E4a: exact frequency invariance of the normalised ray map --------
    ch = chamber_hexagon_asym(s_left=S_LEFT, s_right=S_RIGHT, y_v=Y_V)
    rng = np.random.default_rng(1000)
    p0 = np.array([0.25 + 0.5 * rng.uniform(), 0.85])
    kx = rng.uniform(-1.5, 1.5)
    ky = math.sqrt(1.0 + kx * kx / eta)
    k0dir = np.array([kx, -ky])

    res1 = propagate_ray(ch, med, p0, k0dir, K=1.0, max_bounces=1200,
                         loop_tol=1e-7, loop_window=100)
    res7 = propagate_ray(ch, med, p0, 7.0 * k0dir, K=7.0, max_bounces=1200,
                         loop_tol=1e-7, loop_window=100)
    # compare bounce points (positions are K-independent)
    n = min(len(res1.bounce_points), len(res7.bounce_points))
    dev = np.abs(res1.bounce_points[:n] - res7.bounce_points[:n]).max()
    out = {
        "K_values": [1.0, 7.0],
        "n_bounces_compared": int(n),
        "max_position_deviation": float(dev),
        "period_K1": int(res1.period),
        "period_K7": int(res7.period),
        "invariant": bool(dev < 1e-9),
    }
    print("E4a frequency invariance:", json.dumps(out), flush=True)

    # ---- E4c: ray-density energy map --------------------------------------
    n_rays = 300
    max_bounces = 400
    n_grid = 512
    H = np.zeros((n_grid, n_grid))
    for ir in range(n_rays):
        rng = np.random.default_rng(20000 + ir)
        p0 = np.array([0.25 + 0.5 * rng.uniform(), 0.85])
        kx = rng.uniform(-1.5, 1.5)
        ky = math.sqrt(1.0 + kx * kx / eta)
        try:
            res = propagate_ray(ch, med, p0, np.array([kx, -ky]), 1.0,
                                max_bounces=max_bounces, loop_tol=1e-7,
                                loop_window=100)
        except RuntimeError:
            continue
        pts = res.bounce_points
        # accumulate path segments with per-pixel line rasterisation
        for a, b in zip(pts[:-1], pts[1:]):
            L = int(np.hypot(*(b - a)) * n_grid * 3)
            ts = np.linspace(0.0, 1.0, max(2, L))
            seg = a[None, :] + ts[:, None] * (b - a)[None, :]
            ii = np.clip((seg[:, 0] * (n_grid - 1)).astype(int), 0, n_grid - 1)
            jj = np.clip((seg[:, 1] * (n_grid - 1)).astype(int), 0, n_grid - 1)
            np.add.at(H, (ii, jj), 1.0)
    H /= H.max()

    # route corridor contrast (use the reference locked route)
    ref = propagate_ray(ch, med, p0, k0dir, 1.0, max_bounces=1500,
                        loop_tol=1e-7, loop_window=100)
    loop = ref.closed_loop
    xs = np.linspace(0.0, 1.0, n_grid)
    X, Y = np.meshgrid(xs, xs, indexing="ij")
    D = np.full((n_grid, n_grid), np.inf)
    for p in loop[:: max(1, len(loop) // 300)]:
        D = np.minimum(D, np.hypot(X - p[0], Y - p[1]))
    # exclude regions within the first bounces of any ray (source transients)
    near = D < 0.025
    far = D > 0.12
    contrast = float(H[near].mean() / H[far].mean())
    out2 = {
        "n_rays": n_rays,
        "max_bounces": max_bounces,
        "grid": n_grid,
        "corridor_contrast": contrast,
        "route_period": int(ref.period),
    }
    print("E4c ray density:", json.dumps(out2), flush=True)

    np.savez_compressed(os.path.join(DATA, "E4_ray_density.npz"), H=H, D=D)
    out.update(out2)
    out["runtime_s"] = round(time.time() - t0, 2)
    with open(os.path.join(DATA, "E4_frequency_invariance.json"), "w") as f:
        json.dump(out, f, indent=2)


if __name__ == "__main__":
    main()
