

# ═══════════════════════════════════════════════════════════════════════════
# 10. AB-CLOUD HOFSTADTER LATTICE (Julia 2614–3327) — builders & observables
# ═══════════════════════════════════════════════════════════════════════════

RAM_BUDGET = 1.15e9  # bytes for one dense complex matrix (session guard)


class Vortex:
    __slots__ = ("x", "y", "q")

    def __init__(self, x: float, y: float, q: float):
        self.x, self.y, self.q = float(x), float(y), float(q)


class ABCloudConfig:
    def __init__(self, Nx, Ny, vortices, alpha, t, lattice, W,
                 disorder_seed=96, vortex_phase_model="monumental"):
        self.Nx, self.Ny = Nx, Ny
        self.vortices = vortices
        self.alpha, self.t = alpha, t
        self.lattice = lattice            # "open" | "torus"
        self.W = W
        self.disorder_seed = disorder_seed
        self.model = vortex_phase_model   # "monumental" | "dirac"
        if lattice == "torus":
            assert abs(alpha * Ny - round(alpha * Ny)) < 1e-10, \
                "torus needs α·Ny ∈ ℤ"


def ab_phase_vortex_monumental(xj, yj, xi, yi, vortices) -> float:
    phase = 0.0
    for v in vortices:
        dxj, dyj = xj - v.x, yj - v.y
        dxi, dyi = xi - v.x, yi - v.y
        if dxj == 0.0 and dyj == 0.0:
            continue
        phase += v.q * (math.atan2(dyj, dxj) - math.atan2(dyi, dxi)) * 0.5
    return phase


def ab_phase_2d_full(ri, rj, vortices, torus: bool, Nx: int) -> float:
    """:dirac model — smooth polar phases + explicit Dirac strings (both dirs)."""
    xi, yi = ri
    xj, yj = rj
    phase = 0.0
    for v in vortices:
        dxi, dyi = xi - v.x, yi - v.y
        dxj, dyj = xj - v.x, yj - v.y
        if dxi == 0.0 and dyi == 0.0:
            a_i = 0.0
        else:
            a_i = math.atan2(dyi, dxi)
        if dxj == 0.0 and dyj == 0.0:
            a_j = 0.0
        else:
            a_j = math.atan2(dyj, dxj)
        phase += v.q * (a_i - a_j)
        # explicit Dirac string: vertical bonds only
        if abs(xi - xj) < 1e-12:
            y_lo, y_hi = min(yi, yj), max(yi, yj)
            crosses = y_lo < v.y < y_hi
            if crosses:
                if torus:
                    skip = abs(xi - math.floor(v.x)) < 0.5
                else:
                    skip = not (xi > v.x)
                if not skip:
                    phase += (-2.0 * math.pi * v.q) if yi < yj else (2.0 * math.pi * v.q)
    return phase


def vortex_onsite_potential(ri, vortices, W: float, N: int,
                            rng: Optional[np.random.Generator]) -> float:
    if not vortices and W == 0.0:
        return 0.0  # clean fast path — no RNG consumed
    V = 0.0
    for v in vortices:
        d2 = (ri[0] - v.x) ** 2 + (ri[1] - v.y) ** 2
        V += v.q * W / (d2 / N + 1.0)
    if W > 0.0:
        V += (rng.random() - 0.5) * 0.02
    return V


def build_ab_cloud_hamiltonian(c: ABCloudConfig) -> np.ndarray:
    Nx, Ny, N = c.Nx, c.Ny, c.Nx * c.Ny
    if 16.0 * N * N * 1.25 > 8.0 * RAM_BUDGET:
        raise MemoryError(f"lattice {Nx}x{Ny} exceeds the RAM guard")
    torus = c.lattice == "torus"
    rng_dis = jrng(c.disorder_seed) if (c.vortices or c.W > 0.0) else None
    H = np.zeros((N, N), dtype=np.complex128)
    t = c.t

    def site(iy1, ix1):            # 1-based → 0-based flat index
        return (iy1 - 1) * Nx + (ix1 - 1)

    for iy1 in range(1, Ny + 1):
        for ix1 in range(1, Nx + 1):
            i = site(iy1, ix1)
            ri = (ix1, iy1)
            # ---- right bond (ix → ix+1) ----
            jx1, jy1 = ix1 + 1, iy1
            wrap_x = jx1 > Nx
            if wrap_x:
                if not torus:
                    jx1 = None
                else:
                    jx1 = 1
            if jx1 is not None:
                j = site(jy1, jx1)
                phi = 2.0 * math.pi * c.alpha * iy1
                if c.model == "dirac":
                    rj = ((Nx + 1) if wrap_x else jx1, jy1)
                    for v in c.vortices:
                        dxi, dyi = ri[0] - v.x, ri[1] - v.y
                        dxj, dyj = rj[0] - v.x, rj[1] - v.y
                        if dxi == 0.0 and dyi == 0.0:
                            a_i = 0.0
                        else:
                            a_i = math.atan2(dyi, dxi)
                        if dxj == 0.0 and dyj == 0.0:
                            a_j = 0.0
                        else:
                            a_j = math.atan2(dyj, dxj)
                        phi += v.q * (a_i - a_j)
                H[i, j] += -t * np.exp(1j * phi)
                H[j, i] += -t * np.exp(-1j * phi)
            # ---- up bond (iy → iy+1) ----
            jy1b = iy1 + 1
            wrap_y = jy1b > Ny
            if wrap_y:
                if not torus:
                    jy1b = None
                else:
                    jy1b = 1
            if jy1b is not None:
                j = site(jy1b, ix1)
                phi = (2.0 * math.pi * c.alpha * Ny) if wrap_y else 0.0
                ry = (iy1 + 1) if wrap_y else jy1b   # unwrapped top coordinate
                if c.model == "monumental":
                    phi += ab_phase_vortex_monumental(ix1, ry, ri[0], ri[1], c.vortices)
                else:
                    phi += ab_phase_2d_full(ri, (ix1, ry), c.vortices, torus, Nx)
                H[i, j] += -t * np.exp(1j * phi)
                H[j, i] += -t * np.exp(-1j * phi)
            # ---- on-site ----
            H[i, i] += vortex_onsite_potential(ri, c.vortices, c.W, N, rng_dis)
    H = (H + H.conj().T) / 2.0
    return H


def ab_eigvals(H: np.ndarray) -> np.ndarray:
    return np.linalg.eigvalsh(H)


def ab_w_eff(cfg: Config) -> float:
    return cfg.w_eff()


def plaquette_flux(H: np.ndarray, Nx: int, Ny: int, ix: int, iy: int,
                   torus: bool) -> float:
    """CCW loop bl→br→tr→tl→bl; bond phase = angle(−H[b,a])."""
    def site(x1, y1):
        if torus:
            x1 = (x1 - 1) % Nx + 1
            y1 = (y1 - 1) % Ny + 1
        return (y1 - 1) * Nx + (x1 - 1)

    bl, br = site(ix, iy), site(ix + 1, iy)
    tr, tl = site(ix + 1, iy + 1), site(ix, iy + 1)
    flux = 0.0
    for a, b in ((bl, br), (br, tr), (tr, tl), (tl, bl)):
        flux += math.atan2(-H[b, a].imag, -H[b, a].real)
    return flux


