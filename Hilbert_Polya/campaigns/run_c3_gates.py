#!/usr/bin/env python3
"""Кампания C3 — семейство 52 затворов H7 (Г2, первая проекция)."""
import csv, json, os
import numpy as np

def main():
    R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    rows = list(csv.DictReader(open(f"{R}/data/c3_gates_table.csv")))
    d = json.load(open(f"{R}/data/c3_gates_verdict.json"))["verdict"]
    r7 = np.array([float(x["r_H7"]) for x in rows])
    print("== C3 gate family ==")
    print(f"  gates: {len(rows)}; best r_H7 = {r7.max():.3f} "
          f"(p={d['best_gate']['p_r']}, Bonferroni {d['min_p_bonferroni']})")
    print(f"  identity_found = {d['identity_found']}")
    print(f"  PC1 spinor twins r = {d['pc1_r']}, PC2 graph r = {d['pc2_r']:.12f}")

if __name__ == "__main__":
    main()
