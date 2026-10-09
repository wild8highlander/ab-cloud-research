#!/usr/bin/env python3
"""Кампания C2 — аргументный принцип до T=1000 (K4/K5/K6)."""
import json, os

def main():
    R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    d = json.load(open(f"{R}/data/c2_argument_verdict.json"))
    print("== C2 argument principle ==")
    for name, blk in list(d["anchors"].items()) + list(d["blocks"].items()):
        print(f"  {name}: N={blk['N_int']} (остаток {blk['residual_to_int']:.1e}, "
              f"на линии {blk['n_on_line_file']})")
    br = d["bridge"]
    k0 = list(br)[0]
    print(f"  мост fp↔mp ({k0}): |ΔN| = {br[k0]['delta']:.1e}")
    g = d["gaps_below_1000"]
    print(f"  T<1000: нулей {g['n']}, зазоры [{g['min_gap']:.3f}, {g['max_gap']:.3f}], "
          f"средний {g['mean_gap']:.3f}")

if __name__ == "__main__":
    main()
