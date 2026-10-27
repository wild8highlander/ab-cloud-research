#!/usr/bin/env python3
"""Кампания V05 — lattice limit (экскурсия по закоммиченному вердикту)."""
import json, os

def main():
    R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    d = json.load(open(f"{R}/data/v05_verdict.json"))
    print("== V05 lattice limit ==")
    print(f"  p = {d['power_law']['p']:.3f}, R² = {d['power_law']['r2']:.3f}, proj_ovl = {d['projector_overlap_mean']:.4f}")
    m = d.get("meta", {})
    print(f"  прогон {m.get('date')} · {m.get('runtime_s')} s · "
          f"{m.get('package')}")

if __name__ == "__main__":
    main()
