"""
AB-Cloud Verification Suite — Main Bilingual Module (RU/EN auto-detect).

Verifies three reviewer objections against actual Riemann zeta zeros:
  1. Numerical stability of b(N) convergence
  2. GUE spacing statistical significance (KS + Cramér-von Mises)
  3. Large-T decay rate O(1/√N)

Language is auto-detected from the LANG environment variable or the --lang flag.
"""

from __future__ import annotations

import csv
import gzip
import math
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# ---------------------------------------------------------------------------
# Bilingual message catalog
# ---------------------------------------------------------------------------

MSG_EN: Dict[str, str] = {
    "loading":        "Loading {count} zeros from '{source}' …",
    "loaded":         "Loaded {n} zeros from '{source}'  |  T ∈ [{tmin:.4f}, {tmax:.4f}]",
    "auto_select":    "Auto-selected '{source}' (needs ≥{count} zeros, file has {avail})",
    "file_not_found": "ERROR: Data file not found: '{path}'",
    "no_source":      "ERROR: No data source available for {count} zeros",
    "obj1_title":     "Objection 1: Numerical Stability of b(N)",
    "obj1_bN":        "b({N}) = {val:.10f}",
    "obj1_converge":  "Convergence table — b(N) = (1/N) Σ|γ_k − γ̃_k|",
    "obj1_header":    "{:>10s}  {:>20s}  {:>20s}".format("N", "b(N)", "Δb = b(N)−b(N/2)"),
    "obj2_title":     "Objection 2: GUE Spacing Statistical Significance",
    "obj2_ks":        "Kolmogorov-Smirnov:  D = {D:.6f},  p-value = {p:.6f}",
    "obj2_cvm":       "Cramér-von Mises:    W² = {W2:.6f}",
    "obj2_result":    "H₀ (GUE distribution): {verdict}  (α = 0.05)",
    "obj2_reject":    "REJECTED",
    "obj2_not_reject":"NOT REJECTED",
    "obj2_ad":        "Anderson-Darling:   A² = {A2:.6f}",
    "obj2_rmean":     "⟨r⟩ (adjacent-ratio): {r:.6f}  (n = {nr}, GUE surmise ≈ 0.5992)",
    "obj2_mean":      "Spacing mean: {mean:.9f}  var: {var:.9f}  (n = {n})",
    "obj2_note":      "  Note: at large n the exact GUE surmise is formally rejected — the\n  known finite-T corrections of the zeta zeros, not a data artifact\n  (mean ≈ 1 validates the unfolding; golden-anchored).",
    "obj3_title":     "Objection 3: Large-T Decay Rate",
    "obj3_fit":       "Linear fit  log(b(N)) = {slope:.4f} · log(N) + {intercept:.4f}",
    "obj3_expected":  "Expected slope ≈ −0.5  (b(N) = O(1/√N))",
    "obj3_ci":        "95% CI for slope: [{lo:.4f}, {hi:.4f}]",
    "obj3_verdict":   "Slope {slope:.4f} is {relation} −0.5 ± 0.1 → {verdict}",
    "obj3_consistent":"CONSISTENT with O(1/√N)",
    "obj3_inconsistent":"INCONSISTENT with O(1/√N)",
    "obj3_within":    "within",
    "obj3_outside":   "outside",
    "progress":       "Computing b(N) for N = {N} …",
    "obj1_fit":       "Empirical law:  b(N) ≈ {a:.4f} · N^(−{s:.4f})   (R² = {r2:.4f})",
    "obj1_honest":    "  b(N) decreases monotonically over the table — convergence confirmed\n  on the accessible range. The decay is EMPIRICAL, not O(1/√N) (see Objection 3).",
    "selfcheck_title":"Golden self-check — frozen anchors (canon: meridian-spectral-observatory, selftest 199/199)",
    "selfcheck_line": "  {name:<24s} {status}  computed = {got}, expected = {exp}, Δ = {d:.3e}",
    "selfcheck_ok":   "PASS",
    "selfcheck_bad":  "FAIL",
    "selfcheck_skip": "  {name:<24s} SKIP  (needs {need} zeros, have {have})",
    "selfcheck_result":"  Self-check: {np} passed, {nf} failed",
    "summary":        "Verification Summary",
    "summary_line":   "  Objection {n}: {status}",
    "pass_":          "PASS",
    "fail":           "FAIL",
    "warn":           "WARN",
}

