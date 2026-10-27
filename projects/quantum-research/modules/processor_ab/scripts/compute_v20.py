#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""compute_v20.py — свежий полный пересчёт кампании V20.

Исполняет процессорную спецификацию AB-облака (P0 программы
«AB-процессор», предрегистрированной в results/PROCESSOR_PROGRAM.md
материнского пакета AB Research Program):

  · компилятор (главные, предрегистрированные метрики V20):
    M = 200 унитарных 4×4 (сид 96), порог fidelity ≥ 1−1e-12;
    M2 = 100 унитарных 8×8 (сид 296), порог ≥ 1−1e-10;
    контроли: identity, permutation, DFT 4×4, CL(2);
    бит-в-бит воспроизводимость;
  · превью-слои следующих фаз (честно помечены как предварительные):
    память P1 (RAM 64/64, латентность), ALU V22 (256/256),
    считывание нулей V23 (аргументная намотка, без таблицы),
    нелокальность V24 (голономия, no-signaling).

Выход: data/v20_verdict.json (+ копия в computations/).
Запуск: python3 scripts/compute_v20.py
"""
import json
import os
import sys
import time

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from rpbridge import alu, compiler as C, isa, memory            # noqa: E402
from rpbridge import nonlocality as NL                          # noqa: E402
from rpbridge import riemann_reader as RR                       # noqa: E402

DATE = '2026-10-11'
SEED_MAIN = 96
SEED_M2 = 296
THR4 = 1e-12
THR8 = 1e-10


def controls():
    dft4 = np.array([[np.exp(2j * np.pi * j * k / 4) / 2
                      for k in range(4)] for j in range(4)])
    h = isa.ab2(np.pi / 2, 0.0, np.pi) * np.exp(-1j * np.pi / 4)
    cl2 = (np.kron(h, np.eye(2, dtype=complex)) @ isa.cnot()
           @ np.kron(np.eye(2, dtype=complex), h)
           @ np.kron(isa.rz(np.pi / 2), np.eye(2, dtype=complex)))
    return {
        'identity': np.eye(4, dtype=complex),
        'permutation': np.roll(np.eye(4, dtype=complex), 1, axis=0),
        'dft4': dft4,
        'cl2': cl2,
    }


def compile_suite(dim, n, count, seed):
    rng = np.random.default_rng(seed)
    Fs, one_minus, gates, twoq = [], [], [], []
    for _ in range(count):
        U = C.haar_unitary(rng, dim)
        comp = C.compile_unitary(U, n)
        F = C.fidelity(U, C.program_matrix(comp, n))
        Fs.append(F)
        one_minus.append(max(0.0, 1.0 - F))
        gates.append(comp['costs']['n_gates'])
        twoq.append(comp['costs']['two_qubit_equiv'])
    return dict(n=count, seed=seed, threshold=(THR4 if dim == 4 else THR8),
                min_fidelity=float(min(Fs)),
                mean_fidelity=float(np.mean(Fs)),
                max_one_minus_F=float(max(one_minus)),
                gates_max=int(max(gates)), gates_mean=float(np.mean(gates)),
                two_qubit_equiv_max=int(max(twoq)),
                passed=bool(max(one_minus) <= (THR4 if dim == 4 else THR8)))


def bit_exact_replay():
    def once():
        rng = np.random.default_rng(SEED_MAIN)
        acc = []
        for _ in range(30):
            U = C.haar_unitary(rng, 4)
            comp = C.compile_unitary(U, 2)
            acc.append(C.program_matrix(comp, 2).view(np.float64))
        return np.concatenate(acc)
    a, b = once(), once()
    return bool(np.array_equal(a, b))


def run():
    t0 = time.time()
    print('== V20 compute: AB processor compiler (P0) ==')

    m4 = compile_suite(4, 2, 200, SEED_MAIN)
    print(f"  4x4: n=200, min F = 1-{m4['max_one_minus_F']:.2e} "
          f"(thr 1e-12): {'PASS' if m4['passed'] else 'FAIL'}")
    m8 = compile_suite(8, 3, 100, SEED_M2)
    print(f"  8x8: n=100, min F = 1-{m8['max_one_minus_F']:.2e} "
          f"(thr 1e-10): {'PASS' if m8['passed'] else 'FAIL'}")

    ctrl_out = {}
    for name, U in controls().items():
        comp = C.compile_unitary(U, 2)
        ctrl_out[name] = C.fidelity(U, C.program_matrix(comp, 2))
    replay = bit_exact_replay()
    print(f"  controls: {', '.join(f'{k}={v:.15f}' for k, v in ctrl_out.items())}")
    print(f"  bit-exact replay: {replay}")

    print('  previews: memory / ALU / reading / nonlocality ...')
    ram = memory.ram_test()
    lat = memory.latency_model()
    pw = memory.phase_word_demo()
    alu_res = alu.run_alu()
    reading = RR.read_zeros(t0=2.0, t1=58.0, M=560, refine=17)
    acc = RR.storage_accounting(reading['zeros_reference'])
    nl = NL.run()

    compiler_passed = bool(m4['passed'] and m8['passed']
                           and all(1 - v <= 1e-13 for v in ctrl_out.values())
                           and replay)
    previews_passed = bool(
        ram['bit_exact'] and lat['passed'] and pw['exact_words'] == 256
        and all(v['bit_exact'] for v in alu_res.values())
        and reading['passed'] and nl['interferometer']['passed']
        and nl['protection']['passed'] and nl['cross_phase']['passed']
        and nl['chsh']['chsh_passed'] and nl['chsh']['no_signaling'])

    verdict = dict(
        meta=dict(package='AB Quantum Processor Program',
                  campaign='V20',
                  name='AB processor compiler: ISA → exact compilation '
                       '(program phase P0)',
                  seeds=dict(main=SEED_MAIN, m2=SEED_M2),
                  date=DATE,
                  source='results/PROCESSOR_PROGRAM.md (mother package '
                         'AB Research Program 1.2.1), pre-registered'),
        isa=dict(primitives=isa.isa_table(),
                 calibration={k: dict(fidelity=v['fidelity'],
                                      t_pulse=float(v['t_pulse']))
                              for k, v in isa.pulse_calibration().items()},
                 fixed_gate_base='V18: {X,Y,Z,H,S,T} fidelity 1−2e-16'),
        compiler=dict(
            mechanism='Givens QR → two-level AB2 blocks + level-PHASE '
                      'ladder; closed form, no optimization',
            m4=m4, m8=m8,
            controls=ctrl_out,
            bit_exact_replay=replay,
            passed=compiler_passed),
        previews=dict(
            status='PRELIMINARY — пороги этих слоёв предрегистрированы '
                   'для фаз P1–P3; здесь фиксируются первые измерения',
            memory_P1=dict(ram=ram, latency=lat, phase_word=pw,
                           capacity=memory.capacity_table()),
            alu_V22=alu_res,
            reading_V23={**reading, 'storage': acc},
            nonlocality_V24=nl),
        summary=dict(compiler=compiler_passed, previews=previews_passed,
                     processor_p0=bool(compiler_passed and previews_passed)),
        verdict_note=dict(
            ru=('ПРОЦЕССОРНАЯ СПЕЦИФИКАЦИЯ ИСПОЛНЕНА (P0): любая '
                'унитарная логика 4×4/8×8 компилируется в ISA AB-облака '
                'точно (машинный пол), контроли точны, повтор бит-в-бит; '
                'превью памяти/ALU/считывания/нелокальности согласованы '
                'с предрегистрированными порогами P1–P3'),
            en=('PROCESSOR SPECIFICATION EXECUTED (P0): arbitrary 4×4/8×8 '
                'unitary logic compiles exactly into the AB-cloud ISA '
                '(machine floor), controls exact, bit-exact replay; '
                'memory/ALU/reading/nonlocality previews match the '
                'pre-registered P1–P3 thresholds')),
        runtime_s=round(time.time() - t0, 1))

    os.makedirs(os.path.join(ROOT, 'data'), exist_ok=True)
    out = os.path.join(ROOT, 'data', 'v20_verdict.json')
    with open(out, 'w', encoding='utf-8') as f:
        json.dump(verdict, f, ensure_ascii=False, indent=1)
    print(f"  verdict: {out} ({verdict['runtime_s']} s)")
    print('  P0 verdict:', 'PROCESSOR_SPEC_EXECUTED'
          if verdict['summary']['processor_p0'] else 'FAILED')
    return verdict


if __name__ == '__main__':
    run()
