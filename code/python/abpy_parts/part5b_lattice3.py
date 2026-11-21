

# ═══════════════════════════════════════════════════════════════════════════
# 14. TESTS 32–33 — ⟨r⟩ bootstrap and L-scaling
# ═══════════════════════════════════════════════════════════════════════════

def _rmean_row(cfg: Config, Nx: int, Ny: int, Nv: int, q: float, W: float,
               n_real: int, rng: np.random.Generator, seed_base: int) -> Tuple[float, float, List[float]]:
    torus = abs(q * (2 - Nx) - round(q * (2 - Nx))) < 1e-9
    bc = "torus" if torus else "open"
    r_vals = []
    for k in range(1, n_real + 1):
        vortices = random_vortex_configuration(Nv, Nx, Ny, q, rng)
        H = build_ab_cloud_hamiltonian(ABCloudConfig(
            Nx, Ny, vortices, cfg.ab_alpha_test16, cfg.ab_t, bc, W, seed_base + k))
        ev = ab_eigvals(H)
        del H
        r, _ = mean_adjacent_spacing_ratio(central_band_eigs(ev, 0.6))
        r_vals.append(r)
    r_m = float(np.mean(r_vals))
    r_se = float(np.std(r_vals, ddof=1) / math.sqrt(len(r_vals))) if len(r_vals) > 1 else 0.0
    return r_m, r_se, r_vals