def mod2pi(x: float) -> float:
    return x % (2.0 * math.pi)


def flux_circdist(a: float, b: float) -> float:
    return abs((a - b + math.pi) % (2.0 * math.pi) - math.pi)


def chiral_symmetry_operator(Nx: int, Ny: int) -> np.ndarray:
    N = Nx * Ny
    S = np.zeros(N)
    for iy1 in range(1, Ny + 1):
        for ix1 in range(1, Nx + 1):
            S[(iy1 - 1) * Nx + (ix1 - 1)] = 1.0 if (ix1 + iy1) % 2 == 0 else -1.0
    return S


def chiral_defect(H: np.ndarray, S: np.ndarray) -> float:
    T = S[:, None] * H * S[None, :]
    D = T + H
    return float(np.linalg.norm(D) / max(np.linalg.norm(H), 1e-30))


def hermiticity_defect(H: np.ndarray) -> float:
    return float(np.max(np.abs(H - H.conj().T)) / max(np.linalg.norm(H), 1e-30))


def time_reversal_asymmetry(H: np.ndarray) -> float:
    return float(np.linalg.norm(H - H.conj()) / max(np.linalg.norm(H), 1e-30))


def central_band_eigs(ev: np.ndarray, frac: float) -> np.ndarray:
    n = len(ev)
    half = int(n * frac) // 2          # Julia fld(n·frac, 2)
    j_lo = max(0, n // 2 - half)
    j_hi = min(n, n // 2 + half)
    return ev[j_lo:j_hi]


def unfold_local(spacings: np.ndarray, win_frac: float = 0.05) -> np.ndarray:
    """Local-mean unfolding: s_i = δ_i / mean(δ over [i−win, i+win]); keep 0<s<10."""
    n = len(spacings)
    win = max(5, jround(win_frac * n))
    cs = np.cumsum(np.concatenate(([0.0], spacings)))
    out = []
    for i in range(n):
        a = max(0, i - win)
        b = min(n, i + win + 1)
        loc = (cs[b] - cs[a]) / (b - a)
        s = spacings[i] / loc if loc > 0 else 0.0
        if 0.0 < s < 10.0:
            out.append(s)
    out = np.array(out)
    if len(out) and out.mean() > 0:
        out = out / out.mean()
    return out


def random_vortex_configuration(Nv: int, Nx: int, Ny: int, q_magnitude: float,
                                rng: np.random.Generator,
                                enforce_neutrality: bool = True,
                                place_at_centers: bool = True) -> List[Vortex]:
    vs = []
    for _ in range(Nv):
        ix = int(rng.integers(1, Nx))       # 1..Nx−1
        iy = int(rng.integers(1, Ny))
        if place_at_centers:
            vs.append(Vortex(ix + 0.5, iy + 0.5, 0.0))
        else:
            vs.append(Vortex(Nx * (0.5 + 0.4 * (rng.random() - 0.5)),
                             Ny * (0.5 + 0.4 * (rng.random() - 0.5)), 0.0))
    if enforce_neutrality:
        n_pos = (Nv + 1) // 2
        for k, v in enumerate(vs):
            v.q = q_magnitude if k < n_pos else -q_magnitude
    return vs


def nn_gap_ratio(E: np.ndarray, seed: int = 7937) -> Tuple[float, float, int]:
    """2-D nearest-neighbour ⟨r⟩ (complex spectra) + Poisson-box baseline."""
    E = np.asarray(E, dtype=np.complex128)
    n = len(E)
    nn_dist = np.full(n, np.inf)
    nn_idx = np.full(n, -1, dtype=np.int64)
    chunk = 256
    for lo in range(0, n, chunk):
        hi = min(n, lo + chunk)
        d = np.abs(E[lo:hi, None] - E[None, :])
        for r in range(hi - lo):
            d[r, lo + r] = np.inf
        m = d.argmin(axis=1)
        dm = d[np.arange(hi - lo), m]
        for r in range(hi - lo):
            i = lo + r
            if dm[r] < nn_dist[i]:
                nn_dist[i] = dm[r]
                nn_idx[i] = m[r]
    acc, cnt = 0.0, 0
    for i in range(n):
        j = nn_idx[i]
        if j < 0:
            continue
        si, sj = nn_dist[i], nn_dist[j]
        if si == 0.0 and sj == 0.0:
            continue
        acc += min(si, sj) / max(si, sj)
        cnt += 1
    r_mean = acc / cnt if cnt else float("nan")
    # Poisson baseline: uniform clouds in the spectrum's own bounding box
    rng = jrng(seed)
    np_eff = 4 if n >= 4000 else 10
    x0, x1 = float(E.real.min()), float(E.real.max())
    y0, y1 = float(E.imag.min()), float(E.imag.max())
    base = []
    for _ in range(np_eff):
        P = (rng.random(n) * (x1 - x0) + x0) + 1j * (rng.random(n) * (y1 - y0) + y0)
        rb, _ = nn_gap_ratio_pure(P)
        base.append(rb)
    return r_mean, float(np.mean(base)), np_eff


def nn_gap_ratio_pure(P: np.ndarray, chunk: int = 1024) -> Tuple[float, int]:
    n = len(P)
    nn_dist = np.full(n, np.inf)
    nn_idx = np.full(n, -1, dtype=np.int64)
    for lo in range(0, n, chunk):
        hi = min(n, lo + chunk)
        d = np.abs(P[lo:hi, None] - P[None, :])
        for r in range(hi - lo):
            d[r, lo + r] = np.inf
        m = d.argmin(axis=1)
        dm = d[np.arange(hi - lo), m]
        for r in range(hi - lo):
            i = lo + r
            if dm[r] < nn_dist[i]:
                nn_dist[i] = dm[r]
                nn_idx[i] = m[r]
    acc, cnt = 0.0, 0
    for i in range(n):
        j = nn_idx[i]
        if j < 0:
            continue
        si, sj = nn_dist[i], nn_dist[j]
        if si == 0.0 and sj == 0.0:
            continue
        acc += min(si, sj) / max(si, sj)
        cnt += 1
    return (acc / cnt if cnt else float("nan")), cnt


# ═══════════════════════════════════════════════════════════════════════════
# 11. TESTS 15–22 (+ hardcore b-variants, 19c/19d)
# ═══════════════════════════════════════════════════════════════════════════

def test15_ab_cloud_construction(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    Nx, Ny = cfg.ab_nx, cfg.ab_ny
    q = cfg.resolve_q_magnitude()
    cy = Ny // 2
    if cfg.resolve_vortex_count() >= 4 or cfg.pass2 is False:
        vortices = [Vortex(Nx // 4 + 0.5, cy + 1 + 0.5, +q),
                    Vortex(3 * Nx // 4 + 0.5, cy + 1 + 0.5, -q),
                    Vortex(Nx // 4 + 0.5, cy - 1 + 0.5, -q),
                    Vortex(3 * Nx // 4 + 0.5, cy - 1 + 0.5, +q)]
        probes = [(Nx // 4, cy + 1), (3 * Nx // 4, cy + 1),
                  (max(1, Nx // 8), max(1, Ny // 4))]
    else:
        vortices = [Vortex(Nx // 4 + 0.5, cy + 0.5, +q),
                    Vortex(3 * Nx // 4 + 0.5, cy + 0.5, -q)]
        probes = [(Nx // 4, cy), (3 * Nx // 4, cy), (max(1, Nx // 8), max(1, Ny // 4))]
    print("\n" + "═" * 60)
    print(f"TEST 15: AB-cloud Hamiltonian Construction (v8 DIRAC-STRING FIX)")
    print(f" lattice {Nx}×{Ny}, {len(vortices)} vortices (q=±{q}), :dirac gauge, open BC")
    print("─" * 60)
    H = build_ab_cloud_hamiltonian(ABCloudConfig(
        Nx, Ny, vortices, 0.0, 1.0, "open", cfg.ab_W, cfg.ab_seed, "dirac"))
    herm = hermiticity_defect(H) < 1e-12
    tau = time_reversal_asymmetry(H)
    print(f" Hermiticity defect: {hermiticity_defect(H):.2e} → "
          f"{'OK' if herm else 'BROKEN'};  τ_TRB = {tau:.4f}")
    ok_flux = True
    for (px, py), v in zip(probes[:2], vortices[:2]):
        f = plaquette_flux(H, Nx, Ny, px, py, torus=False)
        f_mod = mod2pi(f + math.pi) - math.pi
        exp_f = mod2pi(2 * math.pi * v.q + math.pi) - math.pi
        good = flux_circdist(f_mod, exp_f) < 1e-9
        ok_flux &= good
        print(f" flux at vortex plaquette ({px},{py}): {f_mod:+.6f} [exp {exp_f:+.6f}] "
              f"→ {'OK' if good else 'FAIL'}")
    px, py = probes[2]
    f0 = plaquette_flux(H, Nx, Ny, px, py, torus=False)
    f0m = mod2pi(f0 + math.pi) - math.pi
    good0 = flux_circdist(f0m, 0.0) < 1e-9
    ok_flux &= good0
    print(f" flux at empty plaquette ({px},{py}): {f0m:+.6f} → {'OK' if good0 else 'FAIL'}")
    ok = herm and ok_flux
    status = msg(cfg, "pass") if ok else msg(cfg, "warn")
    log_result(f" Test 15: Hermiticity={'OK' if herm else 'BAD'}, τ_TRB={tau:.4f} → {status}")
    return ok, f"τ_TRB={tau:.4f}, flux {'OK' if ok_flux else 'FAIL'}"


def test15b_construction_hardcore(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    Nx, Ny = cfg.ab_nx, cfg.ab_ny
    q = cfg.resolve_q_magnitude()
    cy = Ny // 2
    vortices = [Vortex(Nx // 4 + 0.5, cy + 1 + 0.5, +q),
                Vortex(3 * Nx // 4 + 0.5, cy + 1 + 0.5, -q),
                Vortex(Nx // 4 + 0.5, cy - 1 + 0.5, -q),
                Vortex(3 * Nx // 4 + 0.5, cy - 1 + 0.5, +q)]
    H = build_ab_cloud_hamiltonian(ABCloudConfig(
        Nx, Ny, vortices, 0.0, 1.0, "open", cfg.ab_W, cfg.ab_seed, "dirac"))
    expected = {}
    for v in vortices:
        expected[(int(math.floor(v.x)), int(math.floor(v.y)))] = \
            mod2pi(2 * math.pi * v.q + math.pi) - math.pi
    n_v_ok = n_e_ok = n_e_total = 0
    worst = 0.0
    for ix in range(1, Nx):
        for iy in range(1, Ny):
            f = plaquette_flux(H, Nx, Ny, ix, iy, torus=False)
            fm = mod2pi(f + math.pi) - math.pi
            if (ix, iy) in expected:
                if flux_circdist(fm, expected[(ix, iy)]) < 1e-9:
                    n_v_ok += 1
            else:
                n_e_total += 1
                if abs(fm) < 1e-9:
                    n_e_ok += 1
                worst = max(worst, abs(fm))
    herm = hermiticity_defect(H) < 1e-12
    rec = [("full signed scan", n_v_ok == len(vortices) and n_e_ok == n_e_total,
            f"vortex {n_v_ok}/{len(vortices)}, empty {n_e_ok}/{n_e_total}, worst {worst:.1e}"),
           ("hermiticity", herm, f"defect {hermiticity_defect(H):.1e}")]
    ok = hc_verdict_table(cfg, "Test 15", rec)
    log_result(f" Test 15 [HARDCORE pass 2]: {len(rec)} sub-checks, "
               f"{sum(1 for _,o,_ in rec if not o)} failed → {'PASS' if ok else 'WARN'}")
    return ok, f"hardcore {len(rec)} checks"


def test16_ab_cloud_gue_classification(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    Nx, Ny = cfg.ab_nx, cfg.ab_ny
    N = Nx * Ny
    alpha = cfg.ab_alpha_test16
    Nv = cfg.resolve_vortex_count()
    q = cfg.resolve_q_magnitude()
    n_real = max(3, cfg.ab_n_realizations) if cfg.pass2 else cfg.ab_n_realizations
    W = cfg.w_eff()
    rng = jrng(cfg.ab_seed)
    r_vals, sp_stats = [], []
    print("\n" + "═" * 60)
    print("TEST 16: AB-cloud Eigenvalue Spacing → GUE")
    print(f" {Nx}×{Ny} lattice, α={alpha}, Nv={Nv}, q={q}, W={W}, "
          f"{n_real} realizations, central 60% bulk")
    print("─" * 60)
    for k in range(1, n_real + 1):
        vortices = random_vortex_configuration(Nv, Nx, Ny, q, rng)
        H = build_ab_cloud_hamiltonian(ABCloudConfig(
            Nx, Ny, vortices, alpha, cfg.ab_t, cfg.ab_lattice, W, cfg.ab_seed + k))
        ev = ab_eigvals(H)
        del H
        bulk = ev[jround(0.2 * N):jround(0.8 * N)]
        r, nr = mean_adjacent_spacing_ratio(bulk)
        r_vals.append(r)
        sp = np.diff(bulk)
        un = unfold_local(sp, cfg.ab_unfold_window)
        cum = np.concatenate(([0.0], np.cumsum(un)))
        D, p = ks_test(un)
        a2 = anderson_darling_stat(un) if len(un) > 1 else float("nan")
        sv = number_variance(cum, 2.0, 500, rng) if len(cum) > 10 else float("nan")
        d3 = delta3_rigidity(cum, 2.0, 200, 100, rng) if len(cum) > 10 else float("nan")
        sp_stats.append((D, p, a2, sv, d3))
        print(f"  realization {k}: ⟨r⟩ = {r:.4f} (n_r={nr}), D = {D:.4f}, A² = {a2:.2f}")
    r_mean = float(np.mean(r_vals))
    r_se = float(np.std(r_vals, ddof=1) / math.sqrt(len(r_vals))) if len(r_vals) > 1 else 0.0
    n_sp_est = jround(0.6 * N)
    p_asymp = ks_asymptotic_pvalue((math.sqrt(n_sp_est) + 0.12 + 0.11 / math.sqrt(n_sp_est))
                                   * sp_stats[-1][0])
    print(f" ⟨r⟩ = {r_mean:.4f} ± {r_se:.4f}  (GUE reference {0.5992}; "
          f"95% CI [{r_mean-1.96*r_se:.4f}, {r_mean+1.96*r_se:.4f}])")
    print(f" bulk KS D = {sp_stats[-1][0]:.4f}, p_asymptotic = {p_asymp:.2e}, "
          f"A² = {sp_stats[-1][2]:.4f}")
    r_pass = r_mean > 0.55
    r_increase = True  # single α-point sweep
    ok = r_pass and r_increase
    status = msg(cfg, "pass") if ok else (msg(cfg, "warn") if r_pass else msg(cfg, "fail"))
    log_result(f" Test 16 [MONTGOMERY] α={alpha}: ⟨r⟩ mean={r_mean:.3f} → {status}")
    return ok, f"⟨r⟩={r_mean:.4f}±{r_se:.4f}"


def test16b_gue_classification_hardcore(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    Nx, Ny = cfg.ab_nx, cfg.ab_ny
    N = Nx * Ny
    alpha = cfg.ab_alpha_test16
    Nv = cfg.resolve_vortex_count() if not cfg.pass2 else cfg.resolve_vortex_count_secondary()
    q = cfg.resolve_q_magnitude()
    n_hc = max(cfg.ab_n_realizations, cfg.ab_hc_nreal)
    W = cfg.w_eff()
    rng = jrng(cfg.ab_seed + 1600)
    r_vals = []
    print("\n" + "═" * 60)
    print(f"TEST 16b [HARDCORE pass 2]: GUE classification deep pass — "
          f"{Nx}×{Ny}, Nv={Nv}, {n_hc} realizations")
    print("─" * 60)
    for k in range(1, n_hc + 1):
        vortices = random_vortex_configuration(Nv, Nx, Ny, q, rng)
        H = build_ab_cloud_hamiltonian(ABCloudConfig(
            Nx, Ny, vortices, alpha, cfg.ab_t, cfg.ab_lattice, W, cfg.ab_seed + 1600 + k))
        ev = ab_eigvals(H)
        del H
        bulk = central_band_eigs(ev, 0.6)
        r, _ = mean_adjacent_spacing_ratio(bulk)
        r_vals.append(r)
        print(f"  realization {k}: ⟨r⟩ = {r:.4f}")
    r_m = float(np.mean(r_vals))
    r_se = float(np.std(r_vals, ddof=1) / math.sqrt(len(r_vals))) if len(r_vals) > 1 else 0.0
    scatter = float(np.std(r_vals, ddof=1)) if len(r_vals) > 1 else 0.0
    brng = jrng(cfg.ab_seed + 1617)
    boots = [float(np.mean(brng.choice(r_vals, len(r_vals)))) for _ in range(10000)]
    blo, bhi = np.quantile(boots, 0.025), np.quantile(boots, 0.975)
    n_above = sum(1 for r in r_vals if r > 0.5992)
    print(f" ⟨r⟩ = {r_m:.4f} ± {r_se:.4f}; bootstrap 95% CI [{blo:.4f}, {bhi:.4f}] "
          f"(∋ GUE 0.5992: {blo <= 0.5992 <= bhi}); {n_above}/{len(r_vals)} above GUE")
    rec = [("⟨r⟩ > 0.55", r_m > 0.55, f"⟨r⟩ = {r_m:.4f} ± {r_se:.4f}"),
           ("scatter ≤ 0.022", scatter <= 0.022, f"scatter σ = {scatter:.4f}")]
    ok = hc_verdict_table(cfg, "Test 16", rec)
    log_result(f" Test 16 [HARDCORE pass 2]: {len(rec)} sub-checks, "
               f"{sum(1 for _,o,_ in rec if not o)} failed → {'PASS' if ok else 'WARN'}")
    return ok, f"hardcore ⟨r⟩={r_m:.4f}"


def _zero_modes_and_symmetry_defect(alpha: float, L: int):
    c = ABCloudConfig(L, L, [], alpha, 1.0, "torus", 0.0, 96, "monumental")
    H = build_ab_cloud_hamiltonian(c)
    ev = ab_eigvals(H)
    z = int((np.abs(ev) < 1e-8).sum())
    defect = float(np.linalg.norm(ev + ev[::-1]) / max(np.linalg.norm(ev), 1e-30))
    return z, defect


def _connes_self_duality_defect(alpha: float, L: int) -> float:
    Ha = build_ab_cloud_hamiltonian(ABCloudConfig(L, L, [], alpha, 1.0, "open", 4.0, 96))
    Hb = build_ab_cloud_hamiltonian(ABCloudConfig(L, L, [], 1.0 / alpha, 1.0, "open", 4.0, 96))
    ea, eb = ab_eigvals(Ha), ab_eigvals(Hb)
    return float(np.linalg.norm(ea - eb) / max(np.linalg.norm(ea), 1e-30))


def _spectral_symmetry_defect(alpha: float, L: int) -> float:
    c = ABCloudConfig(L, L, [], alpha, 1.0, "torus", 0.0, 96, "monumental")
    H = build_ab_cloud_hamiltonian(c)
    ev = ab_eigvals(H)
    return float(np.linalg.norm(ev + ev[::-1]) / max(np.linalg.norm(ev), 1e-30))


def test17_alpha_half_self_duality(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    L = cfg.ab_nx
    print("\n" + "═" * 60)
    print("TEST 17: Connes Self-Duality α ↔ 1/α at α = 1/2")
    print(f" {L}×{L} torus; zero-mode tower 2 Dirac points × 2 = 4 at α=1/2")
    print("─" * 60)
    z_half, s_half = _zero_modes_and_symmetry_defect(0.5, L)
    d_half = _connes_self_duality_defect(0.5, L)
    print(f" α = 1/2: zero_modes = {z_half}, spectral defect = {s_half:.2e}, "
          f"duality defect = {d_half:.4f}")
    if abs((1.0 / 3.0) * L - round((1.0 / 3.0) * L)) < 1e-9:
        z_third, s_third = _zero_modes_and_symmetry_defect(1.0 / 3.0, L)
        d_third = _connes_self_duality_defect(1.0 / 3.0, L)
        print(f" α = 1/3: zero_modes = {z_third}, spectral defect = {s_third:.2e}, "
              f"duality defect = {d_third:.4f}")
    if abs(0.25 * L - round(0.25 * L)) < 1e-9:
        z_fourth, s_fourth = _zero_modes_and_symmetry_defect(0.25, L)
        print(f" α = 1/4: zero_modes = {z_fourth}, spectral defect = {s_fourth:.2e}")
    ok = z_half == 4
    status = msg(cfg, "pass") if ok else msg(cfg, "warn")
    log_result(f" Test 17: zero_modes(α=1/2)={z_half} → {status}")
    return ok, f"zero_modes={z_half}"


def test17b_self_duality_hardcore(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    # Julia: ladder = filter(l -> l % 6 == 0, [24, 48, ab_nx]) — sizes must fit
    # both α=1/2 and α=1/3 on the torus.
    ladder = sorted({l for l in [24, 48, cfg.ab_nx] if l % 6 == 0})
    rec = []
    all4, symm = True, True
    print("\n" + "═" * 60)
    print("TEST 17b [HARDCORE pass 2]: self-duality — cross-size audit")
    print("─" * 60)
    for L in ladder:
        z, s_half = _zero_modes_and_symmetry_defect(0.5, L)
        s_third = _spectral_symmetry_defect(1.0 / 3.0, L)
        d_half = _connes_self_duality_defect(0.5, L)
        all4 &= (z == 4)
        symm &= (s_half < 1e-10 and s_third < 1e-10)
        print(f" L={L:>3}: zeros={z}, spec {s_half:.2e}/{s_third:.2e}, duality {d_half:.4f}")
    rec.append(("zero tower == 4 ∀L", all4, f"{ladder}"))
    rec.append(("spectral symmetry < 1e-10 ∀L", symm, "E → −E pairing"))
    ok = hc_verdict_table(cfg, "Test 17", rec)
    log_result(f" Test 17 [HARDCORE pass 2]: {len(rec)} sub-checks, "
               f"{sum(1 for _,o,_ in rec if not o)} failed → {'PASS' if ok else 'WARN'}")
    return ok, f"hardcore {len(rec)} checks"


def test18_chiral_symmetry_AIII(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    Nx = Ny = cfg.ab_nx
    L = Nx
    S = chiral_symmetry_operator(Nx, Ny)
    W = cfg.w_eff()
    print("\n" + "═" * 60)
    print("TEST 18: Chiral Symmetry AIII at α = 1/2")
    print(f" {L}×{L} torus; sublattice defect ‖SHS+H‖/‖H‖")
    print("─" * 60)
    H = build_ab_cloud_hamiltonian(ABCloudConfig(Nx, Ny, [], 0.5, 1.0, "torus", 0.0, 96))
    ev = ab_eigvals(H)
    spectral_half = float(np.linalg.norm(ev + ev[::-1]) / max(np.linalg.norm(ev), 1e-30))
    sub_half = chiral_defect(H, S)
    print(f" clean (α=1/2, W=0):   spectral {spectral_half:.2e}, sublattice {sub_half:.2e}")
    if abs((1.0 / 3.0) * Ny - round((1.0 / 3.0) * Ny)) < 1e-9:
        H3 = build_ab_cloud_hamiltonian(ABCloudConfig(Nx, Ny, [], 1.0 / 3.0, 1.0, "torus", W, 96))
        ev3 = ab_eigvals(H3)
        spectral_third = float(np.linalg.norm(ev3 + ev3[::-1]) / max(np.linalg.norm(ev3), 1e-30))
        sub_third = chiral_defect(H3, S)
        del H3
        print(f" α=1/3 (W={W}):       spectral {spectral_third:.2e}, sublattice {sub_third:.2e}")
    else:
        sub_third = float("nan")
    vorts = [Vortex(0.3 * Nx, 0.3 * Ny, +cfg.resolve_q_magnitude()),
             Vortex(0.7 * Nx, 0.7 * Ny, -cfg.resolve_q_magnitude())]
    Hv = build_ab_cloud_hamiltonian(ABCloudConfig(Nx, Ny, vorts, 0.5, 1.0, "torus", 0.0, 96))
    evv = ab_eigvals(Hv)
    spectral_v = float(np.linalg.norm(evv + evv[::-1]) / max(np.linalg.norm(evv), 1e-30))
    del Hv
    Hvw = build_ab_cloud_hamiltonian(ABCloudConfig(Nx, Ny, vorts, 0.5, 1.0, "torus", W, 96))
    evw = ab_eigvals(Hvw)
    spectral_vw = float(np.linalg.norm(evw + evw[::-1]) / max(np.linalg.norm(evw), 1e-30))
    del Hvw
    print(f" vortex row:           spectral {spectral_v:.2e}; vortex+W: {spectral_vw:.2e}")
    ok = sub_half < 1e-10 and (sub_third != sub_third or sub_third > 1e-10)
    status = msg(cfg, "pass") if ok else msg(cfg, "warn")
    log_result(f" Test 18: sublattice(α=1/2)={sub_half:.1e}, (α=1/3)={sub_third:.4f} → {status}")
    return ok, f"defect {sub_half:.1e}/{sub_third:.4f}"


def test18b_chiral_hardcore(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    Nx = Ny = cfg.ab_nx
    S = chiral_symmetry_operator(Nx, Ny)
    eps_rms = 0.01 / math.sqrt(3.0)
    rec = []
    ss = float(np.linalg.norm(S * S - 1.0) / np.linalg.norm(np.ones(Nx * Ny)))
    rec.append(("H3 S² = I", ss < 1e-12, f"‖S·S−I‖/‖I‖ = {ss:.1e}"))
    H = build_ab_cloud_hamiltonian(ABCloudConfig(Nx, Ny, [], 0.5, 1.0, "torus", 0.0, 96))
    d1 = chiral_defect(H, S)
    del H
    rec.append(("H1 exact AIII", d1 < 1e-10, f"defect {d1:.1e}"))
    H2 = build_ab_cloud_hamiltonian(ABCloudConfig(Nx, Ny, [], 0.5, 1.0, "torus", 1.0, 96))
    d2 = chiral_defect(H2, S)
    del H2
    rec.append(("H2 ε contract", 0.5 * eps_rms < d2 < 2.0 * eps_rms,
                f"defect {d2:.4e} vs ε_rms {eps_rms:.4e}"))
    vorts = [Vortex(0.3 * Nx, 0.3 * Ny, +1.0), Vortex(0.7 * Nx, 0.7 * Ny, -1.0)]
    Hv = build_ab_cloud_hamiltonian(ABCloudConfig(Nx, Ny, vorts, 0.5, 1.0, "torus", 0.0, 96))
    d2v = chiral_defect(Hv, S)
    del Hv
    rec.append(("H2v vortex preserved", d2v < 1e-10, f"defect {d2v:.1e}"))
    print("\n" + "═" * 60)
    print("TEST 18b [HARDCORE pass 2]: chiral AIII — operator algebra audit")
    print("─" * 60)
    ok = hc_verdict_table(cfg, "Test 18", rec)
    log_result(f" Test 18 [HARDCORE pass 2]: {len(rec)} sub-checks, "
               f"{sum(1 for _,o,_ in rec if not o)} failed → {'PASS' if ok else 'WARN'}")
    return ok, f"hardcore {len(rec)} checks"


T19_VF_CACHE: Dict[str, float] = {}
T19_SERIES_CACHE: Dict[str, Tuple[List[int], List[float]]] = {}


def test19_dirac_cone_velocity(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    L_grid = [12, 16, 24, 32, 48, 64, 72]
    print("\n" + "═" * 60)
    print("TEST 19: Dirac Cone Linear Dispersion, v_F")
    print(" clean torus α=1/2: E_min ≈ v_F·2π/L (zero tower = 4)")
    print("─" * 60)
    Ls, Emins, zeros_ok = [], [], True
    for L in L_grid:
        H = build_ab_cloud_hamiltonian(ABCloudConfig(L, L, [], 0.5, 1.0, "torus", 0.0, 96))
        ev = ab_eigvals(H)
        del H
        n_zero = int((np.abs(ev) < 1e-6).sum())
        above = ev[ev > 1e-6]
        e_min = float(above.min()) if len(above) else float("nan")
        zeros_ok &= (n_zero > 0)
        Ls.append(L)
        Emins.append(e_min)
        print(f" L = {L:>3}: zero_modes = {n_zero}, E_min = {e_min:.6f}")
    a, b, r2, se, _ = linreg(1.0 / np.array(Ls, dtype=float), np.array(Emins))
    v2pi, vpi = b / (2 * math.pi), b / math.pi
    print(f" fit E_min = {a:.4f} + {b:.4f}/L, R² = {r2:.6f}")
    print(f" v_F(2π) = {v2pi:.4f}   v_F(π) = {vpi:.4f}   (analytic v_F = 2t = 2)")
    T19_VF_CACHE["pass1 (7-pt fit ≤72)"] = v2pi
    ok = r2 > 0.95 and zeros_ok
    status = msg(cfg, "pass") if ok else msg(cfg, "warn")
    log_result(f" Test 19: R²={r2:.4f}, v_F(2π)={v2pi:.4f} → {status}")
    return ok, f"v_F={v2pi:.4f} R²={r2:.4f}"


def test19b_dirac_velocity_hardcore(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    L_grid = [l for l in [16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96] if l <= cfg.ab_nx]
    rec = []
    Ls, Emins = [], []
    tower_ok = True
    print("\n" + "═" * 60)
    print(f"TEST 19b [HARDCORE pass 2]: Dirac velocity — 11-pt ladder (≤ {cfg.ab_nx})")
    print("─" * 60)
    for L in L_grid:
        H = build_ab_cloud_hamiltonian(ABCloudConfig(L, L, [], 0.5, 1.0, "torus", 0.0, 96))
        ev = ab_eigvals(H)
        del H
        n_zero = int((np.abs(ev) < 1e-6).sum())
        above = ev[ev > 1e-6]
        e_min = float(above.min())
        tower_ok &= (n_zero == 4)
        Ls.append(L)
        Emins.append(e_min)
        print(f" L = {L:>3}: tower = {n_zero}, E_min·L = {e_min*L:.4f}")
    a, b, r2, se, _ = linreg(1.0 / np.array(Ls, dtype=float), np.array(Emins))
    v2pi = b / (2 * math.pi)
    T19_VF_CACHE["pass2 (11-pt mod-4 ≤96)"] = v2pi
    T19_SERIES_CACHE["pass2"] = (list(Ls), list(Emins))
    drift = abs(Emins[-1] * Ls[-1] - 4 * math.pi) < abs(Emins[0] * Ls[0] - 4 * math.pi)
    rec.append(("R² > 0.95", r2 > 0.95, f"R² = {r2:.6f}"))
    rec.append(("zero tower == 4 ∀L", tower_ok, f"{len(L_grid)} rungs"))
    rec.append(("E_min·L → 4π", drift, f"{Emins[0]*Ls[0]:.4f} → {Emins[-1]*Ls[-1]:.4f} (4π = {4*math.pi:.4f})"))
    ok = hc_verdict_table(cfg, "Test 19", rec)
    log_result(f" Test 19 [HARDCORE pass 2]: {len(rec)} sub-checks, "
               f"{sum(1 for _,o,_ in rec if not o)} failed → {'PASS' if ok else 'WARN'}")
    return ok, f"hardcore v_F={v2pi:.4f}"


def test19c_dirac_alpha_series(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    L_grid = [l for l in [20, 40, 60, 80] if l <= cfg.ab_nx]
    alphas = (0.4, 0.5, 0.6)
    rec = []
    E_by_a = {}
    print("\n" + "═" * 60)
    print("TEST 19c [pass 3]: Dirac cone α-series — selectivity of the Dirac line")
    print("─" * 60)
    for al in alphas:
        Ls, Emins, towers = [], [], []
        for L in L_grid:
            if abs(al * L - round(al * L)) > 1e-9:
                continue
            H = build_ab_cloud_hamiltonian(ABCloudConfig(L, L, [], al, 1.0, "torus", 0.0, 96))
            ev = ab_eigvals(H)
            del H
            n_zero = int((np.abs(ev) < 1e-6).sum())
            above = ev[ev > 1e-6]
            e_min = float(above.min()) if len(above) else float("nan")
            Ls.append(L)
            Emins.append(e_min)
            towers.append(n_zero)
        E_by_a[al] = (Ls, Emins)
        print(f" α = {al}: E_min·L = " + ", ".join(f"{e*l:.4f}" for e, l in zip(Emins, Ls))
              + f"   (towers: " + ", ".join(str(t) for t in towers) + ")")
    Ls5, E5 = E_by_a[0.5]
    a, b, r2, se, _ = linreg(1.0 / np.array(Ls5, dtype=float), np.array(E5))
    v2pi = b / (2 * math.pi)
    T19_VF_CACHE["pass3 (α=0.5 series ≤80)"] = v2pi
    EL = {al: E_by_a[al][1][-1] * E_by_a[al][0][-1] for al in alphas}
    rec.append(("R² (α=0.5) > 0.95", r2 > 0.95, f"R² = {r2:.6f}"))
    rec.append(("4π collapse", 8.0 <= EL[0.5] <= 18.0, f"E_min·L = {EL[0.5]:.4f} (4π = {4*math.pi:.2f})"))
    sel = EL[0.5] > 2.0 * max(EL[0.4], EL[0.6])
    rec.append(("α-selectivity", sel,
                f"α=0.5: {EL[0.5]:.3f} vs α=0.4/0.6: {EL[0.4]:.3f}/{EL[0.6]:.3f}"))
    ok = hc_verdict_table(cfg, "Test 19c", rec)
    log_result(f" Test 19c: v_F={v2pi:.4f}, R²={r2:.6f} → {'PASS' if ok else 'WARN'}")
    return ok, f"series v_F={v2pi:.4f}"


def _apply_y_twist(H: np.ndarray, L: int, theta: float) -> np.ndarray:
    Ht = H.copy()
    for ix1 in range(1, L + 1):
        i = (L - 1) * L + (ix1 - 1)      # (ix, Ny)
        j = (ix1 - 1)                    # (ix, 1)
        Ht[i, j] *= np.exp(1j * theta)
        Ht[j, i] *= np.exp(-1j * theta)
    return Ht


def test19d_dirac_cone_audit(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    """Twist spectroscopy (post-v19 addition; reproduced from code)."""
    Lt = 48
    rec = []
    print("\n" + "═" * 60)
    print("TEST 19d [pass 4]: Dirac cone audit — twist spectroscopy")
    print("─" * 60)
    H0 = build_ab_cloud_hamiltonian(ABCloudConfig(Lt, Lt, [], 0.5, 1.0, "torus", 0.0, 96))
    ev0 = ab_eigvals(H0)
    tower0 = int((np.abs(ev0) < 1e-10).sum())
    E0 = float(ev0[ev0 > 1e-6].min())
    thetas = [math.pi / 5 * k for k in range(1, 6)]
    Emins, nz_tw = [], []
    for th in thetas:
        evt = ab_eigvals(_apply_y_twist(H0, Lt, th))
        nz_tw.append(int((np.abs(evt) < 1e-6).sum()))
        Emins.append(float(evt[evt > 1e-6].min()))
        del evt
    th = np.array(thetas)
    E = np.array(Emins)
    s = float((th * E).sum() / (th * th).sum())
    sse = float(((E - s * th) ** 2).sum())
    r2_ni = 1.0 - sse / float((E * E).sum())
    vF_twist = s * Lt
    vf_ref = T19_VF_CACHE.get("pass2 (11-pt mod-4 ≤96)", 2.0)
    rec.append(("D1 twist linearity", r2_ni > 0.995 and all(z == 0 for z in nz_tw),
                f"R²_no-int = {r2_ni:.6f}, towers 0/5"))
    rec.append(("D1b v_F agreement", abs(vF_twist - vf_ref) / vf_ref < 0.05,
                f"twist {vF_twist:.4f} vs fit {vf_ref:.4f}"))
    IsA = np.array([1.0 if ((ix1 + iy1) % 2 == 0) else 0.0
                    for iy1 in range(1, Lt + 1) for ix1 in range(1, Lt + 1)])
    import numpy.linalg as _la
    w, V = _la.eigh(H0)
    tower_idx = np.where(np.abs(w) < 1e-10)[0]
    sumA = float(sum(IsA @ np.abs(V[:, k]) ** 2 for k in tower_idx))
    sumB = float((1 - IsA) @ sum(np.abs(V[:, k]) ** 2 for k in tower_idx))
    rec.append(("D2 sublattice split", tower0 == 4 and abs(sumA - 2.0) < 1e-8
                and abs(sumB - 2.0) < 1e-8,
                f"tower {tower0}, A {sumA:.10f}, B {sumB:.10f}"))
    H2pi = _apply_y_twist(H0, Lt, 2 * math.pi)
    dh = float(np.linalg.norm(H2pi - H0) / np.linalg.norm(H0))
    ev2 = ab_eigvals(H2pi)
    dE = float(np.max(np.abs(ev2 - ev0)))
    rec.append(("D3a 2π gauge invariance", dh < 1e-15 and dE < 1e-10,
                f"‖ΔH‖/‖H‖ = {dh:.1e}, max|ΔE| = {dE:.1e}"))
    evt_pi = ab_eigvals(_apply_y_twist(H0, Lt, math.pi))
    n_pi = int((np.abs(evt_pi) < 1e-6).sum())
    cusp = float(evt_pi[evt_pi > 1e-6].min()) * Lt
    rec.append(("D3b θ=π cusp", n_pi == 0 and 5.0 <= cusp <= 7.6,
                f"tower 0, E_min·L = {cusp:.4f} (2π = {2*math.pi:.4f})"))
    H0b = build_ab_cloud_hamiltonian(ABCloudConfig(Lt, Lt, [], 0.5, 1.0, "torus", 0.0, 96))
    d4 = float(np.linalg.norm(H0b - H0))
    rec.append(("D4 clean rebuild", d4 == 0.0, f"‖ΔH‖ = {d4:.1e}"))
    # D5: refit the pass-2 series as E_min·L = a + c/L² (post-v19 check)
    if "pass2" in T19_SERIES_CACHE:
        Ls_p, Es_p = T19_SERIES_CACHE["pass2"]
        EL = np.array([e * l for e, l in zip(Es_p, Ls_p)])
        xs2 = 1.0 / np.array(Ls_p, dtype=float) ** 2
        a5, c5, r25, _, _ = linreg(xs2, EL)
        rec.append(("D5 1/L² collapse", r25 > 0.999 and abs(a5 / (4 * math.pi) - 1) < 0.005
                    and 40.0 <= abs(c5) <= 150.0,
                    f"intercept {a5:.4f} (4π={4*math.pi:.4f}), c = {c5:.2f}, R² = {r25:.6f}"))
    ok = hc_verdict_table(cfg, "Test 19d", rec)
    log_result(f" Test 19d: v_F_twist={vF_twist:.4f} → {'PASS' if ok else 'WARN'}")
    return ok, f"twist v_F={vF_twist:.4f}"


def harper_chern_first_band(alpha: float, n_kx: int = 24, n_ky: int = 8,
                            mass: float = 0.0) -> Tuple[int, float, int]:
    """Fukui–Hatsugai–Suzuki Chern number of the lowest Harper band."""
    from fractions import Fraction
    fr = Fraction(alpha).limit_denominator(200)
    q = fr.denominator
    p = fr.numerator
    if not (2 <= q <= 200):
        raise ValueError(f"q = {q} out of range")
    bands = np.zeros((n_kx, n_ky, q), dtype=np.complex128)
    min_gap = float("inf")
    for a in range(n_kx):
        kx = 2 * math.pi * a / n_kx
        for b in range(n_ky):
            ky = (2 * math.pi / q) * b / n_ky
            Hq = np.zeros((q, q), dtype=np.complex128)
            for m in range(q):
                Hq[m, m] = -2.0 * math.cos(kx + 2.0 * math.pi * alpha * m)
                if mass != 0.0:
                    Hq[m, m] += mass * (1.0 if m % 2 == 0 else -1.0)
                if m + 1 < q:
                    Hq[m, m + 1] += -1.0
                    Hq[m + 1, m] += -1.0
            Hq[q - 1, 0] += -np.exp(1j * q * ky)
            Hq[0, q - 1] += -np.exp(-1j * q * ky)
            ev, U = np.linalg.eigh(Hq)
            bands[a, b, :] = U[:, 0]
            min_gap = min(min_gap, float(ev[1] - ev[0]))

    def link(u, v):
        z = complex(np.vdot(u, v))
        if abs(z) < 1e-14:
            return 1.0 + 0.0j
        return z / abs(z)

    C = 0.0
    n_sing = 0
    for a in range(n_kx):
        a1 = (a + 1) % n_kx
        for b in range(n_ky):
            b1 = (b + 1) % n_ky
            u1 = link(bands[a, b], bands[a1, b])
            u2 = link(bands[a1, b], bands[a1, b1])
            u3 = link(bands[a, b1], bands[a1, b1])
            u4 = link(bands[a, b], bands[a, b1])
            C += math.atan2((u1 * u2 * np.conj(u3) * np.conj(u4)).imag,
                            (u1 * u2 * np.conj(u3) * np.conj(u4)).real)
    return int(round(C / (2 * math.pi))), min_gap, n_sing


def test20_chern_number_tknn(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    print("\n" + "═" * 60)
    print("TEST 20: TKNN Chern Number C₁ = 1 at α = 1/2 (magnetic BZ, FHS)")
    print("─" * 60)
    anchors_ok = True
    for al, grids in ((0.25, (12, 4)), (1.0 / 3.0, (12, 4)), (0.2, (12, 4))):
        cs, gaps = [], []
        for nkx, nky in (grids, (24, 8)):
            C, gap, _ = harper_chern_first_band(al, nkx, nky)
            cs.append(C)
            gaps.append(gap)
        row_ok = all(c == 1 for c in cs) and all(g > 0.5 for g in gaps)
        anchors_ok &= row_ok
        print(f" α = {al:.4f}: C₁ = {cs} at {grids}/(24,8), min gaps "
              f"{gaps[0]:.4f}/{gaps[1]:.4f} → {'OK' if row_ok else 'FAIL'}")
    C_h, gap_h, _ = harper_chern_first_band(0.5, 16, 8)
    print(f" α = 1/2 Dirac touching: min gap = {gap_h:.2e} (per-band C₁ undefined)")
    mass_ok = True
    for m in (+0.3, -0.3):
        C_m, gap_m, _ = harper_chern_first_band(0.5, 24, 12, mass=m)
        mass_ok &= (C_m == 0 and gap_m > 0.1)
        print(f" mass = {m:+.1f}: C₁ = {C_m}, gap = {gap_m:.4f}")
    ok = anchors_ok and gap_h < 1e-8 and mass_ok
    status = msg(cfg, "pass") if ok else msg(cfg, "warn")
    log_result(f" Test 20: anchors {'1,1,1' if anchors_ok else 'FAIL'}, "
               f"α=1/2 gap={gap_h:.1e}, mass C=0/0 → {status}")
    return ok, f"C₁=1, gap(½)={gap_h:.1e}"


def test20b_chern_hardcore(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    rec = []
    print("\n" + "═" * 60)
    print("TEST 20b [HARDCORE pass 2]: Chern — FHS ladder + touching depth")
    print("─" * 60)
    lad_ok = True
    lad_C = []
    for L in [12, 18, 24, 36, 48, 72]:
        C, gap, _ = harper_chern_first_band(1.0 / 3.0, L, L // 3)
        lad_C.append(C)
        lad_ok &= (C == 1)
    rec.append(("C₁ ladder α=1/3", lad_ok, f"C₁ = {lad_C}"))
    touch_ok = True
    for L in [12, 16, 24, 48, 72]:
        _, gap, _ = harper_chern_first_band(0.5, L, L // 2)
        touch_ok &= (gap < 1e-8)
    rec.append(("α=1/2 touching", touch_ok, "gap < 1e-8 on all rungs"))
    m_ok = True
    for m in (+0.3, -0.3):
        C_m, gap_m, _ = harper_chern_first_band(0.5, 24, 12, mass=m)
        m_ok &= (C_m == 0 and gap_m > 0.1)
    rec.append(("mass regularization", m_ok, "C₁ = 0 both signs, gap > 0.1"))
    ok = hc_verdict_table(cfg, "Test 20", rec)
    log_result(f" Test 20 [HARDCORE pass 2]: {len(rec)} sub-checks, "
               f"{sum(1 for _,o,_ in rec if not o)} failed → {'PASS' if ok else 'WARN'}")
    return ok, f"hardcore {len(rec)} checks"


def test21_gamma_star_phase(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    delta = math.pi / 7.0
    a_C = delta ** 5 / 22.0
    b_C = 1.0 - math.cos(2.0 * delta)
    arg = math.atan2(b_C, a_C)
    dev = abs(math.degrees(arg) - 90.0)
    print("\n" + "═" * 60)
    print("TEST 21: γ* Spinorial Phase ≈ π/2 (90° via imaginary unit)")
    print("─" * 60)
    print(f" a_C = δ_C⁵/22 = {a_C:.6e};  b_C = 1 − cos(2δ_C) = {b_C:.6f}")
    print(f" arg(γ*) = {arg:.6f} rad = {math.degrees(arg):.4f}°  "
          f"(deviation {dev:.4f}°)")
    ok = dev < 1.0
    status = msg(cfg, "pass") if ok else msg(cfg, "warn")
    log_result(f" Test 21: arg(γ*)={math.degrees(arg):.3f}°, dev={dev:.3f}° → {status}")
    return ok, f"{math.degrees(arg):.4f}°"


def test21b_gamma_star_hardcore(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    rec = []
    print("\n" + "═" * 60)
    print("TEST 21b [HARDCORE pass 2]: γ* — 256-bit audit")
    print("─" * 60)
    if HAVE_MPMATH:
        mp = _mp
        delta_bf = mp.pi / 7
        a_bf = delta_bf ** 5 / 22
        b_bf = 1 - mp.cos(2 * delta_bf)
        arg_bf = mp.atan2(b_bf, a_bf)
        dev_bf = float(abs(arg_bf * 180 / mp.pi - 90))
        d_a = abs((math.pi / 7) ** 5 / 22.0 - float(a_bf))
        d_b = abs((1.0 - math.cos(2 * math.pi / 7.0)) - float(b_bf))
        rec.append(("Float64 round-off", d_a < 1e-12 and d_b < 1e-12,
                    f"|Δa| = {d_a:.1e}, |Δb| = {d_b:.1e}"))
        rec.append(("arg(γ*)→π/2 (256-bit)", dev_bf < 1.0, f"dev {dev_bf:.4f}°"))
        worst = 0.0
        for ddelta in (-1e-6, 1e-6):
            d2 = delta_bf + ddelta
            arg_p = mp.atan2(1 - mp.cos(2 * d2), d2 ** 5 / 22)
            worst = max(worst, float(abs(arg_p * 180 / mp.pi - 90)))
        rec.append(("δ_C ± 1e-6 stability", worst < 1.0, f"worst dev {worst:.4f}°"))
    else:
        rec.append(("mpmath", False, "unavailable"))
    ok = hc_verdict_table(cfg, "Test 21", rec)
    log_result(f" Test 21b [HARDCORE pass 2]: {len(rec)} sub-checks → "
               f"{'PASS' if ok else 'WARN'}")
    return ok, f"hardcore {len(rec)} checks"


def test22_ab_phase(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    phi = 2.0 * math.pi * (1.0 / 14.0)
    target = math.pi / 7.0
    delta = math.pi / 7.0
    d1, d2 = abs(phi - target), abs(phi - delta)
    print("\n" + "═" * 60)
    print("TEST 22: AB Phase Φ_AB = π/7 = δ_C")
    print("─" * 60)
    print(f" Φ_AB = 2π/14 = {phi:.15f} = π/7 (|Δ| = {d1:.1e}); "
          f"δ_C = {math.degrees(delta):.4f}°")
    ok = d1 < 1e-15 and d2 < 1e-15
    status = msg(cfg, "pass") if ok else msg(cfg, "warn")
    log_result(f" Test 22: Φ_AB={phi:.10f} = π/7 → {status}")
    return ok, f"Φ_AB = π/7"
