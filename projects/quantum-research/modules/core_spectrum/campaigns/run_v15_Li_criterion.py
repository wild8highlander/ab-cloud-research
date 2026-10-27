#!/usr/bin/env python3
"""Кампания V15 — Li criterion (экскурсия по закоммиченному вердикту)."""
import json, os

def main():
    R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    d = json.load(open(f"{R}/data/v15_verdict.json"))
    print("== V15 Li criterion ==")
    print(f"  λ_1 = {d['lambda_1']:.6f}, λ_min@{d['argmin_n']}, Th4 |Δ| = {d['Th4_max_abs_diff']:.1e}, n ≤ {d['n_max']} positive = {d['all_positive_certified']}")
    m = d.get("meta", {})
    print(f"  прогон {m.get('date')} · {m.get('runtime_s')} s · "
          f"{m.get('package')}")

if __name__ == "__main__":
    main()
