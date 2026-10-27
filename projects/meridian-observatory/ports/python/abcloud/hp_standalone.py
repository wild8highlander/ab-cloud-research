# -*- coding: utf-8 -*-
"""Hilbert–Pólya audit gates H1–H8 — 1:1 port of hp_audit_standalone.jl (v25.2-NUMINA).

Source: meridian-spectral-observatory/hp_audit_standalone.jl (7722 lines).
Ported here (numeric parity surface):

  HPConfig / make_hp_config (L2428/2446) · apply_preset! (L6715, v24.3
  reset-then-override semantics) · resolve_vortex_count / resolve_q_magnitude /
  ab_w_eff (L2454-2461) · random_vortex_configuration (L2738) ·
  vortex_onsite_potential (L2917) + build_ab_cloud_hamiltonian (L2950) — the
  builder is the SAME suite-lineage code as lattice.py (compared line by line;
  only the :dirac stub and the console log differ, neither reachable from the
  HP gates which run :monumental only) so lattice.py is REUSED, not copied ·
  _hp_std_vortices/_hp_std_config/_hp_spectrum (L3164-3190) ·
  _hp_unfold_local/_hp_periodogram/_hp_raw_ft/_hp_k_residual (L3196-3294,
  reused from unfold.py where identical) · helper sections before each gate ·
  the eight gate runners hp_h01..hp_h08 (L3716/4188/4265/4452/4619/4957/5086/
  5238) · HPRegime/hp_regimes/_hp5_plan (L3398-3465) · gue_matrix_eigenvalues
  (L2665) · _hp_isprime/_hp_isprimepower/_hp_arith_tables (L3650-3714) ·
  GATE_NAME/GATE_MIN (L6770) · load_zeros (L6747) · the battery orchestrator
  (run_battery_core L7112, computation only).

INTENTIONALLY NOT PORTED (I/O cosmetics — the numeric verdicts are the parity
surface, these are presentation layers of the Julia original):
  * AURORA console (_mr_* panels, ANSI colors, prompts, menus, telescope
    frames, plasma banner/bar/ribbon);
  * ABPlotV23 plotting engine (Hershey fonts, Canvas/Fig, PNG writers, _crc32 —
    used ONLY for PNG chunks, no gate computation touches it);
  * HTML/markdown report generation (final_report.md/.html, write_run_reports);
  * rep_tee_stdout console capture, file logging (log_comp/log_result become
    no-ops — the numbers they carried are returned in the result dicts);
  * the interactive parameter editor (hp_params_menu!) and profile files;
  * the subprocess heartbeat (v23.8) and progress bars (prog_update).

RNG CONTRACT (golden anchors are generated with this exact semantics; Julia's
MersenneTwister is dSFMT and is NOT reproduced bit-for-bit): every random draw
goes through MT19937RNG wrapping abcloud.mt19937.MT19937 —
    random()        : two UInt32 draws → ((a>>5)*2**26 + (b>>6)) / 2**53
    randint(lo,hi)  : lo + floor(u*(hi-lo+1)), one double
    randn()         : Box-Muller, u1 (redrawn while <= 0, no u2 on redraw),
                      u2 → sqrt(-2 ln u1)·cos(2π u2); two doubles per value
    randchoice(vec) : vec[floor(u*len)], one double
Every Julia ``MersenneTwister(seed)`` site maps to ``MT19937RNG(seed)`` at the
same position in the call flow; ``randperm`` follows Julia's Random algorithm
(a[1]=1; for i in 2..n: j = rand(1:i); a[i]=a[j]; a[j]=i — one draw per step).

Indexing: Julia is 1-based, Python 0-based — slices are converted per call.
``var``/``std`` = ddof=1 (Julia corrected=true); ``quantile`` = linear
interpolation (numpy default == Julia default); GUE CDF = the EXACT β=2 Wigner
surmise (the standalone's own gue_cdf, not the 32768-point table).
"""

import bisect
import math
import os
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np

from .lattice import (Vortex, ABCloudConfig, build_ab_cloud_hamiltonian,
                      central_band_eigs, vortex_onsite_potential,
                      MODEL_MONUMENTAL)
from .mt19937 import MT19937
from .unfold import (hp_unfold_local, hp_raw_ft, hp_periodogram, hp_k_residual,
                     hp_kgue_envelope, pearson_cor, hp_rankdata, hp_aicc,
                     hp_wald_ci, hp_fluct_hp, hp_unit_spacings)
from .gof import (compute_K_form_factor, mean_adjacent_spacing_ratio, linreg,
                  ks_test, smooth_counting_function)
from .special import gue2_surmise_cdf

PI = math.pi

__all__ = [
    "HPConfig", "make_hp_config", "apply_preset",
    "resolve_vortex_count", "resolve_q_magnitude", "ab_w_eff",
    "random_vortex_configuration", "vortex_onsite_potential",
    "build_ab_cloud_hamiltonian",
    "MT19937RNG",
    "HP_ALPHA_SMALL", "HP_ALPHA_GRID", "HP5_SOLVE_CAP", "HPRegime", "hp_regimes",
    "hp_h01_berry_keating", "hp_h02_weyl_law", "hp_h03_power_law",
    "hp_h04_critical_q", "hp_h05_ensemble", "hp_h06_stability",
    "hp_h07_sequence_correlation", "hp_h08_all_numbers",
    "GATE_NAME", "GATE_MIN", "load_zeros", "run_battery", "smoke_test",
]

# ═════════════════════════════════════════════════════════════════════════════
# §0. RNG — the portable classic MT19937 with the golden-anchor draw contract
# ═════════════════════════════════════════════════════════════════════════════


class MT19937RNG:
    """Tiny wrapper over abcloud.mt19937.MT19937 implementing the port-wide
    randomness contract (see module docstring).  Every Julia
    ``MersenneTwister(seed)`` construction site maps to ``MT19937RNG(seed)``."""

    __slots__ = ("_mt",)

    def __init__(self, seed: int):
        self._mt = MT19937(int(seed))

    def random(self) -> float:
        """Uniform double in [0, 1) from two consecutive UInt32 draws."""
        return self._mt.random()

    def randint(self, lo: int, hi: int) -> int:
        """Julia ``rand(rng, lo:hi)`` — lo + floor(u * len), one double."""
        u = self.random()
        return lo + int(math.floor(u * (hi - lo + 1)))

    def randn(self) -> float:
        """Box–Muller standard normal (2 doubles per value; u2 NOT consumed
        on a u1 <= 0 redraw)."""
        u1 = self.random()
        while u1 <= 0.0:
            u1 = self.random()
        u2 = self.random()
        return math.sqrt(-2.0 * math.log(u1)) * math.cos(2.0 * PI * u2)

    def randchoice(self, vec):
        """Julia ``rand(rng, vec)`` — vec[floor(u * len)], one double."""
        u = self.random()
        idx = int(math.floor(u * len(vec)))
        if idx >= len(vec):  # cannot happen for u < 1; belt and braces
            idx = len(vec) - 1
        return vec[idx]


def _randn_vec(rng: MT19937RNG, count: int):
    """``count`` sequential Box–Muller draws (the exact randn!() stream order)."""
    out = [0.0] * count
    rnd = rng.random
    sqrt, log, cos = math.sqrt, math.log, math.cos
    for i in range(count):
        u1 = rnd()
        while u1 <= 0.0:
            u1 = rnd()
        u2 = rnd()
        out[i] = sqrt(-2.0 * log(u1)) * cos(2.0 * PI * u2)
    return out


def _randperm(rng: MT19937RNG, n: int):
    """Julia Random.randperm (Random stdlib algorithm): a[1] = 1; for i in
    2..n draw j ~ U(1..i) and insert — one double per step, n-1 draws total.
    Returns a permutation of 1..n (1-based values, like Julia)."""
    if n <= 0:
        return []
    a = [0] * n
    a[0] = 1
    for i in range(2, n + 1):
        j = rng.randint(1, i)
        a[i - 1] = a[j - 1]
        a[j - 1] = i
    return a


# ═════════════════════════════════════════════════════════════════════════════
# §0b. Small statistics / range helpers (Julia Statistics semantics)
# ═════════════════════════════════════════════════════════════════════════════


def _mean(v):
    return sum(v) / len(v)


def _std(v):
    """Julia ``std`` — corrected (ddof=1); NaN for n < 2 like Julia."""
    n = len(v)
    if n < 2:
        return float("nan")
    m = sum(v) / n
    return math.sqrt(sum((x - m) ** 2 for x in v) / (n - 1))


def _median(v):
    return float(np.median(np.asarray(v, dtype=float)))


def _quantile(v, p):
    return float(np.quantile(np.asarray(v, dtype=float), p))


def _argmax(v):
    """First index of the maximum (Julia argmax semantics)."""
    best = 0
    for i in range(1, len(v)):
        if v[i] > v[best]:
            best = i
    return best


def _argmin(v):
    best = 0
    for i in range(1, len(v)):
        if v[i] < v[best]:
            best = i
    return best


def _frange(a: float, step: float, stop: float):
    """Julia ``a:step:stop`` (StepRangeLen{Float64}): length =
    floor((stop-a)/step) + 1, values a + k*step (identical IEEE arithmetic in
    Julia and Python → identical lengths; golden check: 0.3:0.004:3.2 = 726)."""
    n = int(math.floor((stop - a) / step)) + 1
    return [a + step * k for k in range(max(n, 0))]


def _linspace(a: float, b: float, n: int):
    """Julia ``range(a, b; length=n)`` = StepRangeLen(a, (b-a)/(n-1), n)."""
    if n <= 0:
        return []
    if n == 1:
        return [float(a)]
    step = (b - a) / (n - 1)
    return [a + step * k for k in range(n)]


def _clamp(x, lo, hi):
    return lo if x < lo else (hi if x > hi else x)


# ═════════════════════════════════════════════════════════════════════════════
# §3. STANDALONE CONFIG — HPConfig (Julia L2428-2452)
# ═════════════════════════════════════════════════════════════════════════════


@dataclass
class HPConfig:
    """The exact cfg.* slice the H1–H8 runners touch, with SUITE launch
    defaults (Julia make_hp_config L2446)."""
    hp_L: int = 56
    hp_n_ensemble: int = 40
    hp_n_q_grid: int = 21
    hp_q_min: float = 0.05
    hp_q_max: float = 1.0
    hp_primes: list = field(default_factory=lambda: [2, 3, 5, 7, 11, 13])
    hp_t_max: float = 40.0
    hp_dt: float = 0.025
    hp_h1_configs: int = 3
    hp_zeta_cap: int = 20_000
    hp_L_ladder: list = field(default_factory=lambda: [28, 36, 44, 52, 60])
    hp_L_weyl: int = 56
    hp_weyl_grid: int = 60
    hp_jitter_trials: int = 12
    hp_pos_jitter: float = 0.35
    hp_alpha_jitter: float = 0.02
    hp_n_gue_calib: int = 5
    hp_seed: int = 2026
    hp_gue_band: float = 0.022
    hp_pass_fraction: float = 0.90
    hp_regime_mode: str = "showdown"          # :showdown | :baseline | :regime_d
    hp_deep_nulls: int = 20
    hp_deep_configs: int = 10
    hp_alpha_scan: bool = True
    hp_alpha_scan_n: int = 40
    hp_num_nmax: int = 200                    # H8 NUM-TRACE: comb depth n = 2..nmax
    hp_num_shufs: int = 200                   # H8: permutation draws for the gap null
    # AB physics constants (suite defaults)
    ab_t: float = 1.0
    ab_center_fraction: float = 0.6
    ab_alpha_test16: float = 0.5
    ab_K_smooth_window: int = 3
    ab_n_realizations: int = 5
    ab_W: float = 4.0
    ab_W_max: float = 1.0
    ab_nv_list: list = field(default_factory=lambda: [4])
    ab_q_list: list = field(default_factory=lambda: [1.0])
    gue_matrix_size: int = 12_000


def make_hp_config() -> HPConfig:
    """Julia make_hp_config (L2446) — the defaults live in the dataclass."""
    return HPConfig()


def apply_preset(cfg: HPConfig, which) -> HPConfig:
    """Julia apply_preset! (L6715) — v24.3 fix: a preset is a COMPLETE
    parameter set.  Reset every field to the code defaults first, then apply
    the preset's overrides; fields the preset does not name keep the default."""
    defaults = make_hp_config()
    for f in defaults.__dataclass_fields__:
        v = getattr(defaults, f)
        if isinstance(v, list):
            v = list(v)
        setattr(cfg, f, v)
    w = str(which).lstrip(":")
    if w == "fast":
        cfg.hp_L = 72
        cfg.hp_L_weyl = 72
        cfg.hp_n_ensemble = 100
        cfg.hp_alpha_scan_n = 40
        cfg.hp_regime_mode = "showdown"
    elif w == "full":
        cfg.hp_L = 56
        cfg.hp_L_weyl = 56
        cfg.hp_n_ensemble = 40
        cfg.hp_alpha_scan_n = 30
        cfg.hp_regime_mode = "showdown"
    elif w == "smoke":
        cfg.hp_L = 20
        cfg.hp_L_weyl = 20
        cfg.hp_n_ensemble = 8
        cfg.hp_h1_configs = 2
        cfg.hp_deep_nulls = 4
        cfg.hp_deep_configs = 4
        cfg.hp_alpha_scan_n = 6
        cfg.hp_zeta_cap = 2000
        cfg.hp_jitter_trials = 2
        cfg.hp_L_ladder = [16, 20, 24]
        cfg.hp_weyl_grid = 60
        cfg.hp_n_gue_calib = 3
        cfg.hp_t_max = 20.0
    else:
        raise ValueError(f"unknown preset {which!r}")
    return cfg


def ab_w_eff(cfg: HPConfig) -> float:
    """Julia ab_w_eff (L2454): min(cfg.ab_W, cfg.ab_W_max)."""
    return min(cfg.ab_W, cfg.ab_W_max)


def resolve_vortex_count(cfg: HPConfig) -> int:
    """Julia resolve_vortex_count (L2456)."""
    if cfg.gue_matrix_size == 0:
        return 4
    return 4 if not cfg.ab_nv_list else int(cfg.ab_nv_list[0])


def resolve_q_magnitude(cfg: HPConfig) -> float:
    """Julia resolve_q_magnitude (L2461)."""
    return 1.0 if not cfg.ab_q_list else float(cfg.ab_q_list[0])


# ═════════════════════════════════════════════════════════════════════════════
# §5. PHYSICS CORE — vortex placement (Julia L2738-2779)
# ═════════════════════════════════════════════════════════════════════════════


