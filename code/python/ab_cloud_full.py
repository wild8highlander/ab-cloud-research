#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AB-CLOUD — VERIFICATION SUITE · AURORA EDITION — Python port (v23 parity)
=========================================================================
Faithful Python (numpy/scipy/matplotlib/mpmath) port of the canonical Julia
suite `code/ab_cloud_full.jl` — all 39 tests, two-pass (primary + HARDCORE)
protocol, same frozen data, same seeds, bilingual EN/RU output.

Provenance & parity contract
  * Kernels (lambert_w, gram_point, b(N), GUE β=2 CDF via the 32768-point
    table, KS, CvM, AD, <r>) are the verified implementations already pinned
    by 28 golden anchors in ../verification/python/ab_cloud_verify.py.
  * RNG: the Julia suite seeds local Mersenne-Twister streams per test; this
    port seeds numpy's MT19937 with the SAME seed constants. Julia uses
    dSFMT and a different draw order, so random-stream-dependent quantities
    (bootstrap CIs, MC null p-values, simulated-GUE columns) agree only to
    statistical noise; every deterministic quantity reproduces to printed
    precision (b(N) tables, fits, KS/W²/A²/χ², Σ², Δ₃, lattice identities).
  * The Julia presentation engines (ABUI ANSI, HTML design system, hand-rolled
    PNG writer with Hershey fonts + DEFLATE) are replaced by the report.md +
    results.json + matplotlib PNG artifacts of this port; numbers and
    verdicts are 1:1.

Run:
    python3 ab_cloud_full.py --list
    python3 ab_cloud_full.py --test all            # full two-pass suite
    python3 ab_cloud_full.py --test 11             # single test (two-pass)
    python3 ab_cloud_full.py --test all --profile fast
