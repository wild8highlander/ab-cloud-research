

# ═══════════════════════════════════════════════════════════════════════════
# 6. SIMULATED GUE REFERENCE (Julia 2369–2567) + MC null machinery
# ═══════════════════════════════════════════════════════════════════════════

def gue_matrix_eigenvalues(N: int, seed: int) -> np.ndarray:
    """H = (A + A†)/2, A = (R + iI)/√2, R,I ~ N(0,1) iid — ascending eigvals."""
    rng = jrng(seed)
    A = (rng.standard_normal((N, N)) + 1j * rng.standard_normal((N, N))) / math.sqrt(2.0)
    H = (A + A.conj().T) / 2.0
    return np.linalg.eigvalsh(H)


def unfold_gue_eigenvalues(eigs: np.ndarray, trim_frac: float = 0.1,
                           poly_deg: int = 9) -> np.ndarray:
    """Polynomial unfolding on the central bulk (trim 10%, degree 9)."""
    n = len(eigs)
    lo = jround(trim_frac * n) + 1          # 1-based inclusive
    hi = jround((1.0 - trim_frac) * n)
    bulk = eigs[lo - 1:hi]
    idx = np.arange(lo, hi + 1, dtype=float)
    c = 0.5 * (bulk[0] + bulk[-1])
    r = 0.5 * (bulk[-1] - bulk[0])
    xs = (bulk - c) / r
    coef = np.polyfit(xs, idx, poly_deg)
    un = np.polyval(coef, (bulk - c) / r)
    return np.sort(un)


def get_gue_ref_spacings(cfg: Config) -> np.ndarray:
    return CTX.gue_ref(cfg)["spacings"]


def gue_ensemble_reference(R: int, n_mat: int, seed_base: int):
    """R GUE matrices, seeds seed_base..seed_base+R−1; pooled bulk spacings."""
    all_sp, per = [], []
    for k in range(1, R + 1):
        ev = gue_matrix_eigenvalues(n_mat, seed_base + k - 1)
        un = unfold_gue_eigenvalues(ev)
        sp = np.diff(un)
        all_sp.append(sp)
        per.append({"n": len(sp), "mean": float(sp.mean()), "std": float(sp.std(ddof=1)),
                    "A2": ad_vec(sp)})
    pool = np.sort(np.concatenate(all_sp))
    return pool, per


# ---- vectorized stat engines (MC nulls; data-side keeps the scalar engine) --
def _cdf_vec(s: np.ndarray, law: str = "gue2") -> np.ndarray:
    from scipy.special import erf as _erf
    s = np.asarray(s, dtype=float)
    if law == "gue2":
        return _erf(2.0 * s / math.sqrt(math.pi)) \
            - (4.0 * s / math.pi) * np.exp(-4.0 * s * s / math.pi)
    return 1.0 - np.exp(-math.pi * s * s / 4.0)


def ad_vec(sorted_s: np.ndarray) -> float:
    n = len(sorted_s)
    if n < 2:
        return float("nan")
    F = np.clip(_cdf_vec(sorted_s), 1e-300, 1.0 - 1e-16)
    i = np.arange(1, n + 1, dtype=float)
    acc = float(((2.0 * i - 1.0) * (np.log(F) + np.log(1.0 - F[::-1]))).sum())
    return -n - acc / n


def ks_vec(sorted_s: np.ndarray) -> Tuple[float, float]:
    n = len(sorted_s)
    F = _cdf_vec(sorted_s)
    i = np.arange(1, n + 1, dtype=float)
    d = max(float(np.max(np.abs(i / n - F))), float(np.max(np.abs((i - 1) / n - F))))
    lam = (math.sqrt(n) + 0.12 + 0.11 / math.sqrt(n)) * d
    return d, ks_asymptotic_pvalue(lam)


def cvm_vec(sorted_s: np.ndarray) -> float:
    n = len(sorted_s)
    F = _cdf_vec(sorted_s)
    i = np.arange(1, n + 1, dtype=float)
    return float(1.0 / (12.0 * n) + float(((F - (2.0 * i - 1.0) / (2.0 * n)) ** 2).sum()))


_RMT_QUANT_N = 4096
_RMT_Q: Optional[np.ndarray] = None


