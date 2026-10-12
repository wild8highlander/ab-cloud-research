#!/usr/bin/env python3
"""Кампания V08 — self-adjointness (экскурсия по закоммиченному вердикту)."""
import json, os

def main():
    R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    d = json.load(open(f"{R}/data/v08_verdict.json"))
    print("== V08 self-adjointness ==")
    print(f"  defects (0,0) = {d['finite_self_adjoint']}, unitarity drift = {d['unitarity']['unitarity_drift_max']:.1e}")
    m = d.get("meta", {})
    print(f"  прогон {m.get('date')} · {m.get('runtime_s')} s · "
          f"{m.get('package')}")

if __name__ == "__main__":
    main()
