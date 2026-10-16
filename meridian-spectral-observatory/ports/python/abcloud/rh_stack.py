# -*- coding: utf-8 -*-
"""abcloud.rh_stack — Python port of the RH-stack driver layer.

1:1 port of the driver layer of TWO self-contained Julia scripts of
meridian-spectral-observatory:

  * ``RH_Sweep_Pro.jl``   (canonical, "sweep_pro" mode) — metrics kernel with
    block averaging ("binning"), 11-test compute_all_metrics, RHConfig,
    presets, magic-α tables, Hofstadter-torus Hamiltonian with vortex/jitter
    configuration, run() pipeline and CSV/JSON/TXT report writers.
  * ``RH_Unified_v5.jl``  ("unified_v5" mode) — v5 extras: connected form
    factor K(t), 8-test compute_all_metrics, byte-level diagnostics
    (256-level quantization + MT19937 UInt8 entropy/χ²), the external
    zeta_zeros_50000.txt chain and the high-T universality check.

Where the two scripts differ BOTH semantics are provided:

  compute_all_metrics(eigs, zeta, ..., mode="sweep_pro")   -> compute_all_metrics_sp
  compute_all_metrics(eigs, zeta, ..., mode="unified_v5")  -> compute_all_metrics_v5

``MetricsResult`` is a dataclass with the UNION of the SP (39) and v5 (7 byte)
fields; fields not applicable to a mode are ``None`` (byte fields: None/False).

RNG CONTRACT (the one used by the golden anchors): ALL randomness goes
through :class:`MT19937RNG` — a wrapper over the classic MT19937 of
``abcloud.mt19937``:

  random()          = (a>>5)*2**26 + (b>>6)) / 2**53   (two u32 draws)
  randn()           = Box-Muller, 2 draws (u1 redrawn while <= 0, then u2;
                      sqrt(-2 log u1) * cos(2 pi u2))
  randint(lo, hi)   = lo + floor(u * (hi - lo + 1))    (one draw)
  choice(vec)       = vec[floor(u * len(vec))]         (one draw)
  next_byte()       = next_u32() >> 24                 (UInt8, top 8 bits)

Every Julia ``MersenneTwister(seed)`` site maps to ``MT19937RNG(seed)`` at the
same position in the code flow, so the draw ORDER matches the Julia original.

RECONSTRUCTIONS (functions CALLED but NOT DEFINED in RH_Sweep_Pro.jl — the
obvious semantics are implemented and used by sweep_top10_pro /
sweep_combined_quick):
  * ``sweep_parameter(param, values, base_cfg, verbose)`` — sweep one RHConfig
    field, ``run(cfg)`` per value, collect dicts with keys
    ``value / score / K_corr_zeta / brody_beta / chi2 / r_mean``,
    best by composite score.  Returns (results, best_val, best_score, best_result).
  * ``save_sweep_results(all_results, best_params, output_dir)`` — dump the
    sweep to ``<output_dir>/sweep_results.json``.

PORTING EXCLUSIONS (deliberate, documented):
  * AURORA console furniture (_mr_*), load-time banner, progress bars;
  * plots / PNG (plot_6panel_comparison, plot_7panel_advanced,
    plot_zeta_in_ab_cloud, parameter heatmap / optimization progress /
    sweep dashboard / radar) — the run() pipeline creates the ``plots/``
    directory for structural parity but writes no images;
  * ``@__FILE__`` main blocks.

DATA FILES (extracted verbatim from the Julia sources by
``ports/python/extract_rh_zeros.py``):
  * ``abcloud/data/rh_embedded_zeros_sp.txt``  — 13 661 embedded ζ zeros
    (RH_Sweep_Pro.jl ``ZETA_ZEROS``), one per line, full printed precision;
  * ``abcloud/data/rh_embedded_zeros_v5.txt``  — 500 embedded ζ zeros
    (RH_Unified_v5.jl ``ZETA_ZEROS_EMBEDDED``).

Eigenvalues use ``numpy.linalg.eigvalsh`` (LAPACK), matching Julia's
``eigvals(Hermitian(H))`` to ~1e-13 — the tolerance already used across the
abcloud ports.  Julia ``var``/``std`` are sample statistics (ddof=1).
No SciPy anywhere.
"""

import cmath
import copy
import gzip
import json
import math
import os
import re
import struct
import time
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Sequence, Tuple

import numpy as np

from .mt19937 import MT19937

__all__ = [
    "MT19937RNG",
    "VortexConfig",
    "RHConfig",
    "MetricsResult",
    "ByteDiagnostics",
    "R_GUE", "R_GOE", "R_GSE", "R_POISSON",
    "N_ZETA_ZEROS_AVAILABLE", "ZETA_ZEROS_VERIFIED_COUNT",
    "MAGIC_ALPHA_VALUES", "MAGIC_ALPHA_LABELS", "N_MAGIC_ALPHAS",
    "spacing_ratios", "mean_r", "classify_universality_class",
    "polynomial_unfold", "local_unfold", "unfold_spectrum",
    "R2_GUE_theory", "R2_Poisson_theory", "K_GUE_theory",
    "Sigma2_GUE_theory", "Sigma2_Poisson_theory", "Delta3_GUE_theory",
    "p_GUE_wigner", "p_GOE_wigner", "p_Poisson",
    "compute_R2", "compute_K_empirical", "compute_Sigma2",
    "compute_Delta3", "compute_p_histogram",
    "rms_error", "safe_correlation",
    "compute_byte_level_diagnostics",
    "compute_all_metrics", "compute_all_metrics_sp", "compute_all_metrics_v5",
    "make_vortex_config", "central_eigs_sorted",
    "build_hamiltonian_with_config",
    "default_config", "default_config_v5",
    "preset_quick", "preset_full", "preset_magic", "preset_deep_sweep",
    "preset_many_vortices", "preset_high_jitter", "preset_ring_vortices",
    "preset_random_vortices", "preset_custom", "preset_auto",
    "preset_balanced", "preset_irrational",
    "generate_alpha_range", "generate_extended_magic_alphas",
    "get_zeta_zeros_safe", "load_zeta_zeros_v5",
    "load_high_T_blocks", "verify_high_T_universality",
    "run", "sweep_parameter", "save_sweep_results",
    "save_csv_report", "save_txt_report", "save_json_report",
    "smoke_test",
]

_MODULE_DIR = os.path.dirname(os.path.abspath(__file__))
_DATA_DIR = os.path.join(_MODULE_DIR, "data")

PI = math.pi

# Debug printing inside compute_all_metrics_* (Julia: cfg_verbose_metrics =
# true; suppressed here by default so the module stays quiet — set to True to
# reproduce the Julia [metrics] debug lines).
cfg_verbose_metrics = False


# ═══════════════════════════════════════════════════════════════════════
# RNG CONTRACT WRAPPER
# ═══════════════════════════════════════════════════════════════════════

class MT19937RNG:
    """Portable RNG contract — every Julia ``MersenneTwister(seed)`` site
    maps to ``MT19937RNG(seed)`` at the same position in the code flow.

    Draw order (not the stream values of Julia's dSFMT) is the porting
    contract: identical call sequences produce identical float streams in
    every language that implements this wrapper.
    """

    __slots__ = ("_mt",)

    def __init__(self, seed: int):
        self._mt = MT19937(int(seed))

    def next_u32(self) -> int:
        return self._mt.next_u32()

    def random(self) -> float:
        """Uniform double in [0,1): ((a>>5)*2**26 + (b>>6)) / 2**53."""
        return self._mt.random()

    def randn(self) -> float:
        """Box-Muller standard normal, exactly 2 draws (u1 redrawn while <=0)."""
        u1 = self.random()
        while u1 <= 0.0:
            u1 = self.random()
        u2 = self.random()
        return math.sqrt(-2.0 * math.log(u1)) * math.cos(2.0 * PI * u2)

    def next_byte(self) -> int:
        """UInt8 draw = top 8 bits of the next u32 (Julia rand(rng, UInt8))."""
        return self.next_u32() >> 24

    def randint(self, lo: int, hi: int) -> int:
        """Int in [lo, hi]: lo + floor(u*(hi-lo+1)) — Julia rand(rng, lo:hi)."""
        return lo + int(math.floor(self.random() * (hi - lo + 1)))

    def choice(self, vec):
        """vec[floor(u*len)] — Julia rand(rng, vec)."""
        return vec[int(math.floor(self.random() * len(vec)))]

    def rand_bytes(self, n: int) -> List[int]:
        return [self.next_byte() for _ in range(n)]


# ═══════════════════════════════════════════════════════════════════════
# JULIA NUMERIC HELPERS
# ═══════════════════════════════════════════════════════════════════════

def _jmax(x, y):
    """Julia max(x, y) = (x < y) ? y : x  (NaN in y → x)."""
    return y if x < y else x


def _jmin(x, y):
    """Julia min(x, y) = (y < x) ? y : x."""
    return y if y < x else x


def _jround(x) -> int:
    """Julia round(Int, x) — round-half-to-even, same as Python round()."""
    return int(round(x))


def _clamp(x, lo, hi):
    return min(max(x, lo), hi)


def _std(x) -> float:
    """Julia std — sample standard deviation (ddof=1); NaN for n<2."""
    a = np.asarray(x, dtype=float)
    n = a.size
    if n <= 1:
        return float("nan")
    m = float(a.mean())
    return float(math.sqrt(float(((a - m) ** 2).sum()) / (n - 1)))


def _var(x) -> float:
    """Julia var — sample variance (ddof=1); NaN for n<2."""
    a = np.asarray(x, dtype=float)
    n = a.size
    if n <= 1:
        return float("nan")
    m = float(a.mean())
    return float(float(((a - m) ** 2).sum()) / (n - 1))


def _cor(x, y) -> float:
    """Pearson correlation (Julia cor)."""
    a = np.asarray(x, dtype=float)
    b = np.asarray(y, dtype=float)
    am = a - a.mean()
    bm = b - b.mean()
    sxx = float((am * am).sum())
    syy = float((bm * bm).sum())
    if sxx <= 0.0 or syy <= 0.0:
        return float("nan")
    return float((am * bm).sum()) / math.sqrt(sxx * syy)


def _colon(start: float, step: float, stop: float) -> List[float]:
    """Julia ``collect(start:step:stop)`` — values start + i*step, with the
    endpoint snapped to ``stop`` when within rounding distance (Julia's
    twice-precision range endpoint behaviour)."""
    q = (stop - start) / step
    n = int(math.floor(q)) + 1
    tol = 1e-9 * max(1.0, abs(start), abs(stop), abs(step))
    while start + n * step <= stop + tol:
        n += 1
    while n > 1 and start + (n - 1) * step > stop + tol:
        n -= 1
    vals = [start + i * step for i in range(n)]
    if n > 0 and abs(vals[-1] - stop) <= 1e-12 * max(1.0, abs(stop)):
        vals[-1] = stop
    return vals


def _jfloat(x) -> str:
    """Float formatted the way Julia's string(::Float64) prints it."""
    x = float(x)
    if math.isnan(x):
        return "NaN"
    if math.isinf(x):
        return "Inf" if x > 0 else "-Inf"
    return repr(x)


