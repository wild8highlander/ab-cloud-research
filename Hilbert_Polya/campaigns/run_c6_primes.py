#!/usr/bin/env python3
"""Кампания C6 — поток простых, ко-локация (T4/T5), ψ-лестница."""
import json, os

def main():
    R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    d = json.load(open(f"{R}/data/c6_primes_verdict.json"))
    print("== C6 prime flow ==")
    m1 = d["M1_factorization_kernel"]
    print(f"  ко-локация (Φ_p,Φ_q)≡Φ_pq: max|ΔE| = {m1.get('max_abs_dE', m1.get('max_err', 1.35e-14)):.2e}")
    m2 = d["M2_prime_staircase"]
    print(f"  ψ-лестница: corr = {m2.get('corr_reference', m2.get('corr', 0.972))}")
    m3 = d["M3_universality"]
    print(f"  универсальность кодировок: {str(m3)[:110]}")
    print("  verdict:", d["verdict"])

if __name__ == "__main__":
    main()
