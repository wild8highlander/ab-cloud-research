#!/usr/bin/env python3
"""Кампания V02 — null models (экскурсия по закоммиченному вердикту)."""
import json, os

def main():
    R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    d = json.load(open(f"{R}/data/v02_verdict.json"))
    print("== V02 null models ==")
    print(f"  M0 ⟨r⟩ = {d['models']['M0_ab_cloud']['r_mean']:.4f}, D_KS = {d['models']['M0_ab_cloud']['KS_GUE']:.4f} (GUE)")
    m = d.get("meta", {})
    print(f"  прогон {m.get('date')} · {m.get('runtime_s')} s · "
          f"{m.get('package')}")

if __name__ == "__main__":
    main()
