#!/usr/bin/env python3
"""Кампания V13 — formal bridge (экскурсия по закоммиченному вердикту)."""
import json, os

def main():
    R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    d = json.load(open(f"{R}/data/v13_verdict.json"))
    print("== V13 formal bridge ==")
    print(f"  RH: {d['rh_conclusion']}, blockers = {len(d['rh_blockers'])} (assumed {d['n_assumed']})")
    m = d.get("meta", {})
    print(f"  прогон {m.get('date')} · {m.get('runtime_s')} s · "
          f"{m.get('package')}")

if __name__ == "__main__":
    main()
