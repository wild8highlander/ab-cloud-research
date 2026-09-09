"""
test11_honest.py — an honestly-calibrated re-implementation of ab_cloud_v18.jl's
Test 11 (Anderson-Darling GOF of zeta-zero spacings vs the GUE beta=2 Wigner surmise).

WHAT WAS WRONG WITH THE ORIGINAL TEST 11
-----------------------------------------
The original built its Monte-Carlo *null* distribution by bootstrapping (WITH
replacement) 49999 spacings out of a pool of only ~8000 real spacings taken
from a single 10000x10000 GUE matrix. Because 49999 draws are taken with
replacement from just 8000 distinct values (~6.25x oversampling), the
resulting resamples are full of exact ties -- something that can never happen
in genuinely continuous data. The Anderson-Darling statistic is very sensitive
to this: reproduced here, that artifact alone inflates the *typical* null A^2
from the textbook O(1) scale (median ~0.5-1, 95% critical value ~2.5, for a
correctly specified continuous null at ANY n) up to a median of several to
several dozen, depending on the luck of the specific pool realization -- which
plausibly fully explains why the original run reported a reference median of
12.5 instead of the ~1 the asymptotic AD theory promises.

THE FIX
-------
For a one-sample GOF test of a FULLY SPECIFIED continuous null (H0: spacings
are i.i.d. draws from gue2_surmise_cdf), the textbook-correct Monte-Carlo null
is obtained by drawing n_mc independent replicate samples of size n directly,
i.i.d., from that SAME cdf (inverse-transform sampling) -- not by bootstrapping
a finite empirical pool. That is what this script does. It also reports the
MC p-value with add-one (Laplace) smoothing, since "p = 0.0000" out of a few
thousand replicates is a display artifact, not a real zero.

Everything else (data, unfolding, the A^2 formula itself) is UNCHANGED from
the original -- those parts were already verified (see PASS 3 in the original
log: exact-formula vs interpolation-table A^2 agree to 2e-5).
"""
import argparse
import numpy as np
from scipy.special import erf

# ─────────────────────────────────────────────────────────────────────────
# 1. GUE beta=2 Wigner surmise CDF (exact, closed form -- identical to
#    gue2_surmise_cdf in ab_cloud_v18.jl, just erf instead of
#    regularized_gamma_p(0.5, .) -- the two are identical: P(1/2,x) = erf(sqrt(x)))
# ─────────────────────────────────────────────────────────────────────────
def gue2_cdf(s):
    s = np.asarray(s, dtype=float)
    x2 = 4.0 * s ** 2 / np.pi
    return np.where(s < 0, 0.0, erf(2.0 * s / np.sqrt(np.pi)) - (4.0 * s / np.pi) * np.exp(-x2))


# fine monotone grid + linear interpolation, used ONLY to draw the honest
# i.i.d. null samples fast (inverse-transform sampling). The test statistic
# itself always uses the exact closed-form gue2_cdf above, never this grid.
_GRID_S = np.linspace(0.0, 8.0, 400_001)
_GRID_F = gue2_cdf(_GRID_S)
_GRID_F[-1] = 1.0


def sample_gue2(n, rng):
    u = rng.random(n)
    return np.interp(u, _GRID_F, _GRID_S)


# ─────────────────────────────────────────────────────────────────────────
# 2. Anderson-Darling statistic -- byte-for-byte the same formula as
#    anderson_darling_stat() in ab_cloud_v18.jl
# ─────────────────────────────────────────────────────────────────────────
def anderson_darling_stat(spacings, cdf_func=gue2_cdf):
    n = len(spacings)
    s = np.sort(spacings)
    Fi = np.clip(cdf_func(s), 1e-300, 1.0 - 1e-16)
    Fni = np.clip(cdf_func(s[::-1]), 1e-300, 1.0 - 1e-16)
    i = np.arange(1, n + 1)
    return -n - np.sum((2 * i - 1) * (np.log(Fi) + np.log(1.0 - Fni))) / n


# ─────────────────────────────────────────────────────────────────────────
# 3. Unfolding -- identical leading-order Riemann-von Mangoldt density,
#    unchanged from normalized_spacings() in ab_cloud_v18.jl
# ─────────────────────────────────────────────────────────────────────────
def normalized_spacings(zeros):
    zeros = np.asarray(zeros, dtype=float)
    gaps = np.diff(zeros)
    density = np.log(zeros[:-1] / (2.0 * np.pi)) / (2.0 * np.pi)
    return gaps * density


