"""
abcloud.runner — orchestration of the 38-test suite (Python clone).

Mirrors the Julia two-pass design:
  pass 1  — primary/standard implementation on the primary lattice;
  pass 2  — HARDCORE deep validation (no-lattice-dependence where applicable);
  pass 3  — SERIES for tests 19/29/31 (α-sweeps);
  pass 4  — AUDIT for test 19 (twist audit).

Verdict algebra (same as the Julia suite):
  overall = PASS  iff (pass 1 PASS) or (pass 2 HARDCORE PASS), where a FAIL
  caused by a *statistical threshold* in pass 1 can be cleared by pass 2;
  a runtime exception in either pass yields FAIL with the exception recorded.

CLONE-CONVENTION: the clone's "passes" re-run the same Python implementation
with tightened acceptance windows / deeper sub-checks, exactly as documented
per test; the equivalence map is in the README.
"""

from __future__ import annotations

import datetime
import time
from dataclasses import asdict
from pathlib import Path

import numpy as np

from .core import ABConfig, gram_points, safe_json, zeta_zeros
from .tests_01_14 import TESTS_01_14
from .tests_15_26 import TESTS_15_26
from .tests_27_38 import TESTS_27_38

ALL_TESTS = {**TESTS_01_14, **TESTS_15_26, **TESTS_27_38}

TEST_TITLES = {
    1: "b(N) convergence table", 2: "Monotonicity verification",
    3: "Convergence rate (power-law fit)", 4: "GUE KS test (full range)",
    5: "GUE KS test (high-T only)", 6: "Spacing chi^2 histogram test",
    7: "Decay slope (log-log regression)", 8: "Residual analysis of fit",
    9: "Bootstrap CI for slope", 10: "Cross-validation stability",
    11: "Anderson-Darling test", 12: "Real zeros vs GUE matrix",
    13: "Number variance Σ²(L)", 14: "Spectral rigidity Δ₃(L)",
    15: "AB-cloud Hamiltonian construction", 16: "AB-cloud GUE classification",
    17: "Connes self-duality α↔1/α", 18: "Chiral symmetry AIII at α=1/2",
    19: "Dirac cone v_F", 20: "TKNN Chern number C₁=1 (gapped anchors)",
    21: "γ* spinorial phase ≈ π/2", 22: "AB phase Φ_AB = π/7 = δ_C",
    23: "Complex fractal factor CF", 24: "Dirac string flux verification",
    25: "Byers-Yang theorem check", 26: "PBC torus Dirac string",
    27: "Binary chiral symmetry at α=1/2", 28: "f_GUE figure of merit",
    29: "Dirac dip in DOS at α=1/2", 30: "Dirac cone vF scaling vs L",
    31: "Hatano-Nelson non-Hermitian skin", 32: "Multi-realization ⟨r⟩ bootstrap",
    33: "L-scaling ⟨r⟩", 34: "DIRECT AB-cloud vs ζ (full loaded set)",
    35: "Spectral form factor K(t)", 36: "Byte-level robustness",
    37: "(1/2)! via Γ — half-factorial & GUE normalization",
    38: "Curie point of the vortex-flux lattice magnet",
}


class ProgressBar:
    """Single-line stderr progress bar (the Julia UI3 analogue)."""

    def __init__(self, enabled: bool = True, width: int = 16):
        self.enabled = enabled
        self.width = width
        self.t0 = time.time()
        self.label = ""
        self.frac = 0.0
        self.extra = ""

    def update(self, frac: float, extra: str = ""):
        self.frac = max(0.0, min(1.0, frac))
        self.extra = extra
        self._render()

    def _render(self):
        if not self.enabled:
            return
        import sys

        filled = int(self.width * self.frac)
        bar = "█" * filled + "░" * (self.width - filled)
        el = time.time() - self.t0
        line = (f"\r [{bar}] {self.frac*100:5.1f}%  {el:6.0f}s  "
                f"{self.label} {self.extra}")
        sys.stderr.write(line[:78] + " " * 4)
        sys.stderr.flush()

    def finish(self):
        if self.enabled:
            import sys

            sys.stderr.write("\n")
            sys.stderr.flush()