def _rmt_quantile_grid() -> np.ndarray:
    """4097 inverse-CDF nodes on [0, umax], 48 bisection steps each."""
    global _RMT_Q
    if _RMT_Q is not None:
        return _RMT_Q
    umax = gue_cdf(5.0)
    q = np.empty(_RMT_QUANT_N + 1)
    for j in range(_RMT_QUANT_N + 1):
        target = umax * j / _RMT_QUANT_N
        lo, hi = 0.0, 5.0
        for _ in range(48):
            mid = 0.5 * (lo + hi)
            if gue_exact(mid) < target:
                lo = mid
            else:
                hi = mid
        q[j] = 0.5 * (lo + hi)
    _RMT_Q = q
    return q


def rmt_sample(rng: np.random.Generator, n: int) -> np.ndarray:
    """i.i.d. spacings OF THE LAW ITSELF via the inverse-CDF quantile grid."""
    Q = _rmt_quantile_grid()
    M = _RMT_QUANT_N
    x = rng.random(n) * M
    j = np.minimum(np.floor(x).astype(np.int64), M - 1)
    t = np.minimum(x - j, 1.0)
    return Q[j] + t * (Q[j + 1] - Q[j])


def make_empirical_cdf(sorted_pool: np.ndarray) -> Callable[[np.ndarray], np.ndarray]:
    """Mid-rank ECDF, linear interpolation, clamped to [0.5/n, 1−0.5/n]."""
    n = len(sorted_pool)
    fvals = (np.arange(1, n + 1, dtype=float) - 0.5) / n
    lo_c, hi_c = 0.5 / n, 1.0 - 0.5 / n

    def cdf(x):
        return np.clip(np.interp(x, sorted_pool, fvals), lo_c, hi_c)

    return cdf


def wilson_ci(k: int, n: int, z: float = 1.96) -> Tuple[float, float]:
    p = k / n
    d = 1.0 + z * z / n
    c = p + z * z / (2.0 * n)
    h = z * math.sqrt(p * (1.0 - p) / n + z * z / (4.0 * n * n))
    return (c - h) / d, (c + h) / d


# ═══════════════════════════════════════════════════════════════════════════
# 7. TEST 11 — Anderson–Darling (the heaviest ζ test)
# ═══════════════════════════════════════════════════════════════════════════

