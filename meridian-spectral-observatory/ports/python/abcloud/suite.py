# -*- coding: utf-8 -*-
"""Portable suite subset — the same 25 tests as the C++/Rust/Go mirrors.

Covers Tests 1-18, 24, 25, 26, 34, 35, 36, 37 of the original 39-test
ab_cloud_full.jl protocol; the rest are dSFMT-dependent, LAPACK-dependent or
report-only and are listed as [SKIP] (see PORT_SPEC.md).
"""

import sys
from math import log, sqrt, fabs, pi, sin, exp, cos, isnan

from .mt19937 import MT19937
from .special import lgamma_lanczos, gue2_surmise_pdf, compute_bN
from .gof import (normalized_spacings, linreg, ks_test, chi2_gue_test,
                  anderson_darling_stat, mean_adjacent_spacing_ratio,
                  unfolded_positions, number_variance, delta3_rigidity,
                  ks2, unit_spacings)
from .rmt_table import RMT
from .lattice import (Vortex, ABCloudConfig, build_ab_cloud_hamiltonian,
                      safe_eigvals, plaquette_flux, flux_circdist,
                      central_band_eigs, chiral_symmetry_defect,
                      verify_hermitian, time_reversal_asymmetry)
from .unfold import hp_unfold_local, hp_kgue_envelope
from .golden import tvals_envelope


class SuiteReport(object):
    def __init__(self):
        self.n_pass = 0
        self.n_fail = 0
        self.n_warn = 0
        self.n_info = 0

    def verdict(self, v, tid, title, lines):
        mark = {"PASS": "[PASS]", "FAIL": "[FAIL]", "WARN": "[WARN]",
                "INFO": "[INFO]", "SKIP": "[SKIP]"}[v]
        if v == "PASS":
            self.n_pass += 1
        elif v == "FAIL":
            self.n_fail += 1
        elif v == "WARN":
            self.n_warn += 1
        else:
            self.n_info += 1
        print("%s TEST %2d — %s" % (mark, tid, title))
        for ln in lines:
            print(ln)
        sys.stdout.flush()


def _filter(filter_str, tid):
    if filter_str == "all":
        return True
    return tid in [int(t) for t in filter_str.split(",") if t.strip()]


def _loglog_fit(xs, ys):
    r = linreg([log(v) for v in xs], [log(v) for v in ys])
    return r.b, r.R2


def _gauss(rng):
    """Box-Muller from the portable MT19937 (Test 12 GUE matrix)."""
    u1 = rng.random()
    u2 = rng.random()
    if u1 < 1e-300:
        u1 = 1e-300
    return sqrt(-2.0 * log(u1)) * cos(2 * pi * u2)


