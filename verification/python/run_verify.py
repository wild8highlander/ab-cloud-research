#!/usr/bin/env python3
"""
run_verify.py — CLI runner for the AB-Cloud Verification Suite.

Thin launcher: all math (Lambert W, θ-Newton Gram points, GUE table CDF,
KS/CvM/AD, ⟨r⟩, frozen golden anchors) lives in ab_cloud_verify.py so that
this runner can never drift from the canonical kernel.

Usage:
    python3 run_verify.py                          # 50 000 zeros, all objections
    python3 run_verify.py --zeros 5000 --objection 1
    python3 run_verify.py --objection 2 --lang ru
    python3 run_verify.py --data-dir ../data --source 500k --zeros 200000
"""

import argparse
import sys

import ab_cloud_verify as core


def main() -> int:
    parser = argparse.ArgumentParser(description="AB-Cloud Verification Suite (runner)")
    parser.add_argument("--zeros", type=int, default=50000, help="Number of zeros to load")
    parser.add_argument("--source", default="auto",
                        help="auto,50k,50k_full,500k,2M,highT,2M_gz,csv,zeros6")
    parser.add_argument("--objection", default="all", help="Which objection: 1,2,3,all")
    parser.add_argument("--lang", default=None, help="Output language: en, ru")
    parser.add_argument("--data-dir", default=None, help="Path to data/ directory")
    parser.add_argument("--no-selfcheck", action="store_true",
                        help="Skip the frozen-anchor self-check")
    args = parser.parse_args()

    res = core.run_verification(
        data_dir=args.data_dir,
        count=args.zeros,
        source=args.source,
        objection=args.objection,
        lang=args.lang,
        run_selfcheck=not args.no_selfcheck,
    )
    sc = res.get("selfcheck")
    return 1 if (sc and sc.get("fail", 0) > 0) else 0


if __name__ == "__main__":
    sys.exit(main())
