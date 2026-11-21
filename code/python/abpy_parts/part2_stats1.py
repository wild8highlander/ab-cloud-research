

# ═══════════════════════════════════════════════════════════════════════════
# 4. RUN CONTEXT (caches shared by the tests) + HARDCORE helpers
# ═══════════════════════════════════════════════════════════════════════════

class Ctx:
    """Run-wide caches: the Gram deviate series d_k and the GUE reference."""

    def __init__(self):
        self._d_series: Optional[np.ndarray] = None
        self._b_pref: Optional[np.ndarray] = None
        self._gue_ref = None          # cache dict (eigs, unfolded, spacings, N, seed)

    def d_series(self, zeros: np.ndarray) -> np.ndarray:
        if self._d_series is None or len(self._d_series) != len(zeros):
            n = len(zeros)
            d = np.empty(n)
            for k in range(1, n + 1):
                d[k - 1] = abs(zeros[k - 1] - gram_point(k))
            self._d_series = d
            pref = np.empty(n + 1)
            pref[0] = 0.0
            pref[1:] = np.cumsum(d)
            self._b_pref = pref / np.arange(0, n + 1, dtype=float)
            self._b_pref[0] = 0.0
        return self._d_series

    def b_pref(self, zeros: np.ndarray) -> np.ndarray:
        self.d_series(zeros)
        return self._b_pref

    def gue_ref(self, cfg: Config):
        if self._gue_ref is not None:
            return self._gue_ref
        N, seed = cfg.gue_matrix_size, cfg.gue_matrix_seed
        # RAM guard (spec §1.17: "RAM guard may downscale") — 3 dense copies
        # of an N² complex matrix must fit the session budget.
        n_cap = int(math.sqrt(1.4e9 / (16.0 * 3.2)))
        if N > n_cap:
            print(f"  [GUE ref RAM guard] {N}² exceeds the session budget → {n_cap}² "
                  f"(frozen v19 run kept 12000²; statistical columns shift, "
                  f"data-side numbers unaffected)")
            N = n_cap
        t0 = time.time()
        print(f"  [GUE ref] building {N}x{N} simulated GUE matrix (seed {seed}) …")
        eigs = gue_matrix_eigenvalues(N, seed)
        un = unfold_gue_eigenvalues(eigs)
        sp = np.diff(un)
        self._gue_ref = {"eigs": eigs, "unfolded": un, "spacings": sp, "N": N, "seed": seed}
        print(f"  [GUE ref] done in {time.time()-t0:.0f}s — {len(sp)} bulk spacings")
        return self._gue_ref


CTX = Ctx()


def hc_bN_series(zeros: np.ndarray) -> np.ndarray:
    """d_k = |γ_k − γ̃_k| (Julia 10606) — the raw Gram deviate series."""
    return CTX.d_series(zeros)


def hc_dense_grid(max_N: int, start: int = 25, ratio: float = 1.22) -> List[int]:
    """Julia 10620–10640: 25 · 1.22^k checkpoints + final max_N (40 pts at 50k)."""
    dens = []
    n = start
    while n < max_N:
        dens.append(n)
        n = max(jround(n * ratio), n + 1)
    dens.append(max_N)
    return dens


def hc_walkforward_errors(dens: List[int], b_dense: np.ndarray) -> Tuple[float, float]:
    """Out-of-sample prediction error, best of 3 laws refit on revealed points."""
    n = len(dens)
    if n < 6:
        return float("nan"), float("nan")
    split = clamp(jround(0.6 * n), 3, n - 2)
    errs = []
    for i in range(split, n):          # hidden points (0-based)
        Ns = np.array(dens[:i], dtype=float)
        bs = b_dense[:i]
        Ni, bi = dens[i], b_dense[i]
        pred_a = pred_b = pred_c = float("nan")
        if i >= 3:
            _, slope_a, _, _, _ = linreg(np.log(Ns), np.log(bs))
            pred_a = math.exp(np.log(bs).mean() - slope_a * np.log(Ns).mean()
                              + slope_a * math.log(Ni))
            inv_logN = 1.0 / np.log(Ns)
            a2, b2, _, _, _ = linreg(inv_logN, bs)
            pred_b = a2 + b2 / math.log(Ni)
        if i >= 2:
            l1, l2 = math.log(bs[-1]), math.log(bs[-2])
            n1, n2 = math.log(Ns[-1]), math.log(Ns[-2])
            if n1 != n2:
                slope_c = (l1 - l2) / (n1 - n2)
                pred_c = math.exp(l1 + slope_c * (math.log(Ni) - n1))
        cands = [p for p in (pred_a, pred_b, pred_c) if p == p and p > 0]
        if not cands:
            continue
        errs.append(min(abs(p - bi) / bi for p in cands))
    if not errs:
        return float("nan"), float("nan")
    e = np.array(errs)
    return float(np.median(e)), float(e.max())


def hc_verdict_table(cfg: Config, label: str, rec: List[Tuple[str, bool, str]]) -> bool:
    """Julia hc_verdict_table — prints sub-check rows, all-pass boolean."""
    print("─" * 60)
    n_fail = 0
    for name, ok, note in rec:
        if not ok:
            n_fail += 1
        print(f" {name:<20} {'PASS' if ok else 'WARN'} — {note}")
    print("─" * 60)
    overall = "PASS" if n_fail == 0 else "WARN"
    print(f" {label} [HARDCORE pass 2]: {len(rec)} sub-checks, {n_fail} failed → {overall}")
    return n_fail == 0


# ═══════════════════════════════════════════════════════════════════════════
# 5. TESTS 1–10 (ζ statistics, primary + HARDCORE variants)
# ═══════════════════════════════════════════════════════════════════════════

