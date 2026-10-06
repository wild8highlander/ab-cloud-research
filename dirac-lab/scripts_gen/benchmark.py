#!/usr/bin/env python3
"""Quick-mode benchmark of the Dirac Laboratory suite.

Runs all four canonical modules in quick mode (no figures, isolated result
directories) and writes results/PERFORMANCE.md with measured wall times.

Usage:
    python3 scripts_gen/benchmark.py
"""

import os
import re
import shutil
import subprocess
import sys
import time
import platform
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES = [
    ("Core suite D1-D8", "code/dirac_lab.py", "QUICK"),
    ("Extensions I: D9-D10", "code/dirac_lab_extensions.py", "FULL"),
    ("Extensions II: D11", "code/dirac_lab_extensions2.py", "QUICK"),
    ("Extensions III: D12-D14", "code/dirac_lab_extensions3.py", "QUICK"),
]
TMP = os.path.join(ROOT, "results", "bench_quick_tmp")

# Canonical FULL-mode wall times recorded in results/run_20261006_full_v13
FULL_REFERENCE = [
    ("Core suite D1-D8", "8 tests / 33 checks", "~2.0 min"),
    ("Extensions I: D9-D10", "2 tests / 19 checks", "~1.0 min"),
    ("Extensions II: D11", "1 test / 15 checks", "~0.3 min"),
    ("Extensions III: D12-D14", "3 tests / 29 checks", "~4.4 min"),
]


def run_quick(module: str, quick: bool):
    args = [sys.executable, module, "--no-figures", "--resdir", TMP]
    if quick:
        args.append("--quick")
    t0 = time.perf_counter()
    proc = subprocess.run(args, cwd=ROOT, capture_output=True, text=True)
    dt = time.perf_counter() - t0
    out = proc.stdout + proc.stderr
    m = re.search(r"(\d+)/(\d+)\s+(?:[A-Za-z-]+\s+)?tests?\s+PASS", out)
    npass, ntot = (m.group(1), m.group(2)) if m else ("?", "?")
    return dt, npass, ntot, proc.returncode


def main():
    rows = []
    for label, module, mode in MODULES:
        print(f"[bench] {label} ({module}, {mode}) ...", flush=True)
        dt, npass, ntot, rc = run_quick(module, mode == "QUICK")
        ok = "OK" if rc == 0 else f"rc={rc}"
        print(f"        {dt:6.1f} s   {npass}/{ntot} PASS   {ok}", flush=True)
        rows.append((label, module, mode, dt, npass, ntot, rc))
    shutil.rmtree(TMP, ignore_errors=True)

    total = sum(r[3] for r in rows)
    all_pass = sum(int(r[4]) for r in rows if r[4].isdigit())
    all_tot = sum(int(r[5]) for r in rows if r[5].isdigit())

    try:
        import numpy, scipy
        np_ver, sp_ver = numpy.__version__, scipy.__version__
    except Exception:
        np_ver = sp_ver = "?"

    lines = [
        "# Performance — Dirac Laboratory",
        "",
        f"*Measured: {datetime.now().strftime('%Y-%m-%d %H:%M')} · "
        f"Python {platform.python_version()} · numpy {np_ver} · scipy {sp_ver} · "
        f"{os.cpu_count()} logical cores · {platform.system()} {platform.release()}*",
        "",
        "## Measured wall times (no figures)",
        "",
        "Mode independence (v1.4): D10b transport runs at L = 48, D10a pair",
        "statistics at the canonical 2000 zeros and the D9d composite vortex",
        "on the canonical 200^2 domain in BOTH modes — quick verdicts are now",
        "identical to FULL. D9-D10 are still measured in FULL here: it is the",
        "canonical mode and, for this module, also the faster one (the",
        "reduced quick domain converges the sparse eigensolvers more slowly).",
        "All other modules run their quick mode.",
        "",
        "| Module | Module file | Mode | Wall time | Verdict |",
        "|---|---|---|---|---|",
    ]
    for label, module, mode, dt, npass, ntot, rc in rows:
        lines.append(f"| {label} | `{module}` | {mode} | **{dt:.1f} s** | {npass}/{ntot} PASS |")
    lines += [
        f"| **Total** |  |  | **{total:.1f} s** | **{all_pass}/{all_tot} PASS** |",
        "",
        "## Full mode (canonical run `results/run_20261006_full_v13`)",
        "",
        "| Module | Scope | Wall time (recorded) |",
        "|---|---|---|",
    ]
    for label, scope, t in FULL_REFERENCE:
        lines.append(f"| {label} | {scope} | {t} |")
    lines += [
        "| **Total** | **14 tests / 96 checks** | **~7.7 min** |",
        "",
        "## Where the time goes and what is already optimized",
        "",
        "- **Dense Hermitian eigendecompositions** dominate the core suite:",
        "  the largest Hamiltonian is the 2L^2 = 8192-dimensional L = 64 torus",
        "  (D1 finite-size track); `numpy.linalg.eigvalsh` (LAPACK `dsyevd`,",
        "  multi-threaded BLAS) is used everywhere the full spectrum is needed.",
        "- **Wall physics (D9, D13)**: the open-grid spectra are dense but the",
        "  multiplet isolation needs only the sorted eigenvalue list — no",
        "  eigenvector diagonalization on the largest grids.",
        "- **D11/D12** avoid naive O(N_u^2) Fourier sums: the Dirichlet comb has",  
        "  a closed-form kernel (O(N_u) per evaluation, no diagonalization at all),",
        "  and the dilation operator is diagonal by construction (F† diag F with",
        "  the unitary DFT) — its spectrum is exact arithmetic, not iterative.",
        "- **D11c/D14** form factors use the vectorized sliding-window estimator",
        "  (per-window local re-unfolding, L_w = 200, stride L_w/2; the phase",
        "  matrix is one `np.outer` per window) instead of quadratic pair loops.",
        "- **Reproducibility first**: every module is seeded (seed 96) and the",
        "  suite is deterministic; threading affects only BLAS internals, never",
        "  the published numbers.",
        "",
        "## How to reproduce",
        "",
        "```bash",
        "python3 scripts_gen/benchmark.py        # this table, quick mode",
        "make quick                              # core sanity pass only",
        "make all                                # canonical FULL run (~8-12 min)",
        "```",
        "",
        "To pin BLAS threading: `OMP_NUM_THREADS=4 make all` (results are",
        "thread-count independent; only wall time changes).",
        "",
    ]
    out = os.path.join(ROOT, "results", "PERFORMANCE.md")
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"\n[bench] written {out}")


if __name__ == "__main__":
    main()