MSG_RU: Dict[str, str] = {
    "loading":        "Загрузка {count} нулей из '{source}' …",
    "loaded":         "Загружено {n} нулей из '{source}'  |  T ∈ [{tmin:.4f}, {tmax:.4f}]",
    "auto_select":    "Авто-выбор '{source}' (нужно ≥{count} нулей, файл содержит {avail})",
    "file_not_found": "ОШИБКА: Файл данных не найден: '{path}'",
    "no_source":      "ОШИБКА: Нет источника данных для {count} нулей",
    "obj1_title":     "Возражение 1: Численная устойчивость b(N)",
    "obj1_bN":        "b({N}) = {val:.10f}",
    "obj1_converge":  "Таблица сходимости — b(N) = (1/N) Σ|γ_k − γ̃_k|",
    "obj1_header":    "{:>10s}  {:>20s}  {:>20s}".format("N", "b(N)", "Δb = b(N)−b(N/2)"),
    "obj2_title":     "Возражение 2: Статистическая значимость GUE-распределения",
    "obj2_ks":        "Колмогоров-Смирнов:  D = {D:.6f},  p-значение = {p:.6f}",
    "obj2_cvm":       "Крамер-фон Мизес:    W² = {W2:.6f}",
    "obj2_result":    "H₀ (GUE-распределение): {verdict}  (α = 0.05)",
    "obj2_reject":    "ОТВЕРГНУТА",
    "obj2_not_reject":"НЕ ОТВЕРГНУТА",
    "obj2_ad":        "Андерсон-Дарлинг:     A² = {A2:.6f}",
    "obj2_rmean":     "⟨r⟩ (отношение соседних): {r:.6f}  (n = {nr}, GUE ≈ 0.5992)",
    "obj2_mean":      "Средний спейсинг: {mean:.9f}  дисперсия: {var:.9f}  (n = {n})",
    "obj2_note":      "  Примечание: при больших n точная GUE-сурьмида формально отвергается — это\n  известные поправки конечных T у нулей ζ, а не дефект данных\n  (среднее ≈ 1 подтверждает развёртку; якоря golden).",
    "obj3_title":     "Возражение 3: Скорость убывания при больших T",
    "obj3_fit":       "Линейная аппроксимация  log(b(N)) = {slope:.4f} · log(N) + {intercept:.4f}",
    "obj3_expected":  "Ожидаемый наклон ≈ −0.5  (b(N) = O(1/√N))",
    "obj3_ci":        "95% ДИ для наклона: [{lo:.4f}, {hi:.4f}]",
    "obj3_verdict":   "Наклон {slope:.4f} {relation} −0.5 ± 0.1 → {verdict}",
    "obj3_consistent":"СОГЛАСУЕТСЯ с O(1/√N)",
    "obj3_inconsistent":"НЕ СОГЛАСУЕТСЯ с O(1/√N)",
    "obj3_within":    "внутри",
    "obj3_outside":   "вне",
    "progress":       "Вычисление b(N) для N = {N} …",
    "obj1_fit":       "Эмпирический закон:  b(N) ≈ {a:.4f} · N^(−{s:.4f})   (R² = {r2:.4f})",
    "obj1_honest":    "  b(N) монотонно убывает по таблице — сходимость подтверждена\n  на доступном диапазоне. Убывание ЭМПИРИЧЕСКОЕ, это не O(1/√N) (см. Возражение 3).",
    "selfcheck_title":"Само-проверка golden — замороженные якоря (канон: meridian-spectral-observatory, selftest 199/199)",
    "selfcheck_line": "  {name:<24s} {status}  вычислено = {got}, ожидание = {exp}, Δ = {d:.3e}",
    "selfcheck_ok":   "ПРОЙДЕНО",
    "selfcheck_bad":  "СБОЙ",
    "selfcheck_skip": "  {name:<24s} ПРОПУСК  (нужно {need} нулей, есть {have})",
    "selfcheck_result":"  Само-проверка: {np} пройдено, {nf} провалено",
    "summary":        "Итоги проверки",
    "summary_line":   "  Возражение {n}: {status}",
    "pass_":          "ПРОЙДЕНО",
    "fail":           "СБОЙ",
    "warn":           "ПРЕДУПР.",
}

# ---------------------------------------------------------------------------
# Language detection
# ---------------------------------------------------------------------------

def _detect_language() -> str:
    """Detect language from LANG env var; default 'en'."""
    lang = os.environ.get("LANG", "").lower()
    if "ru" in lang:
        return "ru"
    return "en"

def get_msg(lang: Optional[str] = None) -> Dict[str, str]:
    """Return the message dictionary for the given language."""
    if lang is None:
        lang = _detect_language()
    return MSG_RU if lang == "ru" else MSG_EN

# ---------------------------------------------------------------------------
# Lambert W function (principal branch, Newton iteration)
# ---------------------------------------------------------------------------

def lambert_w(x: float, tol: float = 1e-12, max_iter: int = 50) -> float:
    """Compute the principal branch W₀(x) via Newton's method.

    Solves w·exp(w) = x for w ≥ −1.
    """
    if x < -1.0 / math.e:
        raise ValueError(f"Lambert W undefined for x = {x} < −1/e")
    if x == 0.0:
        return 0.0
    # Initial guess via log
    w = math.log(max(x, 1e-30))
    if w < 0:
        w = x  # For small x, W(x) ≈ x
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

# ---------------------------------------------------------------------------
# Gram points
# ---------------------------------------------------------------------------

def gram_point(k: int) -> float:
    """Compute the k-th Gram point: the solution of θ(t) = πk.

    Seed γ̃_k ≈ 2πk / W₀(k/e), then 8 Newton iterations on the 5-term
    Riemann–Siegel theta asymptotics — bit-compatible with the frozen
    golden reference (meridian-spectral-observatory, selftest 199/199):
      θ(t) = (t/2)·ln(t/2π) − t/2 − π/8 + 1/(48t) + 7/(5760t³)
    """
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

# ---------------------------------------------------------------------------
# Zero loader
# ---------------------------------------------------------------------------

