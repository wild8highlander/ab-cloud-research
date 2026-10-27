#!/usr/bin/env python3
"""Кампания C7 — динамика волнового пакета (L=96)."""
import json, os

def main():
    R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    d = json.load(open(f"{R}/data/c7_dynamics_verdict.json"))
    print("== C7 wave-packet dynamics (L=96) ==")
    for k in ("clean", "z16", "z64", "z256", "r256"):
        if k in d:
            print(f"  {k}: {str(d[k])[:150]}")

if __name__ == "__main__":
    main()