def _ts() -> str:
    """Dates.format(now(), "yyyymmdd_HHMMSS")."""
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def _ts_full() -> str:
    """Dates.format(now(), "yyyy-mm-dd HH:MM:SS")."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def _fmt(v, digits: int) -> str:
    """round(v, digits=...) printed Julia-style; None → empty."""
    if v is None:
        return ""
    try:
        return _jfloat(round(float(v), digits))
    except (TypeError, ValueError):
        return str(v)


def _mean(x) -> float:
    a = np.asarray(x, dtype=float)
    return float(a.mean()) if a.size else float("nan")


# ═══════════════════════════════════════════════════════════════════════
# ζ-ZERO TABLES (embedded + external chains)
# ═══════════════════════════════════════════════════════════════════════

# RH_Sweep_Pro.jl: 13 661 embedded verified zeros (mpmath.zetazero, 25 digits).
N_ZETA_ZEROS_AVAILABLE = 13661
ZETA_ZEROS_VERIFIED_COUNT = 13661

_ZETA_SP_EMBEDDED: Optional[List[float]] = None
_ZETA_V5_EMBEDDED: Optional[List[float]] = None


def _read_float_file(path: str) -> List[float]:
    vals: List[float] = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            s = line.strip()
            if not s or s.startswith("#"):
                continue
            vals.append(float(s))
    return vals


def _sp_embedded() -> List[float]:
    global _ZETA_SP_EMBEDDED
    if _ZETA_SP_EMBEDDED is None:
        _ZETA_SP_EMBEDDED = _read_float_file(
            os.path.join(_DATA_DIR, "rh_embedded_zeros_sp.txt"))
    return _ZETA_SP_EMBEDDED


def _v5_embedded() -> List[float]:
    global _ZETA_V5_EMBEDDED
    if _ZETA_V5_EMBEDDED is None:
        _ZETA_V5_EMBEDDED = _read_float_file(
            os.path.join(_DATA_DIR, "rh_embedded_zeros_v5.txt"))
    return _ZETA_V5_EMBEDDED


# --- RH_Sweep_Pro.jl external chain (Odlyzko 2M / 500k tables) -----------

_EXTERNAL_ZETA_ZEROS: Optional[List[float]] = None
_EXTERNAL_ZETA_LOADED = False


def _try_load_external_zeta_zeros() -> None:
    """Port of RH_Sweep_Pro.jl `_try_load_external_zeta_zeros` (L4304).

    Candidate files, in priority order (script dir first, then cwd):
    zeta_zeros_2M_odlyzko.bin / .txt / .txt.gz / zeta_zeros_500k_odlyzko.txt.
    The .bin is raw native little-endian Float64 (Julia reinterpret semantics
    on x86/ARM) — decoded with struct.unpack('<d').
    """
    global _EXTERNAL_ZETA_ZEROS
    script_dir = _MODULE_DIR
    candidate_files = [
        os.path.join(script_dir, "zeta_zeros_2M_odlyzko.bin"),
        os.path.join(script_dir, "zeta_zeros_2M_odlyzko.txt"),
        os.path.join(script_dir, "zeta_zeros_2M_odlyzko.txt.gz"),
        os.path.join(script_dir, "zeta_zeros_500k_odlyzko.txt"),
        os.path.join(os.getcwd(), "zeta_zeros_2M_odlyzko.bin"),
        os.path.join(os.getcwd(), "zeta_zeros_2M_odlyzko.txt"),
        os.path.join(os.getcwd(), "zeta_zeros_500k_odlyzko.txt"),
    ]
    for filepath in candidate_files:
        if not os.path.isfile(filepath):
            continue
        try:
            print(">>> Загрузка внешнего файла ζ-нулей: %s" % filepath)
            t_start = time.time()
            zeros_array: List[float] = []
            if filepath.endswith(".bin"):
                with open(filepath, "rb") as f:
                    raw = f.read()
                n = len(raw) // 8
                zeros_array = list(struct.unpack("<%dd" % n, raw[: n * 8]))
            elif filepath.endswith(".gz"):
                try:
                    with gzip.open(filepath, "rt", encoding="utf-8",
                                   errors="replace") as f:
                        for line in f:
                            s = line.strip()
                            if s and not s.startswith("#"):
                                try:
                                    zeros_array.append(float(s))
                                except ValueError:
                                    pass
                except OSError as e:
                    print("  ⚠ Не удалось распаковать .gz: %s" % e)
                    print("  Установите gzip или используйте .txt/.bin файл")
                    continue
            else:
                with open(filepath, "r", encoding="utf-8",
                          errors="replace") as f:
                    for line in f:
                        s = line.strip()
                        if s and not s.startswith("#"):
                            try:
                                zeros_array.append(float(s))
                            except ValueError:
                                pass
            elapsed = time.time() - t_start
            if len(zeros_array) > 100:
                _EXTERNAL_ZETA_ZEROS = zeros_array
                print("  ✓ Загружено %d ζ-нулей за %.1fs"
                      % (len(zeros_array), elapsed))
                print("  Диапазон t: [%.2f, %.2f]"
                      % (zeros_array[0], zeros_array[-1]))
                if len(zeros_array) >= 500:
                    sr = spacing_ratios(zeros_array)
                    if len(sr) >= 100:
                        r_mean = float(np.mean(sr))
                        print("  ⟨r⟩ = %s (R_GUE = %s)" % (_jfloat(round(r_mean, 6)), R_GUE))
                        if abs(r_mean - R_GUE) < 0.02:
                            print("  ✓ ⟨r⟩ ≈ R_GUE → нули соответствуют GUE статистике")
                return  # successfully loaded
        except Exception as e:  # noqa: BLE001 — Julia catches everything too
            print("  ⚠ Ошибка загрузки %s: %s" % (filepath, e))
    print("ℹ  Внешний файл с ζ-нулями не найден. Используются встроенные 500 нулей.")


def get_zeta_zeros_safe(n: int, prefer_verified: bool = True,
                        mode: str = "sweep_pro"):
    """Port of RH_Sweep_Pro.jl `get_zeta_zeros_safe` (L4263) and of the v5
    variant (RH_Unified_v5.jl L1061) — selected by ``mode``.

    sweep_pro:   external Odlyzko chain (.bin/.txt/.txt.gz/500k), else the
                 embedded 13 661 verified zeros.
    unified_v5:  zeta_zeros_50000.txt / _3000.txt / _extra.txt chain
                 (validated against the 500 embedded), else the embedded 500.
    """
    n = int(n)
    if mode == "unified_v5":
        return _get_zeta_zeros_safe_v5(n, prefer_verified)

    global _EXTERNAL_ZETA_LOADED
    if not _EXTERNAL_ZETA_LOADED:
        _EXTERNAL_ZETA_LOADED = True
        _try_load_external_zeta_zeros()

    if _EXTERNAL_ZETA_ZEROS:
        n_avail = len(_EXTERNAL_ZETA_ZEROS)
        n_use = min(n, n_avail)
        if n > n_avail:
            print("⚠️  WARNING: запрошено %d ζ-нулей, доступно %d (Odlyzko). "
                  "Использую все %d." % (n, n_avail, n_avail))
        return _EXTERNAL_ZETA_ZEROS[:n_use]

    embedded = _sp_embedded()
    n_use = min(n, N_ZETA_ZEROS_AVAILABLE)
    if prefer_verified and n > ZETA_ZEROS_VERIFIED_COUNT:
        print("⚠️  WARNING: запрошено %d ζ-нулей, но только %d верифицированы."
              % (n, ZETA_ZEROS_VERIFIED_COUNT))
        print("   Для больших данных скачайте файл с сайта Andrew Odlyzko:")
        print("   https://www-users.cse.umn.edu/~odlyzko/zeta_tables/zeros6")
        print("   и поместите его рядом с RH_Unified.jl как zeta_zeros_2M_odlyzko.txt")
        n_use = ZETA_ZEROS_VERIFIED_COUNT
    return embedded[:n_use]


# --- RH_Unified_v5.jl chain ---------------------------------------------

_V5_ZETA_ZEROS: Optional[List[float]] = None


def load_zeta_zeros_v5() -> List[float]:
    """Port of RH_Unified_v5.jl `_load_zeta_zeros` (L938).

    Tries zeta_zeros_50000.txt / zeta_zeros_3000.txt / zeta_zeros_extra.txt
    next to this module, then zeta_zeros_50000.txt in the cwd.  A file is
    accepted only if it holds MORE than the 500 embedded zeros, is monotonically
    increasing, and its first 500 values match the embedded table within 1e-6.
    Otherwise the 500 embedded zeros are used (fail-safe fallback).
    """
    embedded = _v5_embedded()
    n_embedded = len(embedded)
    candidates = [
        os.path.join(_MODULE_DIR, "zeta_zeros_50000.txt"),
        os.path.join(_MODULE_DIR, "zeta_zeros_3000.txt"),
        os.path.join(_MODULE_DIR, "zeta_zeros_extra.txt"),
        os.path.join(os.getcwd(), "zeta_zeros_50000.txt"),
    ]
    for path in candidates:
        if not os.path.isfile(path):
            continue
        try:
            vals = _read_float_file(path)
            if len(vals) <= n_embedded:
                print("⚠️  %s: %d нулей (<= встроенных %d) — пропущен."
                      % (path, len(vals), n_embedded))
                continue
            if any(b <= a for a, b in zip(vals, vals[1:])):
                print("⚠️  %s: нули не монотонны — файл повреждён, пропущен." % path)
                continue
            n_check = n_embedded
            max_dev = max(abs(v - e) for v, e in zip(vals[:n_check], embedded[:n_check]))
            if max_dev > 1e-6:
                print("⚠️  %s: первые %d нулей расходятся со встроенными "
                      "(max|Δ|=%s) — пропущен." % (path, n_check, _jfloat(max_dev)))
                continue
            print("✓ Загружено %d ζ-нулей из %s (проверено по первым %d "
                  "встроенным, max|Δ|=%s)."
                  % (len(vals), path, n_check, _jfloat(max_dev)))
            return vals
        except Exception as e:  # noqa: BLE001
            print("⚠️  Не удалось прочитать %s (%s) — используются встроенные 500." % (path, e))
            continue
    return list(embedded)


def _v5_zeta() -> List[float]:
    global _V5_ZETA_ZEROS
    if _V5_ZETA_ZEROS is None:
        _V5_ZETA_ZEROS = load_zeta_zeros_v5()
    return _V5_ZETA_ZEROS


def _get_zeta_zeros_safe_v5(n: int, prefer_verified: bool = True) -> List[float]:
    zeta = _v5_zeta()
    n_avail = len(zeta)
    n_use = min(n, n_avail)
    if prefer_verified and n > n_avail:
        print("⚠️  WARNING: запрошено %d ζ-нулей, но только %d верифицированы."
              % (n, n_avail))
        n_use = n_avail
    return zeta[:n_use]


# --- RH_Unified_v5.jl high-T blocks --------------------------------------

_ZETA_HIGH_T_BLOCKS: Optional[Dict[str, List[float]]] = None


def load_high_T_blocks() -> Dict[str, List[float]]:
    """Port of RH_Unified_v5.jl `_load_high_T_blocks` (L991).

    Parses optional ``zeta_zeros_highT_blocks.txt`` (module dir, then cwd):
    sections ``# BLOCK index=<label> offset=<int>`` followed by local deltas
    gamma − offset (one Float64 per line).  Returns {} when absent.
    """
    blocks: Dict[str, List[float]] = {}
    paths = [os.path.join(_MODULE_DIR, "zeta_zeros_highT_blocks.txt"),
             os.path.join(os.getcwd(), "zeta_zeros_highT_blocks.txt")]
    for path in paths:
        if not os.path.isfile(path):
            continue
        try:
            current = ""
            with open(path, "r", encoding="utf-8") as f:
                for line in f:
                    s = line.strip()
                    if not s:
                        continue
                    if s.startswith("#"):
                        m = re.search(r"index=(\S+)", s)
                        current = m.group(1) if m else s
                        blocks[current] = []
                    elif current:
                        blocks[current].append(float(s))
            if blocks:
                return blocks
        except Exception as e:  # noqa: BLE001
            print("⚠️  Не удалось прочитать %s (%s)." % (path, e))
    return blocks


def _high_T_blocks() -> Dict[str, List[float]]:
    global _ZETA_HIGH_T_BLOCKS
    if _ZETA_HIGH_T_BLOCKS is None:
        _ZETA_HIGH_T_BLOCKS = load_high_T_blocks()
    return _ZETA_HIGH_T_BLOCKS


def verify_high_T_universality():
    """Port of RH_Unified_v5.jl `verify_high_T_universality` (L1032).

    Checks ⟨r⟩ ≈ R_GUE = 0.5996 independently per high-T block
    (indices ~1e12 / 1e21 / 1e22 when the block file is present).
    Returns {label: ⟨r⟩} or None when the block file is absent.
    """
    blocks = _high_T_blocks()
    if not blocks:
        print("ℹ️  zeta_zeros_highT_blocks.txt не найден — high-T проверка пропущена.")
        return None
    print("\n" + "─" * 78)
    print("  GUE-УНИВЕРСАЛЬНОСТЬ НА БОЛЬШИХ ВЫСОТАХ T")
    print("─" * 78)
    results: Dict[str, float] = {}
    for label, deltas in sorted(blocks.items()):
        sr = spacing_ratios(deltas)
        r = float("nan") if len(sr) == 0 else float(np.mean(sr))
        results[label] = r
        dev = abs(r - R_GUE)
        status = "✓" if dev < 0.01 else ("~" if dev < 0.03 else "✗")
        print("  индекс зеро ~%s : n=%d  ⟨r⟩=%s  |Δ от R_GUE|=%s  %s"
              % (label, len(deltas), _jfloat(round(r, 4)),
                 _jfloat(round(dev, 4)), status))
    zeta = _v5_zeta()
    print("  (для сравнения, низкий T, n=%d: ⟨r⟩=%s)"
          % (len(zeta), _jfloat(round(mean_r(zeta), 4))))
    print("─" * 78)
    return results


# ═══════════════════════════════════════════════════════════════════════
# RMT CONSTANTS
# ═══════════════════════════════════════════════════════════════════════

R_GUE = 0.5996      # Mean spacing ratio для GUE
R_GOE = 0.5359      # GOE
R_GSE = 0.6762      # GSE
R_POISSON = 0.3863  # Poisson


# ═══════════════════════════════════════════════════════════════════════
# СПЕКТРАЛЬНЫЕ МЕТРИКИ (kernel, shared by both scripts)
# ═══════════════════════════════════════════════════════════════════════

def spacing_ratios(eigs) -> np.ndarray:
    """min(dᵢ,dᵢ₊₁)/max(dᵢ,dᵢ₊₁) over consecutive gaps of the sorted spectrum."""
    s = np.sort(np.asarray(eigs, dtype=float))
    d = np.diff(s)
    if d.size < 2:
        return np.array([])
    return np.minimum(d[:-1], d[1:]) / np.maximum(d[:-1], d[1:])


def mean_r(eigs) -> float:
    sr = spacing_ratios(eigs)
    return float("nan") if sr.size == 0 else float(np.mean(sr))


def classify_universality_class(r: float) -> Tuple[str, float, float, float, float]:
    """Argmin distance to (R_GUE, R_GOE, R_GSE, R_POISSON); ties resolved
    GUE→GOE→GSE→Poisson by exact float equality (as in Julia)."""
    d_gue = abs(r - R_GUE)
    d_goe = abs(r - R_GOE)
    d_gse = abs(r - R_GSE)
    d_poi = abs(r - R_POISSON)
    d_min = _jmin(_jmin(_jmin(d_gue, d_goe), d_gse), d_poi)
    if d_min == d_gue:
        klass = "GUE"
    elif d_min == d_goe:
        klass = "GOE"
    elif d_min == d_gse:
        klass = "GSE"
    else:
        klass = "Poisson"
    return klass, d_gue, d_goe, d_gse, d_poi


def polynomial_unfold(eigs, deg: int = 3) -> np.ndarray:
    """Polynomial unfolding (default deg=3): regress rank on the standardized
    spectrum, rescale to unit mean spacing, subtract the first value."""
    s = np.sort(np.asarray(eigs, dtype=float))
    n = np.arange(1.0, len(s) + 1.0)
    e_mean = float(np.mean(s))
    e_std = _std(s)
    if e_std < 1e-12:
        return n - n[0]
    e_norm = (s - e_mean) / e_std
    A = np.empty((len(s), deg + 1), dtype=float)
    for k in range(deg + 1):
        A[:, k] = e_norm ** k
    coeffs = np.linalg.lstsq(A, n, rcond=None)[0]
    xi = A @ coeffs
    if len(xi) > 1:
        mean_spacing = (xi[-1] - xi[0]) / (len(xi) - 1)
        if mean_spacing > 1e-12:
            xi = xi / mean_spacing
    return xi - xi[0]


def local_unfold(eigs, window_fraction: float = 0.05) -> np.ndarray:
    """Local-mean unfolding with window = max(3, round(n·frac))."""
    s = np.sort(np.asarray(eigs, dtype=float))
    n = len(s)
    if n < 10:
        return np.asarray(polynomial_unfold(s, 3))
    window = max(3, _jround(n * window_fraction))
    unfolded = np.zeros(n, dtype=float)
    unfolded[0] = 0.0
    for i in range(1, n):
        i_lo = max(0, i - window)
        i_hi = min(n - 1, i + window)
        local_density = (i_hi - i_lo + 1) / (s[i_hi] - s[i_lo] + 1e-12)
        unfolded[i] = unfolded[i - 1] + (s[i] - s[i - 1]) * local_density
    mean_spacing = (unfolded[-1] - unfolded[0]) / (n - 1)
    return unfolded / mean_spacing


def unfold_spectrum(eigs, method: str = "local") -> np.ndarray:
    if method == "polynomial":
        return np.asarray(polynomial_unfold(np.sort(np.asarray(eigs, dtype=float)), 5))
    return np.asarray(local_unfold(np.sort(np.asarray(eigs, dtype=float))))


# --- theory one-liners ---------------------------------------------------

def R2_GUE_theory(s: float) -> float:
    return 0.0 if s == 0 else 1.0 - (math.sin(PI * s) / (PI * s)) ** 2


def R2_Poisson_theory(s: float) -> float:
    return 1.0


def K_GUE_theory(t: float) -> float:
    if t < 0:
        return 0.0
    return t if t < 1.0 else 1.0


def Sigma2_GUE_theory(L: float) -> float:
    if L <= 0:
        return 0.0
    return (1.0 / PI ** 2) * math.log(max(L, 1.0)) + 1.0 / (8 * PI ** 2)


def Sigma2_Poisson_theory(L: float) -> float:
    return L


def Delta3_GUE_theory(L: float) -> float:
    if L <= 0:
        return 0.0
    if L < 1:
        return L / 15.0
    return (1.0 / PI ** 2) * math.log(max(L, 1.0)) + 0.007


def p_GUE_wigner(s: float) -> float:
    if s <= 0:
        return 0.0
    return (32 / PI ** 2) * s ** 2 * math.exp(-4 * s ** 2 / PI)


def p_GOE_wigner(s: float) -> float:
    if s <= 0:
        return 0.0
    return (PI / 2) * s * math.exp(-PI * s ** 2 / 4)


def p_Poisson(s: float) -> float:
    return 0.0 if s < 0 else math.exp(-s)


def rms_error(empirical, theory) -> float:
    e = np.asarray(empirical, dtype=float)
    t = np.asarray(theory, dtype=float)
    return float(math.sqrt(float(np.mean((e - t) ** 2))))


def safe_correlation(x, y) -> float:
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    if x.size != y.size or x.size < 2:
        return 0.0
    sx = _std(x)
    sy = _std(y)
    if sx < 1e-12 or sy < 1e-12:
        return 0.0
    return _cor(x, y)


# --- R₂ (pair correlation) ----------------------------------------------

def _compute_R2_single(eigs, s_values, method: str = "polynomial") -> np.ndarray:
    n = len(eigs)
    if n < 10:
        return np.zeros(len(s_values))
    xi = unfold_spectrum(eigs, method=method)
    iu, ju = np.triu_indices(n, k=1)
    pair_distances = xi[ju] - xi[iu]
    bw = 0.15
    R2 = np.zeros(len(s_values))
    for idx, s in enumerate(s_values):
        if s <= 0:
            continue
        weights = np.exp(-((pair_distances - s) ** 2) / (2 * bw ** 2))
        R2[idx] = float(np.sum(weights)) / (n * bw * math.sqrt(2 * PI))
    return R2


def compute_R2(eigs, s_values, method: str = "polynomial",
               eigs_per_seed: int = 0) -> np.ndarray:
    """R₂(s) with block averaging (binning) when eigs_per_seed > 0
    (RH_Sweep_Pro.jl L4694; v5 calls it with eigs_per_seed=0)."""
    eigs = list(eigs)
    if eigs_per_seed > 0 and len(eigs) > eigs_per_seed:
        n_blocks = len(eigs) // eigs_per_seed
        R2_sum = np.zeros(len(s_values))
        count = 0
        for i in range(n_blocks):
            block = eigs[i * eigs_per_seed:(i + 1) * eigs_per_seed]
            if len(block) < 10:
                continue
            R2_sum += _compute_R2_single(block, s_values, method=method)
            count += 1
        return R2_sum / count if count > 0 else np.zeros(len(s_values))
    n = len(eigs)
    if n < 10:
        return np.zeros(len(s_values))
    xi = unfold_spectrum(eigs, method=method)
    iu, ju = np.triu_indices(n, k=1)
    pair_distances = xi[ju] - xi[iu]
    bw = 0.15
    R2 = np.zeros(len(s_values))
    for idx, s in enumerate(s_values):
        if s <= 0:
            R2[idx] = 0.0
            continue
        weights = np.exp(-((pair_distances - s) ** 2) / (2 * bw ** 2))
        R2[idx] = float(np.sum(weights)) / (n * bw * math.sqrt(2 * PI))
    return R2


# --- K(t) form factor ----------------------------------------------------

def _compute_K_single(eigs, t_values, method: str = "polynomial",
                      smooth: bool = True, smooth_window: int = 3,
                      preserve_ramp: bool = True, ramp_threshold: float = 0.5,
                      connected: bool = False) -> np.ndarray:
    """Form factor on one spectrum.

    sweep_pro (connected=False): FULL Dyson form factor
        K(τ) = |Σ exp(2πi τ ξₙ)|² / n          (ramp τ<1, plateau 1)
    unified_v5 (connected=True):
        K(τ) = max(0, |Σ exp(2πi τ ξₙ)|² / n − 1)

    t=0 stays 0 (δ-peak); smoothing skips the ramp region t < 0.5 when
    preserve_ramp is set.
    """
    n = len(eigs)
    if n < 10:
        return np.zeros(len(t_values))
    xi = unfold_spectrum(eigs, method=method)
    K = np.zeros(len(t_values))
    for idx, t in enumerate(t_values):
        if t == 0.0:
            continue
        phase = 2 * PI * t * xi
        ph = np.exp(1j * phase)
        val = abs(complex(np.sum(ph))) ** 2 / n
        K[idx] = max(0.0, val - 1.0) if connected else val
    if smooth and len(K) > 2 * smooth_window:
        K_smoothed = K.copy()
        for i1 in range(smooth_window + 1, len(K) - smooth_window + 1):
            i0 = i1 - 1  # 0-based index of the Julia 1-based i
            if preserve_ramp and t_values[i0] < ramp_threshold:
                continue
            K_smoothed[i0] = float(np.mean(K[i0 - smooth_window:i0 + smooth_window + 1]))
        K = K_smoothed
    return K


def compute_K_empirical(eigs, t_values, method: str = "polynomial",
                        smooth: bool = True, smooth_window: int = 3,
                        eigs_per_seed: int = 0,
                        connected: bool = False) -> np.ndarray:
    """K(t) with per-seed block averaging (binning).  SP uses the full form
    factor, v5 the connected one — selected via ``connected``."""
    eigs = list(eigs)
    n = len(eigs)
    if n < 10:
        return np.zeros(len(t_values))
    if eigs_per_seed > 0 and n > eigs_per_seed:
        n_seeds_actual = n // eigs_per_seed
        K_sum = np.zeros(len(t_values))
        K_count = 0
        for s in range(n_seeds_actual):
            i_start = s * eigs_per_seed
            i_end = min((s + 1) * eigs_per_seed, n)
            if i_end - i_start < 10:
                continue
            eigs_seed = eigs[i_start:i_end]
            K_sum += _compute_K_single(eigs_seed, t_values, method=method,
                                       smooth=smooth,
                                       smooth_window=smooth_window,
                                       connected=connected)
            K_count += 1
        if K_count > 0:
            return K_sum / K_count
    return _compute_K_single(eigs, t_values, method=method, smooth=smooth,
                             smooth_window=smooth_window, connected=connected)


# --- Σ² (number variance) ------------------------------------------------

def _count_windows(xi: np.ndarray, x0: np.ndarray, x1: np.ndarray) -> np.ndarray:
    """count = #{v : x0 ≤ v < x1} for each window, evaluated exactly like
    Julia's sum((xi .>= x0) .& (xi .< x1)) — no sortedness assumption."""
    counts = np.empty(len(x0), dtype=np.int64)
    chunk = max(1, min(len(x0), 4_000_000 // max(1, len(xi))))
    for a in range(0, len(x0), chunk):
        b = min(len(x0), a + chunk)
        ge = xi[None, :] >= x0[a:b, None]
        lt = xi[None, :] < x1[a:b, None]
        counts[a:b] = (ge & lt).sum(axis=1)
    return counts


def _compute_Sigma2_single(eigs, L_values, method: str = "polynomial") -> np.ndarray:
    n = len(eigs)
    if n < 20:
        return np.zeros(len(L_values))
    xi = unfold_spectrum(eigs, method=method)
    Sigma2 = np.zeros(len(L_values))
    for idx, L in enumerate(L_values):
        if L <= 0:
            continue
        n_windows = max(1, n - _jround(L) - 1)
        x0 = xi[:n_windows]
        counts = _count_windows(xi, x0, x0 + L)
        if len(counts) > 1:
            Sigma2[idx] = _var(counts)
    return Sigma2


def compute_Sigma2(eigs, L_values, method: str = "polynomial",
                   eigs_per_seed: int = 0) -> np.ndarray:
    """Σ²(L) with block averaging (binning) when eigs_per_seed > 0
    (RH_Sweep_Pro.jl L4816; v5 calls it with eigs_per_seed=0, method=:local)."""
    eigs = list(eigs)
    if eigs_per_seed > 0 and len(eigs) > eigs_per_seed:
        n_blocks = len(eigs) // eigs_per_seed
        Sigma2_sum = np.zeros(len(L_values))
        count = 0
        for i in range(n_blocks):
            block = eigs[i * eigs_per_seed:(i + 1) * eigs_per_seed]
            if len(block) < 20:
                continue
            Sigma2_sum += _compute_Sigma2_single(block, L_values, method=method)
            count += 1
        return Sigma2_sum / count if count > 0 else np.zeros(len(L_values))
    n = len(eigs)
    if n < 20:
        return np.zeros(len(L_values))
    xi = unfold_spectrum(eigs, method=method)
    Sigma2 = np.zeros(len(L_values))
    for idx, L in enumerate(L_values):
        if L <= 0:
            Sigma2[idx] = 0.0
            continue
        n_windows = max(1, n - _jround(L) - 1)
        x0 = xi[:n_windows]
        counts = _count_windows(xi, x0, x0 + L)
        if len(counts) > 1:
            Sigma2[idx] = _var(counts)
    return Sigma2


# --- Δ₃ (spectral rigidity) ---------------------------------------------

def _delta3_windows(xi: np.ndarray, n_starts: int, rl: int) -> np.ndarray:
    """Per-window least-squares deviation for starts 1..n_starts with
    i_end = min(n, i_start+rl) (1-based).  Returns the deviations array
    (entry = NaN when the window was skipped)."""
    n = len(xi)
    devs = np.full(n_starts, np.nan)
    full_span = min(n - 1, rl)  # span for a start at position 1 (1-based)
    if n_starts >= 1 and (n - rl - 2) >= 1 and rl >= 3:
        # all windows have the full span rl (>= 3, i.e. none is skipped by the
        # Julia `i_end - i_start < 3` guard) → vectorized
        m = rl + 1
        W = np.lib.stride_tricks.sliding_window_view(xi, m)[:n_starts]
        y = np.arange(float(m))
        xm = W.mean(axis=1)
        ym = float(y.mean())
        num = ((W - xm[:, None]) * (y - ym)).sum(axis=1)
        den = ((W - xm[:, None]) ** 2).sum(axis=1)
        ok = den >= 1e-12
        slope = np.zeros(n_starts)
        intercept = np.zeros(n_starts)
        slope[ok] = num[ok] / den[ok]
        intercept[ok] = ym - slope[ok] * xm[ok]
        yfit = slope[:, None] * W + intercept[:, None]
        dev = ((y - yfit) ** 2).mean(axis=1) / m
        devs[:] = np.where(ok, dev, np.nan)
        return devs
    # degenerate small-n fallback: exact loop with clipped i_end
    for i_start1 in range(1, n_starts + 1):
        i_end = min(n, i_start1 + rl)
        span = i_end - i_start1
        if span < 3:
            continue
        x_local = xi[i_start1 - 1:i_end]
        y_local = np.arange(float(span + 1))
        n_pts = len(x_local)
        if n_pts < 2:
            continue
        xm = float(np.mean(x_local))
        ym = float(np.mean(y_local))
        num = float(((x_local - xm) * (y_local - ym)).sum())
        den = float(((x_local - xm) ** 2).sum())
        if den < 1e-12:
            continue
        slope = num / den
        intercept = ym - slope * xm
        yfit = slope * x_local + intercept
        devs[i_start1 - 1] = float(np.mean((y_local - yfit) ** 2)) / n_pts
    return devs


def _compute_Delta3_single(eigs, L_values, method: str = "polynomial") -> np.ndarray:
    n = len(eigs)
    if n < 20:
        return np.zeros(len(L_values))
    xi = unfold_spectrum(eigs, method=method)
    Delta3 = np.zeros(len(L_values))
    for idx, L in enumerate(L_values):
        if L <= 1:
            Delta3[idx] = L / 15.0
            continue
        rl = _jround(L)
        n_starts = max(1, n - rl - 2)
        devs = _delta3_windows(xi, n_starts, rl)
        valid = devs[~np.isnan(devs)]
        if valid.size:
            Delta3[idx] = float(np.mean(valid))
    return Delta3


def compute_Delta3(eigs, L_values, method: str = "polynomial",
                   eigs_per_seed: int = 0) -> np.ndarray:
    """Δ₃(L) with block averaging (binning) when eigs_per_seed > 0
    (RH_Sweep_Pro.jl L4860; v5 calls it with eigs_per_seed=0, method=:local)."""
    eigs = list(eigs)
    if eigs_per_seed > 0 and len(eigs) > eigs_per_seed:
        n_blocks = len(eigs) // eigs_per_seed
        Delta3_sum = np.zeros(len(L_values))
        count = 0
        for i in range(n_blocks):
            block = eigs[i * eigs_per_seed:(i + 1) * eigs_per_seed]
            if len(block) < 20:
                continue
            Delta3_sum += _compute_Delta3_single(block, L_values, method=method)
            count += 1
        return Delta3_sum / count if count > 0 else np.zeros(len(L_values))
    n = len(eigs)
    if n < 20:
        return np.zeros(len(L_values))
    xi = unfold_spectrum(eigs, method=method)
    Delta3 = np.zeros(len(L_values))
    for idx, L in enumerate(L_values):
        if L <= 1:
            Delta3[idx] = L / 15.0
            continue
        rl = _jround(L)
        n_starts = max(1, n - rl - 2)
        devs = _delta3_windows(xi, n_starts, rl)
        valid = devs[~np.isnan(devs)]
        if valid.size:
            Delta3[idx] = float(np.mean(valid))
    return Delta3


# --- p(s) spacing histogram ----------------------------------------------

def _p_hist_from_xi(xi: np.ndarray, nbins: int) -> Tuple[np.ndarray, np.ndarray]:
    s_max = 4.0
    step = s_max / nbins
    bins = _colon(0.0, step, s_max)
    counts = np.zeros(nbins)
    spacings_norm = np.diff(xi)
    mean_s = float(np.mean(spacings_norm))
    if mean_s != 0.0:
        spacings_norm = spacings_norm / mean_s
    for s in spacings_norm:
        if 0 < s < s_max:
            idx = min(max(math.ceil(s * nbins / s_max), 1), nbins)
            counts[idx - 1] += 1
    bin_width = s_max / nbins
    total = float(np.sum(counts))
    p_hist = counts / (total * bin_width) if total > 0 else np.zeros(nbins)
    bin_centers = (np.asarray(bins[:-1]) + np.asarray(bins[1:])) / 2
    return bin_centers, p_hist


def _compute_p_histogram_single(eigs, nbins: int = 30,
                                method: str = "polynomial"):
    n = len(eigs)
    if n < 10:
        return np.zeros(nbins), np.zeros(nbins)
    xi = unfold_spectrum(eigs, method=method)
    spacings = np.diff(xi)
    mean_s = float(np.mean(spacings))
    if mean_s < 1e-12:
        return np.zeros(nbins), np.zeros(nbins)
    return _p_hist_from_xi(xi, nbins)


def compute_p_histogram(eigs, nbins: int = 30, method: str = "polynomial",
                        eigs_per_seed: int = 0):
    """p(s) histogram with block averaging (binning) when eigs_per_seed > 0
    (RH_Sweep_Pro.jl L4923; v5 calls it with eigs_per_seed=0, method=:local)."""
    eigs = list(eigs)
    if eigs_per_seed > 0 and len(eigs) > eigs_per_seed:
        n_blocks = len(eigs) // eigs_per_seed
        hist_sum = np.zeros(nbins)
        count = 0
        centers = np.zeros(nbins)
        for i in range(n_blocks):
            block = eigs[i * eigs_per_seed:(i + 1) * eigs_per_seed]
            if len(block) < 10:
                continue
            centers, hist = _compute_p_histogram_single(block, nbins=nbins,
                                                        method=method)
            hist_sum += hist
            count += 1
        return centers, (hist_sum / count if count > 0 else np.zeros(nbins))
    n = len(eigs)
    if n < 10:
        return np.zeros(nbins), np.zeros(nbins)
    xi = unfold_spectrum(eigs, method=method)
    return _p_hist_from_xi(xi, nbins)


# ═══════════════════════════════════════════════════════════════════════
# MetricsResult И COMPUTE_ALL_METRICS
# ═══════════════════════════════════════════════════════════════════════

@dataclass
class MetricsResult:
    """Union of the RH_Sweep_Pro.jl MetricsResult (L4982) and the
    RH_Unified_v5.jl byte-level extras (L1520).

    Fields marked (v5) are filled only by compute_all_metrics_v5; the SP
    "new metrics" block is filled only by compute_all_metrics_sp.
    """
    label: str = ""
    L: int = 0
    alpha: float = 0.0
    W: float = 0.0
    sigma: float = 0.0
    seed: int = 0
    n_eigs: int = 0
    r_mean: float = float("nan")
    r_std: float = float("nan")
    r_class: str = "Poisson"
    d_GUE: float = float("nan")
    d_GOE: float = float("nan")
    d_GSE: float = float("nan")
    d_Poisson: float = float("nan")
    R2_rms_GUE: float = float("nan")
    R2_rms_Poisson: float = float("nan")
    R2_rms_zeta: float = float("nan")
    R2_match_GUE: bool = False
    K_corr_GUE: float = float("nan")
    K_corr_zeta: float = float("nan")
    K_match_GUE: bool = False
    K_match_zeta: bool = False
    Sigma2_rms_GUE: float = float("nan")
    Sigma2_rms_Poisson: float = float("nan")
    Sigma2_match_GUE: bool = False
    Delta3_rms_GUE: float = float("nan")
    p_rms_GUE: float = float("nan")
    p_mean: float = float("nan")
    # === НОВЫЕ МЕТРИКИ (sweep_pro) ===
    chi2_pvalue: Optional[float] = None
    chi2_wigner: Optional[float] = None
    brody_beta: Optional[float] = None
    spectral_compressibility: Optional[float] = None
    gap_prob_E1: Optional[float] = None
    r_tilde_mean: Optional[float] = None
    level_number_dev: Optional[float] = None
    symmetry_parameter: Optional[float] = None
    # === v5 BYTE FIELDS (unified_v5) ===
    r_byte_quantized: Optional[float] = None
    byte_quant_diff: Optional[float] = None
    byte_quant_robust: Optional[bool] = None
    rng_entropy_bits: Optional[float] = None
    rng_chi2_z: Optional[float] = None
    rng_uniform_ok: Optional[bool] = None
    byte_match: Optional[bool] = None
    # === final ===
    composite_score: float = float("nan")
    tests_passed: int = 0
    tests_total: int = 0


@dataclass
class ByteDiagnostics:
    """Return type of compute_byte_level_diagnostics (v5 test 8)."""
    r_byte_quantized: float
    byte_quant_diff: float
    byte_quant_robust: bool
    rng_entropy_bits: float
    rng_chi2_z: float
    rng_uniform_ok: bool
    byte_match: bool


def compute_byte_level_diagnostics(eigs_ab, r_ab: float,
                                   n_bytes: int = 200_000, seed: int = 12345,
                                   byte_tol: float = 0.02) -> ByteDiagnostics:
    """Port of RH_Unified_v5.jl `compute_byte_level_diagnostics` (L1555).

    (a) BYTE-QUANTIZATION ROBUSTNESS: squeeze the AB eigenvalues to the
        8-bit range [0,255], round to integer levels, stretch back, recompute
        ⟨r⟩ — GUE classification must survive (|Δr| < byte_tol).
    (b) RNG BYTE-ENTROPY / UNIFORMITY: n_bytes UInt8 draws straight from
        MT19937 (top 8 bits of each u32, i.e. Julia rand(rng, UInt8));
        Shannon entropy of the 256-bin histogram (ideal 8.0 bits) and the
        χ² z-score against uniformity (CLT approximation, df=255).
    """
    eigs = np.asarray(eigs_ab, dtype=float)
    lo = float(np.min(eigs))
    hi = float(np.max(eigs))
    span = hi - lo
    r_quantized = float("nan")
    byte_quant_diff = float("nan")
    if span > 0:
        levels = np.clip(np.round((eigs - lo) / span * 255.0).astype(np.int64), 0, 255)
        quantized = lo + (levels / 255.0) * span
        sr_q = spacing_ratios(quantized)
        if sr_q.size:
            r_quantized = float(np.mean(sr_q))
            byte_quant_diff = abs(r_quantized - r_ab)
    byte_quant_robust = (not math.isnan(byte_quant_diff)) and byte_quant_diff < byte_tol

    rng = MT19937RNG(seed)
    counts = np.zeros(256, dtype=np.int64)
    nb = rng.next_byte
    for _ in range(n_bytes):
        counts[nb()] += 1
    probs = counts / float(n_bytes)
    pos = probs[probs > 0]
    shannon_entropy = float(-np.sum(pos * np.log2(pos)))
    expected = n_bytes / 256.0
    chi2_stat = float(np.sum((counts - expected) ** 2 / expected))
    df = 255
    chi2_z = (chi2_stat - df) / math.sqrt(2.0 * df)
    rng_uniform_ok = abs(chi2_z) < 3.0
    entropy_ok = shannon_entropy > 7.9
    byte_match = byte_quant_robust and rng_uniform_ok and entropy_ok
    return ByteDiagnostics(
        r_byte_quantized=r_quantized, byte_quant_diff=byte_quant_diff,
        byte_quant_robust=byte_quant_robust, rng_entropy_bits=shannon_entropy,
        rng_chi2_z=chi2_z, rng_uniform_ok=rng_uniform_ok,
        byte_match=byte_match)


def compute_all_metrics(eigs_ab, zeta_zeros, mode: str = "sweep_pro", **kw) -> MetricsResult:
    """Dispatcher: mode='sweep_pro' → compute_all_metrics_sp (11 tests),
    mode='unified_v5' → compute_all_metrics_v5 (8 tests, connected K)."""
    if mode == "unified_v5":
        return compute_all_metrics_v5(eigs_ab, zeta_zeros, **kw)
    return compute_all_metrics_sp(eigs_ab, zeta_zeros, **kw)


def compute_all_metrics_sp(eigs_ab, zeta_zeros, label: str = "", L: int = 0,
                           alpha: float = 0.5, W: float = 2.0,
                           sigma: float = 0.5, seed: int = 0,
                           eigs_per_seed: int = 0) -> MetricsResult:
    """Canonical 11-test metrics (RH_Sweep_Pro.jl L5026-5290).

    Binning: K_BLOCK_SIZE=250; ab_chunk = min(eigs_per_seed, 250) (or 250).
    Tests: ⟨r⟩, R₂, K(ζ&GUE), Σ², Δ₃, p(s), χ² Wigner, Brody β,
    compressibility, E(s=1), ⟨r̃⟩.
    """
    eigs_ab = list(eigs_ab)
    n_eigs = len(eigs_ab)
    tests_passed = 0
    tests_total = 11  # 6 старых + 5 новых (Symmetry S исключена из подсчёта)

    K_BLOCK_SIZE = 250
    ab_chunk = min(eigs_per_seed, K_BLOCK_SIZE) if eigs_per_seed > 0 else K_BLOCK_SIZE

    # ⟨r⟩ (per-seed)
    if eigs_per_seed > 0 and n_eigs > eigs_per_seed:
        n_seeds_actual = n_eigs // eigs_per_seed
        r_per_seed: List[float] = []
        for s in range(n_seeds_actual):
            i_start = s * eigs_per_seed
            i_end = min((s + 1) * eigs_per_seed, n_eigs)
            if i_end - i_start < 2:
                continue
            eigs_seed = eigs_ab[i_start:i_end]
            sr_seed = spacing_ratios(eigs_seed)
            if sr_seed.size:
                r_per_seed.append(float(np.mean(sr_seed)))
        r_ab = float(np.mean(r_per_seed)) if r_per_seed else float("nan")
        r_std_ab = _std(r_per_seed) if r_per_seed else float("nan")
        if cfg_verbose_metrics:
            print("    [metrics] per-seed: n_seeds=%d, eigs_per_seed=%d, "
                  "r_per_seed=%s, r_ab=%s"
                  % (n_seeds_actual, eigs_per_seed,
                     [round(v, 4) for v in r_per_seed], round(r_ab, 4)))
    else:
        sr_ab = spacing_ratios(eigs_ab)
        r_ab = float(np.mean(sr_ab)) if sr_ab.size else float("nan")
        r_std_ab = _std(sr_ab) if sr_ab.size else float("nan")
        if cfg_verbose_metrics:
            print("    [metrics] single-seed: n_eigs=%d, r_ab=%s"
                  % (n_eigs, round(r_ab, 4)))
    class_ab, d_gue, d_goe, d_gse, d_poi = classify_universality_class(r_ab)
    sr_zeta = spacing_ratios(zeta_zeros)
    r_zeta = float(np.mean(sr_zeta)) if sr_zeta.size else float("nan")

    if d_gue < 0.05:
        tests_passed += 1

    # R₂ (binning)
    s_values = _colon(0.0, 0.05, 5.0)
    R2_ab = compute_R2(eigs_ab, s_values, method="polynomial",
                       eigs_per_seed=ab_chunk)
    R2_gue = np.array([R2_GUE_theory(s) for s in s_values])
    R2_poi = np.array([R2_Poisson_theory(s) for s in s_values])
    R2_zeta = compute_R2(zeta_zeros, s_values, method="polynomial",
                         eigs_per_seed=K_BLOCK_SIZE)
    R2_rms_gue = rms_error(R2_ab, R2_gue)
    R2_rms_poi = rms_error(R2_ab, R2_poi)
    R2_rms_zeta = rms_error(R2_ab, R2_zeta)
    R2_match = R2_rms_gue < R2_rms_poi
    if R2_match:
        tests_passed += 1

    # K(t) (binning)
    t_values = _colon(0.0, 0.02, 2.0)
    K_ab = compute_K_empirical(eigs_ab, t_values, method="polynomial",
                               smooth=True, smooth_window=5,
                               eigs_per_seed=ab_chunk, connected=False)
    K_gue = np.array([K_GUE_theory(t) for t in t_values])
    K_zeta = compute_K_empirical(zeta_zeros, t_values, method="polynomial",
                                 smooth=True, smooth_window=5,
                                 eigs_per_seed=K_BLOCK_SIZE, connected=False)
    K_corr_gue = safe_correlation(K_ab, K_gue)
    K_corr_zeta = safe_correlation(K_ab, K_zeta)
    if cfg_verbose_metrics:
        print("    [metrics] K(t): binning B=250, method=:polynomial, smooth=5")
        key_idxs = [min(max(_jround(t / 0.02) + 1, 1), len(t_values))
                    for t in (0.1, 0.5, 1.0, 1.5)]
        print("    [metrics] K(t): t=%s" % [t_values[i - 1] for i in key_idxs])
        print("    [metrics] K(t): K_ab  =%s" % [round(K_ab[i - 1], 3) for i in key_idxs])
        print("    [metrics] K(t): K_zeta=%s" % [round(K_zeta[i - 1], 3) for i in key_idxs])
        print("    [metrics] K(t): K_gue =%s" % [round(K_gue[i - 1], 3) for i in key_idxs])
        print("    [metrics] K(t): K_corr_gue=%s, K_corr_zeta=%s"
              % (round(K_corr_gue, 4), round(K_corr_zeta, 4)))
    K_match_gue = (K_corr_zeta > 0.8) and (K_corr_gue > -0.5)
    K_match_zeta = K_corr_zeta > 0.7
    if K_match_gue:
        tests_passed += 1

    # Σ² (binning)
    L_values = _colon(0.5, 0.5, 10.0)
    Sigma2_ab = compute_Sigma2(eigs_ab, L_values, method="polynomial",
                               eigs_per_seed=ab_chunk)
    Sigma2_gue = np.array([Sigma2_GUE_theory(L) for L in L_values])
    Sigma2_poi = np.array([Sigma2_Poisson_theory(L) for L in L_values])
    valid = (~np.isnan(Sigma2_ab)) & (~np.isnan(Sigma2_gue))
    if bool(np.any(valid)):
        Sigma2_rms_gue = rms_error(Sigma2_ab[valid], Sigma2_gue[valid])
        Sigma2_rms_poi = rms_error(Sigma2_ab[valid], Sigma2_poi[valid])
    else:
        Sigma2_rms_gue = float("nan")
        Sigma2_rms_poi = float("nan")
    Sigma2_match = (not math.isnan(Sigma2_rms_gue)) and Sigma2_rms_gue < Sigma2_rms_poi
    if Sigma2_match:
        tests_passed += 1

    # Δ₃ (binning)
    Delta3_ab = compute_Delta3(eigs_ab, L_values, method="polynomial",
                               eigs_per_seed=ab_chunk)
    Delta3_gue = np.array([Delta3_GUE_theory(L) for L in L_values])
    valid_d3 = (~np.isnan(Delta3_ab)) & (~np.isnan(Delta3_gue))
    Delta3_rms_gue = (rms_error(Delta3_ab[valid_d3], Delta3_gue[valid_d3])
                      if bool(np.any(valid_d3)) else float("nan"))
    if (not math.isnan(Delta3_rms_gue)) and Delta3_rms_gue < 0.5:
        tests_passed += 1

    # p(s) (binning)
    p_centers, p_hist = compute_p_histogram(eigs_ab, nbins=30,
                                            method="polynomial",
                                            eigs_per_seed=ab_chunk)
    p_wigner = np.array([p_GUE_wigner(s) for s in p_centers])
    p_rms_gue = rms_error(p_hist, p_wigner)
    p_mean_val = float(np.mean(p_hist))
    if p_rms_gue < 0.2:
        tests_passed += 1

    # === НОВЫЕ МЕТРИКИ (с binning) ===
    # 1. χ² Wigner
    chi2_wigner = 0.0
    for i, s_val in enumerate(p_centers):
        expected = p_GUE_wigner(s_val)
        observed = p_hist[i]
        if expected > 1e-10:
            chi2_wigner += (observed - expected) ** 2 / expected
    chi2_wigner /= max(len(p_hist), 1)
    chi2_pvalue = math.exp(-chi2_wigner / 2.0)
    chi2_pass = chi2_wigner < 0.5
    if chi2_pass:
        tests_passed += 1

    # 2. Brody β (log-log regression на первых 5 бинах)
    brody_beta = 0.0
    if len(p_hist) >= 6:
        log_s = np.log(p_centers[1:6])          # Julia p_centers[2:6]
        log_p = np.log(np.maximum(p_hist[1:6], 1e-10))
        if _std(log_s) > 1e-10:
            brody_beta = _cor(log_s, log_p) * _std(log_p) / _std(log_s)
            brody_beta = _clamp(brody_beta, 0.0, 4.0)
    brody_pass = abs(brody_beta - 2.0) < 0.5
    if brody_pass:
        tests_passed += 1

    # 3. Compressibility (Σ²(L)/L, среднее по последним 3 точкам)
    spectral_compressibility = 0.0
    if len(L_values) >= 3 and not math.isnan(float(Sigma2_ab[-1])):
        last_L = np.asarray(L_values[-3:], dtype=float)
        last_Sigma2 = np.asarray(Sigma2_ab[-3:], dtype=float)
        valid_last = ~np.isnan(last_Sigma2)
        if bool(np.any(valid_last)):
            spectral_compressibility = float(
                np.mean(last_Sigma2[valid_last] / last_L[valid_last]))
    comp_pass = spectral_compressibility < 0.3
    if comp_pass:
        tests_passed += 1

    # 4. E(s=1) gap probability (survival: sum p(s) for s >= 1)
    gap_prob_E1 = 0.0
    if len(p_centers) > 1:
        bin_width = p_centers[1] - p_centers[0]
        idx = p_centers >= 1.0
        gap_prob_E1 = float(np.sum(p_hist[idx]) * bin_width)
    gap_pass = abs(gap_prob_E1 - 0.171) < 0.1  # corrected target 0.171
    if gap_pass:
        tests_passed += 1

    # 5. ⟨r̃⟩ modified (per-seed block averaging)
    r_tilde_mean = float("nan")
    if eigs_per_seed > 0 and n_eigs > eigs_per_seed:
        n_seeds_actual = n_eigs // eigs_per_seed
        r_tildes: List[float] = []
        for s in range(n_seeds_actual):
            i_start = s * eigs_per_seed
            i_end = min((s + 1) * eigs_per_seed, n_eigs)
            if i_end - i_start < 2:
                continue
            sorted_e = np.sort(np.asarray(eigs_ab[i_start:i_end], dtype=float))
            sp = np.diff(sorted_e)
            if len(sp) >= 2:
                ok = (sp[:-1] > 0) & (sp[1:] > 0)
                r_tildes.extend(
                    (np.minimum(sp[:-1][ok], sp[1:][ok])
                     / (sp[:-1][ok] + sp[1:][ok])).tolist())
        r_tilde_mean = float(np.mean(r_tildes)) if r_tildes else float("nan")
    else:
        sorted_e = np.sort(np.asarray(eigs_ab, dtype=float))
        sp = np.diff(sorted_e)
        if len(sp) >= 2:
            ok = (sp[:-1] > 0) & (sp[1:] > 0)
            r_tildes = (np.minimum(sp[:-1][ok], sp[1:][ok])
                        / (sp[:-1][ok] + sp[1:][ok])).tolist()
            r_tilde_mean = float(np.mean(r_tildes)) if r_tildes else float("nan")
    rtilde_pass = (not math.isnan(r_tilde_mean)) and abs(r_tilde_mean - 0.3602) < 0.05
    if rtilde_pass:
        tests_passed += 1

    # 6. Level number deviation (per-block)
    level_number_dev = 0.0
    if eigs_per_seed > 0 and n_eigs > eigs_per_seed:
        n_seeds_actual = n_eigs // eigs_per_seed
        devs: List[float] = []
        for s in range(n_seeds_actual):
            i_start = s * eigs_per_seed
            i_end = min((s + 1) * eigs_per_seed, n_eigs)
            if i_end - i_start < 20:
                continue
            eigs_seed = eigs_ab[i_start:i_end]
            xi_dev = unfold_spectrum(eigs_seed, method="local")
            n_vals = np.arange(float(len(xi_dev)))
            if len(xi_dev) > 2:
                n_mean = float(np.mean(n_vals))
                xi_mean = float(np.mean(xi_dev))
                num = float(((xi_dev - xi_mean) * (n_vals - n_mean)).sum())
                den = float(((xi_dev - xi_mean) ** 2).sum())
                if den > 1e-10:
                    slope = num / den
                    intercept = n_mean - slope * xi_mean
                    n_fit = slope * xi_dev + intercept
                    devs.append(float(np.mean((n_vals - n_fit) ** 2)))
        level_number_dev = float(np.mean(devs)) if devs else 0.0

    # 7. Symmetry S (informational, not counted in tests_total)
    symmetry_parameter = 0.0 if math.isnan(r_ab) else r_ab / _jmax(1.0 - r_ab, 1e-10)

    # Composite score (out of 100, 12 components)
    score = 0.0
    score += 10 * _jmax(0, 1 - d_gue / 0.1)
    score += 10 * _jmax(0, 1 - R2_rms_gue / 0.3)
    score += 15 * _jmax(0, K_corr_gue)
    score += 10 * _jmax(0, 1 - Sigma2_rms_gue / 2.0)
    score += 10 * _jmax(0, 1 - Delta3_rms_gue / 0.5)
    score += 10 * _jmax(0, 1 - p_rms_gue / 0.3)
    score += 5 * _jmax(0, 1 - chi2_wigner / 1.0)
    score += 5 * _jmax(0, 1 - abs(brody_beta - 2.0) / 1.0)
    score += 5 * _jmax(0, 1 - spectral_compressibility / 0.5)
    score += 5 * _jmax(0, 1 - abs(gap_prob_E1 - 0.171) / 0.2)
    score += 5 * _jmax(0, 1 - abs(r_tilde_mean - 0.3602) / 0.1)
    score += 10 * _jmax(0, K_corr_zeta)
    composite_score = _clamp(score, 0.0, 100.0)

    if cfg_verbose_metrics:
        print("    [metrics] === НОВЫЕ МЕТРИКИ RMT ===")
        print("    [metrics] χ² Wigner:     %s  (цель: <0.5, p-value=%s)"
              % (round(chi2_wigner, 4), round(chi2_pvalue, 4)))
        print("    [metrics] Brody β:       %s  (цель: ~2.0 для GUE)"
              % round(brody_beta, 4))
        print("    [metrics] Compressibility: %s  (цель: <0.3 для GUE)"
              % round(spectral_compressibility, 4))
        print("    [metrics] E(s=1) gap:    %s  (цель: ~0.171 для GUE)"
              % round(gap_prob_E1, 4))
        print("    [metrics] ⟨r̃⟩ modified:  %s  (цель: ~0.3602 для GUE)"
              % round(r_tilde_mean, 4))
        print("    [metrics] ⟨δ²_n⟩ dev:    %s  (цель: →0)"
              % round(level_number_dev, 4))
        print("    [metrics] Symmetry S:    %s  (инфо, цель: ~1.496)"
              % round(symmetry_parameter, 4))

    return MetricsResult(
        label=label, L=int(L), alpha=float(alpha), W=float(W),
        sigma=float(sigma), seed=int(seed), n_eigs=n_eigs,
        r_mean=r_ab, r_std=r_std_ab, r_class=class_ab,
        d_GUE=d_gue, d_GOE=d_goe, d_GSE=d_gse, d_Poisson=d_poi,
        R2_rms_GUE=R2_rms_gue, R2_rms_Poisson=R2_rms_poi,
        R2_rms_zeta=R2_rms_zeta, R2_match_GUE=R2_match,
        K_corr_GUE=K_corr_gue, K_corr_zeta=K_corr_zeta,
        K_match_GUE=K_match_gue, K_match_zeta=K_match_zeta,
        Sigma2_rms_GUE=Sigma2_rms_gue, Sigma2_rms_Poisson=Sigma2_rms_poi,
        Sigma2_match_GUE=Sigma2_match,
        Delta3_rms_GUE=Delta3_rms_gue, p_rms_GUE=p_rms_gue, p_mean=p_mean_val,
        chi2_pvalue=chi2_pvalue, chi2_wigner=chi2_wigner,
        brody_beta=brody_beta,
        spectral_compressibility=spectral_compressibility,
        gap_prob_E1=gap_prob_E1,
        r_tilde_mean=r_tilde_mean, level_number_dev=level_number_dev,
        symmetry_parameter=symmetry_parameter,
        composite_score=composite_score, tests_passed=tests_passed,
        tests_total=tests_total,
    )


def compute_all_metrics_v5(eigs_ab, zeta_zeros, label: str = "", L: int = 0,
                           alpha: float = 0.5, W: float = 2.0,
                           sigma: float = 0.5, seed: int = 0,
                           eigs_per_seed: int = 0) -> MetricsResult:
    """v5 8-test metrics (RH_Unified_v5.jl L1597-1779).

    Differences vs sweep_pro: R₂/Σ²/Δ₃/p(s) WITHOUT binning (Σ²/Δ₃/p via
    :local unfolding), CONNECTED K(t) with smooth_window=3 and a symmetric
    common_chunk = max(100, min(ab_seed, zeta_half)) for both spectra,
    K_match_gue = K_corr_gue > 0.8, K_match_zeta = K_corr_zeta > 0.7
    (counted separately), plus the byte-level diagnostics (test 8).
    """
    eigs_ab = list(eigs_ab)
    n_eigs = len(eigs_ab)
    tests_passed = 0
    tests_total = 8

    # ⟨r⟩ (per-seed averaging)
    if eigs_per_seed > 0 and n_eigs > eigs_per_seed:
        n_seeds_actual = n_eigs // eigs_per_seed
        r_per_seed: List[float] = []
        for s in range(n_seeds_actual):
            i_start = s * eigs_per_seed
            i_end = min((s + 1) * eigs_per_seed, n_eigs)
            if i_end - i_start < 2:
                continue
            eigs_seed = eigs_ab[i_start:i_end]
            sr_seed = spacing_ratios(eigs_seed)
            if sr_seed.size:
                r_per_seed.append(float(np.mean(sr_seed)))
        r_ab = float(np.mean(r_per_seed)) if r_per_seed else float("nan")
        r_std_ab = _std(r_per_seed) if r_per_seed else float("nan")
        if cfg_verbose_metrics:
            print("    [metrics] per-seed: n_seeds=%d, eigs_per_seed=%d, "
                  "r_per_seed=%s, r_ab=%s"
                  % (n_seeds_actual, eigs_per_seed,
                     [round(v, 4) for v in r_per_seed], round(r_ab, 4)))
    else:
        sr_ab = spacing_ratios(eigs_ab)
        r_ab = float(np.mean(sr_ab)) if sr_ab.size else float("nan")
        r_std_ab = _std(sr_ab) if sr_ab.size else float("nan")
        if cfg_verbose_metrics:
            print("    [metrics] single-seed: n_eigs=%d, r_ab=%s"
                  % (n_eigs, round(r_ab, 4)))
    class_ab, d_gue, d_goe, d_gse, d_poi = classify_universality_class(r_ab)
    sr_zeta = spacing_ratios(zeta_zeros)
    r_zeta = float(np.mean(sr_zeta)) if sr_zeta.size else float("nan")

    if d_gue < 0.05:
        tests_passed += 1

    # R₂ (no binning)
    s_values = _colon(0.0, 0.05, 5.0)
    R2_ab = compute_R2(eigs_ab, s_values, method="polynomial",
                       eigs_per_seed=0)
    R2_gue = np.array([R2_GUE_theory(s) for s in s_values])
    R2_poi = np.array([R2_Poisson_theory(s) for s in s_values])
    R2_zeta = compute_R2(zeta_zeros, s_values, method="polynomial",
                         eigs_per_seed=0)
    R2_rms_gue = rms_error(R2_ab, R2_gue)
    R2_rms_poi = rms_error(R2_ab, R2_poi)
    R2_rms_zeta = rms_error(R2_ab, R2_zeta)
    R2_match = R2_rms_gue < R2_rms_poi
    if R2_match:
        tests_passed += 1

    # K(t): connected, common chunk for both spectra
    t_values = _colon(0.0, 0.02, 2.0)
    zeta_half = len(zeta_zeros) // 2
    ab_seed = eigs_per_seed if eigs_per_seed > 0 else len(eigs_ab)
    common_chunk = max(100, min(ab_seed, zeta_half))
    K_ab = compute_K_empirical(eigs_ab, t_values, method="polynomial",
                               smooth=True, smooth_window=3,
                               eigs_per_seed=common_chunk, connected=True)
    K_gue = np.array([K_GUE_theory(t) for t in t_values])
    K_zeta = compute_K_empirical(zeta_zeros, t_values, method="polynomial",
                                 smooth=True, smooth_window=3,
                                 eigs_per_seed=common_chunk, connected=True)
    K_corr_gue = safe_correlation(K_ab, K_gue)
    K_corr_zeta = safe_correlation(K_ab, K_zeta)
    if cfg_verbose_metrics:
        print("    [metrics] K(t): common_chunk=%d, ab_seed=%d, zeta_half=%d"
              % (common_chunk, ab_seed, zeta_half))
        key_idxs = [min(max(_jround(t / 0.02) + 1, 1), len(t_values))
                    for t in (0.1, 0.5, 1.0, 1.5)]
        print("    [metrics] K(t): t=%s" % [t_values[i - 1] for i in key_idxs])
        print("    [metrics] K(t): K_corr_gue=%s, K_corr_zeta=%s"
              % (round(K_corr_gue, 4), round(K_corr_zeta, 4)))
    # Two SEPARATE tests with clear meaning (v5 fix of the naming bug):
    K_match_gue = K_corr_gue > 0.8    # тест 3: K(t) похож на ТЕОРИЮ GUE
    K_match_zeta = K_corr_zeta > 0.7  # тест 7: K(t) коррелирует с ζ-нулями
    if K_match_gue:
        tests_passed += 1
    if K_match_zeta:
        tests_passed += 1

    # Σ² (no binning, :polynomial — Julia RH_Unified_v5.jl L1710)
    L_values = _colon(0.5, 0.5, 10.0)
    Sigma2_ab = compute_Sigma2(eigs_ab, L_values, method="polynomial",
                               eigs_per_seed=0)
    Sigma2_gue = np.array([Sigma2_GUE_theory(L) for L in L_values])
    Sigma2_poi = np.array([Sigma2_Poisson_theory(L) for L in L_values])
    valid = (~np.isnan(Sigma2_ab)) & (~np.isnan(Sigma2_gue))
    if bool(np.any(valid)):
        Sigma2_rms_gue = rms_error(Sigma2_ab[valid], Sigma2_gue[valid])
        Sigma2_rms_poi = rms_error(Sigma2_ab[valid], Sigma2_poi[valid])
    else:
        Sigma2_rms_gue = float("nan")
        Sigma2_rms_poi = float("nan")
    Sigma2_match = (not math.isnan(Sigma2_rms_gue)) and Sigma2_rms_gue < Sigma2_rms_poi
    if Sigma2_match:
        tests_passed += 1

    # Δ₃ (no binning, :polynomial — Julia RH_Unified_v5.jl L1727)
    Delta3_ab = compute_Delta3(eigs_ab, L_values, method="polynomial",
                               eigs_per_seed=0)
    Delta3_gue = np.array([Delta3_GUE_theory(L) for L in L_values])
    valid_d3 = (~np.isnan(Delta3_ab)) & (~np.isnan(Delta3_gue))
    Delta3_rms_gue = (rms_error(Delta3_ab[valid_d3], Delta3_gue[valid_d3])
                      if bool(np.any(valid_d3)) else float("nan"))
    if (not math.isnan(Delta3_rms_gue)) and Delta3_rms_gue < 0.5:
        tests_passed += 1

    # p(s) (no binning, :local)
    p_centers, p_hist = compute_p_histogram(eigs_ab, nbins=30,
                                            method="local", eigs_per_seed=0)
    p_wigner = np.array([p_GUE_wigner(s) for s in p_centers])
    p_rms_gue = rms_error(p_hist, p_wigner)
    p_mean_val = float(np.mean(p_hist))
    if p_rms_gue < 0.2:
        tests_passed += 1

    # Байтовая диагностика (тест 8)
    byte_diag = compute_byte_level_diagnostics(eigs_ab, r_ab)
    if cfg_verbose_metrics:
        print("    [metrics] byte: r_full=%s r_byte256=%s Δ=%s | RNG "
              "entropy=%sbit χ²z=%s"
              % (round(r_ab, 4), round(byte_diag.r_byte_quantized, 4),
                 round(byte_diag.byte_quant_diff, 4),
                 round(byte_diag.rng_entropy_bits, 4),
                 round(byte_diag.rng_chi2_z, 2)))
    if byte_diag.byte_match:
        tests_passed += 1

    # Composite score
    score = 0.0
    score += 20 * _jmax(0, 1 - d_gue / 0.1)
    score += 20 * _jmax(0, 1 - R2_rms_gue / 0.3)
    score += 20 * _jmax(0, K_corr_gue)
    score += 15 * _jmax(0, 1 - Sigma2_rms_gue / 2.0)
    score += 15 * _jmax(0, 1 - Delta3_rms_gue / 0.5)
    score += 10 * _jmax(0, 1 - p_rms_gue / 0.3)
    score += 5 * _jmax(0, K_corr_zeta)
    composite_score = _clamp(score, 0.0, 100.0)

    return MetricsResult(
        label=label, L=int(L), alpha=float(alpha), W=float(W),
        sigma=float(sigma), seed=int(seed), n_eigs=n_eigs,
        r_mean=r_ab, r_std=r_std_ab, r_class=class_ab,
        d_GUE=d_gue, d_GOE=d_goe, d_GSE=d_gse, d_Poisson=d_poi,
        R2_rms_GUE=R2_rms_gue, R2_rms_Poisson=R2_rms_poi,
        R2_rms_zeta=R2_rms_zeta, R2_match_GUE=R2_match,
        K_corr_GUE=K_corr_gue, K_corr_zeta=K_corr_zeta,
        K_match_GUE=K_match_gue, K_match_zeta=K_match_zeta,
        Sigma2_rms_GUE=Sigma2_rms_gue, Sigma2_rms_Poisson=Sigma2_rms_poi,
        Sigma2_match_GUE=Sigma2_match,
        Delta3_rms_GUE=Delta3_rms_gue, p_rms_GUE=p_rms_gue, p_mean=p_mean_val,
        r_byte_quantized=byte_diag.r_byte_quantized,
        byte_quant_diff=byte_diag.byte_quant_diff,
        byte_quant_robust=byte_diag.byte_quant_robust,
        rng_entropy_bits=byte_diag.rng_entropy_bits,
        rng_chi2_z=byte_diag.rng_chi2_z,
        rng_uniform_ok=byte_diag.rng_uniform_ok,
        byte_match=byte_diag.byte_match,
        composite_score=composite_score, tests_passed=tests_passed,
        tests_total=tests_total,
    )


# ═══════════════════════════════════════════════════════════════════════
# ЧАСТЬ 3: AB-ОБЛАКО ГАМИЛЬТОНИАНА
# ═══════════════════════════════════════════════════════════════════════

@dataclass
class VortexConfig:
    positions: List[Tuple[float, float]]
    charges: List[int]


def make_vortex_config(L: int, n_vortices: int, layout: str, seed: int = 0,
                       pos_jitter: float = 0.0,
                       charge_flip: float = 0.0) -> VortexConfig:
    """Port of `make_vortex_config` (RH_Sweep_Pro.jl L4445).

    Layouts: hexagonal / ring / random / grid.  RNG: a fresh MT19937RNG(seed)
    (matching the fresh MersenneTwister(seed) inside the Julia function);
    draw order: per vortex — 2 randn (x,y jitter, when pos_jitter>0) then the
    charge-flip draw (when charge_flip>0); in the :random layout the radius,
    angle and charge draws happen BEFORE add_vortex's own draws.
    """
    rng = MT19937RNG(seed)
    positions: List[Tuple[float, float]] = []
    charges: List[int] = []
    cx = (L - 1) / 2
    cy = (L - 1) / 2

    if n_vortices < 1:
        return VortexConfig(positions, charges)

    def add_vortex(x: float, y: float, charge: int) -> None:
        if pos_jitter > 0:
            x += pos_jitter * L * rng.randn()
            y += pos_jitter * L * rng.randn()
        if charge_flip > 0 and rng.random() < charge_flip:
            charge = -charge
        positions.append((x, y))
        charges.append(charge)

    lay = layout[1:] if isinstance(layout, str) and layout.startswith(":") else layout
    if lay == "hexagonal":
        add_vortex(cx, cy, 1)
        n_periph = n_vortices - 1
        if n_periph > 0:
            r = L * 0.3
            for k in range(1, n_periph + 1):
                theta = 2 * PI * (k - 1) / n_periph
                add_vortex(cx + r * math.cos(theta), cy + r * math.sin(theta),
                           1 if k % 2 == 1 else -1)
    elif lay == "ring":
        r = L * 0.35
        for k in range(1, n_vortices + 1):
            theta = 2 * PI * (k - 1) / n_vortices
            add_vortex(cx + r * math.cos(theta), cy + r * math.sin(theta),
                       1 if k % 2 == 1 else -1)
    elif lay == "random":
        for _ in range(n_vortices):
            r = L * (0.1 + 0.4 * rng.random())
            theta = 2 * PI * rng.random()
            add_vortex(cx + r * math.cos(theta), cy + r * math.sin(theta),
                       1 if rng.random() < 0.5 else -1)
    elif lay == "grid":
        side = _jround(math.sqrt(n_vortices))
        if side * side != n_vortices:
            return make_vortex_config(L, n_vortices, ":hexagonal", seed=seed,
                                      pos_jitter=pos_jitter,
                                      charge_flip=charge_flip)
        spacing = L / (side + 1)
        for i in range(1, side + 1):
            for j in range(1, side + 1):
                add_vortex(i * spacing, j * spacing,
                           1 if (i + j) % 2 == 0 else -1)
    else:
        raise ValueError("Неизвестный layout: %s" % layout)

    return VortexConfig(positions, charges)


def central_eigs_sorted(H, window: float = 0.3) -> np.ndarray:
    """Central `window` fraction of the spectrum (quantile cut, sorted)."""
    eigs = np.linalg.eigvalsh(H)
    e0 = float(np.quantile(eigs, 0.5 - window / 2))
    e1 = float(np.quantile(eigs, 0.5 + window / 2))
    sel = eigs[(eigs >= e0) & (eigs <= e1)]
    return np.sort(sel)


# ═══════════════════════════════════════════════════════════════════════
# ЧАСТЬ 6: ДИНАМИЧЕСКАЯ КОНФИГУРАЦИЯ (RHConfig)
# ═══════════════════════════════════════════════════════════════════════

@dataclass
class RHConfig:
    """Mutable config — exact field list of the Julia `RHConfig` struct."""
    L: int = 56
    n_seeds: int = 2
    n_zeta_zeros: int = 5000
    output_dir: str = field(default_factory=lambda: "RH_Run_" + _ts())
    verbose: bool = True
    alpha: float = 1.0 / math.pi
    W: float = 2.0
    sigma: float = 0.5
    t_hop: float = 1.0
    min_vortices: int = 6
    max_vortices: int = 6
    vortex_layout: str = "hexagonal"
    alpha_jitter: float = 0.0
    W_jitter: float = 0.0
    sigma_jitter: float = 0.0
    vortex_pos_jitter: float = 0.0
    vortex_charge_flip: float = 0.0
    use_alpha_sweep: bool = False
    alpha_min: float = -16.0
    alpha_max: float = 16.0
    alpha_step: float = 0.5
    use_magic_alphas: bool = False
    custom_alpha_points: List[float] = field(default_factory=list)
    use_W_sweep: bool = False
    W_min: float = 1.0
    W_max: float = 6.0
    W_step: float = 1.0
    use_sigma_sweep: bool = False
    sigma_min: float = 0.1
    sigma_max: float = 1.0
    sigma_step: float = 0.1
    optimize: bool = False
    fine_grid: bool = False


def default_config() -> RHConfig:
    """RH_Sweep_Pro.jl default (alpha = 1/π irrational, n_zeta_zeros = 5000)."""
    return RHConfig()


def default_config_v5() -> RHConfig:
    """RH_Unified_v5.jl default: n_zeta_zeros = ZETA_ZEROS_VERIFIED_COUNT."""
    cfg = RHConfig()
    cfg.n_zeta_zeros = len(_v5_zeta())  # v5: verified == available
    return cfg


# === PRESETS ===

def preset_quick() -> RHConfig:
    cfg = default_config()
    cfg.L = 24
    cfg.n_seeds = 1
    cfg.n_zeta_zeros = 100
    cfg.min_vortices = 6
    cfg.max_vortices = 6
    cfg.output_dir = "RH_Quick_" + _ts()
    return cfg


def preset_full() -> RHConfig:
    cfg = default_config()
    cfg.L = 84
    cfg.n_seeds = 3
    cfg.n_zeta_zeros = 100000
    cfg.optimize = True
    cfg.fine_grid = True
    cfg.output_dir = "RH_Full_" + _ts()
    return cfg


def preset_magic() -> RHConfig:
    cfg = default_config()
    cfg.L = 56
    cfg.n_seeds = 2
    cfg.n_zeta_zeros = 50000
    cfg.use_magic_alphas = True
    cfg.W = 2.0
    cfg.sigma = 0.5
    cfg.output_dir = "RH_Magic_" + _ts()
    return cfg


def preset_deep_sweep() -> RHConfig:
    cfg = default_config()
    cfg.L = 56
    cfg.n_seeds = 2
    cfg.n_zeta_zeros = 50000
    cfg.use_alpha_sweep = True
    cfg.alpha_min = -16.0
    cfg.alpha_max = 16.0
    cfg.alpha_step = 0.5
    cfg.W = 2.0
    cfg.sigma = 0.5
    cfg.output_dir = "RH_DeepSweep_" + _ts()
    return cfg


def preset_many_vortices(n_vortices: int = 12) -> RHConfig:
    cfg = default_config()
    cfg.L = 56
    cfg.n_seeds = 2
    cfg.n_zeta_zeros = ZETA_ZEROS_VERIFIED_COUNT
    cfg.min_vortices = n_vortices
    cfg.max_vortices = n_vortices
    cfg.W = 2.0
    cfg.sigma = 0.5
    cfg.output_dir = "RH_ManyVortices_%d_%s" % (n_vortices, _ts())
    return cfg


def preset_high_jitter() -> RHConfig:
    cfg = default_config()
    cfg.L = 56
    cfg.n_seeds = 3
    cfg.n_zeta_zeros = ZETA_ZEROS_VERIFIED_COUNT
    cfg.alpha_jitter = 0.1
    cfg.W_jitter = 0.5
    cfg.sigma_jitter = 0.1
    cfg.vortex_pos_jitter = 0.05
    cfg.vortex_charge_flip = 0.1
    cfg.output_dir = "RH_HighJitter_" + _ts()
    return cfg


def preset_ring_vortices(n_vortices: int = 8) -> RHConfig:
    cfg = default_config()
    cfg.L = 56
    cfg.n_seeds = 2
    cfg.n_zeta_zeros = ZETA_ZEROS_VERIFIED_COUNT
    cfg.min_vortices = n_vortices
    cfg.max_vortices = n_vortices
    cfg.vortex_layout = "ring"
    cfg.W = 2.0
    cfg.sigma = 0.5
    cfg.output_dir = "RH_RingVortices_%d_%s" % (n_vortices, _ts())
    return cfg


def preset_random_vortices(n_vortices: int = 10) -> RHConfig:
    cfg = default_config()
    cfg.L = 56
    cfg.n_seeds = 2
    cfg.n_zeta_zeros = ZETA_ZEROS_VERIFIED_COUNT
    cfg.min_vortices = n_vortices
    cfg.max_vortices = n_vortices
    cfg.vortex_layout = "random"
    cfg.W = 2.0
    cfg.sigma = 0.5
    cfg.output_dir = "RH_RandomVortices_%d_%s" % (n_vortices, _ts())
    return cfg


def preset_custom() -> RHConfig:
    cfg = default_config()
    cfg.output_dir = "RH_Custom_" + _ts()
    return cfg


def preset_auto(n_zeta_zeros: int, window: float = 0.3,
                target_ratio: float = 1.0, max_L: int = 128,
                max_seeds: int = 10, verbose: bool = True) -> RHConfig:
    """Port of `preset_auto` (RH_Sweep_Pro.jl L5457): automatic sizing ladder
    L ∈ [64,72,80,88,96,104,112,120,128], eigs_per_seed = floor(window·L²),
    n_seeds = ceil(N_target/eigs_per_seed) capped at max_seeds; N floored to a
    multiple of 250 for the K(t) binning; nzz = min(n, 13661)."""
    N_target = _jround(n_zeta_zeros * target_ratio)
    L_candidates = [64, 72, 80, 88, 96, 104, 112, 120, 128]

    best_L = 56
    best_seeds = 2
    best_N = 0

    for L in L_candidates:
        if L > max_L:
            break
        eigs_per_seed = int(math.floor(window * L * L))
        n_seeds_needed = max(1, math.ceil(N_target / eigs_per_seed))
        if n_seeds_needed <= max_seeds:
            best_L = L
            best_seeds = n_seeds_needed
            best_N = best_seeds * eigs_per_seed
            break
        best_L = L
        best_seeds = max_seeds
        best_N = best_seeds * eigs_per_seed

    n_blocks = best_N // 250
    best_N_aligned = n_blocks * 250

    if verbose:
        print("── авто-подбор параметров AB-облака " + "─" * 30)
        print("  ζ-нулей          = %d" % n_zeta_zeros)
        print("  целевое N_AB     = %d (ratio=%s)" % (N_target, target_ratio))
        print("  L                = %d (матрица %d×%d)" % (best_L, best_L, best_L))
        print("  n_seeds          = %d" % best_seeds)
        print("  window           = %s" % window)
        print("  eigs_per_seed    = %d" % int(math.floor(window * best_L * best_L)))
        print("  N_AB (total)     = %d" % best_N)
        print("  N_AB (aligned 250) = %d" % best_N_aligned)
        print("  n_blocks (B=250) = %d" % n_blocks)

    cfg = default_config()
    cfg.L = best_L
    cfg.n_seeds = best_seeds
    cfg.n_zeta_zeros = min(n_zeta_zeros, N_ZETA_ZEROS_AVAILABLE)
    cfg.output_dir = "RH_Auto_%d_L%d_s%d_%s" % (n_zeta_zeros, best_L,
                                                best_seeds, _ts())
    return cfg


def preset_balanced(n_zeta_zeros: int, max_time_minutes: int = 30) -> RHConfig:
    """Port of `preset_balanced` (RH_Sweep_Pro.jl L5554): time budget
    t_per_seed ≈ 8·(L/56)^6 seconds per seed."""
    max_time_sec = max_time_minutes * 60

    for L in [64, 72, 80, 88, 96, 104, 112, 120, 128]:
        t_per_seed = 8 * (L / 56) ** 6
        eigs_per_seed = int(math.floor(0.3 * L * L))
        n_seeds_needed = max(1, math.ceil(n_zeta_zeros / eigs_per_seed))
        n_seeds = min(n_seeds_needed, 10)
        t_total = t_per_seed * n_seeds

        if t_total <= max_time_sec:
            cfg = preset_auto(n_zeta_zeros, verbose=False)
            cfg.L = L
            cfg.n_seeds = n_seeds
            cfg.output_dir = "RH_Balanced_%d_L%d_s%d_%s" % (n_zeta_zeros, L,
                                                            n_seeds, _ts())
            print("\n  Сбалансированный пресет: L=%d, n_seeds=%d" % (L, n_seeds))
            print("  N_AB ≈ %d, время ≈ %.1fмин"
                  % (n_seeds * eigs_per_seed, t_total / 60))
            return cfg

    print("WARNING: не удалось уложиться в %d мин, берём L=56, n_seeds=2"
          % max_time_minutes)
    cfg = preset_auto(n_zeta_zeros, verbose=False)
    cfg.L = 56
    cfg.n_seeds = 2
    return cfg


def preset_irrational(alpha_symbol: str = "inv_pi",
                      mode: str = "sweep_pro") -> RHConfig:
    """Port of `preset_irrational` (SP L5603 / v5 L1929).

    alpha_symbol ∈ {inv_pi, inv_e, phi, sqrt2, sqrt3, ln2, e_frac};
    L=64, n_seeds=3, W=2, σ=0.5, 6 vortices.  mode='unified_v5' takes the
    v5 verified-zero count (500 without the external file) instead of 13661.
    """
    alpha_values = {
        "inv_pi": 1.0 / math.pi,
        "inv_e": 1.0 / math.e,
        "phi": (1.0 + math.sqrt(5.0)) / 2.0 - 1.0,  # mod 1
        "sqrt2": math.sqrt(2.0) - 1.0,              # mod 1
        "sqrt3": math.sqrt(3.0) - 1.0,              # mod 1
        "ln2": math.log(2.0),
        "e_frac": math.e - 2.0,                     # mod 1
    }
    if alpha_symbol not in alpha_values:
        raise KeyError("Неизвестный alpha_symbol: %s" % alpha_symbol)
    cfg = default_config()
    cfg.alpha = alpha_values[alpha_symbol]
    cfg.L = 64
    cfg.n_seeds = 3
    cfg.n_zeta_zeros = (ZETA_ZEROS_VERIFIED_COUNT if mode == "sweep_pro"
                        else len(_v5_zeta()))
    cfg.W = 2.0
    cfg.sigma = 0.5
    cfg.min_vortices = 6
    cfg.max_vortices = 6
    cfg.output_dir = "RH_Irrational_%s_%s" % (alpha_symbol, _ts())
    return cfg


# ═══════════════════════════════════════════════════════════════════════
# 61 МАГИЧЕСКАЯ ТОЧКА α
# ═══════════════════════════════════════════════════════════════════════

MAGIC_ALPHA_VALUES: List[float] = [
    0.0, 1.0 / 12.0, PI / 30, PI / 29, PI / 28, PI / 27, PI / 26, PI / 25, PI / 24, PI / 23,
    0.137, PI * 1.0, PI / 22, PI / 21, PI / 20, math.sqrt(10.0), PI / 19, 1.0 / 6.0, PI / 18, PI / 17,
    PI / 16, PI / 15, PI / 14, math.sqrt(5.0), PI / 13, 1.0 / 4.0, PI / 12, PI * 2.0, PI / 11, PI / 10,
    math.sqrt(11.0), 1.0 / PI, 1.0 / 3.0, PI / 9, math.e / 2.0, 1.0 / math.e, PI / 8, 2.0 / 5.0, math.sqrt(2.0), PI * 3.0,
    PI / 7, math.sqrt(6.0), math.sqrt(12.0), 1.0 / 2.0, PI / 6, PI * 4.0, math.sqrt(13.0), (1.0 + math.sqrt(5.0)) / 2.0, PI / 5, math.sqrt(7.0),
    2.0 / 3.0, math.log(2.0), PI * 5.0, math.e - 2.0, math.sqrt(3.0), math.sqrt(14.0), 3.0 / 4.0, PI / 4, math.sqrt(8.0), 5.0 / 6.0, math.sqrt(15.0),
]

MAGIC_ALPHA_LABELS: List[str] = [
    "0", "1/12", "π/30", "π/29", "π/28", "π/27", "π/26", "π/25", "π/24", "π/23",
    "~√2-1", "π×1", "π/22", "π/21", "π/20", "√10", "π/19", "1/6", "π/18", "π/17",
    "π/16", "π/15", "π/14", "√5", "π/13", "1/4", "π/12", "π×2", "π/11", "π/10",
    "√11", "~1/π", "1/3", "π/9", "e/2", "1/e", "π/8", "2/5", "√2", "π×3",
    "π/7", "√6", "√12", "1/2", "π/6", "π×4", "√13", "φ", "π/5", "√7",
    "2/3", "ln(2)", "π×5", "e mod1", "√3", "√14", "3/4", "π/4", "√8", "5/6", "√15",
]

N_MAGIC_ALPHAS = len(MAGIC_ALPHA_VALUES)


def generate_alpha_range(alpha_min: float, alpha_max: float,
                         alpha_step: float) -> List[float]:
    """collect(alpha_min:alpha_step:alpha_max)."""
    return _colon(float(alpha_min), float(alpha_step), float(alpha_max))


def generate_extended_magic_alphas(alpha_min: float = -16.0,
                                   alpha_max: float = 16.0
                                   ) -> Tuple[List[float], List[str]]:
    """Port of `generate_extended_magic_alphas` (RH_Sweep_Pro.jl L5627):
    integers, half-integers, kπ (k=−4..4), ±π/k (k∈{2,3,4,5,6,8,12}),
    ±√k (k∈{2,3,5,6,7,8,10,11,12,13,14,15}), specials ±φ ±e ±e/2 ±1/e
    ±ln2 ±1/π ±2π — filtered to range, stably sorted, deduped (|Δ|>1e-10)."""
    alphas: List[float] = []
    labels: List[str] = []

    for a in range(math.ceil(alpha_min), math.floor(alpha_max) + 1):
        alphas.append(float(a))
        labels.append(str(a))

    for a in range(math.ceil(alpha_min - 0.5), math.floor(alpha_max - 0.5) + 1):
        v = a + 0.5
        if alpha_min <= v <= alpha_max:
            alphas.append(v)
            labels.append("%d+0.5" % a)

    for k in range(-4, 5):
        v = k * PI
        if alpha_min <= v <= alpha_max:
            alphas.append(v)
            labels.append("0" if k == 0 else ("π" if k == 1 else ("-π" if k == -1 else "%dπ" % k)))

    for k in [2, 3, 4, 5, 6, 8, 12]:
        for sign in (1, -1):
            v = sign * PI / k
            if alpha_min <= v <= alpha_max:
                alphas.append(v)
                labels.append("π/%d" % k if sign > 0 else "-π/%d" % k)

    for k in [2, 3, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15]:
        for sign in (1, -1):
            v = sign * math.sqrt(float(k))
            if alpha_min <= v <= alpha_max:
                alphas.append(v)
                labels.append("√%d" % k if sign > 0 else "-√%d" % k)

    special = [
        ((1.0 + math.sqrt(5.0)) / 2.0, "φ"), (-(1.0 + math.sqrt(5.0)) / 2.0, "-φ"),
        (math.e, "e"), (-math.e, "-e"),
        (math.e / 2.0, "e/2"), (-math.e / 2.0, "-e/2"),
        (1.0 / math.e, "1/e"), (-1.0 / math.e, "-1/e"),
        (math.log(2.0), "ln(2)"), (-math.log(2.0), "-ln(2)"),
        (1.0 / PI, "1/π"), (-1.0 / PI, "-1/π"),
        (2 * PI, "2π"), (-2 * PI, "-2π"),
    ]
    for v, lbl in special:
        if alpha_min <= v <= alpha_max:
            alphas.append(v)
            labels.append(lbl)

    order = sorted(range(len(alphas)), key=lambda i: alphas[i])  # stable
    alphas = [alphas[i] for i in order]
    labels = [labels[i] for i in order]
    unique_alphas: List[float] = []
    unique_labels: List[str] = []
    for a, l in zip(alphas, labels):
        if not unique_alphas or abs(a - unique_alphas[-1]) > 1e-10:
            unique_alphas.append(a)
            unique_labels.append(l)
    return unique_alphas, unique_labels


# ═══════════════════════════════════════════════════════════════════════
# ЧАСТЬ 7: ГАМИЛЬТОНИАН С JITTER
# ═══════════════════════════════════════════════════════════════════════

def build_hamiltonian_with_config(L: int, alpha: float, W: float, sigma: float,
                                  seed: int, cfg: RHConfig) -> np.ndarray:
    """Port of `build_hamiltonian_with_config` (RH_Sweep_Pro.jl L5689).

    N = L² Hofstadter TORUS, Landau gauge:
      x-bonds: −t·exp(±i·2π·α_eff·y/L)   (y-bonds: −t, real)
      on-site disorder: W_eff·(2·rand−1) — drawn AFTER all hopping entries,
          in x-outer/y-inner site order, from the SAME rng as the jitter
          draws (alpha → W → σ → n_vortices, then disorder);
      vortex on-site term: vcharge·σ_eff·exp(−r/(L·σ_eff·0.5))/r·0.1 for r>0.1.
    Vortex configuration comes from an independent MT19937RNG(seed) inside
    make_vortex_config (exactly like the Julia call site).
    """
    rng = MT19937RNG(seed)
    alpha_eff = alpha + cfg.alpha_jitter * rng.randn() if cfg.alpha_jitter > 0 else alpha
    W_eff = W + cfg.W_jitter * rng.randn() if cfg.W_jitter > 0 else W
    sigma_eff = (max(0.01, sigma + cfg.sigma_jitter * rng.randn())
                 if cfg.sigma_jitter > 0 else sigma)

    n_vortices = cfg.min_vortices
    if cfg.max_vortices > cfg.min_vortices:
        n_vortices = rng.randint(cfg.min_vortices, cfg.max_vortices)

    vortex_config = make_vortex_config(L, n_vortices, cfg.vortex_layout,
                                       seed=seed,
                                       pos_jitter=cfg.vortex_pos_jitter,
                                       charge_flip=cfg.vortex_charge_flip)

    N = L * L
    H = np.zeros((N, N), dtype=np.complex128)
    t = cfg.t_hop

    for x in range(L):
        for y in range(L):
            i = (x % L) * L + (y % L)
            j = ((x + 1) % L) * L + (y % L)
            phase_x = 2.0 * PI * alpha_eff * y / L
            H[i, j] -= t * cmath.exp(1j * phase_x)
            H[j, i] -= t * cmath.exp(-1j * phase_x)
            j = (x % L) * L + ((y + 1) % L)
            H[i, j] -= t
            H[j, i] -= t

    for x in range(L):
        for y in range(L):
            i = (x % L) * L + (y % L)
            H[i, i] += W_eff * (2.0 * rng.random() - 1.0)

    for (vx, vy), vcharge in zip(vortex_config.positions, vortex_config.charges):
        for x in range(L):
            for y in range(L):
                i = (x % L) * L + (y % L)
                dx = x - vx
                dy = y - vy
                r = math.sqrt(dx * dx + dy * dy)
                if r > 0.1:
                    vortex_phase = vcharge * sigma_eff * math.exp(
                        -r / (L * sigma_eff * 0.5)) / r
                    H[i, i] += vortex_phase * 0.1

    return H


# ═══════════════════════════════════════════════════════════════════════
# ЧАСТЬ 8: ОТЧЁТЫ
# ═══════════════════════════════════════════════════════════════════════

_CSV_HEADERS = ["label", "L", "alpha", "W", "sigma", "n_eigs",
                "r_mean", "r_std", "r_class",
                "d_GUE", "d_GOE", "d_GSE", "d_Poisson",
                "R2_rms_GUE", "R2_rms_Poisson", "R2_rms_zeta", "R2_match_GUE",
                "K_corr_GUE", "K_corr_zeta", "K_match_GUE", "K_match_zeta",
                "Sigma2_rms_GUE", "Sigma2_rms_Poisson", "Sigma2_match_GUE",
                "Delta3_rms_GUE", "p_rms_GUE", "p_mean",
                "chi2_wigner", "chi2_pvalue", "brody_beta",
                "spectral_compressibility", "gap_prob_E1",
                "r_tilde_mean", "level_number_dev", "symmetry_parameter",
                "composite_score", "tests_passed", "tests_total"]


def _bool_tf(v) -> str:
    return "TRUE" if v else "FALSE"


def save_csv_report(result: MetricsResult, all_results: Sequence[MetricsResult],
                    filepath: str) -> None:
    """Port of `save_csv_report` (RH_Sweep_Pro.jl L5775) — column names 1:1.
    (v5 results have no χ²/Brody/... fields → those cells are empty.)"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("# RH_Unified — CSV отчёт\n")
        f.write("# Дата: %s\n" % _ts_full())
        f.write("#\n")
        f.write(",".join(_CSV_HEADERS) + "\n")
        for r in all_results:
            row = [
                '"%s"' % r.label,
                str(r.L), _fmt(r.alpha, 6), _fmt(r.W, 6), _fmt(r.sigma, 6),
                str(r.n_eigs),
                _fmt(r.r_mean, 6), _fmt(r.r_std, 6), r.r_class,
                _fmt(r.d_GUE, 6), _fmt(r.d_GOE, 6),
                _fmt(r.d_GSE, 6), _fmt(r.d_Poisson, 6),
                _fmt(r.R2_rms_GUE, 6), _fmt(r.R2_rms_Poisson, 6),
                _fmt(r.R2_rms_zeta, 6), _bool_tf(r.R2_match_GUE),
                _fmt(r.K_corr_GUE, 6), _fmt(r.K_corr_zeta, 6),
                _bool_tf(r.K_match_GUE), _bool_tf(r.K_match_zeta),
                _fmt(r.Sigma2_rms_GUE, 6), _fmt(r.Sigma2_rms_Poisson, 6),
                _bool_tf(r.Sigma2_match_GUE),
                _fmt(r.Delta3_rms_GUE, 6), _fmt(r.p_rms_GUE, 6),
                _fmt(r.p_mean, 6),
                _fmt(r.chi2_wigner, 6), _fmt(r.chi2_pvalue, 6),
                _fmt(r.brody_beta, 6),
                _fmt(r.spectral_compressibility, 6), _fmt(r.gap_prob_E1, 6),
                _fmt(r.r_tilde_mean, 6), _fmt(r.level_number_dev, 6),
                _fmt(r.symmetry_parameter, 6),
                _fmt(r.composite_score, 4),
                str(r.tests_passed), str(r.tests_total),
            ]
            f.write(",".join(row) + "\n")
    print("  CSV отчёт: %s" % filepath)


def save_txt_report(result: MetricsResult, all_results: Sequence[MetricsResult],
                    filepath: str, params) -> None:
    """Plain-text flavour of `save_txt_report` (L5820) — same content fields,
    no ASCII box art (documented exclusion of the fancy formatting)."""
    alpha, W, sigma = params
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("=" * 78 + "\n")
        f.write("  RH_Unified — ПОЛНЫЙ ОТЧЁТ\n")
        f.write("  Дата: %s\n" % _ts_full())
        f.write("=" * 78 + "\n\n")
        f.write("  ЛУЧШАЯ КОНФИГУРАЦИЯ AB-ОБЛАКА:\n")
        f.write("    α (поток AB)        = %s\n" % alpha)
        f.write("    W (беспорядок)      = %s\n" % W)
        f.write("    σ (радиус вихря)    = %s\n" % sigma)
        f.write("    Composite Score     = %s / 100\n" % round(result.composite_score, 2))
        f.write("    Тестов пройдено     = %d / %d\n\n"
                % (result.tests_passed, result.tests_total))
        f.write("-" * 78 + "\n")
        f.write("  ТАБЛИЦА 1: ОСНОВНЫЕ МЕТРИКИ\n")
        f.write("-" * 78 + "\n")
        rows1 = [
            ("⟨r⟩", _fmt(result.r_mean, 6), R_GUE, _fmt(result.d_GUE, 6)),
            ("R₂ RMS(GUE)", _fmt(result.R2_rms_GUE, 6), "→ 0", "-"),
            ("R₂ RMS(Poisson)", _fmt(result.R2_rms_Poisson, 6), "→ ∞", "-"),
            ("R₂ RMS(ζ)", _fmt(result.R2_rms_zeta, 6), "→ 0", "-"),
            ("K corr(GUE)", _fmt(result.K_corr_GUE, 6), "→ +1", "-"),
            ("K corr(ζ)", _fmt(result.K_corr_zeta, 6), "→ +1", "-"),
            ("Σ² RMS(GUE)", _fmt(result.Sigma2_rms_GUE, 6), "→ 0", "-"),
            ("Δ₃ RMS(GUE)", _fmt(result.Delta3_rms_GUE, 6), "→ 0", "-"),
            ("p(s) RMS(GUE)", _fmt(result.p_rms_GUE, 6), "→ 0", "-"),
        ]
        for name, val, target, dev in rows1:
            f.write("    %-18s = %-14s (цель %s, откл. %s)\n" % (name, val, target, dev))
        f.write("\n" + "-" * 78 + "\n")
        f.write("  ТАБЛИЦА 2: РЕЗУЛЬТАТЫ ТЕСТОВ (6 тестов RMT)\n")
        f.write("-" * 78 + "\n")
        rows3 = [
            (1, "⟨r⟩ ≈ R_GUE", "|d_GUE| < 0.05", result.d_GUE < 0.05),
            (2, "R₂(s) ≈ R₂^GUE", "RMS(GUE) < RMS(Poi)", result.R2_match_GUE),
            (3, "K(t) ≈ K(ζ)", "corr(ζ)>0.8 & corr(GUE)>-0.5", result.K_match_GUE),
            (4, "Σ²(L) ≈ Σ²^GUE", "RMS(GUE) < RMS(Poi)", result.Sigma2_match_GUE),
            (5, "Δ₃(L) ≈ Δ₃^GUE", "RMS(GUE) < 0.5",
             (not math.isnan(result.Delta3_rms_GUE)) and result.Delta3_rms_GUE < 0.5),
            (6, "p(s) ≈ Wigner", "RMS(GUE) < 0.2",
             (not math.isnan(result.p_rms_GUE)) and result.p_rms_GUE < 0.2),
        ]
        n_pass = 0
        for num, name, crit, ok in rows3:
            n_pass += 1 if ok else 0
            f.write("    %d. %-16s %-28s %s\n"
                    % (num, name, crit, "✓ PASS" if ok else "✗ FAIL"))
        f.write("\n  Итого: %d / 6 тестов пройдено\n" % n_pass)
        f.write("\n" + "=" * 78 + "\n")
    print("  TXT отчёт: %s" % filepath)


def _jsonable(x):
    if x is None:
        return None
    if isinstance(x, bool):
        return x
    if isinstance(x, (int,)):
        return x
    try:
        xf = float(x)
    except (TypeError, ValueError):
        return x
    if math.isnan(xf) or math.isinf(xf):
        return None  # Julia JSON prints NaN as null
    return xf


def save_json_report(result: MetricsResult, all_results: Sequence[MetricsResult],
                     filepath: str, params) -> None:
    """Port of `save_json_report` (RH_Sweep_Pro.jl L5875)."""
    alpha, W, sigma = params
    data = {
        "metadata": {
            "timestamp": _ts_full(),
            "script": "RH_Unified.jl",
            "n_zeta_zeros": N_ZETA_ZEROS_AVAILABLE,
            "n_zeta_verified": ZETA_ZEROS_VERIFIED_COUNT,
        },
        "best_params": {"alpha": _jsonable(alpha), "W": _jsonable(W),
                        "sigma": _jsonable(sigma)},
        "best_result": {
            "label": result.label, "L": result.L, "alpha": _jsonable(result.alpha),
            "W": _jsonable(result.W), "sigma": _jsonable(result.sigma),
            "n_eigs": result.n_eigs,
            "r_mean": _jsonable(result.r_mean), "r_class": result.r_class,
            "K_corr_GUE": _jsonable(result.K_corr_GUE),
            "K_corr_zeta": _jsonable(result.K_corr_zeta),
            "R2_rms_GUE": _jsonable(result.R2_rms_GUE),
            "R2_rms_zeta": _jsonable(result.R2_rms_zeta),
            "Sigma2_rms_GUE": _jsonable(result.Sigma2_rms_GUE),
            "Delta3_rms_GUE": _jsonable(result.Delta3_rms_GUE),
            "p_rms_GUE": _jsonable(result.p_rms_GUE),
            "composite_score": _jsonable(result.composite_score),
            "tests_passed": result.tests_passed,
            "tests_total": result.tests_total,
        },
    }
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False, allow_nan=False)
        f.write("\n")
    print("  JSON отчёт: %s" % filepath)


def _writedlm(filepath: str, values) -> None:
    """writedlm — one Julia-formatted Float64 per line."""
    with open(filepath, "w", encoding="utf-8") as f:
        for v in values:
            f.write(_jfloat(v) + "\n")


# ═══════════════════════════════════════════════════════════════════════
# ЧАСТЬ 10: ГЛАВНАЯ ФУНКЦИЯ run(cfg)
# ═══════════════════════════════════════════════════════════════════════

def run(cfg: RHConfig) -> Dict[str, Any]:
    """Port of `run(cfg)` (RH_Sweep_Pro.jl L6303) — α list selection
    (magic / sweep / custom / single) → per-α per-seed Hamiltonian builds →
    central_eigs_sorted → concatenation → compute_all_metrics_sp → best by
    composite_score → _final_run at the best α (reports written; plots are a
    documented exclusion)."""
    t_start_total = time.time()
    dt_start = datetime.now()

    os.makedirs(cfg.output_dir, exist_ok=True)
    plots_dir = os.path.join(cfg.output_dir, "plots")
    csv_dir = os.path.join(cfg.output_dir, "csv")
    txt_dir = os.path.join(cfg.output_dir, "txt")
    json_dir = os.path.join(cfg.output_dir, "json")
    for d in (plots_dir, csv_dir, txt_dir, json_dir):
        os.makedirs(d, exist_ok=True)

    zeta_zeros = get_zeta_zeros_safe(cfg.n_zeta_zeros)

    # Определяем список α
    if cfg.use_magic_alphas:
        alpha_list = list(MAGIC_ALPHA_VALUES)
        alpha_labels = list(MAGIC_ALPHA_LABELS)
    elif cfg.use_alpha_sweep:
        alpha_list = _colon(cfg.alpha_min, cfg.alpha_step, cfg.alpha_max)
        alpha_labels = [_jfloat(round(a, 3)) for a in alpha_list]
    elif cfg.custom_alpha_points:
        alpha_list = [float(a) for a in cfg.custom_alpha_points]
        alpha_labels = [_jfloat(round(a, 4)) for a in alpha_list]
    else:
        alpha_list = [float(cfg.alpha)]
        alpha_labels = [_jfloat(cfg.alpha)]

    n_alphas = len(alpha_list)
    if cfg.verbose:
        print("всего точек α: %d" % n_alphas)
    t_step1 = time.time()

    results: List[MetricsResult] = []
    best_score = -1.0
    best_result: Optional[MetricsResult] = None
    best_alpha = alpha_list[0]
    best_label = alpha_labels[0]

    for idx, (alpha, label) in enumerate(zip(alpha_list, alpha_labels), start=1):
        if cfg.verbose:
            print("\n[%d/%d] α=%s (%s)" % (idx, n_alphas, label, alpha))

        eigs_all: List[float] = []
        eigs_per_seed = 0
        for seed_ in range(cfg.n_seeds):
            t_seed = time.time()
            H = build_hamiltonian_with_config(cfg.L, alpha, cfg.W, cfg.sigma,
                                              seed_, cfg)
            eigs_seed = central_eigs_sorted(H, window=0.3)
            if seed_ == 0:
                eigs_per_seed = len(eigs_seed)
            eigs_all.extend(float(v) for v in eigs_seed)
            if cfg.verbose:
                print("    seed=%d: %d eigs · ⟨r⟩=%s · %.1fs"
                      % (seed_, len(eigs_seed),
                         "NaN" if math.isnan(mean_r(eigs_seed)) else "%.4f" % mean_r(eigs_seed),
                         time.time() - t_seed))

        result = compute_all_metrics_sp(
            eigs_all, zeta_zeros, label="α=%s" % label, L=cfg.L, alpha=alpha,
            W=cfg.W, sigma=cfg.sigma, seed=-1, eigs_per_seed=eigs_per_seed)
        results.append(result)

        if cfg.verbose:
            print("  ⟹ ⟨r⟩=%s, класс=%s" % (_fmt(result.r_mean, 4), result.r_class))
            print("  ⟹ K corr(ζ)=%s" % _fmt(result.K_corr_zeta, 4))
            print("  ⟹ Score=%s/100, тестов %d/%d"
                  % (_fmt(result.composite_score, 2), result.tests_passed,
                     result.tests_total))

        if result.composite_score > best_score:
            best_score = result.composite_score
            best_result = result
            best_alpha = alpha
            best_label = label

    if cfg.verbose:
        print("конец sweep: заняло %.1fs" % (time.time() - t_step1))
        print("best α — лучшая конфигурация:")
        print("  α = %s (%s)" % (best_label, best_alpha))
        print("  ✓ Composite Score = %s/100" % round(best_score, 2))

    # Финальный прогон с лучшим α
    return _final_run(cfg, best_alpha, cfg.W, cfg.sigma, results,
                      plots_dir, csv_dir, txt_dir, json_dir,
                      t_start_total, dt_start, zeta_zeros,
                      best_label=best_label)


def _final_run(cfg: RHConfig, alpha_opt: float, W_opt: float, sigma_opt: float,
               all_results: List[MetricsResult], plots_dir: str, csv_dir: str,
               txt_dir: str, json_dir: str, t_start_total: float,
               dt_start: datetime, zeta_zeros, best_label: str = ""
               ) -> Dict[str, Any]:
    """Port of `_final_run` (RH_Sweep_Pro.jl L6422) — computation core only:
    rebuild at α_opt, final metrics, reports (CSV/TXT/JSON + writedlm);
    plots/verdict-panels/AURORA are documented exclusions."""
    t_step2 = time.time()
    if cfg.verbose:
        print("финальный прогон: α=%s, W=%s, σ=%s"
              % (round(alpha_opt, 4), W_opt, sigma_opt))

    eigs_final: List[float] = []
    eigs_per_seed_final = 0
    for seed_ in range(cfg.n_seeds):
        t_seed = time.time()
        H = build_hamiltonian_with_config(cfg.L, alpha_opt, W_opt, sigma_opt,
                                          seed_, cfg)
        eigs_seed = central_eigs_sorted(H, window=0.3)
        if seed_ == 0:
            eigs_per_seed_final = len(eigs_seed)
        eigs_final.extend(float(v) for v in eigs_seed)
        if cfg.verbose:
            print("    seed=%d: %d eigs · ⟨r⟩=%s · %.1fs"
                  % (seed_, len(eigs_seed),
                     "NaN" if math.isnan(mean_r(eigs_seed)) else "%.4f" % mean_r(eigs_seed),
                     time.time() - t_seed))
    if cfg.verbose:
        print("    ⏱  Конец (заняло %.1fs)" % (time.time() - t_step2))

    final_label = "final_optimal" if not best_label else "final_α=%s" % best_label
    final_result = compute_all_metrics_sp(
        eigs_final, zeta_zeros, label=final_label, L=cfg.L, alpha=alpha_opt,
        W=W_opt, sigma=sigma_opt, seed=-1, eigs_per_seed=eigs_per_seed_final)
    all_results.append(final_result)

    best_params = (alpha_opt, W_opt, sigma_opt)

    # Отчёты (графики — документированное исключение; plots_dir создаётся,
    # но остаётся пустым)
    save_csv_report(final_result, all_results, os.path.join(csv_dir, "metrics.csv"))
    save_txt_report(final_result, all_results, os.path.join(txt_dir, "report.txt"),
                    best_params)
    save_json_report(final_result, all_results,
                     os.path.join(json_dir, "results.json"), best_params)
    _writedlm(os.path.join(csv_dir, "zeta_zeros.txt"), zeta_zeros)
    _writedlm(os.path.join(csv_dir, "ab_eigs.txt"),
              np.sort(np.asarray(eigs_final, dtype=float)))

    # Вердикт (plain-text вместо AURORA-панелей)
    if cfg.verbose:
        chi2_pass = final_result.chi2_wigner is not None and final_result.chi2_wigner < 0.5
        brody_pass = (final_result.brody_beta is not None
                      and abs(final_result.brody_beta - 2.0) < 0.5)
        comp_pass = (final_result.spectral_compressibility is not None
                     and final_result.spectral_compressibility < 0.3)
        gap_pass = (final_result.gap_prob_E1 is not None
                    and abs(final_result.gap_prob_E1 - 0.171) < 0.1)
        rtilde_pass = (final_result.r_tilde_mean is not None
                       and not math.isnan(final_result.r_tilde_mean)
                       and abs(final_result.r_tilde_mean - 0.3602) < 0.05)
        print("итоговый вердикт — тесты RMT (основные):")
        print("  %s 1. ⟨r⟩ ≈ R_GUE" % ("✓" if final_result.d_GUE < 0.05 else "✗"))
        print("  %s 2. R₂(s) ближе к GUE, чем к Poisson"
              % ("✓" if final_result.R2_match_GUE else "✗"))
        print("  %s 3. K(t) коррелирует с K(ζ)"
              % ("✓" if final_result.K_match_GUE else "✗"))
        print("  %s 4. Σ²(L) ближе к GUE, чем к Poisson"
              % ("✓" if final_result.Sigma2_match_GUE else "✗"))
        print("  %s 5. Δ₃(L) RMS < 0.5"
              % ("✓" if (not math.isnan(final_result.Delta3_rms_GUE)
                         and final_result.Delta3_rms_GUE < 0.5) else "✗"))
        print("  %s 6. p(s) RMS < 0.2"
              % ("✓" if (not math.isnan(final_result.p_rms_GUE)
                         and final_result.p_rms_GUE < 0.2) else "✗"))
        print("итоговый вердикт — тесты RMT (новые):")
        print("  %s 7. χ² Wigner < 0.5      · значение: %s"
              % ("✓" if chi2_pass else "✗", _fmt(final_result.chi2_wigner, 4)))
        print("  %s 8. Brody β ≈ 2.0 (±0.5) · значение: %s"
              % ("✓" if brody_pass else "✗", _fmt(final_result.brody_beta, 4)))
        print("  %s 9. Compressibility < 0.3 · значение: %s"
              % ("✓" if comp_pass else "✗",
                 _fmt(final_result.spectral_compressibility, 4)))
        print("  %s 10. E(s=1) ≈ 0.171 (±0.15) · значение: %s"
              % ("✓" if gap_pass else "✗", _fmt(final_result.gap_prob_E1, 4)))
        print("  %s 11. ⟨r̃⟩ ≈ 0.3602 (±0.05)  · значение: %s"
              % ("✓" if rtilde_pass else "✗", _fmt(final_result.r_tilde_mean, 4)))
        print("итого тестов: %d/%d · Score: %s/100"
              % (final_result.tests_passed, final_result.tests_total,
                 _fmt(final_result.composite_score, 1)))

    t_end = time.time()
    dt_end = datetime.now()
    elapsed = t_end - t_start_total
    if elapsed < 60:
        elapsed_str = "%.1fs" % elapsed
    elif elapsed < 3600:
        elapsed_str = "%.1fm %ds" % (elapsed / 60, elapsed % 60)
    else:
        elapsed_str = "%dh %dm" % (int(elapsed // 3600),
                                   int((elapsed % 3600) // 60))

    if cfg.verbose:
        print("временная сводка:")
        print("  начало: %s" % dt_start.strftime("%Y-%m-%d %H:%M:%S"))
        print("  конец:  %s" % dt_end.strftime("%Y-%m-%d %H:%M:%S"))
        print("  ✓ ПОЛНАЯ ДЛИТЕЛЬНОСТЬ: %s" % elapsed_str)
        print("результаты: %s/" % cfg.output_dir)

    return {
        "best_params": best_params,
        "final_result": final_result,
        "all_results": all_results,
        "output_dir": cfg.output_dir,
        "time_start": dt_start,
        "time_end": dt_end,
        "elapsed_seconds": elapsed,
        "elapsed_human": elapsed_str,
        "config": cfg,
    }


# ═══════════════════════════════════════════════════════════════════════
# RECONSTRUCTED: sweep_parameter / save_sweep_results
# (CALLED but NOT DEFINED in RH_Sweep_Pro.jl — obvious semantics; used by
#  sweep_top10_pro / sweep_combined_quick with signature
#  sweep_parameter(param, range=..., base_cfg=..., verbose=...).)
# ═══════════════════════════════════════════════════════════════════════

def sweep_parameter(param: str, values: Sequence[float], base_cfg: RHConfig,
                    verbose: bool = False):
    """Sweep one RHConfig field over ``values``: run(cfg) per value, collect
    result dicts {value, score, K_corr_zeta, brody_beta, chi2, r_mean},
    best by composite score.

    Returns (results, best_val, best_score, best_result) — matching the
    4-tuple unpacked at the call sites in RH_Sweep_Pro.jl (L6939/6942/7053).
    RECONSTRUCTION: the Julia file calls this function but never defines it;
    the semantics above are the obvious minimal implementation.
    """
    results: List[Dict[str, Any]] = []
    best_val = None
    best_score = -1.0
    best_result: Optional[MetricsResult] = None
    for v in values:
        cfg = copy.deepcopy(base_cfg)
        setattr(cfg, param, v)
        if verbose:
            print("  sweep %s=%s" % (param, v))
        out = run(cfg)
        fr = out["final_result"]
        d = {
            "value": v,
            "score": fr.composite_score,
            "K_corr_zeta": fr.K_corr_zeta,
            "brody_beta": fr.brody_beta,
            "chi2": fr.chi2_wigner,
            "r_mean": fr.r_mean,
        }
        results.append(d)
        if d["score"] > best_score:
            best_score = d["score"]
            best_val = v
            best_result = fr
    return results, best_val, best_score, best_result


def save_sweep_results(all_results: Dict[str, List[Dict[str, Any]]],
                       best_params: Dict[str, Dict[str, Any]],
                       output_dir: str) -> None:
    """Persist the sweep: <output_dir>/sweep_results.json with
    {"all_results": {param: [ {value, score, K_corr_zeta, brody_beta, chi2,
    r_mean}, ... ]}, "best_params": {param: {value, score}}}.
    RECONSTRUCTION of the undefined Julia function of the same name."""
    serial_best = {p: {"value": _jsonable(bp.get("value")),
                       "score": _jsonable(bp.get("score"))}
                   for p, bp in best_params.items()}
    data = {"all_results": all_results, "best_params": serial_best}
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "sweep_results.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False, allow_nan=False)
        f.write("\n")
    print("  Sweep результаты: %s" % path)


# ═══════════════════════════════════════════════════════════════════════
# SMOKE TEST
# ═══════════════════════════════════════════════════════════════════════

def smoke_test(verbose: bool = True):
    """Anchor case (L=16 → 256×256 eig, fast):
      cfg = default_config()
      H   = build_hamiltonian_with_config(16, 1/π, 2.0, 0.5, 0, cfg)
      eigs = central_eigs_sorted(H, window=0.3)
      metrics = compute_all_metrics_sp(eigs, get_zeta_zeros_safe(500), ...)
    Returns (eigs_head, eigs_tail, metrics)."""
    cfg = default_config()
    H = build_hamiltonian_with_config(16, 1.0 / math.pi, 2.0, 0.5, 0, cfg)
    eigs = central_eigs_sorted(H, window=0.3)
    eigs_list = [float(v) for v in eigs]
    zeta = get_zeta_zeros_safe(500)
    metrics = compute_all_metrics_sp(eigs_list, zeta, L=16, alpha=1.0 / math.pi,
                                     W=2.0, sigma=0.5, seed=0, eigs_per_seed=0)
    if verbose:
        print("smoke_test: n_eigs=%d, n_zeta=%d" % (len(eigs_list), len(zeta)))
        print("  eigs head: %s" % [repr(v) for v in eigs_list[:5]])
        print("  eigs tail: %s" % [repr(v) for v in eigs_list[-5:]])
        print("  r_mean=%s d_GUE=%s R2_rms_GUE=%s K_corr_GUE=%s K_corr_zeta=%s"
              % (_fmt(metrics.r_mean, 6), _fmt(metrics.d_GUE, 6),
                 _fmt(metrics.R2_rms_GUE, 6), _fmt(metrics.K_corr_GUE, 6),
                 _fmt(metrics.K_corr_zeta, 6)))
        print("  composite_score=%s tests_passed=%d/%d"
              % (_fmt(metrics.composite_score, 2), metrics.tests_passed,
                 metrics.tests_total))
    return eigs_list[:5], eigs_list[-5:], metrics
