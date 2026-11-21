

# ═══════════════════════════════════════════════════════════════════════════
# 17. TEST 39 — TEST 34G geometry sweep (finite-size lab port)
# ═══════════════════════════════════════════════════════════════════════════

T34G_MAX_SITES = 144 * 144


def _wrap_pi(x: float) -> float:
    return (x + math.pi) % (2.0 * math.pi) - math.pi


def _ring_vortices(L: int, Nv: int, q: float) -> List[Tuple[float, float, float]]:
    c = (L + 0.5) / 2.0
    R = L / 4.0
    out = []
    for k in range(Nv):
        ang = 2 * math.pi * k / Nv + math.pi / Nv
        out.append((c + R * math.cos(ang), c + R * math.sin(ang), q))
    return out


def _bond_phase_flat(a, b, vorts, alpha_q: float) -> float:
    phi = 0.0
    for (vx, vy, vqq) in vorts:
        aa = math.atan2(a[1] - vy, a[0] - vx)
        bb = math.atan2(b[1] - vy, b[0] - vx)
        phi += vqq * alpha_q * _wrap_pi(bb - aa)
    return phi


def t34g_build_flat(L: int, seed: int, alpha: float, Nv: int, q: float,
                    W: float) -> np.ndarray:
    """Torus with Peierls phases from a vortex ring (covering-space offsets)."""
    rng = jrng(seed)
    N = L * L
    H = np.zeros((N, N), dtype=np.complex128)
    vorts = _ring_vortices(L, Nv, q)
    aq = alpha * q
    for y1 in range(1, L + 1):
        for x1 in range(1, L + 1):
            i = (y1 - 1) * L + (x1 - 1)
            a = (x1, y1)
            for (x2, y2) in ((x1 % L + 1, y1), (x1, y1 % L + 1)):
                j = (y2 - 1) * L + (x2 - 1)
                phi = _bond_phase_flat(a, (x2, y2), vorts, aq)
                H[i, j] += -np.exp(1j * phi)
                H[j, i] += -np.exp(-1j * phi)
            H[i, i] += (rng.random() - 0.5) * W
    return H


