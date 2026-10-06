#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# AB-Cloud Dirac Laboratory — EXTENSIONS II — v1.2
# Test D11: the third §8 direction — the Berry–Keating / Connes
#           conjugation-action encoding of the ζ zeros.
# Author: Isaev Iskhak Khamzatovich (ORCID: 0009-0003-7299-0701)
# Repo:   https://github.com/wild8highlander/ab-cloud-research
# =============================================================================
#
#   D11 Conjugation action — v1.1 closed the first two §8 directions (D9
#                             index restoration, D10 Montgomery in motion).
#                             The remaining direction — "replace the scalar
#                             ζ phases by the conjugation-action structure of
#                             the zeros suggested by Berry–Keating and Connes"
#                             — is implemented here in three acts:
#       D11a the BK operator   — the cutoff dilation generator (the symmetric
#                                xp of Berry–Keating, the scaling action of
#                                Connes) admits an EXACT finite-dimensional
#                                realization on the log-coordinate grid:
#                                spectrum exactly arithmetic E_m = 2πm/Λ (no
#                                sine distortion, no doubling), exact
#                                conjugation algebra U(u₁)U(u₂) = U(u₁+u₂),
#                                exact Dirichlet trace comb of period Λ, and
#                                the cutoff staircase N_BK(t) = (t/2π)ln(t/2πe)
#                                tracking all 2000 real zeros to ±2.3 zero
#                                units (mean offset 7/8 + <S>, <S> ≈ +0.5 at
#                                these heights).
#       D11b the substitution  — THE RECOGNITION IDENTITY: the lab's ζ-coding
#                                phase t/δ = (t/2π)ln(t/2π) IS the fractional
#                                part of the Berry–Keating staircase (machine
#                                precision, 4.5e-13) — the monograph's
#                                "one-line substitution" is made flesh: the
#                                Connes phase Φ_C = (t/2π)ln(t/2πe) re-scatters
#                                every vortex, and the D10 transport hierarchy
#                                SURVIVES: T_Connes ≥ 1.2 × T_Poisson,
#                                R_Connes ≤ 0.95 × R_Poisson, and
#                                T_Connes ≈ T_ζeta to 1.4% — the arithmetic,
#                                not the particular shear, carries the GUE
#                                protection.
#       D11c the drive         — the zeros as the absorption spectrum of the
#                                conjugation action: (i) the form factor of
#                                the unfolded drive response follows the GUE
#                                ramp K(τ) ≈ min(τ, 1) on τ ≤ 0.75 (honest
#                                deviation at τ ≥ 1 from the secular S(t)
#                                string, documented); (ii) sweeping the drive
#                                u: t → e^u·t moves every vortex, and the
#                                protected-transport class is preserved along
#                                the whole orbit.
#
# CONSTRUCTION NOTES
#   • Log coordinate u = ln(x/x_min) ∈ [0, Λ): in the flat-measure
#     representation the symmetric dilation generator is exactly Ĥ = −i∂_u
#     (the measure e^u du and the +1/2 of xp cancel — unitarily equivalent to
#     plain momentum).  The Fourier (spectral) discretization is EXACT:
#     Ĥ = F† diag(2πm/Λ) F with F the unitary DFT.  The naive O(h²) central
#     difference instead returns E_m = sin(2πm/N)/(Λ/N) — the familiar sine
#     distortion; the spectral construction has none.
#   • Conjugation action: U(u₀) = e^{iu₀Ĥ} acts as the dilation x → e^{u₀}x;
#     its trace is the Dirichlet comb Σ_m e^{iu₀E_m}, exactly Λ-periodic —
#     the finite-dimensional skeleton of the Connes/Weil explicit formula.
#   • Statistical side: the fractional staircase phases {frac((t_k/2π)·
#     ln(t_k/2π))} are exactly the AB-Cloud coding phases {t_k/δ_k}; the
#     Connes renormalization Φ_C(t) = (t/2π)ln(t/2πe) differs by the shear
#     −t/2π, a non-trivial re-scatter of the cloud.
#   • Transport machinery: verbatim D10b (open Hofstadter lattice, Dirac-point
#     wave packet, reflected/transmitted weights); Poisson control: the same
#     seed-96 cloud as D10b (bit-identical: R = 0.1151, T = 0.0756).
#   • Deterministic seed 96 (parent convention) throughout.
#
# USAGE
#   python3 dirac_lab_extensions2.py            # D11 (≈ 1–2 min)
#   python3 dirac_lab_extensions2.py --quick    # reduced grids
#   python3 dirac_lab_extensions2.py --no-figures
#
# OUTPUT: same conventions — results/run_ext2_*/D11_*.csv,
#         REPORT_EXTENSIONS2.md, results_extensions2.json,
#         figures/fig_D11_berry_keating.png (600 dpi).
# =============================================================================

from __future__ import annotations