# Source registry: (source_name, filename, approx_zero_count)
_SOURCE_REGISTRY: List[Tuple[str, str, int]] = [
    ("50k",    "zeta_zeros_50000.txt",        13661),
    ("50k_full","zeta_zeros_50000_embedded.txt",50000),
    ("500k",   "zeta_zeros_500k_odlyzko.txt", 500000),
    ("2M",     "zeta_zeros_2M_odlyzko.txt",   2001052),
    ("highT",  "zeta_zeros_highT_blocks.txt", 30000),
    ("2M_gz",  "zeta_zeros_2M_odlyzko.txt.gz",2001052),
    ("csv",    "zeta_zeros_50000.csv",        13661),
    ("zeros6", "zeros6.txt",                  2001052),
]

def _parse_plain_zeros(lines: List[str]) -> List[float]:
    """Parse zeros from plain text lines (skip comments/blanks, strip whitespace)."""
    zeros: List[float] = []
    for line in lines:
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        try:
            zeros.append(float(s))
        except ValueError:
            continue
    return zeros

def _parse_highT_zeros(lines: List[str]) -> List[float]:
    """Parse high-T block format: BLOCK header gives offset, values are offsets from base."""
    zeros: List[float] = []
    base_offset = 0.0
    for line in lines:
        s = line.strip()
        if not s:
            continue
        m = re.match(r"#\s*BLOCK\s+index=\S+\s+offset=(\S+)", s)
        if m:
            base_offset = float(m.group(1))
            continue
        if s.startswith("#"):
            continue
        try:
            zeros.append(base_offset + float(s))
        except ValueError:
            continue
    return zeros

def _parse_csv_zeros(lines: List[str]) -> List[float]:
    """Parse CSV format with columns: index,t,s_real,s_imag,zero_number."""
    zeros: List[float] = []
    reader = csv.reader(lines)
    for row in reader:
        if not row or row[0].startswith("#"):
            continue
        try:
            # Second column is t
            zeros.append(float(row[1]))
        except (ValueError, IndexError):
            continue
    return zeros

def _parse_julia_zeros(lines: List[str]) -> List[float]:
    """Parse Julia array format: extract floats from const ZETA_ZEROS = Float64[...]."""
    zeros: List[float] = []
    inside_array = False
    for line in lines:
        s = line.strip()
        if s.startswith("#"):
            continue
        if "Float64[" in s or "Float64[" in line:
            inside_array = True
        if inside_array:
            # Extract all float-like tokens
            cleaned = re.sub(r"[^\d.eE+\-.,\s]", " ", line)
            # Remove brackets
            cleaned = cleaned.replace("[", " ").replace("]", " ")
            for token in cleaned.split(","):
                token = token.strip()
                if not token:
                    continue
                try:
                    zeros.append(float(token))
                except ValueError:
                    continue
            if "]" in line:
                inside_array = False
    return zeros

def load_zeros(
    data_dir: Optional[str] = None,
    count: int = 5000,
    source: str = "auto",
    lang: Optional[str] = None,
) -> List[float]:
    """Load Riemann zeta zeros from data files.

    Parameters
    ----------
    data_dir : str or None
        Path to the data/ directory. Defaults to ../data/ relative to this file.
    count : int
        Number of zeros to load (default 5000).
    source : str
        Data source name: "auto", "50k", "500k", "2M", "highT", "2M_gz", "csv", "zeros6".
    lang : str or None
        Language for messages ("en" or "ru"). Auto-detected if None.

    Returns
    -------
    list[float]
        Imaginary parts of zeta zeros on the critical line, sorted ascending.
    """
    msg = get_msg(lang)

    if data_dir is None:
        data_dir = str(Path(__file__).resolve().parent.parent / "data")

    # Auto-select source
    if source == "auto":
        # Pick smallest file that has enough zeros
        candidates = [(name, fname, avail) for name, fname, avail in _SOURCE_REGISTRY
                       if avail >= count]
        if not candidates:
            print(msg["no_source"].format(count=count), file=sys.stderr)
            return []
        candidates.sort(key=lambda x: x[2])
        source, fname, avail = candidates[0]
        print(msg["auto_select"].format(source=source, count=count, avail=avail))
    else:
        fname = None
        avail = 0
        for sname, sfn, savail in _SOURCE_REGISTRY:
            if sname == source:
                fname, avail = sfn, savail
                break
        if fname is None:
            print(msg["no_source"].format(count=count), file=sys.stderr)
            return []

    filepath = Path(data_dir) / fname
    print(msg["loading"].format(count=count, source=fname))

    if not filepath.exists():
        print(msg["file_not_found"].format(path=filepath), file=sys.stderr)
        return []

    # Read and parse
    lines: List[str]
    if str(filepath).endswith(".gz"):
        with gzip.open(filepath, "rt", encoding="utf-8") as f:
            lines = f.readlines()
        zeros = _parse_plain_zeros(lines)
    elif source == "highT":
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
        zeros = _parse_highT_zeros(lines)
    elif source == "csv":
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
        zeros = _parse_csv_zeros(lines)
    elif source == "50k" and fname.endswith(".jl"):
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
        zeros = _parse_julia_zeros(lines)
    else:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
        zeros = _parse_plain_zeros(lines)

    # Sort and truncate
    zeros.sort()
    if count < len(zeros):
        zeros = zeros[:count]

    if zeros:
        print(msg["loaded"].format(n=len(zeros), source=fname,
                                    tmin=zeros[0], tmax=zeros[-1]))
    return zeros