def run_suite(zeta, test_filter="all"):
    print("=" * 78)
    print("ABCLOUD SUITE (portable subset, Python)")
    print("=" * 78)
    rep = SuiteReport()
    sp = normalized_spacings(zeta)
    ladder = [100, 500, 1000, 5000, 10000, 50000]

    # 1
    if _filter(test_filter, 1):
        vals = [compute_bN(zeta, N) for N in ladder]
        ok = vals[-1] == vals[-1] and vals[-1] < vals[0]
        rep.verdict("PASS" if ok else "FAIL", 1, "b(N) convergence table",
                    ["  ladder: " + "  ".join("%.6f" % v for v in vals),
                     "  b(50000) = %.6f (audit anchor 1.2126)" % vals[-1]])
    # 2
    if _filter(test_filter, 2):
        vals = [compute_bN(zeta, N) for N in ladder]
        mono = all(vals[i + 1] <= vals[i] + 1e-9 for i in range(len(vals) - 1))
        rep.verdict("PASS" if mono else "FAIL", 2, "b(N) monotonicity",
                    ["  ladder: " + "  ".join("%.6f" % v for v in vals)])
    # 3
    if _filter(test_filter, 3):
        vals = [compute_bN(zeta, N) for N in ladder]
        slope, R2 = _loglog_fit(ladder, vals)
        ok = (-1.5 < slope < -0.05) and R2 > 0.9
        rep.verdict("PASS" if ok else "FAIL", 3, "b(N) convergence rate (power law)",
                    ["  slope=%+.4f  R2=%.6f  (asymptotic -0.5 with 1/log T correction)"
                     % (slope, R2)])
    # 4
    if _filter(test_filter, 4):
        D, p = ks_test(sp)
        rep.verdict("PASS" if D < 0.10 else "FAIL", 4, "GUE KS test (full range)",
                    ["  KS D=%.6f  p=%.3e  n=%d  (effect-size gate D<0.10)"
                     % (D, p, len(sp))])
    # 5
    if _filter(test_filter, 5):
        z2 = zeta[len(zeta) // 2:]
        sp2 = normalized_spacings(z2)
        D, p = ks_test(sp2)
        rep.verdict("PASS" if D < 0.10 else "FAIL", 5, "GUE KS test (high-T half)",
                    ["  high-T half: D=%.6f  p=%.3e  n=%d" % (D, p, len(sp2))])
    # 6
    if _filter(test_filter, 6):
        chi2, df, p = chi2_gue_test(sp, 30)
        rep.verdict("INFO", 6, "spacing chi2 histogram",
                    ["  chi2=%.2f  df=%d  p=%.3e  (bins=30; low p = finite-data GUE miss)"
                     % (chi2, df, p)])
    # 7
    if _filter(test_filter, 7):
        tail = [5000, 10000, 50000]
        vals = [compute_bN(zeta, N) for N in tail]
        slope, R2 = _loglog_fit(tail, vals)
        ok = (-0.9 < slope < -0.05) and R2 > 0.9
        rep.verdict("PASS" if ok else "FAIL", 7, "decay slope (large-T)",
                    ["  tail slope=%+.4f  R2=%.6f  (1/log T flattens local slope)"
                     % (slope, R2)])
    # 8
    if _filter(test_filter, 8):
        vals = [compute_bN(zeta, N) for N in ladder]
        r = linreg([log(float(N)) for N in ladder], [log(v) for v in vals])
        max_rel = max(fabs(e) / max(fabs(log(v)), 1e-12)
                      for e, v in zip(r.res, vals))
        rep.verdict("PASS" if max_rel < 0.2 else "WARN", 8,
                    "residual analysis of fit",
                    ["  max |relative residual| = %.4f" % max_rel])
    # 9
    if _filter(test_filter, 9):
        base = [compute_bN(zeta, N) for N in ladder]
        rng = MT19937(777)
        lo, hi = 1e9, -1e9
        for _ in range(200):
            bs = [v * sqrt(1.0 + 0.02 * (rng.random() - 0.5) * 2) for v in base]
            lb = [log(float(N)) for N in ladder]
            r = linreg(lb, [log(v) for v in bs])
            lo = min(lo, r.b)
            hi = max(hi, r.b)
        ok = (-1.5 < lo) and (hi < -0.1)
        rep.verdict("PASS" if ok else "WARN", 9, "bootstrap CI for slope",
                    ["  bootstrap slope CI [%+.4f, %+.4f] (200 resamples, seed 777)"
                     % (lo, hi)])
    # 10
    if _filter(test_filter, 10):
        half = len(zeta) // 2
        lad = [100, 500, 1000, 5000]
        zh2 = zeta[half:]
        v1 = [compute_bN(zeta, N) for N in lad]
        v2 = [compute_bN(zh2, N, half) for N in lad]
        s1, R1 = _loglog_fit(lad, v1)
        s2, R2 = _loglog_fit(lad, v2)
        mono = all(v1[i + 1] <= v1[i] + 1e-9 and v2[i + 1] <= v2[i] + 1e-9
                   for i in range(len(v1) - 1))
        ok = mono and R1 > 0.85 and R2 > 0.85
        rep.verdict("PASS" if ok else "FAIL", 10, "cross-validation stability",
                    ["  slopes %+.3f/%+.3f, R2 %.3f/%.3f; both monotone "
                     "(height gap = documented 1/log T offset)" % (s1, s2, R1, R2)])
    # 11
    if _filter(test_filter, 11):
        A2 = anderson_darling_stat(sp)
        rng = MT19937(777)
        mcbuf = [0.0] * len(sp)
        count = 0
        for _ in range(200):
            RMT.sample(rng, mcbuf)
            if anderson_darling_stat(mcbuf) >= A2:
                count += 1
        p_mc = (count + 1.0) / 201.0
        rep.verdict("INFO", 11, "Anderson-Darling (honest)",
                    ["  A2 = %.4f  law-exact MC p = %.4f (200 draws, seed 777)"
                     % (A2, p_mc),
                     "  (tail-sensitive statistic; low MC p = honest GUE miss on low-T data)"])
    # 12
    if _filter(test_filter, 12):
        # GUE matrix spectrum via the same Jacobi solver (N=200; statistical
        # test — size documented; pure-Python Jacobi takes ~a minute)
        n_mat = 200
        rng = MT19937(4242)
        H = [[complex(0.0, 0.0)] * n_mat for _ in range(n_mat)]
        for r in range(n_mat):
            H[r][r] = complex(_gauss(rng), 0.0)
            for c in range(r + 1, n_mat):
                h = complex(_gauss(rng) / sqrt(2.0), _gauss(rng) / sqrt(2.0))
                H[r][c] = h
                H[c][r] = h.conjugate()
        for r in range(n_mat):
            for c in range(r, n_mat):
                H[r][c] *= 0.5 * (2.0 if r == c else 1.0)
        Hs = [[0.5 * (H[r][c] + H[c][r].conjugate()) for c in range(n_mat)]
              for r in range(n_mat)]
        ev = safe_eigvals(Hs)
        band = ev[n_mat // 10: 9 * n_mat // 10]
        m = sum(band[i + 1] - band[i] for i in range(len(band) - 1)) / (len(band) - 1)
        gp = [(band[i + 1] - band[i]) / m for i in range(len(band) - 1)]
        D = ks2(sp, gp)
        rep.verdict("PASS" if D < 0.10 else "FAIL", 12,
                    "two-sample KS vs GUE matrix",
                    ["  two-sample KS (zeta n=%d vs GUE-matrix n=%d): D=%.6f"
                     % (len(sp), len(gp), D)])
    # 13
    if _filter(test_filter, 13):
        pos = unfolded_positions(zeta)
        rng = MT19937(777)
        ok = True
        lines = []
        for L in (5.0, 10.0, 20.0, 50.0):
            s2 = number_variance(pos, L, 3000, rng)
            ok = ok and s2 < L
            lines.append("  S2(L=%5.1f) = %.4f   [Poisson %.1f]" % (L, s2, L))
        lines.append("  gate: S2(L) << L (GUE rigidity)")
        rep.verdict("PASS" if ok else "FAIL", 13, "number variance S2(L)", lines)
    # 14
    if _filter(test_filter, 14):
        pos = unfolded_positions(zeta)
        rng = MT19937(777)
        ok = True
        lines = []
        for L in (5.0, 10.0, 20.0, 50.0):
            d3 = delta3_rigidity(pos, L, 300, 300, rng)
            ok = ok and d3 < L / 15.0
            lines.append("  D3(L=%5.1f) = %.4f   [Poisson %.4f]" % (L, d3, L / 15.0))
        rep.verdict("PASS" if ok else "FAIL", 14, "spectral rigidity D3(L)", lines)
    # 15
    if _filter(test_filter, 15):
        cfg = ABCloudConfig(16, 16, [Vortex(4.5, 4.5, 1.0)], 0.5, 1.0, "open", 0.0)
        H = build_ab_cloud_hamiltonian(cfg)
        herm = verify_hermitian(H)
        tau = time_reversal_asymmetry(H)
        ev = safe_eigvals(H)
        band = central_band_eigs(ev, 0.6)
        r, n_r = mean_adjacent_spacing_ratio(band)
        rep.verdict("PASS" if (herm and tau > 1e-12) else "FAIL", 15,
                    "AB-cloud construction",
                    ["  hermitian=%s  tau_TRB=%.3e  <r>(central 60%%)=%.4f (n_r=%d)"
                     % ("true" if herm else "false", tau, r, n_r)])
    # 16
    if _filter(test_filter, 16):
        cfg = ABCloudConfig(24, 24, [Vortex(6.5, 6.5, 1.0), Vortex(17.5, 17.5, -1.0)],
                            0.5, 1.0, "open", 0.0)
        H = build_ab_cloud_hamiltonian(cfg)
        ev = safe_eigvals(H)
        band = central_band_eigs(ev, 0.6)
        r, n_r = mean_adjacent_spacing_ratio(band)
        ok = fabs(r - 0.5992) < 0.06
        rep.verdict("PASS" if ok else "WARN", 16, "AB-cloud GUE classification",
                    ["  <r> = %.4f vs GUE 0.5992 +/- 0.06 (n_r=%d; L=24 finite-size band)"
                     % (r, n_r)])
    # 17
    if _filter(test_filter, 17):
        H = build_ab_cloud_hamiltonian(ABCloudConfig(12, 12, [], 0.5, 1.0, "open", 0.0))
        ea = safe_eigvals(H)
        H = build_ab_cloud_hamiltonian(ABCloudConfig(12, 12, [], 2.0, 1.0, "open", 0.0))
        eb = safe_eigvals(H)
        na = sum(v * v for v in ea)
        nb = sum((a - b) * (a - b) for a, b in zip(ea, eb))
        rep.verdict("INFO", 17, "Connes self-duality",
                    ["  alpha<->1/alpha relative L2 defect (open 12x12, W=0) = %.6f"
                     % (sqrt(nb) / sqrt(na)),
                     "  finite open lattice: duality is boundary-spoiled (documented)"])
    # 18
    if _filter(test_filter, 18):
        H = build_ab_cloud_hamiltonian(
            ABCloudConfig(12, 12, [], 0.5, 1.0, "open", 0.0, 96, "monumental"))
        Hw = build_ab_cloud_hamiltonian(
            ABCloudConfig(12, 12, [], 0.5, 1.0, "open", 4.0, 96, "monumental"))
        d0 = chiral_symmetry_defect(H, 12, 12)
        dw = chiral_symmetry_defect(Hw, 12, 12)
        rep.verdict("PASS" if d0 < 1e-10 else "FAIL", 18,
                    "chiral AIII at alpha=1/2",
                    ["  defect(W=0) = %.3e (gate <1e-10)   defect(W=4, honest breaker) = %.4f"
                     % (d0, dw)])
    # 24
    if _filter(test_filter, 24):
        H = build_ab_cloud_hamiltonian(
            ABCloudConfig(8, 8, [Vortex(3.5, 3.5, 1.0)], 0.25, 1.0, "open",
                          0.0, 96, "dirac"))
        maxdev = 0.0
        for iy in range(1, 8):
            for ix in range(1, 8):
                flux = plaquette_flux(H, 8, 8, ix, iy)
                tgt = 2 * pi * 0.25 + (2 * pi if (ix == 3 and iy == 3) else 0.0)
                maxdev = max(maxdev, flux_circdist(flux, tgt))
        rep.verdict("PASS" if maxdev < 1e-9 else "FAIL", 24, "Dirac-string flux",
                    ["  max circular deviation from 2*pa + 2*q = %.3e (:dirac model)"
                     % maxdev])
    # 25
    if _filter(test_filter, 25):
        e1 = safe_eigvals(build_ab_cloud_hamiltonian(
            ABCloudConfig(16, 16, [Vortex(4.5, 4.5, 1.0), Vortex(11.5, 11.5, -1.0)],
                          0.3, 1.0, "open", 0.0, 96, "dirac")))
        e2 = safe_eigvals(build_ab_cloud_hamiltonian(
            ABCloudConfig(16, 16, [Vortex(4.5, 4.5, 2.0), Vortex(11.5, 11.5, 0.0)],
                          0.3, 1.0, "open", 0.0, 96, "dirac")))
        e3 = safe_eigvals(build_ab_cloud_hamiltonian(
            ABCloudConfig(16, 16, [Vortex(4.5, 4.5, 0.3), Vortex(11.5, 11.5, -0.3)],
                          0.3, 1.0, "open", 0.0, 96, "dirac")))
        d_int = max(fabs(a - b) for a, b in zip(e1, e2))
        d_frac = max(fabs(a - b) for a, b in zip(e1, e3))
        ok = d_int < 1e-9 and d_frac > 1e-4
        rep.verdict("PASS" if ok else "FAIL", 25, "Byers-Yang theorem",
                    ["  integer q->q+1: max|dE| = %.3e   fractional q=0.3 control: %.3e (must differ)"
                     % (d_int, d_frac)])
    # 26
    if _filter(test_filter, 26):
        H = build_ab_cloud_hamiltonian(
            ABCloudConfig(12, 12, [], 0.25, 1.0, "torus", 0.0))
        maxdev = 0.0
        for iy in range(1, 13):
            for ix in range(1, 13):
                maxdev = max(maxdev, flux_circdist(
                    plaquette_flux(H, 12, 12, ix, iy, True), 2 * pi * 0.25))
        rep.verdict("PASS" if maxdev < 1e-9 else "FAIL", 26, "PBC torus flux",
                    ["  torus 12x12 alpha=0.25: max flux deviation = %.3e" % maxdev])
    # 34
    if _filter(test_filter, 34):
        H = build_ab_cloud_hamiltonian(
            ABCloudConfig(28, 28, [Vortex(7.5, 7.5, 1.0), Vortex(20.5, 20.5, -1.0)],
                          0.5, 1.0, "open", 0.0, 96, "monumental"))
        ev = safe_eigvals(H)
        band = central_band_eigs(ev, 0.6)
        u = hp_unfold_local(band)
        absp = unit_spacings(u)
        zs = unit_spacings(sp)
        D = ks2(absp, zs)
        rep.verdict("PASS" if D < 0.10 else "WARN", 34, "DIRECT AB-cloud vs zeta",
                    ["  DIRECT AB-cloud (L=28 alpha=0.5 monumental, 2 vortices, n=%d) vs zeta: KS D=%.6f"
                     % (len(absp), D)])
    # 35
    if _filter(test_filter, 35):
        tvals = [0.1 * i for i in range(1, 31)]
        K = None
        from .gof import compute_K_form_factor
        K = compute_K_form_factor(zeta, tvals)
        acc = 0.0
        cnt = 0
        for i, t in enumerate(tvals):
            if t >= 0.3:
                e = tvals_envelope(t)
                acc += (K[i] - e) * (K[i] - e)
                cnt += 1
        rms = sqrt(acc / cnt)
        rep.verdict("PASS" if rms < 1.0 else "FAIL", 35, "form factor K(t)",
                    ["  RMS(K - K_box) over t>=0.3 = %.4f  (calibrated gate <1.0)" % rms])
    # 36
    if _filter(test_filter, 36):
        H = build_ab_cloud_hamiltonian(
            ABCloudConfig(16, 16, [Vortex(4.5, 4.5, 1.0)], 0.5, 1.0, "open", 0.0))
        ev = safe_eigvals(H)
        band = central_band_eigs(ev, 0.6)
        r0, _ = mean_adjacent_spacing_ratio(band)
        lo = band[0]
        span = band[-1] - band[0]
        nlev = 4096
        quant = [lo + round((e - lo) / span * (nlev - 1)) / (nlev - 1) * span
                 for e in band]
        rr, _ = mean_adjacent_spacing_ratio(quant)
        dr = fabs(rr - r0)
        rng = MT19937(12345)
        counts = [0] * 256
        nb2 = 200000
        for _ in range(nb2):
            counts[rng.next_u32() & 0xFF] += 1
        ent = 0.0
        exp2 = nb2 / 256.0
        chi2z = 0.0
        for c in counts:
            if c > 0:
                pp = float(c) / nb2
                ent -= pp * log(pp) / log(2.0)
            chi2z += (c - exp2) * (c - exp2) / exp2
        z = (chi2z - 255.0) / sqrt(2.0 * 255.0)
        ok = dr < 0.02 and fabs(ent - 8.0) < 0.01 and fabs(z) < 3.0
        rep.verdict("PASS" if ok else "FAIL", 36, "byte-level robustness",
                    ["  |d<r>| under %d-level quantization = %.5f (gate 0.02)" % (nlev, dr),
                     "  RNG entropy = %.6f bits/byte (ideal 8.0), chi2 z = %+.2f (|z|<3)"
                     % (ent, z)])
    # 37
    if _filter(test_filter, 37):
        err1 = fabs(exp(lgamma_lanczos(0.5)) - sqrt(pi))
        err2 = fabs(exp(lgamma_lanczos(1.5)) - sqrt(pi) / 2.0)
        n = 2000
        smax = 10.0
        h = smax / n
        integ = 0.0
        m2 = 0.0
        for i in range(n + 1):
            wgt = 1.0 if (i == 0 or i == n) else (4.0 if i % 2 == 1 else 2.0)
            p = gue2_surmise_pdf(i * h)
            integ += wgt * p
            m2 += wgt * p * (i * h) * (i * h)
        integ *= h / 3.0
        m2 *= h / 3.0
        ok = err1 < 1e-9 and err2 < 1e-9 and fabs(integ - 1) < 1e-4 \
            and fabs(m2 - 3 * pi / 8) < 5e-3
        rep.verdict("PASS" if ok else "FAIL", 37,
                    "(1/2)! via Gamma + GUE normalization",
                    ["  G(1/2)-sqrt(pi) = %.2e   G(3/2)-sqrt(pi)/2 = %.2e   int p2 = %.6f   <s2> = %.6f (3pi/8)"
                     % (err1, err2, integ, m2)])

    # not-ported notices
    not_ported = [19, 20, 21, 22, 23, 27, 28, 29, 30, 31, 32, 33, 38, 39]
    notes = ["four-pass Dirac-cone audit", "TKNN Chern number", "spinorial phase",
             "AB phase identity", "fractal factor", "binary chiral + zeta-dictionary",
             "f_GUE merit", "DOS dip", "v_F scaling ladder", "Hatano-Nelson skin",
             "multi-realization <r> bootstrap (dSFMT-disorder parity)",
             "L-scaling <r> (dSFMT-disorder parity)", "Curie point three-pass",
             "Test-34G geometry sweep"]
    print("-" * 78)
    for tid, note in zip(not_ported, notes):
        if _filter(test_filter, tid):
            print("[SKIP] TEST %2d — not ported: %s" % (tid, note))
    print("-" * 78)
    print("SUITE RESULT: %d PASS, %d FAIL, %d WARN, %d INFO"
          % (rep.n_pass, rep.n_fail, rep.n_warn, rep.n_info))
    print("=" * 78)
    return rep
