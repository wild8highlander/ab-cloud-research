#!/usr/bin/env python3
"""Кампания V04 — operator passport (экскурсия по закоммиченному вердикту)."""
import json, os

def main():
    R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    d = json.load(open(f"{R}/data/v04_verdict.json"))
    print("== V04 operator passport ==")
    print(f"  ‖H−H†‖ = {d['P1_max']:.1e}, ‖Hv−λv‖ = {d['P4_max']:.1e}, Th1 = {d['P1_hermiticity']}")
    m = d.get("meta", {})
    print(f"  прогон {m.get('date')} · {m.get('runtime_s')} s · "
          f"{m.get('package')}")

if __name__ == "__main__":
    main()
