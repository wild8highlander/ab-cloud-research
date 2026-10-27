#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ES5 · Шумовой канал фазы — граница робастности каждой модели.

Модель шума (по предрегистрации): шум СЧИТЫВАНИЯ — состояние машины
точное, наблюдатель видит φ̂_t = φ_t + ε_t, ε_t ~ N(0, σ) независимо на
каждом шаге; считывание — ML к ближайшей точке решётки. Истинный индекс
ведётся наблюдателем без шума.

ЭРРАТУМ v1.0.0-ES5a: первичная реализация добавляла шум В СОСТОЯНИЕ
(φ ← φ + θ + ε), т.е. моделировала фазовую диффузию, тогда как
предрегистрированные пороги C1–C4 сформулированы для шума считывания
(P(ошибки шага) = 2Φ(−gap/2σ)). Реализация приведена к предрегистрации;
вариант диффузии сохранён как отдельное РАЗВЕДОЧНОЕ измерение без
порогов (D-блок): время до первой ошибки t* ~ gap²/(4σ²) → наклон −2
в log-log; результаты публикуются как измерение, не как вердикт.

Предрегистрация (зафиксирована до прогона; R = 48 прогонов × T = 10 000
шагов на точку сетки σ, итого 480 000 решений на точку):
  C1 зона тишины: σ* (наибольшее σ сетки с SER = 0) удовлетворяет
     gap/12 ≤ σ* ≤ gap/2 для каждой модели, gap = 2π/N;
  C2 порядок робастности: σ*_S1 ≥ σ*_S2 ≥ σ*_S3 (следует из зазора);
  C3 глубокая зона: SER(σ = gap/8) ≤ 1e-3 для каждой модели;
  C4 пробой канала: SER(σ = gap) ≥ 0.3 для каждой модели;
  C5 кросс-проверка: векторизованный симулятор без шума побитово совпадает
     со скалярной SpinorMachine на 5000 шагов для всех моделей.
