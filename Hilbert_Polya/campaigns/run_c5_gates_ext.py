#!/usr/bin/env python3
"""Кампания C5 — расширенное семейство (6 новых ручек, 35+2 затворов)."""
import csv, json, os
import numpy as np

def main():
    R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    rows = list(csv.DictReader(open(f"{R}/data/c5_gates_ext_table.csv")))
    d = json.load(open(f"{R}/data/c5_gates_ext_verdict.json"))
    core = rows[:-2]
    r7 = np.array([abs(float(x["r_H7"])) for x in core])
    rm = np.array([float(x["r_mean"]) for x in core])
    print("== C5 extended gates ==")
    print(f"  new gates: {len(core)} (+2 decoys)")
    print(f"  <r> = {rm.mean():.3f} ± {rm.std():.3f}  (GUE class everywhere)")
    print(f"  |r_H7| max = {r7.max():.3f}  (C3 best 0.226; PC 1.000)")
    print(f"  r_EF = {d['verdict']['rEF_mean']:+.3f} ± {d['verdict']['rEF_sd']:.3f}")
    print(f"  verdict: {d['verdict']['verdict'][:80]}…")

if __name__ == "__main__":
    main()
