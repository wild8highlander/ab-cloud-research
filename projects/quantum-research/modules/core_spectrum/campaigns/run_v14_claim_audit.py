#!/usr/bin/env python3
"""Кампания V14 — claim audit (экскурсия по закоммиченному вердикту)."""
import json, os

def main():
    R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    d = json.load(open(f"{R}/data/v14_verdict.json"))
    print("== V14 claim audit ==")
    print(f"  all_a1 = {d['all_a1']}, covered = {d['covered']}, claims = {d['consistency']['n_claims']}")
    m = d.get("meta", {})
    print(f"  прогон {m.get('date')} · {m.get('runtime_s')} s · "
          f"{m.get('package')}")

if __name__ == "__main__":
    main()
