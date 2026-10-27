#!/usr/bin/env python3
"""Кампания V18 — AB operator as processor (экскурсия)."""
import json, os

def main():
    R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    d = json.load(open(f"{R}/data/v18_verdict.json"))
    print("== V18 AB operator as processor ==")
    print(f"  min gate fidelity = {d['p1_min_fidelity']:.15f}")
    e = d['p2_entanglement']
    print(f"  best concurrence = {e['best_concurrence']:.4f} at t = {e['t_entangle']:.3f}")
    p = d['p3_pong']
    print(f"  AB-Pong: score {p['score']['left']}:{p['score']['right']}, "
          f"kicks {p['kicks']}, replay bit-exact = {p['replay_bit_exact']}")
    print(f"  processor = {d['summary']['processor']}")

if __name__ == "__main__":
    main()
