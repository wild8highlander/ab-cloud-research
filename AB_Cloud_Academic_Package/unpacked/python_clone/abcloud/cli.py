"""abcloud.cli — command-line entry point of the Python clone.

Usage:
    python -m abcloud.cli --test all          # full suite (two-pass)
    python -m abcloud.cli --test 1            # single test
    python -m abcloud.cli --test 12 --no-two-pass
    python -m abcloud.cli --test all --full   # reference-scale run (slow!)
    python -m abcloud.cli --list
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .core import ABConfig
from .runner import ALL_TESTS, run_suite


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="abcloud",
        description="AB-Cloud v23 SUPERCOMBO — Python reimplementation "
                    "(38-test verification suite for the AB-lattice / ζ-zeros "
                    "framework).",
    )
    p.add_argument("--test", default="all",
                   help="test number, range (e.g. 1-14), comma list, or 'all'")
    p.add_argument("--no-two-pass", action="store_true",
                   help="disable the HARDCORE second pass")
    p.add_argument("--full", action="store_true",
                   help="reference-scale configuration (zeros=50000, L=24/32); "
                        "default is the fast validation profile")
    p.add_argument("--zeros", type=int, default=None,
                   help="number of zeta zeros (default 2000 fast / 50000 full)")
    p.add_argument("--lattice", type=int, default=None,
                   help="primary lattice size L (default 24 fast / 24 full)")
    p.add_argument("--alpha", type=float, default=0.5)
    p.add_argument("--W", type=float, default=4.0, help="on-site disorder (Julia ab_W=4)")
    p.add_argument("--seed", type=int, default=12345)
    p.add_argument("--out", default="results_py",
                   help="output directory for reports")
    p.add_argument("--no-progress", action="store_true")
    p.add_argument("--list", action="store_true", help="list tests and exit")
    return p


def parse_tests(spec: str) -> list[int]:
    spec = spec.strip().lower()
    if spec in ("all", "*"):
        return sorted(ALL_TESTS)
    out: set[int] = set()
    for part in spec.split(","):
        part = part.strip()
        if "-" in part:
            a, b = part.split("-")
            out.update(range(int(a), int(b) + 1))
        elif part:
            out.add(int(part))
    bad = [t for t in sorted(out) if t not in ALL_TESTS]
    if bad:
        raise SystemExit(f"Unknown test id(s): {bad}. Valid: 1..38")
    return sorted(out)


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    if args.list:
        for tid in sorted(ALL_TESTS):
            print(f"  {tid:2d}  {ALL_TESTS[tid].__name__}")
        return 0
    tests = parse_tests(args.test)
    cfg = ABConfig(
        zeros=args.zeros if args.zeros else (50000 if args.full else 2000),
        L=args.lattice if args.lattice else 24,
        L_secondary=32,
        alpha=args.alpha,
        W=args.W,
        seed=args.seed,
        fast=not args.full,
    )
    print("═" * 62)
    print("  AB-Cloud v23 SUPERCOMBO — Python clone")
    print(f"  tests: {tests[0]}..{tests[-1]} ({len(tests)})  zeros: {cfg.zeros}"
          f"  L: {cfg.L}  α: {cfg.alpha}  W: {cfg.W}  seed: {cfg.seed}")
    print("═" * 62)
    suite = run_suite(tests, cfg, Path(args.out),
                      no_two_pass=args.no_two_pass,
                      progress=not args.no_progress)
    t = suite["totals"]
    print(f"\n  Totals: {t['pass']} PASS / {t['fail']} FAIL   "
          f"(wall {suite['wall_seconds']} s)   → {args.out}/final_report.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
