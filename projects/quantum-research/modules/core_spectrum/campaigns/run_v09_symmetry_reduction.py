#!/usr/bin/env python3
"""Кампания V09 — symmetry reduction (экскурсия по закоммиченному вердикту)."""
import json, os

def main():
    R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    d = json.load(open(f"{R}/data/v09_verdict.json"))
    print("== V09 symmetry reduction ==")
    print(f"  Th5 = {d['theorem_verified']}, union err = {d['part_A']['block_union_err']:.1e}, vortex ε = {d['part_B']['max_commutator']:.1f}")
    m = d.get("meta", {})
    print(f"  прогон {m.get('date')} · {m.get('runtime_s')} s · "
          f"{m.get('package')}")

if __name__ == "__main__":
    main()
