#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""scripts/compute_v161718.py — вычислительный прогон кампаний V16–V18.

V16 · полный гамильтониан × полная алгебраическая функция критической
      прямой (Γ-лестница, θ-фазовый вес, карта 96 конфигураций);
V17 · электрон на критической прямой (волновод 96×24, ζ/случайное/чистое);
V18 · AB-оператор как процессор (ворота, зацепление, игра AB-Pong).

Запуск: python3 scripts/compute_v161718.py [full|fast]
Результаты: data/v16_verdict.json, data/v17_verdict.json,
            data/v18_verdict.json, data/v16_rows.csv, data/v17_trajectories.csv
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

    # ── V16 ──────────────────────────────────────────────────────────────
    print('== V16 full hamiltonian x full algebraic function ==')
    t0 = time.time()
    from rpbridge import fullham
    r16 = fullham.run(zeros, full=FULL)
    save('v16_verdict.json', r16)
    with open(os.path.join(DATA, 'v16_rows.csv'), 'w', newline='',
              encoding='utf-8') as f:
        wr = csv.DictWriter(f, fieldnames=list(r16['best'].keys()))
        wr.writeheader()
        for row in r16['rows']:
            wr.writerow(row)
    print(f'  -> v16_rows.csv  ({time.time() - t0:.1f} s)')

    # ── V17 ──────────────────────────────────────────────────────────────
    print('== V17 electron on the critical line ==')
    t0 = time.time()
    from rpbridge import electron
    r17 = electron.run(zeros, full=FULL)
    save('v17_verdict.json', r17)
    with open(os.path.join(DATA, 'v17_trajectories.csv'), 'w', newline='',
              encoding='utf-8') as f:
        wr = csv.writer(f)
        wr.writerow(['t', 'x_clean', 'y_clean', 'x_random', 'y_random',
                     'x_zeta', 'y_zeta', 'C_clean', 'C_random', 'C_zeta'])
        n = len(r17['modes']['clean']['traj']['t'])
        for j in range(n):
            wr.writerow([r17['modes']['clean']['traj']['t'][j],
                         r17['modes']['clean']['traj']['x'][j],
                         r17['modes']['clean']['traj']['y'][j],
                         r17['modes']['random']['traj']['x'][j],
                         r17['modes']['random']['traj']['y'][j],
                         r17['modes']['zeta']['traj']['x'][j],
                         r17['modes']['zeta']['traj']['y'][j],
                         r17['modes']['clean']['traj']['C'][j],
                         r17['modes']['random']['traj']['C'][j],
                         r17['modes']['zeta']['traj']['C'][j]])
    print(f'  -> v17_trajectories.csv  ({time.time() - t0:.1f} s)')

    # ── V18 ──────────────────────────────────────────────────────────────
    print('== V18 AB operator as processor ==')
    t0 = time.time()
    from rpbridge import processor
    r18 = processor.run()
    save('v18_verdict.json', r18)
    # лог партии — отдельный файл (данные игры)
    game = processor.play_pong(serve_right=True)
    with open(os.path.join(DATA, 'v18_pong_log.csv'), 'w', newline='',
              encoding='utf-8') as f:
        wr = csv.writer(f)
        wr.writerow(['t', 'event'])
        for row in game['log']:
            wr.writerow(row)
    print(f'  -> v18_pong_log.csv  ({time.time() - t0:.1f} s)')

    print(f'ALL V16-V18 DONE in {time.time() - t00:.1f} s')


if __name__ == '__main__':
    main()
