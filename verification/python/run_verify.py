#!/usr/bin/env python3
"""
run_verify.py — Standalone CLI runner for AB-Cloud Verification Suite.

Self-contained single file: includes Lambert W approximation, GUE PDF/CDF,
KS test, Cramér-von Mises test, zero loader, and all three objections.

Usage:
    python run_verify.py --zeros 200000 --source 500k --objection all
    python run_verify.py --zeros 5000 --source 50k --objection 1 --lang ru
    python run_verify.py --data-dir ../data --zeros 1000 --objection 2
"""

from __future__ import annotations

import argparse
import csv
import gzip
import math
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# ═══════════════════════════════════════════════════════════════════════════
# Bilingual messages
# ═══════════════════════════════════════════════════════════════════════════

MSG_EN: Dict[str, str] = {
    "loading":        "Loading {count} zeros from '{source}' ...",
    "loaded":         "Loaded {n} zeros | T in [{tmin:.4f}, {tmax:.4f}]",
    "auto_select":    "Auto-selected '{source}' (needs >= {count} zeros, file has {avail})",
    "file_not_found": "ERROR: Data file not found: '{path}'",
    "no_source":      "ERROR: No data source available for {count} zeros",
    "obj1_title":     "Objection 1: Numerical Stability of b(N)",
    "obj1_converge":  "Convergence table: b(N) = (1/N) Sum|gamma_k - gram_k|",
    "obj1_header":    "         N                b(N)          delta_b = b(N)-b(N/2)",
    "obj2_title":     "Objection 2: GUE Spacing Statistical Significance",
    "obj2_ks":        "Kolmogorov-Smirnov: D = {D:.6f}, p-value = {p:.6f}",
    "obj2_cvm":       "Cramer-von Mises:   W2 = {W2:.6f}",
    "obj2_result":    "H0 (GUE distribution): {verdict} (alpha = 0.05)",
    "obj2_reject":    "REJECTED",
    "obj2_keep":      "NOT REJECTED",
    "obj3_title":     "Objection 3: Large-T Decay Rate",
    "obj3_fit":       "Fit: log(b(N)) = {slope:.4f} * log(N) + {intercept:.4f}",
    "obj3_expected":  "Expected slope ~ -0.5 (b(N) = O(1/sqrt(N)))",
    "obj3_ci":        "95% CI for slope: [{lo:.4f}, {hi:.4f}]",
    "obj3_verdict":   "Slope {slope:.4f} is {relation} -0.5 +/- 0.1 -> {verdict}",
    "obj3_ok":        "CONSISTENT with O(1/sqrt(N))",
    "obj3_bad":       "INCONSISTENT with O(1/sqrt(N))",
    "obj3_in":        "within",
    "obj3_out":       "outside",
    "progress":       "Computing b(N) for N = {N} ...",
    "summary":        "Verification Summary",
    "summary_line":   "  Objection {n}: {status}",
    "pass_":          "PASS",
    "fail":           "FAIL",
    "warn":           "WARN",
}

