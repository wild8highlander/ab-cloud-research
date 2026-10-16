# -*- coding: utf-8 -*-
"""Golden selftest — compute_all 1:1 with ports/golden/gen_golden.jl.

Computes every scalar anchor of abcloud_golden.json from the input zeros and
compares against the reference with per-section tolerances. The same section
names, key formats (Julia string(Float64) semantics) and evaluation order as
the Julia generator (and the C++/Rust/Go mirrors) are used.
"""

import json
import os
from math import log, sin, fabs, sqrt, exp, isnan

from .mt19937 import MT19937
from .special import (lgamma_lanczos, regularized_gamma_p, chi2_cdf,
                      ks_asymptotic_pvalue, goe_surmise_cdf, gue2_surmise_cdf,
                      gue2_surmise_pdf, lambert_w, gram_point, compute_bN)
from .gof import (normalized_spacings, linreg, ks_test, cvm_test,
                  anderson_darling_stat, chi2_gue_test,
                  mean_adjacent_spacing_ratio, unfolded_positions,
                  number_variance, delta3_rigidity, compute_K_form_factor)
from .lattice import (Vortex, ABCloudConfig, build_ab_cloud_hamiltonian,
                      safe_eigvals, plaquette_flux, flux_circdist,
                      chiral_symmetry_defect)
from .unfold import (hp_kgue_envelope, hp_unfold_local, hp_aicc, hp_wald_ci,
                     hp_rankdata, pearson_cor, hp_raw_ft, default_omega_grid)

PI = 3.14159265358979323846


def shortest(v):
    """Julia string(Float64): shortest round-trip repr, decimal point kept."""
    for prec in range(1, 18):
        s = "%.*g" % (prec, v)
        if "e" not in s and float(s) == v:
            if "." not in s and "n" not in s and "i" not in s:
                s += ".0"
            return s
    for prec in range(1, 18):
        s = "%.*g" % (prec, v)
        if float(s) == v:
            return s
    return "%.17g" % v


def tvals_envelope(t):
    return hp_kgue_envelope(t)