def test32_200_realization_rmean(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    Nx, Ny = cfg.ab_nx, cfg.ab_ny
    N = Nx * Ny
    n_real = max(3, cfg.ab_n_realizations)
    q1 = cfg.resolve_q_magnitude()
    W1 = cfg.w_eff()
    Nv1 = cfg.resolve_vortex_count()
    rng = jrng(cfg.ab_seed)   # shared stream across rows and realizations
    print("\n" + "═" * 60)
    print(f"TEST 32: Multi-realization ⟨r⟩ bootstrap ({n_real} realizations, {Nx}×{Ny})")
    print("─" * 60)
    r1, se1, vals1 = _rmean_row(cfg, Nx, Ny, Nv1, q1, W1, n_real, rng, cfg.ab_seed)
    print(f" q = {q1}: ⟨r⟩ = {r1:.4f} ± {se1:.4f}  (per-real: "
          + ", ".join(f"{v:.4f}" for v in vals1) + ")")
    if abs(q1 - round(q1)) < 1e-9:
        q2 = 0.3
        W2 = min(cfg.ab_W_cmp, cfg.ab_W_max)
        Nv2 = jround(cfg.ab_nv_cmp * N / 5184)
        r2_, se2, vals2 = _rmean_row(cfg, Nx, Ny, Nv2, q2, W2, n_real, rng, cfg.ab_seed)
        print(f" q = {q2}: ⟨r⟩ = {r2_:.4f} ± {se2:.4f} (W={W2}, Nv={Nv2})  → "
              f"nearest class: {classify_universality_class(r2_)}")
    dev = abs(r1 - 0.5992)
    if dev < 0.022:
        status, ok = msg(cfg, "pass"), True
    elif dev < 0.05:
        status, ok = msg(cfg, "warn"), True
    else:
        status, ok = msg(cfg, "fail"), False
    log_result(f" Test 32: ⟨r⟩={r1:.4f}±{se1:.4f} (q={q1}, n={n_real}) vs GUE 0.5992 → {status}")
    return ok, f"⟨r⟩={r1:.4f}±{se1:.4f}"


def test32b_rmean_hardcore(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    Nx, Ny = cfg.ab_nx, cfg.ab_ny
    n_real = max(cfg.ab_n_realizations, cfg.ab_hc_nreal)
    Nv_sec = cfg.resolve_vortex_count_secondary()
    q1 = cfg.resolve_q_magnitude()
    W1 = cfg.w_eff()
    rng = jrng(cfg.ab_seed)
    rec = []
    print("\n" + "═" * 60)
    print(f"TEST 32b [HARDCORE pass 2]: ⟨r⟩ bootstrap — {n_real} realizations on {Nx}×{Ny}")
    print("─" * 60)
    r1, se1, vals1 = _rmean_row(cfg, Nx, Ny, Nv_sec, q1, W1, n_real, rng, cfg.ab_seed)
    print(f" q = {q1}: ⟨r⟩ = {r1:.4f} ± {se1:.4f}  (per-real: "
          + ", ".join(f"{v:.4f}" for v in vals1) + ")")
    q2 = 0.3
    W2 = min(cfg.ab_W_cmp, cfg.ab_W_max)
    Nv2 = jround(25 * Nx * Ny / 900)
    r2_, se2, vals2 = _rmean_row(cfg, Nx, Ny, Nv2, q2, W2, n_real, rng, cfg.ab_seed)
    print(f" q = {q2}: ⟨r⟩ = {r2_:.4f} ± {se2:.4f} (W={W2}, Nv={Nv2})")
    for label, r_m, vals, qb in ((f"q={q1}", r1, vals1, q1), (f"q={q2}", r2_, vals2, q2)):
        brng = jrng(cfg.ab_seed + 7717 + jround(1000 * qb))
        boots = [float(np.mean(brng.choice(vals, len(vals)))) for _ in range(10000)]
        blo, bhi = np.quantile(boots, 0.025), np.quantile(boots, 0.975)
        scatter = float(np.std(vals, ddof=1))
        n_above = sum(1 for v in vals if v > 0.5992)
        rec.append((f"{label} scatter ≤ 0.022", scatter <= 0.022,
                    f"σ = {scatter:.4f}, CI [{blo:.4f},{bhi:.4f}], {n_above}/{len(vals)} above GUE"))
    rec.append(("q=1.0 band", abs(r1 - 0.5992) < 0.022, f"|Δ| = {abs(r1-0.5992):.4f}"))
    ok = hc_verdict_table(cfg, "Test 32", rec)
    log_result(f" Test 32b [HARDCORE pass 2]: {len(rec)} sub-checks → "
               f"{'PASS' if ok else 'WARN'}")
    return ok, f"hardcore ⟨r⟩={r1:.4f}"


def test33_lattice_L_scaling(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    L_grid = [l for l in [10, 20, 30, 50, 80, 112]
              if l * l <= _max_sites(cfg)]
    q_rows = [(cfg.resolve_q_magnitude(), cfg.w_eff())]
    q0 = cfg.resolve_q_magnitude()
    if abs(q0 - round(q0)) < 1e-9:
        q_rows.append((0.3, min(cfg.ab_W_cmp, cfg.ab_W_max)))
    n_avg = min(cfg.ab_n_realizations, 5)
    rng = jrng(cfg.ab_seed)  # continuous stream across all rows
    print("\n" + "═" * 60)
    print(f"TEST 33: L-Scaling for AB-cloud Lattice (⟨r⟩ vs L, {n_avg} realizations/L)")
    print(f" L grid {L_grid}; Nv(L) = round(25·L²/900) even")
    print("─" * 60)
    results = {}
    for q, W in q_rows:
        r_means, r_ses = [], []
        for L in L_grid:
            Nv = jround(25 * L * L / 900)
            if Nv % 2 == 1:
                Nv += 1
            torus = abs(q * (2 - L) - round(q * (2 - L))) < 1e-9
            bc = "torus" if torus else "open"
            r_vals = []
            for k in range(1, n_avg + 1):
                vortices = random_vortex_configuration(Nv, L, L, q, rng)
                H = build_ab_cloud_hamiltonian(ABCloudConfig(
                    L, L, vortices, 0.5, cfg.ab_t, bc, W, cfg.ab_seed + 34 + k))
                ev = ab_eigvals(H)
                del H
                r, _ = mean_adjacent_spacing_ratio(central_band_eigs(ev, 0.6))
                r_vals.append(r)
            r_means.append(float(np.mean(r_vals)))
            r_ses.append(float(np.std(r_vals, ddof=1) / math.sqrt(n_avg)) if n_avg > 1 else 0.0)
            print(f" q={q} L = {L:>3} (Nv={Nv:>3}): ⟨r⟩ = {r_means[-1]:.4f} ± {r_ses[-1]:.4f}")
        results[q] = (r_means, r_ses)
    r_frac = results[0.3][0]
    mono = all(r_frac[i] <= r_frac[i + 1] + 0.05 for i in range(len(r_frac) - 1))
    final_close = abs(r_frac[-1] - 0.595) < 0.05
    ok = mono and final_close
    status = msg(cfg, "pass") if ok else (msg(cfg, "warn") if mono else msg(cfg, "fail"))
    log_result(f" Test 33: L-scaling {', '.join(f'{r:.3f}' for r in r_frac)} → {status}")
    return ok, f"trend {r_frac[0]:.3f}→{r_frac[-1]:.3f}"


def _max_sites(cfg: Config) -> int:
    """RAM-guard ceiling: ~3 dense copies of an L² complex matrix ≤ 1.4 GB."""
    return int(math.sqrt(1.4e9 / (16.0 * 3.0)))


def test33b_lscaling_hardcore(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    L_grid = [l for l in [50, 80] if l * l <= _max_sites(cfg)]
    q = 0.3
    n_avg = max(cfg.ab_n_realizations, cfg.ab_hc_nreal)
    rng = jrng(cfg.ab_seed)
    r_means, r_ses = [], []
    print("\n" + "═" * 60)
    print(f"TEST 33b [HARDCORE pass 2]: L-scaling plateau (q=0.3, {n_avg} real/L, L ≥ 50)")
    print("─" * 60)
    for L in L_grid:
        Nv = jround(25 * L * L / 900)
        if Nv % 2 == 1:
            Nv += 1
        r_vals = []
        for k in range(1, n_avg + 1):
            vortices = random_vortex_configuration(Nv, L, L, q, rng)
            H = build_ab_cloud_hamiltonian(ABCloudConfig(
                L, L, vortices, 0.5, cfg.ab_t, "open", min(cfg.ab_W_cmp, cfg.ab_W_max),
                cfg.ab_seed + 34 + k))
            ev = ab_eigvals(H)
            del H
            r, _ = mean_adjacent_spacing_ratio(central_band_eigs(ev, 0.6))
            r_vals.append(r)
        r_means.append(float(np.mean(r_vals)))
        r_ses.append(float(np.std(r_vals, ddof=1) / math.sqrt(n_avg)) if n_avg > 1 else 0.0)
        print(f" L = {L:>3} (Nv={Nv}): ⟨r⟩ = {r_means[-1]:.4f} ± {r_ses[-1]:.4f}")
    se_floor = 0.022 / math.sqrt(len(r_means))
    wts = [1.0 / max(abs(se), se_floor) ** 2 for se in r_ses]
    w_mean = sum(w * r for w, r in zip(wts, r_means)) / sum(wts)
    chi2 = sum(w * (r - 0.5992) ** 2 for w, r in zip(wts, r_means))
    dof = len(r_means)
    rec = [("plateau in ±0.022 band", abs(w_mean - 0.5992) < 0.022,
            f"weighted ⟨r⟩ = {w_mean:.4f} vs 0.5992 (|Δ| = {abs(w_mean-0.5992):.4f})"),
           ("χ²/dof ≤ 2", dof > 0 and chi2 / dof <= 2.0,
            f"χ² = {chi2:.2f}, dof = {dof}")]
    ok = hc_verdict_table(cfg, "Test 33", rec)
    log_result(f" Test 33b (hardcore): plateau ⟨r⟩={w_mean:.4f}, χ²/dof={chi2/dof:.2f} → "
               f"{'PASS' if ok else 'WARN'}")
    return ok, f"hardcore plateau {w_mean:.4f}"


# ═══════════════════════════════════════════════════════════════════════════
# 15. TESTS 34–36 — direct AB vs ζ, K(t) form factor, byte robustness
# ═══════════════════════════════════════════════════════════════════════════

def _ks_asym_p(n_eff: float, D: float, kmax: int = 200) -> float:
    lam = (n_eff + 0.12 + 0.11 / n_eff) * D
    s, sign = 0.0, 1.0
    for k in range(1, kmax + 1):
        term = sign * math.exp(-2.0 * k * k * lam * lam)
        s += term
        sign = -sign
        if abs(term) < 1e-18:
            break
    return clamp(2.0 * s, 0.0, 1.0)


def _pair_corr_R2(positions: np.ndarray, s_max: float, ds: float) -> np.ndarray:
    """Montgomery pair correlation R₂(s) of an unfolded staircase."""
    nbins = int(round(s_max / ds))
    hist = np.zeros(nbins)
    n = len(positions)
    M = 0
    for i in range(n):
        for j in range(i + 1, n):
            d = positions[j] - positions[i]
            if d >= s_max:
                break
            b = int(d / ds)
            if 0 <= b < nbins:
                hist[b] += 1.0
            M += 1
    return hist / (M * ds) if M > 0 else hist


def test34_direct_ab_vs_zeta(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    Nx, Ny = cfg.ab_nx, cfg.ab_ny
    n_real = max(3, cfg.ab_n_realizations)
    Nv = cfg.resolve_vortex_count()
    q = cfg.resolve_q_magnitude()
    W = cfg.w_eff()
    rng = jrng(cfg.ab_seed + 119)
    pool = []
    print("\n" + "═" * 60)
    print("TEST 34: DIRECT AB-cloud vs ζ (Hilbert-Pólya direct comparison)")
    print(f" {n_real} realizations {Nx}×{Ny}; KS + R₂(s) vs the ζ spacings")
    print("─" * 60)
    for ireal in range(1, n_real + 1):
        vortices = random_vortex_configuration(Nv, Nx, Ny, q, rng)
        H = build_ab_cloud_hamiltonian(ABCloudConfig(
            Nx, Ny, vortices, cfg.ab_alpha_test16, cfg.ab_t, cfg.ab_lattice, W,
            cfg.ab_seed + 119 + ireal))
        ev = ab_eigvals(H)
        del H
        n = len(ev)
        half = int(n * cfg.ab_center_fraction) // 2
        bulk = ev[n // 2 - half: n // 2 + half]
        sp = np.diff(bulk)
        un = unfold_local(sp, cfg.ab_unfold_window)
        if len(un) > 50:
            pool.append(un)
    sp_ab = np.concatenate(pool)
    sp_ab = sp_ab / sp_ab.mean()
    sp_z = normalized_spacings(zeros)
    sp_z = sp_z[(sp_z > 0) & (sp_z < 10)]
    sp_z = sp_z / sp_z.mean()
    # 2-sample KS (asymmetric asymptotic)
    xs = np.sort(sp_ab)
    ys = np.sort(sp_z)
    nx_, ny_ = len(xs), len(ys)
    allv = np.concatenate((xs, ys))
    cdfx = np.searchsorted(xs, allv, side="right") / nx_
    cdfy = np.searchsorted(ys, allv, side="right") / ny_
    D = float(np.max(np.abs(cdfx - cdfy)))
    n_eff = math.sqrt(nx_ * ny_ / (nx_ + ny_))
    p = _ks_asym_p(n_eff, D)
    # R₂ pair correlations
    pos_ab = np.concatenate(([0.0], np.cumsum(sp_ab)))
    pos_z = np.concatenate(([0.0], np.cumsum(sp_z)))
    R2_ab = _pair_corr_R2(pos_ab, 3.0, 0.1)
    R2_z = _pair_corr_R2(pos_z, 3.0, 0.1)
    centers = (np.arange(len(R2_ab)) + 0.5) * 0.1
    R2_gue = 1.0 - (np.sin(math.pi * centers) / (math.pi * centers)) ** 2
    mean_diff = float(np.mean(np.abs(R2_ab - R2_z)))
    max_diff = float(np.max(np.abs(R2_ab - R2_z)))
    d_gue = float(np.mean(np.abs(R2_ab - R2_gue)))
    d_pois = float(np.mean(np.abs(R2_ab - 1.0)))
    # estimator self-calibration on a synthetic GUE
    ev_cal = gue_matrix_eigenvalues(2000, 20260916)
    un_cal = unfold_gue_eigenvalues(ev_cal)
    sp_cal = np.diff(un_cal)
    sp_cal = sp_cal[(sp_cal > 0) & (sp_cal < 10)]
    sp_cal = sp_cal / sp_cal.mean()
    pos_cal = np.concatenate(([0.0], np.cumsum(sp_cal)))
    R2_cal = _pair_corr_R2(pos_cal, 3.0, 0.1)
    cal_err = float(np.mean(np.abs(R2_cal - R2_gue)))
    calib_ok = cal_err < 0.15
    ks_pass = (p > 0.01) or (D < 0.10)
    r2_pass = mean_diff < 0.10 and calib_ok
    gue_closer = d_gue < d_pois
    print(f" AB spacings: {len(sp_ab)} ({n_real} realizations); ζ spacings: {len(sp_z)}")
    print(f" 2-sample KS: D = {D:.4f}, p = {p:.3e}  → "
          f"{'PASS' if ks_pass else 'FAIL'} (p>0.01 or D<0.10)")
    print(f" R₂: ⟨|ΔR₂|⟩ = {mean_diff:.4f} (max {max_diff:.4f}), calib err {cal_err:.4f} → "
          f"{'PASS' if r2_pass else 'FAIL'}")
    print(f" d_GUE = {d_gue:.4f} vs d_Pois = {d_pois:.4f} → GUE closer: {gue_closer}")
    ok = ks_pass and r2_pass and gue_closer
    n_ok = sum(1 for x in (ks_pass, r2_pass, gue_closer) if x)
    status = msg(cfg, "pass") if n_ok == 3 else (msg(cfg, "warn") if n_ok > 0 else msg(cfg, "fail"))
    log_result(f" Test 34: KS p={p:.1e}, ⟨|ΔR₂|⟩={mean_diff:.4f}, d_GUE={d_gue:.3f} → {status}")
    return ok, f"D={D:.4f}, ⟨|ΔR₂|⟩={mean_diff:.4f}"


def test34b_ab_vs_zeta_hardcore(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    Nx, Ny = cfg.ab_nx, cfg.ab_ny
    n_hc = max(cfg.ab_n_realizations, cfg.ab_hc_nreal)
    Nv = cfg.resolve_vortex_count_secondary()
    q = cfg.resolve_q_magnitude()
    W = cfg.w_eff()
    rng = jrng(cfg.ab_seed + 3500)
    Ds = []
    pool = []
    print("\n" + "═" * 60)
    print(f"TEST 34b [HARDCORE pass 2]: AB vs ζ — {n_hc} realizations on {Nx}×{Ny}")
    print("─" * 60)
    sp_z = normalized_spacings(zeros)
    sp_z = sp_z[(sp_z > 0) & (sp_z < 10)]
    sp_z = sp_z / sp_z.mean()
    for k in range(1, n_hc + 1):
        vortices = random_vortex_configuration(Nv, Nx, Ny, q, rng)
        H = build_ab_cloud_hamiltonian(ABCloudConfig(
            Nx, Ny, vortices, cfg.ab_alpha_test16, cfg.ab_t, cfg.ab_lattice, W,
            cfg.ab_seed + 3500 + k))
        ev = ab_eigvals(H)
        del H
        n = len(ev)
        half = int(n * cfg.ab_center_fraction) // 2
        bulk = ev[n // 2 - half: n // 2 + half]
        un = unfold_local(np.diff(bulk), cfg.ab_unfold_window)
        if len(un) > 50:
            pool.append(un)
            xs = np.sort(un)
            ys = np.sort(sp_z)
            nx_, ny_ = len(xs), len(ys)
            allv = np.concatenate((xs, ys))
            cdfx = np.searchsorted(xs, allv, side="right") / nx_
            cdfy = np.searchsorted(ys, allv, side="right") / ny_
            Ds.append(float(np.max(np.abs(cdfx - cdfy))))
        print(f"  realization {k}: D_k = {Ds[-1]:.4f}")
    sp_ab = np.concatenate(pool)
    sp_ab = sp_ab / sp_ab.mean()
    xs, ys = np.sort(sp_ab), np.sort(sp_z)
    nx_, ny_ = len(xs), len(ys)
    allv = np.concatenate((xs, ys))
    cdfx = np.searchsorted(xs, allv, side="right") / nx_
    cdfy = np.searchsorted(ys, allv, side="right") / ny_
    D = float(np.max(np.abs(cdfx - cdfy)))
    n_eff = math.sqrt(nx_ * ny_ / (nx_ + ny_))
    p = _ks_asym_p(n_eff, D)
    R2_ab = _pair_corr_R2(np.concatenate(([0.0], np.cumsum(sp_ab))), 4.0, 0.05)
    R2_z = _pair_corr_R2(np.concatenate(([0.0], np.cumsum(sp_z))), 4.0, 0.05)
    mean_diff = float(np.mean(np.abs(R2_ab - R2_z)))
    d_spread = max(Ds) - min(Ds)
    rec = [("per-real D spread < 0.10", d_spread < 0.10,
            f"D_k {min(Ds):.4f}…{max(Ds):.4f} (median {float(np.median(Ds)):.4f})"),
           ("pooled KS", (p > 0.01) or (D < 0.10), f"D = {D:.4f}, p = {p:.1e}"),
           ("R₂ contract", mean_diff < 0.10, f"⟨|ΔR₂|⟩ = {mean_diff:.4f} (ds=0.05)")]
    ok = hc_verdict_table(cfg, "Test 34", rec)
    log_result(f" Test 34b: D={D:.4f}, ⟨|ΔR₂|⟩={mean_diff:.4f} → {'PASS' if ok else 'WARN'}")
    return ok, f"hardcore D={D:.4f}"


def compute_K_form_factor(eigs: np.ndarray, t_values: List[float],
                          smooth_window: int = 3, eigs_per_seed: int = 0) -> np.ndarray:
    """K(t) = ⟨|Σ e^{2πi t u_k}|²/n⟩ over blocks of unfolded levels."""
    eigs = np.sort(np.asarray(eigs, dtype=float))
    n = len(eigs)
    if eigs_per_seed <= 0:
        n_blocks = max(1, n // 5000) if n > 5000 else 1
        eps = n // n_blocks
    else:
        eps = eigs_per_seed
    blocks = [eigs[i:i + eps] for i in range(0, n - eps + 1, eps)]
    K = np.zeros(len(t_values))
    nb = 0
    for blk in blocks:
        nb += 1
        sp = np.diff(blk)
        # robust unfolding: unit-mean kept spacings → unit-density positions
        sp_keep = sp[(sp > 0)]
        if len(sp_keep) < 10:
            continue
        sp_keep = sp_keep / sp_keep.mean()
        u = np.concatenate(([0.0], np.cumsum(sp_keep)))
        u = u / (u[-1] / len(u))
        for ti, t in enumerate(t_values):
            K[ti] += max(0.0, abs(np.exp(2j * math.pi * t * u).sum()) ** 2 / len(u))
    K /= max(nb, 1)
    # moving average for t ≥ 0.5 only (preserve the ramp)
    s_w = smooth_window
    if s_w > 0:
        Ks = K.copy()
        for ti, t in enumerate(t_values):
            if t >= 0.5:
                lo, hi = max(0, ti - s_w), min(len(K), ti + s_w + 1)
                Ks[ti] = float(np.mean(K[lo:hi]))
        K = Ks
    return K


def test35_form_factor_Kt(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    Nx, Ny = cfg.ab_nx, cfg.ab_ny
    n_real = max(3, cfg.ab_n_realizations)
    Nv = cfg.resolve_vortex_count()
    q = cfg.resolve_q_magnitude()
    W = cfg.w_eff()
    rng = jrng(cfg.ab_seed + 42)
    central_all = []
    print("\n" + "═" * 60)
    print("TEST 35: Spectral Form Factor K(t) — GUE ramp+plateau diagnostic")
    print("─" * 60)
    for ireal in range(1, n_real + 1):
        vortices = random_vortex_configuration(Nv, Nx, Ny, q, rng)
        H = build_ab_cloud_hamiltonian(ABCloudConfig(
            Nx, Ny, vortices, cfg.ab_alpha_test16, cfg.ab_t, cfg.ab_lattice, W,
            cfg.ab_seed + 42 + ireal))
        ev = ab_eigvals(H)
        del H
        n = len(ev)
        half = int(n * cfg.ab_center_fraction) // 2
        central_all.append(ev[n // 2 - half: n // 2 + half])
    eigs = np.concatenate(central_all)
    t_values = cfg.ab_K_t_values
    K_ab = compute_K_form_factor(eigs, t_values, cfg.ab_K_smooth_window)
    K_zeta = compute_K_form_factor(np.asarray(zeros, dtype=float), t_values,
                                   cfg.ab_K_smooth_window)
    K_box = np.array([t * (1.0 - (math.sin(2 * math.pi * t) / (2 * math.pi * t)
                                 if abs(2 * math.pi * t) > 1e-12 else 1.0))
                      for t in t_values])
    mask = np.array([t >= 0.3 for t in t_values])
    rms_gue = float(np.sqrt(np.mean((K_ab[mask] - K_box[mask]) ** 2)))
    corr_gue = float(np.corrcoef(K_ab, K_box)[0, 1])
    corr_zeta = float(np.corrcoef(K_ab, K_zeta)[0, 1])
    print(f" {n_real} realizations, {len(eigs)} central eigenvalues")
    print(" t:", ", ".join(f"{t:g}" for t in t_values))
    print(" K_AB:", ", ".join(f"{v:.4f}" for v in K_ab))
    print(" K_box:", ", ".join(f"{v:.4f}" for v in K_box))
    print(f" RMS(K−K_box) = {rms_gue:.4f}, corr(K_AB, K_box) = {corr_gue:.4f}, "
          f"corr vs ζ = {corr_zeta:.4f}")
    ok = rms_gue < 0.30 and corr_gue > 0.50
    status = msg(cfg, "pass") if ok else msg(cfg, "warn")
    log_result(f" Test 35: K(t) ramp+plateau — RMS_GUE={rms_gue:.4f}, "
               f"corr_GUE={corr_gue:.4f} → {status}")
    return ok, f"RMS={rms_gue:.4f}, corr={corr_gue:.4f}"


def test35b_form_factor_hardcore(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    Nx, Ny = cfg.ab_nx, cfg.ab_ny
    n_hc = max(cfg.ab_n_realizations, cfg.ab_hc_nreal)
    Nv = cfg.resolve_vortex_count_secondary()
    q = cfg.resolve_q_magnitude()
    W = cfg.w_eff()
    rng = jrng(cfg.ab_seed + 3600)
    t_values = cfg.ab_K_t_values
    Ks, rms_vals = [], []
    print("\n" + "═" * 60)
    print(f"TEST 35b [HARDCORE pass 2]: K(t) — {n_hc}-realization ensemble ({Nx}×{Ny})")
    print("─" * 60)
    for k in range(1, n_hc + 1):
        vortices = random_vortex_configuration(Nv, Nx, Ny, q, rng)
        H = build_ab_cloud_hamiltonian(ABCloudConfig(
            Nx, Ny, vortices, cfg.ab_alpha_test16, cfg.ab_t, cfg.ab_lattice, W,
            cfg.ab_seed + 3600 + k))
        ev = ab_eigvals(H)
        del H
        n = len(ev)
        half = int(n * cfg.ab_center_fraction) // 2
        bulk = ev[n // 2 - half: n // 2 + half]
        K_k = compute_K_form_factor(bulk, t_values, cfg.ab_K_smooth_window)
        K_box = np.array([t * (1.0 - (math.sin(2 * math.pi * t) / (2 * math.pi * t)
                                      if abs(2 * math.pi * t) > 1e-12 else 1.0))
                          for t in t_values])
        mask = np.array([t >= 0.3 for t in t_values])
        rms_vals.append(float(np.sqrt(np.mean((K_k[mask] - K_box[mask]) ** 2))))
        Ks.append(K_k)
        print(f"  realization {k}: RMS = {rms_vals[-1]:.4f}")
    K_ens = np.mean(Ks, axis=0)
    K_box = np.array([t * (1.0 - (math.sin(2 * math.pi * t) / (2 * math.pi * t)
                                  if abs(2 * math.pi * t) > 1e-12 else 1.0))
                      for t in t_values])
    mask = np.array([t >= 0.3 for t in t_values])
    rms_ens = float(np.sqrt(np.mean((K_ens[mask] - K_box[mask]) ** 2)))
    corr_ens = float(np.corrcoef(K_ens, K_box)[0, 1])
    rms_scatter = float(np.std(rms_vals, ddof=1))
    rec = [("ensemble RMS < 0.30", rms_ens < 0.30, f"RMS = {rms_ens:.4f}"),
           ("corr > 0.50", corr_ens > 0.50, f"corr = {corr_ens:.4f}"),
           ("RMS scatter ≤ 0.15", rms_scatter <= 0.15, f"σ = {rms_scatter:.4f}")]
    ok = hc_verdict_table(cfg, "Test 35", rec)
    log_result(f" Test 35b: RMS={rms_ens:.4f}, corr={corr_ens:.4f} → "
               f"{'PASS' if ok else 'WARN'}")
    return ok, f"hardcore RMS={rms_ens:.4f}"


def test36_byte_robustness(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    target = cfg.ab37_n_eigs_pass2 if cfg.pass2 else cfg.ab37_n_eigs_pass1
    Nx, Ny = cfg.ab_nx, cfg.ab_ny
    Nv = cfg.resolve_vortex_count_secondary() if cfg.pass2 else cfg.resolve_vortex_count()
    q = cfg.resolve_q_magnitude()
    W = cfg.w_eff()
    rng = jrng(cfg.ab_seed + 88)
    central_all = []
    n_real = 0
    print("\n" + "═" * 60)
    print("TEST 36: Byte-level robustness — quantization + RNG entropy")
    print(f" target {target} central eigenvalues on {Nx}×{Ny}")
    print("─" * 60)
    while sum(len(b) for b in central_all) < target and n_real < 64:
        n_real += 1
        vortices = random_vortex_configuration(Nv, Nx, Ny, q, rng)
        H = build_ab_cloud_hamiltonian(ABCloudConfig(
            Nx, Ny, vortices, cfg.ab_alpha_test16, cfg.ab_t, cfg.ab_lattice, W,
            cfg.ab_seed + 88 + n_real))
        ev = ab_eigvals(H)
        del H
        n = len(ev)
        half = int(n * cfg.ab_center_fraction) // 2
        central_all.append(ev[n // 2 - half: n // 2 + half])
    eigs = np.concatenate(central_all)
    r_raw_all, _ = mean_adjacent_spacing_ratio(eigs)
    # multi-window byte estimator
    n = len(eigs)
    n_windows = clamp(n // 15 - 2, 1, 120)
    starts = np.linspace(1, n - 14, n_windows)
    r_raws, r_bytes = [], []
    for st in starts:
        s0 = jround(st) - 1
        win = eigs[s0:s0 + 15]
        rr, _ = mean_adjacent_spacing_ratio(win)
        lo, hi = float(win.min()), float(win.max())
        q256 = np.round((win - lo) / (hi - lo) * 255).astype(np.int64)
        win_q = lo + q256 * (hi - lo) / 255.0
        rb, _ = mean_adjacent_spacing_ratio(win_q)
        r_raws.append(rr)
        r_bytes.append(rb)
    d_multi = abs(float(np.mean(r_bytes)) - float(np.mean(r_raws)))
    # legacy single window (central 15 of realization 1)
    w1 = central_all[0]
    c15 = w1[len(w1) // 2 - 7: len(w1) // 2 + 8]
    lo, hi = float(c15.min()), float(c15.max())
    c15q = lo + np.round((c15 - lo) / (hi - lo) * 255) * (hi - lo) / 255.0
    r_local_raw, _ = mean_adjacent_spacing_ratio(c15)
    r_local_byte, _ = mean_adjacent_spacing_ratio(c15q)
    d_single = abs(r_local_byte - r_local_raw)
    # RNG entropy block
    brng = jrng(cfg.ab_byte_seed)
    data = brng.integers(0, 256, cfg.ab_n_bytes)
    counts = np.bincount(data, minlength=256)
    p = counts / counts.sum()
    H_bits = float(-(p[p > 0] * np.log2(p[p > 0])).sum())
    chi2 = float(((counts - cfg.ab_n_bytes / 256.0) ** 2 / (cfg.ab_n_bytes / 256.0)).sum())
    chi2_z = (chi2 - 255.0) / math.sqrt(2.0 * 255.0)
    print(f" {n_real} realizations, {n} central eigenvalues; raw ⟨r⟩ = {r_raw_all:.4f} "
          f"({classify_universality_class(r_raw_all)})")
    print(f" multi-window ({n_windows} windows): ⟨r⟩_raw = {np.mean(r_raws):.4f}, "
          f"⟨r⟩_byte = {np.mean(r_bytes):.4f}, |Δ⟨r⟩| = {d_multi:.4f}")
    print(f" single window (diag): raw {r_local_raw:.4f}, byte {r_local_byte:.4f}, "
          f"|Δr| = {d_single:.4f}")
    print(f" RNG: H = {H_bits:.4f} bits, χ²_z = {chi2_z:+.4f}")
    ok = d_multi < cfg.ab_byte_tol and abs(chi2_z) < 3.0 and H_bits > 7.9
    status = msg(cfg, "pass") if ok else msg(cfg, "warn")
    log_result(f" Test 36: byte robust — r_256={np.mean(r_bytes):.4f}, "
               f"|Δr|_multi={d_multi:.4f}, H={H_bits:.4f} → {status}")
    return ok, f"|Δ⟨r⟩|={d_multi:.4f}, H={H_bits:.4f}"
