#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""scripts/compute_v19.py — вычислительный прогон кампании V19.

V19 · сшивка ветвей алгебраической функции (дорожная карта R2):
      механизм hodge-laboratory (Ферма-накрытие, фазовый закон
      ζ^{ra+sb}, ортогональность характеров) перенесён на ПОЛНУЮ
      алгебраическую функцию критической прямой Z_id(t) = e^{iθ}ζ(½+it).

Слои: A (эталон) → B (Z₂-монодромия и аргументное замыкание) →
      C (Γ-фаза как носитель двойной структуры) → D (регрессия R1–R4).

Запуск: python3 scripts/compute_v19.py [full|fast]
Результат: data/v19_verdict.json, data/v19_stitch_log.csv
"""
import csv
import json
import os
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

DATA = os.path.join(ROOT, 'data')
FULL = '--fast' not in sys.argv


def save(name, obj):
    p = os.path.join(DATA, name)
    with open(p, 'w', encoding='utf-8') as f:
        json.dump(obj, f, ensure_ascii=False, indent=1, default=float)
    print(f'  -> {name}')


def main():
    from rpbridge.zeros import load_zeros
    zeros = load_zeros(nmax=100000 if FULL else 300)
    t00 = time.time()

    print('== V19 branch stitching of the algebraic function (R2) ==')
    t0 = time.time()
    from rpbridge import stitching
    r19 = stitching.run(zeros, full=FULL)
    save('v19_verdict.json', r19)
    rows = []
    for case in r19['layer_A']['closed_form']['cases']:
        rows.append(dict(layer='A', a=case['a'], b=case['b'],
                         r=case['r'], s=case['s'],
                         period_exact=case['period_exact'],
                         resid_rel=case['resid_rel']))
    for row in r19['layer_C']['spectral_report']['rows']:
        rows.append(dict(layer='C', a='', b='', r='', s='',
                         period_exact='',
                         resid_rel=row['r_align']))
    with open(os.path.join(DATA, 'v19_stitch_log.csv'), 'w', newline='',
              encoding='utf-8') as f:
        wr = csv.DictWriter(f, fieldnames=['layer', 'a', 'b', 'r', 's',
                                           'period_exact', 'resid_rel'])
        wr.writeheader()
        wr.writerows(rows)
    print(f'  -> v19_stitch_log.csv ({time.time() - t0:.1f} s total '
          f'{time.time() - t00:.1f} s)')
    print(f"  verdict: {r19['stitch_verdict']}")


if __name__ == '__main__':
    main()
