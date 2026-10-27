#!/usr/bin/env python3
"""
wave_directional.py — Directional-drive wave response of the attractor.

Instead of an isotropic antenna, the source is a Gaussian beam patched with
the phase gradient of the LOCKED ray direction at the launch point, so the
drive injects energy directly onto the attractor route. The time-averaged
intensity |E|^2 then exhibits (i) the route footprint and (ii) the nested
fine structure of the wavelength cascade, regularised by the grid (the
analogue of the metamaterial unit-cell cutoff).

Diagnostic PNGs are written to figures/_diagnostics/ for visual inspection.
"""

from __future__ import annotations

import json
import math
import os
import sys
import time

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ray_billiard import Medium, chamber_hexagon_asym, chirality_index, \
    propagate_ray

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))
DATA = os.path.join(ROOT, "data")
DIAG = os.path.join(ROOT, "figures", "_diagnostics")
os.makedirs(DATA, exist_ok=True)
os.makedirs(DIAG, exist_ok=True)

ETA = 9.0             # wave-level anisotropy (moderate: everything resolves;
                      #   the ray level covers eta = 100 separately)
GAMMA = 1e-3
N = 384
# three frequency BANDS; within each band |E|^2 is averaged over sub-frequencies.
# The standing-wave fringes shift with f, while the geometric attractor
# footprint is frequency-invariant -> band averaging reveals the route and
# simultaneously demonstrates the broadband character of the attractor.
BANDS = {"f6": [5.6, 6.0, 6.4, 6.8],
         "f9": [8.6, 9.0, 9.4, 9.8],
         "f14": [13.2, 13.6, 14.0, 14.4]}
SRC = (0.50, 0.60)
SIGMA = 0.035


def chamber_mask(ch, n):
    xs = np.linspace(0.0, 1.0, n)
    X, Y = np.meshgrid(xs, xs, indexing="ij")
    P = np.column_stack([X.ravel(), Y.ravel()])
    v = ch.vertices
    x, y = P[:, 0], P[:, 1]
    cnt = np.zeros(len(P), dtype=int)
    for i in range(len(v) - 1):
        x1, y1 = v[i]
        x2, y2 = v[i + 1]
        cond = ((y1 > y) != (y2 > y))
        with np.errstate(divide="ignore", invalid="ignore"):
            xint = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
        cnt += (cond & (x < xint)).astype(int)
    return ((cnt % 2) == 1).reshape(n, n)


def assemble(mask, k0, eta, gamma):
    n = mask.shape[0]
    idx = -np.ones((n, n), dtype=np.int64)
    idx[mask] = np.arange(mask.sum())
    dx = 1.0 / (n - 1)
    invdx2 = 1.0 / dx**2
    rows, cols, vals = [], [], []
    II, JJ = np.where(mask)
    cx = (1.0 / eta) * invdx2
    cy = invdx2
    for ei, (i, j) in enumerate(zip(II, JJ)):
        diag = cx * 2.0 - cy * 2.0 + k0**2 * (1.0 + 1j * gamma)
        for di, dj, c in ((-1, 0, -cx), (1, 0, -cx), (0, -1, cy), (0, 1, cy)):
            ii, jj = i + di, j + dj
            if 0 <= ii < n and 0 <= jj < n and mask[ii, jj]:
                rows.append(ei); cols.append(idx[ii, jj]); vals.append(c)
        rows.append(ei); cols.append(ei); vals.append(diag)
    A = sp.csr_matrix((vals, (rows, cols)),
                      shape=(mask.sum(), mask.sum()), dtype=complex)
    return A, idx


def k_from_direction(d, k0, eta, dx):
    """Wave vector on the dispersion contour whose group velocity is
    parallel to unit vector d (requires d_y^2 > eta d_x^2).

    The locked attractor direction saturates at the dispersion asymptote
    (d_y^2 = eta d_x^2) where no finite k exists, and the cascade drives
    |kx| beyond any grid. We therefore pick the grid-resolvable
    representative: the direction with |kx| = c*k0, c chosen so that the
    x-oscillation period spans >= ~15 grid nodes (|kx|*dx <= 0.4 rad).
    The grid cutoff here plays the role of the metamaterial unit-cell
    cutoff in the experiment.
    """
    d = np.asarray(d, dtype=float)
    d = d / np.hypot(*d)
    c_res = 0.4 / (k0 * dx)             # resolution-limited |kx|/k0
    c_asy = None                        # asymptote would be c -> inf
    # direction for a given c: tan(alpha) = m, m = sqrt(c^2/(eta(1+c^2)))
    c = min(6.0, c_res)
    if c < 0.2:                         # would be nearly isotropic; floor it
        c = 0.2
    m = math.sqrt(c * c / (eta * (eta + c * c)))
    s = np.sign(d[0]) if d[0] != 0 else 1.0
    sy = np.sign(d[1]) if d[1] != 0 else 1.0
    d_used = np.array([s * m, sy * 1.0])
    d_used = d_used / np.hypot(*d_used)
    lam2 = k0**2 / (d_used[1]**2 - eta * d_used[0]**2)
    lam = math.sqrt(lam2)
    return np.array([-eta * lam * d_used[0], lam * d_used[1]])