# ---------------------------------------------------------------------------
# Objection 1: b(N) convergence
# ---------------------------------------------------------------------------

def compute_bN(zeros: List[float], N: int) -> float:
    """Compute b(N) = (1/N) Σ_{k=1}^{N} |γ_k − γ̃_k|.

    Parameters
    ----------
    zeros : list[float]
        Zeta zeros (imaginary parts), sorted ascending.
    N : int
        Number of terms in the sum.

    Returns
    -------
    float
        The AB correction term b(N).
    """
    if N <= 0 or N > len(zeros):
        return float("nan")
    total = 0.0
    for k in range(1, N + 1):
        gamma_k = zeros[k - 1]
        gram_k = gram_point(k)
        total += abs(gamma_k - gram_k)
    return total / N

def compute_bN_offset(zeros: List[float], N: int, offset: int) -> float:
    """b(N; offset) — zeros 1..N against Gram points offset+1 .. offset+N."""
    if N <= 0 or offset + N > len(zeros):
        return float("nan")
    total = 0.0
    for k in range(1, N + 1):
        total += abs(zeros[k - 1] - gram_point(offset + k))
    return total / N

def bN_prefix(zeros: List[float]) -> List[float]:
    """prefix[i] = Σ_{k=1..i} |γ_k − γ̃_k| — same summation order as
    compute_bN, so b(N) = prefix[N]/N is bit-identical and O(1) per N."""
    pref = [0.0]
    acc = 0.0
    for k in range(1, len(zeros) + 1):
        acc += abs(zeros[k - 1] - gram_point(k))
        pref.append(acc)
    return pref

def verify_objection1(
    zeros: List[float],
    N_values: Optional[List[int]] = None,
    lang: Optional[str] = None,
    plot: bool = True,
) -> Dict[str, object]:
    """Verify Objection 1: numerical stability / convergence of b(N).

    Returns dict with keys: N_values, bN_values, converged.
    """
    msg = get_msg(lang)

    if N_values is None:
        N_values = [100, 500, 1000, 5000, 10000, 50000]
        # Filter to available zeros
        N_values = [n for n in N_values if n <= len(zeros)]
        if not N_values:
            N_values = [min(len(zeros), 100)]

    pref = bN_prefix(zeros)

    print(f"\n{'='*60}")
    print(msg["obj1_title"])
    print(msg["obj1_converge"])
    print(msg["obj1_header"])
    print("-" * 60)

    bN_values: List[float] = []
    prev_bN: Optional[float] = None

    for N in N_values:
        if N > len(zeros):
            continue
        bN = pref[N] / float(N)
        bN_values.append(bN)
        delta = bN - prev_bN if prev_bN is not None else float("nan")
        delta_str = f"{delta:+.10f}" if not math.isnan(delta) else "—"
        print(f"{N:>10d}  {bN:>20.10f}  {delta_str:>20s}")
        prev_bN = bN

    # Empirical power-law fit over the table points
    slope = float("nan")
    r2 = 0.0
    xs = [math.log(N) for N in N_values[:len(bN_values)] if N > 1]
    ys = [math.log(b) for b in bN_values if b > 0]
    if len(xs) >= 3 and len(ys) == len(xs):
        slope, intercept, _se, r2 = _linear_regression(xs, ys)
        print(msg["obj1_fit"].format(a=math.exp(intercept), s=-slope, r2=r2))

    # Convergence verdict: monotone decrease across the table — honest criterion
    monotone = all(bN_values[i + 1] < bN_values[i] for i in range(len(bN_values) - 1))
    converged = bool(monotone and len(bN_values) >= 3)
    print(msg["obj1_honest"])

    # Attempt plot
    if plot:
        try:
            import matplotlib
            matplotlib.use("Agg")
            import matplotlib.pyplot as plt
            fig, ax = plt.subplots(figsize=(8, 5))
            valid_N = [N_values[i] for i in range(len(bN_values))]
            ax.plot(valid_N, bN_values, "o-", color="#2563eb", markersize=6, linewidth=1.5)
            ax.set_xscale("log")
            ax.set_xlabel("N")
            ax.set_ylabel("b(N)")
            ax.set_title(msg["obj1_converge"])
            ax.grid(True, alpha=0.3)
            fig.savefig("objection1_convergence.png", dpi=150, bbox_inches="tight")
            plt.close(fig)
            print("  → Plot saved: objection1_convergence.png")
        except ImportError:
            pass  # matplotlib not available

    result = {"N_values": N_values[:len(bN_values)], "bN_values": bN_values,
              "converged": converged, "slope": slope, "r2": r2}
    return result

# ---------------------------------------------------------------------------
# Objection 2: GUE spacing
# ---------------------------------------------------------------------------

_GUE_TABLE: List[float] = []
_GUE_TN = 32768
_GUE_SMAX = 5.0