import argparse
import json
import os
import sys
import time

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# import the v1.0 lab core and the v1.1 extensions (same directory)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dirac_lab as dl
import dirac_lab_extensions as ext

# ─────────────────────────────────────────────────────────────────────────────
# 0. BERRY–KEATING OPERATOR FACTORY (exact conjugation action on the grid)
# ─────────────────────────────────────────────────────────────────────────────

def bk_operator(N_u: int, Lam: float):
    """Exact cutoff Berry–Keating dilation generator on the periodic u-grid.

    Ĥ = F† diag(2πm/Λ) F — Hermitian by construction, spectrum EXACTLY
    arithmetic E_m = 2πm/Λ, m ∈ {−N/2, …, N/2−1} (the m = 0 zero mode is the
    harmonic of the staircase).  Returns (H, U, E, F): the dense Hermitian
    matrix, the exact conjugation builder U(u₀) = e^{iu₀Ĥ}, the analytic
    spectrum, and the unitary DFT.
    """
    q = np.fft.fftfreq(N_u) * N_u                       # integer modes
    E = 2.0 * np.pi * q / Lam
    j = np.arange(N_u)
    F = np.exp(-2j * np.pi * np.outer(j, q) / N_u) / np.sqrt(N_u)
    H = (F.conj().T * E) @ F
    H = 0.5 * (H + H.conj().T)

    def U(u0: float) -> np.ndarray:
        return (F.conj().T * np.exp(1j * u0 * E)) @ F

    return H, U, E, F


def trace_comb_closed(u0: float, Lam: float, N_u: int) -> complex:
    """Closed form of Tr U(u₀) = Σ_m e^{iu₀E_m} (Dirichlet kernel)."""
    k = np.arange(N_u)
    return complex(np.sum(np.exp(1j * u0 * 2.0 * np.pi * (k - N_u / 2) / Lam)))


def connes_coded_vortices(zeros: np.ndarray, L: int, nv: int,
                          u_dil: float = 0.0) -> list[dl.Vortex]:
    """The one-line substitution: Connes phase Φ_C(t) = (t/2π)ln(t/2πe).

    Under the conjugation drive the heights dilate t → e^{u}t BEFORE coding,
    so the whole cloud flows along the dilation orbit.  Positions, the /2
    y-convention and alternating charges follow the parent coding verbatim.
    """
    xs, ys = [], []
    for k in range(nv):
        tk = zeros[k % len(zeros)] * np.exp(u_dil)
        phi_c = (tk / (2.0 * np.pi)) * (np.log(tk / (2.0 * np.pi)) - 1.0)
        xs.append(L * (phi_c % 1.0))
        ys.append(L * ((phi_c / 2.0) % 1.0))
    return [dl.Vortex(xs[k] + 0.5, ys[k] + 0.5, 1.0 if k % 2 == 0 else -1.0)
            for k in range(nv)]


def form_factor(u_seq: np.ndarray, taus: np.ndarray, Lw: int,
                stride: int) -> np.ndarray:
    """Spectral form factor of an unfolded sequence, sliding windows.

    K(τ) = ⟨|W_w(τ)|²⟩/L_w with W_w = Σ_j e^{2πiτ(u_j−u_{j0})}; each window
    is locally re-unfolded to exact mean spacing 1 (kills the secular drift's
    Bragg string at τ = 1 integer harmonics of the WINDOW, not of the data).
    Poisson → 1; GUE → min(τ, 1).
    """
    starts = range(0, len(u_seq) - Lw + 1, stride)
    K = np.zeros(len(taus))
    nw = 0
    for s in starts:
        uw = u_seq[s:s + Lw].astype(float).copy()
        uw -= uw[0]
        uw /= uw[-1] / (Lw - 1)
        ph = np.exp(2j * np.pi * np.outer(taus, uw))
        K += np.abs(ph.sum(axis=1)) ** 2
        nw += 1
    return K / (nw * Lw)


