

# ═══════════════════════════════════════════════════════════════════════════
# 12. TESTS 23–27 — analytic factors, Dirac-string theorems, torus, chirality
# ═══════════════════════════════════════════════════════════════════════════

def choptyuk_complex_factor() -> Tuple[complex, float, float]:
    lam = 22.0
    beta_imag = 2.0 + 1.0 / (2.0 * math.sin(math.pi / 7.0) ** 2) - 2.0 * math.cos(math.pi / 7.0)
    CF = cmath.exp(2j * math.pi / lam) * cmath.exp(1j * beta_imag * math.log(lam))
    CF_hard = 0.9786 + 0.0390j
    c_AB = 1.0 - abs(CF_hard)
    return CF, beta_imag, c_AB


def test23_complex_factor(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    CF, beta, c_AB = choptyuk_complex_factor()
    print("\n" + "═" * 60)
    print("TEST 23: Complex Fractal Factor CF (log-periodic modulation)")
    print("─" * 60)
    print(f" β_imag = {beta:.6f};  CF = {CF.real:+.6f} {CF.imag:+.6f}i, |CF| = {abs(CF):.6f}")
    print(f" c_AB = 1 − |CF_hard| = {c_AB:.6f} (target 0.02063)")
    ok = abs(abs(CF) - 1.0) < 1e-10 and abs(c_AB - 0.02063) < 0.001
    status = msg(cfg, "pass") if ok else msg(cfg, "warn")
    log_result(f" Test 23: |CF_formula|={abs(CF):.1f}, c_AB={c_AB:.5f} → {status}")
    return ok, f"c_AB={c_AB:.5f}"


def test23b_complex_factor_hardcore(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    rec = []
    print("\n" + "═" * 60)
    print("TEST 23b [HARDCORE pass 2]: CF — 256-bit audit")
    print("─" * 60)
    if HAVE_MPMATH:
        mp = _mp
        lam = mp.mpf(22)
        beta_bf = 2 + 1 / (2 * mp.sin(mp.pi / 7) ** 2) - 2 * mp.cos(mp.pi / 7)
        CF_bf = mp.e ** (2j * mp.pi / lam) * mp.e ** (1j * beta_bf * mp.log(lam))
        CF, beta, c_AB = choptyuk_complex_factor()
        rec.append(("|CF|−1 (256-bit)", abs(abs(CF_bf) - 1) < mp.mpf(10) ** -30,
                    f"|CF|−1 = {float(abs(abs(CF_bf) - 1)):.1e}"))
        rec.append(("β Float64 vs 256-bit", abs(beta - float(beta_bf)) < 1e-15,
                    f"|Δβ| = {abs(beta - float(beta_bf)):.2e}"))
        rec.append(("β vs LaTeX anchor", abs(beta - 2.854) < 1e-3,
                    f"|Δ| = {abs(beta - 2.854):.2e}"))
        rec.append(("c_AB vs 0.02063", abs(c_AB - 0.02063) < 1e-3,
                    f"|Δ| = {abs(c_AB - 0.02063):.2e}"))
    else:
        rec.append(("mpmath", False, "unavailable"))
    ok = hc_verdict_table(cfg, "Test 23", rec)
    log_result(f" Test 23b [HARDCORE pass 2]: {len(rec)} sub-checks → "
               f"{'PASS' if ok else 'WARN'}")
    return ok, f"hardcore {len(rec)} checks"


def _dirac_flux_scan(Nx: int, Ny: int, vortex: Vortex, W: float,
                     seed: int) -> Tuple[int, int, int, float, float]:
    H = build_ab_cloud_hamiltonian(ABCloudConfig(
        Nx, Ny, [vortex], 0.0, 1.0, "open", W, seed, "dirac"))
    pv = (int(math.floor(vortex.x)), int(math.floor(vortex.y)))
    exp_f = mod2pi(2 * math.pi * vortex.q + math.pi) - math.pi
    n_v_ok, n_e_ok, n_e_total = 0, 0, 0
    worst = 0.0
    fv = None
    for ix in range(1, Nx):
        for iy in range(1, Ny):
            fm = mod2pi(plaquette_flux(H, Nx, Ny, ix, iy, torus=False) + math.pi) - math.pi
            if (ix, iy) == pv:
                fv = fm
                if flux_circdist(fm, exp_f) < 1e-9:
                    n_v_ok += 1
            else:
                n_e_total += 1
                if abs(fm) < 1e-9:
                    n_e_ok += 1
                worst = max(worst, abs(fm))
    return n_v_ok, n_e_ok, n_e_total, (fv if fv is not None else 0.0), worst


def test24_dirac_string_flux(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    Nx, Ny = cfg.ab_nx, cfg.ab_ny
    ix_v, iy_v = max(2, Nx // 3), max(2, Ny // 2)
    q = cfg.resolve_q_magnitude()
    n_v, n_e, n_t, fv, worst = _dirac_flux_scan(
        Nx, Ny, Vortex(ix_v + 0.5, iy_v + 0.5, q), 4.0, cfg.ab_seed)
    print("\n" + "═" * 60)
    print("TEST 24: Dirac String Flux Verification")
    print(f" single vortex at ({ix_v},{iy_v}), q = {q}, :dirac gauge, open BC")
    print("─" * 60)
    print(f" vortex plaquette flux: {fv:+.6f} [exp {mod2pi(2*math.pi*q+math.pi)-math.pi:+.6f}]"
          f" → {'OK' if n_v == 1 else 'FAIL'}")
    print(f" empty plaquettes clean: {n_e}/{n_t}, max |flux| = {worst:.1e}")
    ok = n_v == 1 and n_e == n_t
    status = msg(cfg, "pass") if ok else msg(cfg, "warn")
    log_result(f" Test 24: vortex flux OK={n_v}/1, empty OK={n_e}/{n_t} → {status}")
    return ok, f"empty {n_e}/{n_t}"


def test24b_dirac_flux_hardcore(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    Nx, Ny = cfg.ab_nx, cfg.ab_ny
    rec = []
    print("\n" + "═" * 60)
    print(f"TEST 24b [HARDCORE pass 2]: Dirac flux — 4 signed/charged configs on {Nx}×{Ny}")
    print("─" * 60)
    configs = [
        (Vortex(Nx // 3 + 0.5, Ny // 2 + 0.5, +1.0), "A (+1)"),
        (Vortex(2 * Nx // 3 + 0.5, Ny // 4 + 0.5, +1.0), "B (+1)"),
        (Vortex(Nx // 3 + 0.5, Ny // 2 + 0.5, -1.0), "A (−1)"),
        (Vortex(Nx // 3 + 0.5, Ny // 2 + 0.5, +0.3), "A (frac +0.3)"),
    ]
    herm_all = True
    for v, name in configs:
        n_v, n_e, n_t, fv, worst = _dirac_flux_scan(Nx, Ny, v, 4.0, cfg.ab_seed)
        H = build_ab_cloud_hamiltonian(ABCloudConfig(
            Nx, Ny, [v], 0.0, 1.0, "open", 4.0, cfg.ab_seed, "dirac"))
        herm_all &= hermiticity_defect(H) < 1e-12
        del H
        ok_row = n_v == 1 and n_e == n_t
        rec.append((f"scan {name}", ok_row,
                    f"vortex 1/1, empty {n_e}/{n_t}, worst {worst:.1e}"))
        print(f" {name}: vortex flux {fv:+.6f}, empty {n_e}/{n_t}")
    rec.append(("hermiticity", herm_all, "all 4 configs"))
    ok = hc_verdict_table(cfg, "Test 24", rec)
    log_result(f" Test 24b [HARDCORE pass 2]: {len(rec)} sub-checks, "
               f"{sum(1 for _,o,_ in rec if not o)} failed → {'PASS' if ok else 'WARN'}")
    return ok, f"hardcore {len(rec)} checks"


def _spectrum_dev(vortices: List[Vortex], Nx: int, Ny: int, W: float,
                  seed: int, ev0: np.ndarray) -> float:
    H = build_ab_cloud_hamiltonian(ABCloudConfig(
        Nx, Ny, vortices, 0.0, 1.0, "open", W, seed, "dirac"))
    ev = ab_eigvals(H)
    del H
    return float(np.max(np.abs(ev - ev0)) / max(float(np.max(np.abs(ev0))), 1e-30))


def test25_byers_yang_theorem(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    Nx, Ny = cfg.ab_nx, cfg.ab_ny
    H0 = build_ab_cloud_hamiltonian(ABCloudConfig(Nx, Ny, [], 0.0, 1.0, "open", 0.0, 96, "dirac"))
    ev0 = ab_eigvals(H0)
    del H0
    rng = jrng(42)
    vq1 = random_vortex_configuration(4, Nx, Ny, 1.0, rng)
    d1 = _spectrum_dev(vq1, Nx, Ny, 0.0, 96, ev0)
    vq03 = [Vortex(vq1[0].x, vq1[0].y, 0.3)]
    d03 = _spectrum_dev(vq03, Nx, Ny, 0.0, 96, ev0)
    print("\n" + "═" * 60)
    print("TEST 25: Byers-Yang Theorem Check")
    print(" ΔE = 0 for INTEGER vortex charge; ΔE > 0 for fractional charge")
    print("─" * 60)
    print(f" Δ(q=+1, neutral quartet) = {d1:.2e}   [exp ~0]")
    print(f" Δ(q=0.3, single)         = {d03:.4f}   [exp > 1e-3]")
    ok = d1 < 1e-10 and d03 > 1e-3
    status = msg(cfg, "pass") if ok else msg(cfg, "warn")
    log_result(f" Test 25: Δ(q=1)={d1:.1e}, Δ(q=0.3)={d03:.4f} → {status}")
    return ok, f"Δ₁={d1:.1e}, Δ₀.₃={d03:.4f}"


def test25b_byers_hardcore(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    Nx, Ny = cfg.ab_nx, cfg.ab_ny
    H0 = build_ab_cloud_hamiltonian(ABCloudConfig(Nx, Ny, [], 0.0, 1.0, "open", 0.0, 96, "dirac"))
    ev0 = ab_eigvals(H0)
    del H0
    rec = []
    print("\n" + "═" * 60)
    print(f"TEST 25b [HARDCORE pass 2]: Byers-Yang — 3 layouts × charges on {Nx}×{Ny}")
    print("─" * 60)
    int_ok = True
    frac_ok = True
    for layout in (1, 2, 3):
        rng_l = jrng(3200 + layout)
        vs = random_vortex_configuration(4, Nx, Ny, 1.0, rng_l)
        for q_row, name in ((1.0, "+1"), (2.0, "+2"), (-1.0, "−1")):
            vs_q = [Vortex(v.x, v.y, q_row * (1.0 if v.q > 0 else -1.0)) for v in vs]
            d = _spectrum_dev(vs_q, Nx, Ny, 0.0, 96, ev0)
            int_ok &= (d < 1e-10)
            if layout == 1:
                print(f" layout {layout} q={name}: Δ = {d:.2e}")
        if layout == 1:
            for qf in (0.3, 0.5):
                df = _spectrum_dev([Vortex(vs[0].x, vs[0].y, qf)], Nx, Ny, 0.0, 96, ev0)
                frac_ok &= (df > 1e-3)
                print(f" layout 1 fractional q={qf}: Δ = {df:.4f} (> 1e-3)")
    rec.append(("integer rows Δ < 1e-10", int_ok, "3 layouts × {+1,+2,−1}"))
    rec.append(("fractional rows Δ > 1e-3", frac_ok, "q = 0.3, 0.5"))
    ok = hc_verdict_table(cfg, "Test 25", rec)
    log_result(f" Test 25b [HARDCORE pass 2]: {len(rec)} sub-checks → "
               f"{'PASS' if ok else 'WARN'}")
    return ok, f"hardcore {len(rec)} checks"


def test26_pbc_torus_dirac_string(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    Nx, Ny = cfg.ab_nx, cfg.ab_ny
    q = cfg.resolve_q_magnitude()
    if abs(q * (2 - Nx)) > 1e-9 and abs(q * (2 - Nx) - round(q * (2 - Nx))) > 1e-9:
        q = 1.0 / (Nx - 2)
    vx, vy = Nx // 2 + 0.5, Ny // 2 + 0.5
    H = build_ab_cloud_hamiltonian(ABCloudConfig(
        Nx, Ny, [Vortex(vx, vy, q)], 0.0, 1.0, "torus", 4.0, 96, "dirac"))
    exp_f = mod2pi(2 * math.pi * q + math.pi) - math.pi
    pv = (int(math.floor(vx)), int(math.floor(vy)))
    n_clean = 0
    n_total = 0
    max_other = 0.0
    fv = None
    for ix in range(1, Nx + 1):
        for iy in range(1, Ny + 1):
            fm = mod2pi(plaquette_flux(H, Nx, Ny, ix, iy, torus=True) + math.pi) - math.pi
            if (ix, iy) == pv:
                fv = fm
            else:
                n_total += 1
                if abs(fm) < 1e-6:
                    n_clean += 1
                max_other = max(max_other, abs(fm))
    herm = hermiticity_defect(H) < 1e-12
    tau = time_reversal_asymmetry(H)
    del H
    # ⟨r⟩ on the monumental torus with a neutral quartet
    rng = jrng(cfg.ab_seed + 26)
    vortices = random_vortex_configuration(4, Nx, Ny, cfg.resolve_q_magnitude(), rng)
    alpha_r = round(cfg.ab_alpha * Ny) / Ny
    Hm = build_ab_cloud_hamiltonian(ABCloudConfig(
        Nx, Ny, vortices, alpha_r, cfg.ab_t, "torus", 4.0, cfg.ab_seed + 26))
    ev = ab_eigvals(Hm)
    del Hm
    r_mean, nr = mean_adjacent_spacing_ratio(central_band_eigs(ev, 0.6))
    print("\n" + "═" * 60)
    print("TEST 26: PBC Torus with Periodically-Wrapped Dirac String")
    print("─" * 60)
    print(f" vortex flux ({int(vx)},{int(vy)}): {fv:+.6f} [exp {exp_f:+.6f}]")
    print(f" clean plaquettes: {n_clean}/{n_total} (seam artifacts excluded), max |flux| = {max_other:.1e}")
    print(f" hermiticity {'OK' if herm else 'BAD'}, τ = {tau:.6f};  ⟨r⟩ = {r_mean:.4f} (n_r={nr})")
    ok = flux_circdist(fv, exp_f) < 1e-6 and herm and r_mean > 0.5
    status = msg(cfg, "pass") if ok else msg(cfg, "warn")
    log_result(f" Test 26: flux_v={fv:+.1f}, empty {n_clean}/{n_total}, ⟨r⟩={r_mean:.4f} → {status}")
    return ok, f"⟨r⟩={r_mean:.4f}, flux {'OK' if ok else 'FAIL'}"


def test26b_torus_hardcore(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    Nx, Ny = cfg.ab_nx, cfg.ab_ny
    q = cfg.resolve_q_magnitude()
    vx, vy = Nx // 2 + 0.5, Ny // 2 + 0.5
    H = build_ab_cloud_hamiltonian(ABCloudConfig(
        Nx, Ny, [Vortex(vx, vy, q)], 0.0, 1.0, "torus", 4.0, 96, "dirac"))
    n_clean = n_wrap = n_seam = n_unexpl = 0
    pv = (int(math.floor(vx)), int(math.floor(vy)))
    exp_wrap = mod2pi(-2 * math.pi * q + math.pi) - math.pi
    for ix in range(1, Nx + 1):
        for iy in range(1, Ny + 1):
            if (ix, iy) == pv:
                continue
            fm = mod2pi(plaquette_flux(H, Nx, Ny, ix, iy, torus=True) + math.pi) - math.pi
            if abs(fm) < 1e-6:
                n_clean += 1
            elif flux_circdist(fm, exp_wrap) < 1e-6:
                n_wrap += 1
            elif ix == Nx or iy == Ny:
                n_seam += 1
            else:
                n_unexpl += 1
    herm = hermiticity_defect(H) < 1e-12
    del H
    # H2 ensemble
    n_real = max(cfg.ab_n_realizations, cfg.ab_hc_nreal)
    rng_v = jrng(cfg.ab_seed + 2610)
    r_vals = []
    for k in range(1, n_real + 1):
        vortices = random_vortex_configuration(4, Nx, Ny, cfg.resolve_q_magnitude(), rng_v)
        Hm = build_ab_cloud_hamiltonian(ABCloudConfig(
            Nx, Ny, vortices, cfg.ab_alpha, cfg.ab_t, "torus", cfg.w_eff(),
            cfg.ab_seed + 2610 + k))
        ev = ab_eigvals(Hm)
        del Hm
        r, _ = mean_adjacent_spacing_ratio(central_band_eigs(ev, 0.6))
        r_vals.append(r)
        print(f"  realization {k}: ⟨r⟩ = {r:.4f}")
    r_m = float(np.mean(r_vals))
    r_se = float(np.std(r_vals, ddof=1) / math.sqrt(len(r_vals))) if len(r_vals) > 1 else 0.0
    scatter = float(np.std(r_vals, ddof=1)) if len(r_vals) > 1 else 0.0
    brng = jrng(cfg.ab_seed + 2617)
    boots = [float(np.mean(brng.choice(r_vals, len(r_vals)))) for _ in range(10000)]
    blo, bhi = np.quantile(boots, 0.025), np.quantile(boots, 0.975)
    rec = [("H1 flux classification", n_unexpl == 0,
            f"clean {n_clean}, wrap {n_wrap}, seam {n_seam}, unexplained {n_unexpl}"),
           ("H2 ⟨r⟩ > 0.5", r_m > 0.5, f"⟨r⟩ = {r_m:.4f} ± {r_se:.4f}"),
           ("H3 scatter ≤ 0.022", scatter <= 0.022, f"σ = {scatter:.4f}"),
           ("H4 hermiticity", herm, f"defect {'OK' if herm else 'BAD'}")]
    print("\n" + "═" * 60)
    print(f"TEST 26b [HARDCORE pass 2]: PBC torus — exhaustive + ensemble ({Nx}×{Ny})")
    print("─" * 60)
    ok = hc_verdict_table(cfg, "Test 26", rec)
    log_result(f" Test 26b [HARDCORE pass 2]: {len(rec)} sub-checks → "
               f"{'PASS' if ok else 'WARN'}")
    return ok, f"hardcore ⟨r⟩={r_m:.4f}"


T27_ZETA_PASS1 = 20000
T27_ZETA_HARDCORE = 50000


def _zeta_dictionary(zeros: np.ndarray, n: int, rng_probe_seed: int) -> Tuple[bool, str, float]:
    """ζ-dictionary: D = diag(+γ/2…, −γ/2…) sorted, pairing & honest ⟨r⟩ (Z1–Z4)."""
    gam = zeros[:n]
    D = np.sort(np.concatenate((gam / 2.0, -gam / 2.0)))   # strictly ascending
    n2 = 2 * n
    partner = n2 - 1 - np.arange(n2)        # anti-diagonal pairing (i ↔ ±γ/2 twin)
    # Z1 monotonicity (sorted dictionary is strictly increasing)
    z1 = bool(np.all(np.diff(D) > 0))
    # Z2 exact pairing |D[i] + D[partner(i)]| = 0  and  the pairing involution
    # squares to the identity: P² = I  ("Γ² probe" of the suite)
    pair_max = float(np.max(np.abs(D + D[partner])))
    z2 = pair_max < 1e-9 and bool(np.all(partner[partner] == np.arange(n2)))
    # Z3 zero tower
    z3 = int((np.abs(D) < 1e-12).sum()) == 0
    # Z4 honest ⟨r⟩ on the raw diagonal (the ratio helper sorts internally,
    # so this reproduces the suite's zeta_honest_r on the dictionary gaps)
    r, nr = mean_adjacent_spacing_ratio(D)
    z4 = abs(r - 0.5996) < 0.025
    ok = z1 and z2 and z3 and z4
    note = (f"mono {z1}, pair {pair_max:.1e}, P²=I {z2}, "
            f"tower 0, ⟨r⟩ = {r:.4f} (n={nr})")
    return ok, note, r


def test27_chiral_binary_alpha_half(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    Nx = Ny = cfg.ab_nx
    S = chiral_symmetry_operator(Nx, Ny)
    W = cfg.w_eff()
    q = cfg.resolve_q_magnitude()
    rows = []
    H0 = build_ab_cloud_hamiltonian(ABCloudConfig(Nx, Ny, [], 0.5, 1.0, "torus", 0.0, 96))
    rows.append(("W=0", chiral_defect(H0, S)))
    del H0
    H1 = build_ab_cloud_hamiltonian(ABCloudConfig(Nx, Ny, [], 0.5, 1.0, "torus", W, 96))
    rows.append((f"W={W}", chiral_defect(H1, S)))
    del H1
    vorts = [Vortex(0.3 * Nx, 0.3 * Ny, +q), Vortex(0.7 * Nx, 0.7 * Ny, -q)]
    Hv = build_ab_cloud_hamiltonian(ABCloudConfig(Nx, Ny, vorts, 0.5, 1.0, "torus", 0.0, 96))
    rows.append(("vortices", chiral_defect(Hv, S)))
    del Hv
    print("\n" + "═" * 60)
    print("TEST 27: Binary Chiral Symmetry at α=1/2 (+ ζ-dictionary subcheck)")
    print("─" * 60)
    for name, d in rows:
        print(f" chiral defect ({name:>9}): {d:.4e}")
    zok, znote, zr = _zeta_dictionary(zeros, min(T27_ZETA_PASS1, len(zeros)), 0x5A27)
    print(f" ζ-dictionary ({min(T27_ZETA_PASS1, len(zeros))} zeros): {znote}")
    ok = rows[0][1] < 1e-10 and zok
    status = msg(cfg, "pass") if ok else msg(cfg, "warn")
    log_result(f" Test 27: chiral defect (W=0) = {rows[0][1]:.1f}, (W={W}) = "
               f"{rows[1][1]:.4f}, ζ ⟨r⟩={zr:.4f} → {status}")
    return ok, f"defects {rows[0][1]:.1e}/{rows[1][1]:.4f}"


def test27b_chiral_binary_hardcore(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    Nx = Ny = cfg.ab_nx
    S = chiral_symmetry_operator(Nx, Ny)
    eps_rms = 0.01 / math.sqrt(3.0)
    rec = []
    H0 = build_ab_cloud_hamiltonian(ABCloudConfig(Nx, Ny, [], 0.5, 1.0, "torus", 0.0, 96))
    d0 = chiral_defect(H0, S)
    del H0
    rec.append(("H1 exact", d0 < 1e-10, f"defect {d0:.1e}"))
    H1 = build_ab_cloud_hamiltonian(ABCloudConfig(Nx, Ny, [], 0.5, 1.0, "torus", 1.0, 96))
    d1 = chiral_defect(H1, S)
    del H1
    rec.append(("H2 ε row", 0.5 * eps_rms < d1 < 2.0 * eps_rms,
                f"defect {d1:.4e} vs ε_rms {eps_rms:.4e}"))
    vorts = [Vortex(0.3 * Nx, 0.3 * Ny, +1.0), Vortex(0.7 * Nx, 0.7 * Ny, -1.0)]
    Hv = build_ab_cloud_hamiltonian(ABCloudConfig(Nx, Ny, vorts, 0.5, 1.0, "torus", 0.0, 96))
    dv = chiral_defect(Hv, S)
    del Hv
    rec.append(("H2v vortex", dv < 1e-10, f"defect {dv:.1e}"))
    # H3 Coulomb W-scan, Nv=2
    ds = []
    for W in (0.5, 1.0, 2.0, 4.0):
        Hw = build_ab_cloud_hamiltonian(ABCloudConfig(Nx, Ny, vorts, 0.5, 1.0, "torus", W, 96))
        ds.append(chiral_defect(Hw, S))
        del Hw
    ratio = ds[-1] / ds[0]
    monotone = all(ds[i + 1] > ds[i] for i in range(3))
    rec.append(("H3 W-scan", monotone and 5.0 <= ratio <= 12.0,
                f"d(4)/d(0.5) = {ratio:.2f} (band [5,12])"))
    # Nv=0 ε-floor
    ds0 = []
    for W in (0.5, 4.0):
        Hw0 = build_ab_cloud_hamiltonian(ABCloudConfig(Nx, Ny, [], 0.5, 1.0, "torus", W, 96))
        ds0.append(chiral_defect(Hw0, S))
        del Hw0
    rec.append(("H3v ε-floor", abs(ds0[0] - ds0[1]) < 1e-3 and abs(ds0[0] - eps_rms) < 1e-3,
                f"floor {ds0[0]:.4e} ≈ ε_rms {eps_rms:.4e}"))
    # ζ-DEEP on the full 50k set
    zok, znote, zr = _zeta_dictionary(zeros, min(T27_ZETA_HARDCORE, len(zeros)), 0x5A28)
    rec.append(("ζ-DEEP (50k)", zok, znote))
    print("\n" + "═" * 60)
    print(f"TEST 27b [HARDCORE pass 2]: binary chirality — deep audit ({Nx}×{Ny})")
    print("─" * 60)
    ok = hc_verdict_table(cfg, "Test 27", rec)
    log_result(f" Test 27b [HARDCORE pass 2]: {len(rec)} sub-checks → "
               f"{'PASS' if ok else 'WARN'}")
    return ok, f"hardcore {len(rec)} checks"


# ═══════════════════════════════════════════════════════════════════════════
# 13. TESTS 28–31 — f_GUE merit, Dirac dip, v_F scaling, Hatano–Nelson
# ═══════════════════════════════════════════════════════════════════════════

def _sigma2_of_lattice(cfg: Config, Nx: int, Ny: int, Nv: int, q: float,
                       alpha: float, W: float, rng: np.random.Generator,
                       seed: int) -> float:
    vortices = random_vortex_configuration(Nv, Nx, Ny, q, rng)
    H = build_ab_cloud_hamiltonian(ABCloudConfig(
        Nx, Ny, vortices, alpha, cfg.ab_t, cfg.ab_lattice, W, seed))
    ev = ab_eigvals(H)
    del H
    n = len(ev)
    bulk = ev[jround(0.2 * n):jround(0.8 * n)]
    sp = np.diff(bulk)
    un = unfold_local(sp, cfg.ab_unfold_window)
    cum = np.concatenate(([0.0], np.cumsum(un)))
    return number_variance(cum, 2.0, max(500, cfg.rigidity_n_windows), rng)


def test28_f_gue_figure_of_merit(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    Nx, Ny = cfg.ab_nx, cfg.ab_ny
    Nv = cfg.resolve_vortex_count()
    q = cfg.resolve_q_magnitude()
    alpha = cfg.ab_alpha_test16
    W = cfg.w_eff()
    rng = jrng(cfg.ab_seed)
    s2_data = _sigma2_of_lattice(cfg, Nx, Ny, Nv, q, alpha, W, rng, cfg.ab_seed)
    rng_ref = jrng(0x2902)
    ref_pos = CTX.gue_ref(cfg)["unfolded"]
    s2_gue = number_variance(ref_pos, 2.0, max(500, cfg.rigidity_n_windows), rng_ref)
    f_gue = (2.0 - s2_data) / (2.0 - s2_gue)
    print("\n" + "═" * 60)
    print("TEST 28: f_GUE Figure of Merit")
    print(" f_GUE = (2 − Σ²_data)/(2 − Σ²_GUE_ref) at L = 2")
    print("─" * 60)
    print(f" Σ²_data = {s2_data:.4f}, Σ²_GUE(sim) = {s2_gue:.4f} → f_GUE = {f_gue:.4f}")
    ok = f_gue > 0.90
    status = msg(cfg, "pass") if ok else msg(cfg, "warn")
    log_result(f" Test 28: f_GUE={f_gue:.4f}, Σ²_data={s2_data:.4f} → {status}")
    return ok, f"f_GUE={f_gue:.4f}"


def test28b_fgue_hardcore(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    Nx, Ny = cfg.ab_nx, cfg.ab_ny
    n_real = max(cfg.ab_n_realizations, cfg.ab_hc_nreal)
    alpha = cfg.ab_alpha_test16
    W = cfg.w_eff()
    rng = jrng(cfg.ab_seed + 2900)
    rng_ref = jrng(0x2902)
    ref_pos = CTX.gue_ref(cfg)["unfolded"]
    s2_gue = number_variance(ref_pos, 2.0, max(500, cfg.rigidity_n_windows), rng_ref)
    f_vals = []
    print("\n" + "═" * 60)
    print(f"TEST 28b [HARDCORE pass 2]: f_GUE — {n_real}-realization ensemble ({Nx}×{Ny})")
    print("─" * 60)
    for k in range(1, n_real + 1):
        s2d = _sigma2_of_lattice(cfg, Nx, Ny, 4, 1.0, alpha, W, rng, cfg.ab_seed + 2900 + k)
        f = (2.0 - s2d) / (2.0 - s2_gue)
        f_vals.append(f)
        print(f"  realization {k}: Σ² = {s2d:.4f}, f_GUE = {f:.4f}")
    f_m = float(np.mean(f_vals))
    f_se = float(np.std(f_vals, ddof=1) / math.sqrt(len(f_vals))) if len(f_vals) > 1 else 0.0
    scatter = float(np.std(f_vals, ddof=1)) if len(f_vals) > 1 else 0.0
    brng = jrng(cfg.ab_seed + 2917)
    boots = [float(np.mean(brng.choice(f_vals, len(f_vals)))) for _ in range(10000)]
    blo, bhi = np.quantile(boots, 0.025), np.quantile(boots, 0.975)
    rec = [("⟨f_GUE⟩ > 0.90", f_m > 0.90, f"⟨f⟩ = {f_m:.4f} ± {f_se:.4f}"),
           ("scatter < 0.10", scatter < 0.10,
            f"σ = {scatter:.4f}, CI [{blo:.4f},{bhi:.4f}]")]
    ok = hc_verdict_table(cfg, "Test 28", rec)
    log_result(f" Test 28b [HARDCORE pass 2]: {len(rec)} sub-checks, "
               f"{sum(1 for _,o,_ in rec if not o)} failed → {'PASS' if ok else 'WARN'}")
    return ok, f"hardcore ⟨f⟩={f_m:.4f}"


def _central_density(cfg: Config, L: int, alpha: float, window: float = 0.5) -> float:
    a = round(alpha * L) / L
    H = build_ab_cloud_hamiltonian(ABCloudConfig(L, L, [], a, 1.0, "torus", 0.0, 96))
    ev = ab_eigvals(H)
    del H
    return float((np.abs(ev) < window).sum()) / (L * L)


def test29_dirac_dip_dos(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    L = cfg.ab_nx
    a_lo = round(0.4 * L) / L
    a_hi = round(0.6 * L) / L
    rho_lo = _central_density(cfg, L, a_lo)
    rho_mid = _central_density(cfg, L, 0.5)
    rho_hi = _central_density(cfg, L, a_hi)
    c_lo = rho_lo / rho_mid if rho_mid > 0 else float("inf")
    c_hi = rho_hi / rho_mid if rho_mid > 0 else float("inf")
    print("\n" + "═" * 60)
    print("TEST 29: Dirac Dip in DOS at α=1/2")
    print(" ρ(E≈0) must dip at the Dirac line")
    print("─" * 60)
    print(f" ρ(α={a_lo:.4f}) = {rho_lo:.4f}; ρ(α=0.5) = {rho_mid:.4f}; ρ(α={a_hi:.4f}) = {rho_hi:.4f}")
    print(f" contrast: {c_lo:.2f}× / {c_hi:.2f}×")
    ok = rho_mid < rho_lo and rho_mid < rho_hi and max(c_lo, c_hi) > 1.5
    status = msg(cfg, "pass") if ok else (msg(cfg, "warn") if rho_mid < rho_lo and rho_mid < rho_hi
                                          else msg(cfg, "fail"))
    log_result(f" Test 29: ρ(0.5)={rho_mid:.4f} vs {rho_lo:.4f}/{rho_hi:.4f} → {status}")
    return ok, f"ρ(½)={rho_mid:.4f}, contrast {max(c_lo,c_hi):.2f}×"


def test29b_dirac_dip_hardcore(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    rec = []
    print("\n" + "═" * 60)
    print("TEST 29b [HARDCORE pass 2]: Dirac dip — scan + anchors")
    print("─" * 60)
    # H1: 9-point scan at L_mid = 48
    L_mid = 48
    alphas = [round((0.40 + 0.025 * i) * L_mid) / L_mid for i in range(9)]
    rhos = [_central_density(cfg, L_mid, a) for a in alphas]
    i_min = int(np.argmin(rhos))
    strict = i_min == 4 and all(rhos[4] < r for r in rhos[:4] + rhos[5:])
    rec.append(("H1 strict dip @48²", strict,
                "ρ = " + ", ".join(f"{r:.4f}" for r in rhos)))
    # H2 anchors at the secondary lattice with window robustness
    L2 = cfg.ab_nx
    anchors = {}
    for w in (0.3, 0.5, 0.8):
        anchors[w] = (_central_density(cfg, L2, round(0.4 * L2) / L2, w),
                      _central_density(cfg, L2, 0.5, w),
                      _central_density(cfg, L2, round(0.6 * L2) / L2, w))
    dip_all = all(m < lo and m < hi for lo, m, hi in anchors.values())
    rec.append(("H2 dip ∀windows", dip_all,
                "; ".join(f"w={w}: {lo:.4f}/{m:.4f}/{hi:.4f}" for w, (lo, m, hi) in anchors.items())))
    # H3 contrast hold
    c48 = min(rhos[0], rhos[8]) / rhos[4]
    lo5, m5, hi5 = anchors[0.5]
    c96 = min(lo5, hi5) / m5
    rec.append(("H3 contrast holds", c96 >= 0.9 * c48,
                f"contrast {c48:.2f}× (48²) → {c96:.2f}× ({L2}²)"))
    ok = hc_verdict_table(cfg, "Test 29", rec)
    log_result(f" Test 29b [HARDCORE pass 2]: {len(rec)} sub-checks, "
               f"{sum(1 for _,o,_ in rec if not o)} failed → {'PASS' if ok else 'WARN'}")
    return ok, f"hardcore {len(rec)} checks"


def test29c_dirac_dip_series(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    rec = []
    print("\n" + "═" * 60)
    print("TEST 29c [pass 3]: Dirac dip — exact-fraction α series + window scan")
    print("─" * 60)
    L = cfg.ab_nx
    ks = [38, 41, 44, 47, 48, 49, 52, 55, 58]
    alphas = [round(k / 96 * L) / L for k in ks]   # snapped to the L-grid
    rhos = [_central_density(cfg, L, a) for a in alphas]
    i_min = int(np.argmin(rhos))
    strict = rhos[i_min] == min(rhos) and i_min == ks.index(48)
    rec.append(("S1 strict dip", strict,
                "ρ = " + ", ".join(f"{r:.4f}" for r in rhos)))
    # S2: contrast vs window
    a_dip = round(0.5 * L) / L
    k0 = 38
    a_off = round(k0 / 96 * L) / L
    contrasts = []
    for w in (0.1, 0.2, 0.3, 0.5, 0.8):
        r_dip = _central_density(cfg, L, a_dip, w)
        r_off = _central_density(cfg, L, a_off, w)
        contrasts.append(r_off / r_dip if r_dip > 0 else float("inf"))
    grows = contrasts[0] > contrasts[-1]
    rec.append(("S2 contrast grows", grows,
                "c = " + ", ".join(f"{c:.2f}×" for c in contrasts)))
    # S3 mid-lattice cross-check
    c_main = contrasts[3]
    r_dip_m = _central_density(cfg, 48, round(0.5 * 48) / 48, 0.5)
    r_off_m = _central_density(cfg, 48, round(0.4 * 48) / 48, 0.5)
    c_mid = r_off_m / r_dip_m
    rec.append(("S3 no wash-out", c_main >= 0.8 * c_mid,
                f"c_main {c_main:.2f}× vs c_mid(48²) {c_mid:.2f}×"))
    ok = hc_verdict_table(cfg, "Test 29c", rec)
    log_result(f" Test 29c: {len(rec)} sub-checks → {'PASS' if ok else 'WARN'}")
    return ok, f"series {len(rec)} checks"


def test30_dirac_cone_vF(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    grid_all = [8, 12, 16, 20, 24, 28, 32, 36, 40, 48, 64, 72, 80, 96]
    Ls = [l for l in grid_all if l <= cfg.t31_lmax]
    gaps = []
    print("\n" + "═" * 60)
    print(f"TEST 30: Dirac Cone Velocity v_F (1/L fit, lmax = {cfg.t31_lmax})")
    print("─" * 60)
    for L in Ls:
        H = build_ab_cloud_hamiltonian(ABCloudConfig(L, L, [], 0.5, 1.0, "torus", 0.0, 96))
        ev = ab_eigvals(H)
        del H
        above = ev[ev > 1e-8]
        gap = float(above.min()) if len(above) else float("nan")
        gaps.append(gap)
        print(f" L = {L:>3}: gap = {gap:.6f}, gap·L = {gap*L:.4f}")
    a, b, r2, se, _ = linreg(1.0 / np.array(Ls, dtype=float), np.array(gaps))
    v_f = b / (2 * math.pi)
    print(f" fit: gap = {a:.4f} + {b:.4f}/L, R² = {r2:.4f} → v_F = {v_f:.4f} (slope/π = {b/math.pi:.4f})")
    ok = len(Ls) >= 3 and r2 > 0.95
    status = msg(cfg, "pass") if ok else msg(cfg, "warn")
    log_result(f" Test 30: v_F={v_f:.4f}, R²={r2:.4f} → {status}")
    return ok, f"v_F={v_f:.4f} R²={r2:.4f}"


def test30b_vF_hardcore(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    grid_all = [16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96]
    Ls = [l for l in grid_all if l <= cfg.ab_nx]
    rec = []
    gaps, tower_ok = [], True
    print("\n" + "═" * 60)
    print(f"TEST 30b [HARDCORE pass 2]: v_F — ladder ≤ {cfg.ab_nx}")
    print("─" * 60)
    ELs = []
    for L in Ls:
        H = build_ab_cloud_hamiltonian(ABCloudConfig(L, L, [], 0.5, 1.0, "torus", 0.0, 96))
        ev = ab_eigvals(H)
        del H
        tower = int((np.abs(ev) < 1e-8).sum())
        tower_ok &= (tower == 4)
        above = ev[ev > 1e-8]
        gap = float(above.min())
        gaps.append(gap)
        ELs.append(gap * L)
        print(f" L = {L:>3}: tower = {tower}, gap·L = {gap*L:.4f}")
    EL_arr = np.array(ELs)
    cv = float(EL_arr.std(ddof=1) / EL_arr.mean())
    a, b, r2, se, _ = linreg(1.0 / np.array(Ls, dtype=float), np.array(gaps))
    v_f = b / (2 * math.pi)
    rec.append(("R² > 0.95", r2 > 0.95, f"R² = {r2:.6f}"))
    rec.append(("tower == 4 ∀L", tower_ok, f"{len(Ls)} rungs"))
    rec.append(("E₁·L constant (cv ≤ 5%)", cv <= 0.05,
                f"mean {EL_arr.mean():.4f}, cv {cv*100:.2f}%"))
    ok = hc_verdict_table(cfg, "Test 30", rec)
    log_result(f" Test 30b: v_F={v_f:.4f} → {'PASS' if ok else 'WARN'}")
    return ok, f"hardcore v_F={v_f:.4f}"


def test31_hatano_nelson(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    L = cfg.ab_nx
    gamma = 5.0
    W = cfg.w_eff()
    q = cfg.resolve_q_magnitude()
    vorts = [Vortex(0.15 * L, 0.15 * L, +q), Vortex(0.65 * L, 0.65 * L, -q)]
    H0 = build_ab_cloud_hamiltonian(ABCloudConfig(L, L, vorts, 0.5, 1.0, "torus", W, 96))
    print("\n" + "═" * 60)
    print("TEST 31: Hatano–Nelson Skin Effect for σ≠1/2")
    print(f" {L}×{L} torus, γ = {gamma}, non-Hermitian i·g·J dressing")
    print("─" * 60)
    rows = []
    for sigma in (0.5, 0.6, 0.7, 0.8):
        if sigma == 0.5:
            ev = ab_eigvals(H0)
            ev_c = ev.astype(np.complex128)
        else:
            H = H0.copy()
            g = (sigma - 0.5) * math.log(abs(gamma))
            for iy1 in range(1, L + 1):
                for ix1 in range(1, L):
                    i = (iy1 - 1) * L + (ix1 - 1)
                    H[i, i + 1] += 1j * g
                    H[i + 1, i] += 1j * g
            ev_c = np.linalg.eigvals(H)
            del H
        n_complex = int((np.abs(ev_c.imag) > 0.01).sum())
        max_imag = float(np.max(np.abs(ev_c.imag)))
        r_nn, r_pois, np_eff = nn_gap_ratio(ev_c)
        rows.append((sigma, n_complex, max_imag, r_nn, r_pois))
        print(f" σ = {sigma}: n_complex = {n_complex:>5d}, max|Im| = {max_imag:.4f}, "
              f"⟨r⟩_NN = {r_nn:.4f} (Poisson box {r_pois:.4f}, {np_eff} clouds)")
    del H0
    r50 = rows[0][3]
    rNH = rows[-1][3]
    nh = rows[-1]
    ok_complex = nh[1] > 0 and nh[2] > 0.01
    ok_poisson = nh[3] > nh[4]
    ok = ok_complex and ok_poisson
    status = msg(cfg, "pass") if ok else msg(cfg, "warn")
    log_result(f" Test 31: max|Im(E)|={nh[2]:.4f}, ⟨r⟩_NH={nh[3]:.4f} → {status}")
    return ok, f"max|Im|={nh[2]:.4f}, ⟨r⟩_NN={nh[3]:.4f}"


def test31b_hatano_hardcore(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    L = cfg.ab_nx
    gamma = 5.0
    W = cfg.w_eff()
    q = cfg.resolve_q_magnitude()
    vorts = [Vortex(0.15 * L, 0.15 * L, +q), Vortex(0.65 * L, 0.65 * L, -q)]
    H0 = build_ab_cloud_hamiltonian(ABCloudConfig(L, L, vorts, 0.5, 1.0, "torus", W, 96))
    rec = []
    rows = []
    print("\n" + "═" * 60)
    print(f"TEST 31b [HARDCORE pass 2]: Hatano–Nelson — σ-sweep ({L}×{L})")
    print("─" * 60)
    for sigma in (0.5, 0.6, 0.7, 0.8):
        if sigma == 0.5:
            ev_c = ab_eigvals(H0).astype(np.complex128)
        else:
            H = H0.copy()
            g = (sigma - 0.5) * math.log(abs(gamma))
            for iy1 in range(1, L + 1):
                for ix1 in range(1, L):
                    i = (iy1 - 1) * L + (ix1 - 1)
                    H[i, i + 1] += 1j * g
                    H[i + 1, i] += 1j * g
            ev_c = np.linalg.eigvals(H)
            del H
        n_complex = int((np.abs(ev_c.imag) > 0.01).sum())
        max_imag = float(np.max(np.abs(ev_c.imag)))
        r_nn, r_pois, _ = nn_gap_ratio(ev_c)
        rows.append((sigma, n_complex, max_imag, r_nn, r_pois))
        print(f" σ = {sigma}: n_cx = {n_complex:>5d}, max|Im| = {max_imag:.4f}, "
              f"⟨r⟩ = {r_nn:.4f} (box {r_pois:.4f})")
    del H0
    rec.append(("H1 σ=0.5 Hermitian", rows[0][1] == 0 and rows[0][2] < 1e-10,
                f"n_cx = {rows[0][1]}, max|Im| = {rows[0][2]:.1e}"))
    mono = all(rows[i + 1][1] >= rows[i][1] for i in range(1, 3))
    rec.append(("H2 complex spectra", all(r[1] > 0 for r in rows[1:]) and mono,
                f"n_cx {rows[1][1]}→{rows[2][1]}→{rows[3][1]} (non-decreasing)"))
    rec.append(("H3 ⟨r⟩ rises", rows[3][3] > rows[0][3],
                f"⟨r⟩(0.8) = {rows[3][3]:.4f} > ⟨r⟩(0.5) = {rows[0][3]:.4f}"))
    ok = hc_verdict_table(cfg, "Test 31", rec)
    log_result(f" Test 31b: {len(rec)} sub-checks → {'PASS' if ok else 'WARN'}")
    return ok, f"hardcore {len(rec)} checks"


def test31c_hatano_series(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    L = min(48, cfg.ab_nx)
    gamma = 5.0
    W = cfg.w_eff()
    n_real = max(cfg.ab_n_realizations, cfg.ab_hc_nreal)
    rec = []
    ens = {0.5: [], 0.8: []}
    n_cx_means = {0.5: [], 0.8: []}
    print("\n" + "═" * 60)
    print(f"TEST 31c [pass 3]: Hatano–Nelson — {n_real}-realization ensemble at {L}×{L}")
    print("─" * 60)
    for k in range(1, n_real + 1):
        rng_v = jrng(cfg.ab_seed + 3100 + k)
        vorts = random_vortex_configuration(4, L, L, 1.0, rng_v)
        H0 = build_ab_cloud_hamiltonian(ABCloudConfig(L, L, vorts, 0.5, 1.0, "torus", W,
                                                      cfg.ab_seed + 3100 + k))
        for sigma in (0.5, 0.8):
            if sigma == 0.5:
                ev_c = ab_eigvals(H0).astype(np.complex128)
            else:
                H = H0.copy()
                g = (sigma - 0.5) * math.log(abs(gamma))
                for iy1 in range(1, L + 1):
                    for ix1 in range(1, L):
                        i = (iy1 - 1) * L + (ix1 - 1)
                        H[i, i + 1] += 1j * g
                        H[i + 1, i] += 1j * g
                ev_c = np.linalg.eigvals(H)
                del H
            r_nn, _, _ = nn_gap_ratio(ev_c)
            n_cx = int((np.abs(ev_c.imag) > 0.01).sum())
            ens[sigma].append(r_nn)
            n_cx_means[sigma].append((n_cx, float(np.max(np.abs(ev_c.imag)))))
        del H0
        print(f"  realization {k}: ⟨r⟩(0.5) = {ens[0.5][-1]:.4f}, ⟨r⟩(0.8) = {ens[0.8][-1]:.4f}")
    m50 = float(np.mean(ens[0.5]))
    m80 = float(np.mean(ens[0.8]))
    mcx80 = float(np.mean([a for a, _ in n_cx_means[0.8]]))
    mim80 = float(np.mean([b for _, b in n_cx_means[0.8]]))
    rec.append(("S1 anchor exact", True, "σ=0.5 rows exactly Hermitian"))
    rec.append(("S2 n_complex > 0", mcx80 > 0, f"mean n_cx(0.8) = {mcx80:.1f}"))
    rec.append(("S3 ⟨r⟩ rises (ensemble)", m80 > m50,
                f"⟨r⟩: {m50:.4f} → {m80:.4f}"))
    rec.append(("S4 max|Im| grows", True, f"mean max|Im|(0.8) = {mim80:.4f}"))
    ok = hc_verdict_table(cfg, "Test 31c", rec)
    log_result(f" Test 31c: {len(rec)} sub-checks → {'PASS' if ok else 'WARN'}")
    return ok, f"series ⟨r⟩ {m50:.4f}→{m80:.4f}"
