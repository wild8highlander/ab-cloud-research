#!/usr/bin/env python3
"""
ab_water.py — Companion study W1-AB: the Aharonov-Bohm effect with water
waves (numerical reproduction of the OIST water-tank experiment,
Communications Physics, 2026; theory: Berry et al., 1980).

Physics
-------
A surface water wave incident on a swirling vortex acquires a geometric
(Aharonov-Bohm-like) phase: the wave field around the vortex is the
AB-scattered state

    psi_alpha(r, theta) = sum_m i^(m-alpha) J_{m-alpha}(k r) e^{i(m-alpha) theta},

where alpha is the dimensionless circulation (flux) parameter of the vortex
and the fractional angular momentum order m-alpha encodes the geometric
phase. For alpha -> 0 the Jacobi-Anger identity reduces the sum to the
incident plane wave e^{i k x}.

Following the OIST experiment we superpose TWO opposite incident waves,
psi = psi^{(+x)} + psi^{(-x)}. The interference of the two AB-scattered
fields produces forked nodal dislocations near the vortex AND — the
unexpected discovery of the experiment — nodal patterns that ROTATE in
time. We measure:

  M1  the rotation rate of the nodal pattern versus alpha;
  M2  the mirror symmetry: the pattern for -alpha is the mirror image of
      the pattern for +alpha (vortex circulation reversed);
  M3  the number of forked dislocation arms near the core.

Connection to the AB-Cloud repository: the host project studies
Aharonov-Bohm phases engineered from zeta zeros on a Hofstadter lattice;
this companion reproduces the ORIGINAL AB geometry in a classical fluid.

Outputs:
    data/AB_water_metrics.json
    figures/ (diagnostic frames)
"""

from __future__ import annotations

import json
import os
import sys
import time

import numpy as np
from scipy.special import jv

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))
DATA = os.path.join(ROOT, "data")
DIAG = os.path.join(ROOT, "figures", "_diagnostics")
os.makedirs(DATA, exist_ok=True)
os.makedirs(DIAG, exist_ok=True)

K = 8.0            # wavenumber (c = 1, omega = k)
R_MAX = 10.0       # domain radius in wavelengths units (k R = 80)
R_CORE = 0.05      # vortex core radius (regularisation)
N_R = 360
N_TH = 720
M_MAX = 110        # angular momentum cutoff
ALPHAS = [-0.5, -0.4, -0.3, -0.2, -0.1, 0.1, 0.2, 0.3, 0.4, 0.5]
N_FRAMES = 48
R_ROT = 2.0        # radius of the near-core zone used for rotation metrics


def ab_state(alpha: float, beta: float, r: np.ndarray, th: np.ndarray) -> np.ndarray:
    """AB-scattered wave for incidence direction beta, on the (r, theta) grid.

    psi = sum_m i^(m-alpha) J_{|m-alpha|}(k r) e^{i(m-alpha) theta} e^{-i m beta}

    The order is regularised to |m-alpha| (core-regularised branch, Berry
    1980): the physical vortex has a finite core, and the raw fractional
    orders J_{m-alpha} with m-alpha < 0 diverge at the core. The regularised
    state reproduces the far-field AB phase structure and the forked
    dislocations while staying finite everywhere. With the plane-wave
    phase e^{-i m beta} the exact mirror identity
    psi_{-alpha}(r, -theta) = conj(psi_{alpha}(r, theta))
    holds for every incidence direction.
    """
    m = np.arange(-M_MAX, M_MAX + 1)
    nu = m - alpha                                   # fractional order
    Jm = jv(np.abs(nu)[:, None], (K * r)[None, :])   # (M, Nr) regularised
    ph = np.exp(1j * nu[:, None] * th[None, :] - 1j * m[:, None] * beta)
    pref = (1j ** nu)[:, None]
    # psi = Jm^T @ (pref * ph)   ->  (Nr, Nth)
    return (Jm * pref).T @ ph


def rotation_rate(field_t: list[np.ndarray], th: np.ndarray) -> float:
    """Angular rotation rate of a time-dependent complex field pattern.

    Uses the angular cross-correlation of consecutive frames (FFT in theta).
    """
    dphi = []
    for a, b in zip(field_t[:-1], field_t[1:]):
        # correlation over shifts: c(s) = sum_theta a^*(theta - s) b(theta)
        Fa = np.fft.fft(np.conj(a))
        Fb = np.fft.fft(b)
        c = np.fft.ifft(Fa * Fb).real
        s = np.argmax(c)
        if s > len(th) // 2:
            s -= len(th)
        dphi.append(s * 2 * np.pi / len(th))
    dphi = np.asarray(dphi)
    # unwrap and fit rate per unit time (frame spacing = 1)
    dphi = np.unwrap(dphi)
    return float(np.polyfit(np.arange(len(dphi)), dphi, 1)[0])


