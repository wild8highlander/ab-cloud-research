#!/usr/bin/env python3
"""Кампания V19 — сшивка ветвей алгебраической функции (R2, механизм
hodge-laboratory). Печатает вердикты четырёх слоёв и композит."""
import json, os

def main():
    R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    d = json.load(open(f"{R}/data/v19_verdict.json"))
    print("== V19 branch stitching of the algebraic function (R2) ==")
    print(f"  stitch verdict: {d['stitch_verdict']}")
    A, B, C, D = d['layer_A'], d['layer_B'], d['layer_C'], d['layer_D']
    print(f"  [A] reference (hodge-lab mechanism, N=15): "
          f"{'PASS' if A['passed'] else 'FAIL'}, "
          f"closed-form resid {A['closed_form']['max_rel_resid']:.1e}, "
          f"phase-law resid {A['phase_law']['max_rel_resid']:.1e}")
    Bz, Ba = B['z2_monodromy'], B['argument_closure']
    print(f"  [B] Z_id critical line: alternation "
          f"{Bz['alternation_rate']*100:.2f}% over {Bz['n_intervals']} "
          f"intervals; argument closure T={Ba['T']}: "
          f"{Ba['n_sign_changes']} vs {Ba['n_zeros']} zeros "
          f"({'EXACT' if Ba['exact_match'] else 'MISMATCH'})")
    print(f"  [C] stitched object (Gamma-phase): ladder conc "
          f"{C['theta_ladder']['concentration']:.3f}, sign coherence "
          f"{C['sign_coherence']['agreement']:.4f} "
          f"(z = {C['sign_coherence']['z_score']:.1f}), verdict "
          f"{C['verdict']}")
    print(f"  [D] regression R1/R2/R4: "
          f"{'PASS' if D['passed'] else 'FAIL'} "
          f"(flagship {D['R1_flagship']['resid_rel']:.1e}, suite worst "
          f"{D['R2_suite']['worst_phase_dev']:.1e})")

if __name__ == "__main__":
    main()
