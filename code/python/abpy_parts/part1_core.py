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