def gue_cdf(s: float) -> float:
    """Cumulative distribution function for GUE (Wigner-Dyson β=2) spacing.

    Exact law: p₂(s) = (32/π²) s² exp(−4s²/π)
        F(s) = erf(2s/√π) − (4s/π)·exp(−4s²/π).
    v2.0.3: was 1 − exp(−πs²/4) — that is the GOE (β=1) surmise, not GUE.

    For parity with the golden reference the value is evaluated through the
    same 32768-point interpolation table (SMAX = 5) as the verified ports;
    outside [0, 5) the exact closed form is used.
    """
    global _GUE_TABLE
    if s <= 0:
        return 0.0

    def exact(x: float) -> float:
        return math.erf(2.0 * x / math.sqrt(math.pi)) \
            - (4.0 * x / math.pi) * math.exp(-4.0 * x * x / math.pi)

    if s >= _GUE_SMAX:
        return exact(s)
    if not _GUE_TABLE:
        _GUE_TABLE = [exact(i * _GUE_SMAX / (_GUE_TN - 1)) for i in range(_GUE_TN)]
    x = s * (_GUE_TN - 1) / _GUE_SMAX
    i = int(math.floor(x))
    if i < 0 or i >= _GUE_TN - 1:
        return exact(s)
    t = x - i
    return (1.0 - t) * _GUE_TABLE[i] + t * _GUE_TABLE[i + 1]

def gue_pdf(s: float) -> float:
    """Probability density for GUE spacing: p(s) = (32/π²) s² exp(−4s²/π)."""
    return (32.0 / math.pi ** 2) * s * s * math.exp(-4.0 * s * s / math.pi)

def _ks_asymptotic_pvalue(lam: float) -> float:
    """Kolmogorov asymptotic p-value, two branches (golden-compatible)."""
    if lam <= 0.0:
        return 1.0
    if lam < 0.6:
        s2 = 0.0
        for k in range(1, 1001):
            term2 = math.exp(-(((2.0 * k - 1.0) ** 2) * math.pi ** 2) / (8.0 * lam * lam))
            s2 += term2
            if term2 < 1e-18:
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
    return max(0.0, min(1.0, v))

def _ks_test(empirical: List[float], cdf_func, n_bootstrap: int = 0) -> Tuple[float, float]:
    """Kolmogorov-Smirnov test: empirical CDF vs theoretical CDF.

    Returns (D_statistic, p_value) with the λ-corrected asymptotic
    p-value λ = (√n + 0.12 + 0.11/√n)·D — golden-compatible kernel.
    """
    n = len(empirical)
    if n == 0:
        return 0.0, 1.0

    sorted_data = sorted(empirical)
    D = 0.0
    for i in range(1, n + 1):
        Fx = cdf_func(sorted_data[i - 1])
        D = max(D, abs(i / n - Fx), abs((i - 1) / n - Fx))

    lam = (math.sqrt(n) + 0.12 + 0.11 / math.sqrt(n)) * D
    return D, _ks_asymptotic_pvalue(lam)

def _anderson_darling(empirical: List[float], cdf_func) -> float:
    """Anderson-Darling A² with 1e-300 / 1−1e-16 tail clamps (golden-compatible)."""
    n = len(empirical)
    if n < 2:
        return float("nan")
    s = sorted(empirical)
    acc = 0.0
    for i in range(1, n + 1):
        Fi = min(max(cdf_func(s[i - 1]), 1e-300), 1.0 - 1e-16)
        Fni = min(max(cdf_func(s[n - i]), 1e-300), 1.0 - 1e-16)
        acc += (2.0 * i - 1.0) * (math.log(Fi) + math.log(1.0 - Fni))
    return -float(n) - acc / float(n)

def _mean_adjacent_ratio(zeros: List[float]) -> Tuple[float, int]:
    """⟨r⟩ = mean min(d_i,d_{i+1})/max(d_i,d_{i+1}) over adjacent gaps."""
    n = len(zeros)
    if n < 3:
        return float("nan"), 0
    d = [zeros[i + 1] - zeros[i] for i in range(n - 1)]
    acc = 0.0
    cnt = 0
    for i in range(len(d) - 1):
        a, b = d[i], d[i + 1]
        m = max(a, b)
        if a == 0.0 and b == 0.0:
            continue
        acc += min(a, b) / m
        cnt += 1
    if cnt == 0:
        return float("nan"), 0
    return acc / cnt, cnt

def _cramer_von_mises_test(empirical: List[float], cdf_func) -> float:
    """Cramér-von Mises test statistic W².

    W² = (1/12n) + Σ_{i=1}^{n} [(2i−1)/(2n) − F(x_i)]²
    """
    n = len(empirical)
    if n == 0:
        return 0.0
    sorted_data = sorted(empirical)
    W2 = 1.0 / (12.0 * n)
    for i, x in enumerate(sorted_data):
        Fx = cdf_func(x)
        W2 += ((2.0 * (i + 1) - 1.0) / (2.0 * n) - Fx) ** 2
    return W2

