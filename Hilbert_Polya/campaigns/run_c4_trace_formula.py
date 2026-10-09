#!/usr/bin/env python3
"""Кампания C4 — следовая формула Tr e^{-uH} vs явная формула (T6, Г2-3)."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import numpy as np
from hpbridge import traceformula as TF

def main():
    R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    d = json.load(open(f"{R}/data/c4_trace_verdict.json"))
    v = d["verdict"]
    print("== C4 trace formula ==")
    print(f"  M0 identity |ΔQ| = {v['M0_max_abs_diff_Q']:.2e}")
    print(f"  M1 Tr e^(-xH_xi) |ΔK| = {v['M1_max_abs_diff_K']:.2e} (абс.)")
    print(f"  PC0 zeros window r = {v['PC0_Hxi_r']:.4f}, resid = {v['PC0_resid_rel']:.3f}")
    print(f"  gates r_EF = {v['gates_rEF_mean']:+.3f} ± {v['gates_rEF_sd']:.3f}, "
          f"best resid = {v['gates_resid_min']:.3f}")
    print(f"  gap (trace metric) = {v['gap_orders']:.2f} orders")
    print(f"  C3 protocol repro: |Δ| = {v.get('repro_err_C3', 0):.1e}")

if __name__ == "__main__":
    main()