MSG_RU: Dict[str, str] = {
    "loading":        "Загрузка {count} нулей из '{source}' ...",
    "loaded":         "Загружено {n} нулей | T в [{tmin:.4f}, {tmax:.4f}]",
    "auto_select":    "Авто-выбор '{source}' (нужно >= {count} нулей, файл имеет {avail})",
    "file_not_found": "ОШИБКА: Файл данных не найден: '{path}'",
    "no_source":      "ОШИБКА: Нет источника данных для {count} нулей",
    "obj1_title":     "Возражение 1: Численная устойчивость b(N)",
    "obj1_converge":  "Таблица сходимости: b(N) = (1/N) Sum|gamma_k - gram_k|",
    "obj1_header":    "         N                b(N)          delta_b = b(N)-b(N/2)",
    "obj2_title":     "Возражение 2: Статистическая значимость GUE-распределения",
    "obj2_ks":        "Колмогоров-Смирнов: D = {D:.6f}, p-значение = {p:.6f}",
    "obj2_cvm":       "Крамер-фон Мизес:   W2 = {W2:.6f}",
    "obj2_result":    "H0 (GUE-распределение): {verdict} (alpha = 0.05)",
    "obj2_reject":    "ОТВЕРГНУТА",
    "obj2_keep":      "НЕ ОТВЕРГНУТА",
    "obj3_title":     "Возражение 3: Скорость убывания при больших T",
    "obj3_fit":       "Аппрокс.: log(b(N)) = {slope:.4f} * log(N) + {intercept:.4f}",
    "obj3_expected":  "Ожидаемый наклон ~ -0.5 (b(N) = O(1/sqrt(N)))",
    "obj3_ci":        "95% ДИ для наклона: [{lo:.4f}, {hi:.4f}]",
    "obj3_verdict":   "Наклон {slope:.4f} {relation} -0.5 +/- 0.1 -> {verdict}",
    "obj3_ok":        "СОГЛАСУЕТСЯ с O(1/sqrt(N))",
    "obj3_bad":       "НЕ СОГЛАСУЕТСЯ с O(1/sqrt(N))",
    "obj3_in":        "внутри",
    "obj3_out":       "вне",
    "progress":       "Вычисление b(N) для N = {N} ...",
    "summary":        "Итоги проверки",
    "summary_line":   "  Возражение {n}: {status}",
    "pass_":          "ПРОЙДЕНО",
    "fail":           "СБОЙ",
    "warn":           "ПРЕДУПР.",
}

# ═══════════════════════════════════════════════════════════════════════════
# Math utilities (self-contained, no external deps)
# ═══════════════════════════════════════════════════════════════════════════

def lambert_w(x: float, tol: float = 1e-12, max_iter: int = 50) -> float:
    """Principal branch W0(x) via Newton's method. Solves w*exp(w) = x."""
    if x < -1.0 / math.e:
        raise ValueError(f"Lambert W undefined for x={x}")
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
        d = f / fp
        w -= d
        if abs(d) < tol * max(abs(w), 1.0):
            break
    return w


def gram_point(k: int) -> float:
    """k-th Gram point: gram_k ~ 2*pi*k / W(k/e)."""
    if k <= 0:
        return 0.0
    return 2.0 * math.pi * k / lambert_w(k / math.e)


def gue_pdf(s: float) -> float:
    """GUE (Wigner-Dyson) spacing PDF: p(s) = (pi*s/2)*exp(-pi*s^2/4)."""
    return (math.pi * s / 2.0) * math.exp(-math.pi * s * s / 4.0)


def gue_cdf(s: float) -> float:
    """GUE spacing CDF: P(s) = 1 - exp(-pi*s^2/4)."""
    return 1.0 - math.exp(-math.pi * s * s / 4.0)


def compute_bN(zeros: List[float], N: int) -> float:
    """Compute b(N) = (1/N) * sum_{k=1}^{N} |gamma_k - gram_k|."""
    if N <= 0 or N > len(zeros):
        return float("nan")
    total = 0.0
    for k in range(1, N + 1):
        total += abs(zeros[k - 1] - gram_point(k))
    return total / N


def ks_test(data: List[float], cdf) -> Tuple[float, float]:
    """Kolmogorov-Smirnov goodness-of-fit test. Returns (D, p-value)."""
    n = len(data)
    if n == 0:
        return 0.0, 1.0
    sd = sorted(data)
    dp = dm = 0.0
    for i, x in enumerate(sd):
        fx = cdf(x)
        dp = max(dp, (i + 1) / n - fx)
        dm = max(dm, fx - i / n)
    D = max(dp, dm)
    z = D * math.sqrt(n)
    pv = 0.0
    for k in range(1, 100):
        t = 2.0 * ((-1) ** (k + 1)) * math.exp(-2.0 * k * k * z * z)
        pv += t
        if abs(t) < 1e-15:
            break
    return D, max(0.0, min(1.0, pv))


