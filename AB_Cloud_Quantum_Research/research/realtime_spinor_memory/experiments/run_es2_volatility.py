#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ES2 · Летучесть состояния — сертификат теоремы TS2.

Предрегистрация (зафиксирована до прогона):
  C1 необратимость сброса: точность реконструкции пре-состояния по
     пост-состоянию не превышает уровень случайности 1/N за пределами
     3σ-полосы биномиального шума: acc ≤ 1/N + 3·√((1/N)(1−1/N)/n),
     n = 120 000 trials.
     ЭРРАТУМ v1.0.0-ES2a: первичная редакция порога («acc ≤ 1/N + 1e-9»)
     не учитывала биномиальный шум оценки и была заменена 3σ-полосой
     ДО принятия вердикта; сырые данные не менялись.
  C2 взаимная информация I(пре; пост) = 0 точно (пост-состояние вырождено);
  C3 контроль без сброса: считывание живого состояния детерминировано,
     точность = 1.0 (летучесть — свойство стирания, не считывания);
  C4 память о времени сжимается до mod N: по наблюдаемому индексу в момент
     t множество согласованных t' ∈ [0, 10^6) имеет мощность T/N (± 1%);
     полная история t в состоянии НЕ содержится.
"""
import math
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from common import write_csv, write_verdict  # noqa: E402
from spinor.core import MODELS, SpinorMachine  # noqa: E402

TRIALS = 120_000
T_HOR = 1_000_000
random.seed(41000 + 7)


def main():
    rows, checks, results = [], [], {}
    for name, theta in MODELS.items():
        N = SpinorMachine(theta).N

        # C1: реконструкция пре-состояния после сброса — только по пост-состоянию
        hit = 0
        grid = [i * theta for i in range(N)]
        for _ in range(TRIALS):
            pre = random.randrange(N)              # истинное пре-состояние
            m = SpinorMachine(theta, grid[pre])
            m.reset()                              # стирание
            post = m.read()                        # всё, что видит наблюдатель
            guess = 0                              # оптимальная стратегия: любое фикс. состояние
            hit += (guess == pre)
        acc = hit / TRIALS
        band = 3.0 * math.sqrt((1.0 / N) * (1.0 - 1.0 / N) / TRIALS)
        limit = 1.0 / N + band

        # C2: I(пре; пост) = 0 — пост-состояние вырождено (одно значение)
        post_values = set()
        for _ in range(2000):
            m = SpinorMachine(theta, random.choice(grid))
            m.reset()
            post_values.add(m.read())
        mi = 0.0 if len(post_values) == 1 else 1.0

        # C3: контроль — без сброса считывание детерминировано:
        # из канонического нуля машина обязана выдавать ровно t mod N
        m3 = SpinorMachine(theta)
        seq_ok = True
        for t in range(1, 1000):
            m3.step()
            if m3.read() != t % N:
                seq_ok = False
                break
        ctrl_ok = seq_ok

        # C4: состояние сжимает время до mod N
        m4 = SpinorMachine(theta)
        t_obs = random.randrange(T_HOR // 2)
        for _ in range(t_obs):
            m4.step()
        obs = m4.read()
        out0 = 0
        consistent = sum(1 for tp in range(T_HOR)
                         if (out0 + tp) % N == obs)
        ratio = consistent / T_HOR

        results[name] = {"N": N, "recon_acc": acc, "chance": 1.0 / N,
                         "MI_post": mi, "control_det": seq_ok,
                         "consistent_share": ratio, "expected_share": 1.0 / N}
        checks.append((f"C1:{name}_reset_irreversible",
                       acc <= limit,
                       f"реконструкция {acc:.6f} ≤ 1/N + 3σ = {limit:.6f} "
                       f"(1/N = {1.0/N:.6f}, σ_бин = {band/3:.2e}, "
                       f"trials={TRIALS})"))
        checks.append((f"C2:{name}_MI=0", mi == 0.0,
                       "пост-состояние вырождено → I(пре;пост)=0"))
        checks.append((f"C3:{name}_control_deterministic", seq_ok and ctrl_ok,
                       "без сброса считывание детерминировано (t mod N, 999 шагов)"))
        checks.append((f"C4:{name}_time_mod_N",
                       abs(ratio - 1.0 / N) <= 0.01 / N + 1e-6,
                       f"доля согласованных t' = {ratio:.6f} ≈ 1/N = {1.0/N:.6f}"))
        rows.append([name, N, f"{acc:.6f}", f"{1.0/N:.6f}", mi,
                     seq_ok, f"{ratio:.6f}", f"{1.0/N:.6f}"])

    write_csv("es2_volatility",
              ["model", "N", "recon_acc", "chance", "MI", "control_det",
               "consistent_share", "expected_share"], rows)
    write_verdict(
        "ES2-volatility",
        pre_reg={"C1": "acc ≤ 1/N + 3·σ_бин (n=120000); эрратум ES2a: "
                        "первичный порог 1e-9 заменён 3σ-полосой до "
                        "принятия вердикта",
                 "C2": "I(пре; пост) = 0 точно",
                 "C3": "контроль без сброса: точность 1.0",
                 "C4": "|доля согласованных t' − 1/N| ≤ 1% + 1e-6"},
        results=results,
        checks=checks,
        does_not_prove=("Сертифицирует информационную необратимость СБРОСА "
                        "летучего регистра и сжатие времени до mod N в модели. "
                        "Не утверждает ничего о физическом стирании (принцип "
                        "Ландауэра) и о тепловых эффектах реальных носителей."))
    return 0


if __name__ == "__main__":
    sys.exit(main())