def t34g_build_fold(L: int, seed: int, alpha: float, Nv: int, q: float, W: float,
                    kind: str = "klein") -> np.ndarray:
    """Quotient of the L×L torus: Klein glide (x+L/2, L+1−y) or pillow (L+1−x, L+1−y).

    Fundamental domain: FULL x range 1..L, y ∈ 1..L/2 → n = L²/2 sites."""
    assert L % 2 == 0, f"fold geometry needs even L, got {L}"
    rng = jrng(seed)
    half = L // 2
    n = L * half
    H = np.zeros((n, n), dtype=np.complex128)
    vorts = _ring_vortices(L, Nv, q)
    images = []
    for (vx, vy, vq) in vorts:
        if kind == "klein":
            images.append((((int(vx) + L // 2 - 1) % L) + 0.5, L + 1 - vy, -vq))
        else:
            images.append((L + 1 - vx, L + 1 - vy, vq))
    allv = vorts + images
    aq = alpha * q

    def idx(x1: int, y1: int) -> int:
        return (y1 - 1) * L + (x1 - 1)

    def fold(x2: int, y2: int):
        if y2 <= half:
            return x2, y2
        if kind == "klein":
            return ((x2 + half - 1) % L) + 1, L + 1 - y2
        return L + 1 - x2, L + 1 - y2

    for y1 in range(1, half + 1):
        for x1 in range(1, L + 1):
            i = idx(x1, y1)
            a = (x1, y1)
            for (x2, y2) in (((x1 % L) + 1, y1), (x1, (y1 % L) + 1)):
                x2f, y2f = fold(x2, y2)
                j = idx(x2f, y2f)
                phi = 0.0
                for (vx, vy, vqq) in allv:
                    aa = math.atan2(a[1] - vy, a[0] - vx)
                    bb = math.atan2(y2f - vy, x2f - vx)
                    phi += vqq * aq * _wrap_pi(bb - aa)
                H[i, j] += -np.exp(1j * phi)
                H[j, i] += -np.exp(-1j * phi)
            H[i, i] += (rng.random() - 0.5) * W
    return H


def t34g_build_cubic(m: int, seed: int, alpha: float, Nv: int, q: float,
                     W: float) -> np.ndarray:
    """Surface of the [−m,m]³ lattice (step 2): the cube-sphere graph."""
    coords = []
    for x in range(-m, m + 1, 2):
        for y in range(-m, m + 1, 2):
            for z in range(-m, m + 1, 2):
                if abs(x) == m or abs(y) == m or abs(z) == m:
                    coords.append((x, y, z))
    index = {c: i for i, c in enumerate(coords)}
    n = len(coords)
    H = np.zeros((n, n), dtype=np.complex128)
    c0 = (m + 0.5) / 2.0
    R = m / 2.0 + 0.5
    vorts = []
    for k in range(Nv):
        ang = 2 * math.pi * k / Nv + math.pi / Nv
        vorts.append((c0 + R * math.cos(ang), c0 + R * math.sin(ang), 0.0, q))
    aq = alpha * q
    rng = jrng(seed)
    for (x, y, z), i in index.items():
        a3 = (x, y, z, 0.0)
        for dx, dy, dz in ((2, 0, 0), (-2, 0, 0), (0, 2, 0), (0, -2, 0), (0, 0, 2), (0, 0, -2)):
            c2 = (x + dx, y + dy, z + dz)
            if c2 in index:
                j = index[c2]
                b3 = (c2[0], c2[1], c2[2], 0.0)
                phi = 0.0
                for (vx, vy, vz, vqq) in vorts:
                    aa = math.atan2(math.sqrt((a3[1]-vy)**2 + (a3[2]-vz)**2), a3[0]-vx)
                    bb = math.atan2(math.sqrt((b3[1]-vy)**2 + (b3[2]-vz)**2), b3[0]-vx)
                    phi += vqq * aq * _wrap_pi(bb - aa)
                H[i, j] += -np.exp(1j * phi)
                H[j, i] += -np.exp(-1j * phi)
        H[i, i] += (rng.random() - 0.5) * W
    return H


# ---- PSL(2,q) Cayley machinery ----------------------------------------------
class GF:
    """Prime field GF(p) or GF(8) = GF(2)[x]/(x³+x+1)."""

    def __init__(self, q: int):
        self.q = q
        self.is_gf8 = (q == 8)
        if self.is_gf8:
            self._log = [0] * 8
            self._exp = [0] * 15
            v = 1
            for i in range(14):
                self._exp[i] = v
                if i < 7:          # first cycle only — the group has order 7
                    self._log[v] = i
                v <<= 1
                if v & 8:
                    v ^= 0b1011  # x³+x+1
            self._exp[14] = v

    def mul(self, a: int, b: int) -> int:
        if not self.is_gf8:
            return (a * b) % self.q
        if a == 0 or b == 0:
            return 0
        return self._exp[self._log[a] + self._log[b]]

    def inv(self, a: int) -> int:
        if not self.is_gf8:
            return pow(a, self.q - 2, self.q)
        return self._exp[7 - self._log[a]]

    def sub(self, a: int, b: int) -> int:
        if not self.is_gf8:
            return (a - b) % self.q
        return (a ^ b) & 7


def psl_elements(q: int) -> List[Tuple[int, int, int, int]]:
    """PSL(2,q): matrices with ad−bc ≡ 1 (mod q), modulo ±I (odd q)."""
    gf = GF(q)
    els = []
    if gf.is_gf8:
        for a in range(8):
            for b in range(8):
                for c in range(8):
                    for d in range(8):
                        if (gf.mul(a, d) ^ gf.mul(b, c)) == 1:
                            els.append((a, b, c, d))
        return sorted(set(els))          # PSL(2,8) = SL(2,8), |G| = 504
    inv = [gf.inv(a) if a else 0 for a in range(q)]
    minus1 = (-1) % q
    for a in range(q):
        for b in range(q):
            for c in range(q):
                if a != 0:
                    d = gf.mul(inv[a], (1 + gf.mul(b, c)) % q)
                    els.append((a, b, c, d))
                elif b != 0 and gf.mul(b, c) == minus1:
                    for d in range(q):   # a = 0: −bc ≡ 1, d free
                        els.append((0, b, c, d))
    uniq = set()
    for e in els:
        uniq.add(min(e, tuple((-x) % q for x in e)))
    return sorted(uniq)


def psl_matmul(gf: GF, m1, m2) -> Tuple[int, int, int, int]:
    a, b, c, d = m1
    e, f, g_, h = m2
    if gf.is_gf8:
        return (gf.mul(a, e) ^ gf.mul(b, g_), gf.mul(a, f) ^ gf.mul(b, h),
                gf.mul(c, e) ^ gf.mul(d, g_), gf.mul(c, f) ^ gf.mul(d, h))
    return ((gf.mul(a, e) + gf.mul(b, g_)) % gf.q,
            (gf.mul(a, f) + gf.mul(b, h)) % gf.q,
            (gf.mul(c, e) + gf.mul(d, g_)) % gf.q,
            (gf.mul(c, f) + gf.mul(d, h)) % gf.q)


def psl_order(gf: GF, m, max_o: int = 16) -> int:
    """Order in PSL: smallest k with M^k ≡ ±I (in char 2, −I = I)."""
    ident = (1, 0, 0, 1)
    neg = ident if gf.is_gf8 else tuple((-x) % gf.q for x in ident)
    cur = m
    for o in range(1, max_o + 1):
        if cur == ident or cur == neg:
            return o
        cur = psl_matmul(gf, cur, m)
    return -1


_CAYLEY_CACHE: Dict[int, tuple] = {}


def cayley_generating_pair(q: int):
    """Deterministic (3,7) generating pair of PSL(2,q) by BFS search."""
    if q in _CAYLEY_CACHE:
        return _CAYLEY_CACHE[q]
    gf = GF(q)
    els = psl_elements(q)
    idx = {e: i for i, e in enumerate(els)}
    n = len(els)
    assert n == q * (q * q - 1) // (2 if q % 2 == 1 else 1), \
        f"|PSL(2,{q})| = {n} unexpected"
    gens3 = [e for e in els if psl_order(gf, e) == 3]
    gens7 = [e for e in els if psl_order(gf, e) == 7]
    ident = (1, 0, 0, 1)
    found = None
    for B in gens3:
        for C in gens7:
            seen = {ident}
            frontier = [ident]
            while frontier:
                nxt = []
                for m in frontier:
                    for g in (B, C):
                        mm = psl_matmul(gf, m, g)
                        key = min(mm, tuple((-x) % q for x in mm)) if q % 2 == 1 else mm
                        if key not in seen:
                            seen.add(key)
                            nxt.append(mm)
                            if len(seen) == n:
                                break
                    if len(seen) == n:
                        break
                if len(seen) == n:
                    break
                frontier = nxt
            if len(seen) == n:
                found = (gf, els, idx, B, C, n)
                break
        if found:
            break
    if not found:
        raise RuntimeError(f"no (3,7) generating pair found for q={q}")
    _CAYLEY_CACHE[q] = found
    return found


def t34g_build_cayley(q: int, seed: int, alpha: float, Nv: int, q_flux: float,
                      W: float) -> np.ndarray:
    """Magnetic Cayley graph Cay(PSL(2,q); B, C) — heptagons carry 2πqαNv/7."""
    gf, els, idx, B, C, n = cayley_generating_pair(q)
    rng = jrng(seed)
    H = np.zeros((n, n), dtype=np.complex128)
    phiB = 0.0
    phiC = 2.0 * math.pi * q_flux * alpha * Nv / 7.0
    mulB = np.empty(n, dtype=np.int64)
    mulC = np.empty(n, dtype=np.int64)
    for i, e in enumerate(els):
        mb = psl_matmul(gf, e, B)
        mc = psl_matmul(gf, e, C)
        mulB[i] = idx[min(mb, tuple((-x) % q for x in mb))] if q % 2 == 1 else idx[mb]
        mulC[i] = idx[min(mc, tuple((-x) % q for x in mc))] if q % 2 == 1 else idx[mc]
    for i in range(n):
        H[i, mulB[i]] += -np.exp(1j * phiB)
        H[mulB[i], i] += -np.exp(-1j * phiB)
        H[i, mulC[i]] += -np.exp(1j * phiC)
        H[mulC[i], i] += -np.exp(-1j * phiC)
        H[i, i] += (rng.random() - 0.5) * W
    return H


def t34g_unfold_levels(E: np.ndarray) -> np.ndarray:
    n = len(E)
    trim_eff = min(20, max(3, n // 8))
    m_eff = min(25, max(5, n // 12))
    lo, hi = trim_eff, n - trim_eff
    x = E[lo:hi]
    sp = np.diff(x)
    w = len(sp)
    cs = np.concatenate(([0.0], np.cumsum(sp)))
    out = []
    for i in range(w):
        a = max(0, i - m_eff)
        b = min(w, i + m_eff + 1)
        loc = (cs[b] - cs[a]) / (b - a)
        if loc > 0 and 0 < sp[i] / loc < 10:
            out.append(sp[i] / loc)
    out = np.array(out)
    return out / out.mean() if len(out) else out


def t34g_gue_cdf(s):
    from scipy.special import erf as _erf
    s = np.asarray(s, dtype=float)
    return _erf(2.0 * s / math.sqrt(math.pi)) \
        - (4.0 * s / math.pi) * np.exp(-4.0 * s * s / math.pi)


def t34g_ks_one(sp: np.ndarray) -> float:
    s = np.sort(sp)
    n = len(s)
    if n < 3:
        return float("nan")
    F = t34g_gue_cdf(s)
    i = np.arange(1, n + 1, dtype=float)
    return float(max(np.max(np.abs(F - (i - 1) / n)), np.max(np.abs(i / n - F))))


def t34g_ks_two(x: np.ndarray, y: np.ndarray) -> Tuple[float, float]:
    xs, ys = np.sort(x), np.sort(y)
    nx_, ny_ = len(xs), len(ys)
    if nx_ < 2 or ny_ < 2:
        return float("nan"), float("nan")
    allv = np.concatenate((xs, ys))
    cdfx = np.searchsorted(xs, allv, side="right") / nx_
    cdfy = np.searchsorted(ys, allv, side="right") / ny_
    D = float(np.max(np.abs(cdfx - cdfy)))
    lam = math.sqrt(nx_ * ny_ / (nx_ + ny_)) * D
    s, sign = 0.0, 1.0
    for k in range(1, 101):
        term = sign * math.exp(-2.0 * k * k * lam * lam)
        s += term
        sign = -sign
        if abs(term) < 1e-18:
            break
    return D, clamp(2.0 * s, 0.0, 1.0)


def t34g_pair_correlation(u: np.ndarray, smax: float = 3.0, nbins: int = 150,
                          kmax: int = 40) -> Tuple[np.ndarray, float]:
    ds = smax / nbins
    hist = np.zeros(nbins)
    n = len(u)
    M = 0
    for i in range(n):
        for j in range(i + 1, min(n, i + kmax)):
            d = u[j] - u[i]
            if d <= smax:
                b = int(d / ds)
                if 0 <= b < nbins:
                    hist[b] += 1.0
                M += 1
    R2 = hist / (M * ds) if M > 0 else hist
    centers = (np.arange(nbins) + 0.5) * ds
    plateau_mask = (centers >= 1.0) & (centers <= 2.0)
    plateau = float(R2[plateau_mask].mean()) if plateau_mask.any() else float("nan")
    return R2, plateau


def test39_t34g_geometry_sweep(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    budget_L = cfg.t34g_L
    max_sites = min(T34G_MAX_SITES, _max_sites_bytes())
    budget = min(budget_L * budget_L, max_sites)
    reps = cfg.t34g_reps
    alpha, Nv, q, W = cfg.t34g_alpha, cfg.t34g_nv, cfg.t34g_q, cfg.t34g_W
    sp_z = normalized_spacings(zeros)
    sp_z = sp_z[(sp_z > 0) & (sp_z < 10)]
    sp_z = sp_z / sp_z.mean()
    print("\n" + "═" * 60)
    print("TEST 39: TEST 34G — geometry sweep (torus/Klein/pillow/cube/Hurwitz)")
    print(f" budget ≈ {budget} sites, {reps} reps; universal verdict = 7/7 geometries")
    print("─" * 60)
    geoms = ["torus", "klein", "pillow", "cubic", "psl27", "psl28", "psl213"]
    if cfg.t34g_geoms != "all":
        geoms = [g.strip() for g in cfg.t34g_geoms.split(",")]
    all_ok = True
    summary = []
    for ig, geom in enumerate(geoms):
        seed0 = cfg.ab_seed + 3900 + 1000 * ig
        pooled = []
        Ds = []
        for k in range(1, reps + 1):
            rng_seed = seed0 + k
            if geom == "torus":
                L = max(12, int(math.isqrt(budget)))
                H = t34g_build_flat(L, rng_seed, alpha, Nv, q, W)
            elif geom in ("klein", "pillow"):
                # fold needs EVEN L: round the site-budget sqrt down to even
                L = max(12, 2 * (int(math.isqrt(budget // 2)) // 2))
                H = t34g_build_fold(L, rng_seed, alpha, Nv, q, W, geom)
            elif geom == "cubic":
                m = 1
                while 6 * (m + 1) ** 2 - 12 * (m + 1) + 8 <= budget:
                    m += 2
                H = t34g_build_cubic(m, rng_seed, alpha, Nv, q, W)
            else:
                qg = {"psl27": 7, "psl28": 8, "psl213": 13}[geom]
                H = t34g_build_cayley(qg, rng_seed, alpha, Nv, q, W)
            ev = np.linalg.eigvalsh(H)
            n = len(ev)
            ilo, ihi = max(2, int(0.25 * n)), min(n - 1, int(math.ceil(0.75 * n)))
            window = ev[ilo:ihi]
            sp = t34g_unfold_levels(window)
            if len(sp) < 10:
                print(f" {geom:>7} rep {k}: unfold produced only {len(sp)} spacings "
                      f"(n={n}, window {len(window)})")
                if len(sp) == 0:
                    continue
            pooled.append(sp)
            Ds.append(t34g_ks_one(sp) if len(sp) else float("nan"))
            del H
        if not pooled:
            print(f" {geom:>7}: no usable spacings → FAIL")
            all_ok = False
            summary.append((geom, float("nan"), float("nan"), float("nan"),
                            float("nan"), float("nan"), False))
            continue
        sp_all = np.concatenate(pooled)
        D_one = t34g_ks_one(sp_all)
        D2, p2 = t34g_ks_two(sp_all, sp_z)
        u = np.concatenate(([0.0], np.cumsum(sp_all)))
        R2, plateau = t34g_pair_correlation(u)
        centers = (np.arange(len(R2)) + 0.5) * (3.0 / len(R2))
        R2_gue = 1.0 - (np.sin(math.pi * centers) / (math.pi * centers)) ** 2
        d_gue = float(np.mean(np.abs(R2 - R2_gue)))
        d_pois = float(np.mean(np.abs(R2 - 1.0)))
        v_ok = (((p2 == p2 and p2 > 0.01) or (D2 == D2 and D2 < 0.10))
                and (d_gue < d_pois) and (0.75 <= plateau <= 1.25))
        all_ok &= v_ok
        summary.append((geom, D2, p2, d_gue, d_pois, plateau, v_ok))
        print(f" {geom:>7} (n={len(sp_all)}): D = {D2:.4f}, p = {p2:.3e}, "
              f"d_GUE = {d_gue:.3f}, d_Pois = {d_pois:.3f}, plateau = {plateau:.3f} "
              f"→ {'PASS' if v_ok else 'FAIL'}")
    rec = [(g, ok, f"D={d:.4f}, plateau={pl:.3f}") for (g, d, p, dg, dp, pl, ok) in summary]
    ok = hc_verdict_table(cfg, "Test 34G", rec)
    log_result(f" Test 39: geometry sweep {sum(1 for r in rec if r[1])}/{len(rec)} → "
               f"{'PASS' if ok else 'WARN'}")
    return ok, f"{sum(1 for r in rec if r[1])}/{len(rec)} geometries"