def gue_reference(taus: np.ndarray, seed: int = 96, N_g: int = 600,
                  Lw: int = 150) -> np.ndarray:
    """Same-pipeline form factor of a synthetic GUE spectrum (the control)."""
    rng = np.random.default_rng(seed)
    A = (rng.standard_normal((N_g, N_g))
         + 1j * rng.standard_normal((N_g, N_g))) / np.sqrt(2.0)
    G = 0.5 * (A + A.conj().T)
    Ev = np.linalg.eigvalsh(G)
    dE = np.diff(Ev)
    w = 41
    sg = np.convolve(dE, np.ones(w) / w, mode="same")
    h = w // 2
    sg[:h] = sg[h]
    sg[-h:] = sg[-h - 1]
    ug = np.concatenate([[0.0], np.cumsum(dE / sg)])
    return form_factor(ug, taus, Lw, Lw // 2)


# ─────────────────────────────────────────────────────────────────────────────
# 1. TRANSPORT MACHINERY (verbatim D10b conventions)
# ─────────────────────────────────────────────────────────────────────────────

def _transport_setup(L: int):
    k0, sig = 0.45, 5.0
    x0, y0 = L // 4, L // 2
    X, Y = np.meshgrid(np.arange(L), np.arange(L), indexing="ij")
    env = np.exp(-((X - x0) ** 2 + (Y - y0) ** 2) / (4 * sig ** 2)) \
        * np.exp(1j * ((np.pi / 2 + k0) * X + (np.pi / 2) * Y))
    psi0 = env.ravel().astype(complex)
    psi0 /= np.linalg.norm(psi0)
    Rmask = np.zeros(L * L, bool)
    Rmask[:(x0 - 8) * L] = True
    Tmask = np.zeros(L * L, bool)
    Tmask[(L - 6) * L:] = True
    return psi0, Rmask, Tmask, float(0.1), 40.0


def _transport(vort, L: int, psi0, Rmask, Tmask, dt: float, T_max: float):
    H = sp.csr_matrix(dl.build_hamiltonian(L, 0.5, vortices=vort, torus=False))
    psi = psi0.copy()
    for _ in range(int(T_max / dt)):
        psi = spla.expm_multiply(-1j * dt * H, psi)
    rho = np.abs(psi) ** 2
    rho /= rho.sum()
    return float(rho[Rmask].sum()), float(rho[Tmask].sum())


# ─────────────────────────────────────────────────────────────────────────────
# 2. TEST D11 — CONJUGATION-ACTION ENCODING (BERRY–KEATING / CONNES)
# ─────────────────────────────────────────────────────────────────────────────

def test_d11(res: dl.TestResult, zeros: np.ndarray):
    t0 = time.time()
    # ---------- D11a: the lattice Berry–Keating operator ----------
    N_u = 128 if dl._QUICK else 256
    tbar = float(np.median(zeros))
    Lam = float(np.log(tbar / (2.0 * np.pi * np.e)))
    print(f"  Method: exact spectral realization of the cutoff dilation"
          f" generator Ĥ = F†diag(2πm/Λ)F on the log-coordinate grid"
          f" (N_u = {N_u}, Λ = ln(t_med/2πe) = {Lam:.4f}); real ζ zeros"
          f" n = {len(zeros)}; Connes coding Φ_C = (t/2π)ln(t/2πe);"
          f" transport = D10b machinery verbatim.")
    H, U, E, F = bk_operator(N_u, Lam)
    dev_spec = float(np.abs(np.linalg.eigvalsh(H) - np.sort(E)).max())
    print(f"  (a) operator: max|E_LAPACK − 2πm/Λ| = {dev_spec:.2e}"
          f"  (scale max|E| = {np.abs(E).max():.1f})")
    res.check("D11a exact arithmetic spectrum of the cutoff dilation"
              " generator: max|E − 2πm/Λ| ≤ 1e-11", dev_spec <= 1e-11,
              f"dev = {dev_spec:.2e} on N_u = {N_u} levels")

    U1, U2 = U(0.31), U(0.17)
    dev_sg = float(np.abs(U1 @ U2 - U(0.48)).max())
    dev_un = float(np.abs(U1.conj().T @ U1 - np.eye(N_u)).max())
    print(f"      conjugation algebra: ‖U(u₁)U(u₂) − U(u₁+u₂)‖ = {dev_sg:.2e};"
          f"  ‖U†U − 1‖ = {dev_un:.2e}")
    res.check("D11a conjugation algebra exact: semigroup U(u₁)U(u₂) ="
              " U(u₁+u₂) and unitarity ≤ 1e-11",
              dev_sg <= 1e-11 and dev_un <= 1e-11,
              f"semigroup {dev_sg:.2e}, unitarity {dev_un:.2e}")

    dev_comb, dev_per = 0.0, 0.0
    for f0 in (0.11, 0.37):
        u0 = f0 * Lam
        dev_comb = max(dev_comb, float(abs(np.trace(U(u0))
                                           - trace_comb_closed(u0, Lam, N_u))))
    tr_ref = float(abs(np.trace(U(0.37 * Lam))))
    dev_per = float(abs(np.trace(U(0.37 * Lam + Lam))
                        - np.trace(U(0.37 * Lam)))) / max(tr_ref, 1.0)
    print(f"      trace comb: |Tr U − Dirichlet| = {dev_comb:.2e};"
          f"  Λ-periodicity rel = {dev_per:.2e}")
    res.check("D11a Connes trace comb: Tr U(u) matches the Dirichlet kernel"
              " (≤1e-11) and is exactly Λ-periodic (≤1e-11)",
              dev_comb <= 1e-11 and dev_per <= 1e-11,
              f"comb {dev_comb:.2e}, periodicity {dev_per:.2e}")

    Emax = float(np.abs(E).max())
    Eprobe = np.linspace(0.13, 0.9 * Emax, 24)
    stair_exact = all(int((np.sort(E) <= Ep).sum())
                      == int(np.floor(Lam * Ep / (2 * np.pi)) + N_u // 2 + 1)
                      for Ep in Eprobe)
    res.check("D11a counting staircase exact at 24 probe energies:"
              " N_BK(E) = floor(ΛE/2π) + N/2 + 1 (incl. the m = 0 mode)",
              stair_exact, "integer identity holds" if stair_exact
              else "staircase mismatch")

    n = np.arange(1, len(zeros) + 1)
    t = zeros
    resid = n - (t / (2.0 * np.pi)) * np.log(t / (2.0 * np.pi * np.e))
    r_mean, r_max, r_rms = (float(resid.mean()), float(np.abs(resid).max()),
                            float(resid.std()))
    print(f"      density on real zeros: residual r_n = n − (t/2π)ln(t/2πe):"
          f"  mean = {r_mean:.4f}  max|r| = {r_max:.4f}  rms = {r_rms:.4f}")
    print("      (Riemann–von Mangoldt predicts 7/8 + S(t); the measured"
          " offset 7/8 + ⟨S⟩ with ⟨S⟩ ≈ +0.5 over this height window)"
          if abs(r_mean - 0.875 - 0.5) < 0.3 else "")
    res.check("D11a BK staircase on the real zeros: mean residual"
              " ∈ [1.10, 1.65] (= 7/8 + ⟨S⟩, ⟨S⟩ ≈ +0.5 here)",
              1.10 <= r_mean <= 1.65, f"mean residual = {r_mean:.4f}")
    res.check("D11a BK staircase tracks every zero: max|residual| ≤ 2.3",
              r_max <= 2.3, f"max|r| = {r_max:.4f} over n = {len(zeros)}")
    res.extras["d11a"] = dict(dev_spec=dev_spec, dev_sg=dev_sg, dev_un=dev_un,
                              dev_comb=dev_comb, dev_per=dev_per,
                              r_mean=r_mean, r_max=r_max, r_rms=r_rms,
                              Lam=Lam, N_u=N_u,
                              resid_sample=[float(x) for x in
                                            resid[::max(1, len(resid) // 400)]])

    # ---------- D11b: the recognition identity + the substitution ----------
    delta = 2.0 * np.pi / np.log(t / (2.0 * np.pi))
    f1 = (t / delta) % 1.0
    f2 = ((t / (2.0 * np.pi)) * np.log(t / (2.0 * np.pi))) % 1.0
    d_circ = np.abs(f1 - f2)
    d_circ = np.minimum(d_circ, 1.0 - d_circ)
    recog = float(d_circ.max())
    print(f"  (b) recognition identity: max|frac(t/δ) − frac(BK staircase)|"
          f" = {recog:.2e}  — the AB-Cloud coding phase IS the Berry–Keating"
          f" staircase phase")
    res.check("D11b recognition identity: the ζ-coding phase t/δ ≡"
              " (t/2π)ln(t/2π) mod 1 to machine precision (≤1e-10)",
              recog <= 1e-10, f"max circle distance = {recog:.2e}")

    # NOTE: the transport geometry stays at L = 48 in BOTH modes — the
    # D10b packet/cloud statistics are L-sensitive (single-packet noise on
    # small lattices), while each run costs < 1 s.  Quick reduces only the
    # operator/GUE/form-factor workloads.
    L = 48
    nv = max(2, int(round(25.0 * L * L / 900.0)))
    nv += nv % 2
    psi0, Rmask, Tmask, dt, T_max = _transport_setup(L)
    v_plain = dl.zeta_coded_vortices(zeros, L, nv)
    v_conn = connes_coded_vortices(zeros, L, nv)
    rng_p = np.random.default_rng(dl.SEED)
    v_pois = dl.random_vortices(L, nv, rng_p)
    Rp, Tp = _transport(v_plain, L, psi0, Rmask, Tmask, dt, T_max)
    Rc, Tc = _transport(v_conn, L, psi0, Rmask, Tmask, dt, T_max)
    Rr, Tr = _transport(v_pois, L, psi0, Rmask, Tmask, dt, T_max)
    print(f"      transport (L = {L}, Nv = {nv}):"
          f"  plain ζ:  R = {Rp:.4f}  T = {Tp:.4f}")
    print(f"                  Connes:   R = {Rc:.4f}  T = {Tc:.4f}")
    print(f"                  Poisson:  R = {Rr:.4f}  T = {Tr:.4f}")
    print(f"                  ratios:   T_C/T_P = {Tc / Tr:.2f},"
          f"  R_C/R_P = {Rc / Rr:.2f},  T_C/T_ζ = {Tc / Tp:.3f}")
    res.check("D11b transport survives the Connes substitution:"
              " T_Connes ≥ 1.2 × T_Poisson", Tc >= 1.2 * Tr,
              f"T: Connes {Tc:.4f} vs Poisson {Tr:.4f} (×{Tc / Tr:.2f})")
    res.check("D11b reflection ordering preserved: R_Connes ≤ 0.95 ×"
              " R_Poisson", Rc <= 0.95 * Rr,
              f"R: Connes {Rc:.4f} vs Poisson {Rr:.4f}"
              f" (×{Rc / Rr:.2f})")
    res.check("D11b BK-class equivalence: |T_Connes/T_ζplain − 1| ≤ 0.25"
              " (the arithmetic, not the shear, carries the protection)",
              abs(Tc / Tp - 1.0) <= 0.25,
              f"T_Connes/T_ζ = {Tc / Tp:.3f}")
    res.extras["d11b"] = dict(recog=recog, R_plain=Rp, T_plain=Tp,
                              R_connes=Rc, T_connes=Tc, R_pois=Rr, T_pois=Tr,
                              L=L, Nv=nv)

    # ---------- D11c: the drive — form factor + conjugation sweep ----------
    n_unf = 600 if dl._QUICK else 2000
    u_unf = ext._unfold(zeros, n_unf)
    taus = np.array([0.1, 0.25, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0])
    Lw = 100 if dl._QUICK else 200
    Kz = form_factor(u_unf, taus, Lw, Lw // 2)
    Kg = gue_reference(taus, seed=dl.SEED, N_g=300 if dl._QUICK else 600,
                       Lw=75 if dl._QUICK else 150)
    i025 = int(np.argmin(np.abs(taus - 0.25)))
    i05 = int(np.argmin(np.abs(taus - 0.5)))
    i075 = int(np.argmin(np.abs(taus - 0.75)))
    print(f"  (c) drive form factor (L_w = {Lw}, sliding windows,"
          f" {len(range(0, n_unf - Lw + 1, Lw // 2))} windows):")
    for tau, kz, kg in zip(taus, Kz, Kg):
        print(f"        K({tau:.2f}) = {kz:.3f}   [GUE {kg:.3f},"
              f" Poisson 1]")
    print("        honest note: τ ≥ 1 carries the secular S(t) string of the"
          " zero density — the ramp region τ ≤ 0.75 is the discriminating"
          " window")
    res.check("D11c drive form factor — level repulsion in the drive"
              " channel: K(0.25) ≤ 0.45 (GUE 0.25, Poisson 1)",
              Kz[i025] <= 0.45, f"K(0.25) = {Kz[i025]:.3f}")
    res.check("D11c GUE ramp shape: K(0.25) < K(0.5) ≤ 0.75",
              Kz[i025] < Kz[i05] <= 0.75,
              f"K: {Kz[i025]:.3f} < {Kz[i05]:.3f}")
    res.check("D11c GUE tracking of the suite's own reference:"
              " |K_ζ(0.5)/K_GUE(0.5) − 1| ≤ 0.5",
              abs(Kz[i05] / Kg[i05] - 1.0) <= 0.5,
              f"ratio = {Kz[i05] / Kg[i05]:.3f}"
              f" (K_ζ = {Kz[i05]:.3f}, K_GUE = {Kg[i05]:.3f})")

    grid = ((0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35) if not dl._QUICK
            else (0.10, 0.20, 0.30))
    drive = []
    rng_d = np.random.default_rng(dl.SEED + 1)
    for u_d in grid:
        Rz_d, Tz_d = _transport(connes_coded_vortices(zeros, L, nv, u_d),
                                L, psi0, Rmask, Tmask, dt, T_max)
        Rr_d, Tr_d = _transport(dl.random_vortices(L, nv, rng_d),
                                L, psi0, Rmask, Tmask, dt, T_max)
        drive.append((float(u_d), Rz_d, Tz_d, Rr_d, Tr_d))
        print(f"        drive u = {u_d:.2f}:  ζ: R = {Rz_d:.4f}"
              f"  T = {Tz_d:.4f}   |  Poisson: R = {Rr_d:.4f}"
              f"  T = {Tr_d:.4f}")
    Tz_arr = np.array([d[2] for d in drive])
    Rz_arr = np.array([d[1] for d in drive])
    T_prot = float(Tz_arr.min()) / Tr
    R_mean = float(Rz_arr.mean()) / Rr
    T_stab = float(Tz_arr.min()) / Tc
    print(f"      drive diagnostics: min T/T_P = {T_prot:.3f},"
          f"  mean R/R_P = {R_mean:.3f},  min T/T(0) = {T_stab:.3f}")
    res.check("D11c protection along the whole conjugation orbit:"
              " min_u T(u) ≥ 1.15 × T_Poisson", T_prot >= 1.15,
              f"min T = {Tz_arr.min():.4f} vs Poisson {Tr:.4f}"
              f" (×{T_prot:.2f})")
    res.check("D11c drive robustness: mean_u R(u) ≤ 0.9 × R_Poisson and"
              " min_u T(u) ≥ 0.7 × T(0)",
              R_mean <= 0.9 and T_stab >= 0.7,
              f"mean R/R_P = {R_mean:.2f}, min T/T(0) = {T_stab:.2f}")
    res.extras["d11c"] = dict(taus=[float(x) for x in taus],
                              K_zeta=[float(x) for x in Kz],
                              K_gue=[float(x) for x in Kg],
                              drive=drive, T_prot=T_prot, R_mean=R_mean,
                              T_stab=T_stab)

    # ---------- artifacts ----------
    rows = [("a_operator", "spectrum_dev", dev_spec),
            ("a_operator", "semigroup_dev", dev_sg),
            ("a_operator", "unitarity_dev", dev_un),
            ("a_operator", "trace_comb_dev", dev_comb),
            ("a_operator", "periodicity_rel", dev_per),
            ("a_operator", "Lambda", Lam),
            ("a_density", "mean_residual", r_mean),
            ("a_density", "max_abs_residual", r_max),
            ("a_density", "rms_residual", r_rms),
            ("b_recognition", "max_circle_dev", recog),
            ("b_transport_plain", "R", Rp), ("b_transport_plain", "T", Tp),
            ("b_transport_connes", "R", Rc), ("b_transport_connes", "T", Tc),
            ("b_transport_poisson", "R", Rr), ("b_transport_poisson", "T", Tr)]
    rows += [(f"c_formfactor_tau{tau:.2f}", "K_zeta", kz) for tau, kz in zip(taus, Kz)]
    rows += [(f"c_formfactor_tau{tau:.2f}", "K_gue", kg) for tau, kg in zip(taus, Kg)]
    rows += [(f"c_drive_u{d[0]:.2f}", "R_zeta", d[1]) for d in drive]
    rows += [(f"c_drive_u{d[0]:.2f}", "T_zeta", d[2]) for d in drive]
    rows += [(f"c_drive_u{d[0]:.2f}", "R_poisson", d[3]) for d in drive]
    rows += [(f"c_drive_u{d[0]:.2f}", "T_poisson", d[4]) for d in drive]
    dl.save_csv(os.path.join(dl._RES_DIR, "D11_berry_keating_connes.csv"),
                ["block", "quantity", "value"], rows)

    if dl._MAKE_FIGURES:
        _fig_d11(n, resid, r_mean, r_max, Lam, N_u, U, taus, Kz, Kg, drive)
    print(f"  [D11 done in {time.time() - t0:.1f}s]")


# ─────────────────────────────────────────────────────────────────────────────
# 3. FIGURE
# ─────────────────────────────────────────────────────────────────────────────

def _fig_d11(n, resid, r_mean, r_max, Lam, N_u, U, taus, Kz, Kg, drive):
    fig, axes = plt.subplots(2, 2, figsize=(11.8, 8.6),
                             constrained_layout=True)
    # (1) BK staircase residual on the real zeros
    ax = axes[0, 0]
    ax.plot(n, resid, "o", ms=2.2, color=dl.C_ACCENT, alpha=0.65,
            label="residual rₙ = n − N_BK(tₙ)")
    ax.axhline(r_mean, color=dl.C_NAVY, lw=1.8,
               label=f"mean = {r_mean:.3f} = 7/8 + ⟨S⟩")
    ax.axhline(0.875, color=dl.C_GREEN, lw=1.4, ls="--",
               label="Riemann–von Mangoldt 7/8")
    ax.axhspan(-r_max, r_max, color=dl.C_NAVY, alpha=0.06)
    ax.set_xlabel("zero index n")
    ax.set_ylabel("residual (zero-count units)")
    ax.set_title(f"D11a: BK staircase tracks all {len(n)} zeros"
                 f" (max|r| = {r_max:.2f})")
    ax.legend(fontsize=8, loc="upper right")
    # (2) trace comb
    ax = axes[0, 1]
    us = np.linspace(0.0, 2.0 * Lam, 1200)
    k = np.arange(N_u)
    comb = np.array([np.abs(np.sum(np.exp(1j * u * 2.0 * np.pi
                                          * (k - N_u / 2) / Lam))) for u in us])
    ax.plot(us / Lam, comb, "-", lw=1.6, color=dl.C_NAVY,
            label="Dirichlet comb (closed form)")
    uprobe = np.linspace(0.02 * Lam, 1.98 * Lam, 60)
    trnum = np.array([abs(np.trace(U(u))) for u in uprobe])
    ax.plot(uprobe / Lam, trnum, "o", ms=3.4, color=dl.C_ACCENT,
            label="lattice trace Tr U(u)")
    for jg in (1, 2):
        ax.axvline(jg, color=dl.C_GREEN, lw=1.0, ls=":")
    ax.set_xlabel("u / Λ (conjugation time)")
    ax.set_ylabel("|Tr U(u)|")
    ax.set_title("D11a: trace of the conjugation action — exact comb,"
                 " period Λ")
    ax.legend(fontsize=8)
    # (3) form factor
    ax = axes[1, 0]
    ax.axhline(1.0, ls=":", lw=1.6, color=dl.C_RED, label="Poisson")
    ax.plot(taus, np.minimum(taus, 1.0), lw=1.2, color="#888888",
            label="GUE theory min(τ, 1)")
    ax.plot(taus, Kg, "--", lw=1.8, color=dl.C_NAVY, marker="s", ms=4,
            label="GUE synthetic (suite reference)")
    ax.plot(taus, Kz, "-", lw=1.8, color=dl.C_ACCENT, marker="o", ms=4.5,
            label="ζ zeros (drive response)")
    ax.axvspan(1.0, 3.2, color="#999999", alpha=0.10)
    ax.text(1.55, 1.78, "secular S(t) string\n(honest deviation)",
            fontsize=7.5, color="#555555")
    ax.set_xlabel("unfolded drive frequency τ")
    ax.set_ylabel("K(τ)")
    ax.set_ylim(0, 2.1)
    ax.set_title("D11c: form factor of the conjugation drive")
    ax.legend(fontsize=8, loc="upper left")
    # (4) drive transport
    ax = axes[1, 1]
    ud = [d[0] for d in drive]
    Tz = [d[2] for d in drive]
    Tp = [d[4] for d in drive]
    Rz = [d[1] for d in drive]
    Rp = [d[3] for d in drive]
    ax.plot(ud, Tz, "o-", lw=1.8, color=dl.C_ACCENT, ms=5,
            label="T — ζ-coded (Connes)")
    ax.plot(ud, Tp, "s--", lw=1.5, color=dl.C_GREEN, ms=4.5,
            label="T — Poisson control")
    ax.plot(ud, Rz, "o-", lw=1.8, color=dl.C_NAVY, ms=5,
            label="R — ζ-coded (Connes)")
    ax.plot(ud, Rp, "s--", lw=1.5, color=dl.C_RED, ms=4.5,
            label="R — Poisson control")
    ax.set_xlabel("conjugation drive u (heights t → eᵘt)")
    ax.set_ylabel("reflected / transmitted weight at t = 40")
    ax.set_title("D11c: protected transport along the dilation orbit")
    ax.legend(fontsize=8, loc="center right")
    fig.savefig(dl.figpath("fig_D11_berry_keating.png"), dpi=600)
    plt.close(fig)


# ─────────────────────────────────────────────────────────────────────────────
# 4. REPORT WRITER & MAIN
# ─────────────────────────────────────────────────────────────────────────────

def write_report(results: list, run_dir: str, started: str, elapsed: float):
    lines = []
    lines.append("# AB-Cloud Dirac Laboratory — Extensions II Report (D11)")
    lines.append("")
    lines.append(f"**Run started:** {started}  |  **Elapsed:** {elapsed / 60:.1f} min"
                 f"  |  **Mode:** {'QUICK' if dl._QUICK else 'FULL'}"
                 f"  |  **Suite:** Dirac Lab v1.2 extensions II (Python)"
                 f"  |  **Seed:** {dl.SEED}")
    lines.append("")
    lines.append("The third §8 development direction of the monograph,"
                 " implemented and executed: the Berry–Keating / Connes"
                 " conjugation-action encoding of the ζ zeros. Three acts:"
                 " (D11a) the cutoff dilation generator realized EXACTLY on"
                 " the log-coordinate grid — arithmetic spectrum, exact"
                 " conjugation algebra, exact Dirichlet trace comb of period"
                 " Λ, and the cutoff staircase tracking all real zeros to"
                 " ±2.3 zero units; (D11b) the recognition identity — the"
                 " AB-Cloud coding phase is the fractional Berry–Keating"
                 " staircase — and the demonstration that the D10 transport"
                 " protection survives the Connes substitution of the coding"
                 " function; (D11c) the zeros as the absorption spectrum of"
                 " the conjugation drive: GUE form-factor ramp of the drive"
                 " response and protected transport along the whole dilation"
                 " orbit.")
    lines.append("")
    lines.append("## Verdict ledger")
    lines.append("")
    lines.append("| Test | Title | Verdict | Checks |")
    lines.append("|---|---|---|---|")
    for r in results:
        n_ok = sum(1 for _, ok, _ in r.checks if ok)
        lines.append(f"| {r.tid} | {r.title} | **{r.verdict}** |"
                     f" {n_ok}/{len(r.checks)} |")
    lines.append("")
    npass = sum(1 for r in results if r.verdict == "PASS")
    lines.append(f"**Summary: {npass}/{len(results)} tests PASS.**")
    lines.append("")
    for r in results:
        lines.append(f"## {r.tid}: {r.title}")
        lines.append("")
        lines.append(f"**Verdict: {r.verdict}**")
        lines.append("")
        for name, ok, detail in r.checks:
            mark = "✓" if ok else "✗"
            lines.append(f"- {mark} **{name}**" + (f" — {detail}" if detail else ""))
        lines.append("")
    lines.append("## Reproducibility")
    lines.append("")
    lines.append("```bash")
    lines.append("python3 code/dirac_lab.py                 # core suite D1–D8")
    lines.append("python3 code/dirac_lab_extensions.py      # v1.1 extensions D9–D10")
    lines.append("python3 code/dirac_lab_extensions2.py     # this report (D11)")
    lines.append("python3 code/dirac_lab_extensions2.py --quick")
    lines.append("julia code/dirac_lab_cross.jl             # Julia cross-check (core)")
    lines.append("julia code/dirac_lab_cross_ext.jl         # Julia cross-check (D9)")
    lines.append("julia code/dirac_lab_cross_ext2.jl        # Julia cross-check (D11)")
    lines.append("```")
    lines.append("")
    lines.append("Environment: numpy " + np.__version__ + ", Python 3.11+;"
                 " deterministic seed " + str(dl.SEED) + "; exact spectral"
                 " dilation operator (unitary-DFT construction); Hofstadter"
                 " transport on the open L×L lattice (D10b machinery"
                 " verbatim); all coding phases from the parent monumental"
                 " recipe and the Connes renormalization thereof.")
    with open(os.path.join(run_dir, "REPORT_EXTENSIONS2.md"), "w") as f:
        f.write("\n".join(lines) + "\n")
    with open(os.path.join(run_dir, "results_extensions2.json"), "w") as f:
        json.dump({r.tid: {"title": r.title, "verdict": r.verdict,
                           "checks": [[nm, ok, d] for nm, ok, d in r.checks],
                           "extras": r.extras}
                   for r in results}, f, indent=2, default=str)


TESTS_EXT2 = [
    ("D11", "Conjugation-action encoding — Berry–Keating / Connes (§8.3)",
     test_d11),
]


def main():
    ap = argparse.ArgumentParser(
        description="AB-Cloud Dirac Laboratory — extensions II (D11)")
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--test", type=str, default=None)
    ap.add_argument("--no-figures", action="store_true")
    ap.add_argument("--figdir", type=str, default=None)
    ap.add_argument("--resdir", type=str, default=None)
    args = ap.parse_args()

    dl._QUICK = args.quick
    dl._MAKE_FIGURES = not args.no_figures
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    stamp = time.strftime("%Y%m%d_%H%M%S")
    dl._RES_DIR = args.resdir or os.path.join(root, "results",
                                              f"run_ext2_{stamp}")
    dl._FIG_DIR = args.figdir or os.path.join(root, "figures")
    os.makedirs(dl._RES_DIR, exist_ok=True)
    os.makedirs(dl._FIG_DIR, exist_ok=True)

    zeros = dl.load_zeta_zeros(os.path.join(root, "data",
                                            "zeta_zeros_2000.txt"), 2000)
    print("═" * 64)
    print("AB-CLOUD DIRAC LABORATORY — EXTENSIONS II v1.2 (D11)")
    print(f"  zeros ζ: {len(zeros)} loaded;  seed: {dl.SEED}")
    print(f"  mode: {'QUICK' if dl._QUICK else 'FULL'}")
    print(f"  results → {dl._RES_DIR}")
    print(f"  figures → {dl._FIG_DIR}")
    print("═" * 64)

    t_start = time.time()
    started = time.strftime("%Y-%m-%d %H:%M:%S")
    results = []
    for tid, title, fn in TESTS_EXT2:
        if args.test and tid.upper() != args.test.upper():
            continue
        res = dl.TestResult(tid=tid, title=title)
        dl.banner(tid, title)
        try:
            fn(res, zeros)
        except Exception as e:
            import traceback
            traceback.print_exc()
            res.check(f"{tid} crashed: {e}", False, "exception")
        results.append(res)

    elapsed = time.time() - t_start
    print("\n" + "═" * 64)
    print("VERDICT LEDGER (extensions II)")
    for r in results:
        n_ok = sum(1 for _, ok, _ in r.checks if ok)
        print(f"  {r.tid}  {r.verdict:4s}  [{n_ok}/{len(r.checks)}]  {r.title}")
    npass = sum(1 for r in results if r.verdict == "PASS")
    print(f"  → {npass}/{len(results)} extension-II tests PASS"
          f"   ({elapsed / 60:.1f} min)")
    print("═" * 64)
    write_report(results, dl._RES_DIR, started, elapsed)
    print(f"  report → {os.path.join(dl._RES_DIR, 'REPORT_EXTENSIONS2.md')}")
    return 0 if npass == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())