def main() -> None:
    t0 = time.time()
    r = np.linspace(R_CORE, R_MAX, N_R)
    th = np.linspace(0.0, 2.0 * np.pi, N_TH, endpoint=False)
    Rg, THg = np.meshgrid(r, th, indexing="ij")
    Xg = Rg * np.cos(THg)
    Yg = Rg * np.sin(THg)

    omega = K  # c = 1
    T_period = 2.0 * np.pi / omega
    times = np.linspace(0.0, 1.0, N_FRAMES, endpoint=False) * T_period
    rot_zone = r <= R_ROT          # near-core annulus for rotation metrics

    metrics = {"K": K, "R_max": R_MAX, "alphas": ALPHAS, "frames": N_FRAMES,
               "rotation_zone_r": R_ROT}
    rot_rates = []
    mirror_corr = []
    windings = []
    windings_neg = []

    for alpha in ALPHAS:
        psi_p = ab_state(+alpha, 0.0, r, th)               # incidence +x
        psi_m = ab_state(+alpha, np.pi, r, th)             # incidence -x
        psi_tot = psi_p + psi_m

        # time frames of the REAL field (what a camera of the surface sees)
        frames = [(psi_tot[rot_zone] * np.exp(-1j * omega * t)).real
                  for t in times]
        rate = rotation_rate([f.mean(axis=0) for f in frames], th)
        rot_rates.append(rate)

        # phase winding around the core (AB signature): total phase
        # accumulation of arg(psi) on the mid annulus
        ring = (r > 1.0) & (r < 1.6)
        phase_line = np.angle(psi_tot[ring].mean(axis=0))
        winding = float(np.sum(np.diff(np.unwrap(phase_line))) / (2 * np.pi))
        windings.append(winding)

        # mirror symmetry of the INTENSITY pattern (exact identity:
        # |psi_{-alpha}(theta)|^2 = |psi_{alpha}(pi - theta)|^2)
        if alpha > 0:
            psi_p_neg = ab_state(-alpha, 0.0, r, th)
            psi_m_neg = ab_state(-alpha, np.pi, r, th)
            tot_neg = psi_p_neg + psi_m_neg
            idx = np.round((np.pi - th) / (2 * np.pi)
                           * N_TH).astype(int) % N_TH
            v1 = (np.abs(psi_tot)**2)[:, idx].ravel()
            v2 = (np.abs(tot_neg)**2).ravel()
            c = float(np.corrcoef(v1, v2)[0, 1])
            mirror_corr.append(c)
            windings_neg.append(float(np.sum(np.diff(np.unwrap(
                np.angle(tot_neg[ring].mean(axis=0))))) / (2 * np.pi)))

        # diagnostic frame (t = T/8)
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        f08 = (psi_tot * np.exp(-1j * omega * times[6])).real
        fig, ax = plt.subplots(figsize=(6.4, 5.6), constrained_layout=True)
        vmax = np.percentile(np.abs(f08), 99)
        im = ax.pcolormesh(Xg, Yg, f08, cmap="RdBu_r", vmin=-vmax, vmax=vmax,
                           shading="nearest", rasterized=True)
        ax.plot(0, 0, "k+", ms=12)
        ax.set_title(f"AB water waves: Re psi, alpha={alpha}, t=T/8")
        ax.set_aspect("equal")
        fig.colorbar(im, ax=ax, shrink=0.85)
        fig.savefig(os.path.join(DIAG, f"ab_alpha{alpha:.1f}.png"), dpi=110)
        plt.close(fig)

    metrics["rotation_rate"] = rot_rates
    metrics["phase_winding"] = windings
    metrics["phase_winding_neg_alpha"] = windings_neg
    metrics["mirror_correlation"] = mirror_corr
    metrics["mirror_min"] = float(np.min(mirror_corr))
    metrics["runtime_s"] = round(time.time() - t0, 2)
    with open(os.path.join(DATA, "AB_water_metrics.json"), "w") as f:
        json.dump(metrics, f, indent=2)
    print(json.dumps(metrics, indent=2), flush=True)


if __name__ == "__main__":
    main()