def cvm_test(data: List[float], cdf) -> float:
    """Cramer-von Mises test statistic W^2."""
    n = len(data)
    if n == 0:
        return 0.0
    sd = sorted(data)
    w2 = 1.0 / (12.0 * n)
    for i, x in enumerate(sd):
        w2 += ((2.0 * (i + 1) - 1.0) / (2.0 * n) - cdf(x)) ** 2
    return w2


def linreg(x: List[float], y: List[float]) -> Tuple[float, float, float, float]:
    """Linear regression y = m*x + b. Returns (m, b, m_std_err, r2)."""
    n = len(x)
    if n < 2:
        return 0.0, 0.0, 0.0, 0.0
    sx, sy = sum(x), sum(y)
    sxx = sum(a * a for a in x)
    sxy = sum(a * b for a, b in zip(x, y))
    den = n * sxx - sx * sx
    if abs(den) < 1e-30:
        return 0.0, 0.0, 0.0, 0.0
    m = (n * sxy - sx * sy) / den
    b = (sy - m * sx) / n
    ym = sy / n
    sst = sum((yi - ym) ** 2 for yi in y)
    ssr = sum((yi - (m * xi + b)) ** 2 for xi, yi in zip(x, y))
    r2 = 1.0 - ssr / sst if sst > 0 else 0.0
    mse = ssr / (n - 2) if n > 2 else 0.0
    se = math.sqrt(mse * n / den) if den > 0 else 0.0
    return m, b, se, r2

# ═══════════════════════════════════════════════════════════════════════════
# Zero loader (self-contained)
# ═══════════════════════════════════════════════════════════════════════════

SOURCES: List[Tuple[str, str, int]] = [
    ("50k",    "zeta_zeros_50000.txt",        13661),
    ("500k",   "zeta_zeros_500k_odlyzko.txt", 500000),
    ("2M",     "zeta_zeros_2M_odlyzko.txt",   2001052),
    ("highT",  "zeta_zeros_highT_blocks.txt", 30000),
    ("2M_gz",  "zeta_zeros_2M_odlyzko.txt.gz",2001052),
    ("csv",    "zeta_zeros_50000.csv",        13661),
    ("zeros6", "zeros6.txt",                  2001052),
]


def _parse_plain(lines: List[str]) -> List[float]:
    out: List[float] = []
    for ln in lines:
        s = ln.strip()
        if not s or s.startswith("#"):
            continue
        try:
            out.append(float(s))
        except ValueError:
            continue
    return out


def _parse_highT(lines: List[str]) -> List[float]:
    out: List[float] = []
    base = 0.0
    for ln in lines:
        s = ln.strip()
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
    return out


def _parse_csv(lines: List[str]) -> List[float]:
    out: List[float] = []
    for row in csv.reader(lines):
        if not row or row[0].startswith("#"):
            continue
        try:
            out.append(float(row[1]))
        except (ValueError, IndexError):
            continue
    return out


def _parse_julia(lines: List[str]) -> List[float]:
    out: List[float] = []
    inside = False
    for ln in lines:
        if ln.strip().startswith("#"):
            continue
        if "Float64[" in ln:
            inside = True
        if inside:
            c = re.sub(r"[^\d.eE+\-.,\s]", " ", ln).replace("[", " ").replace("]", " ")
            for tok in c.split(","):
                tok = tok.strip()
                if tok:
                    try:
                        out.append(float(tok))
                    except ValueError:
                        pass
            if "]" in ln:
                inside = False
    return out


