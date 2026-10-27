# -*- coding: utf-8 -*-
"""HP-audit computational core — port of hp_audit_standalone.jl detectors.

The full HP-аудит includes a hand-rolled PNG graphics engine (lines 1–2000
of the original) and an interactive shell — those are presentation layers,
NOT physics, and are intentionally out of scope for the port (use the Julia
original for the rendered reports).  What is ported here is the complete
H1 detector machinery and its verdict protocol:

  D1 — raw-position periodogram with a Hann index window
       P(ω) = |Σₖ wₖ e^{−iωTₖ}|² / Σwₖ²  (unfold-free — the Riemann–Weil
       explicit formula makes the zero-density fluctuation a sum of PURE
       TONES in the raw ordinate T, so arithmetic content shows Bragg
       peaks at ω = log p and harmonics k·log p);
  SNR yardstick — P(log p)/median(P) over the scanned band
       (empirically calibrated: ζ control 10⁶–10⁹, GUE/vortex-free
       nulls ≤ 5);
  band scan — ω ∈ [0.3, 3.2] step 0.004 (covers log 2 … log 25);
  D2 — K(t)-residual route (form factor minus GUE envelope, polynomial
       detrend) — retained as a cross-check, intrinsically less sensitive.

Gate conventions (hp_audit_standalone.jl):
  H1 PASS  — ≥ 4 of the 6 prime harmonics (p = 2,3,5,7,11,13) above
             SNR 10 on the same scan;
  H1 STRONG — every SNR above 100.
"""

import math

from .unfold import hp_raw_ft, hp_k_residual, hp_kgue_envelope

PRIMES = (2, 3, 5, 7, 11, 13)
OMEGA_MIN = 0.3
OMEGA_MAX = 3.2
OMEGA_STEP = 0.004
SNR_PEAK = 10.0
SNR_STRONG = 100.0


def default_omega_grid():
    """The audit's band grid: 0.3:0.004:3.2 (726 points)."""
    n = int(round((OMEGA_MAX - OMEGA_MIN) / OMEGA_STEP)) + 1
    return [OMEGA_MIN + OMEGA_STEP * k for k in range(n)]


def nearest_index(grid, omega):
    """First index of the closest grid point (Julia argmin semantics)."""
    best_i, best_d = 0, abs(grid[0] - omega)
    for i in range(1, len(grid)):
        d = abs(grid[i] - omega)
        if d < best_d:
            best_i, best_d = i, d
    return best_i


def median(v):
    s = sorted(v)
    n = len(s)
    mid = n // 2
    return s[mid] if n % 2 == 1 else (s[mid - 1] + s[mid]) / 2.0


def h1_detect(positions, omega_grid=None):
    """Run the H1 primary detector on sorted positions Tₖ.

    Returns dict with the band median and per-prime SNRs."""
    if omega_grid is None:
        omega_grid = default_omega_grid()
    P = hp_raw_ft(list(positions), omega_grid)
    med = median(P)
    out = {"n_positions": len(positions), "band_median": med,
           "n_freq": len(omega_grid), "snr": {}}
    for p in PRIMES:
        i = nearest_index(omega_grid, math.log(p))
        out["snr"][p] = P[i] / med
    n_peaks = sum(1 for v in out["snr"].values() if v >= SNR_PEAK)
    n_strong = sum(1 for v in out["snr"].values() if v >= SNR_STRONG)
    out["n_peaks"] = n_peaks
    out["n_strong"] = n_strong
    out["verdict"] = ("STRONG" if n_strong == len(PRIMES)
                      else "PASS" if n_peaks >= 4 else "NO SIGNAL")
    return out


def h1_report(positions, title="H1 detector"):
    """Human-readable H1 report (computational part of the audit gate)."""
    res = h1_detect(positions)
    lines = [f"{title}: n={res['n_positions']} positions, "
             f"{res['n_freq']} freqs, band median {res['band_median']:.6e}"]
    for p in PRIMES:
        snr = res["snr"][p]
        mark = "PEAK" if snr >= SNR_PEAK else "—"
        strong = " (strong)" if snr >= SNR_STRONG else ""
        lines.append(f"  SNR(log {p:2d}) = {snr:.6e}  [{mark}]{strong}")
    lines.append(f"  verdict: {res['verdict']} "
                 f"({res['n_peaks']}/6 above SNR {SNR_PEAK:.0f})")
    return res, "\n".join(lines)


def h1_null_control(eigs, omega_grid=None):
    """Null control on a lattice (vortex-free) spectrum: the same detector
    must NOT find prime harmonics (SNR ≤ 5 calibrated band)."""
    res = h1_detect(eigs, omega_grid)
    res["expected"] = "no peaks (SNR ≤ 5)"
    return res


def k_residual_rms(eigs, tvals, dpoly: int = 3) -> float:
    """D2 cross-check: RMS of the polynomially detrended K(t) residual
    against the connected GUE envelope."""
    from .gof import compute_K_form_factor
    K = compute_K_form_factor(eigs, tvals)
    res = hp_k_residual(K, tvals, dpoly=dpoly)
    return math.sqrt(sum(r * r for r in res) / len(res))
