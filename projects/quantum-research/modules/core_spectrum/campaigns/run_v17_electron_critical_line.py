#!/usr/bin/env python3
"""Кампания V17 — electron on the critical line (экскурсия)."""
import json, os

def main():
    R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    d = json.load(open(f"{R}/data/v17_verdict.json"))
    print("== V17 electron on the critical line ==")
    s = d['summary']
    print(f"  transit: zeta {s['transit_zeta']:.4f} / random "
          f"{s['transit_random']:.4f} (x{s['ratio_zeta_over_random']:.2f}) / clean "
          f"{s['transit_clean']:.4f}")
    print(f"  energy max dev = {s['energy_max_dev']:.2e}, "
          f"r_phase zeta = {s['r_phase_zeta']:.3f}")

if __name__ == "__main__":
    main()
