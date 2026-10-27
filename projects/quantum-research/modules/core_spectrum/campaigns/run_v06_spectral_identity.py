#!/usr/bin/env python3
"""Кампания V06 — spectral identity (экскурсия по закоммиченному вердикту)."""
import json, os

def main():
    R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    d = json.load(open(f"{R}/data/v06_verdict.json"))
    print("== V06 spectral identity ==")
    print(f"  gate rank = {d['gate_rank_corr']:.4f}, H_ξ resid = {d['Hxi_control']['max_abs_log_resid']:.1e}")
    m = d.get("meta", {})
    print(f"  прогон {m.get('date')} · {m.get('runtime_s')} s · "
          f"{m.get('package')}")

if __name__ == "__main__":
    main()
