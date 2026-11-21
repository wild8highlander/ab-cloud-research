#!/usr/bin/env python3
"""Parity table: Python port headline numbers vs the frozen Julia v19 run."""
import sys

# (test, fragment from the Python log, expected frozen v19 value/verdict)
CHECKS = [
    (1,  "Test 1: b(N=50000)",            "1.2126 / PASS   (v19: b(50000)=1.2125526773, PASS)"),
    (2,  "Test 2: Monotonicity",          "0 / 499 / PASS  (v19: PASS)"),
    (3,  "Test 3: α = ",                  "α=0.1685, R²=0.9895 / PASS (v19: same)"),
    (4,  "Test 4: D=",                    "D=0.021619 / WARN (v19: D=0.021619, WARN)"),
    (5,  "Test 5: best p",                "0.000000 / WARN  (v19: WARN)"),
    (6,  "Test 6: χ² p(bins=300)",        "0.000000 / WARN  (v19: WARN)"),
    (7,  "Test 7: Slope=",                "−0.1504 CI[−0.1594,−0.1414] / PASS (v19: same)"),
    (8,  "Test 8: Runs=",                 "3 (5.8) / PASS   (v19: same)"),
    (9,  "Test 9: Bootstrap slope=",      "≈−0.1745 / PASS  (v19: −0.1746; RNG noise)"),
    (10, "Test 10: Max deviation=",       "8.5% / PASS      (v19: 8.5%)"),
    (11, "Test 11: A²=",                  "61.4924 / WARN   (v19: A²=61.492426, WARN)"),
    (12, "Test 12: D=",                   "≈0.02–0.03 / WARN (v19: 0.0233; GUE downscale 5000²)"),
    (13, "Test 13: closer-to-GUE",        "9/9 / PASS       (v19: 9/9)"),
    (14, "Test 14: closer-to-GUE",        "9/9 / PASS       (v19: 9/9)"),
    (15, "Test 15: Hermiticity",          "τ_TRB=0.1037 / PASS (v19: 0.1037)"),
    (16, "Test 16 [MONTGOMERY]",          "⟨r⟩≈0.594 / PASS  (v19: 0.5939±0.0012)"),
    (17, "Test 17: zero_modes",           "4; 138 (α=1/3) / PASS (v19: 4; 138)"),
    (18, "Test 18: sublattice",           "0.0e+00, 0.0058 / PASS (v19: same)"),
    (19, "Test 19: R²=",                  "v_F≈1.90 / PASS  (v19: 1.8998)"),
    (20, "Test 20: anchors",              "1,1,1; gap 5.5e-16 / PASS (v19: same)"),
    (21, "Test 21: arg(γ*)=",             "89.874° / PASS   (v19: 89.8741°)"),
    (22, "Test 22: Φ_AB=",                "0.4487989505 = π/7 / PASS (v19: same)"),
    (23, "Test 23: |CF_formula|",         "c_AB=0.02062 / PASS (v19: same)"),
    (24, "Test 24: vortex flux",          "empty 5040/5040 / PASS (v19: PASS)"),
    (25, "Test 25: Δ(q=1)",               "≈0 / Δ(0.3)>1e-3 / PASS (v19: PASS)"),
    (26, "Test 26: flux_v",               "⟨r⟩≈0.59, flux OK / PASS (v19: PASS)"),
    (27, "Test 27: chiral defect",        "0.0e+00 / PASS   (v19: PASS; ζ ⟨r⟩=0.6119)"),
    (28, "Test 28: f_GUE",                "≈0.87–0.91 / PASS-WARN (v19: 0.8704, WARN)"),
    (29, "Test 29: ρ(0.5)",               "dip 10× / PASS   (v19: 0.1944/0.0193, 10.08×)"),
    (30, "Test 30: v_F=",                 "≈1.80 R²≈0.998 / PASS (v19: 1.798, 0.9977)"),
    (31, "Test 31: max|Im(E)|",           ">0.01, ⟨r⟩_NH / PASS (v19: 0.6397, 0.8938)"),
    (32, "Test 32: ⟨r⟩=",                 "≈0.60 / PASS     (v19: PASS)"),
    (33, "Test 33: L-scaling",            "rising → PASS/WARN (v19: PASS)"),
    (34, "Test 34: KS p=",                "D, R₂ contract / PASS-WARN (v19: WARN)"),
    (35, "Test 35: K(t)",                 "RMS≈0.42 / WARN  (v19: 0.4193, WARN)"),
    (36, "Test 36: byte robust",          "|Δ⟨r⟩|<0.02, H>7.9 / PASS (v19: PASS)"),
    (37, "Test 37: (1/2)!",               "err 4.4e-16 / PASS (v19: PASS)"),
    (38, "Test 38: Curie 3-pass",         "T*∈(0.05,3) (post-v19 test; no frozen target)"),
    (39, "Test 39: geometry sweep",       "7/7 at budget 72² (post-v19 test; no frozen target)"),
]


def main(paths):
    text = ""
    for p in paths:
        try:
            with open(p, encoding="utf-8", errors="replace") as f:
                text += f.read() + "\n"
        except FileNotFoundError:
            print(f"[missing log] {p}")
    print(f"{'T':>3} {'port line (from run log)':<58} expected (frozen Julia v19)")
    print("─" * 130)
    n_found = n_missing = 0
    for tid, frag, expect in CHECKS:
        lines = [l.strip() for l in text.splitlines() if frag in l]
        got = lines[-1] if lines else "(not in log)"
        status = "OK " if lines else "-- "
        if lines:
            n_found += 1
        else:
            n_missing += 1
        print(f"{status}{tid:>2} {got[:56]:<58} {expect}")
    print("─" * 130)
    print(f"found in logs: {n_found}/{len(CHECKS)}")


if __name__ == "__main__":
    main(sys.argv[1:])