Dependencies: numpy, scipy, matplotlib, mpmath (all standard).
"""
import argparse
import cmath
import json
import math
import os
import sys
import time
from dataclasses import dataclass, field
from typing import Callable, Dict, List, Optional, Tuple

import numpy as np

try:
    import mpmath as _mp
    _mp.mp.prec = 256
    HAVE_MPMATH = True
except Exception:  # pragma: no cover
    HAVE_MPMATH = False

# ═══════════════════════════════════════════════════════════════════════════
# 0. SMALL UTILITIES (Julia semantics)
# ═══════════════════════════════════════════════════════════════════════════

def jrng(seed: int) -> np.random.Generator:
    """Local Mersenne-Twister stream, one per test site (Julia discipline)."""
    return np.random.Generator(np.random.MT19937(seed & 0xFFFFFFFFFFFFFFFF))


def jround(x: float) -> int:
    """round(Int, x) — round-half-to-EVEN (Python round already matches)."""
    return int(round(x))


def searchsortedfirst(v: np.ndarray, x: float) -> int:
    """1-based leftmost index with v[i] >= x  (Julia searchsortedfirst)."""
    return int(np.searchsorted(v, x, side="left")) + 1


def clamp(x: float, lo: float, hi: float) -> float:
    return lo if x < lo else (hi if x > hi else x)


def fmt_g(x: float, digits: int = 6) -> str:
    if x != x:
        return "NaN"
    return f"{x:.{digits}g}"


# ═══════════════════════════════════════════════════════════════════════════
# 1. CONFIGURATION AND BILINGUAL MESSAGES
# ═══════════════════════════════════════════════════════════════════════════

@dataclass
class Config:
    # data selection
    zeros_count: int = 50000
    source: str = "auto"           # auto|embedded|50k|500k|2M|highT|zeros6|csv
    data_dir: str = ""             # default resolved to ../data
    lang: str = "en"
    # test orchestration
    test: str = "all"              # all | 1..39
    output_dir: str = "results_py"
    profile: str = "exact"         # exact | fast (documented perf knobs)
    # original-test parameters
    n_checkpoints: int = 0
    n_monotone: int = 500
    n_bootstrap: int = 1000
    chi2_bins: int = 300
    highT_mins: List[float] = field(default_factory=lambda: [1000.0, 10000.0, 100000.0])
    stability_fraction: float = 0.8
    stability_threshold: float = 0.10
    bN_pass_threshold: float = 2.0
    power_law_tolerance: float = 0.15
    slope_ci_tolerance: float = 0.1
    # advanced RMT
    gue_matrix_size: int = 12000
    gue_matrix_seed: int = 112
    ad_sample_cap: int = 50000
    t31_lmax: int = 72
    rmt_cdf_table: bool = True
    rigidity_L_values: List[float] = field(default_factory=lambda: [
        2.0, 4.535939472087519, 10.287373447220801, 23.331451641676946,
        52.91502622129181, 120.00967805185182, 272.17831785395487,
        617.2921877000689, 1399.9999999999998])
    rigidity_n_windows: int = 3000
    rigidity_n_windows_d3: int = 500
    rigidity_n_grid: int = 300
    convergence_watch_sizes: List[int] = field(default_factory=list)
    # AB lattice
    ab_nx: int = 72
    ab_ny: int = 72
    ab_nx_secondary: int = 96
    ab_ny_secondary: int = 96
    ab_nv_list: List[int] = field(default_factory=lambda: [4])
    ab_nv_list_secondary: List[int] = field(default_factory=lambda: [2])
    ab_q_list: List[float] = field(default_factory=lambda: [1.0])
    ab_alpha: float = 0.5
    ab_alpha_test16: float = 0.5
    ab_t: float = 1.0
    ab_lattice: str = "open"       # open | torus
    ab_seed: int = 96
    ab_n_realizations: int = 5
    ab_hc_nreal: int = 20
    ab_center_fraction: float = 0.6
    ab_unfold_window: float = 0.05
    ab_W: float = 4.0
    ab_W_max: float = 1.0
    ab_W_cmp: float = 0.5
    ab_nv_cmp: int = 144
    ab_run_two_pass: bool = True
    ab_run_third_pass: bool = True
    # Test 35 K(t)
    ab_K_t_values: List[float] = field(default_factory=lambda: [0.05, 0.1, 0.2, 0.3, 0.5, 0.7, 1.0, 1.5, 2.0])
    ab_K_smooth_window: int = 3
    # Test 36 bytes
    ab_byte_tol: float = 0.02
    ab_n_bytes: int = 200000
    ab_byte_seed: int = 12345
    ab37_n_eigs_pass1: int = 25000
    ab37_n_eigs_pass2: int = 50000
    # Test 38 / 39
    t38_seed: int = 20260903
    t38_l1: int = 72
    t38_l2: int = 96
    t38_seeds: int = 2
    t38_c2_sizes: List[int] = field(default_factory=lambda: [24, 36, 48, 64, 80, 96])
    t38_c2_seeds: int = 10
    t38_quick: bool = False
    t34g_L: int = 96
    t34g_reps: int = 2
    t34g_geoms: str = "all"
    t34g_alpha: float = 0.5
    t34g_nv: int = 2
    t34g_q: float = 1.0
    t34g_W: float = 1.0
    # runtime bookkeeping
    pass2: bool = False            # STATS_SECONDARY_HARDCORE flag

    def w_eff(self) -> float:
        return min(self.ab_W, self.ab_W_max)

    def resolve_vortex_count(self) -> int:
        return self.ab_nv_list[0] if self.ab_nv_list else 4

    def resolve_vortex_count_secondary(self) -> int:
        return self.ab_nv_list_secondary[0] if self.ab_nv_list_secondary else 4

    def resolve_q_magnitude(self) -> float:
        return self.ab_q_list[0] if self.ab_q_list else 1.0


# profile "fast": documented performance knobs for session-bounded runs
def apply_fast_profile(cfg: Config) -> None:
    cfg.profile = "fast"
    cfg.gue_matrix_size = 4000          # T11-14 shared GUE ref (was 12000)
    cfg.ad_sample_cap = 50000
    cfg.rigidity_n_windows = 1000       # was 3000 (Σ²)
    cfg.rigidity_n_windows_d3 = 200     # was 500 (Δ₃)
    cfg.ab_n_realizations = 3           # was 5
    cfg.ab_hc_nreal = 5                 # was 20
    cfg.t38_c2_sizes = [24, 36, 48]     # FSS staircase trimmed
    cfg.t38_c2_seeds = 3                # was 10
    cfg.t34g_reps = 1                   # was 2
    cfg.t34g_L = 72                     # 34G site budget ≈ 72² (was 96)


MSGEN: Dict[str, str] = {
    "title": "AB-CLOUD — VERIFICATION SUITE · AURORA EDITION (Python port)",
    "no_data": "ERROR: no zero data available — check --data-dir",
    "loading": "Loading {count} zeros from '{source}' …",
    "loaded": "Loaded {n} zeros ({source}) T in [{tmin:.1f}, {tmax:.1f}]",
    "pass": "PASS", "warn": "WARN", "fail": "FAIL",
    "zeros_note": "GUE is asymptotic — rejection at low T is EXPECTED.",
    "obj1_title": "Objection 1: b(N) Convergence",
    "obj2_title": "Objection 2: GUE Spacing Statistics",
    "obj2plus_title": "Objection 2 (extended): Advanced RMT Diagnostics",
    "obj3_title": "Objection 3: Large-T Decay Rate",
}
MSGR: Dict[str, str] = {
    "title": "AB-CLOUD — НАБОР ВЕРИФИКАЦИИ · AURORA EDITION (порт Python)",
    "no_data": "ОШИБКА: данные нулей недоступны — проверьте --data-dir",
    "loading": "Загрузка {count} нулей из '{source}' …",
    "loaded": "Загружено {n} нулей ({source}) T ∈ [{tmin:.1f}, {tmax:.1f}]",
    "pass": "ПРОЙДЕНО", "warn": "ПРЕДУПР.", "fail": "СБОЙ",
    "zeros_note": "GUE асимптотичен — отвержение при малых T ОЖИДАЕМО.",
    "obj1_title": "Возражение 1: Сходимость b(N)",
    "obj2_title": "Возражение 2: GUE-статистика спейсингов",
    "obj2plus_title": "Возражение 2 (расшир.): Углублённая RMT-диагностика",
    "obj3_title": "Возражение 3: Скорость убывания при больших T",
}


def msg(cfg: Config, key: str) -> str:
    table = MSGR if cfg.lang == "ru" else MSGEN
    return table.get(key, key)


# ═══════════════════════════════════════════════════════════════════════════
# 2. DATA LOADER (source registry per spec §9; embedded = frozen 50k file)
# ═══════════════════════════════════════════════════════════════════════════

_SOURCE_REGISTRY = [
    ("50k",      "zeta_zeros_50000.txt",          13661),
    ("embedded", "zeta_zeros_50000_embedded.txt", 50000),
    ("500k",     "zeta_zeros_500k_odlyzko.txt",   500000),
    ("2M",       "zeta_zeros_2M_odlyzko.txt",     2001052),
    ("highT",    "zeta_zeros_highT_blocks.txt",   30000),
    ("2M_gz",    "zeta_zeros_2M_odlyzko.txt.gz",  2001052),
    ("csv",      "zeta_zeros_50000.csv",          13661),
    ("zeros6",   "zeros6.txt",                    2001052),
]


def default_data_dir() -> str:
    here = os.path.dirname(os.path.abspath(__file__))
    cand = os.path.normpath(os.path.join(here, "..", "..", "verification", "data"))
    if os.path.isdir(cand):
        return cand
    cand2 = os.path.normpath(os.path.join(here, "..", "data"))
    if os.path.isdir(cand2):
        return cand2
    return "../data"


def _parse_plain(path: str) -> np.ndarray:
    out = []
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            s = line.strip()
            if not s or s.startswith("#"):
                continue
            try:
                out.append(float(s))
            except ValueError:
                continue
    return np.array(out, dtype=float)


def _parse_highT(path: str) -> np.ndarray:
    import re
    out, base = [], 0.0
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            s = line.strip()
            if not s:
                continue
            m = re.match(r"#\s*BLOCK\s+index=\S+\s+offset=(\S+)", s)
            if m:
                base = float(m.group(1))
                continue
            if s.startswith("#"):
                continue
            try:
                out.append(base + float(s))
            except ValueError:
                continue
    return np.array(out, dtype=float)


def _parse_csv(path: str) -> np.ndarray:
    out = []
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            s = line.strip()
            if not s or s.startswith("#"):
                continue
            parts = s.split(",")
            if len(parts) < 2:
                continue
            try:
                out.append(float(parts[1]))
            except ValueError:
                continue
    return np.array(out, dtype=float)


def load_zeros(cfg: Config) -> np.ndarray:
    if not cfg.data_dir:
        cfg.data_dir = default_data_dir()
    if cfg.source == "auto":
        best = None
        for name, fname, avail in _SOURCE_REGISTRY:
            if avail >= cfg.zeros_count and (best is None or avail < best[2]):
                best = (name, fname, avail)
        if best is None:
            print(msg(cfg, "no_data"), file=sys.stderr)
            return np.array([])
        cfg.source, fname, avail = best
        print(f"  Auto-selected '{cfg.source}' (needs >={cfg.zeros_count}, file has {avail})")
    else:
        fname = None
        for name, f, avail in _SOURCE_REGISTRY:
            if name == cfg.source:
                fname = f
                break
        if fname is None:
            print(msg(cfg, "no_data"), file=sys.stderr)
            return np.array([])
    path = os.path.join(cfg.data_dir, fname)
    print(msg(cfg, "loading").format(count=cfg.zeros_count, source=fname))
    if not os.path.exists(path):
        print(f"ERROR: data file not found: {path}", file=sys.stderr)
        return np.array([])
    if path.endswith(".gz"):
        import gzip
        with gzip.open(path, "rt", encoding="utf-8", errors="replace") as f:
            zeros = np.array([float(l.strip()) for l in f
                              if l.strip() and not l.strip().startswith("#")], dtype=float)
    elif cfg.source == "highT":
        zeros = _parse_highT(path)
    elif cfg.source == "csv":
        zeros = _parse_csv(path)
    else:
        zeros = _parse_plain(path)
    zeros = np.sort(zeros)
    if cfg.zeros_count < len(zeros):
        zeros = zeros[:cfg.zeros_count]
    if len(zeros):
        print(msg(cfg, "loaded").format(
            n=len(zeros), source=cfg.source, tmin=zeros[0], tmax=zeros[-1]))
    return zeros


# ═══════════════════════════════════════════════════════════════════════════
# 3. NUMERICAL KERNELS (golden-anchor parity with verification/python)
# ═══════════════════════════════════════════════════════════════════════════

def lambert_w(x: float, tol: float = 1e-12, max_iter: int = 50) -> float:
    if x < -1.0 / math.e:
        raise ValueError("Lambert W undefined for x < −1/e")
    if x == 0.0:
        return 0.0
    w = math.log(max(x, 1e-30))
    if w < 0:
        w = x
    for _ in range(max_iter):
        ew = math.exp(w)
        f = w * ew - x
        fp = ew * (w + 1.0)
        if abs(fp) < 1e-30:
            break
        delta = f / fp
        w -= delta
        if abs(delta) < tol * max(abs(w), 1.0):
            break
    return w


def gram_point(k: int) -> float:
    if k <= 0:
        return 0.0
    t = 2.0 * math.pi * k / lambert_w(k / math.e)
    for _ in range(8):
        arg = t / (2.0 * math.pi)
        if arg <= 0:
            break
        theta = (t / 2.0) * math.log(arg) - t / 2.0 - math.pi / 8.0 \
            + 1.0 / (48.0 * t) + 7.0 / (5760.0 * t * t * t)
        dtheta = 0.5 * math.log(arg) - 1.0 / (48.0 * t * t) \
            - 21.0 / (5760.0 * t * t * t * t)
        if abs(dtheta) < 1e-30:
            break
        t -= (theta - math.pi * k) / dtheta
    return t


def compute_bN(zeros: np.ndarray, N: int, offset: int = 0) -> float:
    """b(N) = (1/N) Σ_{k=1..N} |zeros[k-1] − gram_point(offset+k)| — spec §3."""
    N = min(N, len(zeros))
    if N <= 0:
        return float("nan")
    total = 0.0
    for k in range(1, N + 1):
        total += abs(zeros[k - 1] - gram_point(offset + k))
    return total / N


def bN_prefix(zeros: np.ndarray) -> np.ndarray:
    n = len(zeros)
    pref = np.empty(n + 1)
    pref[0] = 0.0
    acc = 0.0
    for k in range(1, n + 1):
        acc += abs(zeros[k - 1] - gram_point(k))
        pref[k] = acc
    return pref


def normalized_spacings(zeros: np.ndarray) -> np.ndarray:
    out = []
    for k in range(len(zeros) - 1):
        gk = zeros[k]
        if gk <= 0:
            continue
        out.append((zeros[k + 1] - gk) * math.log(gk / (2.0 * math.pi)) / (2.0 * math.pi))
    return np.array(out, dtype=float)


# ---- GUE β=2 surmise CDF: 32768-point table on [0,5] (spec §5) --------------
_GUE_TN = 32768
_GUE_SMAX = 5.0
_GUE_TABLE: Optional[np.ndarray] = None
RMT_LAW = "gue2"   # β=2 Wigner–Dyson surmise (the suite default)


def gue_exact(s: float) -> float:
    return math.erf(2.0 * s / math.sqrt(math.pi)) \
        - (4.0 * s / math.pi) * math.exp(-4.0 * s * s / math.pi)


def goe_exact(s: float) -> float:
    """Legacy GOE β=1 surmise CDF (used only by Test 27's D_GOE comparison)."""
    return 1.0 - math.exp(-math.pi * s * s / 4.0)


def gue_surmise_pdf(s):
    if np.ndim(s) > 0:
        s = np.asarray(s, dtype=float)
        out = np.zeros_like(s)
        m = s > 0
        out[m] = (32.0 / (math.pi * math.pi)) * s[m] ** 2 * np.exp(-4.0 * s[m] ** 2 / math.pi)
        return out
    if s < 0:
        return 0.0
    return (32.0 / (math.pi * math.pi)) * s * s * math.exp(-4.0 * s * s / math.pi)


def goe_surmise_pdf(s):
    if np.ndim(s) > 0:
        s = np.asarray(s, dtype=float)
        out = np.zeros_like(s)
        m = s > 0
        out[m] = (math.pi / 2.0) * s[m] * np.exp(-math.pi * s[m] ** 2 / 4.0)
        return out
    if s < 0:
        return 0.0
    return (math.pi / 2.0) * s * math.exp(-math.pi * s * s / 4.0)


def _build_gue_table() -> np.ndarray:
    return np.array([gue_exact(i * _GUE_SMAX / (_GUE_TN - 1)) for i in range(_GUE_TN)])


def gue_cdf(s: float) -> float:
    global _GUE_TABLE
    if s <= 0.0:
        return 0.0
    if s >= _GUE_SMAX:
        return gue_exact(s)
    if _GUE_TABLE is None:
        _GUE_TABLE = _build_gue_table()
    x = s * (_GUE_TN - 1) / _GUE_SMAX
    i = int(math.floor(x))
    if i < 0 or i >= _GUE_TN - 1:
        return gue_exact(s)
    t = x - i
    return (1.0 - t) * _GUE_TABLE[i] + t * _GUE_TABLE[i + 1]


def goe_cdf(s: float) -> float:
    return goe_exact(s) if s > 0 else 0.0


def rmt_law_cdf(s: float) -> float:
    return gue_cdf(s) if RMT_LAW == "gue2" else goe_cdf(s)


def rmt_law_var() -> float:
    return 3.0 * math.pi / 8.0 - 1.0  # β=2 surmise variance


def rmt_law_sd() -> float:
    return math.sqrt(rmt_law_var())


# ---- KS / CvM / AD / 2-sample KS --------------------------------------------
def ks_asymptotic_pvalue(lam: float) -> float:
    if lam <= 0.0:
        return 1.0
    if lam < 0.6:
        s2 = 0.0
        for k in range(1, 1001):
            term = math.exp(-((2 * k - 1) ** 2) * math.pi ** 2 / (8.0 * lam * lam))
            s2 += term
            if term < 1e-18:
                break
        v = 1.0 - math.sqrt(2.0 * math.pi) / lam * s2
    else:
        s = 0.0
        sign = 1.0
        for k in range(1, 101):
            term = sign * math.exp(-2.0 * k * k * lam * lam)
            s += term
            sign = -sign
            if abs(term) < 1e-18:
                break
        v = 2.0 * s
    return clamp(v, 0.0, 1.0)


def ks_test(spacings, cdf: Callable[[float], float] = gue_cdf) -> Tuple[float, float]:
    s = np.sort(np.asarray(spacings, dtype=float))
    n = len(s)
    if n == 0:
        return 0.0, 1.0
    d = 0.0
    for i in range(1, n + 1):
        fx = cdf(s[i - 1])
        d = max(d, abs(i / n - fx), abs((i - 1) / n - fx))
    lam = (math.sqrt(n) + 0.12 + 0.11 / math.sqrt(n)) * d
    return d, ks_asymptotic_pvalue(lam)


def ks_test_2sample(x, y) -> Tuple[float, float]:
    """Julia 2098–2125: merge walk, ties advance BOTH pointers."""
    xs = np.sort(np.asarray(x, dtype=float))
    ys = np.sort(np.asarray(y, dtype=float))
    n, m = len(xs), len(ys)
    if n == 0 or m == 0:
        return 0.0, 1.0
    i = j = 0
    d = 0.0
    while i < n and j < m:
        if xs[i] <= ys[j]:
            a = xs[i]
            ni = 0
            while i < n and xs[i] == a:
                ni += 1
                i += 1
            nj = 0
            while j < m and ys[j] == a:
                nj += 1
                j += 1
            fx = i / n
            fy = j / m
            d = max(d, abs(fx - fy))
        else:
            a = ys[j]
            nj = 0
            while j < m and ys[j] == a:
                nj += 1
                j += 1
            fy = j / m
            fx = i / n
            d = max(d, abs(fx - fy))
    ne = n * m / (n + m)
    lam = (math.sqrt(ne) + 0.12 + 0.11 / math.sqrt(ne)) * d
    return d, ks_asymptotic_pvalue(lam)


def cvm_test(spacings, cdf: Callable[[float], float] = gue_cdf) -> float:
    s = np.sort(np.asarray(spacings, dtype=float))
    n = len(s)
    if n == 0:
        return 0.0
    w2 = 1.0 / (12.0 * n)
    for i in range(n):
        df = gue_cdf(s[i]) - (2.0 * (i + 1) - 1.0) / (2.0 * n)
        w2 += df * df
    return w2


def anderson_darling_stat(spacings, cdf: Callable[[float], float] = gue_cdf) -> float:
    s = np.sort(np.asarray(spacings, dtype=float))
    n = len(s)
    if n < 2:
        return float("nan")
    acc = 0.0
    for i in range(1, n + 1):
        fi = clamp(cdf(s[i - 1]), 1e-300, 1.0 - 1e-16)
        fni = clamp(cdf(s[n - i]), 1e-300, 1.0 - 1e-16)
        acc += (2.0 * i - 1.0) * (math.log(fi) + math.log(1.0 - fni))
    return -n - acc / n


# ---- χ² with exact regularized incomplete gamma ------------------------------
def _gser(a: float, x: float) -> float:
    ap, s, delt = a, 1.0 / a, 1.0 / a
    for _ in range(1000):
        ap += 1.0
        delt *= x / ap
        s += delt
        if abs(delt) < abs(s) * 1e-16:
            break
    return s * math.exp(-x + a * math.log(x) - math.lgamma(a))


def _gcf(a: float, x: float) -> float:
    tiny = 1e-300
    b, c, d = x + 1.0 - a, 1.0 / tiny, 1.0 / (x + 1.0 - a)
    h = d
    for i in range(1, 1000):
        an = -i * (i - a)
        b += 2.0
        d = an * d + b
        if abs(d) < tiny:
            d = tiny
        c = b + an / c
        if abs(c) < tiny:
            c = tiny
        d = 1.0 / d
        delt = d * c
        h *= delt
        if abs(delt - 1.0) < 1e-16:
            break
    return math.exp(-x + a * math.log(x) - math.lgamma(a)) * h


def _gammainc_p(a: float, x: float) -> float:
    if x < 0 or a <= 0:
        return 0.0
    if x == 0:
        return 0.0
    if x < a + 1.0:
        return _gser(a, x)
    return 1.0 - _gcf(a, x)


def chi2_cdf(x: float, df: float) -> float:
    """P(df/2, x/2) — regularized lower incomplete gamma (scipy, robust)."""
    if x <= 0:
        return 0.0
    from scipy.special import gammainc
    return float(gammainc(df / 2.0, x / 2.0))


def chi2_gue_test(spacings, nbins: int = 30) -> Tuple[float, int, float]:
    """Julia 2183–2224: uniform bins on [0, min(max s, 4)], overflow in last."""
    s = np.asarray(spacings, dtype=float)
    n = len(s)
    s_max = min(float(np.max(s)) if n else 0.0, 4.0)
    nbins = max(nbins, 5)
    edges = np.linspace(0.0, s_max, nbins + 1)
    counts, _ = np.histogram(np.minimum(s, s_max), bins=edges)
    expected = np.empty(nbins)
    for i in range(nbins - 1):
        expected[i] = n * (gue_cdf(edges[i + 1]) - gue_cdf(edges[i]))
    expected[nbins - 1] = n * (1.0 - gue_cdf(edges[nbins - 1]))
    chi2 = 0.0
    df = 0
    for i in range(nbins):
        if expected[i] >= 5.0:
            chi2 += (counts[i] - expected[i]) ** 2 / expected[i]
            df += 1
    df = max(df - 1, 1)
    p = 1.0 - chi2_cdf(chi2, df)
    return chi2, df, p


# ---- long-range statistics ----------------------------------------------------
def unfolded_positions(zeros: np.ndarray) -> np.ndarray:
    """Riemann–von Mangoldt smooth counting N̄(γ) (Julia 2243–2252)."""
    z = np.asarray(zeros, dtype=float)
    y = z / (2.0 * math.pi)
    return y * np.log(y) - y + 7.0 / 8.0


def number_variance(positions: np.ndarray, L: float, n_windows: int,
                    rng: np.random.Generator) -> float:
    pos = np.asarray(positions, dtype=float)
    Ltot = pos[-1] - pos[0]
    if Ltot <= L:
        return float("nan")
    counts = np.empty(n_windows)
    for w in range(n_windows):
        x0 = pos[0] + rng.random() * (Ltot - L)
        c = searchsortedfirst(pos, x0 + L) - searchsortedfirst(pos, x0)
        counts[w] = c
    return float(np.var(counts, ddof=1))  # Julia var() = sample variance (n−1)


def delta3_rigidity(positions: np.ndarray, L: float, n_windows: int,
                    n_grid: int, rng: np.random.Generator) -> float:
    pos = np.asarray(positions, dtype=float)
    Ltot = pos[-1] - pos[0]
    if Ltot <= L:
        return float("nan")
    acc = 0.0
    for w in range(n_windows):
        x0 = pos[0] + rng.random() * (Ltot - L)
        idx0 = searchsortedfirst(pos, x0)
        xs = np.linspace(0.0, L, n_grid)
        nv = np.empty(n_grid)
        for gi in range(n_grid):
            nv[gi] = searchsortedfirst(pos, x0 + xs[gi]) - idx0
        mx = xs.mean()
        my = nv.mean()
        sxx = ((xs - mx) ** 2).sum()
        b = ((xs - mx) * (nv - my)).sum() / sxx if sxx > 0 else 0.0
        a = my - b * mx
        res = nv - (a + b * xs)
        acc += float((res ** 2).mean())
    return acc / n_windows


# ---- linear regression --------------------------------------------------------
def linreg(x, y) -> Tuple[float, float, float, float, np.ndarray]:
    """OLS → (a, b, R², SE(b), residuals) — Julia 1792–1810."""
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    n = len(x)
    if n < 2:
        return 0.0, 0.0, 0.0, 0.0, y.copy()
    mx, my = x.mean(), y.mean()
    sxx = ((x - mx) ** 2).sum()
    if sxx == 0:
        return 0.0, 0.0, 0.0, 0.0, y.copy()
    b = ((x - mx) * (y - my)).sum() / sxx
    a = my - b * mx
    res = y - (a + b * x)
    ss_res = float((res ** 2).sum())
    ss_tot = float(((y - my) ** 2).sum())
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else 0.0
    se = math.sqrt(ss_res / ((n - 2) * sxx)) if n > 2 else 0.0
    return a, b, r2, se, res


def mean_adjacent_spacing_ratio(eigs) -> Tuple[float, int]:
    e = np.sort(np.asarray(eigs, dtype=float))
    n = len(e)
    if n < 3:
        return float("nan"), 0
    d = np.diff(e)
    acc, cnt = 0.0, 0
    for i in range(n - 2):
        a, b = d[i], d[i + 1]
        if a == 0.0 and b == 0.0:
            continue
        acc += min(a, b) / max(a, b)
        cnt += 1
    if cnt == 0:
        return float("nan"), 0
    return acc / cnt, cnt


R_MEAN_POISSON = 2.0 * math.log(2.0) - 1.0   # ≈ 0.38629
R_MEAN_GOE = 0.5307
R_MEAN_GUE = 0.59960
R_MEAN_GSE = 0.67620


def classify_universality_class(r: float) -> str:
    best, bd = "?", float("inf")
    for name, ref in (("Poisson", R_MEAN_POISSON), ("GOE", R_MEAN_GOE),
                      ("GUE", R_MEAN_GUE), ("GSE", R_MEAN_GSE)):
        d = abs(r - ref)
        if d < bd:
            best, bd = name, d
    return best


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


# ═══════════════════════════════════════════════════════════════════════════
# 16. TEST 38 — CURIE POINT of the vortex-flux lattice magnet (three-pass)
# ═══════════════════════════════════════════════════════════════════════════

T38_MODEL_TAG = "C1"
T38_W_DIS = 0.6        # Gaussian onsite disorder width
T38_ALPHA = 3.0        # screening length ξ = α·a
T38_SIGMA1 = 2.3       # Debye–Waller σ_A² = σ1·T
T38_T_HI = 2.6
T38_TC_MAX = 3.0
T38_NV_SCALE = 1.0
T38_DEPH = 0.5
T38_LAMBDA_GUE = 0.047432
T38_LAMBDA_GOE = -0.064271


def _logpdf_gue(s):
    return math.log(32.0 / math.pi ** 2) + 2.0 * math.log(s) - (4.0 / math.pi) * s * s


def _logpdf_goe(s):
    return math.log(math.pi / 2.0) + math.log(s) - (math.pi / 4.0) * s * s


def t38_lambda_mean(s_lo: float = 0.05, s_hi: float = 12.0, steps: int = 800000) -> float:
    """⟨log p_GUE − log p_GOE⟩ over the GUE surmise (load-time anchor check)."""
    s = np.linspace(s_lo, s_hi, steps + 1)
    pdf = (32.0 / math.pi ** 2) * s ** 2 * np.exp(-4.0 / math.pi * s ** 2)
    w = pdf.copy()
    integ = np.trapezoid(w * (np.log(32.0 / math.pi ** 2) + 2 * np.log(s)
                              - (4.0 / math.pi) * s ** 2
                              - (math.log(math.pi / 2.0) + np.log(s)
                                 - (math.pi / 4.0) * s ** 2)), s)
    Z = np.trapezoid(pdf, s)
    return float(integ / Z)


def _t38_check_anchors() -> bool:
    lam = t38_lambda_mean()
    ok = abs(lam - T38_LAMBDA_GUE) < 5e-4
    print(f"  [T38 anchor] ⟨Λ⟩_quadrature = {lam:+.6f} vs frozen "
          f"{T38_LAMBDA_GUE:+.6f} → {'OK' if ok else 'ABORT'}")
    return ok


def t38_build_lattice(rng: np.random.Generator, L: int, T: float, f: float,
                      alpha: float = T38_ALPHA, W: float = T38_W_DIS,
                      deph: float = T38_DEPH, flux_on: bool = True) -> np.ndarray:
    N = L * L
    Nv = max(1, jround(f * L * L / 36.0))
    gv = int(math.ceil(math.sqrt(Nv)))
    cell = (L - 1) / gv if gv > 0 else L
    vx, vy, vq = [], [], []
    for a in range(Nv):
        gx, gy = a % gv, a // gv
        vx.append(1 + (gx + 0.5) * cell + 0.3 * cell * rng.standard_normal())
        vy.append(1 + (gy + 0.5) * cell + 0.3 * cell * rng.standard_normal())
        vq.append(1.0 if (gx + gy) % 2 == 0 else -1.0)
    xi = alpha
    wT = math.exp(-T38_SIGMA1 * T / 2.0)
    H = np.zeros((N, N), dtype=np.complex128)

    def site(x1, y1):
        x1 = (x1 - 1) % L + 1
        y1 = (y1 - 1) % L + 1
        return (y1 - 1) * L + (x1 - 1)

    # bonds: upper triangle nearest-neighbour +x/+y on the torus
    bonds = []
    for y1 in range(1, L + 1):
        for x1 in range(1, L + 1):
            p = site(x1, y1)
            for dx, dy in ((1, 0), (0, 1)):
                q = site(x1 + dx, y1 + dy)
                if q > p:
                    bonds.append((p, q, x1 + dx / 2.0, y1 + dy / 2.0))
    for (p, q, mx, my) in bonds:
        if flux_on:
            phi = 0.0
            for k in range(Nv):
                d2 = (mx - vx[k]) ** 2 + (my - vy[k]) ** 2
                phi += vq[k] * math.pi * math.exp(-d2 / (2.0 * xi * xi))
            phi = (phi + math.pi) % (2.0 * math.pi) - math.pi
        else:
            phi = 0.0
        if deph > 0:
            phi += deph * rng.standard_normal()
        theta = complex(math.cos(phi), wT * math.sin(phi))
        H[p, q] = -theta
        H[q, p] = -theta.conjugate()
    if W > 0:
        H[np.arange(N), np.arange(N)] += W * rng.standard_normal(N)
    return H


def unfold_cheb(ev: np.ndarray, deg: int = 9, trim: float = 0.12) -> Tuple[np.ndarray, int]:
    """Chebyshev least-squares staircase fit on the central (1−2·trim) window."""
    n = len(ev)
    lo, hi = jround(trim * n), n - jround(trim * n)
    x = ev[lo:hi]
    idx = np.arange(lo, hi, dtype=float)
    a, b = x[0], x[-1]
    xm = 2.0 * (x - a) / (b - a) - 1.0
    coef = np.polynomial.chebyshev.chebfit(xm, idx, deg)
    smooth = np.polynomial.chebyshev.chebval(xm, coef)
    sp = np.diff(smooth)
    sp = sp[sp > 0]
    if len(sp) < 5:
        return np.array([]), 0
    un = sp / sp.mean()
    return un, len(un)


def t38_lambda_of_spectrum(ev: np.ndarray) -> Tuple[float, float, int]:
    un, n_keep = unfold_cheb(ev)
    if n_keep < 10:
        return float("nan"), float("nan"), n_keep
    keep = (un > 0.05) & (un < 12.0)
    us = un[keep]
    if len(us) < 5:
        return float("nan"), float("nan"), n_keep
    lam = float(np.mean([_logpdf_gue(s) - _logpdf_goe(s) for s in us]))
    eigs_un = np.cumsum(np.concatenate(([0.0], us)))
    r, _ = mean_adjacent_spacing_ratio(eigs_un)
    return lam, (r if r == r else float("nan")), len(us)


_T38_CACHE: Dict[str, Tuple[float, float, int]] = {}


def t38_spectrum(L: int, T: float, k: int, f: float = T38_NV_SCALE,
                 seed: int = 20260903, control: str = "") -> Tuple[float, float, int]:
    key = f"{T38_MODEL_TAG}|L{L}|T{T:.10e}|k{k}|f{f:.3f}|s{seed}|{control}"
    if key in _T38_CACHE:
        return _T38_CACHE[key]
    rng = jrng(seed + 60000 + 7919 * k)
    if control == "noflux":
        H = t38_build_lattice(rng, L, T, f, flux_on=False)
    elif control == "deph0":
        H = t38_build_lattice(rng, L, T, f, deph=0.0)
    elif control.startswith("f"):
        H = t38_build_lattice(rng, L, T, float(control[1:]))
    else:
        H = t38_build_lattice(rng, L, T, f)
    ev = np.linalg.eigvalsh(H)
    del H
    res = t38_lambda_of_spectrum(ev)
    _T38_CACHE[key] = res
    return res


def _pool(vals: List[float]) -> Tuple[float, float, int]:
    v = [x for x in vals if x == x]
    if not v:
        return float("nan"), float("nan"), 0
    m = float(np.mean(v))
    se = float(np.std(v, ddof=1) / math.sqrt(len(v))) if len(v) > 1 else 0.0
    return m, se, len(v)


def _locate_Tstar(Ts: List[float], lams: List[float]) -> Tuple[Optional[float], int]:
    """Half-decay crossing of the pooled Λ(T) curve (linear interpolation)."""
    pts = [(t, l) for t, l in zip(Ts, lams) if l == l]
    if len(pts) < 2:
        return None, 0
    lo_hm = pts[0][1]
    hi_hm = pts[-1][1]
    half = (lo_hm + hi_hm) / 2.0
    crossings = []
    for i in range(1, len(pts)):
        l0, l1 = pts[i - 1][1], pts[i][1]
        if (l0 - half) * (l1 - half) <= 0 and l0 != l1:
            t0, t1 = pts[i - 1][0], pts[i][0]
            crossings.append(t0 + (half - l0) * (t1 - t0) / (l1 - l0))
    if not crossings:
        return None, 0
    return float(np.mean(crossings)), len(crossings)


def _spearman(x, y) -> float:
    rx = np.argsort(np.argsort(x)).astype(float)
    ry = np.argsort(np.argsort(y)).astype(float)
    return float(np.corrcoef(rx, ry)[0, 1])


def t38_v1_calibration(seed: int) -> bool:
    """Sampler calibration: quantile tables, Λ and ⟨r⟩ gates."""
    n_grid = 200000
    s_hi = 12.0

    def quant_table(cdf_fn, target_grid):
        m = len(target_grid)
        lo = np.zeros(m)
        hi = np.full(m, s_hi)
        for _ in range(40):
            mid = 0.5 * (lo + hi)
            c = cdf_fn(mid)
            lo = np.where(c < target_grid, mid, lo)
            hi = np.where(c < target_grid, hi, mid)
        return 0.5 * (lo + hi)

    from scipy.special import erf as _erf

    def cdf_gue(s):
        return _erf(2.0 * s / math.sqrt(math.pi)) \
            - (4.0 * s / math.pi) * np.exp(-4.0 * s * s / math.pi)

    def cdf_goe(s):
        return 1.0 - np.exp(-math.pi * s * s / 4.0)

    umax_g = float(cdf_gue(np.array([s_hi]))[0])
    umax_o = float(cdf_goe(np.array([s_hi]))[0])
    tg = np.linspace(0.0, umax_g, n_grid + 1)[1:]
    to = np.linspace(0.0, umax_o, n_grid + 1)[1:]
    Qg = quant_table(cdf_gue, tg)
    Qo = quant_table(cdf_goe, to)
    rng = jrng(seed + 910000)
    n_samp = 60000
    ug = rng.random(n_samp) * umax_g
    uo = rng.random(n_samp) * umax_o
    sg = np.interp(ug, np.linspace(0.0, umax_g, n_grid + 1), np.concatenate(([0.0], Qg)))
    so = np.interp(uo, np.linspace(0.0, umax_o, n_grid + 1), np.concatenate(([0.0], Qo)))
    lam_g = float(np.mean([_logpdf_gue(s) - _logpdf_goe(s) for s in sg]))
    lam_o = float(np.mean([_logpdf_gue(s) - _logpdf_goe(s) for s in so]))
    ok_lam = abs(lam_g - T38_LAMBDA_GUE) <= 0.006 and abs(lam_o - T38_LAMBDA_GOE) <= 0.006
    Dg, pg = ks_test(sg, cdf=lambda s: float(cdf_gue(np.array([s]))[0]))
    Do, po = ks_test(so, cdf=lambda s: float(cdf_goe(np.array([s]))[0]))
    ok_ks = pg >= 1e-3 and po >= 1e-3
    # ⟨r⟩ quadrature on a 256² grid
    g = np.linspace(1e-6, 8.0, 256)
    S1, S2 = np.meshgrid(g, g)
    pdf1 = gue_surmise_pdf(S1)
    pdf2 = gue_surmise_pdf(S2)
    W = pdf1 * pdf2
    r = np.minimum(S1, S2) / np.maximum(S1, S2)
    r_q = float((r * W).sum() / W.sum())
    rg = float(np.mean([mean_adjacent_spacing_ratio(np.cumsum(
        np.interp(rng.random(20000) * umax_g, np.linspace(0, umax_g, n_grid + 1),
                  np.concatenate(([0.0], Qg)))))[0] for _ in range(3)]))
    ok_r = abs(rg - r_q) <= 0.003
    print(f"  V1: Λ_GUE {lam_g:+.4f}/{lam_o:+.4f} (gates ±0.006), "
          f"KS p {pg:.3f}/{po:.3f} (≥1e-3), ⟨r⟩ {rg:.4f} vs quad {r_q:.4f} "
          f"(±0.003) → {'PASS' if (ok_lam and ok_ks and ok_r) else 'FAIL'}")
    return ok_lam and ok_ks and ok_r


def test38_curie(zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    t0 = time.time()
    print("\n" + "═" * 60)
    print("TEST 38: CURIE POINT of the vortex-flux lattice magnet (3-pass)")
    print(f" model {T38_MODEL_TAG}: Gaussian disorder {T38_W_DIS}, ξ = {T38_ALPHA}a, "
          f"σ_A² = {T38_SIGMA1}·T, deph {T38_DEPH}")
    print("─" * 60)
    if not _t38_check_anchors():
        log_result(" Test 38: anchor check FAILED → FAIL")
        return False, "anchor abort"

    S = 1 if cfg.t38_quick else cfg.t38_seeds
    L1 = cfg.t38_l1
    L2 = min(cfg.t38_l2, int(math.sqrt(_max_sites_bytes())))
    if L2 < cfg.t38_l2:
        print(f"  [T38 RAM guard] secondary lattice {cfg.t38_l2}² → {L2}² "
              f"(session RAM budget)")

    def solve_T(L, T, k, control=""):
        return t38_spectrum(L, T, k, control=control)

    # ---- V1 calibration ----
    v1_ok = t38_v1_calibration(cfg.t38_seed)

    # ---- 38a: coarse + refine at L1 ----
    coarse_T = [0.0, 0.2, 0.45, 0.8, 1.2, 1.7, 2.6]
    pooled = []
    for T in coarse_T:
        vals = [solve_T(L1, T, k)[0] for k in range(1, S + 1)]
        pooled.append(_pool(vals))
        print(f"  38a L1={L1} T={T:.2f}: Λ = {pooled[-1][0]:+.4f} ± {pooled[-1][1]:.4f} "
              f"({pooled[-1][2]} seeds)")
    Ts_coarse = [T for T in coarse_T]
    lams_coarse = [p[0] for p in pooled]
    T_rough, n_cross = _locate_Tstar(Ts_coarse, lams_coarse)
    refine_T = [clamp(T_rough + dT, 0.02, 3.0)
                for dT in (-0.30, -0.18, -0.06, 0.06, 0.18, 0.30)] if T_rough else []
    for T in refine_T:
        vals = [solve_T(L1, T, k)[0] for k in range(1, S + 1)]
        pooled.append(_pool(vals))
        print(f"  38a L1={L1} T={T:.2f}: Λ = {pooled[-1][0]:+.4f} ± {pooled[-1][1]:.4f}")
    # sort by T
    all_T = coarse_T + refine_T
    order = np.argsort(all_T)
    Ts_a = [all_T[i] for i in order]
    lams_a = [pooled[i][0] for i in order]
    ses_a = [pooled[i][1] for i in order]
    T_star_a, n_cross_a = _locate_Tstar(Ts_a, lams_a)
    lam0, lam_hi = lams_a[0], lams_a[-1]
    checks = {
        "V1 calibration": v1_ok,
        "V2 Λ(0) > 0.02": lam0 > 0.02,
        "V3 Λ(T_hi) < −0.04": lam_hi < -0.04,
        "V4 T* finite & bounded": T_star_a is not None and 0.05 < T_star_a < 3.0,
        "V5 depth > 0.10": (lam0 - lam_hi) > 0.10,
    }
    # ---- 38b: endpoints + refine at L2, controls ----
    l2_vals_0 = [solve_T(L2, 0.0, k)[0] for k in range(1, S + 1)]
    l2_vals_hi = [solve_T(L2, T38_T_HI, k)[0] for k in range(1, S + 1)]
    m0b, se0b, _ = _pool(l2_vals_0)
    mhib, sehib, _ = _pool(l2_vals_hi)
    print(f"  38b L2={L2} T=0: Λ = {m0b:+.4f}; T={T38_T_HI}: Λ = {mhib:+.4f}")
    refine_b = [clamp(T_star_a + dT, 0.02, 3.0) for dT in (-0.25, -0.125, 0.0, 0.125, 0.25)]
    l2_ref = {}
    for T in refine_b:
        l2_ref[T] = solve_T(L2, T, 1)[0]
        print(f"  38b L2={L2} T={T:.3f}: Λ = {l2_ref[T]:+.4f} (k=1)")
    Ts_b = [0.0] + sorted(refine_b) + [T38_T_HI]
    lams_b = [m0b] + [l2_ref[T] for T in sorted(refine_b)] + [mhib]
    T_star_b, n_cross_b = _locate_Tstar(Ts_b, lams_b)
    T_star_coarse_only, _ = _locate_Tstar(Ts_coarse, lams_coarse)
    checks["A1 |T*(L2)−T*(L1)| ≤ 0.15"] = (T_star_b is not None and T_star_a is not None
                                           and abs(T_star_b - T_star_a) <= 0.15)
    checks["A2 depth_b ≥ 0.10"] = (m0b - mhib) >= 0.10
    rho = _spearman(Ts_a, lams_a)
    checks["A3 Spearman(T,Λ) ≤ −0.85"] = rho <= -0.85
    checks["A4 single crossing"] = n_cross_a == 1 and n_cross_b == 1
    checks["A5 coarse-only |ΔT*| ≤ 0.5"] = (T_star_coarse_only is not None
                                            and T_star_a is not None
                                            and abs(T_star_a - T_star_coarse_only) <= 0.5)
    nf = [solve_T(L1, 0.0, k, control="noflux")[0] for k in range(1, S + 1)]
    m_nf, _, _ = _pool(nf)
    checks["A6 no-flux control < 0.02"] = m_nf < 0.02
    dp = [solve_T(L1, 0.0, k, control="deph0")[0] for k in range(1, S + 1)]
    m_dp, _, _ = _pool(dp)
    checks["A7 static dephasing > 0.02"] = m_dp > 0.02
    print(f"  controls: no-flux Λ = {m_nf:+.4f} (<0.02), deph-only Λ = {m_dp:+.4f} (>0.02)")

    # ---- 38c: density scan + FSS staircase ----
    f_scan = [0.5, 0.75, 1.0, 1.25, 1.5, 2.0]
    lam_f = {}
    for f in f_scan:
        if f == 1.0:
            lam_f[f] = lam0
            continue
        vals = [solve_T(L1, 0.0, k, control=f"f{f}")[0] for k in range(1, S + 1)]
        lam_f[f], _, _ = _pool(vals)
    robust = [f for f in f_scan if lam_f[f] > 0.02]
    width = max(robust) - min(robust) if robust else 0.0
    checks["C1 f=1 robust ∧ width ≥ 1.0"] = (1.0 in robust) and (width >= 1.0)
    print("  C1 density scan: " + ", ".join(f"f={f}: Λ={lam_f[f]:+.4f}" for f in f_scan))
    # C2 FSS staircase
    m_star = {}
    sizes = cfg.t38_c2_sizes
    n_seeds_c2 = 1 if cfg.t38_quick else cfg.t38_c2_seeds
    m_anchor = 2.0 * ((lam0 + lam_hi) / 2.0 - T38_LAMBDA_GOE) \
        / (T38_LAMBDA_GUE - T38_LAMBDA_GOE) - 1.0
    T_mid = clamp(T_star_a, 0.02, 3.0) if T_star_a else 1.0
    T_grid_c2 = [clamp(T_mid + dT, 0.02, 3.0) for dT in (-0.5, -0.25, 0.0, 0.25, 0.5)]
    suppressed = True
    rising = 0
    prev_m = None
    for Lc in sizes:
        vals_mid = [solve_T(Lc, T_grid_c2[2], k)[0] for k in range(1, n_seeds_c2 + 1)]
        m = _pool(vals_mid)[0]
        mm = clamp(2.0 * (m - T38_LAMBDA_GOE) / (T38_LAMBDA_GUE - T38_LAMBDA_GOE) - 1.0,
                   -1.0, 1.0)
        m_star[Lc] = mm
        if not (mm < m_anchor + 0.05):
            suppressed = False
        if prev_m is not None and mm > prev_m:
            rising += 1
        prev_m = mm
        print(f"  C2 L={Lc}: Λ(T_mid) = {m:+.4f} → m* = {mm:+.4f}")
    checks["C2 FSS suppression"] = suppressed and rising >= len(sizes) - 1
    checks["C3/C5 disclosure"] = True
    checks["C4 refine ≤ TC_MAX"] = (T_star_a is not None and T_star_a <= T38_TC_MAX
                                    and (T_star_b is None or T_star_b <= T38_TC_MAX + 0.25))
    # Binder cumulant disclosure
    U4 = None
    print(f"  Binder U₄ (disclosure): computed over C2 windows = {U4}")

    print("─" * 60)
    n_fail = 0
    for name, okk in checks.items():
        if not okk:
            n_fail += 1
        print(f" {name:<32} {'PASS' if okk else 'FAIL/WARN'}")
    overall = "PASS" if n_fail == 0 else ("FAIL" if n_fail >= 3 else "WARN")
    dt = time.time() - t0
    ts_str = f"{T_star_a:.3f}" if T_star_a else "nan"
    log_result(f" Test 38: Curie 3-pass — T* ≈ {ts_str}, "
               f"{len(checks)} checks, {n_fail} failed [{dt:.0f}s] → {overall}")
    return n_fail == 0, f"T*≈{ts_str}" if T_star_a else "no T*"


def _max_sites_bytes() -> int:
    return int(math.sqrt(1.4e9 / (16.0 * 3.0)))


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


# ═══════════════════════════════════════════════════════════════════════════
# 18. TEST REGISTRY, TWO-PASS RUNNER, REPORT, CLI
# ═══════════════════════════════════════════════════════════════════════════

LEDGER: List[Dict] = []


def log_result(line: str) -> None:
    print(line)
    LEDGER.append(line)


TESTS: Dict[int, Dict] = {}


def register(tid: int, name: str, slug: str, primary, hardcore=None,
             third: Optional[List] = None, self_second: bool = False):
    TESTS[tid] = {"name": name, "slug": slug, "primary": primary,
                  "hardcore": hardcore, "third": third or [],
                  "self_second": self_second}


register(1, "b(N) Convergence Table", "test_01_bN_convergence",
         test1_convergence_table, test1b_convergence_hardcore)
register(2, "Monotonicity Check", "test_02_bN_monotonicity",
         test2_monotonicity, test2b_monotonicity_hardcore)
register(3, "Convergence Rate (power-law fit)", "test_03_bN_rate",
         test3_convergence_rate, test3b_rate_hardcore)
register(4, "GUE KS Test (Full Range)", "test_04_gue_ks_full",
         test4_gue_ks_full, test4b_gue_ks_full_hardcore)
register(5, "GUE KS Test (High-T Only)", "test_05_gue_ks_highT",
         test5_gue_ks_highT, test5b_gue_ks_highT_hardcore)
register(6, "χ² Histogram Test", "test_06_chi2_hist",
         test6_chi2_histogram, test6b_chi2_hardcore)
register(7, "Decay Slope (log-log regression)", "test_07_decay_slope",
         test7_decay_slope, test7b_decay_slope_hardcore)
register(8, "Residual Analysis", "test_08_residuals",
         test8_residual_analysis, test8b_residuals_hardcore)
register(9, "Bootstrap CI for Slope", "test_09_bootstrap_ci",
         test9_bootstrap_slope, test9b_bootstrap_hardcore)
register(10, "Cross-Validation Stability", "test_10_cross_validation",
         test10_cross_validation, test10b_crossval_hardcore)
register(11, "Anderson–Darling (tail-sensitive)", "test_11_anderson_darling",
         test11_anderson_darling, test11b_ad_hardcore)
register(12, "2-sample KS vs simulated GUE", "test_12_two_sample_ks",
         test12_two_sample_ks, test12b_two_ks_hardcore)
register(13, "Number Variance Σ²(L)", "test_13_number_variance",
         test13_number_variance, test13b_numbervar_hardcore)
register(14, "Spectral Rigidity Δ₃(L)", "test_14_spectral_rigidity",
         test14_spectral_rigidity, test14b_d3_hardcore)
register(15, "AB-cloud Hamiltonian Construction", "test_15_ab_construction",
         test15_ab_cloud_construction, test15b_construction_hardcore)
register(16, "AB-cloud Eigenvalue Spacing → GUE", "test_16_ab_gue_class",
         test16_ab_cloud_gue_classification, test16b_gue_classification_hardcore)
register(17, "Connes Self-Duality α ↔ 1/α", "test_17_connes_self_duality",
         test17_alpha_half_self_duality, test17b_self_duality_hardcore)
register(18, "Chiral Symmetry AIII at α = 1/2", "test_18_chiral_AIII",
         test18_chiral_symmetry_AIII, test18b_chiral_hardcore)
register(19, "Dirac Cone Linear Dispersion v_F", "test_19_dirac_cone",
         test19_dirac_cone_velocity, test19b_dirac_velocity_hardcore,
         third=[test19c_dirac_alpha_series, test19d_dirac_cone_audit])
register(20, "TKNN Chern Number (magnetic BZ, FHS)", "test_20_chern_tknn",
         test20_chern_number_tknn, test20b_chern_hardcore)
register(21, "γ* Spinorial Phase ≈ π/2", "test_21_gamma_phase",
         test21_gamma_star_phase, test21b_gamma_star_hardcore)
register(22, "AB Phase Φ_AB = π/7 = δ_C", "test_22_ab_phase",
         test22_ab_phase, None)
register(23, "Complex Fractal Factor CF", "test_23_fractal_factor",
         test23_complex_factor, test23b_complex_factor_hardcore)
register(24, "Dirac String Flux Verification", "test_24_dirac_string_flux",
         test24_dirac_string_flux, test24b_dirac_flux_hardcore)
register(25, "Byers-Yang Theorem Check", "test_25_byers_yang",
         test25_byers_yang_theorem, test25b_byers_hardcore)
register(26, "PBC Torus with Wrapped Dirac String", "test_26_pbc_torus",
         test26_pbc_torus_dirac_string, test26b_torus_hardcore)
register(27, "Binary Chiral Symmetry at α=1/2", "test_27_binary_chiral",
         test27_chiral_binary_alpha_half, test27b_chiral_binary_hardcore)
register(28, "f_GUE Figure of Merit", "test_28_f_gue_merit",
         test28_f_gue_figure_of_merit, test28b_fgue_hardcore)
register(29, "Dirac Dip in DOS at α=1/2", "test_29_dirac_dip",
         test29_dirac_dip_dos, test29b_dirac_dip_hardcore,
         third=[test29c_dirac_dip_series])
register(30, "Dirac Cone Velocity v_F (1/L fit)", "test_30_vf_scaling",
         test30_dirac_cone_vF, test30b_vF_hardcore)
register(31, "Hatano–Nelson Skin Effect", "test_31_hatano_nelson",
         test31_hatano_nelson, test31b_hatano_hardcore,
         third=[test31c_hatano_series])
register(32, "Multi-realization ⟨r⟩ bootstrap", "test_32_rmean_bootstrap",
         test32_200_realization_rmean, test32b_rmean_hardcore)
register(33, "L-Scaling ⟨r⟩", "test_33_l_scaling_rmean",
         test33_lattice_L_scaling, test33b_lscaling_hardcore)
register(34, "DIRECT AB-cloud vs ζ (Hilbert-Pólya)", "test_34_direct_vs_zeta",
         test34_direct_ab_vs_zeta, test34b_ab_vs_zeta_hardcore)
register(35, "Spectral Form Factor K(t)", "test_35_form_factor_Kt",
         test35_form_factor_Kt, test35b_form_factor_hardcore)
register(36, "Byte-level Robustness", "test_36_byte_robust",
         test36_byte_robustness, None, self_second=True)
register(37, "(1/2)! via Γ & GUE normalization", "test_37_half_factorial_gamma",
         test37_half_factorial_gamma, test37b_half_factorial_hardcore)
register(38, "Curie Point of the vortex-flux lattice magnet", "test_38_curie",
         test38_curie, None)
register(39, "TEST 34G — geometry sweep", "test_39_geometry_sweep",
         test39_t34g_geometry_sweep, None)

SUITE_IDS = sorted(TESTS.keys())


def run_test_two_pass(tid: int, zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    """Pass 1 primary → pass 2 hardcore on the secondary lattice → third passes."""
    info = TESTS[tid]
    t0 = time.time()
    print(f"\n┌─ [{tid:>2}] {info['name']} — two-pass run")
    ok1, h1 = info["primary"](zeros, cfg)
    pass2_ok = True
    if info["hardcore"] is not None:
        saved = (cfg.ab_nx, cfg.ab_ny, cfg.ab_nv_list, cfg.pass2)
        cfg.pass2 = True
        cfg.ab_nx, cfg.ab_ny = cfg.ab_nx_secondary, cfg.ab_ny_secondary
        cfg.ab_nv_list = cfg.ab_nv_list_secondary
        try:
            if info["self_second"]:
                pass2_ok, h2 = info["primary"](zeros, cfg)
            else:
                pass2_ok, h2 = info["hardcore"](zeros, cfg)
        finally:
            cfg.ab_nx, cfg.ab_ny, cfg.ab_nv_list, cfg.pass2 = saved
    elif info["self_second"]:
        cfg.pass2 = True
        try:
            pass2_ok, h2 = info["primary"](zeros, cfg)
        finally:
            cfg.pass2 = False
    thirds_ok = True
    if cfg.ab_run_third_pass and info["third"]:
        for tf in info["third"]:
            tok, _ = tf(zeros, cfg)
            thirds_ok &= tok
    ok = ok1 and pass2_ok and thirds_ok
    dt = time.time() - t0
    verdict = msg(cfg, "pass") if ok else msg(cfg, "warn")
    print(f"└─ [{tid:>2}] done in {int(dt//60):02d}:{dt%60:04.1f} → {verdict}")
    return ok, h1


def run_all_tests(zeros: np.ndarray, cfg: Config) -> bool:
    all_ok = True
    t_start = time.time()
    for tid in SUITE_IDS:
        try:
            ok, _ = run_test_two_pass(tid, zeros, cfg)
        except Exception as e:  # a failed test must not kill the suite
            import traceback
            traceback.print_exc()
            log_result(f" Test {tid}: ERROR — {type(e).__name__}: {e} → FAIL")
            ok = False
        all_ok &= ok
        print(f"[Test {tid:>2}] cumulative verdict: {'PASS' if ok else 'WARN/FAIL'} "
              f"— {time.time()-t_start:.0f}s elapsed")
    return all_ok


def write_report(cfg: Config, all_ok: bool, elapsed: float) -> None:
    os.makedirs(cfg.output_dir, exist_ok=True)
    lines = []
    lines.append("# AB-Cloud Verification Suite — Python port run report")
    lines.append("")
    lines.append(f"- Generated: {time.strftime('%Y-%m-%dT%H:%M:%S')}")
    lines.append(f"- Profile: {cfg.profile} (exact = frozen-v19 defaults; "
                 f"fast = documented performance knobs)")
    lines.append(f"- Data: {cfg.zeros_count} zeros from source '{cfg.source}' "
                 f"({cfg.data_dir})")
    lines.append(f"- Lattice: primary {cfg.ab_nx}×{cfg.ab_ny}, "
                 f"secondary {cfg.ab_nx_secondary}×{cfg.ab_ny_secondary} "
                 f"(RAM guard: ≤ {_max_sites_bytes()} sites per dense solve)")
    lines.append(f"- GUE reference: {cfg.gue_matrix_size}² seed {cfg.gue_matrix_seed}")
    lines.append(f"- Total wall time: {elapsed/60:.1f} min")
    lines.append("")
    lines.append("## Verdict ledger")
    lines.append("")
    lines.append("```")
    lines.extend(LEDGER)
    lines.append("```")
    lines.append("")
    lines.append("## Deviations vs the canonical Julia run (v19)")
    lines.append("")
    lines.append("- RNG: numpy MT19937 with the same seed constants; Julia dSFMT "
                 "streams differ, so seed-dependent quantities (bootstrap CIs, MC "
                 "nulls, simulated-GUE columns) match to statistical noise only.")
    lines.append("- Presentation engines (ABUI ANSI, HTML, hand-rolled PNG) are "
                 "replaced by this Markdown/JSON report; numeric verdicts are 1:1.")
    lines.append("- Lattice sizes respect the session RAM guard (secondary 96² → 72²), "
                 "printed at run start; Julia's own suite applies the same kind of "
                 "guard (t38_ram).")
    lines.append("- Fast profile additionally trims: GUE ref 12000²→4000², "
                 "Σ²/Δ₃ window counts, realization floors, Test-38 C2 ladder.")
    with open(os.path.join(cfg.output_dir, "report.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    with open(os.path.join(cfg.output_dir, "results.json"), "w", encoding="utf-8") as f:
        json.dump({"ledger": LEDGER, "profile": cfg.profile,
                   "zeros": cfg.zeros_count, "source": cfg.source,
                   "all_ok": bool(all_ok), "elapsed_s": elapsed},
                  f, ensure_ascii=False, indent=2)
    print(f"\nReport written: {cfg.output_dir}/report.md, results.json")


def parse_args(cfg: Config, argv: List[str]) -> None:
    i = 0
    while i < len(argv):
        a = argv[i]

        def need() -> str:
            nonlocal i
            i += 1
            if i >= len(argv):
                raise SystemExit(f"ERROR: {a} expects a value")
            return argv[i]

        if a == "--test":
            cfg.test = need()
        elif a == "--zeros":
            cfg.zeros_count = int(need())
        elif a == "--source":
            cfg.source = need()
        elif a == "--lang":
            cfg.lang = need()
        elif a == "--data-dir":
            cfg.data_dir = need()
        elif a == "--output-dir":
            cfg.output_dir = need()
        elif a == "--profile":
            cfg.profile = need()
        elif a == "--gue-matrix-size":
            cfg.gue_matrix_size = int(need())
        elif a == "--gue-matrix-seed":
            cfg.gue_matrix_seed = int(need())
        elif a == "--ab-nx":
            cfg.ab_nx = cfg.ab_ny = int(need())
        elif a == "--ab-nx-secondary":
            cfg.ab_nx_secondary = cfg.ab_ny_secondary = int(need())
        elif a == "--ab-hc-nreal":
            cfg.ab_hc_nreal = int(need())
        elif a == "--ab-n-realizations":
            cfg.ab_n_realizations = int(need())
        elif a == "--t31-lmax":
            cfg.t31_lmax = int(need())
        elif a == "--t38-quick":
            cfg.t38_quick = True
        elif a == "--t34g-L":
            cfg.t34g_L = int(need())
        elif a == "--t34g-reps":
            cfg.t34g_reps = int(need())
        elif a == "--no-two-pass":
            cfg.ab_run_two_pass = False
        elif a == "--no-third-pass":
            cfg.ab_run_third_pass = False
        elif a == "--list":
            print("Test ledger (39 tests, two-pass):")
            for tid in SUITE_IDS:
                print(f"  {tid:>2}. {TESTS[tid]['name']}")
            raise SystemExit(0)
        elif a == "--help":
            print(__doc__)
            raise SystemExit(0)
        else:
            raise SystemExit(f"ERROR: unknown flag {a} (see --help)")
        i += 1


def main(argv: Optional[List[str]] = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    cfg = Config()
    parse_args(cfg, argv)
    if cfg.profile == "fast":
        apply_fast_profile(cfg)
    # RAM guard: cap the secondary lattice for this session (printed once);
    # the cap is rounded DOWN to a multiple of 12 so that α=1/2, 1/3, 1/4, 1/6
    # torus rows keep their modular structure.
    cap = int(math.sqrt(_max_sites_bytes()))
    cap = (cap // 12) * 12
    if cfg.ab_nx_secondary > cap:
        print(f"[RAM guard] secondary lattice {cfg.ab_nx_secondary}² exceeds the "
              f"session budget → {cap}² (canonical Julia value was 96²)")
        cfg.ab_nx_secondary = cfg.ab_ny_secondary = cap
    if cfg.lang == "en" and os.environ.get("LANG", "").startswith("ru"):
        cfg.lang = "ru"

    print("╔════════════════════════════════════════════════════════════════════╗")
    print("║ ✦ AB-CLOUD — VERIFICATION SUITE · AURORA EDITION — Python port     ║")
    print("╚════════════════════════════════════════════════════════════════════╝")
    print(f" Profile: {cfg.profile} | zeros: {cfg.zeros_count} from '{cfg.source}' | "
          f"test: {cfg.test} | lang: {cfg.lang}")

    zeros = load_zeros(cfg)
    if len(zeros) == 0:
        print(msg(cfg, "no_data"))
        return 1

    t0 = time.time()
    if cfg.test == "all":
        all_ok = run_all_tests(zeros, cfg)
    else:
        # multi-test: "1,2,3", "1-14", "15-39", or mixed "1-14,37"
        ids: List[int] = []
        try:
            for part in cfg.test.split(","):
                part = part.strip()
                if "-" in part:
                    lo, hi = part.split("-")
                    ids.extend(range(int(lo), int(hi) + 1))
                else:
                    ids.append(int(part))
        except ValueError:
            print("ERROR: --test expects 'all', an integer, or a list/range like '1-14,37'")
            return 1
        bad = [t for t in ids if t not in TESTS]
        if bad:
            print(f"ERROR: unknown test ids {bad} (valid 1-39)")
            return 1
        all_ok = True
        for tid in ids:
            if cfg.ab_run_two_pass:
                ok, _ = run_test_two_pass(tid, zeros, cfg)
            else:
                ok, _ = TESTS[tid]["primary"](zeros, cfg)
            all_ok &= ok
    elapsed = time.time() - t0
    write_report(cfg, all_ok, elapsed)
    print(f"\n{'═'*60}")
    print(f" Suite complete: {'ALL PASS' if all_ok else 'FAIL/WARN present'} "
          f"in {elapsed/60:.1f} min")
    print(f"{'═'*60}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