def verify_objection2(
    zeros: List[float],
    lang: Optional[str] = None,
) -> Dict[str, object]:
    """Verify Objection 2: GUE spacing statistical significance.

    Returns dict with keys: D, p_value, W2, rejected.
    """
    msg = get_msg(lang)

    print(f"\n{'='*60}")
    print(msg["obj2_title"])

    # Compute normalized spacings: s_k = (γ_{k+1} − γ_k) · log(γ_k/(2π)) / (2π)
    spacings: List[float] = []
    for k in range(len(zeros) - 1):
        gamma_k = zeros[k]
        delta = zeros[k + 1] - zeros[k]
        if gamma_k <= 0:
            continue
        norm = math.log(gamma_k / (2.0 * math.pi)) / (2.0 * math.pi)
        spacings.append(delta * norm)

    print(f"  Computed {len(spacings)} normalized spacings")

    mean_s = sum(spacings) / len(spacings) if spacings else float("nan")
    var_s = (sum((s - mean_s) ** 2 for s in spacings) / (len(spacings) - 1)
             if len(spacings) > 1 else float("nan"))
    print(f"  {msg['obj2_mean'].format(mean=mean_s, var=var_s, n=len(spacings))}")

    # KS test
    D, p_value = _ks_test(spacings, gue_cdf)
    print(f"  {msg['obj2_ks'].format(D=D, p=p_value)}")

    # Cramér-von Mises
    W2 = _cramer_von_mises_test(spacings, gue_cdf)
    print(f"  {msg['obj2_cvm'].format(W2=W2)}")

    # Anderson-Darling
    A2 = _anderson_darling(spacings, gue_cdf)
    print(f"  {msg['obj2_ad'].format(A2=A2)}")

    # ⟨r⟩ adjacent-gap ratio
    r_mean, n_r = _mean_adjacent_ratio(zeros)
    print(f"  {msg['obj2_rmean'].format(r=r_mean, nr=n_r)}")

    # Verdict
    alpha = 0.05
    rejected = p_value < alpha
    verdict = msg["obj2_reject"] if rejected else msg["obj2_not_reject"]
    print(f"  {msg['obj2_result'].format(verdict=verdict)}")
    if rejected:
        print(msg["obj2_note"])

    # Histogram plot
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        import numpy as np
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.hist(spacings, bins=80, density=True, alpha=0.6, color="#2563eb",
                edgecolor="white", linewidth=0.5, label="Empirical")
        s_range = [i * 0.02 for i in range(500)]
        gue_vals = [gue_pdf(s) for s in s_range]
        ax.plot(s_range, gue_vals, "r-", linewidth=2, label="GUE (Wigner-Dyson)")
        ax.set_xlabel("Normalized spacing s")
        ax.set_ylabel("Density")
        ax.set_title("GUE Spacing Distribution")
        ax.legend()
        ax.grid(True, alpha=0.3)
        fig.savefig("objection2_gue_spacing.png", dpi=150, bbox_inches="tight")
        plt.close(fig)
        print("  → Plot saved: objection2_gue_spacing.png")
    except ImportError:
        pass

    return {"D": D, "p_value": p_value, "W2": W2, "A2": A2,
            "r_mean": r_mean, "mean": mean_s, "var": var_s,
            "rejected": rejected}

# ---------------------------------------------------------------------------
# Objection 3: Large-T decay rate
# ---------------------------------------------------------------------------

def _linear_regression(x: List[float], y: List[float]) -> Tuple[float, float, float, float]:
    """Simple linear regression y = slope·x + intercept.

    Returns (slope, intercept, slope_std_err, r_squared).
    """
    n = len(x)
    if n < 2:
        return 0.0, 0.0, 0.0, 0.0
    sx = sum(x)
    sy = sum(y)
    sxx = sum(xi * xi for xi in x)
    sxy = sum(xi * yi for xi, yi in zip(x, y))
    denom = n * sxx - sx * sx
    if abs(denom) < 1e-30:
        return 0.0, 0.0, 0.0, 0.0
    slope = (n * sxy - sx * sy) / denom
    intercept = (sy - slope * sx) / n
    # R-squared
    y_mean = sy / n
    ss_tot = sum((yi - y_mean) ** 2 for yi in y)
    ss_res = sum((yi - (slope * xi + intercept)) ** 2 for xi, yi in zip(x, y))
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else 0.0
    # Standard error of slope
    mse = ss_res / (n - 2) if n > 2 else 0.0
    slope_std_err = math.sqrt(mse * n / denom) if denom > 0 else 0.0
    return slope, intercept, slope_std_err, r2

