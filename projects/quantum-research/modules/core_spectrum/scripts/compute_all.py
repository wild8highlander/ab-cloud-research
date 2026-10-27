#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""scripts/compute_all.py — полный вычислительный прогон V1–V15.

Реализует исследования по 15 решениям плана и записывает закоммиченные
вердикты в data/ (JSON) и таблицы (CSV). Запуск: python3 scripts/compute_all.py
Каждая кампания детерминирована (фиксированные seeds); файл нулей —
data/zeta_zeros_50000_embedded.txt (входит в пакет).
"""
import json
import os
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

import numpy as np  # noqa: E402

from rpbridge.zeros import load_zeros  # noqa: E402

DATA = os.path.join(ROOT, 'data')
DATE = '2026-10-10'


def save(name, obj):
    p = os.path.join(DATA, name)
    with open(p, 'w', encoding='utf-8') as f:
        json.dump(obj, f, ensure_ascii=False, indent=1, default=float)
    print(f'  -> {name}')


def csv_save(name, header, rows):
    import csv
    p = os.path.join(DATA, name)
    with open(p, 'w', newline='', encoding='utf-8') as f:
        wr = csv.writer(f)
        wr.writerow(header)
        wr.writerows(rows)
    print(f'  -> {name}')


def v01():
    from rpbridge.blind import run
    return run()


def v02():
    from rpbridge.nullmodels import run
    return run()


def v03(zeros):
    from rpbridge.critical_line import run
    return run(zeros)


def v04():
    from rpbridge.operator import run
    return run()


def v05():
    from rpbridge.limits import run
    return run()


def v06(zeros):
    from rpbridge.spectral_identity import run
    return run(zeros)


def v07(zeros):
    from rpbridge.arithmetic_trace import run
    return run(zeros)


def v08():
    from rpbridge.selfadjoint import run
    return run()


def v09():
    from rpbridge.symmetry import run
    return run()


def v10():
    from rpbridge.inverse import run
    return run()


def v11():
    from rpbridge.universality import run
    return run()


def v12():
    from rpbridge.intervalcert import run
    return run()


def v13():
    from rpbridge.formaloblig import run
    return run()


def v14():
    from rpbridge.audit import run
    return run()


def v15(zeros):
    from rpbridge.li import run
    return run(zeros)


def main():
    only = sys.argv[1:] or None
    z = None
    jobs = [('v01', 'blind spectrum'), ('v02', 'null models'),
            ('v03', 'critical line'), ('v04', 'operator passport'),
            ('v05', 'limit lattice'), ('v06', 'spectral identity'),
            ('v07', 'arithmetic trace'), ('v08', 'self-adjoint'),
            ('v09', 'symmetry reduction'), ('v10', 'inverse problem'),
            ('v11', 'universality split'), ('v12', 'interval certificates'),
            ('v13', 'formal bridge'), ('v14', 'claim audit'),
            ('v15', 'Li criterion')]
    # V16–V19 (v1.1.0/v1.2.0) вычисляются отдельными скриптами — единый прогон
    wanted = set(only) if only else {j[0] for j in jobs} | {'v16', 'v17', 'v18', 'v19'}
    if {'v16', 'v17', 'v18'} & wanted:
        import subprocess
        print('== V16–V18 (compute_v161718.py) ==')
        subprocess.run([sys.executable,
                        os.path.join(ROOT, 'scripts', 'compute_v161718.py')],
                       check=True, cwd=ROOT)
        jobs = [j for j in jobs if j[0] not in ('v16', 'v17', 'v18')]
        if only:
            only = [o for o in only if o not in ('v16', 'v17', 'v18')]
    if {'v19'} & wanted:
        import subprocess
        print('== V19 (compute_v19.py) ==')
        subprocess.run([sys.executable,
                        os.path.join(ROOT, 'scripts', 'compute_v19.py')],
                       check=True, cwd=ROOT)
        jobs = [j for j in jobs if j[0] != 'v19']
        if only:
            only = [o for o in only if o != 'v19']
            if not only:
                print('ALL REQUESTED CAMPAIGNS DONE')
                return
    for vid, title in jobs:
        if only and vid not in only:
            continue
        t0 = time.time()
        print(f'== {vid.upper()} {title} ==')
        if vid in ('v03', 'v06', 'v07', 'v15') and z is None:
            z = load_zeros()
        res = globals()[vid](z) if vid in ('v03', 'v06', 'v07', 'v15') \
            else globals()[vid]()
        res['meta'] = {'campaign': vid.upper(), 'date': DATE,
                       'package': 'AB Research Program 1.2.1',
                       'runtime_s': round(time.time() - t0, 1)}
        save(f'{vid}_verdict.json', res)
        print(f'  done in {res["meta"]["runtime_s"]} s')


if __name__ == '__main__':
    main()
