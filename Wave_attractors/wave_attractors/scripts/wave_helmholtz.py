#!/usr/bin/env python3
"""
wave_helmholtz.py — Wave-level simulation of hyperbolic wave attractors.

Solves the frequency-domain anisotropic Helmholtz equation (TE-like scalar
polarisation, out-of-plane field E ≡ E_z) inside the polygonal chamber:

    (1/mu_y) d^2E/dx^2 + (1/mu_x) d^2E/dy^2 + k0^2 (1 + i gamma) E = S,

with mu_x = 1, mu_y = -eta (hyperbolic medium, eta = |mu_y|) and a perfectly
conducting boundary E|_wall = 0. The dispersion relation of plane waves,

    ky^2 - kx^2 / eta = k0^2,

coincides with the ray model of ray_billiard.py, so the wave simulation and
the ray tracing describe the same medium.

Physics demonstrated
--------------------
A point/line drive excites the chamber; the time-averaged intensity |E|^2
concentrates along the ray-predicted attractor route. Because the attractor
carries an unbounded wavelength cascade (|k| grows geometrically at every
slope reflection), the wave field is regularised by the finite grid — the
numerical analogue of the unit-cell cutoff of a real metamaterial (the
cascade in the experiment terminates at the unit-cell scale).

Frequency independence (E4): the ray route is independent of k0 (the
normalised map (kx/k0, ky/k0) is frequency-invariant); the wave intensity
footprint of the route is therefore broadband. We quantify this by the
spatial correlation of |E|^2 across three frequencies.

Outputs
-------
data/E4_wave_maps.npz     : |E|^2 fields for the three frequencies
data/E4_summary.json      : route-contrast and cross-frequency correlations

Usage:  python3 wave_helmholtz.py [--quick]
"""

from __future__ import annotations

import argparse
import json
import math
import os
import sys
import time

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ray_billiard import (Medium, chamber_hexagon_asym, chirality_index,
                          distance_to_loop, propagate_ray)

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.normpath(os.path.join(HERE, "..", "data"))
os.makedirs(DATA, exist_ok=True)

ETA = 100.0
GAMMA = 2e-4          # weak loss (regularises resonances), dimensionless
N_GRID = 384          # grid nodes per side
FREQS = [6.0, 9.0, 14.0]   # oscillations across the chamber, k0 = 2*pi*f
SRC = (0.50, 0.62)    # drive location (inside the chamber)


def chamber_mask(ch, n: int) -> np.ndarray:
    """Boolean mask of grid nodes inside the chamber polygon."""
    xs = np.linspace(0.0, 1.0, n)
    X, Y = np.meshgrid(xs, xs, indexing="ij")
    P = np.column_stack([X.ravel(), Y.ravel()])
    v = ch.vertices
    inside = np.zeros(len(P), dtype=bool)
    # even-odd rule, vectorised
    x, y = P[:, 0], P[:, 1]
    cnt = np.zeros(len(P), dtype=int)
    for i in range(len(v) - 1):
        x1, y1 = v[i]
        x2, y2 = v[i + 1]
        cond = ((y1 > y) != (y2 > y))
        with np.errstate(divide="ignore", invalid="ignore"):
            xint = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
        cnt += (cond & (x < xint)).astype(int)
    inside = (cnt % 2) == 1
    return inside.reshape(n, n)


def assemble(mask: np.ndarray, k0: float, eta: float, gamma: float):
    """Sparse complex Helmholtz matrix with Dirichlet boundary (E=0 outside).

    Discretisation (5-point):
        (1/eta)(2 E_i - E_w - E_e)/dx^2
        + (E_n - 2 E_i + E_s)/dy^2
        + k0^2 (1 + i gamma) E_i = S_i
    """
    n = mask.shape[0]
    idx = -np.ones((n, n), dtype=np.int64)
    idx[mask] = np.arange(mask.sum())
    dx = 1.0 / (n - 1)
    invdx2 = 1.0 / dx**2

    rows, cols, vals = [], [], []
    II, JJ = np.where(mask)
    for ei, (i, j) in enumerate(zip(II, JJ)):
        diag = (2.0 / eta) * invdx2 - 2.0 * invdx2 + k0**2 * (1.0 + 1j * gamma)
        # x-neighbours (coefficient 1/eta * invdx2 with MINUS sign in the PDE,
        # entering the matrix as -c)
        cx = (1.0 / eta) * invdx2
        for di, dj, c in ((-1, 0, -cx), (1, 0, -cx), (0, -1, invdx2),
                          (0, 1, invdx2)):
            ii, jj = i + di, j + dj
            if 0 <= ii < n and 0 <= jj < n and mask[ii, jj]:
                rows.append(ei); cols.append(idx[ii, jj]); vals.append(c)
            # Dirichlet outside: neighbour contributes 0, nothing to add
        rows.append(ei); cols.append(ei); vals.append(diag)
    A = sp.csr_matrix((vals, (rows, cols)),
                      shape=(mask.sum(), mask.sum()), dtype=complex)
    return A, idx