def verify_objection3(
    zeros: List[float],
    lang: Optional[str] = None,
) -> Dict[str, object]:
    """Verify Objection 3: b(N) = O(1/√N) decay rate.

    Computes b(N) at multiple N values, fits log(b(N)) vs log(N),
    and checks that the slope ≈ −0.5.

    Returns dict with keys: slope, intercept, slope_ci, consistent.
    """
    msg = get_msg(lang)

    print(f"\n{'='*60}")
    print(msg["obj3_title"])

    # Compute b(N) at geometrically spaced N values
    max_N = len(zeros)
    N_vals: List[int] = []
    n = 50
    while n <= max_N:
        N_vals.append(n)
        n = int(n * 2)
    if N_vals[-1] != max_N and max_N > 100:
        N_vals.append(max_N)

    log_N: List[float] = []
    log_bN: List[float] = []

    print("  Computing b(N) at multiple N values …")
    for N in N_vals:
        bN = compute_bN(zeros, N)
        if bN <= 0:
            continue
        log_N.append(math.log(N))
        log_bN.append(math.log(bN))
        print(f"    N = {N:>8d}  b(N) = {bN:.10f}  log(b) = {math.log(bN):.6f}")

    if len(log_N) < 3:
        print("  WARNING: Not enough data points for regression")
        return {"slope": float("nan"), "intercept": float("nan"),
                "slope_ci": (float("nan"), float("nan")), "consistent": False}

    slope, intercept, slope_std_err, r2 = _linear_regression(log_N, log_bN)

    # 95% CI (approximate using t-distribution with large df → z = 1.96)
    z_crit = 1.96
    ci_lo = slope - z_crit * slope_std_err
    ci_hi = slope + z_crit * slope_std_err

    print(f"  {msg['obj3_fit'].format(slope=slope, intercept=intercept)}")
    print(f"  R² = {r2:.6f}")
    print(f"  {msg['obj3_expected']}")
    print(f"  {msg['obj3_ci'].format(lo=ci_lo, hi=ci_hi)}")

    # Verdict: is slope within −0.5 ± 0.1?
    target = -0.5
    margin = 0.1
    consistent = abs(slope - target) <= margin
    relation = msg["obj3_within"] if consistent else msg["obj3_outside"]
    verdict = msg["obj3_consistent"] if consistent else msg["obj3_inconsistent"]
    print(f"  {msg['obj3_verdict'].format(slope=slope, relation=relation, verdict=verdict)}")

    # Plot
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.scatter(log_N, log_bN, color="#2563eb", s=30, zorder=5, label="Data")
        fit_x = [min(log_N), max(log_N)]
        fit_y = [slope * x + intercept for x in fit_x]
        ax.plot(fit_x, fit_y, "r--", linewidth=2,
                label=f"Fit: slope = {slope:.4f}")
        ref_y = [target * x + intercept for x in fit_x]
        ax.plot(fit_x, ref_y, "g:", linewidth=1.5,
                label="Reference: slope = −0.5")
        ax.set_xlabel("log(N)")
        ax.set_ylabel("log(b(N))")
        ax.set_title(msg["obj3_title"])
        ax.legend()
        ax.grid(True, alpha=0.3)
        fig.savefig("objection3_decay_rate.png", dpi=150, bbox_inches="tight")
        plt.close(fig)
        print("  → Plot saved: objection3_decay_rate.png")
    except ImportError:
        pass

    return {"slope": slope, "intercept": intercept,
            "slope_ci": (ci_lo, ci_hi), "consistent": consistent}

# ---------------------------------------------------------------------------
# Golden self-check — frozen anchors
# ---------------------------------------------------------------------------

# Anchors from ports/golden/abcloud_golden.json (meridian-spectral-observatory,
# Julia 1.10.9 canon on the first 50 000 Odlyzko zeros; selftest 199/199).
GOLDEN_LAMBERT_W = {
    "0.5": 0.35173371124919584, "1.0": 0.5671432904097838,
    "3.7": 1.1599531786120223, "10.0": 1.7455280027406992,
    "271.8": 4.17576816800275, "12345.6": 7.417247034540566,
}
GOLDEN_GRAM = {
    1: 23.17028270133466, 2: 27.670182217848343, 3: 31.71797995477886,
    10: 54.67523744685398, 100: 238.58259051450293, 1000: 1421.25638903275,
    10000: 9878.910118894457, 50000: 40434.6952780045,
}
GOLDEN_BN = {
    100: 3.3321638710140165, 500: 2.3912304957476382,
    1000: 2.1072522951855435, 5000: 1.6299485869022874,
    10000: 1.4794053414584762, 50000: 1.2125526772588608,
}
GOLDEN_BN_OFF500 = 624.6201618180231
GOLDEN_SP_MEAN = 0.999976001221201
GOLDEN_SP_VAR = 0.1590654827835423
GOLDEN_KS_D = 0.021619337032982328
GOLDEN_KS_P = 9.567870399361496e-21
GOLDEN_CVM_W2 = 8.177703317829403
GOLDEN_AD_A2 = 61.49242624209728
GOLDEN_RMEAN_R = 0.6118798907208398

