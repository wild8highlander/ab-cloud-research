#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""score_submission.py — публичный счётчик открытого challenge (v2.0).

Использование:
    python3 challenge/score_submission.py <gate.json>

Протокол (challenge/CHALLENGE.md):
  1. rebuild Hamiltonian from spec (package engine, seed logged);
  2. metrics: r_H7 (v2 convention), p_r (64 shifts), r_GUE_z (40), ⟨r⟩, r_EF;
  3. positive controls PC0' (twin → 1.000) and PC0 (zeros vs comb → +0.999)
     must pass in the same run;
  4. verdict: ACCEPT / REJECT with the full report.
"""
import json, os, sys, time
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

GAP_TARGET = 0.7          # r_H7, соответствующий «минус 2 порядка» по D_nn


def main(path):
    t0 = time.time()
    spec = json.load(open(path))
    from hpbridge.zeros_mp import ensure_zeros
    from hpbridge.metrics_v2 import (ZeroReference, corr_shift, null_pvalue,
                                    gue_null_stats, gue_class_verdict,
                                    ef_report2, spacing_ratio_mean)
    from engine.solver import gate_spectrum
    from engine.hamiltonian import unfold_poly, central_band, window_u
    from hpbridge import nonlocaltrace as nl
    from hpbridge.nonlocaltrace import ispectral_twin
    from scipy.linalg import eigvalsh

    gamma = ensure_zeros(800)
    zref = ZeroReference(gamma, k0=224)

    # ── позитивные контроли (обязаны пройти в этом же прогоне) ──
    H_tw, _ = ispectral_twin(gamma[:400], kind="dct")
    ev_tw = np.sort(np.linalg.eigvalsh(H_tw))
    ev_tw = ev_tw[ev_tw > 0]
    cen = central_band(ev_tw, 0.6)
    w_tw = window_u(unfold_poly(cen), 200)
    r_pc1 = corr_shift(w_tw, ZeroReference(gamma, k0=80).window)[0]
    U = np.linspace(0.05, 1.0, 40)
    P = nl.prime_curve(U, nmax=1_000_000)
    rep_pc0 = ef_report2(w_tw, U, P)
    pc1_ok = r_pc1 > 0.99
    pc0_ok = rep_pc0["r_fluct"] > 0.95

    # ── затвор из спеки ──
    h = spec.get("handles", {})
    enc = spec.get("phase_encoding")
    if enc:
        from hpbridge.phasecoding import phase_coded_spectrum
        ev, phi, _ = phase_coded_spectrum(
            spec.get("lattice", 24), Nv=h.get("Nv", 16), q=h.get("q", 1.0),
            alpha=h.get("alpha", 0.5), W=h.get("W", 0.5),
            mode="beta", beta=float(enc.get("beta", 0.23)))
        cen = central_band(ev, 0.6)
        w = window_u(unfold_poly(cen), 200)
        ev = ev
    else:
        w, mean_sp, ev = gate_spectrum(
            h.get("Nv", 16), h.get("q", 1.0), h.get("W", 0.5),
            h.get("alpha", 0.5), seed=h.get("seed", 96),
            bc=h.get("bc", "open"),
            **{k: v for k, v in h.items() if k in
               ("aniso", "dalpha", "mass", "profile", "twist")})
    r, s = corr_shift(w, zref.window)
    null_ws = zref.random_windows(64)
    p_r = null_pvalue(r, [corr_shift(w, zw)[0] for zw in null_ws])
    g_mean, g_std = gue_null_stats(zref, n_gue=40)
    z_gue = (r - g_mean) / max(g_std, 1e-12)
    r_cls, is_gue = gue_class_verdict(ev)
    rep = ef_report2(w, U, P)

    accepted = (r >= GAP_TARGET) and pc1_ok and pc0_ok and is_gue
    report = {
        "gate": spec.get("name", "unnamed"),
        "spec_echo": spec,
        "controls": {"PC0p_r": r_pc1, "PC0p_ok": bool(pc1_ok),
                      "PC0_r_fluct": rep_pc0["r_fluct"],
                      "PC0_ok": bool(pc0_ok)},
        "metrics": {"r_H7": r, "shift": s, "p_r": p_r,
                     "r_GUE_z": z_gue, "r_mean": r_cls,
                     "gue_class": bool(is_gue),
                     "r_EF_fluct": rep["r_fluct"]},
        "target": {"r_H7": GAP_TARGET},
        "verdict": "ACCEPT — joint-paper track" if accepted
                   else "REJECT — the gap stands",
        "runtime_s": round(time.time() - t0, 1),
    }
    print(json.dumps(report, ensure_ascii=False, indent=1))
    outdir = os.path.join(ROOT, "challenge", "submissions")
    os.makedirs(outdir, exist_ok=True)
    stamp = time.strftime("%Y%m%d_%H%M%S")
    outp = os.path.join(outdir, f"report_{spec.get('name', 'gate')}_{stamp}.json")
    json.dump(report, open(outp, "w"), ensure_ascii=False, indent=1)
    print("report saved:", outp)
    return 0 if accepted else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
