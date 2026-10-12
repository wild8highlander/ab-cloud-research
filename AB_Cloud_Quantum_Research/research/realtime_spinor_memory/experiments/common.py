# -*- coding: utf-8 -*-
"""common.py — общий каркас кампаний ES1–ES5.

Дисциплина исследования та же, что во всей программе: пороги
предрегистрированы (константы PRE_REG ниже зафиксированы ДО прогона),
вердикт пишется в data/esK_*.json с полем does_not_prove, отрицательный
результат не ретушируется."""
import csv
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.dirname(HERE)                      # research/realtime_spinor_memory
DATA = os.path.join(RES, "data")
sys.path.insert(0, RES)

os.makedirs(DATA, exist_ok=True)


def write_verdict(name, pre_reg, results, checks, does_not_prove):
    """Вердикт кампании: {experiment, pre_registered, results, checks,
    pass, does_not_prove}. pass = все checks истинны."""
    v = {
        "experiment": name,
        "campaign": "realtime_spinor_memory",
        "package": "AB Cloud Quantum Research v1.0.0",
        "pre_registered": pre_reg,
        "results": results,
        "checks": [{"name": k, "pass": bool(p), "detail": d}
                   for k, p, d in checks],
        "pass": all(p for _, p, _ in checks),
        "does_not_prove": does_not_prove,
    }
    path = os.path.join(DATA, f"{name.lower().replace('-', '_')}_verdict.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(v, f, ensure_ascii=False, indent=1)
    print(f"[{name}] pass={v['pass']} -> {os.path.basename(path)}")
    for k, p, d in checks:
        print(f"   {'PASS' if p else 'FAIL'}  {k}: {d}")
    return v


def write_csv(name, header, rows):
    path = os.path.join(DATA, f"{name}.csv")
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)
    return path