def load_zeros(
    data_dir: str,
    count: int = 5000,
    source: str = "auto",
    msg: Optional[Dict[str, str]] = None,
) -> List[float]:
    """Load zeros from data files. Returns sorted list of floats."""
    if msg is None:
        msg = MSG_EN

    if source == "auto":
        cands = [(n, f, a) for n, f, a in SOURCES if a >= count]
        if not cands:
            print(msg["no_source"].format(count=count), file=sys.stderr)
            return []
        cands.sort(key=lambda x: x[2])
        source, fname, avail = cands[0]
        print(msg["auto_select"].format(source=source, count=count, avail=avail))
    else:
        fname = None
        avail = 0
        for sn, sf, sa in SOURCES:
            if sn == source:
                fname, avail = sf, sa
                break
        if fname is None:
            print(msg["no_source"].format(count=count), file=sys.stderr)
            return []

    fp = Path(data_dir) / fname
    print(msg["loading"].format(count=count, source=fname))

    if not fp.exists():
        print(msg["file_not_found"].format(path=fp), file=sys.stderr)
        return []

    if str(fp).endswith(".gz"):
        with gzip.open(fp, "rt", encoding="utf-8") as f:
            lines = f.readlines()
        zeros = _parse_plain(lines)
    elif source == "highT":
        with open(fp, "r", encoding="utf-8") as f:
            zeros = _parse_highT(f.readlines())
    elif source == "csv":
        with open(fp, "r", encoding="utf-8") as f:
            zeros = _parse_csv(f.readlines())
    elif fname.endswith(".jl"):
        with open(fp, "r", encoding="utf-8") as f:
            zeros = _parse_julia(f.readlines())
    else:
        with open(fp, "r", encoding="utf-8") as f:
            zeros = _parse_plain(f.readlines())

    zeros.sort()
    zeros = zeros[:count]
    if zeros:
        print(msg["loaded"].format(n=len(zeros), source=fname,
                                    tmin=zeros[0], tmax=zeros[-1]))
    return zeros

# ═══════════════════════════════════════════════════════════════════════════
# Objection implementations
# ═══════════════════════════════════════════════════════════════════════════

def run_obj1(zeros: List[float], msg: Dict[str, str]) -> Dict[str, object]:
    """Objection 1: b(N) convergence."""
    Ns = [100, 500, 1000, 5000, 10000, 50000]
    Ns = [n for n in Ns if n <= len(zeros)]
    if not Ns:
        Ns = [min(len(zeros), 100)]

    print(f"\n{'='*60}")
    print(msg["obj1_title"])
    print(msg["obj1_converge"])
    print(msg["obj1_header"])
    print("-" * 60)

    bvals: List[float] = []
    prev: Optional[float] = None
    for N in Ns:
        b = compute_bN(zeros, N)
        bvals.append(b)
        d = b - prev if prev is not None else float("nan")
        ds = f"{d:+.10f}" if not math.isnan(d) else "---"
        print(f"{N:>10d}  {b:>20.10f}  {ds:>20s}")
        prev = b

    converged = abs(bvals[-1] - bvals[-2]) < 0.01 if len(bvals) >= 2 else False
    return {"bN_values": bvals, "converged": converged}


def run_obj2(zeros: List[float], msg: Dict[str, str]) -> Dict[str, object]:
    """Objection 2: GUE spacing."""
    print(f"\n{'='*60}")
    print(msg["obj2_title"])

    spacings: List[float] = []
    for k in range(len(zeros) - 1):
        g = zeros[k]
        if g <= 0:
            continue
        spacings.append((zeros[k + 1] - g) * math.log(g / (2.0 * math.pi)) / (2.0 * math.pi))

    print(f"  Computed {len(spacings)} normalized spacings")

    D, p = ks_test(spacings, gue_cdf)
    print(f"  {msg['obj2_ks'].format(D=D, p=p)}")

    W2 = cvm_test(spacings, gue_cdf)
    print(f"  {msg['obj2_cvm'].format(W2=W2)}")

    rej = p < 0.05
    v = msg["obj2_reject"] if rej else msg["obj2_keep"]
    print(f"  {msg['obj2_result'].format(verdict=v)}")

    return {"D": D, "p_value": p, "W2": W2, "rejected": rej}