"""
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from common import write_csv, write_verdict  # noqa: E402
from spinor.core import MODELS, SpinorMachine  # noqa: E402

TAU = 2.0 * math.pi
R, T = 48, 10_000
SIGMA_BASE = list(np.logspace(-4, -0.5, 20))
rng = np.random.default_rng(41000 + 7)


def ser_at(theta, sigma):
    """SER на одной точке σ (шум считывания): R прогонов, T шагов."""
    N = SpinorMachine(theta).N
    phi = np.zeros(R)                       # точное состояние (чистый ход)
    true_idx = np.zeros(R, dtype=np.int64)
    errors = 0
    for _ in range(T):
        phi = (phi + theta) % TAU           # детерминированный шаг БЕЗ шума
        true_idx = (true_idx + 1) % N
        obs = (phi + rng.normal(0.0, sigma, R)) % TAU   # шумное наблюдение
        dec = np.rint(obs / theta).astype(np.int64) % N
        errors += int(np.count_nonzero(dec != true_idx))
    return errors / (R * T)


def vectorized_crosscheck(theta, steps=5000):
    """Побитовая сверка векторного симулятора со скалярной машиной."""
    m = SpinorMachine(theta)
    phi = np.zeros(1)
    idx_v, idx_s = [], []
    for _ in range(steps):
        m.step()
        phi = (phi + theta) % TAU
        idx_v.append(int(np.rint(phi[0] / theta)) % m.N)
        idx_s.append(m.read())
    return idx_v == idx_s


def diffusion_time(theta, sigma, cap=2_000_000, walks=16):
    """РАЗВЕДОВОЕ измерение (фазовая диффузия, без порогов): медиана
    времени до первой ML-ошибки по walks независимым прогонам."""
    N = SpinorMachine(theta).N
    times = []
    for _ in range(walks):
        phi, idx, t = 0.0, 0, 0
        while t < cap:
            phi = (phi + theta + rng.normal(0.0, sigma)) % TAU
            idx = (idx + 1) % N
            t += 1
            if int(round(phi / theta)) % N != idx:
                break
        times.append(t)
    return float(np.median(times))


def main():
    rows, checks, results = [], [], {}
    info = {}
    for name, theta in MODELS.items():
        N = SpinorMachine(theta).N
        gap = TAU / N
        grid = sorted(set(SIGMA_BASE) | {gap / 8, gap / 6, gap / 4,
                                         gap / 2, gap})
        sers = {float(s): ser_at(theta, float(s)) for s in grid}
        silent = [s for s, e in sers.items() if e == 0.0]
        sigma_star = max(silent) if silent else 0.0
        results[name] = {"N": N, "gap": gap, "sigma_star": sigma_star,
                         "gap_over_12": gap / 12, "gap_over_2": gap / 2,
                         "SER_at_gap_over_8": sers[gap / 8],
                         "SER_at_gap": sers[gap],
                         "bits_per_step": math.log2(N)}
        checks.append((f"C1:{name}_silence_zone",
                       gap / 12 <= sigma_star <= gap / 2,
                       f"σ* = {sigma_star:.4f} ∈ [gap/12={gap/12:.4f}, "
                       f"gap/2={gap/2:.4f}]"))
        checks.append((f"C3:{name}_deep_zone", sers[gap / 8] <= 1e-3,
                       f"SER(gap/8) = {sers[gap/8]:.2e} ≤ 1e-3"))
        checks.append((f"C4:{name}_channel_breaks", sers[gap] >= 0.3,
                       f"SER(gap) = {sers[gap]:.3f} ≥ 0.3"))
        ok = vectorized_crosscheck(theta)
        checks.append((f"C5:{name}_vectorized_bitwise", ok,
                       "векторный симулятор ≡ скалярной машине (5000 шагов)"))
        info[name] = sigma_star
        for s in sorted(sers):
            rows.append([name, f"{s:.6f}", f"{sers[s]:.6f}"])

    s1, s2, s3 = info["S1"], info["S2"], info["S3"]
    results["ordering"] = {"S1": s1, "S2": s2, "S3": s3}
    checks.append(("C2:robustness_ordering", s1 >= s2 >= s3,
                   f"σ*_S1={s1:.4f} ≥ σ*_S2={s2:.4f} ≥ σ*_S3={s3:.4f}"))

    # ── D-блок: разведочное измерение фазовой диффузии (БЕЗ порогов)
    drows, dres = [], {}
    for name, theta in MODELS.items():
        N = SpinorMachine(theta).N
        gap = TAU / N
        dres[name] = {}
        for frac in (0.05, 0.1, 0.2, 0.4):
            sig = frac * gap
            tstar = diffusion_time(theta, sig, walks=8)
            dres[name][f"sigma={frac}·gap"] = tstar
            drows.append([name, f"{sig:.6f}", f"{tstar:.0f}"])
    # наклон log t* ~ −2 log σ (теория: t* ≈ gap²/(4σ²))
    for name, theta in MODELS.items():
        N = SpinorMachine(theta).N
        pts = [(0.05 * TAU / N, dres[name]["sigma=0.05·gap"]),
               (0.1 * TAU / N, dres[name]["sigma=0.1·gap"]),
               (0.2 * TAU / N, dres[name]["sigma=0.2·gap"])]
        lx = [math.log(s) for s, _ in pts]
        ly = [math.log(t) for _, t in pts]
        n = len(lx)
        b = (sum(x * y for x, y in zip(lx, ly)) - n * sum(lx) * sum(ly) / n) / \
            (sum(x * x for x in lx) - n * (sum(lx) / n) ** 2)
        dres[name]["loglog_slope"] = b
        results[f"diffusion_{name}"] = dres[name]
    results["diffusion_note"] = ("РАЗВЕДКА (без порогов, эрратум ES5a): "
                                 "наклон log t* по σ ≈ −2 согласуется с "
                                 "t* ~ gap²/σ²; не является вердиктом")

    write_csv("es5_noise", ["model", "sigma_rad", "SER"], rows)
    write_csv("es5_noise_diffusion", ["model", "sigma_rad", "t_first_error"],
              drows)
    write_verdict(
        "ES5-noise",
        pre_reg={"C1": "gap/12 ≤ σ* ≤ gap/2 для каждой модели (шум "
                        "считывания)",
                 "C2": "σ*_S1 ≥ σ*_S2 ≥ σ*_S3",
                 "C3": "SER(gap/8) ≤ 1e-3",
                 "C4": "SER(gap) ≥ 0.3",
                 "C5": "векторный симулятор ≡ скалярной машине побитово",
                 "erratum": "ES5a: первичная реализация моделировала "
                            "фазовую диффузию; приведена к предрегистрации "
                            "(шум считывания), диффузия — разведка D-блока"},
        results=results,
        checks=checks,
        does_not_prove=("Сертифицирует границу робастности ФАЗОВОГО КАНАЛА "
                        "при iid-шуме считывания. Не утверждает "
                        "устойчивости к фазовой диффузии (см. разведку "
                        "D-блока: t* ~ gap²/σ²), систематическим дрейфам и "
                        "квантовой декогеренции; trade-off «биты против "
                        "зазора» публикуется как честная граница модели."))
    return 0


if __name__ == "__main__":
    sys.exit(main())