def run_suite(tests: list[int], cfg: ABConfig, out_dir: Path,
              no_two_pass: bool = False, progress: bool = True) -> dict:
    """Run the requested tests and write reports into out_dir."""
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    t_start = time.time()
    bar = ProgressBar(enabled=progress)
    bar.label = "AB-Cloud PyClone"

    # shared context: zeta zeros + Gram points (computed once, cached)
    gammas = zeta_zeros(cfg.zeros)
    # γ̃_k = g_k for k = 1..N  (Gram points EXCLUDING g₀; see b_statistic)
    grams = gram_points(cfg.zeros + 1)[1:]
    ctx = {"gammas": gammas, "grams": grams, "cfg": cfg}

    results = []
    log_lines = []
    n_tests = len(tests)
    for i, tid in enumerate(tests):
        fn = ALL_TESTS[tid]
        bar.label = f"T{tid:02d}"
        bar.update(i / n_tests, f"start")
        t_test = time.time()
        entry = {
            "number": tid,
            "title": TEST_TITLES.get(tid, fn.__name__),
            "passes": [],
            "t": None,
        }
        try:
            res = fn(cfg, ctx)
            entry["passes"].append(res)
            # two-pass semantics (Julia algebra): OVERALL = pass1 AND pass2;
            # the master report lists both pass entries separately (the 79
            # entries of the reference run = individual pass verdicts).
            if not no_two_pass and res["verdict"] == "FAIL":
                hc = _hardcore_rerun(tid, cfg, ctx)
                entry["passes"].append(hc)
            entry["overall"] = ("PASS" if all(pp["verdict"] == "PASS"
                                              for pp in entry["passes"])
                                else "FAIL")
        except Exception as e:  # exception → FAIL entry (Julia parity)
            entry["passes"].append({
                "number": tid, "title": entry["title"], "slug": "exception",
                "pass_label": "pass 1", "verdict": "FAIL",
                "sub_checks": [("exception", False, f"{type(e).__name__}: {e}")],
                "metrics": {}, "lines": [f" EXCEPTION: {type(e).__name__}: {e}"],
            })
            entry["overall"] = "FAIL"
        entry["t"] = round(time.time() - t_test, 2)
        results.append(entry)
        log_lines.append(
            f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Test {tid} — "
            f"{entry['overall']} (elapsed {entry['t']:.2f}s)")
        bar.update((i + 1) / n_tests, f"done {entry['overall']}")
    bar.finish()

    suite = {
        "generated": datetime.datetime.now().isoformat(timespec="seconds"),
        "suite": "AB-Cloud v23 SUPERCOMBO — Python clone",
        "config": asdict(cfg),
        "results": results,
        "log": log_lines,
        "totals": {
            "tests": len(results),
            "entries": sum(len(r["passes"]) for r in results),
            "pass": sum(1 for r in results for pp in r["passes"]
                        if pp["verdict"] == "PASS"),
            "fail": sum(1 for r in results for pp in r["passes"]
                        if pp["verdict"] == "FAIL"),
        },
        "wall_seconds": round(time.time() - t_start, 2),
    }
    (out_dir / "results.json").write_text(safe_json(suite), encoding="utf-8")
    (out_dir / "run_log.txt").write_text("\n".join(log_lines), encoding="utf-8")

    from .report import write_reports
    write_reports(suite, out_dir)
    return suite


def _hardcore_rerun(tid: int, cfg: ABConfig, ctx: dict) -> dict:
    """HARDCORE pass-2 analogue: tighten the acceptance window of the
    statistical family tests and re-run (documented per test in the
    monograph, Appendix D).  For non-statistical tests the hardcore pass
    re-validates with a second RNG stream / secondary lattice size."""
    import copy

    cfg2 = copy.copy(cfg)
    cfg2.seed = cfg.seed + 1
    cfg2.L = cfg.L_secondary
    res = ALL_TESTS[tid](cfg2, ctx)
    res["pass_label"] = "HARDCORE pass 2"
    return res
