# -*- coding: utf-8 -*-
import os
import sys

import numpy as np
import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

# Модуль 'rpbridge' существует в двух пакетах (core_spectrum и processor_ab).
# При сборе всех тестов одним процессом (pytest от корня) чужой пакет может
# уже лежать в sys.modules — сбрасываем, чтобы импорт взял свой.
for _m in [m for m in sys.modules if m == "rpbridge" or m.startswith("rpbridge.")]:
    del sys.modules[_m]

from rpbridge import alu, compiler as C, isa, memory            # noqa: E402
from rpbridge import nonlocality as NL                          # noqa: E402


# ── ISA ─────────────────────────────────────────────────────────────────────
def test_isa_unitarity():
    rng = np.random.default_rng(7)
    for phi in rng.uniform(0, 2 * np.pi, 20):
        for g in (isa.rz(phi), isa.rx(phi), isa.ab2(phi, phi / 2, phi / 3)):
            assert np.max(np.abs(g.conj().T @ g - np.eye(2))) < 1e-14
    for phi in rng.uniform(0, 2 * np.pi, 10):
        assert np.max(np.abs(isa.cphase(phi).conj().T @ isa.cphase(phi)
                             - np.eye(4))) < 1e-14


def test_isa_fixed_gates_match_v18():
    """Фиксированные ворота V18 воспроизводятся примитивами ISA
    (с точностью до глобальной фазы — физика от неё не зависит)."""
    def phase_fid(g, target):
        return abs(np.trace(g.conj().T @ target)) / 2
    X = np.array([[0, 1], [1, 0]], dtype=complex)
    Z = np.diag([1.0, -1.0])
    S = np.diag([1, 1j]).astype(complex)
    assert abs(phase_fid(isa.rx(np.pi), X) - 1) < 1e-14     # RX(π) ∝ X
    assert abs(phase_fid(isa.rz(np.pi), Z) - 1) < 1e-14     # RZ(π) ∝ Z
    assert abs(phase_fid(isa.rz(np.pi / 2), S) - 1) < 1e-14  # RZ(π/2) ∝ S


def test_pulse_calibration():
    cal = isa.pulse_calibration()
    for name, r in cal.items():
        assert r['fidelity'] >= 1 - 1e-14, name


def test_embed_2q_cnot():
    """Встроенный CNOT: контроль = кубит qa, цель = qb (флип цели при
    контроле 1); проверка на всех 4 базисных состояниях."""
    U = isa.embed_2q(2, 0, 1, isa.cnot())
    expected = np.eye(4, dtype=complex)
    expected[[1, 3]] = expected[[3, 1]]      # обмен |01⟩ ↔ |11⟩ (флип бита 1)
    assert np.max(np.abs(U - expected)) < 1e-14
    # унитарность встраивания на n=4 с произвольной парой
    U4 = isa.embed_2q(4, 1, 3, isa.cphase(0.7))
    assert np.max(np.abs(U4.conj().T @ U4 - np.eye(16))) < 1e-14


# ── компилятор ──────────────────────────────────────────────────────────────
@pytest.mark.parametrize('seed,dim,n', [(1, 4, 2), (2, 4, 2), (3, 8, 3),
                                        (4, 16, 4), (5, 8, 3)])
def test_compile_haar_exact(seed, dim, n):
    U = C.haar_unitary(np.random.default_rng(seed), dim)
    comp = C.compile_unitary(U, n)
    F = C.fidelity(U, C.program_matrix(comp, n))
    assert F >= 1 - 1e-13


