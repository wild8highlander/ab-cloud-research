#!/usr/bin/env python3
"""Кампания V03 — critical line scan (экскурсия по закоммиченному вердикту)."""
import json, os

def main():
    R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    d = json.load(open(f"{R}/data/v03_verdict.json"))
    print("== V03 critical line scan ==")
    print(f"  argmin σ = {d['argmin_sigma']}, D(0.5) = {d['D_05']:.4f}, min@half = {d['minimum_at_half']}")
    m = d.get("meta", {})
    print(f"  прогон {m.get('date')} · {m.get('runtime_s')} s · "
          f"{m.get('package')}")

if __name__ == "__main__":
    main()
