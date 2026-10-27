#!/usr/bin/env python3
"""Кампания V07 — arithmetic trace (экскурсия по закоммиченному вердикту)."""
import json, os

def main():
    R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    d = json.load(open(f"{R}/data/v07_verdict.json"))
    print("== V07 arithmetic trace ==")
    print(f"  |ΔQ| = {d['verify']['M0_max_abs_diff_Q']:.1e}, |ΔK| = {d['verify']['M1_max_abs_diff_K']:.1e}, PC0 r = {d['PC0_Hxi_r']:.4f}")
    m = d.get("meta", {})
    print(f"  прогон {m.get('date')} · {m.get('runtime_s')} s · "
          f"{m.get('package')}")

if __name__ == "__main__":
    main()
