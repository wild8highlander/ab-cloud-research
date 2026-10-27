#!/usr/bin/env python3
"""Кампания V16 — full hamiltonian × full algebraic function (экскурсия)."""
import json, os

def main():
    R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    d = json.load(open(f"{R}/data/v16_verdict.json"))
    print("== V16 full hamiltonian x full algebraic function ==")
    s = d['summary']
    print(f"  max r_align = {s['r_align_max']:+.4f}, z_best = {s['z_best']:.2f}, "
          f"identity_closed = {s['identity_closed']}")
    print(f"  PC Z_id vs file: r = {d['positive_control']['pc_Z_id_vs_file']['r']}, "
          f"max residual = {d['positive_control']['pc_Z_id_vs_file']['max_residual']:.2e}")

if __name__ == "__main__":
    main()
