#!/usr/bin/env python3
"""Кампания C5 — расширенное семейство (6 новых ручек, 35+2 затворов).

v2.0.5: таблица и вердикт регенерированы честным v2-конвейером
(см. docs/audit_v2.0.5.md): ⟨r⟩ — протокол C8 (канон GUE 0.5996),
r_H7 — v2-конвенция k0=224, r_EF — флуктуационная корреляция v2.
"""
import csv, json, os
import numpy as np

def main():
    R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    rows = list(csv.DictReader(open(f"{R}/data/c5_gates_ext_table.csv")))
    d = json.load(open(f"{R}/data/c5_gates_ext_verdict.json"))
    core = rows[:-2]
    r7 = np.array([abs(float(x["r_H7"])) for x in core])
    rm = np.array([float(x["r_mean"]) for x in core])
    n_gue = sum(1 for x in core if x.get("gue_class") == "1")
    print("== C5 extended gates (v2.0.5) ==")
    print(f"  new gates: {len(core)} (+2 decoys)")
    print(f"  <r> = {rm.mean():.3f} ± {rm.std():.3f}  "
          f"[{rm.min():.3f}, {rm.max():.3f}]")
    print(f"  GUE band 0.5996±0.03: {n_gue}/{len(core)} strict; "
          f"family mean {rm.mean():.3f} (canonical 0.5996)")
    print(f"  |r_H7| max = {r7.max():.3f}  (C3 best 0.226; PC0' = "
          f"{d['PC0p_r']:.9f})")
    v = d["verdict"]
    print(f"  r_EF (fluct) = {v['rEF_fluct_mean']:+.3f} ± "
          f"{v['rEF_fluct_sd']:.3f}  vs honest GUE null "
          f"{v['GUE_mean']:+.3f} ± {v['GUE_sd']:.3f}")
    print(f"  verdict: {v['verdict'][:100]}…")

if __name__ == "__main__":
    main()
