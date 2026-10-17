"""
AB-Cloud Verification Suite — English-Only Interface (thin wrapper).

All computation lives in ab_cloud_verify.py (single canonical kernel, frozen
golden anchors).  This wrapper only pins the output language to English so
that LANG/locale cannot change it.
"""
from ab_cloud_verify import *  # noqa: F401,F403
import argparse
import sys

import ab_cloud_verify as _core

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AB-Cloud Verification Suite (EN)")
    parser.add_argument("--zeros", type=int, default=50000, help="Number of zeros to load")
    parser.add_argument("--source", default="auto", help="auto,50k,50k_full,500k,2M,highT,2M_gz,csv,zeros6")
    parser.add_argument("--objection", default="all", help="Which objection: 1,2,3,all")
    parser.add_argument("--data-dir", default=None, help="Path to data/ directory")
    parser.add_argument("--no-selfcheck", action="store_true", help="Skip the frozen-anchor self-check")
    args = parser.parse_args()

    res = _core.run_verification(
        data_dir=args.data_dir,
        count=args.zeros,
        source=args.source,
        objection=args.objection,
        lang="en",
        run_selfcheck=not args.no_selfcheck,
    )
    sc = res.get("selfcheck")
    sys.exit(1 if (sc and sc.get("fail", 0) > 0) else 0)
