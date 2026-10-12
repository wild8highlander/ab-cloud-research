# -*- coding: utf-8 -*-
"""tasks.py — вычисления без долговременной памяти и контрастный baseline.

modular_counter      — задача «модульный счётчик»: машина выдаёт индекс
                       своего состояния каждый шаг; корректность означает
                       out_t ≡ (out_0 + t) (mod N) на всём горизонте T.
                       Машина НЕ знает t: единственный её регистр — фаза,
                       которая сама и есть счётчик по модулю N.

LogMachine           — контрастная «машина с журналом»: та же динамика,
                       но каждый шаг дописывается в вечный лог, а каждые
                       replay_every шагов журнал полностью перепроверяется
                       (replay). Стоимость верификации растёт линейно по t
                       — реальные дедлайны ломаются (кампания ES3).

Оба объекта честно измеряются по footprint: сколько регистров/ячеек
состояние занимает в момент t.
"""
import math

from .core import SpinorMachine

__all__ = ["modular_counter", "LogMachine"]


def modular_counter(machine: SpinorMachine, steps: int, out=None):
    """Прогон модульного счётчика.

    Возвращает (outputs, correctness):
      outputs     — список считываний длины steps (для внешней проверки);
      correctness — доля шагов с out_t ≡ (out_0 + t) (mod N).
    Машина хранит только фазу; outputs нужен лишь НАБЛЮДАТЕЛЮ.
    """
    out0 = machine.read()
    outs = [] if out is None else out
    ok = 0
    for t in range(steps):
        machine.step()
        o = machine.read()
        outs.append(o)
        if o == (out0 + t + 1) % machine.N:
            ok += 1
    return outs, ok / max(1, steps)


class LogMachine:
    """Контраст: та же фазовая динамика + вечный журнал + периодический
    полный replay. Демонстрирует цену долговременной памяти: рост O(t)."""

    __slots__ = ("machine", "log", "replay_every", "replay_cost")

    def __init__(self, theta: float, replay_every: int = 1024):
        self.machine = SpinorMachine(theta)
        self.log = []            # долговременное хранилище (растёт)
        self.replay_every = int(replay_every)
        self.replay_cost = 0.0   # накопленная стоимость replay (ячейки)

    def step(self) -> int:
        self.machine.step()
        o = self.machine.read()                 # в журнал пишется СИМВОЛ
        self.log.append(o)                      # запись в вечный лог
        if len(self.log) % self.replay_every == 0:
            self.replay()                       # полная перепроверка
        return o

    def replay(self) -> int:
        """Полная перепроверка журнала: O(t) на момент времени t."""
        base = self.log[0] if self.log else 0
        n = self.machine.N
        bad = 0
        for t, o in enumerate(self.log):        # линейный проход по истории
            if o != (base + t) % n:
                bad += 1
        self.replay_cost += len(self.log)
        return bad

    def footprint(self) -> int:
        """Регистр фазы + весь журнал: 1 + t (растёт без ограничений)."""
        return 1 + len(self.log)