def compute_all(zeta, golden):
    """Compute all golden sections from the sorted zero list `zeta`.

    Returns (sections, tvals, omega): sections maps name -> {key: float}.
    """
    sec = {}

    # 1. Lambert W / Gram points
    sec["lambert_w"] = {"x=" + shortest(x): lambert_w(x)
                        for x in (0.5, 1.0, 3.7, 10.0, 271.8, 12345.6)}
    sec["gram_point"] = {"n=%d" % n: gram_point(n)
                         for n in (1, 2, 3, 10, 100, 1000, 10000, 50000)}
    # 2. b(N)
    bN = {"N=%d" % n: compute_bN(zeta, n)
          for n in (100, 500, 1000, 5000, 10000, 50000)}
    bN["N=1000_off500"] = compute_bN(zeta, 1000, 500)
    sec["bN"] = bN
    # 3. spacings
    sp = normalized_spacings(zeta)
    mean = sum(sp) / len(sp)
    var = sum((s - mean) * (s - mean) for s in sp) / (len(sp) - 1)
    sec["spacings"] = {"n": float(len(sp)), "mean": mean, "var": var}
    # 4. surmises / special
    g2, go, p2 = {}, {}, {}
    for s in (0.05, 0.1, 0.25, 0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 4.9):
        k = "s=" + shortest(s)
        g2[k] = gue2_surmise_cdf(s)
        go[k] = goe_surmise_cdf(s)
        p2[k] = gue2_surmise_pdf(s)
    sec["gue2_cdf"], sec["goe_cdf"], sec["gue2_pdf"] = g2, go, p2
    sec["gamma_p"] = {
        "a=%s_x=%s" % (shortest(a), shortest(x)): regularized_gamma_p(a, x)
        for a, x in ((0.5, 0.1), (0.5, 2.0), (1.0, 1.0), (2.0, 3.0), (0.5, 12.0))}
    sec["chi2_cdf"] = {
        "x=%s_df=%s" % (shortest(x), shortest(df)): chi2_cdf(x, df)
        for x, df in ((3.84, 1.0), (16.92, 29.0), (25.0, 10.0))}
    sec["ks_pvalue"] = {"lam=" + shortest(lam): ks_asymptotic_pvalue(lam)
                        for lam in (0.5, 1.3, 0.02)}
    # 5. GOF
    D, p = ks_test(sp)
    sec["ks_zeros"] = {"D": D, "p": p}
    sec["cvm_zeros"] = {"W2": cvm_test(sp)}
    sec["ad_zeros"] = {"A2": anderson_darling_stat(sp)}
    chi2, df, pchi = chi2_gue_test(sp, 30)
    sec["chi2_zeros"] = {"chi2": chi2, "df": float(df), "p": pchi}
    r, n_r = mean_adjacent_spacing_ratio(zeta)
    sec["rmean_zeros"] = {"r": r, "n_r": float(n_r)}
    # 6. S2 / D3 — ONE MT19937(777) stream shared S2 -> D3 (as gen_golden.jl)
    pos = unfolded_positions(zeta)
    rng = MT19937(777)
    sec["S2"] = {"L=" + shortest(L): number_variance(pos, L, 3000, rng)
                 for L in (5.0, 10.0, 20.0, 50.0, 100.0)}
    sec["D3"] = {"L=" + shortest(L): delta3_rigidity(pos, L, 300, 300, rng)
                 for L in (5.0, 10.0, 20.0, 50.0)}
    # 7. K form factor (tvals come from the golden grids — language-neutral)
    tvals = list(golden["grids"]["tvals"])
    omega = list(golden["grids"]["omega"])
    K = compute_K_form_factor(zeta, tvals)
    kz = {}
    for i, t in enumerate(tvals):
        if t in (0.2, 0.5, 1.0, 2.0, 3.0):
            kz["t=" + shortest(t)] = K[i]
    acc = 0.0
    cnt = 0
    for i, t in enumerate(tvals):
        if t >= 0.3:
            e = tvals_envelope(t)
            acc += (K[i] - e) * (K[i] - e)
            cnt += 1
    kz["rms_env"] = sqrt(acc / cnt)
    sec["K_zeros"] = kz
    # 8. H1 zeta positive control (first 20000 zeros, Hann-weighted FT)
    zs = zeta[:20000]
    P = hp_raw_ft(zs, omega)
    Ps = sorted(P)
    n = len(Ps)
    med = Ps[n // 2] if n % 2 == 1 else 0.5 * (Ps[n // 2 - 1] + Ps[n // 2])
    h1 = {"median": med}
    for pr in (2, 3, 5, 7, 11, 13):
        tgt = log(pr)
        best = 0
        bd = 1e300
        for i, om in enumerate(omega):
            d = fabs(om - tgt)
            if d < bd:
                bd = d
                best = i
        h1["snr_log%d" % pr] = P[best] / med
    sec["h1_zeta"] = h1

    # 9. Hamiltonian goldens
    def eigs_of(cfg):
        H = build_ab_cloud_hamiltonian(cfg)
        return safe_eigvals(H)

    def ham_keys(ev):
        n = len(ev)
        return {"eig1": ev[0], "eig2": ev[1], "eig3": ev[2],
                "eigmid": ev[n // 2 - 1],
                # Julia: for k in 0:2 put!("eigend$(3-k)", ev[n-k]) -> eigend3 = max
                "eigend1": ev[n - 3], "eigend2": ev[n - 2], "eigend3": ev[n - 1]}

    ev = eigs_of(ABCloudConfig(8, 8, [], 0.5, 1.0, "open", 0.0, 96, "monumental"))
    sec["ham_L8_open_a05_clean"] = ham_keys(ev)
    ev = eigs_of(ABCloudConfig(8, 8, [Vortex(3.5, 3.5, 1.0), Vortex(6.5, 6.5, -1.0)],
                               0.25, 1.0, "open", 0.0, 96, "monumental"))
    sec["ham_L8_open_a025_2vort"] = ham_keys(ev)
    ev = eigs_of(ABCloudConfig(10, 10, [], 0.2, 1.0, "torus", 0.0, 96, "monumental"))
    sec["ham_L10_torus_a02_clean"] = ham_keys(ev)
    # 9d Byers-Yang (:dirac)
    e1 = eigs_of(ABCloudConfig(8, 8, [Vortex(3.5, 3.5, 1.0), Vortex(6.5, 6.5, -1.0)],
                               0.3, 1.0, "open", 0.0, 96, "dirac"))
    e2 = eigs_of(ABCloudConfig(8, 8, [Vortex(3.5, 3.5, 2.0), Vortex(6.5, 6.5, 0.0)],
                               0.3, 1.0, "open", 0.0, 96, "dirac"))
    sec["byers_yang"] = {"L8_max_diff": max(fabs(a - b) for a, b in zip(e1, e2))}
    # 9e Connes (relative L2 defect, W=0, open 12x12)
    ea = eigs_of(ABCloudConfig(12, 12, [], 0.5, 1.0, "open", 0.0))
    eb = eigs_of(ABCloudConfig(12, 12, [], 2.0, 1.0, "open", 0.0))
    na = sum(v * v for v in ea)
    nb = sum((a - b) * (a - b) for a, b in zip(ea, eb))
    sec["connes"] = {"L12_a05_defect_W0": sqrt(nb) / max(sqrt(na), 1e-30)}
    # 9f chiral AIII
    H = build_ab_cloud_hamiltonian(
        ABCloudConfig(12, 12, [], 0.5, 1.0, "open", 0.0, 96, "monumental"))
    sec["chiral"] = {"L12_a05_defect": chiral_symmetry_defect(H, 12, 12)}
    # 9g Dirac flux (:dirac)
    H = build_ab_cloud_hamiltonian(
        ABCloudConfig(8, 8, [Vortex(3.5, 3.5, 1.0)], 0.25, 1.0, "open",
                      0.0, 96, "dirac"))
    maxdev = 0.0
    for iy in range(1, 8):
        for ix in range(1, 8):
            flux = plaquette_flux(H, 8, 8, ix, iy)
            tgt = 2 * PI * 0.25 + (2 * PI if (ix == 3 and iy == 3) else 0.0)
            maxdev = max(maxdev, flux_circdist(flux, tgt))
    sec["dirac_flux"] = {"L8_max_dev": maxdev}
    # 10. unfold / linreg / aicc / wald / spearman
    u = hp_unfold_local(zeta[:2000])
    sec["unfold"] = {"u2": u[1], "u1000": u[999], "u2000": u[1999]}
    x = [float(i) for i in range(1, 21)]
    y = [2.0 + 0.5 * i + 0.1 * sin(i) for i in range(1, 21)]
    r = linreg(x, y)
    sec["linreg"] = {"a": r.a, "b": r.b, "R2": r.R2}
    sec["aicc"] = {"n40_rss10_k3": hp_aicc(40, 10.0, 3)}
    p, lo, hi = hp_wald_ci(7, 20)
    sec["wald"] = {"p": p, "lo": lo, "hi": hi}
    xr = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]
    yr = [1.1, 2.3, 2.9, 4.2, 5.1, 5.8, 7.2, 7.9]
    sec["spearman"] = {"xy": pearson_cor(hp_rankdata(xr), hp_rankdata(yr))}
    # 11. test11 anchor
    sec["test11"] = {"A2_full": anderson_darling_stat(sp)}
    return sec, tvals, omega


# tolerances: section -> (rtol, atol) — the honest cross-language table
TOLERANCES = {
    "lambert_w": (1e-9, 0.0), "gram_point": (1e-9, 0.0), "bN": (1e-9, 0.0),
    "spacings": (1e-9, 0.0), "gue2_cdf": (1e-7, 0.0), "goe_cdf": (1e-9, 0.0),
    "gue2_pdf": (1e-9, 0.0), "gamma_p": (1e-7, 0.0), "chi2_cdf": (1e-7, 0.0),
    "ks_pvalue": (1e-9, 0.0), "ks_zeros": (1e-6, 0.0), "cvm_zeros": (1e-6, 0.0),
    "ad_zeros": (1e-6, 0.0), "chi2_zeros": (1e-6, 0.0), "rmean_zeros": (1e-9, 0.0),
    "S2": (1e-7, 1e-12), "D3": (1e-7, 1e-12), "K_zeros": (1e-6, 0.0),
    "h1_zeta": (1e-6, 0.0), "ham_L8_open_a05_clean": (1e-7, 1e-8),
    "ham_L8_open_a025_2vort": (1e-7, 1e-8), "ham_L10_torus_a02_clean": (1e-7, 1e-8),
    "byers_yang": (1e-6, 1e-10), "connes": (1e-5, 1e-8),
    "chiral": (1e-5, 1e-9), "dirac_flux": (1e-6, 1e-10),
    "unfold": (1e-8, 0.0), "linreg": (1e-8, 0.0), "aicc": (1e-8, 0.0),
    "wald": (1e-9, 0.0), "spearman": (1e-8, 0.0), "test11": (1e-6, 0.0),
}


def compare(sec, golden):
    """Yield (section, key, golden_value, port_value, rel_err, ok) tuples."""
    for section, gsec in sorted(golden.items()):
        if section in ("meta", "grids"):
            continue
        if section not in sec:
            yield (section, "", None, None, None, False)
            continue
        rtol, atol = TOLERANCES.get(section, (1e-6, 0.0))
        for key, g in sorted(gsec.items()):
            cv = sec[section].get(key)
            if cv is None or not isinstance(g, (int, float)):
                yield (section, key, g, cv, None, False)
                continue
            g = float(g)
            if g == 0.0 and cv == 0.0:
                err, ok = 0.0, True
            elif g == 0.0:
                err = fabs(cv)
                ok = err <= atol + rtol
            else:
                err = fabs(cv - g) / fabs(g)
                ok = err <= rtol or fabs(cv - g) <= atol
            yield (section, key, g, cv, err, ok)


def run_selftest(zeta, golden_path):
    with open(golden_path, "r", encoding="utf-8") as fh:
        golden = json.load(fh)
    sec, _, _ = compute_all(zeta, golden)
    print("=" * 78)
    print("ABCLOUD PYTHON PORT — GOLDEN SELFTEST")
    print("=" * 78)
    n_ok = 0
    n_all = 0
    for section, key, g, cv, err, ok in compare(sec, golden):
        n_all += 1
        if ok:
            n_ok += 1
        if key == "":
            print(" [FAIL] %-28s (section missing)" % section)
        elif not ok:
            print(" [FAIL] %-28s %-18s g=%-22.17g p=%-22.17g rel=%.2e"
                  % (section, key, g, cv, err if err is not None else -1.0))
    print("-" * 78)
    print(" RESULT: %d/%d checks passed" % (n_ok, n_all))
    print("=" * 78)
    if n_ok == n_all:
        print("SELFTEST: PASS — Python kernel matches the Julia golden references.")
        return 0
    print("SELFTEST: FAIL")
    return 1
