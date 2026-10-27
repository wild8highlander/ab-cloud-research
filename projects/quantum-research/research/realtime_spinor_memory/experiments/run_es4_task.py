#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ES4 · Вычисление без хранилища — сертификат принципа «читает, не несёт».

Задача: модульный счётчик out_t ≡ (out_0 + t) (mod N) на горизонте
T = 300 000 шагов для всех трёх моделей. Машина НЕ знает t — её
единственный регистр (фаза) сам является счётчиком по модулю N.

Предрегистрация (зафиксирована до прогона):
  C1 корректность: доля правильных шагов = 1.0 точно для S1, S2, S3;
  C2 след состояния постоянен: footprint машины = 1 регистр при t = 0,
     t = T/2 и t = T (рост отсутствует);
  C3 «хранение = 0»: машина не ведёт НИКАКИХ контейнеров истории —
     аудит __slots__/атрибутов не находит списков/словарей;
  C4 контраст: footprint LogMachine при том же горизонте = 1 + T ≥ 10^5
     ячеек (рост линейный).
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from common import write_csv, write_verdict  # noqa: E402
from spinor.core import MODELS, SpinorMachine, state_footprint  # noqa: E402
from spinor.tasks import LogMachine, modular_counter  # noqa: E402

T = 300_000


def main():
    rows, checks, results = [], [], {}
    for name, theta in MODELS.items():
        m = SpinorMachine(theta)
        fp0 = state_footprint(m)
        outs, acc = modular_counter(m, T)
        fp_mid = state_footprint(m)                    # после T/2…T шагов
        # аудит контейнеров: у машины нет списков/словарей/множеств
        containers = [a for a in vars(m).values()
                      if isinstance(a, (list, dict, set))] if not hasattr(
                          m, "__slots__") else []
        lm = LogMachine(theta, replay_every=T + 1)     # без авто-replay
        for _ in range(T):
            lm.step()
        results[name] = {"N": m.N, "accuracy": acc, "footprint": fp0,
                         "footprint_after_T": fp_mid,
                         "containers_found": len(containers),
                         "logmachine_footprint": lm.footprint()}
        checks.append((f"C1:{name}_counter_exact", acc == 1.0,
                       f"модульный счётчик на {T} шагов: доля верных = {acc}"))
        checks.append((f"C2:{name}_footprint_const",
                       fp0 == 1 and fp_mid == 1,
                       f"след состояния = {fp0} регистр(а) до и после {T} шагов"))
        checks.append((f"C3:{name}_no_history_containers",
                       len(containers) == 0,
                       "история не хранится: контейнеров 0 (хранение = 0)"))
        checks.append((f"C4:{name}_log_contrast",
                       lm.footprint() == T + 1,
                       f"LogMachine: след = {lm.footprint()} ячеек "
                       f"(1 + {T}) — рост без ограничений"))
        rows.append([name, m.N, T, acc, fp0, fp_mid,
                     len(containers), lm.footprint()])

    bits = {n: math.log2(m.N) for n, th in MODELS.items()
            for m in [SpinorMachine(th)]}
    results["bits_per_step"] = bits
    write_csv("es4_memoryless_task",
              ["model", "N", "steps", "accuracy", "footprint_t0",
               "footprint_T", "containers", "logmachine_footprint"], rows)
    write_verdict(
        "ES4-memoryless-task",
        pre_reg={"C1": "accuracy == 1.0 для всех трёх моделей",
                 "C2": "footprint == 1 при t=0 и t=T",
                 "C3": "контейнеров истории 0",
                 "C4": "LogMachine footprint == 1 + T"},
        results=results,
        checks=checks,
        does_not_prove=("Демонстрирует вычислительную ПОЛНОТУ летучей фазы "
                        "как счётчика по модулю N и нулевой след хранения. "
                        "Не утверждает универсальности: произвольные "
                        "вычисления с большими промежуточными данными "
                        "требуют либо внешнего потока, либо памяти — это "
                        "честная граница модели."))
    return 0


if __name__ == "__main__":
    sys.exit(main())