def random_vortex_configuration(Nv: int, Nx: int, Ny: int, *,
                                 q_magnitude: float = 1.0,
                                 enforce_neutrality: bool = True,
                                 rng: MT19937RNG = None,
                                 place_at_centers: bool = False):
    """Julia random_vortex_configuration (L2738) — verbatim, with the
    MT19937RNG contract for every draw (order: per vortex x/y placement,
    then the ±q draw only in the non-neutral branch)."""
    if rng is None:
        raise ValueError("random_vortex_configuration needs an MT19937RNG")
    vortices = []
    for k in range(1, Nv + 1):
        if place_at_centers:
            # Plaquette centers (ix+0.5, iy+0.5), ix ∈ 1..Nx-1 (off-by-one fix
            # documented in the Julia source).
            ix = rng.randint(1, Nx - 1)
            iy = rng.randint(1, Ny - 1)
            x = float(ix) + 0.5
            y = float(iy) + 0.5
        else:
            x = Nx * (0.5 + 0.4 * (rng.random() - 0.5))  # avoid lattice edges
            y = Ny * (0.5 + 0.4 * (rng.random() - 0.5))
        # Odd-Nv charge assignment: deterministic minimal-imbalance split.
        if enforce_neutrality and Nv % 2 == 0:
            q = q_magnitude if k <= Nv // 2 else -q_magnitude
        elif enforce_neutrality and Nv % 2 == 1:
            q = q_magnitude if k <= (Nv + 1) // 2 else -q_magnitude  # |net| = 1
        else:
            q = rng.randchoice([-q_magnitude, q_magnitude])
        vortices.append(Vortex(x, y, q))
    return vortices


# vortex_onsite_potential / build_ab_cloud_hamiltonian: the standalone's
# versions (Julia L2917-3088) are line-by-line the SAME suite code as
# lattice.py (monumental smooth-gauge vertical-bond phase, Landau-gauge
# x-hops, MersenneTwister(cfg.disorder_seed) for the ε draw gated on W > 0,
# (H + H†)/2 symmetrization).  lattice.py already implements the ε stream as
# MT19937(cfg.disorder_seed) — the golden-verified contract — so REUSE it.


# ═════════════════════════════════════════════════════════════════════════════
# §6 helpers — standard HP configs / spectrum (Julia L3161-3190)
# ═════════════════════════════════════════════════════════════════════════════


def _hp_std_vortices(cfg: HPConfig, L: int, rng: MT19937RNG):
    """Julia _hp_std_vortices (L3164): suite-resolved Nv/q at plaquette
    centers; the rng drives BOTH the placement and (via the seed) the
    residual-ε pattern."""
    Nv = resolve_vortex_count(cfg)
    q_mag = resolve_q_magnitude(cfg)
    if Nv == 0:
        return []
    return random_vortex_configuration(Nv, L, L, q_magnitude=q_mag,
                                       enforce_neutrality=True, rng=rng,
                                       place_at_centers=True)


def _hp_std_config(cfg: HPConfig, L: int, seed: int, lattice: str = "open",
                   alpha=None, vortices=None) -> ABCloudConfig:
    """Julia _hp_std_config (L3176): alpha=None ↔ Julia NaN → suite α."""
    a = cfg.ab_alpha_test16 if alpha is None else float(alpha)
    v = _hp_std_vortices(cfg, L, MT19937RNG(seed)) if vortices is None else vortices
    return ABCloudConfig(L, L, v, a, cfg.ab_t, lattice, ab_w_eff(cfg), seed,
                         MODEL_MONUMENTAL)


def _hp_spectrum(cfg: HPConfig, c: ABCloudConfig):
    """Julia _hp_spectrum (L3186): build + full dense Hermitian
    diagonalization (values only), sorted ascending."""
    H = build_ab_cloud_hamiltonian(c)
    ev = np.linalg.eigvalsh(H)
    return sorted(float(v) for v in ev)


# ═════════════════════════════════════════════════════════════════════════════
# §6 helpers — small numeric kernels not already in unfold.py
# ═════════════════════════════════════════════════════════════════════════════


def _hp_spearman(x, y) -> float:
    """Julia _hp_spearman (L3315): cor(rankdata(x), rankdata(y))."""
    return pearson_cor(hp_rankdata(x), hp_rankdata(y))


def _hp_linlsq(X, y):
    """Julia _hp_linlsq (L3337): c = X \\ y; (coef, RSS, R²).  np.linalg.lstsq
    (LAPACK SVD) in place of Julia's QR ``\\`` — agreement ~1e-13 on the
    well-posed design matrices used by H2/H8 (documented deviation)."""
    Xm = np.asarray(X, dtype=float)
    ym = np.asarray(y, dtype=float)
    c, _, _, _ = np.linalg.lstsq(Xm, ym, rcond=None)
    fitted = Xm @ c
    res = ym - fitted
    rss = float(np.sum(res * res))
    my = float(np.mean(ym))
    sst = float(np.sum((ym - my) ** 2))
    r2 = 1.0 - rss / sst if sst > 1e-300 else 0.0
    return [float(v) for v in c], rss, r2


def _polyfit(x, y, deg: int):
    """Julia polyfit (L2648): Vandermonde \\ y (lstsq; documented deviation
    vs QR at the 1e-13 level)."""
    xm = np.asarray(x, dtype=float)
    V = np.empty((len(xm), deg + 1))
    for j in range(deg + 1):
        V[:, j] = xm ** j
    coef, _, _, _ = np.linalg.lstsq(V, np.asarray(y, dtype=float), rcond=None)
    return [float(v) for v in coef]


def _polyval(coef, x: float) -> float:
    """Julia polyval (L2657)."""
    s = 0.0
    for j, c in enumerate(coef):
        s += c * (x ** j)
    return s


def _gue_matrix_eigenvalues(N: int, seed: int = 42):
    """Julia gue_matrix_eigenvalues (L2665) with the portable MT19937RNG:
    N² real draws (column-major flat order) then N² imaginary draws, /√2,
    in-place Hermitian symmetrization, dense eigvalsh (ascending)."""
    rng = MT19937RNG(seed)
    n2 = N * N
    res = _randn_vec(rng, n2)  # real parts first (same seeded stream)
    ims = _randn_vec(rng, n2)  # then imaginary parts
    G = np.zeros((N, N), dtype=np.complex128)
    # reinterpret(Float64, vec(G)) is column-major: flat index = col*N + row
    G.real = np.asarray(res).reshape(N, N).T
    G.imag = np.asarray(ims).reshape(N, N).T
    G /= math.sqrt(2.0)  # entries re, im ~ N(0, 1/2)
    # In-place Hermitian symmetrization A = (G + G†)/2 (upper consumes lower)
    U = np.triu(G, 1)
    L = np.tril(G, -1)
    newU = (U + L.conj().T) / 2.0
    G = newU + newU.conj().T + np.diag(np.diag(G).real)
    ev = np.linalg.eigvalsh(G)
    return [float(v) for v in ev]


# ── number theory helpers (Julia L3650-3714) ─────────────────────────────────


def _hp_isprime(n: int) -> bool:
    """Julia _hp_isprime (L3650): trial division (hp_primes may legally
    contain composites — they become H1 specificity decoys)."""
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def _hp_isprimepower(n: int) -> bool:
    """Julia _hp_isprimepower (L3668): p^k, k ≥ 2 (1 and primes excluded)."""
    if n < 4:
        return False
    f = 2
    while f * f <= n:
        if n % f == 0:
            m = n // f
            while m % f == 0:
                m //= f
            return m == 1
        f += 1
    return False


def _hp_arith_tables(M: int):
    """Julia _hp_arith_tables (L3687): d(n), Ω(n), φ(n), σ(n) for n = 1..M
    by classic sieves (values are 1-based; caller slices k = 1..m_g)."""
    if M < 1:
        return [], [], [], []
    d = [0] * M
    om = [0] * M
    phi = list(range(1, M + 1))
    sig = [0] * M
    for i in range(1, M + 1):          # divisor sweep: d, σ
        for j in range(i - 1, M, i):
            d[j] += 1
            sig[j] += i
    for i in range(2, M + 1):          # Ω: +1 per prime POWER dividing n
        if om[i - 1] != 0:
            continue                    # composite — already counted
        pk = i                          # i is prime: sweep p, p², p³ …
        while pk <= M:
            for j in range(pk - 1, M, pk):
                om[j] += 1
            pk *= i
    for i in range(2, M + 1):          # φ: the standard multiplicative sieve
        if phi[i - 1] != i:
            continue                    # i is prime (untouched by smaller factors)
        for j in range(i - 1, M, i):
            phi[j] -= phi[j] // i
    return d, om, phi, sig


# ═════════════════════════════════════════════════════════════════════════════
# §6 helpers — HP parameter regimes (Julia L3370-3465)
# ═════════════════════════════════════════════════════════════════════════════

HP_ALPHA_SMALL = 25.0 / 900.0  # ≈ 0.0278 — sharp-flux screening length
HP_ALPHA_GRID = [HP_ALPHA_SMALL, 0.05, 0.1, 0.2, 0.35, 0.5]
HP5_SOLVE_CAP = 40             # hard ceiling on dense eigensolves issued by H5


class HPRegime:
    """Julia HPRegime struct (L3398)."""
    __slots__ = ("key", "tag", "nv_mode", "alpha_mode")

    def __init__(self, key: str, tag: str, nv_mode: str, alpha_mode: str):
        self.key = key
        self.tag = tag
        self.nv_mode = nv_mode        # "suite" | "density"
        self.alpha_mode = alpha_mode  # "suite" | "small"


def hp_regimes(cfg: HPConfig):
    """Julia hp_regimes (L3405)."""
    base = HPRegime("A", "baseline (published run)", "suite", "suite")
    combined = HPRegime("D", "combined (density + sharp-flux)", "density", "small")
    if cfg.hp_regime_mode == "baseline":
        return [base]
    if cfg.hp_regime_mode == "regime_d":
        return [combined]  # v24.2: FOCUS-D
    return [base,
            HPRegime("B", "monograph density Nv=L²/36", "density", "suite"),
            HPRegime("C", "sharp-flux α=25/900", "suite", "small"),
            combined]


def _hp_regime_Nv(cfg: HPConfig, L: int, R: HPRegime) -> int:
    if R.nv_mode == "density":
        return max(4, int(round(L * L / 36.0)))
    return resolve_vortex_count(cfg)


def _hp_regime_alpha(cfg: HPConfig, R: HPRegime) -> float:
    return HP_ALPHA_SMALL if R.alpha_mode == "small" else cfg.ab_alpha_test16


def _hp_regime_desc(cfg: HPConfig, L: int, R: HPRegime) -> str:
    Nv = _hp_regime_Nv(cfg, L, R)
    a = _hp_regime_alpha(cfg, R)
    return (f"Nv={Nv} ({100 * Nv / float(L * L):.2f}% of sites"
            f"{', L²/36 anchor' if R.nv_mode == 'density' else ''}), "
            f"α={a:.4f}{', 25/900 sharp-flux' if R.alpha_mode == 'small' else ''}")


def _hp5_plan(cfg: HPConfig) -> dict:
    """Julia _hp5_plan (L3443): ≤ HP5_SOLVE_CAP dense solves; the α-profile
    is shaved first, then the ensemble."""
    n_reg = len(hp_regimes(cfg))
    if n_reg == 1:
        E = _clamp(cfg.hp_n_ensemble, 1, HP5_SOLVE_CAP)
        return {"n_reg": 1, "E": E, "n_alpha": 0, "total": E,
                "asked": cfg.hp_n_ensemble,
                "capped": cfg.hp_n_ensemble > HP5_SOLVE_CAP}
    E = _clamp(cfg.hp_n_ensemble, 1, 7)
    na = _clamp(cfg.hp_alpha_scan_n, 1, 2) if cfg.hp_alpha_scan else 0
    total = n_reg * E + len(HP_ALPHA_GRID) * na
    while total > HP5_SOLVE_CAP and na > 0:  # shave the readout first
        na -= 1
        total = n_reg * E + len(HP_ALPHA_GRID) * na
    while total > HP5_SOLVE_CAP and E > 1:
        E -= 1
        total = n_reg * E + len(HP_ALPHA_GRID) * na
    asked = (n_reg * cfg.hp_n_ensemble +
             (len(HP_ALPHA_GRID) * cfg.hp_alpha_scan_n if cfg.hp_alpha_scan else 0))
    return {"n_reg": n_reg, "E": E, "n_alpha": na, "total": total,
            "asked": asked, "capped": total < asked}


def _hp_regime_config(cfg: HPConfig, L: int, seed: int, R: HPRegime,
                      lattice: str = "open") -> ABCloudConfig:
    """Julia _hp_regime_config (L3470): regime A ≡ _hp_std_config bit-for-bit."""
    a = _hp_regime_alpha(cfg, R)
    if R.nv_mode == "density":
        Nv = _hp_regime_Nv(cfg, L, R)
        v = [] if Nv == 0 else random_vortex_configuration(
            Nv, L, L, q_magnitude=resolve_q_magnitude(cfg),
            enforce_neutrality=True, rng=MT19937RNG(seed),
            place_at_centers=True)
    else:
        v = _hp_std_vortices(cfg, L, MT19937RNG(seed))
    return ABCloudConfig(L, L, v, a, cfg.ab_t, lattice, ab_w_eff(cfg), seed,
                         MODEL_MONUMENTAL)


def _hp_snr_of(P, med: float, omega: float, omega_grid) -> float:
    """The gates' ``snr_of`` closure: P at the grid point nearest ω, divided
    by the band median (0 when the median degenerates)."""
    i = _argmin([abs(g - omega) for g in omega_grid])
    return P[i] / med if med > 1e-300 else 0.0


# ═════════════════════════════════════════════════════════════════════════════
# GATE H1 — PRIME-TRACE (Julia hp_h01_berry_keating L3716)
# ═════════════════════════════════════════════════════════════════════════════


