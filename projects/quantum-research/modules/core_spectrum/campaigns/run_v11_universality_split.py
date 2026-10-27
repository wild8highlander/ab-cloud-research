#!/usr/bin/env python3
"""Кампания V11 — universality split (экскурсия по закоммиченному вердикту)."""
import json, os

def main():
    R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    d = json.load(open(f"{R}/data/v11_verdict.json"))
    print("== V11 universality split ==")
    print(f"  ⟨r⟩ delta = {d['universal_survival_delta']:.4f}, noise-dominated = {d['noise_dominated']}")
    m = d.get("meta", {})
    print(f"  прогон {m.get('date')} · {m.get('runtime_s')} s · "
          f"{m.get('package')}")

if __name__ == "__main__":
    main()