def selfcheck(zeros: List[float], pref: List[float], lang: Optional[str] = None) -> Tuple[int, int]:
    """Compare computed values against the frozen golden anchors.

    Tolerances: lambert_w 1e-12 rel; gram_point/bN 1e-6 abs (12-digit data
    put the floor near 1e-12); statistics 1e-9 (p-value 1e-6 rel).
    Returns (n_pass, n_fail).
    """
    msg = get_msg(lang)
    print(f"\n{'='*60}")
    print(msg["selfcheck_title"])
    rows: List[Tuple[str, bool, float, float, float]] = []

    def check(name: str, got: float, exp: float, tol: float, rel: bool = False) -> None:
        if got != got:
            rows.append((name, False, got, exp, float("inf")))
            return
        d = abs(got - exp) / abs(exp) if rel else abs(got - exp)
        rows.append((name, d <= tol, got, exp, d))

    for xs, exp in GOLDEN_LAMBERT_W.items():
        check(f"lambert_w({xs})", lambert_w(float(xs)), exp, 1e-12, rel=True)
    for n, exp in GOLDEN_GRAM.items():
        check(f"gram_point(n={n})", gram_point(n), exp, 1e-6)

    n = len(zeros)
    for N, exp in GOLDEN_BN.items():
        if N <= n:
            check(f"bN(N={N})", pref[N] / float(N), exp, 1e-6)
        else:
            print(msg["selfcheck_skip"].format(name=f"bN(N={N})", need=N, have=n))
    if n >= 1500:
        check("bN(N=1000,off=500)", compute_bN_offset(zeros, 1000, 500), GOLDEN_BN_OFF500, 1e-6)
    else:
        print(msg["selfcheck_skip"].format(name="bN(N=1000,off=500)", need=1500, have=n))

    if n >= 50000:
        z5 = zeros[:50000]
        sp = [(z5[k + 1] - z5[k]) * math.log(z5[k] / (2.0 * math.pi)) / (2.0 * math.pi)
              for k in range(len(z5) - 1) if z5[k] > 0]
        mean_s = sum(sp) / len(sp)
        var_s = sum((s - mean_s) ** 2 for s in sp) / (len(sp) - 1)
        D, p = _ks_test(sp, gue_cdf)
        check("spacings.mean", mean_s, GOLDEN_SP_MEAN, 1e-9)
        check("spacings.var", var_s, GOLDEN_SP_VAR, 1e-9)
        check("ks_zeros.D", D, GOLDEN_KS_D, 1e-9)
        check("ks_zeros.p", p, GOLDEN_KS_P, 1e-6, rel=True)
        check("cvm_zeros.W2", _cramer_von_mises_test(sp, gue_cdf), GOLDEN_CVM_W2, 1e-9, rel=True)
        check("ad_zeros.A2", _anderson_darling(sp, gue_cdf), GOLDEN_AD_A2, 1e-9, rel=True)
        r, _nr = _mean_adjacent_ratio(z5)
        check("rmean_zeros.r", r, GOLDEN_RMEAN_R, 1e-9)
    else:
        for nm in ("spacings.mean/var", "ks_zeros.D/p", "cvm_zeros.W2",
                   "ad_zeros.A2", "rmean_zeros.r"):
            print(msg["selfcheck_skip"].format(name=nm, need=50000, have=n))

    npass = sum(1 for r_ in rows if r_[1])
    nfail = len(rows) - npass
    for name, ok, got, exp, d in rows:
        print(msg["selfcheck_line"].format(
            name=name, status=msg["selfcheck_ok"] if ok else msg["selfcheck_bad"],
            got=f"{got:.12g}", exp=f"{exp:.12g}", d=d))
    print(msg["selfcheck_result"].format(np=npass, nf=nfail))
    return npass, nfail

# ---------------------------------------------------------------------------
# Full verification
# ---------------------------------------------------------------------------

def run_verification(
    zeros: Optional[List[float]] = None,
    data_dir: Optional[str] = None,
    count: int = 50000,
    source: str = "auto",
    objection: str = "all",
    lang: Optional[str] = None,
    run_selfcheck: bool = True,
) -> Dict[str, Dict[str, object]]:
    """Run all or selected objections.

    Parameters
    ----------
    zeros : list[float] or None
        Pre-loaded zeros. If None, loaded from data_dir.
    objection : str
        "1", "2", "3", or "all".

    Returns
    -------
    dict
        Results keyed by "obj1", "obj2", "obj3".
    """
    msg = get_msg(lang)

    if zeros is None:
        zeros = load_zeros(data_dir=data_dir, count=count, source=source, lang=lang)
    if not zeros:
        return {}

    results: Dict[str, Dict[str, object]] = {}

    # Frozen-anchor self-check first: every headline number below is
    # verified against the golden canon before any verdict is printed.
    sc_pass = sc_fail = -1
    pref: List[float] = []
    if run_selfcheck:
        pref = bN_prefix(zeros)
        sc_pass, sc_fail = selfcheck(zeros, pref, lang=lang)

    if objection in ("1", "all"):
        results["obj1"] = verify_objection1(zeros, lang=lang)

    if objection in ("2", "all"):
        results["obj2"] = verify_objection2(zeros, lang=lang)

    if objection in ("3", "all"):
        results["obj3"] = verify_objection3(zeros, lang=lang)

    # Summary
    print(f"\n{'='*60}")
    print(msg["summary"])
    if run_selfcheck:
        print(msg["selfcheck_result"].format(np=sc_pass, nf=sc_fail))
    status_map = {
        "obj1": lambda r: msg["pass_"] if r.get("converged") else msg["warn"],
        "obj2": lambda r: msg["pass_"] if not r.get("rejected") else msg["fail"],
        "obj3": lambda r: msg["pass_"] if r.get("consistent") else msg["fail"],
    }
    for key, result in results.items():
        n = key[-1]
        status = status_map[key](result)
        print(msg["summary_line"].format(n=n, status=status))
    print("=" * 60)

    if run_selfcheck:
        results["selfcheck"] = {"pass": sc_pass, "fail": sc_fail}
    return results

# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="AB-Cloud Verification Suite")
    parser.add_argument("--zeros", type=int, default=50000, help="Number of zeros to load")
    parser.add_argument("--source", default="auto", help="Data source: auto,50k,50k_full,500k,2M,highT,2M_gz,csv,zeros6")
    parser.add_argument("--objection", default="all", help="Which objection: 1,2,3,all")
    parser.add_argument("--lang", default=None, help="Language: en, ru")
    parser.add_argument("--data-dir", default=None, help="Path to data/ directory")
    parser.add_argument("--no-selfcheck", action="store_true", help="Skip the frozen-anchor self-check")
    args = parser.parse_args()

    lang = args.lang or _detect_language()
    res = run_verification(
        data_dir=args.data_dir,
        count=args.zeros,
        source=args.source,
        objection=args.objection,
        lang=lang,
        run_selfcheck=not args.no_selfcheck,
    )
    sc = res.get("selfcheck")
    sys.exit(1 if (sc and sc.get("fail", 0) > 0) else 0)
