#!/usr/bin/env python3
"""
e7_time_domain.py — E7: time-domain simulation with unit-cell truncation.

Study W1 extension (Hyperbolic wave attractors, AB-Cloud Research).

Physics
-------
The frequency-domain Helmholtz model of study W1 is nondispersive: the
indefinite tensor mu = diag(1, -eta) is assumed frequency-independent.
Taken literally as a time-domain initial-value problem that model is
ILL-POSED — modes with omega^2 = c^2(ky^2 - kx^2/eta) < 0 grow
exponentially (the E7c "naive control" demonstrates the blow-up on the
grid; the discrete growth rate is 2/(dx*sqrt(eta))).

Real hyperbolic metamaterials are dispersive: the negative constituent is
a plasma response (wire-mesh / Drude form)

    mu_y(omega) = 1 - omega_p^2 / omega^2,

with the plasma frequency set by the UNIT CELL: omega_p = pi*c/a (a =
cell size, N_cells = L/a cells across the chamber). With this
regularisation the dispersion quadratic in Omega = omega^2,

    Omega^2 - c^2*S*Omega + c^2*ky^2*omega_p^2 = 0,
    S = omega_p^2/c^2 + kx^2 + ky^2,

has discriminant c^4*[kx^2+(ky-omega_p/c)^2]*[kx^2+(ky+omega_p/c)^2] >= 0:
BOTH branches are real for every k — the dispersive system is
unconditionally well-posed, exactly as passivity demands.

At a fixed drive frequency omega0 below the plasma frequency the medium
is EXACTLY the hyperbolic medium of the ray model with

    eta_eff = (omega_p/omega0)^2 - 1   <=>   omega0 = omega_p/sqrt(eta+1),

so eta_eff = 100 (the value used throughout study W1) corresponds to
omega0/omega_p = 1/sqrt(101). The unit cell enters through omega_p: the
iso-frequency arms at fixed omega0 fold back at |kx| ~ omega_p/c — the
cascade terminates at the unit-cell (Brillouin) scale, the time-domain
analogue of the wavelength-cascade cutoff of the reference experiment.

The ADE-FDTD scheme (leapfrog; E and the auxiliary polarisation chi are
both second-order):

    E_tt   = c^2 (Lap E + Dx chi) - sigma E_t
    chi_tt = -omega_p^2 (chi + Dx E) - sigma chi_t

Protocol (pulsed, as in the reference experiment): a narrowband Gaussian
pulse (Q ~ 13, ~4% bandwidth) is injected by a short line antenna and
left to evolve freely. Diagnostics:

E7a  main run: N_cells = 128 (2 nodes per cell), eta_eff = 100.
     |E|^2 snapshots show the funneling of the pulse energy onto the
     ray-predicted route; F_route(t) = (pulse energy in the corridor) /
     (total pulse energy) is compared against an ISOTROPIC control
     (omega_p = 0) run with the identical pulse and chamber; windowed
     k-spectra show the cascade front marching out along the hyperbola
     and piling up at the unit-cell fold |kx| ~ omega_p/c.

E7b  truncation scan: N_cells in {32, 48, 64, 96, 128, 192} at FIXED
     eta_eff = 100 (omega0 scales with omega_p). The number of hyperbolic
     wavelengths across the chamber grows as N_cells/(2*sqrt(eta+1));
     below a few wavelengths the attractor cannot be expressed — the
     corridor capture C(N_cells) measures the homogenisation convergence
     of the attractor with the number of unit cells.

E7c  naive (nondispersive) control: same geometry, indefinite operator —
     exponential blow-up; measured e-folding rate vs 2/(dx*sqrt(eta)).

Outputs
-------
data/E7_td_snapshots.npz     |E|^2 snapshots, hyper + iso (E7a)
data/E7_route_fraction.csv   F_route(t) for both media (E7a)
data/E7_kspectra.npz         windowed k-spectra at snapshot times (E7a)
data/E7_truncation_scan.csv  capture vs N_cells (E7b)
data/E7_summary.json         all metrics incl. blow-up control (E7c)

Usage:  python3 e7_time_domain.py [--quick]
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
from ray_billiard import chamber_hexagon_asym
import wave_helmholtz as wh

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.normpath(os.path.join(HERE, "..", "data"))
os.makedirs(DATA, exist_ok=True)

ETA_MAIN = 100.0
N_CELLS_MAIN = 128
CFL = 0.30
SIGMA = 0.01          # weak material loss (same for hyper & control)
A_SRC = 1.0           # pulse amplitude (linear problem: arbitrary)
PULSE_PERIODS = 4.0   # Gaussian envelope width in drive periods
T_PULSE = None        # set at runtime: envelope centred at 2*tau
Y_SRC = 0.60
T_MAIN = 120.0
SNAP_TIMES = [3.0, 6.0, 10.0, 16.0, 24.0, 40.0]
N_CELLS_SCAN = [32, 48, 64, 96, 128, 192]
T_SCAN_ANALYSIS = 24.0


# ----------------------------------------------------------------------------
# core solver
# ----------------------------------------------------------------------------
def make_mask(ch, n: int) -> np.ndarray:
    return wh.chamber_mask(ch, n)


def src_line(mask: np.ndarray, src=(0.5, Y_SRC), half: int = 2):
    n = mask.shape[0]
    i0 = int(round(src[0] * (n - 1)))
    j0 = int(round(src[1] * (n - 1)))
    nodes = []
    for dj in range(-half, half + 1):
        i, j = i0, j0 + dj
        if 0 <= i < n and 0 <= j < n and mask[i, j]:
            nodes.append((i, j))
    if not nodes:
        raise RuntimeError("source outside chamber")
    return nodes


class DrubeTD:
    """Leapfrog ADE-FDTD for the (optionally isotropic) medium, c = 1.

    omega_p = 0 reduces the model to the isotropic wave equation
    (the control). eta_naive switches on the nondispersive indefinite
    operator (the ill-posed control of E7c).
    """

    def __init__(self, mask: np.ndarray, omega_p: float, sigma: float,
                 eta_naive: float | None = None):
        self.n = mask.shape[0]
        self.mask = mask
        self.maskf = mask.astype(float)
        self.dx = 1.0 / (self.n - 1)
        self.dt = CFL * self.dx
        self.damp = math.exp(-sigma * self.dt)
        self.omega_p2 = omega_p * omega_p
        self.eta_naive = eta_naive
        self.E = np.zeros((self.n, self.n))
        self.chi = np.zeros((self.n, self.n))
        self.vE = np.zeros((self.n, self.n))
        self.vchi = np.zeros((self.n, self.n))
        self.t = 0.0
        self.dx2 = self.dx * self.dx

    def step(self, src_nodes=None, src_val=0.0):
        Ep = np.pad(self.E, 1)
        lap = (Ep[2:, 1:-1] + Ep[:-2, 1:-1] + Ep[1:-1, 2:] + Ep[1:-1, :-2]
               - 4.0 * self.E) / self.dx2
        dx_e = (Ep[2:, 1:-1] - Ep[:-2, 1:-1]) / (2.0 * self.dx)
        if src_nodes:
            for (i, j) in src_nodes:
                self.vE[i, j] += src_val * self.dt
        if self.eta_naive is not None:
            # naive indefinite control: E_tt = c^2(dyy - (1/eta) dxx) E
            dxx = (Ep[2:, 1:-1] - 2.0 * self.E + Ep[:-2, 1:-1]) / self.dx2
            acc_e = lap - (1.0 + 1.0 / self.eta_naive) * dxx
        else:
            chip = np.pad(self.chi, 1)
            dx_chi = (chip[2:, 1:-1] - chip[:-2, 1:-1]) / (2.0 * self.dx)
            acc_e = lap + dx_chi
            self.vchi = self.vchi * self.damp \
                - self.dt * self.omega_p2 * (self.chi + dx_e)
        self.vE = self.vE * self.damp + self.dt * acc_e
        self.E += self.dt * self.vE
        self.chi += self.dt * self.vchi
        self.E *= self.maskf
        self.chi *= self.maskf
        self.t += self.dt


def pulse(t: float, tau: float, t0: float, omega0: float) -> float:
    """Narrowband Gaussian pulse: envelope centred at t0, width tau."""
    if t > t0 + 3.0 * tau:
        return 0.0
    return A_SRC * math.exp(-((t - t0) ** 2) / (2.0 * tau * tau)) \
        * math.sin(omega0 * t)


def reference_route():
    return wh.reference_loop()


def route_field(loop, n: int) -> np.ndarray:
    xs = np.linspace(0.0, 1.0, n)
    X, Y = np.meshgrid(xs, xs, indexing="ij")
    D = np.full((n, n), np.inf)
    for p in loop[:: max(1, len(loop) // 240)]:
        D = np.minimum(D, np.hypot(X - p[0], Y - p[1]))
    return D


def k_spectrum(E: np.ndarray, mask: np.ndarray):
    """Windowed 2D spectrum over the interior box y in [0.37, 0.97]."""
    n = E.shape[0]
    xs = np.linspace(0.0, 1.0, n)
    X, Y = np.meshgrid(xs, xs, indexing="ij")
    box = ((X > 0.06) & (X < 0.94) & (Y > 0.37) & (Y < 0.97) & mask)
    W = np.hanning(n)
    W2 = np.outer(W, W)
    F = np.abs(np.fft.fftshift(np.fft.fft2(E * box * W2))) ** 2
    k = np.fft.fftshift(np.fft.fftfreq(n, 1.0 / (n - 1))) * 2.0 * math.pi
    return F, k


def kx_front(F: np.ndarray, k: np.ndarray) -> float:
    """|kx| containing 99% of the kx>0 half of the spectral energy."""
    marg = F.sum(axis=1)
    kpos = k[k > 0]
    mpos = marg[k > 0]
    csum = np.cumsum(mpos)
    total = csum[-1]
    if total <= 0:
        return 0.0
    idx = int(np.searchsorted(csum, 0.99 * total))
    return float(kpos[min(idx, len(kpos) - 1)])


# ----------------------------------------------------------------------------
# pulsed run for one medium
# ----------------------------------------------------------------------------
def pulsed_run(mask, omega_p, omega0, tau, t0, T, src_nodes,
               snap_times=(), frac_times=None, route=None):
    solver = DrubeTD(mask, omega_p, SIGMA)
    dt = solver.dt
    total = int(T / dt)
    snap_steps = {max(1, int(t / dt)): t for t in snap_times}
    snaps = {}
    ksps = {}
    fracs = []
    kk = None
    for s in range(1, total + 1):
        solver.step(src_nodes, pulse(solver.t, tau, t0, omega0))
        if frac_times and s % 20 == 0:
            I = solver.E * solver.E
            tot = float(I.sum())
            fr = float(I[route].sum()) / tot if tot > 0 else 0.0
            fracs.append((solver.t, fr))
        if s in snap_steps:
            I = solver.E * solver.E
            snaps[f"t{snap_steps[s]:g}"] = I.copy()
            F, kk = k_spectrum(solver.E, mask)
            ksps[f"t{snap_steps[s]:g}"] = (F.copy(), kx_front(F, kk))
    return solver, np.array(fracs), snaps, ksps, kk


# ----------------------------------------------------------------------------
# E7a: main run
# ----------------------------------------------------------------------------
def run_main(quick: bool) -> dict:
    t0w = time.time()
    n_cells = N_CELLS_MAIN
    n = n_cells if quick else 2 * n_cells
    ch = chamber_hexagon_asym(s_left=0.03, s_right=0.06, y_v=0.35)
    mask = make_mask(ch, n)
    omega_p = math.pi * n_cells
    omega0 = omega_p / math.sqrt(ETA_MAIN + 1.0)
    eta_eff = (omega_p / omega0) ** 2 - 1.0
    T0 = 2.0 * math.pi / omega0
    tau = PULSE_PERIODS * T0 / (2.0 * math.pi)   # envelope width in time
    t_pulse0 = 2.0 * tau
    print(f"[E7a] grid {n}, N_cells {n_cells}, omega_p {omega_p:.1f}, "
          f"omega0 {omega0:.2f}, eta_eff {eta_eff:.1f}, "
          f"pulse width {tau:.2f}", flush=True)

    loop, period = reference_route()
    D = route_field(loop, n)
    near = D < 0.04
    area_frac = float(near.sum() / mask.sum())
    nodes = src_line(mask)
    T = 60.0 if quick else T_MAIN
    snaps_t = [3.0, 6.0, 10.0] if quick else SNAP_TIMES

    _, fr_h, snaps_h, ks_h, kgrid = pulsed_run(
        mask, omega_p, omega0, tau, t_pulse0, T, nodes,
        snap_times=snaps_t, frac_times=True, route=near)
    _, fr_i, snaps_i, _, _ = pulsed_run(
        mask, 0.0, omega0, tau, t_pulse0, T, nodes,
        snap_times=snaps_t, frac_times=True, route=near)

    # metrics at the analysis time (ballistic organisation window)
    t_ana = 10.0 if quick else 24.0
    def at(fr, tt):
        i = np.argmin(np.abs(fr[:, 0] - tt))
        return float(fr[i, 1])
    cap_h, cap_i = at(fr_h, t_ana), at(fr_i, t_ana)
    # formation time (hyper): first t with F >= 90% of its max over window
    win = fr_h[fr_h[:, 0] <= t_ana]
    fmax = win[:, 1].max()
    t_form = float(win[np.argmax(win[:, 1] >= 0.9 * fmax), 0]) \
        if fmax > 0 else None

    summary = {
        "n_grid": n, "n_cells": n_cells, "omega_p": omega_p,
        "omega0": omega0, "eta_eff": eta_eff, "sigma": SIGMA,
        "pulse_width": tau, "T": T,
        "route_period_ray": int(period),
        "corridor_area_fraction": area_frac,
        "capture_hyper": cap_h, "capture_iso": cap_i,
        "capture_ratio": cap_h / cap_i if cap_i > 0 else None,
        "capture_contrast_hyper": cap_h / area_frac,
        "formation_time": t_form,
        "analysis_time": t_ana,
        "kx_front": {k: v[1] for k, v in ks_h.items()},
        "kx_fold_edge": float(math.sqrt(omega_p**2 - omega0**2)),
    }
    snaps = {f"hyp_{k}": v for k, v in snaps_h.items()}
    snaps.update({f"iso_{k}": v for k, v in snaps_i.items()})
    np.savez_compressed(os.path.join(DATA, "E7_td_snapshots.npz"),
                        route=D, **snaps)
    np.savez_compressed(os.path.join(DATA, "E7_kspectra.npz"), k=kgrid,
                        **{k: v[0] for k, v in ks_h.items()})
    with open(os.path.join(DATA, "E7_route_fraction.csv"), "w",
              newline="") as f:
        w = csv.writer(f)
        w.writerow(["t", "route_fraction_hyper", "route_fraction_iso"])
        w.writerows([(a, b, c) for (a, b), (_, c) in zip(fr_h, fr_i)])
    print(f"[E7a] done: capture hyper {cap_h:.4f} vs iso {cap_i:.4f} "
          f"(ratio {cap_h/max(cap_i,1e-30):.2f}), formation t={t_form} "
          f"({time.time()-t0w:.1f}s)", flush=True)
    print(f"[E7a] kx front: " + ", ".join(
        f"t{k}={v[1]:.0f}" for k, v in ks_h.items()), flush=True)
    return summary


# ----------------------------------------------------------------------------
# E7b: truncation scan
# ----------------------------------------------------------------------------
def run_scan(quick: bool) -> list[dict]:
    rows = []
    ch = chamber_hexagon_asym(s_left=0.03, s_right=0.06, y_v=0.35)
    loop, _ = reference_route()
    scan_list = N_CELLS_SCAN[:3] if quick else N_CELLS_SCAN
    for n_cells in scan_list:
        t0 = time.time()
        n = n_cells if quick else 2 * n_cells
        mask = make_mask(ch, n)
        omega_p = math.pi * n_cells
        omega0 = omega_p / math.sqrt(ETA_MAIN + 1.0)
        T0 = 2.0 * math.pi / omega0
        tau = PULSE_PERIODS * T0 / (2.0 * math.pi)
        D = route_field(loop, n)
        near = D < 0.04
        area_frac = float(near.sum() / mask.sum())
        nodes = src_line(mask)
        _, fr_h, _, _, _ = pulsed_run(
            mask, omega_p, omega0, tau, 2.0 * tau, T_SCAN_ANALYSIS, nodes,
            frac_times=True, route=near)
        cap = float(fr_h[np.argmin(np.abs(fr_h[:, 0] - T_SCAN_ANALYSIS * 0.9)),
                         1]) if len(fr_h) else 0.0
        cap_peak = float(fr_h[:, 1].max()) if len(fr_h) else 0.0
        n_lambda = omega0 / (2.0 * math.pi)
        rows.append({
            "n_cells": n_cells, "n_grid": n,
            "omega_p": omega_p, "omega0": omega0, "eta_eff": ETA_MAIN,
            "wavelengths_across_chamber": n_lambda,
            "capture_at_analysis": cap, "capture_peak": cap_peak,
            "capture_contrast": cap / area_frac,
            "corridor_area_fraction": area_frac,
        })
        print(f"[E7b] N_cells={n_cells}: {n_lambda:.2f} wavelengths across, "
              f"capture {cap:.4f} (peak {cap_peak:.4f}, contrast "
              f"x{cap/area_frac:.2f}) ({time.time()-t0:.1f}s)", flush=True)
    with open(os.path.join(DATA, "E7_truncation_scan.csv"), "w",
              newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    return rows


# ----------------------------------------------------------------------------
# E7c: naive nondispersive control (blow-up)
# ----------------------------------------------------------------------------
def run_naive_control() -> dict:
    t0 = time.time()
    n = 256
    ch = chamber_hexagon_asym(s_left=0.03, s_right=0.06, y_v=0.35)
    mask = make_mask(ch, n)
    eta = ETA_MAIN
    solver = DrubeTD(mask, omega_p=1.0, sigma=0.0, eta_naive=eta)
    xs = np.linspace(0.0, 1.0, n)
    X, Y = np.meshgrid(xs, xs, indexing="ij")
    solver.E = np.exp(-((X - 0.5) ** 2 + (Y - 0.6) ** 2) / 1e-4) * mask
    dx = solver.dx
    gamma_pred = 2.0 / (dx * math.sqrt(eta))       # discrete worst case
    hist = []
    t_blow = None
    for s in range(1, 30001):
        solver.step()
        if s % 5 == 0:
            w = float((solver.E ** 2).sum())
            hist.append((solver.t, w))
            if w > 1e10 or not math.isfinite(w):
                t_blow = solver.t
                break
    # fit the late pre-blow-up window (fastest mode dominant)
    k = max(2, len(hist) // 2)
    tt = np.array([h[0] for h in hist[k:]])
    ww = np.array([max(h[1], 1e-300) for h in hist[k:]])
    gamma_meas = float(np.polyfit(tt, np.log(ww), 1)[0]) if len(tt) > 3 else 0.0
    summary = {
        "eta": eta, "n_grid": n,
        "gamma_predicted_discrete": gamma_pred,
        "gamma_predicted_continuum": math.pi / (dx * math.sqrt(eta)),
        "gamma_measured": gamma_meas,
        "ratio_discrete": gamma_meas / gamma_pred,
        "blowup_time": t_blow,
    }
    print(f"[E7c] naive control: blow-up at t={t_blow:.3f}, gamma = "
          f"{gamma_meas:.1f} vs predicted 2/(dx*sqrt(eta)) = "
          f"{gamma_pred:.1f} (ratio {gamma_meas/gamma_pred:.2f}) "
          f"({time.time()-t0:.1f}s)", flush=True)
    return summary


# ----------------------------------------------------------------------------
# stability demonstration (dispersive model, lossless, source-free)
# ----------------------------------------------------------------------------
def run_stability_check() -> dict:
    n = 128
    ch = chamber_hexagon_asym(s_left=0.03, s_right=0.06, y_v=0.35)
    mask = make_mask(ch, n)
    omega_p = math.pi * 64
    solver = DrubeTD(mask, omega_p, sigma=0.0)
    xs = np.linspace(0.0, 1.0, n)
    X, Y = np.meshgrid(xs, xs, indexing="ij")
    solver.E = np.exp(-((X - 0.5) ** 2 + (Y - 0.6) ** 2) / 1e-3) * mask
    e0max = float(np.abs(solver.E).max())
    chi_max = 0.0
    e_max = e0max
    for s in range(1, 8001):
        solver.step()
        e_max = max(e_max, float(np.abs(solver.E).max()))
        chi_max = max(chi_max, float(np.abs(solver.chi).max()))
    summary = {"n_grid": n, "steps": 8000, "T": float(8000 * solver.dt),
               "E_max_over_E0": e_max / e0max,
               "chi_max": chi_max}
    print(f"[E7] stability (dispersive, lossless): max|E|/max|E0| = "
          f"{e_max/e0max:.2f} over T = {8000*solver.dt:.1f}", flush=True)
    return summary


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--quick", action="store_true")
    args = ap.parse_args()
    t0 = time.time()

    main_summary = run_main(args.quick)
    scan_rows = run_scan(args.quick)
    naive = run_naive_control()
    stab = run_stability_check()

    summary = {
        "model": "Drude-regularised hyperbolic medium, ADE-FDTD leapfrog",
        "mapping": "omega0 = omega_p/sqrt(eta+1) <=> eta_eff = (wp/w0)^2-1",
        "unit_cell": "omega_p = pi*c/a, a = L/N_cells",
        "main_run": main_summary,
        "truncation_scan": scan_rows,
        "naive_control": naive,
        "stability_check": stab,
    }
    with open(os.path.join(DATA, "E7_summary.json"), "w") as fjs:
        json.dump(summary, fjs, indent=2)
    print(f"[E7] all done in {time.time()-t0:.1f}s", flush=True)


if __name__ == "__main__":
    main()
