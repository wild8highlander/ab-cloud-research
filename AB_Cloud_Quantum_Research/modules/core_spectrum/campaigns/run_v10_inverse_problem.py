#!/usr/bin/env python3
"""Кампания V10 — inverse problem (экскурсия по закоммиченному вердикту)."""
import json, os

def main():
    R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    d = json.load(open(f"{R}/data/v10_verdict.json"))
    print("== V10 inverse problem ==")
    print(f"  rank = {d['sensitivity']['Nv4']['rank']}, recovery |Δq| = {d['recovery']['q_recovery_max_err']:.3f}")
    m = d.get("meta", {})
    print(f"  прогон {m.get('date')} · {m.get('runtime_s')} s · "
          f"{m.get('package')}")

if __name__ == "__main__":
    main()
