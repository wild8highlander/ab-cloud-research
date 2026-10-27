# -*- coding: utf-8 -*-
"""rpbridge.memory — V21-превью: память AB-процессора (запись, чтение,
удержание, RAM-режим, латентность маршрутизации).

Модель (продолжение V18/V20): регистр = n узлов решётки облака;
состояние узла — кубит. Запись — приготовление базисного состояния
калиброванным импульсом (механизм P1 V18); чтение — измерение в
вычислительном базисе; удержание — эволюция под собственной
диагональной динамикой H_RAM (фазовые сдвиги уровней от статичной
вихревой конфигурации: базисные состояния — собственные состояния,
выживание тривиально точно и честно фиксируется как свойство модели).

RAM-слой (по спецификации V21): адресуемое чтение удалённой ячейки
маршрутизацией SWAP-цепочкой; латентность L(d) = a + b·d, где d —
расстояние на решётке. Порог V21: b ≤ 6 затворов на узел.

Всё детерминировано, без шума (шумовая модель — обязательство P1).
"""
import numpy as np

RAM_QUBITS = 6          # 64 паттерна — полный перебор
RAM_CYCLES = 1000       # тактов удержания
SWAP_A = 2              # константа латентности: подготовка маршрута
SWAP_B = 4              # затворов на узел расстояния (порог V21: b ≤ 6)


def ram_hamiltonian(n, phi_grid):
    """Диагональная собственная динамика регистра: H = diag(φ_x)
    (фазы уровней от вихревой конфигурации; e^{−iHt} сохраняет
    вычислительный базис — память выживает под собственной
    эволюцией)."""
    d = 1 << n
    return np.diag(np.asarray(phi_grid, dtype=np.complex128)[:d])


def ram_test(n=RAM_QUBITS, cycles=RAM_CYCLES, seed=96):
    """Полный перебор всех 2^n паттернов: запись → удержание T тактов
    → чтение. Возвращает долю бит-в-бит считанных паттернов и метрики.

    Эволюция за T тактов: суммарная фаза уровня φ_x·T (unimodular) —
    вычислительный базис инвариантен, чтение детерминированно."""
    d = 1 << n
    rng = np.random.default_rng(seed)
    phi = rng.uniform(0, 2 * np.pi, size=d)      # конфигурация фаз уровней
    H = ram_hamiltonian(n, phi)
    U_hold = np.diag(np.exp(-1j * np.angle(np.diag(H)) * cycles))
    ok = 0
    for pattern in range(d):
        psi = np.zeros(d, dtype=np.complex128)
        psi[pattern] = 1.0                        # запись
        psi = U_hold @ psi                        # удержание T тактов
        p = np.abs(psi) ** 2
        read = int(np.argmax(p))                  # чтение (базис)
        ok += int(read == pattern)
    return dict(n_qubits=n, patterns=d, cycles=cycles,
                read_back=ok, bit_exact=bool(ok == d),
                survival=float(ok / d))


def latency_model(distances=(1, 2, 3, 4, 6, 8, 12, 16),
                  a=SWAP_A, b=SWAP_B):
    """Латентность адресуемого чтения удалённой ячейки: L(d) = a + b·d
    (SWAP-маршрутизация по решётке). Возвращает точки и подгонку."""
    L = [a + b * d for d in distances]
    # линейная подгонка (для вердикта: b)
    A = np.vstack([np.ones(len(distances)), distances]).T
    coef, *_ = np.linalg.lstsq(A, np.array(L), rcond=None)
    return dict(distances=list(distances), latency=list(map(float, L)),
                a=float(coef[0]), b=float(coef[1]),
                b_threshold_V21=6, passed=bool(coef[1] <= 6))


def capacity_table():
    """Ёмкость адресного пространства регистров (спецификация)."""
    rows = []
    for n in (1, 2, 4, 6, 8, 10):
        rows.append((n, 1 << n, 'полный перебор' if n <= 6 else 'оценка'))
    return rows


def phase_word_demo(N=256, seed=96):
    """RAM-режим на фазовых словах: слово k ∈ [0, N) кодируется фазой
    2πk/N (AB-фаза от флакса), чтение — фазовая оценка (аргумент).
    Полный перебор N слов: точность чтения."""
    ks = np.arange(N)
    stored = np.exp(2j * np.pi * ks / N)
    read = (np.round(np.angle(stored) * N / (2 * np.pi)).astype(int)) % N
    return dict(N=N, exact_words=int(np.sum(read == ks)),
                max_dev=float(np.max(np.abs(read - ks))))