def directional_source(mask, kvec, src, sigma):
    n = mask.shape[0]
    xs = np.linspace(0.0, 1.0, n)
    X, Y = np.meshgrid(xs, xs, indexing="ij")
    R2 = (X - src[0])**2 + (Y - src[1])**2
    env = np.exp(-R2 / (2 * sigma**2)) * mask
    b = (env * np.exp(1j * (kvec[0] * X + kvec[1] * Y)))[mask]
    return b


def main():
    ch = chamber_hexagon_asym(s_left=0.03, s_right=0.06, y_v=0.35)
    mask = chamber_mask(ch, N)
    med = Medium("hyperbolic", eta=ETA)

    # reference ray: locked route + direction near the source
    rng = np.random.default_rng(1000)
    p0 = np.array([0.25 + 0.5 * rng.uniform(), 0.85])
    kx = rng.uniform(-1.5, 1.5)
    ky = math.sqrt(1.0 + kx * kx / ETA)
    res = propagate_ray(ch, med, p0, np.array([kx, -ky]), 1.0,
                        max_bounces=1600, loop_tol=1e-7, loop_window=100)
    loop = res.closed_loop
    print(f"route: period {res.period}, chirality "
          f"{chirality_index(loop):+.4f}")

    # locked (saturated) propagation direction: last free flight
    d_unit = res.vg_history[-1]
    print("locked direction:", np.round(d_unit, 4))

    xs = np.linspace(0.0, 1.0, N)
    X, Y = np.meshgrid(xs, xs, indexing="ij")

    fields = {}
    summary = {"grid": N, "eta": ETA, "gamma": GAMMA,
               "bands": {k: v for k, v in BANDS.items()},
               "loop_period": int(res.period),
               "loop_chirality": chirality_index(loop)}
    for band, flist in BANDS.items():
        acc = None
        for f in flist:
            k0 = 2.0 * np.pi * f
            dx = 1.0 / (N - 1)
            kv = k_from_direction(d_unit, k0, ETA, dx)
            A, idx = assemble(mask, k0, ETA, GAMMA)
            b = directional_source(mask, kv, SRC, SIGMA)
            lu = spla.splu(A.tocsc())
            E = lu.solve(b)
            Eg = np.zeros((N, N), dtype=complex)
            Eg[mask] = E
            inten = np.abs(Eg)**2
            acc = inten if acc is None else acc + inten
            print(f"{band}: f={f:.1f}, |kx|dx={abs(kv[0])*dx:.3f} rad",
                  flush=True)
        inten = acc / len(flist)
        fields[band] = inten
        # diagnostic figure
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(6, 6), constrained_layout=True)
        im = ax.imshow(inten.T, origin="lower", extent=[0, 1, 0, 1],
                       cmap="magma", vmax=np.percentile(inten, 99.0))
        lp = np.vstack([loop, loop[:1]])
        ax.plot(lp[:, 0], lp[:, 1], "c-", lw=1.2, alpha=0.8)
        ax.plot(ch.vertices[:, 0], ch.vertices[:, 1], "w-", lw=1.0)
        ax.plot(SRC[0], SRC[1], "r+", ms=10)
        ax.set_title(f"band-averaged |E|^2, {band} (route=cyan)")
        fig.colorbar(im, ax=ax, shrink=0.8)
        fig.savefig(os.path.join(DIAG, f"wave_{band}.png"), dpi=110)
        plt.close(fig)
        print(f"{band}: saved", flush=True)

    # correlations of band-averaged maps, excluding the source neighbourhood
    xs = np.linspace(0.0, 1.0, N)
    X, Y = np.meshgrid(xs, xs, indexing="ij")
    src_zone = np.hypot(X - SRC[0], Y - SRC[1]) < 4 * SIGMA
    keys = list(BANDS.keys())
    corr = {}
    for a in range(len(keys)):
        for bix in range(a + 1, len(keys)):
            u = fields[keys[a]][~src_zone].ravel()
            v = fields[keys[bix]][~src_zone].ravel()
            corr[f"{keys[a]}_{keys[bix]}"] = float(np.corrcoef(u, v)[0, 1])
    summary["cross_frequency_pearson"] = corr
    np.savez_compressed(os.path.join(DATA, "E4_wave_maps.npz"), **fields)
    with open(os.path.join(DATA, "E4_summary.json"), "w") as fjs:
        json.dump(summary, fjs, indent=2)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
