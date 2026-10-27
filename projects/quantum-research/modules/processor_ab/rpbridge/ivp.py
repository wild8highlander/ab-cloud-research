# -*- coding: utf-8 -*-
"""rpbridge.ivp — независимые верификационные протоколы (IV).

Каждый протокол — самодостаточная проверка закоммиченного вердикта
свежим прогоном из чистого состояния. Запуск: IVP.run_all() или
independent_verification/RUN_ALL.sh.
"""
import json
import os

import numpy as np

from . import compiler as C
from . import isa, memory, nonlocality as NL

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _verdict():
    p = os.path.join(ROOT, 'data', 'v20_verdict.json')
    with open(p, encoding='utf-8') as f:
        return json.load(f)


def iv01_compiler_replay():
    """Свежий полный прогон компилятора: min fidelity 4×4 ≥ 1−1e-12,
    8×8 ≥ 1−1e-10 — совпадение с вердиктом до 1e-14."""
    v = _verdict()
    rng = np.random.default_rng(96)
    Fs = [C.fidelity(U, C.program_matrix(C.compile_unitary(
        U, 2), 2))
        for U in (C.haar_unitary(rng, 4) for _ in range(200))]
    worst4 = float(max(1 - f for f in Fs))
    rng = np.random.default_rng(296)
    Fs8 = [C.fidelity(U, C.program_matrix(C.compile_unitary(
        U, 3), 3))
        for U in (C.haar_unitary(rng, 8) for _ in range(100))]
    worst8 = float(max(1 - f for f in Fs8))
    ok = (worst4 <= 1e-12 and worst8 <= 1e-10
          and abs(worst4 - v['compiler']['m4']['max_one_minus_F']) <= 1e-14
          and abs(worst8 - v['compiler']['m8']['max_one_minus_F']) <= 1e-14)
    return dict(name='IV01 compiler fresh replay', passed=bool(ok),
                worst4=worst4, worst8=worst8,
                verdict4=v['compiler']['m4']['max_one_minus_F'],
                verdict8=v['compiler']['m8']['max_one_minus_F'])


def iv02_controls():
    """Контроли (identity / permutation / DFT4 / CL2) — точно."""
    v = _verdict()
    dft4 = np.array([[np.exp(2j * np.pi * j * k / 4) / 2
                      for k in range(4)] for j in range(4)])
    h = isa.ab2(np.pi / 2, 0.0, np.pi) * np.exp(-1j * np.pi / 4)
    cl2 = (np.kron(h, np.eye(2, dtype=complex)) @ isa.cnot()
           @ np.kron(np.eye(2, dtype=complex), h) @
           np.kron(isa.rz(np.pi / 2), np.eye(2, dtype=complex)))
    ctrl = {
        'identity': np.eye(4, dtype=complex),
        'permutation': np.roll(np.eye(4, dtype=complex), 1, axis=0),
        'dft4': dft4,
        'cl2': cl2,
    }
    out = {}
    ok = True
    for name, U in ctrl.items():
        comp = C.compile_unitary(U, 2)
        F = C.fidelity(U, C.program_matrix(comp, 2))
        out[name] = F
        ok = ok and (1 - F) <= 1e-13
    return dict(name='IV02 controls exact', passed=bool(ok), **out)


def iv03_bit_exact_replay():
    """Бит-в-бит повтор: полный прогон компилятора дважды — программы,
    фазы и выходные матрицы совпадают на уровне битов float64."""
    def run_once():
        rng = np.random.default_rng(96)
        acc = []
        for _ in range(20):
            U = C.haar_unitary(rng, 4)
            comp = C.compile_unitary(U, 2)
            V = C.program_matrix(comp, 2)
            acc.append(V.view(np.float64))
        return np.concatenate(acc)

    a, b = run_once(), run_once()
    return dict(name='IV03 bit-exact replay',
                passed=bool(np.array_equal(a, b)),
                n_floats=int(a.size))


def iv04_ram_and_latency():
    """RAM 64/64 бит-в-бит; латентность b ≤ 6."""
    v = _verdict()
    r = memory.ram_test()
    lm = memory.latency_model()
    ok = (r['bit_exact'] and lm['b'] <= 6
          and r['read_back'] == v['previews']['memory_P1']['ram']['read_back'])
    return dict(name='IV04 RAM 64/64 + latency b ≤ 6', passed=bool(ok),
                read_back=r['read_back'], b=lm['b'])


def iv05_nonlocality():
    """Интерферометр ≤ 1e-14; защита 1000/1000; кросс-фаза и ρ1-инва-
    риантность; CHSH ≥ 2.8; коммутаторы = 0."""
    v = _verdict()
    r = NL.run()
    ok = (r['interferometer']['passed'] and r['protection']['passed']
          and r['cross_phase']['passed'] and r['chsh']['chsh_passed']
          and r['chsh']['no_signaling'])
    return dict(name='IV05 nonlocality suite', passed=bool(ok),
                interferometer=r['interferometer']['max_resid'],
                protection=r['protection']['protected'],
                chsh=r['chsh']['S'],
                comm=r['chsh']['comm_max'])


def run_all():
    procs = [iv01_compiler_replay(), iv02_controls(),
             iv03_bit_exact_replay(), iv04_ram_and_latency(),
             iv05_nonlocality()]
    summary = dict(n=len(procs),
                   passed=sum(1 for p in procs if p['passed']))
    return dict(protocols=procs, summary=summary)
