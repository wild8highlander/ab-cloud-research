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
    """Compute the k-th Gram point: γ̃_k ≈ 2πk / W(k/e).

    Uses the asymptotic relation γ̃_k ≈ 2πk / W(k/e) where W is the
    Lambert W function (principal branch).
    """
    if k <= 0:
        return 0.0
    return 2.0 * math.pi * k / lambert_w(k / math.e)

# ---------------------------------------------------------------------------
# Zero loader
# ---------------------------------------------------------------------------

# Source registry: (source_name, filename, approx_zero_count)
_SOURCE_REGISTRY: List[Tuple[str, str, int]] = [
    ("50k",    "zeta_zeros_50000.txt",        13661),
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
        print(msg["progress"].format(N=N), end="\r")
        bN = compute_bN(zeros, N)
        bN_values.append(bN)
        delta = bN - prev_bN if prev_bN is not None else float("nan")
        delta_str = f"{delta:+.10f}" if not math.isnan(delta) else "—"
        print(f"{N:>10d}  {bN:>20.10f}  {delta_str:>20s}")
        prev_bN = bN

    # Check convergence: |b(N_max) − b(N_max/2)| should be small
    converged = False
    if len(bN_values) >= 2:
        converged = abs(bN_values[-1] - bN_values[-2]) < 0.01

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

    result = {"N_values": N_values[:len(bN_values)], "bN_values": bN_values, "converged": converged}
    return result

# ---------------------------------------------------------------------------
# Objection 2: GUE spacing
# ---------------------------------------------------------------------------

def gue_cdf(s: float) -> float:
    """Cumulative distribution function for GUE (Wigner-Dyson) spacing.

    P(s) = ∫₀ˢ (πt/2) exp(−πt²/4) dt = 1 − exp(−πs²/4).
    """
    return 1.0 - math.exp(-math.pi * s * s / 4.0)

def gue_pdf(s: float) -> float:
    """Probability density for GUE spacing: p(s) = (πs/2) exp(−πs²/4)."""
    return (math.pi * s / 2.0) * math.exp(-math.pi * s * s / 4.0)

def _ks_test(empirical: List[float], cdf_func, n_bootstrap: int = 0) -> Tuple[float, float]:
    """Kolmogorov-Smirnov test: empirical CDF vs theoretical CDF.

    Returns (D_statistic, p_value).
    Uses the asymptotic Kolmogorov distribution for p-value.
    """
    n = len(empirical)
    if n == 0:
        return 0.0, 1.0

    sorted_data = sorted(empirical)
    D_plus = 0.0
    D_minus = 0.0
    for i, x in enumerate(sorted_data):
        Fx = cdf_func(x)
        D_plus = max(D_plus, (i + 1) / n - Fx)
        D_minus = max(D_minus, Fx - i / n)
    D = max(D_plus, D_minus)

    # Asymptotic p-value via Kolmogorov distribution approximation
    # P(D > d) ≈ 2 Σ_{k=1}^{∞} (−1)^{k+1} exp(−2k²(nd)²)
    z = D * math.sqrt(n)
    p_value = 0.0
    for k in range(1, 100):
        term = 2.0 * ((-1) ** (k + 1)) * math.exp(-2.0 * k * k * z * z)
        p_value += term
        if abs(term) < 1e-15:
            break
    p_value = max(0.0, min(1.0, p_value))
    return D, p_value

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

    # KS test
    D, p_value = _ks_test(spacings, gue_cdf)
    print(f"  {msg['obj2_ks'].format(D=D, p=p_value)}")

    # Cramér-von Mises
    W2 = _cramer_von_mises_test(spacings, gue_cdf)
    print(f"  {msg['obj2_cvm'].format(W2=W2)}")

    # Verdict
    alpha = 0.05
    rejected = p_value < alpha
    verdict = msg["obj2_reject"] if rejected else msg["obj2_not_reject"]
    print(f"  {msg['obj2_result'].format(verdict=verdict)}")

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

    return {"D": D, "p_value": p_value, "W2": W2, "rejected": rejected}

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
# Full verification
# ---------------------------------------------------------------------------

def run_verification(
    zeros: Optional[List[float]] = None,
    data_dir: Optional[str] = None,
    count: int = 5000,
    source: str = "auto",
    objection: str = "all",
    lang: Optional[str] = None,
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

    if objection in ("1", "all"):
        results["obj1"] = verify_objection1(zeros, lang=lang)

    if objection in ("2", "all"):
        results["obj2"] = verify_objection2(zeros, lang=lang)

    if objection in ("3", "all"):
        results["obj3"] = verify_objection3(zeros, lang=lang)

    # Summary
    print(f"\n{'='*60}")
    print(msg["summary"])
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

    return results

# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="AB-Cloud Verification Suite")
    parser.add_argument("--zeros", type=int, default=5000, help="Number of zeros to load")
    parser.add_argument("--source", default="auto", help="Data source: auto,50k,500k,2M,highT,2M_gz,csv,zeros6")
    parser.add_argument("--objection", default="all", help="Which objection: 1,2,3,all")
    parser.add_argument("--lang", default=None, help="Language: en, ru")
    parser.add_argument("--data-dir", default=None, help="Path to data/ directory")
    args = parser.parse_args()

    lang = args.lang or _detect_language()
    run_verification(
        data_dir=args.data_dir,
        count=args.zeros,
        source=args.source,
        objection=args.objection,
        lang=lang,
    )
