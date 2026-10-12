# -*- coding: utf-8 -*-
"""Тесты ядра вспомогательного исследования «машина без долговременной
памяти». Быстрые smoke-проверки инвариантов TS1–TS3 (полные прогоны —
кампании ES1–ES5 в experiments/)."""
import math
import os
import sys

import pytest

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HERE)

from spinor.core import MODELS, SpinorMachine, cycle_length, state_footprint  # noqa: E402
from spinor.tasks import LogMachine, modular_counter  # noqa: E402

TAU = 2.0 * math.pi


@pytest.mark.parametrize("name,theta", sorted(MODELS.items()))
def test_cycle_length(name, theta):
    m = SpinorMachine(theta)
    assert m.N == round(TAU / theta) == 2 * round(math.pi / theta)


def test_formula_2k_sweep():
    for k in range(2, 17):
        assert cycle_length(math.pi / k) == 2 * k


@pytest.mark.parametrize("name,theta", sorted(MODELS.items()))
def test_counter_exact(name, theta):
    m = SpinorMachine(theta)
    outs, acc = modular_counter(m, 5000)
    assert acc == 1.0
    assert state_footprint(m) == 1


def test_reset_erases():
    m = SpinorMachine(MODELS["S3"])
    for _ in range(37):
        m.step()
    pre = m.read()
    m.reset()
    assert m.read() == 0 and m.phi == 0.0
    assert pre != 0  # пре-состояние было ненулевым — и оно утрачено


def test_footprint_constant():
    m = SpinorMachine(MODELS["S1"])
    lm = LogMachine(MODELS["S1"], replay_every=64)
    for _ in range(256):
        m.step()
        lm.step()
    assert state_footprint(m) == 1
    assert lm.footprint() == 1 + 256


def test_min_gap_equals_theta():
    for theta in MODELS.values():
        N = cycle_length(theta)
        assert abs(TAU / N - theta) < 1e-12


def test_logmachine_replay_detects_tamper():
    lm = LogMachine(MODELS["S2"], replay_every=100)
    for _ in range(100):
        lm.step()
    lm.log[10] = (lm.log[10] + 1) % lm.machine.N   # порча истории
    assert lm.replay() == 1                        # replay её находит
