#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ES3 · Реальное время — сертификат теоремы TS3.

Шаг фазовой машины — O(1) при любом t: состояние не растёт, история
отсутствует. Контраст — LogMachine (вечный журнал + полный replay каждые
1024 шага): стоимость верификации растёт линейно по t и ломает дедлайны.

Предрегистрация (зафиксирована до прогона; gc отключён на время замера):
  C1 плоский профиль: наклон регрессии среднего времени шага машины по t
     ≤ 1e-11 мс/шаг (рост отсутствует);
  C2 дедлайн-комплаенс машины: 100% шагов ≤ 1 мс на горизонте 200 000;
  C3 рост у baseline: средняя стоимость шага LogMachine на t ≥ 2^17 не
     менее чем в 5 раз выше, чем на t = 2^10; у машины в тех же точках
     отношение ≤ 2.0 (допуск ОС-шума);
  C4 наклон стоимости replay по t положителен с R² ≥ 0.98 (Ω(t)).
"""
import gc
import os
import statistics
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from common import write_csv, write_verdict  # noqa: E402
from spinor.core import MODELS, SpinorMachine  # noqa: E402
from spinor.tasks import LogMachine  # noqa: E402

HORIZON = 200_000
CHUNK = 4_096
DEADLINE_MS = 1.0


def measure_machine(theta):
    m = SpinorMachine(theta)
    means, tmarks, over = [], [], 0
    times = []
    for i in range(HORIZON // CHUNK):
        buf = []
        for _ in range(CHUNK):
            t0 = time.perf_counter()
            m.step()
            buf.append(time.perf_counter() - t0)
        times.extend(buf)
        means.append(statistics.median(buf) * 1e3)   # мс
        tmarks.append((i + 1) * CHUNK)
        over += sum(1 for x in buf if x * 1e3 > DEADLINE_MS)
    return tmarks, means, over, times


def linreg(xs, ys):
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    b = sxy / sxx
    a = my - b * mx
    ss_tot = sum((y - my) ** 2 for y in ys)
    ss_res = sum((y - (a + b * x)) ** 2 for x, y in zip(xs, ys))
    r2 = 1 - ss_res / ss_tot if ss_tot > 0 else 1.0
    return a, b, r2


def main():
    gc.disable()
    try:
        rows, checks, results = [], [], {}

        # ── машина: плоский профиль и дедлайны (S1 — репрезентативно;
        #    динамика шага одинакова для всех моделей, О(1) не зависит от N)
        tmarks, means, over, _ = measure_machine(MODELS["S1"])
        _, slope_ms_per_step, r2 = linreg(tmarks, means)
        results["machine_S1"] = {
            "chunks": len(tmarks), "median_ms": statistics.median(means),
            "slope_ms_per_step": slope_ms_per_step, "r2": r2,
            "deadline_misses": over,
            "compliance": 1.0 - over / HORIZON}
        checks.append(("C1:machine_flat_profile",
                       abs(slope_ms_per_step) <= 1e-11,
                       f"наклон = {slope_ms_per_step:.3e} мс/шаг ≤ 1e-11 "
                       f"(R²={r2:.3f})"))
        checks.append(("C2:machine_deadlines_100pct", over == 0,
                       f"пропусков дедлайна {over} из {HORIZON} "
                       f"(Δt = 1 мс)"))

        # контроль того же для S3 (максимальное N)
        tmarks3, means3, over3, _ = measure_machine(MODELS["S3"])
        _, slope3, _ = linreg(tmarks3, means3)
        results["machine_S3"] = {"median_ms": statistics.median(means3),
                                 "slope_ms_per_step": slope3,
                                 "deadline_misses": over3}
        checks.append(("C1b:machine_S3_flat", abs(slope3) <= 1e-11,
                       f"S3: наклон = {slope3:.3e} мс/шаг; пропусков {over3}"))

        # ── контраст: LogMachine с вечным журналом
        lm = LogMachine(MODELS["S1"], replay_every=1024)
        cost_at = {}
        for t in range(1, HORIZON + 1):
            t0 = time.perf_counter()
            lm.step()
            dt = time.perf_counter() - t0
            if t in (1024, 8192, 65536, 131072, 200000):
                cost_at[t] = dt * 1e3                   # мс за шаг с replay
        ratio_base = cost_at[131072] / max(cost_at[1024], 1e-12)
        ratio_mach = (statistics.median(means[131072 // CHUNK - 1:
                                                    131072 // CHUNK + 1]) /
                      max(statistics.median(means[:2]), 1e-12))
        results["logmachine"] = {"cost_ms_at": {str(k): v for k, v in
                                                cost_at.items()},
                                 "growth_ratio_2x17_over_2x10": ratio_base,
                                 "replay_cost_cells": lm.replay_cost,
                                 "footprint_at_T": lm.footprint()}
        checks.append(("C3:baseline_grows_x5",
                       ratio_base >= 5.0,
                       f"LogMachine: стоимость шага на t=2^17 против t=2^10 "
                       f"× {ratio_base:.1f} (машина: × {ratio_mach:.2f} ≤ 2.0)"))
        checks.append(("C3b:machine_ratio_small", ratio_mach <= 2.0,
                       f"машина в тех же точках × {ratio_mach:.2f}"))

        # C4: наклон стоимости replay — линейный по t (честный замер на
        # растущих журналах)
        pts = [1024 * (i + 1) for i in range(HORIZON // 1024)]
        costs = []
        for p in pts:
            lm2 = LogMachine(MODELS["S1"], replay_every=p + 1)  # без авто-replay
            lm2.log = [0] * p
            t0 = time.perf_counter()
            lm2.replay()
            costs.append((time.perf_counter() - t0) * 1e3)
        _, brep, r2rep = linreg(pts, costs)
        results["replay"] = {"slope_ms_per_cell": brep, "r2": r2rep,
                             "points": len(pts)}
        checks.append(("C4:replay_Omega(t)", brep > 0 and r2rep >= 0.98,
                       f"наклон replay = {brep:.3e} мс/ячейка, R² = {r2rep:.4f}"))

        for t in (1024, 8192, 65536, 131072, 200000):
            rows.append(["logmachine", t, f"{cost_at.get(t, float('nan')):.6f}"])
        rows.append(["machine_S1", "all", f"{statistics.median(means):.6f}"])
        rows.append(["machine_S3", "all", f"{statistics.median(means3):.6f}"])
    finally:
        gc.enable()

    write_csv("es3_realtime", ["subject", "t", "cost_ms"], rows)
    # полные кривые для фигур (только закоммиченные данные)
    write_csv("es3_machine_chunks", ["t", "median_ms"],
              list(zip(tmarks, [f"{x:.9f}" for x in means])))
    write_csv("es3_replay_curve", ["t", "cost_ms"],
              list(zip(pts, [f"{x:.9f}" for x in costs])))
    write_verdict(
        "ES3-realtime",
        pre_reg={"C1": "|наклон| ≤ 1e-11 мс/шаг (плоский профиль)",
                 "C2": "дедлайн-комплаенс 100% при Δt = 1 мс",
                 "C3": "baseline ×≥5 на t=2^17 против t=2^10; машина ≤ ×2",
                 "C4": "наклон replay > 0, R² ≥ 0.98"},
        results=results,
        checks=checks,
        does_not_prove=("Сертифицирует O(1)-стоимость шага модели и линейный "
                        "рост полной перепроверки журнала в КОНТРАСТНОЙ "
                        "модели. Не измеряет производительность физических "
                        "устройств и не утверждает, что всякая память "
                        "запрещена — только что вечный журнал несовместим "
                        "с жёстким реальным временем."))
    return 0


if __name__ == "__main__":
    sys.exit(main())