# ─────────────────────────────────────────────────────────────────────────
# 4. The honest Monte-Carlo null: draw n_mc independent replicate samples,
#    each of size n = len(data spacings), i.i.d. from gue2_cdf itself.
# ─────────────────────────────────────────────────────────────────────────
def honest_mc_null(n, n_mc, rng):
    out = np.empty(n_mc)
    for k in range(n_mc):
        out[k] = anderson_darling_stat(sample_gue2(n, rng))
    return out


def mc_pvalue(a2_data, a2_null):
    # add-one (Laplace) smoothing -- avoids the misleading "p = 0.0000"
    r = int(np.sum(a2_null >= a2_data))
    n_mc = len(a2_null)
    return (r + 1) / (n_mc + 1), r


# ─────────────────────────────────────────────────────────────────────────
# 5. T-dependence diagnostic: does A^2 fall as the low-T zeros are dropped?
#    This directly tests the "low-T convergence" explanation instead of just
#    asserting it.
# ─────────────────────────────────────────────────────────────────────────
def t_dependence_scan(zeros, n_mc, rng, cutoffs_frac=(0.0, 0.2, 0.4, 0.6, 0.8)):
    rows = []
    n_total = len(zeros)
    for frac in cutoffs_frac:
        start = int(frac * n_total)
        sub = zeros[start:]
        if len(sub) < 200:
            continue
        sp = normalized_spacings(sub)
        a2 = anderson_darling_stat(sp)
        null = honest_mc_null(len(sp), n_mc, rng)
        p, r = mc_pvalue(a2, null)
        rows.append(dict(
            frac_dropped=frac, t_min=sub[0], n_spacings=len(sp),
            A2=a2, null_median=np.median(null), null_q95=np.quantile(null, 0.95),
            p=p, r=r, n_mc=n_mc,
        ))
    return rows


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--zeros-file", default="zeta_zeros_50k.txt")
    ap.add_argument("--n-mc", type=int, default=2000)
    ap.add_argument("--seed", type=int, default=112)
    ap.add_argument("--t-scan", action="store_true",
                     help="also run the height-dependence diagnostic")
    ap.add_argument("--t-scan-mc", type=int, default=400,
                     help="MC replicates per T-cutoff (smaller, it's per-cutoff)")
    args = ap.parse_args()

    zeros = np.loadtxt(args.zeros_file).reshape(-1)
    zeros.sort()
    print(f"Loaded {len(zeros)} zeta zeros, T in [{zeros[0]:.3f}, {zeros[-1]:.3f}]")

    sp = normalized_spacings(zeros)
    n = len(sp)
    a2_data = anderson_darling_stat(sp)
    print(f"n spacings = {n}")
    print(f"Data: A^2 = {a2_data:.6f} (vs exact GUE beta=2 CDF)")

    rng = np.random.default_rng(args.seed)
    null = honest_mc_null(n, args.n_mc, rng)
    p, r = mc_pvalue(a2_data, null)

    print(f"\nHonest MC null (n_mc={args.n_mc}, i.i.d. draws directly from gue2_cdf, "
          f"NOT bootstrapped from a finite empirical pool):")
    print(f"  median A^2 = {np.median(null):.6f}   (textbook expectation for a correctly")
    print(f"                                  specified continuous null: O(1), ~0.5-1)")
    print(f"  95% quantile = {np.quantile(null, 0.95):.6f}  (classical asymptotic 5% "
          f"critical value ~2.492)")
    print(f"  MC p-value (add-one smoothed) = {p:.6f}  ({r}/{args.n_mc} null draws >= data)")
    verdict = "REJECTED" if p < 0.05 else "not rejected"
    print(f"  H0 (GUE beta=2 surmise): {verdict} at alpha=0.05")

    if args.t_scan:
        print("\n" + "=" * 70)
        print("Height (T) dependence scan -- does A^2 fall as low-T zeros are dropped?")
        print("=" * 70)
        rows = t_dependence_scan(zeros, args.t_scan_mc, rng)
        print(f"{'frac_dropped':>12} {'T_min':>12} {'n':>7} {'A2':>10} "
              f"{'null_med':>9} {'null_q95':>9} {'p':>10}")
        for row in rows:
            print(f"{row['frac_dropped']:>12.2f} {row['t_min']:>12.2f} {row['n_spacings']:>7d} "
                  f"{row['A2']:>10.4f} {row['null_median']:>9.4f} {row['null_q95']:>9.4f} "
                  f"{row['p']:>10.6f}")


if __name__ == "__main__":
    main()