def hp_h01_berry_keating(cfg: HPConfig, zeta_zeros) -> dict:
    L = cfg.hp_L
    n_t = max(50, int(round(cfg.hp_t_max / cfg.hp_dt)))
    tvals = [cfg.hp_dt * k for k in range(1, n_t + 1)]  # t = 0 dropped
    primes = sorted(set(p for p in cfg.hp_primes if _hp_isprime(p)))
    decoys = sorted(set(p for p in cfg.hp_primes if not _hp_isprime(p)))
    if not primes:
        primes = [2, 3, 5, 7, 11, 13]  # degenerate list guard
    omega_targets = [math.log(p) for p in primes]
    omega_decoys = [math.log(p) for p in decoys]
    grid_max = max(3.0, max(omega_targets + omega_decoys) + 0.2)
    omega_grid = _frange(0.3, 0.004, grid_max)
    snr_min = 50.0        # D1 fingerprint threshold
    ctrl_min = 100.0      # D1 ζ-control threshold
    null_lim = 10.0       # D1 null ceiling limit
    n_grid = len(omega_grid)

    def snr_of(P, med, w):
        return _hp_snr_of(P, med, w, omega_grid)

    # ── stage 1: AB-cloud spectra (kept for BOTH routes) ──
    P_ab = np.zeros(n_grid)
    K_ab = np.zeros(n_t)
    n_used = 0
    n_raw = 0
    rms_env_acc = 0.0
    tmask = [i for i, t in enumerate(tvals) if t >= 0.3]
    for k in range(1, cfg.hp_h1_configs + 1):
        seed = cfg.hp_seed + 100 + k
        c = _hp_std_config(cfg, L, seed)
        evals = _hp_spectrum(cfg, c)
        n_raw = len(evals)
        P_ab += np.asarray(hp_raw_ft(evals, omega_grid))
        band = central_band_eigs(evals, cfg.ab_center_fraction)
        K_ab += np.asarray(compute_K_form_factor(
            band, tvals, smooth_window=cfg.ab_K_smooth_window))
        n_used += 1
        seg = [(K_ab[i] / max(n_used, 1) - hp_kgue_envelope(tvals[i])) ** 2
               for i in tmask]
        rms_env_acc += math.sqrt(sum(seg) / len(seg))
    P_ab /= max(n_used, 1)
    K_ab /= max(n_used, 1)
    rms_env = rms_env_acc / max(n_used, 1)
    med_ab = float(np.median(P_ab))
    snrs_ab = [snr_of(P_ab, med_ab, w) for w in omega_targets]
    snrs_ab_decoy = [snr_of(P_ab, med_ab, w) for w in omega_decoys]

    # ── stage 2: ζ positive control ──
    snrs_z = []
    snrs_z_k = []
    snrs_z_decoy = []
    med_z = 1.0
    med_z2 = 1.0
    decoy_max_z = 0.0
    decoys_silent = True
    zeta_ok = False
    zeta_n = 0
    k_sig_z = 0
    if not zeta_zeros:
        pass  # ζ positive control: SKIPPED (no zeros loaded) → WARN
    else:
        zslice = [float(v) for v in zeta_zeros[:min(len(zeta_zeros), cfg.hp_zeta_cap)]]
        zeta_n = len(zslice)
        Pz = np.asarray(hp_raw_ft(zslice, omega_grid))
        med_z = float(np.median(Pz))
        snrs_z = [snr_of(Pz, med_z, w) for w in omega_targets]
        snrs_z_decoy = [snr_of(Pz, med_z, w) for w in omega_decoys]
        k_sig_z = sum(1 for s in snrs_z if s >= ctrl_min)
        # v23.6 specificity clause: silent on the composite decoys
        decoy_max_z = max(snrs_z_decoy) if snrs_z_decoy else 0.0
        decoys_silent = decoy_max_z < ctrl_min
        zeta_ok = (k_sig_z >= max(2, len(primes) // 2)) and decoys_silent
        # D2 route on ζ (the reviewer's literal estimator)
        K_z = compute_K_form_factor(zslice, tvals,
                                    smooth_window=cfg.ab_K_smooth_window)
        res_z = hp_k_residual(K_z, tvals)
        Pz2 = np.asarray(hp_periodogram(res_z, tvals, omega_grid))
        med_z2 = float(np.median(Pz2))
        snrs_z_k = [snr_of(Pz2, med_z2, w) for w in omega_targets]
    z_k_fires = bool(snrs_z_k) and sum(1 for s in snrs_z_k if s >= 3.0) >= 3

    # ── stage 3: null controls — vortex-free + GUE ──
    max_snr_null = 0.0
    null_desc = []
    for k in (1, 2):
        c0 = ABCloudConfig(L, L, [], cfg.ab_alpha_test16, cfg.ab_t, "open",
                           0.0, cfg.hp_seed + 710 + k, MODEL_MONUMENTAL)
        ev0 = _hp_spectrum(cfg, c0)
        P0 = np.asarray(hp_raw_ft(ev0, omega_grid))
        med0 = float(np.median(P0))
        s0 = [snr_of(P0, med0, w) for w in omega_targets]
        max_snr_null = max(max_snr_null, max(s0))
        null_desc.append(f"vortex-free #{k}: max {max(s0):.1f}")
    for k in (1, 2):
        gue = _gue_matrix_eigenvalues(n_raw, seed=cfg.hp_seed + 730 + k)
        Pg = np.asarray(hp_raw_ft(gue, omega_grid))
        sg = [snr_of(Pg, float(np.median(Pg)), w) for w in omega_targets]
        max_snr_null = max(max_snr_null, max(sg))
        null_desc.append(f"GUE #{k}: max {max(sg):.1f}")

    # ── stage 4: the AB verdict (the headline) ──
    k_ab = sum(1 for s in snrs_ab if s >= snr_min)
    threshold = max(snr_min, 10.0 * max_snr_null)
    fp_present = bool(snrs_ab) and max(snrs_ab) >= threshold
    fp_marginal = (not fp_present) and bool(snrs_ab) and max(snrs_ab) >= max_snr_null
    max_snr_ab = max(snrs_ab) if snrs_ab else 0.0
    argmax_prime_ab = primes[_argmax(snrs_ab)] if snrs_ab else 0
    fingerprint = ("PRESENT" if fp_present else
                   "MARGINAL" if fp_marginal else "ABSENT")

    # ── stage 5: fingerprint regime sweep (reviewer actions, rounds 1+2) ──
    reg_rows = []   # {key, max_snr, prime, verdict, null_ceiling}
    reg_ctx = {}    # key → (raw levels/config, averaged periodogram)
    deep_info = []  # {key, deep_max, p95, n_draws, verdict, prime}
    sweep_ok = True
    if cfg.hp_regime_mode == "showdown":
        sweep = [R for R in hp_regimes(cfg)
                 if not (R.nv_mode == "suite" and R.alpha_mode == "suite")]
        for j, R in enumerate(sweep, start=1):
            P_r = np.zeros(n_grid)
            n_r = 0
            n_rraw = 0
            for k in range(1, cfg.hp_h1_configs + 1):
                seed = cfg.hp_seed + 40_000 + 1_000 * j + k
                ev = _hp_spectrum(cfg, _hp_regime_config(cfg, L, seed, R))
                n_rraw = len(ev)
                P_r += np.asarray(hp_raw_ft(ev, omega_grid))
                n_r += 1
            P_r /= max(n_r, 1)
            snrs_r = [snr_of(P_r, float(np.median(P_r)), w) for w in omega_targets]
            mx = max(snrs_r) if snrs_r else 0.0
            pm = primes[_argmax(snrs_r)] if snrs_r else 0
            reg_ctx[R.key] = (n_rraw, P_r.copy())
            # regime-matched nulls (reviewer round 2): SAME parameters, NO arithmetic
            c_vf = ABCloudConfig(L, L, [], _hp_regime_alpha(cfg, R), cfg.ab_t,
                                 "open", 0.0, cfg.hp_seed + 40_000 + 1_000 * j + 900,
                                 MODEL_MONUMENTAL)
            Pv = np.asarray(hp_raw_ft(_hp_spectrum(cfg, c_vf), omega_grid))
            sv = [snr_of(Pv, float(np.median(Pv)), w) for w in omega_targets]
            Pg = np.asarray(hp_raw_ft(_gue_matrix_eigenvalues(
                n_rraw, seed=cfg.hp_seed + 40_000 + 1_000 * j + 950), omega_grid))
            sg = [snr_of(Pg, float(np.median(Pg)), w) for w in omega_targets]
            reg_nc = max(max(sv), max(sg))      # THIS regime's null ceiling
            reg_thr = max(snr_min, 10.0 * reg_nc)
            verd = ("PRESENT" if mx >= reg_thr else
                    "MARGINAL (above regime nulls)" if mx >= reg_nc else
                    "absent (within regime nulls)")
            reg_rows.append({"key": R.key, "max_snr": mx, "prime": pm,
                             "verdict": verd, "null_ceiling": reg_nc,
                             "null_vortex_free": max(sv), "null_gue": max(sg),
                             "desc": _hp_regime_desc(cfg, L, R)})
            sweep_ok = sweep_ok and (verd == "absent (within regime nulls)")

        # ── v23.6 DEEPEN protocol (reviewer round 3, №2) ──
        marginal_keys = [rr["key"] for rr in reg_rows
                         if not rr["verdict"].startswith("absent")]
        if marginal_keys and cfg.hp_deep_nulls >= 2:
            for j, R in enumerate(sweep, start=1):
                if R.key not in marginal_keys:
                    continue
                n_rraw_d, P_r0 = reg_ctx[R.key]
                null_maxima = []
                for i in range(1, cfg.hp_deep_nulls + 1):
                    c_vf = ABCloudConfig(L, L, [], _hp_regime_alpha(cfg, R),
                                         cfg.ab_t, "open", 0.0,
                                         cfg.hp_seed + 40_000 + 1_000 * j + 700 + i,
                                         MODEL_MONUMENTAL)
                    Pv = np.asarray(hp_raw_ft(_hp_spectrum(cfg, c_vf), omega_grid))
                    null_maxima.append(max(snr_of(Pv, float(np.median(Pv)), w)
                                           for w in omega_targets))
                for i in range(1, cfg.hp_deep_nulls + 1):
                    Pg = np.asarray(hp_raw_ft(_gue_matrix_eigenvalues(
                        n_rraw_d, seed=cfg.hp_seed + 40_000 + 1_000 * j + 800 + i),
                        omega_grid))
                    null_maxima.append(max(snr_of(Pg, float(np.median(Pg)), w)
                                           for w in omega_targets))
                p95 = _quantile(null_maxima, 0.95)
                P_ext = P_r0.copy()
                n_ext = cfg.hp_h1_configs
                for i in range(1, cfg.hp_deep_configs + 1):
                    seed = cfg.hp_seed + 40_000 + 1_000 * j + 600 + i
                    ev = _hp_spectrum(cfg, _hp_regime_config(cfg, L, seed, R))
                    P_ext += np.asarray(hp_raw_ft(ev, omega_grid))
                    n_ext += 1
                P_ext /= max(n_ext, 1)
                snrs_deep = [snr_of(P_ext, float(np.median(P_ext)), w)
                             for w in omega_targets]
                deep_mx = max(snrs_deep)
                deep_pm = primes[_argmax(snrs_deep)] if snrs_deep else 0
                row = next(rr for rr in reg_rows if rr["key"] == R.key)
                was_present = row["verdict"].startswith("PRESENT")
                deep_verd = ("absent" if deep_mx <= p95 else
                             "PRESENT" if was_present else "MARGINAL")
                deep_info.append({"key": R.key, "deep_max": deep_mx, "p95": p95,
                                  "n_draws": len(null_maxima),
                                  "verdict": deep_verd, "prime": deep_pm})
                row["max_snr"] = deep_mx
                row["prime"] = deep_pm
                row["null_ceiling"] = p95
                row["verdict"] = (
                    f"absent (deep nulls: {deep_mx:.1f} ≤ P95 {p95:.1f})"
                    if deep_verd == "absent" else
                    f"PRESENT (deep nulls: {deep_mx:.1f} > P95 {p95:.1f})"
                    if deep_verd == "PRESENT" else
                    f"MARGINAL (deep nulls: {deep_mx:.1f} > P95 {p95:.1f})")
            sweep_ok = all(rr["verdict"].startswith("absent") for rr in reg_rows)

    # ── verdict rows (Julia rec, L4026-4076) ──
    min_sig_z = (min([s for s in snrs_z if s >= ctrl_min] or [math.inf])
                 if snrs_z else math.inf)
    null_ok = ((max_snr_null < null_lim) or
               (min_sig_z < math.inf and max_snr_null * 100.0 < min_sig_z))
    env_ok = rms_env < 0.30
    reg_all_absent = bool(reg_rows) and all(rr["verdict"].startswith("absent")
                                            for rr in reg_rows)
    reg_any_present = any(rr["verdict"].startswith("PRESENT") for rr in reg_rows)
    rows = []
    if not snrs_z:
        rows.append(["ζ control fires (D1)", zeta_ok,
                     "skipped — no zeros loaded"])
    else:
        spec = ("; composite decoys silent (specificity ok — the comb is "
                "arithmetic, not generic)" if decoys_silent else
                f"; composite decoys FIRING, max {decoy_max_z:.1e} "
                "(SPECIFICITY VIOLATED — generic comb)")
        rows.append(["ζ control fires (D1)", zeta_ok,
                     f"{k_sig_z}/{len(primes)} prime Bragg peaks with SNR ≥ "
                     f"{ctrl_min:.0f} (Riemann–Weil expectation){spec}"])
    rows.append(["nulls silent (D1)", null_ok,
                 f"vortex-free + GUE ceiling = {max_snr_null:.1f} "
                 f"(abs limit {null_lim:.0f}; weakest ζ peak {min_sig_z:.1e} — "
                 f"100× margin {'ok' if null_ok else 'VIOLATED'})"])
    if fp_present:
        ab_detail = (f"PRESENT — max SNR {max_snr_ab:.1e} at log({argmax_prime_ab})")
    elif fp_marginal:
        ab_detail = f"MARGINAL — max SNR {max_snr_ab:.1f} vs ceiling {max_snr_null:.1f}"
    else:
        ab_detail = (f"ABSENT — max SNR {max_snr_ab:.1f} < threshold {threshold:.0f}")
    rows.append(["AB fingerprint verdict", True, ab_detail])
    if not reg_rows:
        rows.append(["fingerprint regime-robust (sweep)", sweep_ok,
                     "skipped — :baseline mode (single HP-standard point)"])
    else:
        if reg_all_absent:
            reg_txt = ("every regime bump sits WITHIN its regime-matched null "
                       "ceiling → generic lattice/flux-geometry artifact, NOT "
                       "primes — ARITHMETIC FINGERPRINT ABSENT is regime-robust")
        elif reg_any_present:
            reg_txt = ("PRESENT above the regime-matched nulls — headline "
                       "discovery: deepen (more seeds/configs) before any claim")
        else:
            reg_txt = ("MARGINAL above regime nulls at "
                       + ", ".join(f"[{rr['key']}] {rr['max_snr']:.1f} vs ceiling "
                                   f"{rr['null_ceiling']:.1f}" for rr in reg_rows
                                   if rr["verdict"].startswith("MARGINAL"))
                       + " → NOT explained by non-arithmetic spectra at the same "
                         "parameters — deepen before any claim (reviewer round 2)")
        if deep_info:
            reg_txt += (" DEEPENED (v23.6, pre-registered P95 rule): "
                        + "; ".join(f"[{di['key']}] deep AB {di['deep_max']:.1f} "
                                    f"vs P95 {di['p95']:.1f} → {di['verdict']}"
                                    for di in deep_info))
        rows.append(["fingerprint regime-robust (sweep)", sweep_ok,
                     "max SNR per regime (own null ceiling in parens): "
                     + " ".join(f"[{rr['key']}] {rr['max_snr']:.1f} "
                                f"({rr['null_ceiling']:.1f})" for rr in reg_rows)
                     + " → " + reg_txt])
    rows.append(["Envelope cross-check (D2)", env_ok,
                 f"RMS(K−K_box, t≥0.3) = {rms_env:.4f} (Test-35 family target "
                 "< 0.30; gates the test status)"])

    ok = bool(zeta_ok and null_ok and sweep_ok and env_ok)
    return {
        "id": 1, "name": GATE_NAME[1], "ok": ok,
        "verdict": "PASS" if ok else "WARN",
        "rows": rows,
        "n_t": n_t, "n_grid": n_grid, "omega_max": omega_grid[-1],
        "primes": primes, "decoys": decoys,
        "omega_targets": omega_targets, "omega_decoys": omega_decoys,
        "snr_min": snr_min, "ctrl_min": ctrl_min, "null_lim": null_lim,
        "threshold": threshold,
        "n_configs": n_used, "n_raw": n_raw,
        "med_ab": med_ab, "snrs_ab": snrs_ab,
        "snrs_ab_decoy": snrs_ab_decoy,
        "max_snr_ab": max_snr_ab, "argmax_prime_ab": argmax_prime_ab,
        "k_ab": k_ab, "fp_present": fp_present, "fp_marginal": fp_marginal,
        "fingerprint": fingerprint,
        "zeta_n": zeta_n, "med_z": med_z, "snrs_z": snrs_z,
        "snrs_z_decoy": snrs_z_decoy, "k_sig_z": k_sig_z,
        "decoy_max_z": decoy_max_z, "decoys_silent": decoys_silent,
        "zeta_ok": zeta_ok,
        "med_z2": med_z2, "snrs_z_k": snrs_z_k, "z_k_fires": z_k_fires,
        "max_snr_null": max_snr_null, "null_desc": null_desc,
        "min_sig_z": min_sig_z, "null_ok": null_ok,
        "rms_env": rms_env, "env_ok": env_ok,
        "sweep_ok": sweep_ok, "reg_all_absent": reg_all_absent,
        "reg_any_present": reg_any_present,
        "regimes": reg_rows, "deep": deep_info,
    }


# ═════════════════════════════════════════════════════════════════════════════
# GATE H2 — WEYL-DOS (Julia hp_h02_weyl_law L4188)
# ═════════════════════════════════════════════════════════════════════════════


def hp_h02_weyl_law(cfg: HPConfig, zeta_zeros) -> dict:
    L = cfg.hp_L_weyl
    seed = cfg.hp_seed + 101
    raw = _hp_spectrum(cfg, _hp_std_config(cfg, L, seed))
    ref = _hp_spectrum(cfg, ABCloudConfig(L, L, [], cfg.ab_alpha_test16,
                                          cfg.ab_t, "open", 0.0, seed + 1,
                                          MODEL_MONUMENTAL))
    pos = [v for v in raw if v > 1e-9]  # positive branch of the RAW spectrum
    n_grid = _clamp(cfg.hp_weyl_grid, 20, 400)
    Eg = _linspace(pos[0], pos[-1], n_grid)
    N_raw = [float(bisect.bisect_right(pos, E)) for E in Eg]  # searchsortedlast
    N_ref = [float(bisect.bisect_right(ref, E)) for E in Eg]
    n = len(Eg)

    # Model A — ζ (Riemann–Weil) counting shape with FREE coefficients
    XA = [[E * math.log(E), E, 1.0] for E in Eg]
    cA, rssA, r2A = _hp_linlsq(XA, N_raw)
    aiccA = hp_aicc(n, rssA, 3)
    # Model B — natural lattice DOS: vortex-free cumulative spectrum rescaled
    XB = [[nr, 1.0] for nr in N_ref]
    cB, rssB, r2B = _hp_linlsq(XB, N_raw)
    aiccB = hp_aicc(n, rssB, 2)
    daicc = aiccA - aiccB
    winner = ("LATTICE DOS (Model B)" if daicc > 10 else
              "ζ-type E·lnE counting (Model A)" if daicc < -10 else
              "INCONCLUSIVE (|ΔAICc| ≤ 10)")

    fits_ok = n >= 30 and math.isfinite(r2A) and math.isfinite(r2B)
    rows = [
        ["both fits computed", fits_ok,
         f"n = {n} grid points, models A (3-par) / B (2-par)"],
        ["fit quality floor", min(r2A, r2B) >= 0.95,
         f"R²_A = {r2A:.5f}, R²_B = {r2B:.5f} (floor 0.95)"],
        ["decisive separation", abs(daicc) > 10, f"ΔAICc = {daicc:+.1f}"],
        ["winner (headline)", True,
         (f"lattice DOS wins by {daicc:.1f} AICc — raw density is ORDINARY "
          "lattice physics") if daicc > 0 else
         (f"ζ-type ansatz wins by {-daicc:.1f} AICc — raw density carries the "
          "T·lnT shape")],
    ]
    ok = bool(fits_ok and min(r2A, r2B) >= 0.95 and abs(daicc) > 10)
    return {
        "id": 2, "name": GATE_NAME[2], "ok": ok,
        "verdict": "PASS" if ok else "WARN",
        "rows": rows,
        "L": L, "seed": seed,
        "n_levels": len(raw), "n_pos": len(pos),
        "e_lo": pos[0], "e_hi": pos[-1], "n_grid": n,
        "cA": cA, "rssA": rssA, "r2A": r2A, "aiccA": aiccA,
        "cB": cB, "rssB": rssB, "r2B": r2B, "aiccB": aiccB,
        "daicc": daicc, "winner": winner,
        "fits_ok": fits_ok, "decisive": abs(daicc) > 10,
    }


# ═════════════════════════════════════════════════════════════════════════════
# GATE H3 — POWER-LAW (Julia hp_h03_power_law L4265)
# ═════════════════════════════════════════════════════════════════════════════


def hp_h03_power_law(cfg: HPConfig, zeta_zeros) -> dict:
    ladder = list(cfg.hp_L_ladder)
    invL, p_low, p_bulk = [], [], []
    se_low, se_bulk = [], []
    r2_low, r2_bulk = [], []
    rungs = []      # per-rung details (L, M, windows)
    for L in ladder:
        raw = _hp_spectrum(cfg, _hp_std_config(cfg, L, cfg.hp_seed + 200 + L))
        pos = [v for v in raw if v > 1e-9]
        M = len(pos)
        if M < 40:
            rungs.append({"L": L, "M": M, "skipped": True})
            continue

        def _fit(a, b):
            ns = [float(x) for x in range(a, b + 1)]
            a0, b0, R2, se, _ = linreg([math.log(x) for x in ns],
                                       [math.log(v) for v in pos[a - 1:b]])
            return b0, se, R2

        i_lo = (max(1, int(round(0.02 * M)) + 1), max(1, int(round(0.20 * M))))
        i_bu = (max(1, int(round(0.30 * M))), max(2, int(round(0.70 * M))))
        pl, sl, rl = _fit(i_lo[0], i_lo[1])
        pb, sb, rb = _fit(i_bu[0], i_bu[1])
        invL.append(1.0 / L)
        p_low.append(pl); se_low.append(sl); r2_low.append(rl)
        p_bulk.append(pb); se_bulk.append(sb); r2_bulk.append(rb)
        rungs.append({"L": L, "M": M, "skipped": False,
                      "low_window": list(i_lo), "bulk_window": list(i_bu),
                      "p_low": pl, "se_low": sl, "r2_low": rl,
                      "p_bulk": pb, "se_bulk": sb, "r2_bulk": rb})

    # Dirac-cone readout
    d_dir_low = _mean([abs(p - 0.5) for p in p_low]) if p_low else float("nan")
    d_dir_bu = _mean([abs(p - 0.5) for p in p_bulk]) if p_bulk else float("nan")

    # L→∞ extrapolation (Test-38 hardcore A1 scheme): p̂(L) = p_∞ + c/L
    def _extrap(ps):
        if len(ps) < 3:
            return float("nan"), float("nan")
        a, b, R2, se, _ = linreg(invL, ps)
        return a, se  # intercept = p_∞, se of the slope

    p_inf_lo, se_inf_lo = _extrap(p_low)
    p_inf_bu, se_inf_bu = _extrap(p_bulk)
    dic_dev_lo = abs(p_inf_lo - 2.0)
    dic_dev_bu = abs(p_inf_bu - 2.0)
    dic_supported = (dic_dev_bu < 0.25) or (dic_dev_lo < 0.25)

    # per-L decisive evidence
    perL_decisive = False
    perL_min_dev = float("nan")
    perL_min_sigma = float("nan")
    if p_low and p_bulk:
        devs = [abs(p - 2.0) for p in p_low] + [abs(p - 2.0) for p in p_bulk]
        sigs = ([(2.0 - p) / max(se, 1e-12) for p, se in zip(p_low, se_low)] +
                [(2.0 - p) / max(se, 1e-12) for p, se in zip(p_bulk, se_bulk)])
        perL_min_dev = min(devs)
        perL_min_sigma = min(sigs)
        perL_decisive = perL_min_dev > 0.5 and perL_min_sigma >= 5.0

    r2min_lo = min(r2_low) if r2_low else 0.0
    r2min_bu = min(r2_bulk) if r2_bulk else 0.0
    extrap_finite = math.isfinite(p_inf_bu) and math.isfinite(se_inf_bu)
    extrap_stable = extrap_finite and se_inf_bu < 0.15
    se_max = max(max(se_low) if se_low else 0.0, max(se_bulk) if se_bulk else 0.0)

    rows = [
        ["low-window fit quality", r2min_lo >= 0.98,
         f"min R² over ladder = {r2min_lo:.5f} (floor 0.98)"],
        ["bulk-window fit quality", r2min_bu >= 0.98,
         f"min R² over ladder = {r2min_bu:.5f} (floor 0.98)"],
        ["per-L falsification (decisive)", perL_decisive,
         (f"min |p̂−2| = {perL_min_dev:.3f} at ≥ {perL_min_sigma:.0f}σ "
          f"(every rung/window; se ≤ {se_max:.4f}) — the rejection does NOT "
          "rest on the L→∞ extrapolation") if math.isfinite(perL_min_dev)
         else "needs ≥ 1 ladder rung"],
        ["L→∞ extrapolation (note)", extrap_finite,
         "needs ≥ 3 ladder rungs" if not extrap_finite else
         (f"stable: p_∞ = {p_inf_bu:.4f} ± {se_inf_bu:.4f} (se limit 0.15)"
          if extrap_stable else
          f"UNSTABLE (informational): p_∞ = {p_inf_bu:.4f} ± {se_inf_bu:.4f}, "
          "se ≫ estimate — non-monotone rung scatter; the verdict rests on the "
          "per-L fits, NOT on this extrapolation (reviewer sync 2026-09-06)")],
        ["dictionary verdict", True,
         (f"SUPPORTED — |p_∞−2|: low {dic_dev_lo:.3f} / bulk {dic_dev_bu:.3f} "
          "(HEADLINE: the toy ring dictionary as real lattice physics)")
         if dic_supported else
         (f"REJECTED (expected honest negative, status synced with H1/H7) — "
          f"|p_∞−2|: low {dic_dev_lo:.3f} / bulk {dic_dev_bu:.3f}; the real 2D "
          "spectrum is not (n−q)² lattice physics")],
        ["Dirac-cone readout (low window)", True,
         ((f"mean |p̂−1/2|: low {d_dir_low:.3f} < bulk {d_dir_bu:.3f} → the "
           "near-edge (vortex-dominated) spectrum is Dirac-cone-like, not "
           "dictionary-like — reviewer observation 2026-09-06, promoted to a "
           "headline") if d_dir_low < d_dir_bu else
          (f"mean |p̂−1/2|: low {d_dir_low:.3f} vs bulk {d_dir_bu:.3f} — no "
           "special Dirac proximity"))
         if math.isfinite(d_dir_low) and math.isfinite(d_dir_bu)
         else "no ladder rungs fitted"],
    ]
    ok = bool(r2min_lo >= 0.98 and r2min_bu >= 0.98 and perL_decisive
              and extrap_finite)
    return {
        "id": 3, "name": GATE_NAME[3], "ok": ok,
        "verdict": "PASS" if ok else "WARN",
        "rows": rows,
        "ladder": ladder,
        "invL": invL,
        "p_low": p_low, "se_low": se_low, "r2_low": r2_low,
        "p_bulk": p_bulk, "se_bulk": se_bulk, "r2_bulk": r2_bulk,
        "rungs": rungs,
        "d_dir_low": d_dir_low, "d_dir_bu": d_dir_bu,
        "p_inf_lo": p_inf_lo, "se_inf_lo": se_inf_lo,
        "p_inf_bu": p_inf_bu, "se_inf_bu": se_inf_bu,
        "dic_dev_lo": dic_dev_lo, "dic_dev_bu": dic_dev_bu,
        "dic_supported": dic_supported,
        "perL_min_dev": perL_min_dev, "perL_min_sigma": perL_min_sigma,
        "perL_decisive": perL_decisive,
        "r2min_lo": r2min_lo, "r2min_bu": r2min_bu,
        "extrap_finite": extrap_finite, "extrap_stable": extrap_stable,
        "se_max": se_max,
    }


# ═════════════════════════════════════════════════════════════════════════════
# GATE H4 — CRITICAL-Q (Julia hp_h04_critical_q L4452)
# ═════════════════════════════════════════════════════════════════════════════


def hp_h04_critical_q(cfg: HPConfig, zeta_zeros) -> dict:
    L = cfg.hp_L
    n_q = _clamp(cfg.hp_n_q_grid, 5, 81)
    qgrid = _linspace(cfg.hp_q_min, cfg.hp_q_max, n_q)
    # FIXED vortex positions for every q (only the charge moves)
    pos_fixed = _hp_std_vortices(cfg, L, MT19937RNG(cfg.hp_seed + 300))
    claimed_all = [0.5, 0.3, 1.0]
    domain_covers = any(cfg.hp_q_min <= qc <= cfg.hp_q_max for qc in claimed_all)

    ks_prof = []   # mean KS_D profile
    r_prof = []    # mean ⟨r⟩ profile
    noise_ks = []  # per-point |seed1 − seed2|/√2 noise floor
    all_finite = True
    for k, q in enumerate(qgrid, start=1):
        vs = [Vortex(v.x, v.y, q * math.copysign(1.0, v.q)) for v in pos_fixed]
        ds = []
        rs = []
        for rep in (1, 2):
            c = ABCloudConfig(L, L, vs, cfg.ab_alpha_test16, cfg.ab_t, "open",
                              ab_w_eff(cfg), cfg.hp_seed + 400 + 10 * k + rep,
                              MODEL_MONUMENTAL)
            ev = _hp_spectrum(cfg, c)
            band = central_band_eigs(ev, cfg.ab_center_fraction)
            D, _ = ks_test(hp_unit_spacings(band), cdf_func=gue2_surmise_cdf)
            r, _ = mean_adjacent_spacing_ratio(band)
            if not (math.isfinite(D) and math.isfinite(r)):
                all_finite = False
            ds.append(D)
            rs.append(r)
        ks_prof.append(_mean(ds))
        r_prof.append(_mean(rs))
        noise_ks.append(abs(ds[0] - ds[1]) / math.sqrt(2.0))

    # prominence of the sharpest KS_D dip vs the cubic baseline
    qf = [float(q) for q in qgrid]
    coef = _polyfit(qf, ks_prof, 3)
    base = [_polyval(coef, q) for q in qf]
    dip_res = [b - ksv for b, ksv in zip(base, ks_prof)]  # positive = dips below
    k_dip = _argmax(dip_res)
    q_star = qf[k_dip]
    sigma_floor = _mean(noise_ks)
    sigma_floor = sigma_floor if sigma_floor > 1e-12 else 1e-12
    z_dip = dip_res[k_dip] / sigma_floor
    half = dip_res[k_dip] / 2.0
    i_lo = k_dip
    while i_lo > 0 and dip_res[i_lo - 1] >= half:
        i_lo -= 1
    i_hi = k_dip
    while i_hi < len(dip_res) - 1 and dip_res[i_hi + 1] >= half:
        i_hi += 1
    dq = qf[1] - qf[0]
    width_frac = (i_hi - i_lo + 1) * dq / (qf[-1] - qf[0])
    claimed = [0.5, 0.3, 1.0]
    nearest = claimed[_argmin([abs(c - q_star) for c in claimed])]
    sharp = (z_dip >= 3.0) and (width_frac <= 0.35)
    on_claim = abs(q_star - nearest) <= 2.0 * dq

    rows = [
        ["scan completed", all_finite,
         f"{n_q} q-points × 2 seeds, all metrics finite"],
        ["noise floor resolved", sigma_floor > 1e-9,
         f"σ(noise) = {sigma_floor:.5f} from per-point seed pairs"],
        ["sharp-feature verdict", True,
         (f"SHARP: z = {z_dip:.2f} at q* = {q_star:.3f}, width {width_frac:.2f} "
          f"span (nearest claimed {nearest:.1f})") if sharp else
         (f"SMOOTH: max z = {z_dip:.2f}, width {width_frac:.2f} span — no "
          "narrow critical-q feature")],
        ["location vs claimed criticals", on_claim or domain_covers,
         (f"DEGENERATE (v23.6 guard): claimed criticals 0.3/0.5/1.0 all OUTSIDE "
          f"the scan domain [{cfg.hp_q_min:.3f}, {cfg.hp_q_max:.3f}] — the "
          "off/coincide verdict carries no information; set the q-domain back "
          "to [0.05, 1.0] and rerun") if not domain_covers else
         (f"resonance at q* = {q_star:.3f} COINCIDES with q_c = {nearest:.1f} "
          "(within 2 grid steps) — supports the critical-line analogy"
          if on_claim else
          f"resonance at q* = {q_star:.3f} does NOT coincide with any claimed "
          f"critical (nearest {nearest:.1f}, off by {abs(q_star - nearest):.3f} = "
          f"{100 * abs(q_star - nearest) / (qf[-1] - qf[0]):.0f}% of span) → the "
          "sharp feature is real but UNPREDICTED — the analogy is NOT "
          "corroborated (reviewer sync 2026-09-06)")],
        ["⟨r⟩ scan range", True,
         f"{min(r_prof):.4f} … {max(r_prof):.4f} across the grid"],
    ]
    ok = bool(all_finite and sigma_floor > 1e-9 and domain_covers)
    return {
        "id": 4, "name": GATE_NAME[4], "ok": ok,
        "verdict": "PASS" if ok else "WARN",
        "rows": rows,
        "L": L, "n_q": n_q, "qgrid": qf,
        "n_vortices": len(pos_fixed),
        "ks_prof": ks_prof, "r_prof": r_prof, "noise_ks": noise_ks,
        "coef": coef, "base": base, "dip_res": dip_res,
        "k_dip": k_dip, "q_star": q_star,
        "ks_min": ks_prof[k_dip],
        "sigma_floor": sigma_floor, "z_dip": z_dip,
        "dip_lo": i_lo, "dip_hi": i_hi, "dq": dq, "width_frac": width_frac,
        "nearest": nearest, "sharp": sharp, "on_claim": on_claim,
        "domain_covers": domain_covers, "all_finite": all_finite,
        "r_mean": _mean(r_prof), "r_min": min(r_prof), "r_max": max(r_prof),
    }


# ═════════════════════════════════════════════════════════════════════════════
# GATE H5 — REGIME-2×2 (Julia hp_h05_ensemble L4619)
# ═════════════════════════════════════════════════════════════════════════════


def hp_h05_ensemble(cfg: HPConfig, zeta_zeros) -> dict:
    regs = hp_regimes(cfg)
    n_reg = len(regs)
    plan = _hp5_plan(cfg)
    focus_d = cfg.hp_regime_mode == "regime_d"  # v24.2 FOCUS-D
    L = cfg.hp_L
    N = plan["E"]
    band_hw = cfg.hp_gue_band
    alpha_on = bool(cfg.hp_alpha_scan and n_reg > 1 and plan["n_alpha"] > 0)

    results = []
    for i, R in enumerate(regs, start=1):
        rs, ksD, ksP = [], [], []
        n_band = 0
        for k in range(1, N + 1):
            i_blk = 1 if R.key == "A" else 2 if R.key == "B" else 3 if R.key == "C" else 4
            seed = cfg.hp_seed + 10_000 * (i_blk - 1) + 500 + k
            c = _hp_regime_config(cfg, L, seed, R)
            ev = _hp_spectrum(cfg, c)
            band = central_band_eigs(ev, cfg.ab_center_fraction)
            n_band = len(band)
            r, _ = mean_adjacent_spacing_ratio(band)
            D, pv = ks_test(hp_unit_spacings(band), cdf_func=gue2_surmise_cdf)
            rs.append(r); ksD.append(D); ksP.append(pv)
        m_r = _mean(rs)
        s_r = _std(rs)
        in_band = sum(1 for x in rs if abs(x - 0.5992) <= band_hw)
        frac_band, ci_lo, ci_hi = hp_wald_ci(in_band, N)
        n_ks = sum(1 for p in ksP if p > 0.01)
        frac_ks, klo, khi = hp_wald_ci(n_ks, N)
        results.append({
            "R": R, "key": R.key, "tag": R.tag, "desc": _hp_regime_desc(cfg, L, R),
            "rs": rs, "ksD": ksD, "ksP": ksP,
            "m_r": m_r, "s_r": s_r, "in_band": in_band,
            "frac_band": frac_band, "ci_lo": ci_lo, "ci_hi": ci_hi,
            "n_ks": n_ks, "frac_ks": frac_ks, "klo": klo, "khi": khi,
            "med_D": _median(ksD), "n_band": n_band,
        })

    pass_reg = [r["frac_band"] >= cfg.hp_pass_fraction and
                (r["frac_ks"] >= 0.90 or r["med_D"] < 0.10) for r in results]
    clean_reg = [r["frac_band"] >= cfg.hp_pass_fraction and
                 r["frac_ks"] >= 0.90 for r in results]
    n_pass = sum(1 for p in pass_reg if p)
    n_clean = sum(1 for p in clean_reg if p)
    pass_keys = [results[i]["key"] for i in range(n_reg) if pass_reg[i]]
    clean_keys = [results[i]["key"] for i in range(n_reg) if clean_reg[i]]
    or_keys = [results[i]["key"] for i in range(n_reg)
               if pass_reg[i] and not clean_reg[i]]
    max_s_r = max(r["s_r"] for r in results)
    best_i = 0
    for i in range(1, n_reg):
        if ((results[i]["frac_ks"], results[i]["frac_band"]) >
                (results[best_i]["frac_ks"], results[best_i]["frac_band"])):
            best_i = i
    best = results[best_i]

    if focus_d:
        if n_pass == 0:
            headline = (
                f"FOCUS-D MISS — regime [D] at the FULL N={N} ensemble misses "
                f"GUE (in-band {best['in_band']}/{N}, raw individual KS-pass "
                f"{best['n_ks']}/{N}, median D {best['med_D']:.4f}): the N=7 "
                "near-pass does not survive full-power testing")
        elif n_clean == 0:
            headline = (
                f"FOCUS-D, OR-CLAUSE ONLY — [D] 'reaches' GUE via median D < "
                f"0.10 alone at N={N} (raw individual KS-pass {best['n_ks']}/{N})"
                f": the 1/{N} granularity excuse is gone — a real "
                "per-realization systematic remains")
        else:
            headline = (
                f"FOCUS-D CLEAN PASS — [D] reaches GUE at raw individual level, "
                f"N={N} (KS-pass {best['n_ks']}/{N} ≥ 90%, in-band "
                f"{best['in_band']}/{N}): the combined regime (density + "
                "sharp-flux) is the model's genuine GUE candidate — the sparse "
                "α=0.5 baseline was the outlier")
    else:
        if n_pass == 0:
            headline = (f"ROBUST FAILURE — no regime reaches GUE across all "
                        f"{n_reg} tested regime(s): the failure is a MODEL-CLASS "
                        f"property (best attempt: [{best['key']}] {best['desc']})")
        elif n_clean == 0:
            headline = ("PARAMETER-DEPENDENT, OR-CLAUSE ONLY — GUE is 'reached' "
                        f"at regime(s) {','.join(pass_keys)} but via the "
                        "median-D clause ALONE (raw individual KS-pass ≈ 0% "
                        "everywhere) — the GUE claim does not survive "
                        "individual-level testing at ANY regime")
        else:
            headline = (f"PARAMETER-DEPENDENT — GUE recovers at regime(s) "
                        f"{','.join(pass_keys)}, but CLEAN pass (raw individual "
                        f"KS-pass ≥ 90%, no OR-clause) only at "
                        f"[{','.join(clean_keys)}] = "
                        + " & ".join(results[i]["desc"] for i in range(n_reg)
                                     if clean_reg[i])
                        + "; OR-clause-only: "
                        + (",".join(or_keys) if or_keys else "none")
                        + " → GUE quality appears only at a specifically tuned "
                          "parameter point — a finetuning story (Test-38 "
                          "flavor), NOT evidence against it")

    # ── v23.6 α-PROFILE (reviewer round 3, №3): finetuning vs plateau ──
    alpha_prof = []
    alpha_class = ""
    if alpha_on:
        alpha_grid = HP_ALPHA_GRID
        na = plan["n_alpha"]
        Nv_sparse = resolve_vortex_count(cfg)
        for ai, al in enumerate(alpha_grid, start=1):
            rs_a, ksD_a, ksP_a = [], [], []
            nb_a = 0
            for k in range(1, na + 1):
                seed = cfg.hp_seed + 900_000 + 1_000 * ai + k
                vs_a = random_vortex_configuration(
                    Nv_sparse, L, L, q_magnitude=resolve_q_magnitude(cfg),
                    enforce_neutrality=True, rng=MT19937RNG(seed),
                    place_at_centers=True)
                c_a = ABCloudConfig(L, L, vs_a, al, cfg.ab_t, "open",
                                    ab_w_eff(cfg), seed, MODEL_MONUMENTAL)
                ev_a = _hp_spectrum(cfg, c_a)
                band_a = central_band_eigs(ev_a, cfg.ab_center_fraction)
                nb_a = len(band_a)
                r_a, _ = mean_adjacent_spacing_ratio(band_a)
                D_a, p_a = ks_test(hp_unit_spacings(band_a),
                                   cdf_func=gue2_surmise_cdf)
                rs_a.append(r_a); ksD_a.append(D_a); ksP_a.append(p_a)
            n_ks_a = sum(1 for p in ksP_a if p > 0.01)
            fb_a = sum(1 for x in rs_a if abs(x - 0.5992) <= band_hw) / na
            alpha_prof.append({
                "alpha": al, "m_r": _mean(rs_a), "s_r": _std(rs_a),
                "frac_ks": n_ks_a / na, "n_ks": n_ks_a,
                "med_D": _median(ksD_a), "frac_band": fb_a, "n_cfg": na,
                "n_band": nb_a,
            })
        plateau_len = 0
        for a in alpha_prof:
            if a["frac_ks"] < 0.90:
                break
            plateau_len += 1
        if plateau_len == len(alpha_prof):
            alpha_class = ("PLATEAU-ALL (clean GUE at EVERY tested α incl. 0.5 "
                           "— cross-check: this CONTRADICTS regime A's failure "
                           "at the α=0.5 point; investigate seeds/protocol "
                           "before any claim)")
        elif plateau_len >= 2:
            alpha_class = (f"PLATEAU-LOW — clean GUE for all α ≤ "
                           f"{alpha_prof[plateau_len - 1]['alpha']:.4g} (the "
                           "whole sharp-flux side is GUE-universal); the "
                           "published α=0.5 baseline is the OUTLIER, not the "
                           "model")
        elif plateau_len == 1:
            alpha_class = (f"NARROW — clean pass only at α = "
                           f"{alpha_prof[0]['alpha']:.4g} = 25/900 → the GUE "
                           "claim is a FINETUNING story (confirmed along the "
                           "screening axis)")
        else:
            alpha_class = ("NONE — no clean pass anywhere on the α-line "
                           "(contradicts regime C's clean pass?! check "
                           "seeds/protocol)")

    rows = [
        [f"solve plan ≤ {HP5_SOLVE_CAP} eigensolves (v24.1 budget)",
         plan["total"] <= HP5_SOLVE_CAP,
         f"plan: {N} config(s) × {n_reg} regime(s)"
         + (f" + {plan['n_alpha'] * len(HP_ALPHA_GRID)} α-profile"
            if plan["n_alpha"] > 0 else "")
         + f" = {plan['total']} diagonalizations (user cap 2026-09-09 — the old "
           "«N ≥ 30» row retired: a cap must not be a silent auto-FAIL; "
           f"per-config KS granularity 1/{N})"],
    ]
    for i, r in enumerate(results):
        rows.append([
            f"[{r['key']}] {r['tag']}", pass_reg[i],
            f"⟨r⟩ {r['m_r']:.4f}±{r['s_r']:.4f}, in-band {100 * r['frac_band']:.1f}% "
            f"({r['in_band']}/{N}, CI {100 * r['ci_lo']:.1f}–{100 * r['ci_hi']:.1f}%) "
            f"| RAW individual KS-pass {100 * r['frac_ks']:.1f}% ({r['n_ks']}/{N}) "
            f"| median D {r['med_D']:.4f} → "
            + ("GUE reached (clean)" if pass_reg[i] and clean_reg[i] else
               "GUE reached via OR-clause ONLY — median D < 0.10 hides a "
               "systematic per-realization shift (raw KS-pass tells the truth)"
               if pass_reg[i] else "misses GUE"),
        ])
    rows.append(["⟨r⟩ scatter (worst regime)", max_s_r <= 0.02,
                 f"max σ = {max_s_r:.4f} over {n_reg} regime(s) (limit 0.02 — "
                 "a lucky seed would show σ ≈ its own deviation)"])
    rows.append(["clean GUE pass (no OR-clause)", n_clean >= 1,
                 (f"NO regime passes the raw individual KS test at ≥ 90% — "
                  f"every 'GUE reached' verdict rides the median-D clause "
                  f"(systematic per-realization deviation, {N} seeds/regime)")
                 if n_clean == 0 else
                 (f"clean at [{','.join(clean_keys)}] (raw individual KS-pass "
                  f"≥ 90%); OR-clause-only at "
                  f"[{','.join(or_keys) if or_keys else 'none'}]")])
    rows.append(["synthesis (headline, never scored)", True, headline])
    if alpha_prof:
        rows.append(["α-profile (headline, never scored)", True,
                     f"{alpha_class} — "
                     + "; ".join(f"α={a['alpha']:.4f}: KS-pass "
                                 f"{100 * a['frac_ks']:.0f}% ({a['n_ks']}/"
                                 f"{a['n_cfg']}), median D {a['med_D']:.4f}, "
                                 f"in-band {100 * a['frac_band']:.0f}%"
                                 for a in alpha_prof)])

    ok = bool(max_s_r <= 0.02 and all(pass_reg) and n_clean >= 1)
    return {
        "id": 5, "name": "FOCUS-D" if focus_d else GATE_NAME[5],
        "ok": ok, "verdict": "PASS" if ok else "WARN",
        "rows": rows,
        "focus_d": focus_d, "L": L, "N": N, "band_hw": band_hw,
        "plan": plan, "alpha_on": alpha_on,
        "n_reg": n_reg, "n_pass": n_pass, "n_clean": n_clean,
        "pass_keys": pass_keys, "clean_keys": clean_keys, "or_keys": or_keys,
        "max_s_r": max_s_r, "best_regime": best["key"],
        "headline": headline, "alpha_class": alpha_class,
        "regimes": [{k: v for k, v in r.items() if k != "R"} for r in results],
        "alpha_profile": alpha_prof,
    }


# ═════════════════════════════════════════════════════════════════════════════
# GATE H6 — HERMIT-STRESS (Julia hp_h06_stability L4957)
# ═════════════════════════════════════════════════════════════════════════════


def hp_h06_stability(cfg: HPConfig, zeta_zeros) -> dict:
    L = cfg.hp_L
    ok_all = True

    # ── (a) boundary switch: the bulk window must be boundary-blind ──
    vs_base = _hp_std_vortices(cfg, L, MT19937RNG(cfg.hp_seed + 600))
    torus_rung = (L % 2 == 0 and
                  abs(cfg.ab_alpha_test16 * L - round(cfg.ab_alpha_test16 * L))
                  < 1e-10)
    r_open = r_torus = float("nan")
    d_boundary = float("nan")
    if torus_rung:
        ev_o = _hp_spectrum(cfg, ABCloudConfig(L, L, vs_base,
                                               cfg.ab_alpha_test16, cfg.ab_t,
                                               "open", ab_w_eff(cfg),
                                               cfg.hp_seed + 601,
                                               MODEL_MONUMENTAL))
        ev_t = _hp_spectrum(cfg, ABCloudConfig(L, L, vs_base,
                                               cfg.ab_alpha_test16, cfg.ab_t,
                                               "torus", ab_w_eff(cfg),
                                               cfg.hp_seed + 601,
                                               MODEL_MONUMENTAL))
        r_open, _ = mean_adjacent_spacing_ratio(
            central_band_eigs(ev_o, cfg.ab_center_fraction))
        r_torus, _ = mean_adjacent_spacing_ratio(
            central_band_eigs(ev_t, cfg.ab_center_fraction))
        d_boundary = abs(r_open - r_torus)
    a_ok = math.isfinite(d_boundary) and d_boundary <= cfg.hp_gue_band
    ok_all = ok_all and a_ok

    # ── (b) jitter: positions AND α, independent disorder each trial ──
    n_tr = cfg.hp_jitter_trials
    ev_base = _hp_spectrum(cfg, ABCloudConfig(L, L, vs_base,
                                              cfg.ab_alpha_test16, cfg.ab_t,
                                              "open", ab_w_eff(cfg),
                                              cfg.hp_seed + 602,
                                              MODEL_MONUMENTAL))
    band_base = central_band_eigs(ev_base, cfg.ab_center_fraction)
    r_base, _ = mean_adjacent_spacing_ratio(band_base)
    bw = band_base[-1] - band_base[0]
    nq = 50
    qlevels = _linspace(0.0, 1.0, nq)
    qbase = [band_base[0] + qv * bw for qv in qlevels]
    rng_j = MT19937RNG(cfg.hp_seed + 603)
    r_jit = []
    drift_max = 0.0
    jitter_finite = True
    for k in range(1, n_tr + 1):
        if n_tr <= 0:
            break
        vs_j = []
        for v in vs_base:
            xj = _clamp(v.x + cfg.hp_pos_jitter * (rng_j.random() * 2 - 1),
                        1.0, float(L) - 1.0)
            yj = _clamp(v.y + cfg.hp_pos_jitter * (rng_j.random() * 2 - 1),
                        1.0, float(L) - 1.0)
            vs_j.append(Vortex(xj, yj, v.q))
        a_j = cfg.ab_alpha_test16 + cfg.hp_alpha_jitter * (rng_j.random() * 2 - 1)
        ev_j = _hp_spectrum(cfg, ABCloudConfig(L, L, vs_j, a_j, cfg.ab_t,
                                               "open", ab_w_eff(cfg),
                                               cfg.hp_seed + 603 + k,
                                               MODEL_MONUMENTAL))
        band_j = central_band_eigs(ev_j, cfg.ab_center_fraction)
        r_j, _ = mean_adjacent_spacing_ratio(band_j)
        if not (math.isfinite(r_j) and len(band_j) == len(band_base)):
            jitter_finite = False
            continue
        r_jit.append(r_j)
        ej = [band_j[0] + qv * (band_j[-1] - band_j[0]) for qv in qlevels]
        drift_max = max(drift_max, max(abs(e - q) for e, q in zip(ej, qbase))
                        / max(bw, 1e-12))
    r_drift = max(abs(r - r_base) for r in r_jit) if r_jit else float("nan")
    b_ok = bool(jitter_finite and math.isfinite(r_drift) and r_drift <= 0.05
                and drift_max <= 0.05)
    ok_all = ok_all and b_ok

    # ── (c) L-growth: hermiticity at machine ε on EVERY rung + bounded ⟨r⟩ ──
    ladder = list(cfg.hp_L_ladder)
    r_series = []
    L_series = []
    herm_worst = 0.0
    for Lk in ladder:
        c = _hp_std_config(cfg, Lk, cfg.hp_seed + 700 + Lk)
        H = build_ab_cloud_hamiltonian(c)
        dh = float(np.max(np.abs(H - H.conj().T)))
        herm_worst = max(herm_worst, dh)
        ev = sorted(float(v) for v in np.linalg.eigvalsh(H))
        r, _ = mean_adjacent_spacing_ratio(
            central_band_eigs(ev, cfg.ab_center_fraction))
        r_series.append(r)
        L_series.append(float(Lk))
    herm_ok = herm_worst < 1e-9
    r_in_band = all(math.isfinite(x) and 0.53 <= x <= 0.67 for x in r_series)
    c_ok = bool(herm_ok and r_in_band)
    ok_all = ok_all and c_ok

    rows = [
        ["(a) open↔torus bulk", a_ok,
         f"|Δ⟨r⟩| = {d_boundary:.4f} ≤ {cfg.hp_gue_band:.3f}"
         if math.isfinite(d_boundary) else
         "skipped — α·L ∉ ℤ (use even L for the torus rung)"],
        ["(b) jitter stability", b_ok,
         f"⟨r⟩ drift {r_drift:.4f}, spectral drift {drift_max:.4f}·BW over "
         f"{len(r_jit)} trials"],
        ["(c) hermiticity every rung", herm_ok,
         f"worst max|H−H†| = {herm_worst:.2e} (machine-ε limit 1e-9)"],
        ["(c) ⟨r⟩ bounded on ladder", r_in_band,
         "no rungs" if not r_series else
         f"{min(r_series):.4f} … {max(r_series):.4f} over L = "
         f"{','.join(str(int(v)) for v in L_series)}"],
    ]
    ok = bool(ok_all)
    return {
        "id": 6, "name": GATE_NAME[6], "ok": ok,
        "verdict": "PASS" if ok else "WARN",
        "rows": rows,
        "L": L, "torus_rung": torus_rung,
        "a_ok": a_ok, "r_open": r_open, "r_torus": r_torus,
        "d_boundary": d_boundary,
        "b_ok": b_ok, "n_trials": len(r_jit), "r_base": r_base,
        "r_drift": r_drift, "drift_max": drift_max,
        "r_jit": r_jit, "jitter_finite": jitter_finite,
        "c_ok": c_ok, "herm_worst": herm_worst, "herm_ok": herm_ok,
        "r_series": r_series, "L_series": L_series, "r_in_band": r_in_band,
    }


# ═════════════════════════════════════════════════════════════════════════════
# GATE H7 — SEQ-CORR (Julia hp_h07_sequence_correlation L5086)
# ═════════════════════════════════════════════════════════════════════════════


def hp_h07_sequence_correlation(cfg: HPConfig, zeta_zeros) -> dict:
    L = cfg.hp_L
    seed = cfg.hp_seed + 800
    ev = _hp_spectrum(cfg, _hp_std_config(cfg, L, seed))
    band = central_band_eigs(ev, cfg.ab_center_fraction)
    m_ab = len(band)

    # fluctuations around the mean density: uₙ − n for the locally unfolded band
    u_ab = hp_unfold_local(band)
    fl_ab = [u_ab[i] - float(i) for i in range(m_ab)]

    if not zeta_zeros:
        # ζ zeros NOT loaded — the sequence test needs γₙ → calibration only
        fl_ab_mean = _mean(fl_ab)
        return {
            "id": 7, "name": GATE_NAME[7], "ok": False, "verdict": "WARN",
            "rows": [["ζ zeros loaded", False, "skipped — no zeros loaded"]],
            "L": L, "seed": seed, "m_ab": m_ab,
            "fl_ab_mean": fl_ab_mean, "fl_ab_std": _std(fl_ab),
            "skipped": True,
        }

    m = min(m_ab, len(zeta_zeros))
    gam = [float(v) for v in zeta_zeros[:m]]
    # ζ side: the standard smooth-counting fluctuation N̄(γₙ) − (n−1)
    fl_z = [smooth_counting_function(g) - float(k - 1) for k, g in enumerate(gam, start=1)]
    fl_ab_m = fl_ab[:m]
    # EDGE TRIM (calibration round 2 fix): trim the outer 10% on BOTH sides
    trim = max(1, int(round(0.1 * m)))
    keep_lo, keep_hi = trim, m - trim          # 0-based slice [trim : m-trim]
    m_kept = m - 2 * trim
    win_hp = max(3, int(round(0.05 * m)))
    fl_a = hp_fluct_hp(fl_ab_m[keep_lo:keep_hi], win=win_hp)
    fl_zt = hp_fluct_hp(fl_z[keep_lo:keep_hi], win=win_hp)

    r_pearson = pearson_cor(fl_a, fl_zt)
    rho_spear = _hp_spearman(fl_a, fl_zt)

    # calibration: |r| distribution of INDEPENDENT GUE–GUE pairs
    n_cal = _clamp(cfg.hp_n_gue_calib, 2, 50)
    cal_abs = []
    for k in range(1, n_cal + 1):
        g1 = central_band_eigs(_gue_matrix_eigenvalues(
            m, seed=cfg.hp_seed + 900 + k), 1.0)
        g2 = central_band_eigs(_gue_matrix_eigenvalues(
            m, seed=cfg.hp_seed + 900 + k + n_cal), 1.0)
        f1 = hp_fluct_hp([u - float(i) for i, u in enumerate(hp_unfold_local(g1))]
                         [keep_lo:keep_hi], win=win_hp)
        f2 = hp_fluct_hp([u - float(i) for i, u in enumerate(hp_unfold_local(g2))]
                         [keep_lo:keep_hi], win=win_hp)
        cal_abs.append(abs(pearson_cor(f1, f2)))
    band_null = max(cal_abs)
    theory_band = 1.0 / math.sqrt(m_kept)

    # shuffled control: destroys sequence alignment, keeps the marginals
    rng_sh = MT19937RNG(cfg.hp_seed + 950)
    perm = _randperm(rng_sh, m)
    fl_sh = hp_fluct_hp([fl_z[p - 1] for p in perm][keep_lo:keep_hi], win=win_hp)
    r_shuf = pearson_cor(fl_a, fl_sh)

    band_eff = max(band_null, 2.5 / math.sqrt(m_kept))
    inside = abs(r_pearson) <= band_eff

    rows = [
        ["calibration pairs", n_cal >= 3,
         f"{n_cal} independent GUE–GUE pairs, max |r| = {band_null:.5f}"],
        ["shuffled control", abs(r_shuf) <= band_eff,
         f"|r_shuffled| = {abs(r_shuf):.5f} within the band"],
        ["sequence correlation", True,
         (f"|r| = {abs(r_pearson):.5f} ≤ band {band_eff:.5f} → independence "
          "confirmed (honest expected result)") if inside else
         (f"|r| = {abs(r_pearson):.5f} > band {band_eff:.5f} → "
          "CORRELATION DETECTED")],
        ["Spearman consistency", abs(rho_spear) <= max(band_null, 0.05) + 0.05,
         f"ρ = {rho_spear:+.5f} (rank-level agreement with the Pearson verdict)"],
    ]
    ok = bool(n_cal >= 3 and abs(r_shuf) <= band_eff and
              abs(rho_spear) <= max(band_null, 0.05) + 0.05)
    return {
        "id": 7, "name": GATE_NAME[7], "ok": ok,
        "verdict": "PASS" if ok else "WARN",
        "rows": rows,
        "L": L, "seed": seed, "m_ab": m_ab, "m": m,
        "gamma_lo": gam[0], "gamma_hi": gam[-1],
        "trim": trim, "m_kept": m_kept, "win_hp": win_hp,
        "r_pearson": r_pearson, "rho_spear": rho_spear,
        "n_cal": n_cal, "cal_abs": cal_abs, "band_null": band_null,
        "theory_band": theory_band, "band_eff": band_eff,
        "r_shuf": r_shuf, "inside": inside,
        "fl_ab_mean": _mean(fl_ab), "fl_ab_std": _std(fl_ab),
        "skipped": False,
    }


# ═════════════════════════════════════════════════════════════════════════════
# GATE H8 — NUM-TRACE (Julia hp_h08_all_numbers L5238)
# ═════════════════════════════════════════════════════════════════════════════


def _hp8_classify_comb(hits, snrs, p95s, domega, cls, ns, low_cut, false_rate):
    """Julia classify_comb closure (L5283-5322): the pre-registered v25.2-NUMINA
    decision table.  Returns (tok, txt, cov_p, cov_pp, cov_c, n_hits, disc)."""

    def class_mean(mask):
        vals = [1.0 if h else 0.0 for h, m in zip(hits, mask) if m]
        return sum(vals) / len(vals) if vals else float("nan")

    mask_p = [c == 1 for c in cls]
    mask_pp = [c == 2 for c in cls]
    mask_c = [c == 3 for c in cls]
    cov_p = class_mean(mask_p)
    cov_pp = class_mean(mask_pp)
    cov_c = class_mean(mask_c)
    n_hits = sum(1 for h in hits if h)
    pab = [s for s, m in zip(snrs, mask_p) if m] + \
          [s for s, m in zip(snrs, mask_pp) if m]
    med_pab = _median(pab) if pab else float("nan")
    cab = [s for s, m in zip(snrs, mask_c) if m]
    med_cab = _median(cab) if cab else 0.0
    disc = med_pab / med_cab if med_cab > 1e-300 else float("inf")
    low = [n <= low_cut for n in ns]
    n_high = sum(1 for m in low if not m)
    n_hits_high = sum(1 for h, m in zip(hits, low) if h and not m)
    ratios_low = [s / p for s, p, m in zip(snrs, p95s, low) if m]
    ns_low = [n for n, m in zip(ns, low) if m]
    i_str = _argmax(ratios_low)
    strength_low = ratios_low[i_str]

    if cov_p >= 0.5 and cov_c >= 0.5:
        tok = "ALL-NUMBERS" if disc <= 3.0 else "ALL-NUMBERS-LIKE"
        txt = (f"{tok} — primes {100.0 * cov_p:.0f}% AND composites "
               f"{100.0 * cov_c:.0f}% above their P95s (disc ratio {disc:.1f})"
               + (": composites systematically quieter — kernel-limited "
                  "separation at Δω, ESCALATE L before any claim"
                  if tok == "ALL-NUMBERS-LIKE" else
                  ": composites as loud as primes — headline discovery, ESCALATE"))
    elif cov_p >= 0.5 and cov_c <= 3.0 * false_rate:
        tok = "ζ-HARMONIC ONLY"
        txt = (f"ζ-HARMONIC ONLY — primes {100.0 * cov_p:.0f}% fire, composites "
               f"silent ({100.0 * cov_c:.0f}% ≤ "
               f"{100.0 * 3.0 * false_rate:.0f}% false tail): a prime/prime-power "
               "comb, NOT all numbers")
    elif cov_p >= 0.5:
        tok = "MIXED"
        txt = (f"MIXED — primes {100.0 * cov_p:.0f}% fire, composites "
               f"{100.0 * cov_c:.0f}% partial: ζ main-lobe bleed vs a genuine "
               f"all-numbers comb is INDISTINGUISHABLE at Δω ≈ {domega:.2f} → "
               "escalate L")
    elif strength_low >= 2.0 and n_hits_high <= 3.0 * false_rate * n_high + 3:
        tok = "ISOLATED BUMP"
        txt = (f"ISOLATED BUMP — strongest low-n exceedance {strength_low:.1f}× "
               f"its P95 at log({ns_low[i_str]}), high-n band at the "
               f"{100.0 * false_rate:.0f}% false tail: a lone resonance (the "
               "regime-D log(2) story), NOT a comb")
    else:
        tok = "ABSENT"
        txt = (f"ABSENT — {n_hits}/{len(ns)} targets above P95 ≈ the "
               f"{100.0 * false_rate:.0f}% false-hit tail (no arithmetic comb "
               "in ANY class)")
    return tok, txt, cov_p, cov_pp, cov_c, n_hits, disc


def hp_h08_all_numbers(cfg: HPConfig, zeta_zeros) -> dict:
    L = cfg.hp_L
    nmax = max(10, cfg.hp_num_nmax)
    ns = list(range(2, nmax + 1))
    cls = [1 if _hp_isprime(m) else (2 if _hp_isprimepower(m) else 3) for m in ns]
    ns_p = [m for m, c in zip(ns, cls) if c == 1]
    ns_pp = [m for m, c in zip(ns, cls) if c == 2]
    ns_c = [m for m, c in zip(ns, cls) if c == 3]
    omega_targets = [math.log(m) for m in ns]
    omega_grid = _frange(0.3, 0.004, math.log(nmax) + 0.25)
    n_grid = len(omega_grid)
    snr_min = 50.0
    ctrl_min = 100.0
    false_rate = 0.05
    low_cut = 13

    def snr_of(P, med, w):
        return _hp_snr_of(P, med, w, omega_grid)

    def snrs_of_target(P, med):
        return [snr_of(P, med, w) for w in omega_targets]

    # ── stage 1: AB-cloud spectra — the SAME seed stream H1 stage 1 scanned ──
    P_ab = np.zeros(n_grid)
    n_raw = 0
    n_used = 0
    span = 0.0
    for k in range(1, cfg.hp_h1_configs + 1):
        seed = cfg.hp_seed + 100 + k
        c = _hp_std_config(cfg, L, seed)
        evals = _hp_spectrum(cfg, c)
        n_raw = len(evals)
        span = max(span, max(evals) - min(evals))
        P_ab += np.asarray(hp_raw_ft(evals, omega_grid))
        n_used += 1
    P_ab /= max(n_used, 1)
    med_ab = float(np.median(P_ab))
    snrs_ab = snrs_of_target(P_ab, med_ab)

    # ── stage 2: ζ positive control — the DISCRIMINATION test ──
    snrs_z, snrs_z_pp, snrs_z_c = [], [], []
    med_z = 1.0
    zeta_ok = False
    disc_z = float("nan")
    med_pz = float("nan")
    med_cz = 0.0
    k_sig_z = 0
    zeta_n = 0
    if not zeta_zeros:
        pass  # class discrimination UNVALIDATED → WARN
    else:
        zslice = [float(v) for v in zeta_zeros[:min(len(zeta_zeros), cfg.hp_zeta_cap)]]
        zeta_n = len(zslice)
        Pz = np.asarray(hp_raw_ft(zslice, omega_grid))
        med_z = float(np.median(Pz))
        snrs_z = [snr_of(Pz, med_z, math.log(m)) for m in ns_p]
        snrs_z_pp = [snr_of(Pz, med_z, math.log(m)) for m in ns_pp]
        snrs_z_c = [snr_of(Pz, med_z, math.log(m)) for m in ns_c]
        k_sig_z = (sum(1 for s in snrs_z if s >= ctrl_min) +
                   sum(1 for s in snrs_z_pp if s >= ctrl_min))
        med_pz = _median(snrs_z + snrs_z_pp)
        med_cz = _median(snrs_z_c) if snrs_z_c else 0.0
        disc_z = med_pz / med_cz if med_cz > 1e-300 else float("inf")
        cls_ok = k_sig_z >= max(2, (len(ns_p) + len(ns_pp)) // 2)
        disc_ok = disc_z >= 100.0
        zeta_ok = cls_ok and disc_ok

    # ── stage 3: baseline null pool → PER-TARGET P95 ──
    n_null = max(2, cfg.hp_deep_nulls)
    null_draws = []  # per draw: SNR at every target
    for i in range(1, n_null + 1):
        c0 = ABCloudConfig(L, L, [], cfg.ab_alpha_test16, cfg.ab_t, "open",
                           0.0, cfg.hp_seed + 60_000 + 700 + i, MODEL_MONUMENTAL)
        ev0 = _hp_spectrum(cfg, c0)
        P0 = np.asarray(hp_raw_ft(ev0, omega_grid))
        null_draws.append(snrs_of_target(P0, float(np.median(P0))))
    for i in range(1, n_null + 1):
        gue = _gue_matrix_eigenvalues(n_raw, seed=cfg.hp_seed + 60_000 + 800 + i)
        Pg = np.asarray(hp_raw_ft(gue, omega_grid))
        null_draws.append(snrs_of_target(Pg, float(np.median(Pg))))
    p95_ab = [_quantile([d[j] for d in null_draws], 0.95) for j in range(len(ns))]
    hits_ab = [s > p for s, p in zip(snrs_ab, p95_ab)]
    false_meas = (_mean([float(sum(1 for h, p in zip(d, p95_ab) if h > p))
                         for d in null_draws]) / len(ns))
    domega = 2.0 * PI / max(span, 1e-9)
    tok_ab, txt_ab, cov_p, cov_pp, cov_c, n_hits, disc_ab = _hp8_classify_comb(
        hits_ab, snrs_ab, p95_ab, domega, cls, ns, low_cut, false_rate)
    med_p95 = _median(p95_ab)
    # resolution honesty: the Hann main-lobe scale of the raw FT
    domega_nn = []
    for i in range(len(omega_targets)):
        if i == 0:
            domega_nn.append(omega_targets[1] - omega_targets[0])
        elif i == len(ns) - 1:
            domega_nn.append(omega_targets[-1] - omega_targets[-2])
        else:
            domega_nn.append(min(omega_targets[i + 1] - omega_targets[i],
                                 omega_targets[i] - omega_targets[i - 1]))
    n_res = sum(1 for d in domega_nn if d > domega)
    i_last_res = None
    for i in range(len(domega_nn) - 1, -1, -1):
        if domega_nn[i] > domega:
            i_last_res = i
            break
    nulls_ok = bool(len(null_draws) >= 4 and all(math.isfinite(p) for p in p95_ab)
                    and med_p95 > 0.0 and 0.0 < false_meas <= 0.20)
    top5 = sorted(range(len(snrs_ab)), key=lambda i: (-snrs_ab[i], i))[:5]

    # ── stage 4: regime sweep + DEEPEN (H1's reviewer discipline) ──
    reg_rows = []   # {key, token, cov_p, cov_pp, cov_c, txt}
    reg_ctx = {}    # key → (raw levels/config, P_r, draws_r)
    deep_info = []  # {key, deep_max, p95, n_draws, token}
    sweep_ok = True
    if cfg.hp_regime_mode == "showdown":
        sweep = [R for R in hp_regimes(cfg)
                 if not (R.nv_mode == "suite" and R.alpha_mode == "suite")]
        for j, R in enumerate(sweep, start=1):
            P_r = np.zeros(n_grid)
            n_r = 0
            n_rraw = 0
            for k in range(1, cfg.hp_h1_configs + 1):
                seed = cfg.hp_seed + 40_000 + 1_000 * j + k
                ev = _hp_spectrum(cfg, _hp_regime_config(cfg, L, seed, R))
                n_rraw = len(ev)
                P_r += np.asarray(hp_raw_ft(ev, omega_grid))
                n_r += 1
            P_r /= max(n_r, 1)
            draws_r = []
            for i in range(1, n_null + 1):  # vortex-free at the SAME regime α
                c_vf = ABCloudConfig(L, L, [], _hp_regime_alpha(cfg, R),
                                     cfg.ab_t, "open", 0.0,
                                     cfg.hp_seed + 40_000 + 1_000 * j + 700 + i,
                                     MODEL_MONUMENTAL)
                Pv = np.asarray(hp_raw_ft(_hp_spectrum(cfg, c_vf), omega_grid))
                draws_r.append(snrs_of_target(Pv, float(np.median(Pv))))
            for i in range(1, n_null + 1):  # size-matched GUE nulls
                Pg = np.asarray(hp_raw_ft(_gue_matrix_eigenvalues(
                    n_rraw, seed=cfg.hp_seed + 40_000 + 1_000 * j + 800 + i),
                    omega_grid))
                draws_r.append(snrs_of_target(Pg, float(np.median(Pg))))
            p95_r = [_quantile([d[ll] for d in draws_r], 0.95)
                     for ll in range(len(ns))]
            snrs_r = snrs_of_target(P_r, float(np.median(P_r)))
            hits_r = [s > p for s, p in zip(snrs_r, p95_r)]
            tok_r, txt_r, covp_r, covpp_r, covc_r, _, _ = _hp8_classify_comb(
                hits_r, snrs_r, p95_r, 2.0 * PI / max(span, 1e-9),
                cls, ns, low_cut, false_rate)
            reg_rows.append({"key": R.key, "token": tok_r, "cov_p": covp_r,
                             "cov_pp": covpp_r, "cov_c": covc_r, "txt": txt_r,
                             "max_snr": max(snrs_r),
                             "argmax_n": ns[_argmax(snrs_r)],
                             "desc": _hp_regime_desc(cfg, L, R),
                             "n_null_draws": len(draws_r)})
            reg_ctx[R.key] = (n_rraw, P_r.copy(), draws_r)
            sweep_ok = sweep_ok and (tok_r == "ABSENT")
        # DEEPEN: every regime whose shallow reading is anything but ABSENT
        marginal_keys = [rr["key"] for rr in reg_rows if rr["token"] != "ABSENT"]
        if marginal_keys and cfg.hp_deep_configs >= 1:
            for j, R in enumerate(sweep, start=1):
                if R.key not in marginal_keys:
                    continue
                n_rraw_d, P_r0, draws_d = reg_ctx[R.key]
                P_ext = P_r0.copy()
                n_ext = cfg.hp_h1_configs
                for i in range(1, cfg.hp_deep_configs + 1):
                    seed = cfg.hp_seed + 40_000 + 1_000 * j + 600 + i
                    ev = _hp_spectrum(cfg, _hp_regime_config(cfg, L, seed, R))
                    P_ext += np.asarray(hp_raw_ft(ev, omega_grid))
                    n_ext += 1
                P_ext /= max(n_ext, 1)
                snrs_deep = snrs_of_target(P_ext, float(np.median(P_ext)))
                p95_deep = [_quantile([d[ll] for d in draws_d], 0.95)
                            for ll in range(len(ns))]
                hits_d = [s > p for s, p in zip(snrs_deep, p95_deep)]
                tok_d, txt_d, covp_d, covpp_d, covc_d, _, _ = _hp8_classify_comb(
                    hits_d, snrs_deep, p95_deep, 2.0 * PI / max(span, 1e-9),
                    cls, ns, low_cut, false_rate)
                for rr in reg_rows:
                    if rr["key"] == R.key:
                        rr.update({"token": tok_d, "txt": txt_d, "cov_p": covp_d,
                                   "cov_pp": covpp_d, "cov_c": covc_d})
                        break
                deep_info.append({
                    "key": R.key, "deep_max": max(snrs_deep),
                    "p95": _quantile([max(d) for d in draws_d], 0.95),
                    "n_draws": len(draws_d), "token": tok_d,
                    "n_ext": n_ext, "cov_p": covp_d, "cov_c": covc_d,
                })
            sweep_ok = all(rr["token"] == "ABSENT" for rr in reg_rows)

    # ── stage 5: counting-family showdown on the RAW N(E) (H2 machinery) ──
    Lw = cfg.hp_L_weyl
    seedN = cfg.hp_seed + 60_000 + 101
    rawN = _hp_spectrum(cfg, _hp_std_config(cfg, Lw, seedN))
    refN = _hp_spectrum(cfg, ABCloudConfig(Lw, Lw, [], cfg.ab_alpha_test16,
                                           cfg.ab_t, "open", 0.0, seedN + 1,
                                           MODEL_MONUMENTAL))
    posN = [v for v in rawN if v > 1e-9]
    n_grid_weyl = _clamp(cfg.hp_weyl_grid, 20, 400)
    Eg = _linspace(posN[0], posN[-1], n_grid_weyl)
    N_raw = [float(bisect.bisect_right(posN, E)) for E in Eg]
    N_ref = [float(bisect.bisect_right(refN, E)) for E in Eg]
    npts = len(Eg)
    lw = [max(math.log(E), 0.05) for E in Eg]  # π(E) basis guard
    X0 = [[E, 1.0] for E in Eg]
    X1 = [[E * math.log(E), E, 1.0] for E in Eg]
    X2 = [[E / w, 1.0] for E, w in zip(Eg, lw)]
    X3 = [[nr, 1.0] for nr in N_ref]
    c0, rss0, r20 = _hp_linlsq(X0, N_raw); a0 = hp_aicc(npts, rss0, 2)
    c1, rss1, r21 = _hp_linlsq(X1, N_raw); a1 = hp_aicc(npts, rss1, 3)
    c2, rss2, r22 = _hp_linlsq(X2, N_raw); a2 = hp_aicc(npts, rss2, 2)
    c3, rss3, r23 = _hp_linlsq(X3, N_raw); a3 = hp_aicc(npts, rss3, 2)
    models = [
        {"name": "M0 ⌊E⌋-linear (Σ1: Tₙ↔n)", "aicc": a0, "r2": r20, "k": 2,
         "coef": c0},
        {"name": "M1 Σd(n) E·lnE-basis (ζ-basis)", "aicc": a1, "r2": r21,
         "k": 3, "coef": c1},
        {"name": "M2 π(E) E/lnE", "aicc": a2, "r2": r22, "k": 2, "coef": c2},
        {"name": "M3 lattice DOS (vortex-free)", "aicc": a3, "r2": r23, "k": 2,
         "coef": c3},
    ]
    aiccs = [m["aicc"] for m in models]
    ordered = sorted(range(len(aiccs)), key=lambda i: (aiccs[i], i))
    best_i = ordered[0]
    daicc_best = aiccs[ordered[1]] - aiccs[best_i]
    r2_best = models[best_i]["r2"]
    count_ok = bool(npts >= 30 and math.isfinite(r2_best) and r2_best >= 0.95)

    # ── stage 6: gap ↔ arithmetic correlations ──
    seedG = cfg.hp_seed + 60_000 + 600
    evG = _hp_spectrum(cfg, _hp_std_config(cfg, L, seedG))
    bandG = central_band_eigs(evG, cfg.ab_center_fraction)
    gaps = [bandG[i + 1] - bandG[i] for i in range(len(bandG) - 1)]
    m_g = len(gaps)
    d_t, om_t, phi_t, sig_t = _hp_arith_tables(m_g + 1)
    feats = [
        ("d(n)", [float(d_t[k]) for k in range(m_g)]),
        ("Ω(n)", [float(om_t[k]) for k in range(m_g)]),
        ("φ(n)", [float(phi_t[k]) for k in range(m_g)]),
        ("σ(n)", [float(sig_t[k]) for k in range(m_g)]),
        ("ln(n)", [math.log(float(x + 1)) for x in range(m_g)]),
    ]
    win_g = max(3, int(round(0.05 * m_g)))
    g_hp = hp_fluct_hp(gaps, win=win_g)
    n_shuf = max(50, cfg.hp_num_shufs)
    rng_g = MT19937RNG(cfg.hp_seed + 60_000 + 950)
    # independent GUE gap anchors FIRST — pooled into the per-function null
    anchor_rho = {}
    for k in (1, 2):
        gb = sorted(central_band_eigs(_gue_matrix_eigenvalues(
            len(bandG), seed=cfg.hp_seed + 60_000 + 900 + k), 1.0))
        gg_hp = hp_fluct_hp([gb[i + 1] - gb[i] for i in range(len(gb) - 1)],
                            win=win_g)
        for nm, f in feats:
            f_hp = hp_fluct_hp(f, win=win_g)
            anchor_rho[nm] = max(anchor_rho.get(nm, 0.0),
                                 abs(_hp_spearman(gg_hp, f_hp)))
    rho_ab = []
    bands_f = []
    for nm, f in feats:
        f_hp = hp_fluct_hp(f, win=win_g)
        rho = _hp_spearman(g_hp, f_hp)
        sh = []
        for _ in range(n_shuf):
            perm = _randperm(rng_g, m_g)
            sh.append(abs(_hp_spearman(g_hp, [f_hp[p - 1] for p in perm])))
        b95 = _quantile(sh + [anchor_rho.get(nm, 0.0)], 0.95)
        rho_ab.append(rho)
        bands_f.append(b95)
    band_g = max(bands_f)
    i_mx = _argmax([abs(r) for r in rho_ab])
    gue_rhomax = max(anchor_rho.values()) if anchor_rho else 0.0
    gap_ok = n_shuf >= 100
    gap_detected = abs(rho_ab[i_mx]) > band_g

    # ── the verdict table (H1 convention: scored = detector + method) ──
    zeta_row_detail = ("skipped — no zeros loaded" if not zeta_zeros else
                       f"prime-class comb "
                       f"{'confirmed' if sum(1 for s in snrs_z + snrs_z_pp if s >= ctrl_min) >= max(2, (len(ns_p) + len(ns_pp)) // 2) else 'NOT confirmed'}; "
                       f"discrimination ratio {disc_z:.1e} (composites ≥100× "
                       "quieter) → detector "
                       + ("valid" if disc_z >= 100.0 else
                          "INVALID — classes unresolvable at this cap/resolution"))
    rows = [
        ["ζ control discriminates (D1)", zeta_ok, zeta_row_detail],
        ["null calibration (per-target P95)", nulls_ok,
         f"{len(null_draws)} draws ({n_null} vortex-free + {n_null} GUE), "
         f"per-target P95 median {med_p95:.2f}; measured null tail "
         f"{100.0 * false_meas:.1f}% (target ≈ {100.0 * false_rate:.0f}%)"],
        ["integer comb verdict (headline)", True,
         f"baseline: {tok_ab} — primes {100.0 * cov_p:.0f}%, powers "
         f"{100.0 * cov_pp:.0f}%, composites {100.0 * cov_c:.0f}% above their "
         f"P95s; disc {disc_ab:.2f}"],
        ["comb regime-robust (sweep)", sweep_ok,
         "skipped — :" + cfg.hp_regime_mode + " mode (single HP-standard point)"
         if not reg_rows else
         "tokens per regime: "
         + " ".join(f"[{rr['key']}] {rr['token']} (composites "
                    f"{100.0 * rr['cov_c']:.0f}%)" for rr in reg_rows)
         + ("" if not deep_info else
            " DEEPENED: " + ", ".join(f"[{di['key']}] {di['token']}"
                                      for di in deep_info))],
        ["counting-family fits (N(E))", count_ok,
         f"winner {models[best_i]['name']} (R² {r2_best:.5f}"
         + ("" if r2_best >= 0.95 else " < the 0.95 floor")
         + f") by {daicc_best:.1f} AICc over the runner-up"
         + ("" if daicc_best > 10.0 else " — INCONCLUSIVE (|Δ| ≤ 10)")],
        ["gap↔arithmetic correlations", gap_ok,
         f"max |ρ| {abs(rho_ab[i_mx]):.4f} ({feats[i_mx][0]}) vs pooled null "
         f"band {band_g:.4f} ({n_shuf} shuffles ∪ 2 GUE anchors); anchors max "
         f"{gue_rhomax:.4f}"
         + ("" if n_shuf >= 100 else
            " — <100 shuffles, band noisy (method WARN)")],
    ]
    ok = bool(zeta_ok and nulls_ok and sweep_ok and count_ok and gap_ok)
    return {
        "id": 8, "name": GATE_NAME[8], "ok": ok,
        "verdict": "PASS" if ok else "WARN",
        "rows": rows,
        "L": L, "nmax": nmax, "n_targets": len(ns),
        "n_primes": len(ns_p), "n_prime_powers": len(ns_pp),
        "n_composites": len(ns_c),
        "n_grid": n_grid, "omega_max": omega_grid[-1],
        "snr_min": snr_min, "ctrl_min": ctrl_min,
        "false_rate": false_rate, "low_cut": low_cut,
        "n_configs": n_used, "n_raw": n_raw, "span": span, "med_ab": med_ab,
        "snrs_ab": snrs_ab, "p95_ab": p95_ab, "hits_ab": hits_ab,
        "cov_p": cov_p, "cov_pp": cov_pp, "cov_c": cov_c,
        "n_hits": n_hits, "disc_ab": disc_ab,
        "tok_ab": tok_ab, "txt_ab": txt_ab, "med_p95": med_p95,
        "false_meas": false_meas, "domega": domega, "n_resolved": n_res,
        "n_res_max_n": ns[i_last_res] if i_last_res is not None else None,
        "top5": [{"n": ns[i], "omega": omega_targets[i], "snr": snrs_ab[i],
                  "hit": hits_ab[i]} for i in top5],
        "zeta_n": zeta_n, "med_z": med_z, "med_pz": med_pz, "med_cz": med_cz,
        "snrs_z": snrs_z, "snrs_z_pp": snrs_z_pp, "snrs_z_c": snrs_z_c,
        "k_sig_z": k_sig_z, "disc_z": disc_z, "zeta_ok": zeta_ok,
        "null_n_draws": len(null_draws), "null_n_vf": n_null,
        "null_n_gue": n_null, "nulls_ok": nulls_ok,
        "sweep_ok": sweep_ok, "regimes": reg_rows, "deep": deep_info,
        "counting": {"models": models, "best_idx": best_i,
                     "best_name": models[best_i]["name"],
                     "daicc_best": daicc_best, "r2_best": r2_best,
                     "count_ok": count_ok, "npts": npts,
                     "n_pos": len(posN)},
        "gaps": {"m_g": m_g, "win_g": win_g, "n_shuf": n_shuf,
                 "feat_names": [nm for nm, _ in feats],
                 "rho_ab": rho_ab, "bands": bands_f, "band_g": band_g,
                 "max_rho": abs(rho_ab[i_mx]), "max_feat": feats[i_mx][0],
                 "gue_rhomax": gue_rhomax, "gap_detected": gap_detected,
                 "gap_ok": gap_ok},
    }


# ═════════════════════════════════════════════════════════════════════════════
# §8. Battery orchestration (computation-only run_battery_core, Julia L7112)
# ═════════════════════════════════════════════════════════════════════════════

# Console identity: unique gate names (Julia GATE_NAME L6770)
GATE_NAME = {
    1: "PRIME-TRACE", 2: "WEYL-DOS", 3: "POWER-LAW", 4: "CRITICAL-Q",
    5: "REGIME-2×2", 6: "HERMIT-STRESS", 7: "SEQ-CORR", 8: "NUM-TRACE",
}
# (smoke, fast, full), minutes (Julia GATE_MIN L6773, v24.3 honesty fix)
GATE_MIN = {
    1: (0.4, 120.0, 30.0), 2: (0.15, 5.0, 2.0), 3: (0.3, 10.0, 8.0),
    4: (0.2, 75.0, 20.0), 5: (0.4, 80.0, 25.0), 6: (0.5, 40.0, 12.0),
    7: (0.05, 5.0, 3.0), 8: (0.6, 130.0, 40.0),
}

_GATE_RUNNERS = {
    1: hp_h01_berry_keating,
    2: hp_h02_weyl_law,
    3: hp_h03_power_law,
    4: hp_h04_critical_q,
    5: hp_h05_ensemble,
    6: hp_h06_stability,
    7: hp_h07_sequence_correlation,
    8: hp_h08_all_numbers,
}


def _default_zeros_path() -> str:
    """zeros50k.txt next to the Julia script — here three levels above the
    package (ports/python/abcloud → meridian-spectral-observatory)."""
    return str(Path(__file__).resolve().parents[2] / "zeros50k.txt")


def load_zeros(path) -> list:
    """Julia load_zeros (L6747): whitespace-separated floats, '#' comments
    skipped; missing file → empty list (gates skip their ζ side honestly)."""
    try:
        with open(os.fspath(path), "r", encoding="utf-8", errors="replace") as fh:
            text = fh.read()
    except OSError:
        return []
    out = []
    for tok in text.split():
        if not tok or tok.startswith("#"):
            continue
        try:
            out.append(float(tok))
        except ValueError:
            pass
    return out


def run_battery(cfg: HPConfig, gates=(1, 2, 3, 4, 5, 6, 7, 8), zeros=None) -> list:
    """Computation-only equivalent of run_battery_core (Julia L7112): ζ load →
    per-gate runner → per-gate result dict.  NO console/report/telemetry: no
    rep_*, no _mr_*, no HTML/PNG, no result dirs.  Verdicts are the gates' own
    detector-validity booleans (PASS/WARN; FAIL only on an exception — the
    Julia runner's _hp_run! semantics)."""
    if zeros is None:
        zeta = load_zeros(_default_zeros_path())
    elif isinstance(zeros, (str, bytes, os.PathLike)):
        zeta = load_zeros(os.fspath(zeros))
    else:
        zeta = [float(v) for v in zeros]
    out = []
    for k in gates:
        k = int(k)
        fn = _GATE_RUNNERS.get(k)
        if fn is None:
            out.append({"id": k, "name": GATE_NAME.get(k, "?"), "ok": False,
                        "verdict": "FAIL", "error": f"no audit H{k}"})
            continue
        try:
            res = fn(cfg, zeta)
            res["verdict"] = "PASS" if res.get("ok") else "WARN"
            out.append(res)
        except Exception as exc:  # noqa: BLE001 — Julia: EXCEPTION → FAIL
            out.append({"id": k, "name": GATE_NAME.get(k, "?"), "ok": False,
                        "verdict": "FAIL", "error": f"{type(exc).__name__}: {exc}"})
    return out


def smoke_test() -> list:
    """Cheap end-to-end check: gates H1 + H7 on the smoke preset (L=20,
    smoke-shrunk controls) with the first 2000 zeros from ../../../zeros50k.txt
    (relative to the package).  Returns the per-gate result dicts."""
    zeta = load_zeros(_default_zeros_path())[:2000]
    cfg = make_hp_config()
    apply_preset(cfg, "smoke")
    return run_battery(cfg, gates=(1, 7), zeros=zeta)
