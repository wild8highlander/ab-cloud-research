#!/usr/bin/env python3
"""
e6_eta_scan.py — E6: parameter scan over the anisotropy strength eta.

Study W1 extension (Hyperbolic wave attractors, AB-Cloud Research).

Physics
-------
The two dimensionless controls of the hyperbolic billiard are the slope
length s of the shallow walls and the anisotropy eta of the medium
(mu = diag(1, -eta)). E6a maps the lock-in probability P(lock) over the
(s, eta) plane and finds that the attractor phase is a WINDOW with two
boundaries obeying DIFFERENT scaling laws:

  * lower boundary:  s > u1 / sqrt(eta)   <->  u = s*sqrt(eta) > u1
    (the cascade per slope bounce must exceed the cone width ~ 1/sqrt(eta);
     UNIVERSAL in u = s*sqrt(eta) — all eta collapse onto one rise);

  * upper boundary:  s < s2 ~ 0.09 (eta-INDEPENDENT absolute slope;
    the descent of the Vieta-root amplification as the wall steepens).

The W1 resonance scale s* = 1/sqrt(eta) (u = 1) OVERESTIMATES the
window: empirically the attractor closes at u2 ~ 0.5, i.e. the slopes
must be noticeably shallower than the cone-asymptote resonance. E5's
phase diagram (eta = 100) and E6 are consistent within the smoothing.

E6a quantifies both boundaries: for eta in {9, 16, 25, 100, 400} we sweep
the slope s and measure the lock-in fraction over a ray ensemble (bounce
budget scaled with eta because the attractor period and transient grow
with eta). Pooled logistic fits give u1 (rise, variable u) and s2
(decay, variable s).

E6b (wave model) measures how the intensity contrast of the attractor
corridor grows with eta: the anisotropic Helmholtz equation is solved at
eta in {4, 9, 16, 36} with identical chamber, drive and frequency, and
the corridor contrast C = <I>_near / <I>_far is recorded. In the strong
anisotropy limit the caustic alignment sharpens and C grows as a power
law C ~ eta^beta; the fitted beta is reported.

Outputs
-------
data/E6_eta_scan.csv    ray-scan rows (eta, s, u, lock fraction, growth)
data/E6_wave_scan.npz   |E|^2 fields for the four wave-model runs
data/E6_summary.json    fitted constants u*, beta, per-run metrics

Usage:  python3 e6_eta_scan.py [--quick]
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
from ray_billiard import Medium, chamber_hexagon, chamber_hexagon_asym, \
    propagate_ray
import wave_helmholtz as wh

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.normpath(os.path.join(HERE, "..", "data"))
os.makedirs(DATA, exist_ok=True)

# ---------------------------------------------------------------- ray scan --
ETAS_RAY = [9.0, 16.0, 25.0, 100.0, 400.0]
S_VALUES = [0.005, 0.01, 0.02, 0.03, 0.045, 0.06, 0.08, 0.10, 0.11, 0.12,
            0.13, 0.14]
N_RAYS = 12          # ensemble per (eta, s)
Y_V = 0.35


def bounce_budget(eta: float) -> int:
    """Bounce budget scaled with eta: the attractor period and the
    transient both grow with eta (period ~ 8 at eta=9, 22 at eta=100),
    so a fixed 500-bounce budget would miss the locks at large eta."""
    return 500 if eta <= 100.0 else 2500


def loop_window(eta: float) -> int:
    return 60 if eta <= 100.0 else 120


def ray_scan(etas, s_values, n_rays) -> list[dict]:
    rows = []
    t0 = time.time()
    for eta in etas:
        med = Medium("hyperbolic", eta=eta)
        bounces = bounce_budget(eta)
        lw = loop_window(eta)
        for s in s_values:
            ch = chamber_hexagon(s=s, y_v=Y_V)
            rng = np.random.default_rng(20260)
            n_lock = 0
            growths = []
            periods = []
            for _ in range(n_rays):
                p0 = np.array([0.25 + 0.5 * rng.uniform(), 0.85])
                kx = rng.uniform(-1.5, 1.5)
                ky = math.sqrt(1.0 + kx * kx / eta)
                res = propagate_ray(ch, med, p0, np.array([kx, -ky]), 1.0,
                                    max_bounces=bounces, loop_tol=1e-6,
                                    loop_window=lw)
                if res.closed_loop is not None:
                    n_lock += 1
                    periods.append(res.period)
                # transient cascade growth: |k| over the first 25 bounces
                kmag = np.hypot(res.k_history[:26, 0], res.k_history[:26, 1])
                if kmag[0] > 0:
                    growths.append(math.log10(kmag.max() / kmag[0]) / 25.0)
            rows.append({
                "eta": eta,
                "s": s,
                "u": s * math.sqrt(eta),
                "lock_frac": n_lock / n_rays,
                "median_growth_per_bounce_log10":
                    float(np.median(growths)) if growths else 0.0,
                "median_period": float(np.median(periods)) if periods else 0.0,
                "n_rays": n_rays,
            })
        print(f"[E6a] eta={eta}: done ({time.time()-t0:.1f}s cumulative)",
              flush=True)
    return rows


def logistic(x, x0, w):
    return 1.0 / (1.0 + np.exp((x - x0) / w))


def _grid_fit(x, p, rising: bool) -> dict:
    """Brute-force logistic fit; rising=True fits a 0->1 transition."""
    best = None
    lo, hi = (0.0, 1.2) if rising else (0.02, 0.25)
    x0s = np.arange(lo, hi, (hi - lo) / 60)
    for x0 in x0s:
        for w in tuple(np.arange(0.01, 0.16, 0.01)):
            m = logistic(x, x0, w if rising else -w)
            sse = float(np.sum((p - m) ** 2))
            if best is None or sse < best["sse"]:
                best = {"mid": float(x0), "w": float(w), "sse": sse}
    return best


def _smooth(v, k=3):
    ker = np.ones(k) / k
    return np.convolve(v, ker, mode="same")


def fit_universal_transition(rows) -> dict:
    """Two-boundary fit of the attractor window.

    Per-eta windows come from 0.5-crossings of the smoothed lock curve;
    the pooled rise (0 -> 1) and decay (1 -> 0) are then fitted with a
    logistic BOTH in the universal variable u = s*sqrt(eta). The quality
    of the two collapses is reported as the spread of the per-eta
    boundaries in u."""
    out = {}
    per_eta_u = {}
    for eta in sorted({r["eta"] for r in rows}):
        rs = sorted([r for r in rows if r["eta"] == eta], key=lambda r: r["s"])
        ps = np.array([r["lock_frac"] for r in rs])
        us = np.array([r["u"] for r in rs])
        sm = _smooth(ps)
        above = np.where(sm >= 0.5)[0]
        if len(above):
            i0, i1 = int(above[0]), int(above[-1])
            win_lo_u, win_hi_u = float(us[i0]), float(us[i1])
            s_lo, s_hi = float(rs[i0]["s"]), float(rs[i1]["s"])
        else:
            win_lo_u = win_hi_u = s_lo = s_hi = None
        out[str(int(eta))] = {"window_lo_u": win_lo_u, "window_hi_u": win_hi_u,
                              "window_lo_s": s_lo, "window_hi_s": s_hi,
                              "peak_lock": float(ps.max())}
        per_eta_u[int(eta)] = (win_lo_u, win_hi_u)

    # pooled rise: strictly pre-window data
    rise = [(r["u"], r["lock_frac"]) for r in rows
            if per_eta_u[int(r["eta"])][0] is not None
            and r["u"] <= per_eta_u[int(r["eta"])][0]]
    # pooled decay: strictly post-window data
    decay = [(r["u"], r["lock_frac"]) for r in rows
             if per_eta_u[int(r["eta"])][1] is not None
             and r["u"] >= per_eta_u[int(r["eta"])][1]]

    if len(rise) >= 3:
        u = np.array([p[0] for p in rise]); p = np.array([q[1] for q in rise])
        out["pooled_rise_u"] = _grid_fit(u, p, rising=True)
    if len(decay) >= 3:
        u = np.array([p[0] for p in decay]); p = np.array([q[1] for q in decay])
        out["pooled_decay_u"] = _grid_fit(u, p, rising=False)

    los = [v[0] for v in per_eta_u.values() if v[0] is not None]
    his = [v[1] for v in per_eta_u.values() if v[1] is not None]
    if los and his:
        out["collapse"] = {
            "u1_mean": float(np.mean(los)), "u1_std": float(np.std(los)),
            "u2_mean": float(np.mean(his)), "u2_std": float(np.std(his)),
        }
    return out


# --------------------------------------------------------------- wave scan --
ETAS_WAVE = [4.0, 9.0, 16.0, 36.0]
F_WAVE = 9.0
N_GRID_WAVE = 256


def wave_scan(etas, n_grid, freq) -> tuple[dict, dict]:
    """Band-averaged, directionally-driven corridor contrast vs eta
    (protocol of wave_directional.py, E4)."""
    import wave_directional as wd

    ch = chamber_hexagon_asym(s_left=0.03, s_right=0.06, y_v=0.35)
    mask = wh.chamber_mask(ch, n_grid)
    xs = np.linspace(0.0, 1.0, n_grid)
    X, Y = np.meshgrid(xs, xs, indexing="ij")
    dx = 1.0 / (n_grid - 1)
    band = [freq - 0.4, freq - 0.2, freq + 0.2, freq + 0.4]
    fields = {}
    summary = {}
    for eta in etas:
        t0 = time.time()
        med = Medium("hyperbolic", eta=eta)
        rng = np.random.default_rng(1000)
        p0 = np.array([0.25 + 0.5 * rng.uniform(), 0.85])
        kx = rng.uniform(-1.5, 1.5)
        ky = math.sqrt(1.0 + kx * kx / eta)
        res = propagate_ray(ch, med, p0, np.array([kx, -ky]), 1.0,
                            max_bounces=3200, loop_tol=1e-7, loop_window=100)
        if res.closed_loop is None:
            print(f"[E6b] eta={eta}: reference ray did NOT lock — skipped",
                  flush=True)
            continue
        loop = res.closed_loop
        D_route = np.full((n_grid, n_grid), np.inf)
        pts = loop[:: max(1, len(loop) // 220)]
        for p in pts:
            D_route = np.minimum(D_route, np.hypot(X - p[0], Y - p[1]))
        near = D_route < 0.04
        far = D_route > 0.15
        far &= ~(np.hypot(X - wd.SRC[0], Y - wd.SRC[1]) < 4 * wd.SIGMA)

        d_unit = res.vg_history[-1]
        acc = None
        for f in band:
            k0 = 2.0 * math.pi * f
            kv = wd.k_from_direction(d_unit, k0, eta, dx)
            A, idx = wh.assemble(mask, k0, eta, wd.GAMMA)
            b = wd.directional_source(mask, kv, wd.SRC, wd.SIGMA)
            lu = wh.spla.splu(A.tocsc())
            E = lu.solve(b)
            Eg = np.zeros((n_grid, n_grid), dtype=complex)
            Eg[mask] = E
            inten = np.abs(Eg) ** 2
            acc = inten if acc is None else acc + inten
        inten = acc / len(band)
        contrast = float(inten[near].mean() / inten[far].mean())
        peak = float(inten[near].max())
        route_len = float(np.sum(np.hypot(*np.diff(
            np.vstack([loop, loop[:1]]), axis=0).T)))
        eff_width = float(inten[near].sum() / (peak * route_len * n_grid))

        # channeling anisotropy of the band-averaged intensity:
        # spectral weight of |E|^2 patterns at |q_x| > |q_y| (vertical
        # channels) vs total, over q > 3 (drop the DC plateau).
        win1d = np.hanning(n_grid)
        W2 = np.outer(win1d, win1d)
        Fl = np.abs(np.fft.fftshift(np.fft.fft2((inten - inten.mean()) * W2))) ** 2
        kq = np.fft.fftshift(np.fft.fftfreq(n_grid, xs[1] - xs[0]))
        KX, KY = np.meshgrid(kq, kq, indexing="ij")
        qsel = np.hypot(KX, KY) > 3.0
        aniso_H = float(Fl[qsel & (np.abs(KX) > np.abs(KY))].sum()
                        / Fl[qsel].sum())

        fields[f"eta{int(eta)}"] = inten
        summary[str(int(eta))] = {
            "contrast": contrast,
            "effective_corridor_width": eff_width,
            "channeling_anisotropy_H": aniso_H,
            "loop_period": int(res.period),
            "cone_half_angle_deg": math.degrees(med.cone_half_angle()),
            "band": band,
            "solve_s": time.time() - t0,
        }
        print(f"[E6b] eta={eta}: contrast={contrast:.2f}, H={aniso_H:.3f}"
              f" ({time.time()-t0:.1f}s)", flush=True)
    return fields, summary


def fit_power_law(etas, runs) -> dict:
    e = np.array([e for e in etas if str(int(e)) in runs])
    c = np.array([runs[str(int(e))]["contrast"] for e in e])
    if len(e) < 2:
        return {"beta": None, "C0": None}
    A = np.vstack([np.ones_like(e), np.log(e)]).T
    coef, *_ = np.linalg.lstsq(A, np.log(c), rcond=None)
    pred = np.exp(coef[0]) * e ** coef[1]
    r2 = 1.0 - np.sum((c - pred) ** 2) / np.sum((c - c.mean()) ** 2)
    return {"C0": float(np.exp(coef[0])), "beta": float(coef[1]),
            "r2": float(r2)}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--quick", action="store_true")
    args = ap.parse_args()
    t0 = time.time()

    etas_ray = ETAS_RAY[:3] if args.quick else ETAS_RAY
    s_values = S_VALUES[::2] if args.quick else S_VALUES
    n_rays = 8 if args.quick else N_RAYS
    etas_wave = ETAS_WAVE[:2] if args.quick else ETAS_WAVE
    n_wave = 128 if args.quick else N_GRID_WAVE

    print("[E6a] ray-model universality scan: "
          f"etas={etas_ray}, |s|={len(s_values)}, {n_rays} rays", flush=True)
    rows = ray_scan(etas_ray, s_values, n_rays)
    with open(os.path.join(DATA, "E6_eta_scan.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    fit = fit_universal_transition(rows)
    rise = fit.get("pooled_rise_u", {})
    decay = fit.get("pooled_decay_u", {})
    coll = fit.get("collapse", {})
    print(f"[E6a] pooled rise (in u): u1 = {rise.get('mid', float('nan')):.3f} "
          f"(width {rise.get('w', float('nan')):.3f})", flush=True)
    print(f"[E6a] pooled decay (in u): u2 = {decay.get('mid', float('nan')):.3f} "
          f"(width {decay.get('w', float('nan')):.3f})", flush=True)
    if coll:
        print(f"[E6a] per-eta collapse: u1 = {coll['u1_mean']:.3f} +/- "
              f"{coll['u1_std']:.3f}, u2 = {coll['u2_mean']:.3f} +/- "
              f"{coll['u2_std']:.3f}", flush=True)
    for k, v in fit.items():
        if k.isdigit():
            print(f"[E6a]   eta={k}: window u in "
                  f"[{v['window_lo_u']}, {v['window_hi_u']}], "
                  f"peak lock {v['peak_lock']:.2f}", flush=True)

    print(f"[E6b] wave-model contrast scan: etas={etas_wave}, "
          f"grid {n_wave}, f={F_WAVE}", flush=True)
    fields, wsum = wave_scan(etas_wave, n_wave, F_WAVE)
    pl = fit_power_law(etas_wave, wsum)
    print(f"[E6b] contrast power law: C = {pl['C0']:.3f} * eta^"
          f"{pl.get('beta', float('nan')):.3f} "
          f"(R2={pl.get('r2', 0):.4f})", flush=True)

    summary = {
        "ray_scan": {
            "etas": etas_ray, "s_values": s_values, "n_rays": n_rays,
            "bounce_budget": {"eta<=100": 500, "eta>100": 2500},
            "y_v": Y_V,
            "window_fit": fit,
            "scaling_laws": {
                "lower_boundary": "u = s*sqrt(eta) > u1 (universal in u)",
                "upper_boundary": "u < u2 (universal in u)",
                "window": "attractor window u1 < s*sqrt(eta) < u2",
                "w1_resonance": "s* = 1/sqrt(eta) (u=1) overestimates the window "
                                 "(window closes at u2 ~ 0.5)",
            },
        },
        "wave_scan": {
            "etas": etas_wave, "grid": n_wave, "freq": F_WAVE,
            "runs": wsum, "power_law": pl,
        },
    }
    with open(os.path.join(DATA, "E6_summary.json"), "w") as fjs:
        json.dump(summary, fjs, indent=2)
    np.savez_compressed(os.path.join(DATA, "E6_wave_scan.npz"), **fields)
    print(f"[E6] done in {time.time()-t0:.1f}s", flush=True)


if __name__ == "__main__":
    main()
