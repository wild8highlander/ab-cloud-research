#!/usr/bin/env python3
"""Кампания V01 — blind spectrum (экскурсия по закоммиченному вердикту)."""
import json, os

def main():
    R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    d = json.load(open(f"{R}/data/v01_verdict.json"))
    print("== V01 blind spectrum ==")
    print(f"  r_test = {d['r_test']:.3f} (нулевая зона {d['perm_null_mean']:.3f}±{d['perm_null_sd']:.3f}, z = {d['r_test_z']:.2f})")
    m = d.get("meta", {})
    print(f"  прогон {m.get('date')} · {m.get('runtime_s')} s · "
          f"{m.get('package')}")

if __name__ == "__main__":
    main()