def source_vector(mask: np.ndarray, idx: np.ndarray, src: tuple,
                  n: int) -> np.ndarray:
    """Unit-amplitude vertical line antenna (5 nodes) at the source point."""
    b = np.zeros(mask.sum(), dtype=complex)
    i0 = int(round(src[0] * (n - 1)))
    j0 = int(round(src[1] * (n - 1)))
    placed = 0
    for dj in (-2, -1, 0, 1, 2):
        i, j = i0, j0 + dj
        if 0 <= i < n and 0 <= j < n and mask[i, j]:
            b[idx[i, j]] = 1.0
            placed += 1
    if placed == 0:
        raise RuntimeError("source outside chamber")
    return b


def reference_loop(max_bounces: int = 1600) -> tuple[np.ndarray, int]:
    """Ray-predicted attractor route (single reference ray)."""
    med = Medium("hyperbolic", eta=ETA)
    ch = chamber_hexagon_asym(s_left=0.03, s_right=0.06, y_v=0.35)
    rng = np.random.default_rng(1000)
    p0 = np.array([0.25 + 0.5 * rng.uniform(), 0.85])
    kx = rng.uniform(-1.5, 1.5)
    ky = math.sqrt(1.0 + kx * kx / ETA)
    res = propagate_ray(ch, med, p0, np.array([kx, -ky]), 1.0,
                        max_bounces=max_bounces, loop_tol=1e-7,
                        loop_window=100)
    if res.closed_loop is None:
        raise RuntimeError("reference ray did not lock onto a loop")
    return res.closed_loop, res.period


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--quick", action="store_true")
    args = ap.parse_args()
    n = 192 if args.quick else N_GRID
    freqs = [6.0, 9.0] if args.quick else FREQS

    t0 = time.time()
    ch = chamber_hexagon_asym(s_left=0.03, s_right=0.06, y_v=0.35)
    mask = chamber_mask(ch, n)
    print(f"[W1-wave] grid {n}x{n}, interior nodes {int(mask.sum())}",
          flush=True)

    loop, period = reference_loop()
    print(f"[W1-wave] reference route: period {period}, "
          f"chirality {chirality_index(loop):+.4f}", flush=True)

    fields = {}
    summary = {"grid": n, "eta": ETA, "gamma": GAMMA, "freqs": freqs,
               "loop_period": int(period),
               "loop_chirality": chirality_index(loop)}
    xs = np.linspace(0.0, 1.0, n)
    X, Y = np.meshgrid(xs, xs, indexing="ij")
    D_route = np.full((n, n), np.inf)
    pts = loop[:: max(1, len(loop) // 220)]
    for p in pts:
        d = np.hypot(X - p[0], Y - p[1])
        D_route = np.minimum(D_route, d)
    near_route = D_route < 0.04
    far_route = D_route > 0.15
    src_r = np.hypot(X - SRC[0], Y - SRC[1]) < 0.06
    far_route &= ~src_r

    for f in freqs:
        k0 = 2.0 * np.pi * f
        tf = time.time()
        A, idx = assemble(mask, k0, ETA, GAMMA)
        b = source_vector(mask, idx, SRC, n)
        lu = spla.splu(A.tocsc())
        E = lu.solve(b)
        Egrid = np.zeros((n, n), dtype=complex)
        Egrid[mask] = E
        inten = np.abs(Egrid) ** 2
        fields[f"f{int(f)}"] = inten
        c_near = inten[near_route].mean()
        c_far = inten[far_route].mean()
        contrast = c_near / c_far
        summary[f"contrast_f{int(f)}"] = float(contrast)
        print(f"[W1-wave] f={f}: k0={k0:.1f}, solve {time.time()-tf:.1f}s, "
              f"|E|^2 near-route / far-route = {contrast:.2f}", flush=True)

    # cross-frequency correlation of the intensity footprints
    keys = [f"f{int(f)}" for f in freqs]
    corr = {}
    for a in range(len(keys)):
        for bix in range(a + 1, len(keys)):
            u = fields[keys[a]].ravel()
            v = fields[keys[bix]].ravel()
            r = float(np.corrcoef(u, v)[0, 1])
            corr[f"{keys[a]}_{keys[bix]}"] = r
    summary["cross_frequency_pearson"] = corr

    np.savez_compressed(os.path.join(DATA, "E4_wave_maps.npz"),
                        route=D_route, **fields)
    with open(os.path.join(DATA, "E4_summary.json"), "w") as fjs:
        json.dump(summary, fjs, indent=2)
    print(f"[W1-wave] done in {time.time()-t0:.1f}s", flush=True)
    print(json.dumps(summary, indent=2), flush=True)


if __name__ == "__main__":
    main()
