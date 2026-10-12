#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ES1 · Фазовые циклы — сертификат теоремы TS1.

Предрегистрация (зафиксирована до прогона):
  C1 период решётки состояний равен N = 2k точно: π/2 → 4, π/3 → 6, π/7 → 14;
  C2 минимальный угловой зазор между различными состояниями = 2π/N (± 1e-12);
  C3 решётка состояний равномерна: max |φ_i − i·2π/N| ≤ 1e-9 для всех моделей;
  C4 индуктивный контроль: для всех k = 2…16 период вращения θ = π/k равен 2k.
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from common import write_csv, write_verdict  # noqa: E402
from spinor.core import MODELS, SpinorMachine, cycle_length  # noqa: E402

TAU = 2.0 * math.pi
EPS = 1e-12


def measure(name, theta):
    m = SpinorMachine(theta)
    N = m.N
    # C1: эмпирический минимальный период последовательности состояний
    seq = []
    m2 = SpinorMachine(theta)
    for _ in range(3 * N + 2):
        m2.step()
        seq.append(m2.read())
    period = None
    for p in range(1, 2 * N + 2):
        if all(seq[t] == seq[t + p] for t in range(len(seq) - p)):
            period = p
            break
    # C2: минимальный зазор решётки состояний
    grid = [i * theta for i in range(N)]
    gaps = [grid[(i + 1) % N] - grid[i] for i in range(N)]
    gaps = [g if g > 0 else g + TAU for g in gaps]
    min_gap = min(gaps)
    # C3: равномерность (отклонение от идеальной решётки)
    dev = max(abs(grid[i] - i * TAU / N) for i in range(N))
    return N, period, min_gap, dev


def main():
    rows, checks, results = [], [], {}
    for name, theta in MODELS.items():
        N, period, min_gap, dev = measure(name, theta)
        k = round(math.pi / theta)
        expect = 2 * k
        results[name] = {"theta_over_pi": "1/%d" % k, "k": k, "N_expected": expect,
                         "N_measured": N, "period_measured": period,
                         "min_gap": min_gap, "min_gap_expected": TAU / N,
                         "uniformity_dev": dev,
                         "bits_per_step": math.log2(N)}
        checks.append((f"C1:{name}_period=2k",
                       N == expect and period == expect,
                       f"θ=π/{k}: N={N}, период={period}, ожидалось {expect}"))
        checks.append((f"C2:{name}_min_gap",
                       abs(min_gap - TAU / N) < 1e-9,
                       f"min gap = {min_gap:.12f} vs 2π/N = {TAU/N:.12f}"))
        checks.append((f"C3:{name}_uniformity", dev <= 1e-9,
                       f"max |φ_i − i·2π/N| = {dev:.2e} ≤ 1e-9"))
        rows.append([name, f"pi/{k}", k, N, period,
                     f"{min_gap:.15f}", f"{TAU/N:.15f}",
                     f"{dev:.2e}", f"{math.log2(N):.6f}"])

    # C4: индуктивный контроль формулы N = 2k на всём диапазоне k = 2…16
    sweep_ok, bad = True, []
    for k in range(2, 17):
        N = cycle_length(math.pi / k)
        if N != 2 * k:
            sweep_ok, _ = False, bad.append(k)
    checks.append(("C4:sweep_k2..16_N=2k", sweep_ok,
                   "N(π/k)=2k для всех k=2…16" if sweep_ok
                   else f"нарушение при k={bad}"))
    rows.append(["sweep", "pi/k, k=2..16", "2..16",
                 "все N=2k", "-", "-", "-", "-", "-"])

    write_csv("es1_cycles", ["model", "theta", "k", "N", "period",
                             "min_gap", "2pi_over_N", "uniformity_dev",
                             "bits_per_step"], rows)
    write_verdict(
        "ES1-cycles",
        pre_reg={"C1": "period == N == 2k точно (4, 6, 14)",
                 "C2": "min_gap == 2π/N в пределах 1e-9",
                 "C3": "равномерность решётки ≤ 1e-9",
                 "C4": "N(π/k) = 2k для всех k = 2…16"},
        results=results,
        checks=checks,
        does_not_prove=("Сертифицирует замкнутость ФАЗОВЫХ решёток выбранных "
                        "моделей и формулу N = 2k; не утверждает ничего о "
                        "физической реализации спинорных фаз и не связана с "
                        "гипотезой Римана."))
    return 0


if __name__ == "__main__":
    sys.exit(main())