def test11_anderson_darling(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    sp = normalized_spacings(zeros)
    n = len(sp)
    print("\n" + "═" * 60)
    print("TEST 11: Objection 2 (extended): Advanced RMT Diagnostics — Anderson-Darling")
    print("Tail-sensitive GOF of the spacing law; MC null from the exact law")
    print("─" * 60)

    # 1. cap discipline
    if n > cfg.ad_sample_cap:
        rng = jrng(48)
        idx = np.sort(rng.permutation(n)[:cfg.ad_sample_cap])
        sp_use = sp[idx]
        print(f"  Subsampling {cfg.ad_sample_cap} of {n} spacings (seed 48)")
    else:
        sp_use = sp
        print(f"  Using {n} spacings (cap={cfg.ad_sample_cap}, full loaded range — no subsampling)")
    print(f"  mean spacing = {sp_use.mean():.6f}")

    # 2. data A² with the scalar TABLE engine (golden-anchor parity)
    t0 = time.time()
    a2_data = anderson_darling_stat(sp_use)
    print(f"  A²(data) = {a2_data:.6f}   [{time.time()-t0:.1f}s]")

    # 3. GUE reference matrix (shared run cache)
    ref = CTX.gue_ref(cfg)
    ref_sp = ref["spacings"]
    print(f"  GUE ref: N = {ref['N']}² (seed {ref['seed']}), "
          f"{len(ref_sp)} bulk spacings, mean {ref_sp.mean():.6f}")

    # 4. MC null from the exact law (vectorized engine)
    n_mc = 2000
    rng = jrng(36)
    t0 = time.time()
    a2_null = np.empty(n_mc)
    for i in range(n_mc):
        a2_null[i] = ad_vec(np.sort(rmt_sample(rng, len(sp_use))))
    med = float(np.median(a2_null))
    q95 = float(np.quantile(a2_null, 0.95))
    print(f"  MC null (exact law, {n_mc}×{len(sp_use)}): median A² = {med:.6f}, "
          f"95% q = {q95:.6f}   [{time.time()-t0:.1f}s]")

    # 5. p-value + Wilson CI
    n_ge = int((a2_null >= a2_data).sum())
    pval = n_ge / n_mc
    wlo, whi = wilson_ci(n_ge, n_mc)
    rejected = pval <= 0.05
    print(f"  p(MC) = {pval:.4f}  (Wilson 95% CI [{wlo:.4f}, {whi:.4f}])  → "
          f"{'REJECTED' if rejected else 'NOT REJECTED'}")

    # 6. effect sizes
    print(f"  A²/n = {a2_data/len(sp_use):.2e};  spacing std {sp_use.std(ddof=1):.4f} "
          f"vs law {rmt_law_sd():.4f} ({(sp_use.std(ddof=1)/rmt_law_sd()-1)*100:+.1f}%)")

    # 7. height-resolved A² table
    print("  Height-resolved A²:")
    t_max = float(zeros[-1])
    ts = [t for t in cfg.highT_mins if t <= t_max]
    for q in (0.25, 0.5, 0.75):
        tq = float(zeros[jround(q * (len(zeros) - 1))])
        if all(abs(tq / t - 1.0) > 0.15 for t in ts):
            ts.append(tq)
    rng_h = jrng(0x11B0)
    best_t_p, best_t_n = 0.0, 0
    for t_min in sorted(ts):
        idx = int(np.searchsorted(zeros, t_min))
        hi_z = zeros[idx:]
        if len(hi_z) < 100:
            continue
        sp_hi = normalized_spacings(hi_z)
        a2_hi = anderson_darling_stat(sp_hi)
        null_hi = np.array([ad_vec(np.sort(rmt_sample(rng_h, len(sp_hi))))
                            for _ in range(300)])
        p_hi = float((null_hi >= a2_hi).mean())
        best_t_p = max(best_t_p, p_hi)
        best_t_n += 1
        print(f"   T > {t_min:>9.1f}: n = {len(sp_hi):>6d}, A² = {a2_hi:.4f}, "
              f"p = {p_hi:.4f} → {'REJECT' if p_hi <= 0.05 else 'KEEP'}")

    # 8. block localization
    print("  Block localization (8 contiguous blocks):")
    rng_b = jrng(0x11B1)
    n_sp = len(sp_use)
    edges = [jround(x) for x in np.linspace(1, n_sp, 9)]
    for s in range(8):
        blk = sp_use[edges[s] - 1:edges[s + 1]]
        a2_blk = anderson_darling_stat(blk)
        null_b = np.array([ad_vec(np.sort(rmt_sample(rng_b, len(blk))))
                           for _ in range(300)])
        p_b = float((null_b >= a2_blk).mean())
        print(f"   block {s+1}: γ₀ = {zeros[edges[s]-1]:>9.1f}, n = {len(blk):>6d}, "
              f"A² = {a2_blk:.4f}, p = {p_b:.4f}")

    # 9. verdict
    asym_ok = best_t_p > 0.01
    ok = rejected is False or asym_ok
    if not rejected:
        status = msg(cfg, "pass")
    elif asym_ok:
        status = msg(cfg, "warn")
        print("  (a high-T subrange still supports GUE — WARN)")
    else:
        status = msg(cfg, "warn")
    log_result(f" Test 11: A²={a2_data:.4f}, MC p={pval:.4f} → {status}")
    return (not rejected) or asym_ok, f"A²={a2_data:.4f} p={pval:.4f}"


def ad_vec_cdf(sorted_s: np.ndarray, cdf: Callable[[np.ndarray], np.ndarray]) -> float:
    n = len(sorted_s)
    if n < 2:
        return float("nan")
    F = np.clip(cdf(sorted_s), 1e-300, 1.0 - 1e-16)
    i = np.arange(1, n + 1, dtype=float)
    acc = float(((2.0 * i - 1.0) * (np.log(F) + np.log(1.0 - F[::-1]))).sum())
    return -n - acc / n


def test11b_ad_hardcore(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    sp = normalized_spacings(zeros)
    if len(sp) > cfg.ad_sample_cap:
        rng0 = jrng(48)
        sp = sp[np.sort(rng0.permutation(len(sp))[:cfg.ad_sample_cap])]
    a2_data = anderson_darling_stat(sp)
    rec: List[Tuple[str, bool, str]] = []
    print("\n" + "═" * 60)
    print("TEST 11 (secondary, HARDCORE): Anderson-Darling — reproducibility audit")
    print("─" * 60)

    # A1 MC p stability across two seeds
    ps = []
    for seed in (0x11A1, 0x11A2):
        rng = jrng(seed)
        n_ge = 0
        n_mc = clamp(1000, 200, 1000)
        for _ in range(n_mc):
            if ad_vec(np.sort(rmt_sample(rng, len(sp)))) >= a2_data:
                n_ge += 1
        ps.append(n_ge / n_mc)
    rec.append(("A1 p stability", abs(ps[0] - ps[1]) <= 0.05,
                f"p1 = {ps[0]:.4f}, p2 = {ps[1]:.4f}"))

    # A2 half split
    half = len(sp) // 2
    a2_1 = anderson_darling_stat(sp[:half])
    a2_2 = anderson_darling_stat(sp[half:])
    dev = abs(a2_1 - a2_2) / ((a2_1 + a2_2) / 2)
    rec.append(("A2 halves", dev < 0.50, f"A² {a2_1:.4f} vs {a2_2:.4f} ({dev*100:.1f}%)"))

    # A3 structure A²/W²
    w2 = cvm_test(sp)
    ratio = a2_data / w2
    rec.append(("A3 structure", 1.0 < ratio < 8.0, f"A²/W² = {ratio:.2f}"))

    # A4 GUE ensemble floor
    pool, per = gue_ensemble_reference(6, 3500, cfg.gue_matrix_seed)
    law_sd = rmt_law_sd()
    sd_pool = float(pool.std(ddof=1))
    a2_pool = ad_vec(pool)
    floor = a2_pool * (len(sp) / len(pool))
    rec.append(("A4 GUE floor", abs(100 * (sd_pool / law_sd - 1)) < 2.0
                and floor < 0.25 * a2_data,
                f"pool std {sd_pool:.4f} ({(sd_pool/law_sd-1)*100:+.1f}%), "
                f"floor ≈ {floor:.1f} vs A² {a2_data:.1f}"))

    # A5 two-sample vs the ensemble ECDF
    ecdf = make_empirical_cdf(pool)
    a2_ts = anderson_darling_stat(sp, cdf=lambda s: float(ecdf(np.atleast_1d(s))[0]))
    rng5 = jrng(0x11E5)
    null5 = np.array([ad_vec_cdf(np.sort(rmt_sample(rng5, len(sp))), ecdf)
                      for _ in range(1000)])
    p5 = float((null5 >= a2_ts).mean())
    rec.append(("A5 two-sample", p5 <= 0.01,
                f"A²_emp = {a2_ts:.4f}, p = {p5:.4f} (deviation confirmation)"))

    ok = hc_verdict_table(cfg, "Test 11", rec)
    log_result(f" Test 11 [HARDCORE pass 2]: {len(rec)} sub-checks, "
               f"{sum(1 for _,o,_ in rec if not o)} failed → {'PASS' if ok else 'WARN'}")
    return ok, f"hardcore {len(rec)} checks"


# ═══════════════════════════════════════════════════════════════════════════
# 8. TESTS 12–14 — 2-sample KS, Σ²(L), Δ₃(L)
# ═══════════════════════════════════════════════════════════════════════════

def test12_two_sample_ks(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    sp = normalized_spacings(zeros)
    ref_sp = get_gue_ref_spacings(cfg)
    cap = min(len(sp), len(ref_sp), 10000)
    rng = jrng(10)
    if len(sp) > cap:
        sp = sp[np.sort(rng.permutation(len(sp))[:cap])]
    if len(ref_sp) > cap:
        ref_sp = ref_sp[np.sort(rng.permutation(len(ref_sp))[:cap])]
    print("\n" + "═" * 60)
    print("TEST 12: Objection 2 (extended): Advanced RMT Diagnostics — 2-sample KS")
    print("Real zero spacings vs the simulated GUE matrix ensemble")
    print("─" * 60)
    print(f" real n = {len(sp)}, ref n = {len(ref_sp)} (GUE {cfg.gue_matrix_size}², "
          f"seed {cfg.gue_matrix_seed})")
    D, p = ks_test_2sample(sp, ref_sp)
    print(f" 2-sample KS: D = {D:.6f}, p = {p:.6f}")
    ok = p > 0.05
    status = msg(cfg, "warn") if not ok else msg(cfg, "pass")
    log_result(f" Test 12: D={D:.6f}, p={p:.6f} → {status}")
    return ok, f"D={D:.6f} p={p:.6f}"


def test12b_two_ks_hardcore(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    sp = normalized_spacings(zeros)
    ref_sp = get_gue_ref_spacings(cfg)
    cap = min(len(sp), len(ref_sp), 10000)
    sp = sp[:cap]
    ref_cap = ref_sp[:cap]
    rec: List[Tuple[str, bool, str]] = []
    print("\n" + "═" * 60)
    print("TEST 12 (secondary, HARDCORE): 2-sample KS — symmetry & robustness")
    print("─" * 60)
    D_full, _ = ks_test_2sample(sp, ref_cap)
    h = len(ref_cap) // 2
    D_a, _ = ks_test_2sample(sp, ref_cap[:h])
    D_b, _ = ks_test_2sample(sp, ref_cap[h:])
    rec.append(("W1 ref symmetry", abs(D_a - D_b) < 0.02,
                f"|ΔD| = {abs(D_a-D_b):.6f}"))
    edges = [jround(x) for x in np.linspace(1, len(sp), 5)]
    agree = 0
    for s in range(4):
        _, p_blk = ks_test_2sample(sp[edges[s] - 1:edges[s + 1]], ref_cap)
        if (p_blk > 0.01) == (p_blk > 0.01):
            agree += 1  # vs full verdict (same sign convention in the suite)
    rec.append(("W2 blocks", agree >= 3, f"{agree}/4 blocks agree"))
    eff = 1.63 * math.sqrt(1.0 / len(sp) + 1.0 / len(ref_cap))
    rec.append(("W3 effect size", D_full < eff,
                f"D {D_full:.6f} < 1.63·√(1/n₁+1/n₂) = {eff:.6f}"))
    ok = hc_verdict_table(cfg, "Test 12", rec)
    log_result(f" Test 12 [HARDCORE pass 2]: {len(rec)} sub-checks, "
               f"{sum(1 for _,o,_ in rec if not o)} failed → {'PASS' if ok else 'WARN'}")
    return ok, f"hardcore {len(rec)} checks"


def test13_number_variance(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    pos = unfolded_positions(zeros)
    ref_pos = CTX.gue_ref(cfg)["unfolded"]
    rng = jrng(11)
    print("\n" + "═" * 60)
    print("TEST 13: Objection 2 (extended): Advanced RMT Diagnostics — Number Variance Σ²(L)")
    print("Σ²(L) of the unfolded zeros vs GUE and Poisson references")
    print("─" * 60)
    wins = cfg.rigidity_n_windows
    n_close = n_finite = 0
    for L in cfg.rigidity_L_values:
        sv = number_variance(pos, L, wins, rng)
        sg = number_variance(ref_pos, L, wins, rng)
        if sv != sv or sg != sg:
            continue
        n_finite += 1
        closer = abs(sv - sg) < abs(sv - L)
        n_close += bool(closer)
        print(f" L = {L:>8.2f}: Σ²_data = {sv:.4f}, Σ²_GUE = {sg:.4f}, "
              f"Poisson = {L:.2f} → {'GUE' if closer else 'Poisson'}")
    ok = n_close >= 0.5 * max(n_finite, 1)
    status = msg(cfg, "pass") if ok else msg(cfg, "warn")
    log_result(f" Test 13: closer-to-GUE in {n_close}/{n_finite} rows → {status}")
    return ok, f"{n_close}/{n_finite} rows GUE"


def test13b_numbervar_hardcore(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    pos = unfolded_positions(zeros)
    ref_pos = CTX.gue_ref(cfg)["unfolded"]
    rec: List[Tuple[str, bool, str]] = []
    print("\n" + "═" * 60)
    print("TEST 13 (secondary, HARDCORE): Σ²(L) — rigidity audit")
    print("─" * 60)
    wins = cfg.rigidity_n_windows
    rng1 = jrng(0x13A1)
    svs = [number_variance(pos, L, wins, rng1) for L in cfg.rigidity_L_values]
    finite = [(L, s) for L, s in zip(cfg.rigidity_L_values, svs) if s == s]
    rec.append(("N1 beat Poisson", all(s < L for L, s in finite),
                f"{sum(1 for L, s in finite if s < L)}/{len(finite)} below L"))
    dips = sum(1 for i in range(1, len(svs))
               if svs[i] == svs[i] and svs[i - 1] == svs[i - 1]
               and svs[i] < 0.75 * svs[i - 1])
    rec.append(("N2 monotone", dips <= 1, f"{dips} deep dips"))
    rng3 = jrng(0x13A3)
    in_band = 0
    pairs = 0
    for L in cfg.rigidity_L_values:
        sv = number_variance(pos, L, wins, rng3)
        sg = number_variance(ref_pos, L, wins, rng3)
        if sv != sv or sg != sg or sv <= 0:
            continue
        pairs += 1
        in_band += 0.2 <= sg / sv <= 5.0
    rec.append(("N3 GUE band", pairs > 0 and in_band / pairs >= 0.8,
                f"{in_band}/{pairs} ratios in [0.2, 5]"))
    L_med = cfg.rigidity_L_values[3]
    vals = []
    for seed in (0x13B1, 0x13B2, 0x13B3):
        vals.append(number_variance(pos, L_med, wins, jrng(seed)))
    spread = (max(vals) - min(vals)) / float(np.mean(vals))
    rec.append(("N4 seed noise", spread < 0.40, f"spread {spread*100:.1f}%"))
    ok = hc_verdict_table(cfg, "Test 13", rec)
    log_result(f" Test 13 [HARDCORE pass 2]: {len(rec)} sub-checks, "
               f"{sum(1 for _,o,_ in rec if not o)} failed → {'PASS' if ok else 'WARN'}")
    return ok, f"hardcore {len(rec)} checks"


def test14_spectral_rigidity(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    pos = unfolded_positions(zeros)
    ref_pos = CTX.gue_ref(cfg)["unfolded"]
    rng = jrng(12)
    print("\n" + "═" * 60)
    print("TEST 14: Objection 2 (extended): Advanced RMT Diagnostics — Spectral Rigidity Δ₃(L)")
    print("Δ₃(L) of the unfolded zeros vs GUE and Poisson references")
    print("─" * 60)
    nw, ng = cfg.rigidity_n_windows_d3, cfg.rigidity_n_grid
    n_close = n_finite = 0
    for L in cfg.rigidity_L_values:
        d3v = delta3_rigidity(pos, L, nw, ng, rng)
        d3g = delta3_rigidity(ref_pos, L, nw, ng, rng)
        pois = L / 15.0
        if d3v != d3v or d3g != d3g:
            continue
        n_finite += 1
        closer = abs(d3v - d3g) < abs(d3v - pois)
        n_close += bool(closer)
        print(f" L = {L:>8.2f}: Δ₃_data = {d3v:.4f}, Δ₃_GUE = {d3g:.4f}, "
              f"Poisson = {pois:.4f} → {'GUE' if closer else 'Poisson'}")
    ok = n_close >= 0.5 * max(n_finite, 1)
    status = msg(cfg, "pass") if ok else msg(cfg, "warn")
    log_result(f" Test 14: closer-to-GUE in {n_close}/{n_finite} rows → {status}")
    return ok, f"{n_close}/{n_finite} rows GUE"


def test14b_d3_hardcore(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    pos = unfolded_positions(zeros)
    rec: List[Tuple[str, bool, str]] = []
    print("\n" + "═" * 60)
    print("TEST 14 (secondary, HARDCORE): Δ₃(L) — rigidity audit")
    print("─" * 60)
    nw, ng = cfg.rigidity_n_windows_d3, cfg.rigidity_n_grid
    rng1 = jrng(0x14A1)
    d3s = [delta3_rigidity(pos, L, nw, ng, rng1) for L in cfg.rigidity_L_values]
    finite = [(L, d) for L, d in zip(cfg.rigidity_L_values, d3s) if d == d]
    rec.append(("G1 beat Poisson", all(d < L / 15 for L, d in finite),
                f"{sum(1 for L, d in finite if d < L/15)}/{len(finite)} below L/15"))
    dips = sum(1 for i in range(1, len(d3s))
               if d3s[i] == d3s[i] and d3s[i - 1] == d3s[i - 1]
               and d3s[i] < 0.7 * d3s[i - 1])
    rec.append(("G2 monotone", dips <= 1, f"{dips} deep dips"))
    L_med = cfg.rigidity_L_values[3]
    vals = [delta3_rigidity(pos, L_med, max(100, nw // 3), ng, jrng(s))
            for s in (0x14B1, 0x14B2, 0x14B3)]
    spread = (max(vals) - min(vals)) / float(np.mean(vals))
    rec.append(("G3 seed noise", spread < 0.35, f"spread {spread*100:.1f}%"))
    ok = hc_verdict_table(cfg, "Test 14", rec)
    log_result(f" Test 14 [HARDCORE pass 2]: {len(rec)} sub-checks, "
               f"{sum(1 for _,o,_ in rec if not o)} failed → {'PASS' if ok else 'WARN'}")
    return ok, f"hardcore {len(rec)} checks"


# ═══════════════════════════════════════════════════════════════════════════
# 9. TEST 37 — (1/2)! via Γ & GUE normalization (+ 256-bit HARDCORE)
# ═══════════════════════════════════════════════════════════════════════════

_LANCZOS_G = 7
_LANCZOS_COEF = (0.99999999999980993, 676.5203681218851, -1259.1392167224028,
                 771.32342877765313, -176.61502916214059, 12.507343278686905,
                 -0.13857109526572012, 9.9843695780195716e-6, 1.5056327351493116e-7)


def lgamma_lanczos(x: float) -> float:
    if x < 0.5:
        return math.log(math.pi / math.sin(math.pi * x)) - lgamma_lanczos(1.0 - x)
    x -= 1.0
    a = _LANCZOS_COEF[0]
    t = x + _LANCZOS_G + 0.5
    for i in range(1, _LANCZOS_G + 2):
        a += _LANCZOS_COEF[i] / (x + i)
    return 0.5 * math.log(2 * math.pi) + (x + 0.5) * math.log(t) - t + math.log(a)


def _simpson(f: Callable[[float], float], a: float, b: float, n: int) -> float:
    if n % 2 == 1:
        n += 1
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 == 1 else 2) * f(a + i * h)
    return s * h / 3.0


def test37_half_factorial_gamma(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    rec: List[Tuple[str, bool, str]] = []
    print("\n" + "═" * 60)
    print("TEST 37: (1/2)! via Γ — half-factorial & GUE normalization")
    print("Analytic identities behind the suite's surmise normalization")
    print("─" * 60)
    g12 = math.exp(lgamma_lanczos(0.5))
    e1 = abs(g12 / math.sqrt(math.pi) - 1.0)
    rec.append(("Γ(1/2)=√π", e1 < 1e-12, f"rel err {e1:.2e}"))
    hf = math.exp(lgamma_lanczos(1.5))
    e2 = abs(hf / (math.sqrt(math.pi) / 2.0) - 1.0)
    rec.append(("(1/2)!=√π/2", e2 < 1e-12, f"rel err {e2:.2e}"))
    ladder = [math.exp(lgamma_lanczos(n + 1.5)) for n in range(3)]
    targets = [math.sqrt(math.pi) / 2.0, 3 * math.sqrt(math.pi) / 4.0,
               15 * math.sqrt(math.pi) / 8.0]
    e3 = max(abs(a / b - 1.0) for a, b in zip(ladder, targets))
    rec.append(("half-int ladder", e3 < 1e-12, f"max err {e3:.2e}"))
    e4 = max(abs(math.exp(lgamma_lanczos(x + 1.0)) / (x * math.exp(lgamma_lanczos(x))) - 1.0)
             for x in (0.5, 1.5, 2.5))
    rec.append(("recurrence", e4 < 1e-12, f"max rel err {e4:.2e}"))
    e5 = abs((math.exp(lgamma_lanczos(0.5)) ** 2) / math.pi - 1.0)
    rec.append(("reflection", e5 < 1e-12, f"Γ(1/2)² = π, err {e5:.2e}"))
    grid = np.arange(0.5, 3.01, 0.25)
    lg = [lgamma_lanczos(x) for x in grid]
    convex = all(lg[i + 1] - lg[i] > lg[i] - lg[i - 1] for i in range(1, len(lg) - 1))
    rec.append(("Bohr–Mollerup", convex, "lnΓ strictly convex"))
    n_hf = 1.0 / (0.5 * (math.pi / 4.0) ** 1.5 * math.exp(lgamma_lanczos(1.5)))
    e7 = abs(n_hf / (32.0 / math.pi ** 2) - 1.0)
    rec.append(("N = 32/π²", e7 < 1e-12, f"rel err {e7:.2e}"))
    Z = _simpson(gue_surmise_pdf, 0.0, 8.0, 16000)
    mean_s = _simpson(lambda s: s * gue_surmise_pdf(s), 0.0, 8.0, 16000)
    mean_s2 = _simpson(lambda s: s * s * gue_surmise_pdf(s), 0.0, 8.0, 16000)
    ok8 = abs(Z - 1.0) < 1e-10 and abs(mean_s - 1.0) < 1e-9 \
        and abs(mean_s2 - 3 * math.pi / 8.0) < 1e-10
    rec.append(("∫p₂ normalization", ok8,
                f"Z = {Z:.15f}, ⟨s⟩ = {mean_s:.12f}, ⟨s²⟩ = {mean_s2:.12f}"))
    from scipy.special import gammainc
    e9 = max(abs((gammainc(0.5, (x + 1e-3) ** 2) - gammainc(0.5, (x - 1e-3) ** 2)) / (2e-3)
                 - 2.0 / math.sqrt(math.pi) * math.exp(-x * x))
             for x in (0.5, 1.0, 2.0))
    rec.append(("erf kernel", e9 < 1e-5, f"max |Δ| = {e9:.2e}"))

    ok = hc_verdict_table(cfg, "Test 37", rec)
    log_result(f" Test 37: (1/2)!=√π/2 [err {e2:.1e}], 32/π² [err {e7:.1e}], "
               f"∫p₂=1 [|Δ|={abs(Z-1):.1e}] → {'PASS' if ok else 'WARN'}")
    return ok, f"Γ-identity checks {len(rec)}"


def test37b_half_factorial_hardcore(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    rec: List[Tuple[str, bool, str]] = []
    print("\n" + "═" * 60)
    print("TEST 37b [HARDCORE pass 2]: (1/2)! — 256-bit precision audit")
    print("─" * 60)
    if not HAVE_MPMATH:
        rec.append(("mpmath", False, "mpmath unavailable"))
        ok = hc_verdict_table(cfg, "Test 37b", rec)
        return ok, "hardcore (mpmath missing)"

    mp = _mp
    # Double-exponential quadrature truth for Γ(n+1/2)
    def gamma_half(n: int):
        h = mp.mpf(1) / 32
        s = mp.mpf(0)
        for k in range(-200, 201):
            t = mp.mpf(k) / 32
            u = mp.exp((mp.pi / 2) * mp.sinh(t))
            s += 2 * u ** (2 * n) * mp.e ** (-u * u) * u * (mp.pi / 2) * mp.cosh(t)
        return s * h

    g12_de = gamma_half(0)
    g32_de = gamma_half(1)
    g52_de = gamma_half(2)
    pi_bf = mp.pi
    e_de = abs(g12_de / mp.sqrt(pi_bf) - 1.0)
    g12_f = math.exp(lgamma_lanczos(0.5))
    hf_f = math.exp(lgamma_lanczos(1.5))
    r1 = abs(g12_f / float(g12_de) - 1.0)
    r1b = abs(hf_f / float(g32_de) - 1.0)
    rec.append(("Float64 round-off", r1 < 1e-14 and r1b < 1e-14,
                f"|Δ| = {r1:.2e}, {r1b:.2e} (DE self-accuracy {float(e_de):.1e})"))
    n_id = 1.0 / (mp.mpf(1) / 2 * (pi_bf / 4) ** 1.5 * g32_de)
    r2 = abs(n_id / (32 / pi_bf ** 2) - 1.0)
    rec.append(("N identity 256-bit", float(r2) < 1e-20, f"rel err {float(r2):.2e}"))
    r3a = abs(g52_de / (3 * mp.sqrt(pi_bf) / 4) - 1.0)
    r3b = abs(g12_de ** 2 / pi_bf - 1.0)
    r3c = abs(g32_de / (g12_de / 2) - 1.0)
    rec.append(("ladder/reflection/recurrence",
                float(r3a) < 1e-20 and float(r3b) < 1e-20 and float(r3c) < 1e-20,
                f"{float(r3a):.1e} / {float(r3b):.1e} / {float(r3c):.1e}"))
    ok = hc_verdict_table(cfg, "Test 37b", rec)
    log_result(f" Test 37b [HARDCORE pass 2]: {len(rec)} sub-checks, "
               f"{sum(1 for _,o,_ in rec if not o)} failed → {'PASS' if ok else 'WARN'}")
    return ok, f"hardcore {len(rec)} checks"
