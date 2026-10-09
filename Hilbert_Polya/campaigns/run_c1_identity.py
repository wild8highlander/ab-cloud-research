#!/usr/bin/env python3
"""Кампания C1 — функция тождеств Z_id (K1–K4, K7).
Пересчитывает дешёвые инварианты из закоммиченных вердиктов."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from hpbridge.identity import gamma_ladder_closures, Z_id

def main():
    R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    d = json.load(open(f"{R}/data/c1_identity_verdict.json"))
    print("== C1 identity function ==")
    for k, blk in d["criteria"].items():
        flags = {kk: blk[kk] for kk in blk if kk in ("pass", "threshold")}
        print(f"  {k}: {flags}")
    print("  verdict:", d["verdict"])
    res = gamma_ladder_closures([1.0, 2.0, 3.0])
    print(f"  T1 re-derivation: max residual = {max(max(r) for r in res):.2e} (dps=40)")
    re, im = Z_id(17.3, dps=30)
    print(f"  Z_id(17.3) = {re:.9f}, |Im| = {abs(im):.1e}")

if __name__ == "__main__":
    main()