def run_obj3(zeros: List[float], msg: Dict[str, str]) -> Dict[str, object]:
    """Objection 3: Large-T decay rate."""
    print(f"\n{'='*60}")
    print(msg["obj3_title"])

    mx = len(zeros)
    Ns: List[int] = []
    n = 50
    while n <= mx:
        Ns.append(n)
        n = int(n * 2)
    if Ns[-1] != mx and mx > 100:
        Ns.append(mx)

    lx: List[float] = []
    ly: List[float] = []
    print("  Computing b(N) at multiple N values ...")
    for N in Ns:
        b = compute_bN(zeros, N)
        if b <= 0:
            continue
        lx.append(math.log(N))
        ly.append(math.log(b))
        print(f"    N = {N:>8d}  b(N) = {b:.10f}")

    if len(lx) < 3:
        print("  WARNING: not enough data points")
        return {"slope": float("nan"), "slope_ci": (float("nan"), float("nan")),
                "consistent": False}

    m, b0, se, r2 = linreg(lx, ly)
    lo, hi = m - 1.96 * se, m + 1.96 * se

    print(f"  {msg['obj3_fit'].format(slope=m, intercept=b0)}")
    print(f"  R^2 = {r2:.6f}")
    print(f"  {msg['obj3_expected']}")
    print(f"  {msg['obj3_ci'].format(lo=lo, hi=hi)}")

    ok = abs(m - (-0.5)) <= 0.1
    rel = msg["obj3_in"] if ok else msg["obj3_out"]
    verd = msg["obj3_ok"] if ok else msg["obj3_bad"]
    print(f"  {msg['obj3_verdict'].format(slope=m, relation=rel, verdict=verd)}")

    return {"slope": m, "slope_ci": (lo, hi), "consistent": ok}

# ═══════════════════════════════════════════════════════════════════════════
# Main
# ═══════════════════════════════════════════════════════════════════════════

def main() -> None:
    parser = argparse.ArgumentParser(
        description="AB-Cloud Verification Suite (standalone runner)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python run_verify.py --zeros 200000 --source 500k --objection all
  python run_verify.py --zeros 5000 --source 50k --objection 1 --lang ru
  python run_verify.py --data-dir ../data --zeros 1000 --objection 2
""",
    )
    parser.add_argument("--zeros", type=int, default=5000,
                        help="Number of zeros to load (default: 5000)")
    parser.add_argument("--source", default="auto",
                        help="Data source: auto,50k,500k,2M,highT,2M_gz,csv,zeros6")
    parser.add_argument("--objection", default="all",
                        help="Which objection to verify: 1, 2, 3, or all")
    parser.add_argument("--lang", default=None,
                        help="Output language: en or ru (default: auto-detect from LANG)")
    parser.add_argument("--data-dir", default=None,
                        help="Path to data/ directory (default: ../data/)")
    args = parser.parse_args()

    # Language
    lang = args.lang
    if lang is None:
        lang = "ru" if "ru" in os.environ.get("LANG", "").lower() else "en"
    msg = MSG_RU if lang == "ru" else MSG_EN

    # Data dir
    data_dir = args.data_dir
    if data_dir is None:
        data_dir = str(Path(__file__).resolve().parent.parent / "data")

    # Validate objection
    if args.objection not in ("1", "2", "3", "all"):
        print(f"ERROR: --objection must be 1, 2, 3, or all (got '{args.objection}')",
              file=sys.stderr)
        sys.exit(1)

    # Load zeros
    zeros = load_zeros(data_dir, count=args.zeros, source=args.source, msg=msg)
    if not zeros:
        sys.exit(1)

    # Run objections
    results: Dict[str, Dict[str, object]] = {}
    if args.objection in ("1", "all"):
        results["obj1"] = run_obj1(zeros, msg)
    if args.objection in ("2", "all"):
        results["obj2"] = run_obj2(zeros, msg)
    if args.objection in ("3", "all"):
        results["obj3"] = run_obj3(zeros, msg)

    # Summary
    print(f"\n{'='*60}")
    print(msg["summary"])
    smap = {
        "obj1": lambda r: msg["pass_"] if r.get("converged") else msg["warn"],
        "obj2": lambda r: msg["pass_"] if not r.get("rejected") else msg["fail"],
        "obj3": lambda r: msg["pass_"] if r.get("consistent") else msg["fail"],
    }
    for key, res in results.items():
        st = smap[key](res)
        print(msg["summary_line"].format(n=key[-1], status=st))
    print("=" * 60)


if __name__ == "__main__":
    main()
