#!/usr/bin/env python3
"""
verify_td_cross.py — Python-side comparison for the Julia E7 TD kernel.

Compares the field snapshots produced by scripts/julia/td_check.jl with
an exact replica of the same leapfrog ADE-FDTD step in numpy. Because
both sides evaluate the update per grid node in the same operation
order, agreement at the 1e-14 level verifies the port essentially
bit-exactly (the reference cross-verification of the ray core, W1,
reached 3.45e-15).

Writes data/td_cross_verification.json.

Usage:  python3 verify_td_cross.py [csv_file]
        (default: ../data/julia_td_snapshots.csv produced by
         julia td_check.jl ../data/julia_td)
"""

from __future__ import annotations

import csv
import json
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.normpath(os.path.join(HERE, "..", "data"))


def replicate():
    n = 48
    dx = 1.0 / (n - 1)
    dt = 0.3 * dx
    sigma = 0.01
    damp = math.exp(-sigma * dt)
    omega_p2 = (math.pi * 24) ** 2
    dx2 = dx * dx
    xs = np.arange(n) * dx
    X, Y = np.meshgrid(xs, xs, indexing="ij")
    E = np.exp(-((X - 0.5) ** 2 + (Y - 0.45) ** 2) / 1e-3)
    chi = np.zeros((n, n))
    vE = np.zeros((n, n))
    vchi = np.zeros((n, n))
    snaps = {0: (E.copy(), chi.copy())}
    for s in range(1, 401):
        Ep = np.pad(E, 1)
        chip = np.pad(chi, 1)
        lap = (Ep[2:, 1:-1] + Ep[:-2, 1:-1] + Ep[1:-1, 2:] + Ep[1:-1, :-2]
               - 4.0 * E) / dx2
        dx_e = (Ep[2:, 1:-1] - Ep[:-2, 1:-1]) / (2.0 * dx)
        dx_chi = (chip[2:, 1:-1] - chip[:-2, 1:-1]) / (2.0 * dx)
        vE = vE * damp + dt * (lap + dx_chi)
        vchi = vchi * damp - dt * omega_p2 * (chi + dx_e)
        E = E + dt * vE
        chi = chi + dt * vchi
        if s in (100, 200, 300, 400):
            snaps[s] = (E.copy(), chi.copy())
    return snaps


def main() -> None:
    csv_path = sys.argv[1] if len(sys.argv) > 1 else \
        os.path.join(DATA, "julia_td_snapshots.csv")
    if not os.path.exists(csv_path):
        print(f"verify_td_cross: {csv_path} not found — run "
              "julia scripts/julia/td_check.jl ../data/julia_td first")
        raise SystemExit(1)

    ref = {}
    with open(csv_path) as f:
        for row in csv.DictReader(f):
            step = int(row["step"])
            i, j = int(row["i"]) - 1, int(row["j"]) - 1
            ref.setdefault(step, np.full((48, 48, 2), np.nan))
            ref[step][i, j, 0] = float(row["E"])
            ref[step][i, j, 1] = float(row["chi"])

    py = replicate()
    worst = 0.0
    per_step = {}
    for step in sorted(py):
        jE = ref[step][..., 0]
        jchi = ref[step][..., 1]
        pE, pchi = py[step]
        dE = float(np.max(np.abs(jE - pE)))
        dchi = float(np.max(np.abs(jchi - pchi)))
        scale = max(float(np.max(np.abs(pE))), 1e-30)
        per_step[str(step)] = {
            "max_abs_diff_E": dE,
            "max_abs_diff_chi": dchi,
            "rel_diff_E": dE / scale,
        }
        worst = max(worst, dE / scale)
    passed = worst < 1e-11
    result = {
        "model": "E7 time-domain leapfrog ADE-FDTD (Drude hyperbolic)",
        "julia_csv": os.path.basename(csv_path),
        "grid": 48, "steps": 400,
        "per_step": per_step,
        "max_rel_dev": worst,
        "threshold": 1e-11,
        "passed": bool(passed),
    }
    with open(os.path.join(DATA, "td_cross_verification.json"), "w") as fjs:
        json.dump(result, fjs, indent=2)
    print(f"verify_td_cross: max relative deviation {worst:.3e} "
          f"({'PASS' if passed else 'FAIL'})")


if __name__ == "__main__":
    main()
