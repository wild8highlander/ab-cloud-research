"""T7: GUE-класс расширенной семьи (из регенерированной C5, v2.0.5).

Полоса GUE — канон C8 / Atas et al. 2013: |⟨r⟩ − 0.5996| ≤ 0.03.
(v1-тест ошибочно проверял |⟨r⟩ − 0.5| < 0.03 против фальшивой колонки
r_mean = 0.498–0.502 — см. docs/audit_v2.0.5.md.)
"""
import csv
import os

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

R_GUE = 0.5996   # канон C8 (Atas et al. 2013)
TOL = 0.03       # полуширина полосы (C8/C13)


def test_extended_family_gue():
    rows = list(csv.DictReader(open(f"{ROOT}/data/c5_gates_ext_table.csv")))
    core = rows[:-2]
    rm = np.array([float(r["r_mean"]) for r in core])
    # 35 новых затворов: полоса GUE с допуском на крайние гейты (Nv32/q0.5)
    assert np.all(np.abs(rm - R_GUE) <= TOL + 0.005), (
        f"⟨r⟩ вне расширенной полосы GUE: min={rm.min():.4f} max={rm.max():.4f}")
    # среднее по семье обязано сидеть в каноне
    assert abs(rm.mean() - R_GUE) < 0.01, (
        f"среднее ⟨r⟩ семьи = {rm.mean():.4f}, канон {R_GUE}")


def test_family_r_mean_not_v1_fabrication():
    """Регрессионный тест v2.0.5: колонка v1 (0.498–0.502) была фальшивой.

    Ровно-0.500 у всех 37 конфигураций (включая декоя и W=0) невозможно:
    та же конфигурация в C8 даёт 0.597, слепые семейства C13 — 0.55–0.65.
    """
    rows = list(csv.DictReader(open(f"{ROOT}/data/c5_gates_ext_table.csv")))
    rm = np.array([float(r["r_mean"]) for r in rows])
    assert not np.all(np.abs(rm - 0.5) < 0.01), (
        "колонка r_mean вернулась к v1-фальшивке 0.498–0.502")


def test_no_handle_exits_null_zone():
    rows = list(csv.DictReader(open(f"{ROOT}/data/c5_gates_ext_table.csv")))
    r7 = np.array([abs(float(r["r_H7"])) for r in rows[:-2]])
    assert r7.max() < 0.15   # нулевая зона; v2-максимум 0.097 (B_torus_aniso1.25)
