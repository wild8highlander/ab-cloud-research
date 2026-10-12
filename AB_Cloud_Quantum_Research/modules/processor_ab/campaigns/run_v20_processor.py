#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Кампания V20 — компилятор AB-процессора (P0 программы «AB-процессор»).
Печатает закоммиченный вердикт. Свежий пересчёт: scripts/compute_v20.py
"""
import json
import os


def main():
    R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    d = json.load(open(os.path.join(R, 'data', 'v20_verdict.json'),
                       encoding='utf-8'))
    print('== V20 AB processor compiler (P0) ==')
    c = d['compiler']
    m4, m8 = c['m4'], c['m8']
    print(f"  [compiler] 4x4: n={m4['n']}, min F = 1-{m4['max_one_minus_F']:.1e}"
          f" (thr 1e-12): {'PASS' if m4['passed'] else 'FAIL'};"
          f" gates ≤ {m4['gates_max']}, 2q-equiv ≤ {m4['two_qubit_equiv_max']}")
    print(f"  [compiler] 8x8: n={m8['n']}, min F = 1-{m8['max_one_minus_F']:.1e}"
          f" (thr 1e-10): {'PASS' if m8['passed'] else 'FAIL'};"
          f" gates ≤ {m8['gates_max']}, 2q-equiv ≤ {m8['two_qubit_equiv_max']}")
    print('  [controls] ' + ', '.join(
        f"{k} = {v:.15f}" for k, v in c['controls'].items()))
    print(f"  [replay]   bit-exact: {c['bit_exact_replay']}")
    p = d['previews']
    mem = p['memory_P1']
    print(f"  [P1 RAM]   {mem['ram']['read_back']}/{mem['ram']['patterns']} "
          f"бит-в-бит; латентность b = {mem['latency']['b']:.1f} "
          f"(порог V21 ≤ 6); фазовые слова "
          f"{mem['phase_word']['exact_words']}/{mem['phase_word']['N']}")
    print('  [V22 ALU]  ' + ', '.join(
        f"{k}: {v['passed']}/{v['total']}" for k, v in p['alu_V22'].items()))
    rd = p['reading_V23']
    print(f"  [V23 read] нулей считано {rd['zeros_read']} "
          f"(контроль {rd['zeros_reference']}, {'EXACT' if rd['count_exact'] else 'MISMATCH'}), "
          f"макс. отклонение {rd['max_position_dev']:.2e}; "
          f"хранение: {rd['storage']['stored_zeros']} нулей, "
          f"{rd['storage']['stored_formula_constants']} констант формулы")
    nl = p['nonlocality_V24']
    print(f"  [V24 nl]   интерферометр {nl['interferometer']['max_resid']:.1e}; "
          f"защита {nl['protection']['protected']}/"
          f"{nl['protection']['n_seeds']}; CHSH S = {nl['chsh']['S']:.4f}; "
          f"коммутаторы {nl['chsh']['comm_max']:.1e}")
    print(f"  P0 verdict: "
          f"{'PROCESSOR_SPEC_EXECUTED' if d['summary']['processor_p0'] else 'FAILED'}")


if __name__ == '__main__':
    main()
