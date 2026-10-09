"""T7: GUE-класс расширенной семьи (из закоммиченной C5)."""
import csv
import os

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def test_extended_family_gue():
    rows = list(csv.DictReader(open(f"{ROOT}/data/c5_gates_ext_table.csv")))
    core = rows[:-2]
    rm = np.array([float(r["r_mean"]) for r in core])
    assert np.all(np.abs(rm - 0.5) < 0.03)


def test_no_handle_exits_null_zone():
    rows = list(csv.DictReader(open(f"{ROOT}/data/c5_gates_ext_table.csv")))
    r7 = np.array([abs(float(r["r_H7"])) for r in rows[:-2]])
    assert r7.max() < 0.1