def test1_convergence_table(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    max_N = len(zeros)
    pref = CTX.b_pref(zeros)
    if cfg.n_checkpoints <= 0:
        checkpoints = [100, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000]
    else:
        r = max_N ** (1.0 / cfg.n_checkpoints)
        checkpoints = []
        n = 1
        for _ in range(cfg.n_checkpoints):
            checkpoints.append(n)
            n = jround(n * r)
        if not checkpoints or checkpoints[-1] < max_N:
            checkpoints.append(max_N)
    checkpoints = [c for c in checkpoints if c <= max_N]

    print("\n" + "═" * 60)
    print(f"TEST 1: {msg(cfg, 'obj1_title')} — Convergence Table")
    print("Check that b(N) = (1/N) Σ|γ_k − γ̃_k| converges")
    print("─" * 60)
    prev = None
    b_final = pref[min(max_N, len(pref) - 1)]
    for N in checkpoints:
        bN = pref[N]
        delta = (bN - prev) if prev is not None else float("nan")
        ds = f"{delta:+.10f}" if delta == delta else "—"
        print(f"{N:>10d}  {bN:>20.10f}  {ds:>20s}")
        prev = bN
    ok = b_final < cfg.bN_pass_threshold
    status = msg(cfg, "pass") if ok else msg(cfg, "warn")
    print(f"\n Verdict: b({max_N}) = {b_final:.4f} (threshold {cfg.bN_pass_threshold}) → {status}")
    log_result(f" Test 1: b(N={max_N}) = {b_final:.4f} → {status}")
    return ok, f"b({max_N})={b_final:.4f}"


def test1b_convergence_hardcore(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    max_N = len(zeros)
    d = hc_bN_series(zeros)
    pref = CTX.b_pref(zeros)
    b_final = pref[max_N]
    rec: List[Tuple[str, bool, str]] = []

    print("\n" + "═" * 60)
    print("TEST 1 (secondary, HARDCORE): b(N) — deep convergence validation")
    print("─" * 60)

    # H0 reproduce direct vs prefix
    worst = 0.0
    for N in (100, 1000, 10000, 50000):
        if N <= max_N:
            worst = max(worst, abs(compute_bN(zeros, N) - pref[N]))
    rec.append(("H0 reproduce", worst < 1e-9, f"max|direct−prefix| = {worst:.2e}"))

    # H1 dense scan
    dens = hc_dense_grid(max_N)
    b_dense = np.array([pref[n] for n in dens])
    print(f" H1 dense scan — {len(dens)} checkpoints (25·1.22^k + {max_N}):")
    prev = None
    for n, b in zip(dens, b_dense):
        delta = (b - prev) if prev is not None else float("nan")
        ds = f"{delta:+.6f}" if delta == delta else "—"
        print(f"{n:>10d}  {b:>16.10f}  {ds:>14s}")
        prev = b
    rec.append(("H1 dense scan", len(dens) >= 10, f"{len(dens)} checkpoints"))

    # H2 monotone within noise band
    viol = 0
    for i in range(1, len(dens)):
        if b_dense[i] > b_dense[i - 1] + b_dense[i - 1] / math.sqrt(dens[i]):
            viol += 1
    limit = jround(0.05 * (len(dens) - 1))
    rec.append(("H2 monotone", viol <= limit, f"violations {viol}/{len(dens)-1} (limit {limit})"))

    # H3 out-of-sample walk-forward
    med, mx = hc_walkforward_errors(dens, b_dense)
    rec.append(("H3 walk-forward", med < 0.02 and mx < 0.05,
                f"median {med*100:.2f}%, max {mx*100:.2f}%"))

    # H4 stationarity head vs tail
    half = max_N // 2
    b_head = pref[half]
    b_tail = float(d[half:].mean())
    rec.append(("H4 stationarity", b_tail / b_head <= 1.25,
                f"tail/head = {b_tail/b_head:.4f} (limit 1.25)"))

    # H5 bootstrap of b(max_N)
    rng = jrng(0x54E5F0)
    n_boot = clamp(1000, 100, 1000)
    idx = rng.integers(0, max_N, size=(n_boot, max_N))
    boots = d[idx].mean(axis=1)
    lo, hi = np.quantile(boots, 0.025), np.quantile(boots, 0.975)
    width = (hi - lo) / b_final
    margin = cfg.bN_pass_threshold - (b_final + 2.0 * d.std() / math.sqrt(max_N))
    rec.append(("H5 bootstrap CI", width < 0.15 and margin > 0,
                f"CI [{lo:.6f},{hi:.6f}] width {width*100:.2f}%, margin {margin:+.6f}"))

    # H6 outliers
    peak_share = float(np.max(np.abs(d)) / np.abs(d).sum())
    trim_n = clamp(jround(0.01 * max_N), 1, max_N // 4)
    ddesc = np.sort(d)[::-1]
    b_trim = float(ddesc[trim_n:].mean())
    trim_dev = abs(b_trim - b_final) / b_final
    rec.append(("H6 outliers", peak_share < 0.10 and trim_dev < 0.15,
                f"peak share {peak_share*100:.2f}% (k=1), trimmed dev {trim_dev*100:+.2f}%"))

    # H7 Gram sanity
    g = np.array([gram_point(k) for k in range(1, min(50000, max_N) + 1)])
    viol_g = int((np.diff(g) <= 0).sum())
    rec.append(("H7 gram monotone", viol_g == 0, f"violations {viol_g}"))

    ok = hc_verdict_table(cfg, "Test 1", rec)
    log_result(f" Test 1 [HARDCORE pass 2]: {len(rec)} sub-checks, "
               f"{sum(1 for _,o,_ in rec if not o)} failed, b({max_N})={b_final:.4f} "
               f"→ {'PASS' if ok else 'WARN'}")
    return ok, f"hardcore {len(rec)} checks"


def test2_monotonicity(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    pref = CTX.b_pref(zeros)
    n_check = max(min(cfg.n_monotone, len(zeros) // 100), 3)
    Ns = [jround(len(zeros) * i / (n_check + 1)) for i in range(1, n_check + 1)]
    bNs = [pref[N] for N in Ns]
    print("\n" + "═" * 60)
    print(f"TEST 2: {msg(cfg, 'obj1_title')} — Monotonicity Verification")
    print("Check that b(N) is monotonically decreasing")
    print("─" * 60)
    violations = 0
    print(f" {'N':>12} {'b(N)':>16} {'Monotone?':>12}")
    for i, (N, b) in enumerate(zip(Ns, bNs)):
        mono = i == 0 or b <= bNs[i - 1] + 1e-10
        if not mono:
            violations += 1
        print(f" {N:>12d} {b:>16.10f} {'yes' if mono else 'VIOLATION':>12}")
    status = msg(cfg, "pass") if violations == 0 else msg(cfg, "warn")
    log_result(f" Test 2: Monotonicity violations: {violations} / {len(Ns)-1} → {status}")
    return violations == 0, f"violations {violations}/{len(Ns)-1}"


def test2b_monotonicity_hardcore(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    max_N = len(zeros)
    d = hc_bN_series(zeros)
    dens = hc_dense_grid(max_N)
    b_dense = np.array([CTX.b_pref(zeros)[n] for n in dens])
    rec: List[Tuple[str, bool, str]] = []

    print("\n" + "═" * 60)
    print("TEST 2 (secondary, HARDCORE): monotonicity — deep audit")
    print("─" * 60)

    # S1 strict band
    viol = 0
    for i in range(1, len(dens)):
        if b_dense[i] > b_dense[i - 1] + 0.5 * b_dense[i - 1] / math.sqrt(dens[i]):
            viol += 1
    rec.append(("S1 strict band", viol == 0, f"violations {viol}/{len(dens)-1}"))

    # S2 segment means
    n_seg = min(10, max(2, max_N // 50))
    edges = [jround(x) for x in np.linspace(1, max_N, n_seg + 1)]
    means = []
    viol2 = 0
    for s in range(n_seg):
        seg = d[edges[s] - 1:edges[s + 1]]
        m = float(seg.mean())
        means.append(m)
        if s > 0:
            prev, seg_len = means[s - 1], edges[s + 1] - edges[s]
            if m > prev * 1.05 + 0.5 * prev / math.sqrt(seg_len):
                viol2 += 1
    rec.append(("S2 segments", viol2 == 0,
                f"means {means[0]:.6f}→{means[-1]:.6f}, {viol2} increases"))
    print("  segment means:", ", ".join(f"{m:.6f}" for m in means))

    # S3 new lows
    new_lows = 0
    run_min = float("inf")
    for b in b_dense:
        if b < run_min:
            new_lows += 1
            run_min = b
    frac = new_lows / len(b_dense)
    rec.append(("S3 new lows", frac >= 0.60, f"{new_lows}/{len(b_dense)} = {frac*100:.0f}%"))

    # S4 drawdown
    b_final = CTX.b_pref(zeros)[max_N]
    dd = 1.0 - b_final / b_dense[0]
    rec.append(("S4 drawdown", dd >= 0.05, f"1 − b_end/b_start = {dd*100:.1f}%"))

    ok = hc_verdict_table(cfg, "Test 2", rec)
    log_result(f" Test 2 [HARDCORE pass 2]: {len(rec)} sub-checks, "
               f"{sum(1 for _,o,_ in rec if not o)} failed → {'PASS' if ok else 'WARN'}")
    return ok, f"hardcore {len(rec)} checks"


def test3_convergence_rate(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    pref = CTX.b_pref(zeros)
    Ns = []
    n = 50
    while n <= len(zeros):
        Ns.append(n)
        n = jround(n * 1.5)
    if len(Ns) < 5:
        Ns = [jround(len(zeros) * r) for r in np.arange(0.1, 1.01, 0.1)]
    bNs = np.array([pref[N] for N in Ns])
    print("\n" + "═" * 60)
    print(f"TEST 3: {msg(cfg, 'obj1_title')} — Convergence Rate")
    print("Fit b(N) ≈ C · N^(-α) via log-log regression")
    print("─" * 60)
    logN, logb = np.log(np.array(Ns, dtype=float)), np.log(bNs)
    a, b, r2, se, _ = linreg(logN, logb)
    print(f" Fit: log(b(N)) = {b:.4f} · log(N) + {a:.4f}")
    print(f" R² = {r2:.6f} | SE(slope) = {se:.6f}")
    print(f" → b(N) ≈ {math.exp(a):.4f} · N^({b:.4f})")
    print(" The convergence exponent is empirical (not predicted by theory)")
    inv_logN = 1.0 / logN
    a2, b2, r2b, _, _ = linreg(inv_logN, bNs)
    print(f"\n Alternative fit: b(N) ≈ {a2:.4f} + {b2:.4f}/log(N), R² = {r2b:.6f}")
    ok = r2 > 0.9
    status = msg(cfg, "pass") if ok else msg(cfg, "warn")
    print(f"\n Test 3: α = {-b:.4f} (empirical; no expected value), R²={r2:.4f} → {status}")
    log_result(f" Test 3: α = {-b:.4f} (empirical), R²={r2:.4f} → {status}")
    return ok, f"α={-b:.4f} R²={r2:.4f}"


def test3b_rate_hardcore(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    d = hc_bN_series(zeros)
    dens = hc_dense_grid(len(zeros))
    b_dense = np.array([CTX.b_pref(zeros)[n] for n in dens])
    rec: List[Tuple[str, bool, str]] = []
    print("\n" + "═" * 60)
    print("TEST 3 (secondary, HARDCORE): convergence rate — deep fit validation")
    print("─" * 60)
    logN, logb = np.log(np.array(dens, dtype=float)), np.log(b_dense)
    _, bA, r2A, _, _ = linreg(logN, logb)
    rec.append(("R1 power-law R²", r2A > 0.95, f"R² = {r2A:.6f}"))
    inv_logN = 1.0 / logN
    a2, b2, r2B, _, _ = linreg(inv_logN, b_dense)
    best = max(r2A, r2B)
    rec.append(("R2 best-law R²", best > 0.95, f"best R² = {best:.4f}"))
    med, mx = hc_walkforward_errors(dens, b_dense)
    rec.append(("R3 walk-forward", med < 0.02 and mx < 0.05,
                f"median {med*100:.2f}%, max {mx*100:.2f}%"))
    half_i = max(3, len(dens) // 2)
    _, b_lo, _, _, _ = linreg(logN[:half_i], logb[:half_i])
    _, b_hi, _, _, _ = linreg(logN[half_i:], logb[half_i:])
    d_alpha = abs(-b_lo - (-b_hi))
    rec.append(("R4 α stability", d_alpha < 0.2,
                f"α_lower={-b_lo:.4f} vs α_upper={-b_hi:.4f}, |Δα|={d_alpha:.4f}"))
    ok = hc_verdict_table(cfg, "Test 3", rec)
    log_result(f" Test 3 [HARDCORE pass 2]: {len(rec)} sub-checks, "
               f"{sum(1 for _,o,_ in rec if not o)} failed → {'PASS' if ok else 'WARN'}")
    return ok, f"hardcore {len(rec)} checks"


def test4_gue_ks_full(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    sp = normalized_spacings(zeros)
    n = len(sp)
    print("\n" + "═" * 60)
    print(f"TEST 4: {msg(cfg, 'obj2_title')} — KS Test (Full Range)")
    print("H0: normalized spacings follow the GUE (β=2) Wigner surmise")
    print("─" * 60)
    D, p = ks_test(sp)
    W2 = cvm_test(sp)
    crit = 1.358 / math.sqrt(n)
    print(f" n = {n} normalized spacings")
    print(f" KS: D = {D:.6f},  p-value = {p:.6f}")
    print(f" Cramér–von Mises: W² = {W2:.6f}")
    print(f" Critical D (α=0.05): {crit:.6f}")
    rejected = p <= 0.05
    print(f" H0: {'REJECTED' if rejected else 'NOT REJECTED'} — {msg(cfg, 'zeros_note')}")
    status = msg(cfg, "warn") if rejected else msg(cfg, "pass")
    log_result(f" Test 4: D={D:.6f}, p={p:.6f} → {status}")
    return not rejected, f"D={D:.6f} p={p:.6f}"


def test4b_gue_ks_full_hardcore(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    sp = normalized_spacings(zeros)
    n_sp = len(sp)
    rec: List[Tuple[str, bool, str]] = []
    print("\n" + "═" * 60)
    print("TEST 4 (secondary, HARDCORE): GUE KS full range — internal consistency")
    print("─" * 60)
    D, p = ks_test(sp)
    print(f" full-range KS: D = {D:.6f}, p = {p:.6f}")

    # K1 block homogeneity
    n_blk = min(8, max(2, n_sp // 50))
    edges = [jround(x) for x in np.linspace(1, n_sp, n_blk + 1)]
    Ds = []
    for s in range(n_blk):
        Ds.append(ks_test(sp[edges[s] - 1:edges[s + 1]])[0])
    spread = max(Ds) - min(Ds)
    limit = 0.8 / math.sqrt(n_sp / n_blk)
    rec.append(("K1 blocks", spread < limit,
                f"D spread {spread:.6f} (limit {limit:.6f})"))

    # K2 half split
    half = n_sp // 2
    D1 = ks_test(sp[:half])[0]
    D2 = ks_test(sp[half:])[0]
    rec.append(("K2 halves", abs(D1 - D2) < 0.02,
                f"|ΔD| = {abs(D1-D2):.6f} ({D1:.6f} vs {D2:.6f})"))

    # K3 moments
    v_gue = rmt_law_var()
    mean_s, var_s = float(sp.mean()), float(sp.var(ddof=1))
    ok_k3 = abs(mean_s - 1.0) < 0.02 and 0.4 * v_gue < var_s < 1.6 * v_gue
    rec.append(("K3 moments", ok_k3,
                f"mean {mean_s:.4f}, var {var_s:.4f} (law var {v_gue:.4f})"))

    ok = hc_verdict_table(cfg, "Test 4", rec)
    log_result(f" Test 4 [HARDCORE pass 2]: {len(rec)} sub-checks, "
               f"{sum(1 for _,o,_ in rec if not o)} failed → {'PASS' if ok else 'WARN'}")
    return ok, f"hardcore {len(rec)} checks"


def test5_gue_ks_highT(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    print("\n" + "═" * 60)
    print(f"TEST 5: {msg(cfg, 'obj2_title')} — KS Test (High-T Only)")
    print("GUE is asymptotic: rejection should weaken with height")
    print("─" * 60)
    best_p = 0.0
    t_max = float(zeros[-1])
    for t_min in cfg.highT_mins:
        if t_min > t_max:
            continue
        idx = int(np.searchsorted(zeros, t_min))
        hi = zeros[idx:]
        if len(hi) < 100:
            continue
        sp = normalized_spacings(hi)
        D, p = ks_test(sp)
        best_p = max(best_p, p)
        verdict = "KEEP" if p > 0.05 else "REJECT"
        print(f" T > {t_min:>9.0f}: n = {len(sp):>6d}, D = {D:.6f}, p = {p:.6f} → {verdict}")
    ok = best_p > 0.01
    status = msg(cfg, "pass") if ok else msg(cfg, "warn")
    log_result(f" Test 5: best p = {best_p:.6f} → {status}")
    return ok, f"best p={best_p:.6f}"


def test5b_gue_ks_highT_hardcore(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    t_max = float(zeros[-1])
    rec: List[Tuple[str, bool, str]] = []
    print("\n" + "═" * 60)
    print("TEST 5 (secondary, HARDCORE): high-T sweep — denser T grid")
    print("─" * 60)
    ts, rows = [], []
    t = max(50.0, float(zeros[0]))
    while t < t_max / 2:
        ts.append(t)
        t *= 2.5
    p_first = p_last = None
    for t_min in ts:
        idx = int(np.searchsorted(zeros, t_min))
        hi = zeros[idx:]
        if len(hi) < 100:
            continue
        sp = normalized_spacings(hi)
        D, p = ks_test(sp)
        rows.append((t_min, len(sp), D, p))
        p_first = p if p_first is None else p_first
        p_last = p
        print(f" T > {t_min:>9.1f}: n = {len(sp):>6d}, D = {D:.6f}, p = {p:.6f}")
    rec.append(("T2 trend", p_last >= p_first * 0.999,
                f"p {p_first:.3e} → {p_last:.3e} (must not degrade)"))
    top_sp = normalized_spacings(zeros[int(np.searchsorted(zeros, ts[-1])):])
    mean_top = float(top_sp.mean())
    rec.append(("T3 top mean", abs(mean_top - 1.0) < 0.02, f"mean {mean_top:.4f}"))
    ok = hc_verdict_table(cfg, "Test 5", rec)
    log_result(f" Test 5 [HARDCORE pass 2]: {len(rec)} sub-checks, "
               f"{sum(1 for _,o,_ in rec if not o)} failed → {'PASS' if ok else 'WARN'}")
    return ok, f"hardcore {len(rec)} checks"


def test6_chi2_histogram(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    sp = normalized_spacings(zeros)
    print("\n" + "═" * 60)
    print(f"TEST 6: {msg(cfg, 'obj2_title')} — χ² Histogram Test")
    print("χ² GOF of the spacing histogram against the GUE surmise")
    print("─" * 60)
    results = {}
    for nbins in [max(cfg.chi2_bins // 2, 5), max(cfg.chi2_bins, 5), max(cfg.chi2_bins * 2, 5)]:
        chi2, df, p = chi2_gue_test(sp, nbins)
        results[nbins] = p
        print(f" Bins = {nbins:>4d}: χ² = {chi2:.4f}, df = {df}, p = {p:.6f}")
    p_main = results[max(cfg.chi2_bins, 5)]
    ok = p_main > 0.05
    status = msg(cfg, "pass") if ok else msg(cfg, "warn")
    log_result(f" Test 6: χ² p(bins={cfg.chi2_bins}) = {p_main:.6f} → {status}")
    return ok, f"p={p_main:.6f}"


def test6b_chi2_hardcore(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    sp = normalized_spacings(zeros)
    rec: List[Tuple[str, bool, str]] = []
    print("\n" + "═" * 60)
    print("TEST 6 (secondary, HARDCORE): χ² — bin-stability audit")
    print("─" * 60)
    ratios, verdicts = [], []
    for nbins in [max(5, cfg.chi2_bins // d) for d in (1, 2, 4, 8)]:
        chi2, df, p = chi2_gue_test(sp, nbins)
        verdicts.append(p > 0.05)
        ratios.append(chi2 / df)
        print(f" bins {nbins:>4d}: χ²/df = {chi2/df:.4f} → {'KEEP' if p > 0.05 else 'REJECT'}")
    majority = sum(verdicts) > len(verdicts) / 2
    flips = sum(1 for v in verdicts if v != majority)
    rec.append(("C1 bin sweep", flips <= 1, f"{flips} flips vs majority"))
    half = len(sp) // 2
    c1, df1, _ = chi2_gue_test(sp[:half], 150)
    c2, df2, _ = chi2_gue_test(sp[half:], 150)
    dev = abs(c1 / df1 - c2 / df2) / ((c1 / df1 + c2 / df2) / 2)
    rec.append(("C2 halves", dev < 0.50, f"χ²/df {c1/df1:.4f} vs {c2/df2:.4f} ({dev*100:.1f}%)"))
    ok = hc_verdict_table(cfg, "Test 6", rec)
    log_result(f" Test 6 [HARDCORE pass 2]: {len(rec)} sub-checks, "
               f"{sum(1 for _,o,_ in rec if not o)} failed → {'PASS' if ok else 'WARN'}")
    return ok, f"hardcore {len(rec)} checks"


def _doubling_grid(zeros: np.ndarray, start: int) -> List[int]:
    Ns, n = [], start
    while n <= len(zeros):
        Ns.append(n)
        n *= 2
    return Ns


def test7_decay_slope(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    pref = CTX.b_pref(zeros)
    Ns = _doubling_grid(zeros, 500)
    bNs = np.array([pref[N] for N in Ns])
    print("\n" + "═" * 60)
    print(f"TEST 7: {msg(cfg, 'obj3_title')} — Decay Slope")
    print("Fit log(b(N)) vs log(N): expected slope ≈ −0.5")
    print("─" * 60)
    for N, b in zip(Ns, bNs):
        print(f"{N:>10d}  {b:>16.10f}")
    logN, logb = np.log(np.array(Ns, dtype=float)), np.log(bNs)
    a, b, r2, se, _ = linreg(logN, logb)
    ci_lo, ci_hi = b - 1.96 * se, b + 1.96 * se
    print(f"\n Linear fit: log(b(N)) = {b:.4f} · log(N) + {a:.4f}")
    print(f" R² = {r2:.6f} | SE = {se:.6f}")
    print(f" 95% CI for slope: [{ci_lo:.4f}, {ci_hi:.4f}]")
    inv_logN = 1.0 / logN
    a2, b2, r2b, _, _ = linreg(inv_logN, bNs)
    print(f" Alt 1/logN fit: b(N) ≈ {a2:.4f} + {b2:.4f}/log(N), R² = {r2b:.6f}")
    ok = (ci_hi - ci_lo) < 0.1 and r2 > 0.9
    status = msg(cfg, "pass") if ok else msg(cfg, "warn")
    log_result(f" Test 7: Slope={b:.4f} (empirical), 95%CI=[{ci_lo:.4f},{ci_hi:.4f}] → {status}")
    return ok, f"slope {b:.4f} CI [{ci_lo:.4f},{ci_hi:.4f}]"


def test7b_decay_slope_hardcore(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    pref = CTX.b_pref(zeros)
    Ns = _doubling_grid(zeros, 500)
    bNs = np.array([pref[N] for N in Ns])
    logN, logb = np.log(np.array(Ns, dtype=float)), np.log(bNs)
    rec: List[Tuple[str, bool, str]] = []
    print("\n" + "═" * 60)
    print("TEST 7 (secondary, HARDCORE): decay slope — stability + prediction audit")
    print("─" * 60)
    a, b, r2, se, _ = linreg(logN, logb)
    width = 2 * 1.96 * se
    rec.append(("D1 fit", width < 0.1 and r2 > 0.9,
                f"width {width:.4f}, R² = {r2:.4f}"))
    half = len(Ns) // 2
    _, b1, _, _, _ = linreg(logN[:half], logb[:half])
    _, b2, _, _, _ = linreg(logN[half:], logb[half:])
    rec.append(("D2 stability", abs(b1 - b2) < 0.15,
                f"slopes {b1:.4f} vs {b2:.4f}, |Δ| = {abs(b1-b2):.4f}"))
    dens = hc_dense_grid(len(zeros))
    b_dense = np.array([pref[n] for n in dens])
    med, mx = hc_walkforward_errors(dens, b_dense)
    rec.append(("D3 walk-forward", med < 0.02 and mx < 0.05,
                f"median {med*100:.2f}%, max {mx*100:.2f}%"))
    rng = jrng(0x0D04)
    n_boot = clamp(1000, 100, 500)
    slopes = []
    for _ in range(n_boot):
        idx = rng.integers(0, len(Ns), len(Ns))
        if len(set(idx.tolist())) < 3:
            continue
        _, sb, _, _, _ = linreg(logN[idx], logb[idx])
        slopes.append(sb)
    blo, bhi = np.quantile(slopes, 0.025), np.quantile(slopes, 0.975)
    rec.append(("D4 bootstrap", blo <= b <= bhi,
                f"CI [{blo:.4f},{bhi:.4f}] contains {b:.4f}: {blo <= b <= bhi}"))
    ok = hc_verdict_table(cfg, "Test 7", rec)
    log_result(f" Test 7 [HARDCORE pass 2]: {len(rec)} sub-checks, "
               f"{sum(1 for _,o,_ in rec if not o)} failed → {'PASS' if ok else 'WARN'}")
    return ok, f"hardcore {len(rec)} checks"


def test8_residual_analysis(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    pref = CTX.b_pref(zeros)
    Ns = _doubling_grid(zeros, 50)
    bNs = np.array([pref[N] for N in Ns])
    print("\n" + "═" * 60)
    print(f"TEST 8: {msg(cfg, 'obj3_title')} — Residual Analysis")
    print("Check if power-law fit residuals are random or systematic")
    print("─" * 60)
    logN, logb = np.log(np.array(Ns, dtype=float)), np.log(bNs)
    a, b, r2, se, residuals = linreg(logN, logb)
    for N, r in zip(Ns, residuals):
        print(f" N = {N:>8d}: residual = {r:+.6f}")
    signs = [1 if r > 0 else -1 for r in residuals]
    runs = 1 + sum(1 for i in range(1, len(signs)) if signs[i] != signs[i - 1])
    n_pos = sum(1 for s in signs if s > 0)
    n_neg = len(signs) - n_pos
    expected = 1.0 + 2.0 * n_pos * n_neg / len(signs)
    lag1 = float(np.corrcoef(residuals[:-1], residuals[1:])[0, 1])
    systematic = abs(runs - expected) > 2.0 * math.sqrt(expected)
    print(f"\n Runs test: {runs} runs (expected {expected:.1f} for random)")
    print(f" Lag-1 autocorrelation: {lag1:+.4f}")
    ok = not systematic
    status = msg(cfg, "pass") if ok else msg(cfg, "warn")
    log_result(f" Test 8: Runs={runs} (exp={expected:.1f}) → {status}")
    return ok, f"runs {runs} (exp {expected:.1f})"


def test8b_residuals_hardcore(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    pref = CTX.b_pref(zeros)
    Ns = _doubling_grid(zeros, 50)
    bNs = np.array([pref[N] for N in Ns])
    logN, logb = np.log(np.array(Ns, dtype=float)), np.log(bNs)
    _, _, _, _, residuals = linreg(logN, logb)
    n_r = len(residuals)
    signs = [1 if r > 0 else -1 for r in residuals]
    runs = 1 + sum(1 for i in range(1, n_r) if signs[i] != signs[i - 1])
    n_pos = sum(1 for s in signs if s > 0)
    expected = 1.0 + 2.0 * n_pos * (n_r - n_pos) / n_r
    rec: List[Tuple[str, bool, str]] = []
    print("\n" + "═" * 60)
    print("TEST 8 (secondary, HARDCORE): residuals — structure audit")
    print("─" * 60)
    rec.append(("E1 runs", abs(runs - expected) <= 2.5 * math.sqrt(expected),
                f"runs {runs} vs {expected:.1f} ± {2.5*math.sqrt(expected):.1f}"))
    r1 = float(np.corrcoef(residuals[:-1], residuals[1:])[0, 1])
    r2c = float(np.corrcoef(residuals[:-2], residuals[2:])[0, 1])
    rec.append(("E2 autocorr", abs(r1) < 0.95 and abs(r2c) < 0.95,
                f"lag1 {r1:+.4f}, lag2 {r2c:+.4f}"))
    dens = hc_dense_grid(len(zeros))
    b_dense = np.array([pref[n] for n in dens])
    _, _, _, _, res_d = linreg(np.log(np.array(dens, dtype=float)), np.log(b_dense))
    h = len(res_d) // 2
    sd1, sd2 = float(res_d[:h].std(ddof=1)), float(res_d[h:].std(ddof=1))
    ratio = sd1 / sd2
    rec.append(("E3 scale", 0.4 < ratio < 2.5, f"sd ratio {ratio:.3f}"))
    rec.append(("E4 balance", n_r // 4 <= n_pos <= 3 * n_r // 4,
                f"{n_pos}+/ {n_r-n_pos}-"))
    ok = hc_verdict_table(cfg, "Test 8", rec)
    log_result(f" Test 8 [HARDCORE pass 2]: {len(rec)} sub-checks, "
               f"{sum(1 for _,o,_ in rec if not o)} failed → {'PASS' if ok else 'WARN'}")
    return ok, f"hardcore {len(rec)} checks"


def test9_bootstrap_slope(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    pref = CTX.b_pref(zeros)
    Ns = _doubling_grid(zeros, 50)
    bNs = np.array([pref[N] for N in Ns])
    logN, logb = np.log(np.array(Ns, dtype=float)), np.log(bNs)
    n_g = len(Ns)
    print("\n" + "═" * 60)
    print(f"TEST 9: {msg(cfg, 'obj3_title')} — Bootstrap Confidence Interval")
    print(f"Resample the {n_g}-point rate-law fit {cfg.n_bootstrap} times")
    print("─" * 60)
    rng = jrng(42)
    slopes = []
    for _ in range(cfg.n_bootstrap):
        idx = rng.integers(0, n_g, n_g)
        if len(set(idx.tolist())) < 3:
            continue
        _, sb, _, _, _ = linreg(logN[idx], logb[idx])
        slopes.append(sb)
    slopes = np.array(slopes)
    med = float(np.median(slopes))
    blo, bhi = np.quantile(slopes, 0.025), np.quantile(slopes, 0.975)
    contains = blo <= -0.5 <= bhi
    print(f" Bootstrap slope: median = {med:.4f}")
    print(f" 95% CI: [{blo:.4f}, {bhi:.4f}]")
    print(f" Contains −0.5 (O(1/√N))? {'YES' if contains else 'NO'}")
    ok = (bhi - blo) < 0.1
    status = msg(cfg, "pass") if ok else msg(cfg, "warn")
    log_result(f" Test 9: Bootstrap slope={med:.4f} (empirical), "
               f"95%CI=[{blo:.4f},{bhi:.4f}] → {status}")
    return ok, f"median {med:.4f} CI [{blo:.4f},{bhi:.4f}]"


def test9b_bootstrap_hardcore(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    pref = CTX.b_pref(zeros)
    Ns = _doubling_grid(zeros, 50)
    bNs = np.array([pref[N] for N in Ns])
    logN, logb = np.log(np.array(Ns, dtype=float)), np.log(bNs)
    n_g = len(Ns)
    rec: List[Tuple[str, bool, str]] = []
    print("\n" + "═" * 60)
    print("TEST 9 (secondary, HARDCORE): bootstrap — reproducibility audit")
    print("─" * 60)

    def boot(seed: int, n_boot: int, pool: int) -> Tuple[float, float, float]:
        rng = jrng(seed)
        slopes = []
        for _ in range(n_boot):
            idx = rng.integers(0, pool, pool)
            if len(set(idx.tolist())) < 3:
                continue
            _, sb, _, _, _ = linreg(logN[idx], logb[idx])
            slopes.append(sb)
        s = np.array(slopes)
        return float(np.median(s)), float(np.quantile(s, 0.025)), float(np.quantile(s, 0.975))

    n_boot = clamp(1000, 100, 500)
    m1, l1, h1 = boot(0x0B01, n_boot, n_g)
    rec.append(("B1 width", (h1 - l1) < 0.1, f"width {h1-l1:.4f}, median {m1:.4f}"))
    m2, l2, h2 = boot(0x0B02, n_boot, n_g)
    union_lo, union_hi = min(l1, l2), max(h1, h2)
    overlap = (min(h1, h2) - max(l1, l2)) / (union_hi - union_lo) if union_hi > union_lo else 0.0
    rec.append(("B2 seed stability", abs(m1 - m2) < 0.02 and overlap >= 0.60,
                f"|Δmed| = {abs(m1-m2):.4f}, overlap {overlap*100:.0f}%"))
    # jackknife
    loo = []
    for i in range(n_g):
        mask = np.ones(n_g, dtype=bool)
        mask[i] = False
        _, sb, _, _, _ = linreg(logN[mask], logb[mask])
        loo.append(sb)
    loo_min, loo_max = min(loo), max(loo)
    inside = loo_min >= l1 - 0.02 and loo_max <= h1 + 0.02
    rec.append(("B3 jackknife", inside,
                f"LOO [{loo_min:.4f},{loo_max:.4f}] inside CI ± 0.02: {inside}"))
    half_i = max(3, n_g // 2)
    mh, lh, hh = boot(0x0B04, n_boot, half_i)
    rec.append(("B4 half-grid", abs(mh - m1) < 0.05,
                f"half median {mh:.4f} vs full {m1:.4f}, |Δ| = {abs(mh-m1):.4f}"))
    ok = hc_verdict_table(cfg, "Test 9", rec)
    log_result(f" Test 9 [HARDCORE pass 2]: {len(rec)} sub-checks, "
               f"{sum(1 for _,o,_ in rec if not o)} failed → {'PASS' if ok else 'WARN'}")
    return ok, f"hardcore {len(rec)} checks"


def test10_cross_validation(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    N = len(zeros)
    d = hc_bN_series(zeros)
    b_full = float(d.mean())
    half = N // 2
    b_first = float(d[:half].mean())
    b_second = float(d[half:].mean())
    b_even = float(d[::2].mean())
    rng = jrng(123)
    perm = rng.permutation(N)
    sub_size = jround(cfg.stability_fraction * N)
    idx = np.sort(perm[:sub_size])
    b_frac = float(d[idx].mean())
    devs = {
        "first half": abs(b_first - b_full) / b_full,
        "second half (offset)": abs(b_second - b_full) / b_full,
        "even subset": abs(b_even - b_full) / b_full,
        f"{cfg.stability_fraction:.0%} random": abs(b_frac - b_full) / b_full,
    }
    max_dev = max(devs.values())
    print("\n" + "═" * 60)
    print("TEST 10: Cross-Validation Stability Check")
    print("b(N) must be stable across disjoint sub-samples (offset discipline)")
    print("─" * 60)
    print(f" b(full) = {b_full:.10f}")
    for name, b in (("first half", b_first), ("second half (offset)", b_second),
                    ("even subset", b_even),
                    (f"{cfg.stability_fraction:.0%} random", b_frac)):
        print(f" {name:<22}: b = {b:.10f}  dev = {devs[name]*100:.2f}%")
    ok = max_dev < cfg.stability_threshold
    status = msg(cfg, "pass") if ok else msg(cfg, "warn")
    worst = max(devs, key=devs.get)
    log_result(f" Test 10: Max deviation={max_dev*100:.1f}% ({worst}) → {status}")
    return ok, f"max dev {max_dev*100:.1f}% ({worst})"


def test10b_crossval_hardcore(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    N = len(zeros)
    d = hc_bN_series(zeros)
    b_full = float(d.mean())
    rec: List[Tuple[str, bool, str]] = []
    print("\n" + "═" * 60)
    print("TEST 10 (secondary, HARDCORE): cross-validation — offset-discipline tripwire")
    print("─" * 60)
    # V1 deciles
    n_seg = min(10, max(2, N // 50))
    edges = [jround(x) for x in np.linspace(1, N, n_seg + 1)]
    viol = 0
    prev_m = None
    for s in range(n_seg):
        m = float(d[edges[s] - 1:edges[s + 1]].mean())
        if prev_m is not None and m > prev_m * 1.05 + 0.5 * prev_m / math.sqrt(edges[s + 1] - edges[s]):
            viol += 1
        prev_m = m
    rec.append(("V1 deciles", viol == 0, f"{viol} increases"))

    # V2 f-convergence
    rng = jrng(0x0A02)
    devs = []
    for f in (0.3, 0.5, 0.7, 0.9):
        per = []
        for _ in range(5):
            sub_n = jround(f * N)
            idx = np.sort(rng.permutation(N)[:sub_n])
            per.append(abs(float(d[idx].mean()) - b_full) / b_full)
        devs.append(float(np.mean(per)))
    rec.append(("V2 f-convergence", devs[-1] < devs[0] and devs[-1] < 0.10,
                f"dev(f=0.3) = {devs[0]:.4f} → dev(f=0.9) = {devs[-1]:.4f}"))

    # V3 offset tripwire
    half = N // 2
    b_right = float(d[half:].mean())
    b_wrong = float(np.mean([abs(zeros[j] - gram_point(j - half + 1))
                             for j in range(half, N)]))
    trip = (b_wrong - b_right) / b_right
    rec.append(("V3 tripwire", trip > 0.05,
                f"wrong-offset b = {b_wrong:.4f} vs right {b_right:.4f} ({trip*100:.0f}% worse)"))

    # V4 even-odd
    b_even = float(d[::2].mean())
    dev = abs(b_even - b_full) / b_full
    rec.append(("V4 even-odd", dev < 0.10, f"dev {dev*100:.2f}%"))
    ok = hc_verdict_table(cfg, "Test 10", rec)
    log_result(f" Test 10 [HARDCORE pass 2]: {len(rec)} sub-checks, "
               f"{sum(1 for _,o,_ in rec if not o)} failed → {'PASS' if ok else 'WARN'}")
    return ok, f"hardcore {len(rec)} checks"