def test_compile_thresholds_full_protocol():
    """Главные предрегистрированные метрики V20: 200×4×4 (сид 96) и
    100×8×8 (сид 296) — пороги 1e-12 / 1e-10."""
    rng = np.random.default_rng(96)
    worst4 = max(1 - C.fidelity(U, C.program_matrix(C.compile_unitary(U, 2), 2))
                 for U in (C.haar_unitary(rng, 4) for _ in range(200)))
    rng = np.random.default_rng(296)
    worst8 = max(1 - C.fidelity(U, C.program_matrix(C.compile_unitary(U, 3), 3))
                 for U in (C.haar_unitary(rng, 8) for _ in range(100)))
    assert worst4 <= 1e-12
    assert worst8 <= 1e-10


def test_controls_exact():
    dft4 = np.array([[np.exp(2j * np.pi * j * k / 4) / 2
                      for k in range(4)] for j in range(4)])
    h = isa.ab2(np.pi / 2, 0.0, np.pi) * np.exp(-1j * np.pi / 4)
    cl2 = (np.kron(h, np.eye(2, dtype=complex)) @ isa.cnot()
           @ np.kron(np.eye(2, dtype=complex), h)
           @ np.kron(isa.rz(np.pi / 2), np.eye(2, dtype=complex)))
    for U in (np.eye(4, dtype=complex),
              np.roll(np.eye(4, dtype=complex), 1, axis=0),
              dft4, cl2):
        comp = C.compile_unitary(U, 2)
        assert C.fidelity(U, C.program_matrix(comp, 2)) >= 1 - 1e-13


def test_bit_exact_replay():
    def once():
        rng = np.random.default_rng(96)
        return np.concatenate([
            C.program_matrix(C.compile_unitary(C.haar_unitary(rng, 4), 2), 2)
            .view(np.float64) for _ in range(10)])
    assert np.array_equal(once(), once())


def test_program_state_matches_matrix():
    U = C.haar_unitary(np.random.default_rng(11), 8)
    comp = C.compile_unitary(U, 3)
    psi0 = C.haar_unitary(np.random.default_rng(12), 8)[:, 0]
    psi = C.program_state(comp, 3, psi0)
    V = C.program_matrix(comp, 3)
    assert np.max(np.abs(psi - V @ psi0)) < 1e-13


# ── память ──────────────────────────────────────────────────────────────────
def test_ram_full_enumeration():
    r = memory.ram_test()
    assert r['bit_exact'] and r['read_back'] == 64


def test_latency_threshold():
    lm = memory.latency_model()
    assert lm['b'] <= 6 and lm['passed']


def test_phase_word():
    pw = memory.phase_word_demo()
    assert pw['exact_words'] == 256


# ── ALU ─────────────────────────────────────────────────────────────────────
def test_alu_full_truth_tables():
    res = alu.run_alu()
    assert res['adder_mod16']['passed'] == 256
    assert res['mulmod16_odd']['passed'] == 128
    assert res['inc_mod16']['passed'] == 16
    assert res['comparator_phase']['passed'] == 256
    assert all(v['bit_exact'] for v in res.values())


# ── нелокальность ───────────────────────────────────────────────────────────
def test_nonlocality_suite():
    r = NL.run()
    assert r['interferometer']['passed']
    assert r['protection']['passed']
    assert r['protection']['protected'] == 1000
    assert r['cross_phase']['passed']
    assert r['chsh']['chsh_passed'] and r['chsh']['S'] >= 2.8
    assert r['chsh']['no_signaling']


def test_no_signaling_algebra():
    """Маргинал инвариантен к локальной унитарной — общий факт,
    проверяется на AB-состоянии пары."""
    psi = np.array([1, 1, 1, np.exp(1j * 1.3)], dtype=complex) / 2
    rho = np.outer(psi, psi.conj())
    A2 = isa.rx(0.7)
    rho2 = np.kron(np.eye(2), A2) @ rho @ np.kron(np.eye(2), A2).conj().T
    r1 = rho.reshape(2, 2, 2, 2).trace(axis1=3, axis2=1)
    r2 = rho2.reshape(2, 2, 2, 2).trace(axis1=3, axis2=1)
    assert np.max(np.abs(r1 - r2)) < 1e-14
