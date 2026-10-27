#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""compute_all.py — диспетчер пересчёта всех кампаний пакета.

v0.1.0: единственная кампания V20 → scripts/compute_v20.py.
Запуск: python3 scripts/compute_all.py [v20]
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CAMPAIGNS = {
    'v20': 'compute_v20.py',
}


def main():
    only = [a.lower() for a in sys.argv[1:]] or list(CAMPAIGNS)
    for key in only:
        if key not in CAMPAIGNS:
            print(f'неизвестная кампания: {key}')
            return 1
        script = os.path.join(HERE, CAMPAIGNS[key])
        print(f'--- {key} → {CAMPAIGNS[key]}')
        r = subprocess.run([sys.executable, script])
        if r.returncode != 0:
            return r.returncode
    print('ALL CAMPAIGNS RECOMPUTED OK (AB Quantum Processor 0.1.0)')
    return 0


if __name__ == '__main__':
    sys.exit(main())
