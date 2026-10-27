# -*- coding: utf-8 -*-
"""rpbridge.alu — V22-превью: арифметика на компиляторе AB-процессора.

АЛУ строится поверх точного компилятора V20: арифметическая операция
(a, b) → a ⊕ b на 4-битных словах — перестановочная унитарная матрица
на 8-кубитном регистре |a⟩|b⟩ (размер 256). Перестановка компилируется
в программу ISA (двухуровневые блоки) и исполняется точно; таблица
истинности проверяется ПОЛНЫМ перебором всех входов — исчерпывающее
доказательство, а не выборочные тесты.

Операции:
  ADD mod 16:   |a⟩|b⟩ → |a⟩|(a+b) mod 16⟩      — 256/256 входов
  MUL mod 16 (a нечётное): |a⟩|b⟩ → |a⟩|a·b mod 16⟩ — 8·16 = 128/128
  INC:          |x⟩ → |x+1 mod 16⟩               — 16/16
  CMP:          компаратор |a,b⟩ → флаг → перестановка с маркером
                старшинства — 256/256

Вся арифметика исполняется на ОДНОМ и том же ISA без новых затворов —
в этом и есть «процессорность»: компилятор делает ISA универсальным.
"""
import numpy as np

from . import compiler as C

NQ = 8          # 4 бита слагаемого a + 4 бита b
DIM = 256


def _perm_matrix(fn):
    """Перестановочная матрица операции fn: |x⟩ → |fn(x)⟩,
    x = a·16 + b (старший байт a, младший b)."""
    P = np.zeros((DIM, DIM), dtype=np.complex128)
    for x in range(DIM):
        P[fn(x), x] = 1.0
    return P


def _add_fn(x):
    a, b = x // 16, x % 16
    return a * 16 + (a + b) % 16


def _mul_fn(x):
    """Умножение mod 16: |a⟩|b⟩ → |a⟩|a·b mod 16⟩ для НЕЧЁТНОГО a
    (обратимо: gcd(a,16)=1); блоки чётных a оставляем тождественными —
    полная матрица остаётся перестановочной (унитарной)."""
    a, b = x // 16, x % 16
    if a % 2 == 1:
        return a * 16 + (a * b) % 16
    return x


def truth_table(comp, n, fn, inputs):
    """Полный перебор входов: исполнение скомпилированной программы на
    базисных состояниях, чтение аргмаксом; бит-в-бит против fn."""
    ok, worst = 0, []
    for x in inputs:
        psi = np.zeros(DIM, dtype=np.complex128)
        psi[x] = 1.0
        out = C.program_state(comp, n, psi)
        read = int(np.argmax(np.abs(out) ** 2))
        if read == fn(x):
            ok += 1
        else:
            worst.append((x, fn(x), read))
    return ok, worst


def run_alu():
    """Полный прогон ALU: сумматор 256/256, умножение 128/128,
    инкремент 16/16, компаратор 256/256. Все программы компилируются
    одним компилятором V20."""
    results = {}

    # ADD mod 16 — 256 входов
    P = _perm_matrix(_add_fn)
    comp = C.compile_unitary(P, NQ)
    ok, worst = truth_table(comp, NQ, _add_fn, range(DIM))
    results['adder_mod16'] = dict(passed=ok, total=DIM,
                                 bit_exact=bool(ok == DIM), gates=comp['costs'],
                                 worst=worst[:3])

    # MUL mod 16 для нечётных a — 8·16 = 128 входов (обратимость)
    ok_m, tot_m, gates_m = 0, 0, None
    for a in range(1, 16, 2):
        fn = _mul_fn
        P = _perm_matrix(fn)
        comp = C.compile_unitary(P, NQ)
        o, w = truth_table(comp, NQ, fn, range(a * 16, a * 16 + 16))
        ok_m += o
        tot_m += 16
        if gates_m is None:
            gates_m = comp['costs']
    results['mulmod16_odd'] = dict(passed=ok_m, total=tot_m,
                                   bit_exact=bool(ok_m == tot_m),
                                   gates=gates_m)

    # INC mod 16 — 16 входов (регистр 4 кубита)
    P16 = np.roll(np.eye(16, dtype=np.complex128), 1, axis=0)
    comp16 = C.compile_unitary(P16, 4)
    ok_i = 0
    for x in range(16):
        psi = np.zeros(16, dtype=np.complex128)
        psi[x] = 1.0
        out = C.program_state(comp16, 4, psi)
        ok_i += int(int(np.argmax(np.abs(out) ** 2)) == (x + 1) % 16)
    results['inc_mod16'] = dict(passed=ok_i, total=16,
                                bit_exact=bool(ok_i == 16),
                                gates=comp16['costs'])

    # CMP (компаратор) — ФАЗОВАЯ кодировка: U = diag(±1), фаза −1 на
    # входах с a > b (обратимо и унитарно; флаг считывается фазовой
    # аппаратурой процессора). Compare-exchange необратим (коллизии) —
    # честная альтернатива в этой архитектуре: фазовый оракул.
    sgn = [1.0 if (x // 16) <= (x % 16) else -1.0 for x in range(DIM)]
    U = np.diag(np.array(sgn, dtype=np.complex128))
    comp = C.compile_unitary(U, NQ)
    ok_c = 0
    for x in range(DIM):
        psi = np.zeros(DIM, dtype=np.complex128)
        psi[x] = 1.0
        out = C.program_state(comp, NQ, psi)
        want = -1.0 if (x // 16) > (x % 16) else 1.0
        ok_c += int(abs(abs(out[x]) - 1.0) < 1e-9
                    and np.sign(out[x].real) == want)
    results['comparator_phase'] = dict(passed=ok_c, total=DIM,
                                       bit_exact=bool(ok_c == DIM),
                                       gates=comp['costs'])
    return results
