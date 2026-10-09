#!/usr/bin/env python3
"""Кампания C8 — статистическая лестница Пуассон/GOE/GUE + spinor64 (T8/T10)."""
import json, os

def main():
    R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    lad = json.load(open(f"{R}/computations/C8_stats_ladder/data/ladder/stats_ladder.json"))
    sp = json.load(open(f"{R}/computations/C8_stats_ladder/data/spinor64/spinor64_check.json"))
    print("== C8 statistics ladder ==")
    res = lad.get("results", [])
    if isinstance(res, dict):
        for k, v in list(res.items())[:8]:
            print(f"  {k}: {str(v)[:110]}")
    else:
        for row in res[:8]:
            print("  ", {k: row.get(k) for k in list(row)[:6]})
    e2 = sp.get("E2_reduction", {})
    print(f"  spinor64 64->4: {str(e2)[:110]}")
    print(f"  GSE note: {str(lad.get('GSE_note'))[:90]}")

if __name__ == "__main__":
    main()
