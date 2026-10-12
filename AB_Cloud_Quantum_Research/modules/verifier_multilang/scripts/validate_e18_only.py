#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""validate_e18_only.py — точечная Python-репликация E18 (numpy) и встраивание
результата в закоммиченный cross_language_validation.{json,md} (репликация
E17 предыдущей сессии сохраняется: SHA-пины детекторов не менялись)."""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cross_validate import validate_e18, RES  # noqa: E402

e18 = validate_e18()
print("E18: счётчики py↔jl: %d расхождений на %d структурированных целях; "
      "max |Δ(1−F)| = %.3e; py max 1−F = %.3e" % (
          e18["count_mismatches"], e18["n_structured"],
          e18["max_1mF_delta"], e18["python_max_1mF"]))

jpath = os.path.join(RES, "cross_language_validation.json")
with open(jpath) as f:
    out = json.load(f)
out["e18"] = e18
with open(jpath, "w") as f:
    json.dump(out, f, indent=2, default=float)

mpath = os.path.join(RES, "cross_language_validation.md")
with open(mpath, encoding="utf-8") as f:
    md = f.read()
anchor = "\nВывод: ключевые результаты"
rows = ("| E18 (v0.4.0): счётчики примитивов py↔jl (7 структурированных "
        "целей) | %d расхождений | — | точно |\n"
        "| E18 (v0.4.0): max \\|Δ(1−F)\\| py↔jl / py max 1−F | %.2e / %.2e | "
        "4.4e−16 | машинное поле |\n" % (
            e18["count_mismatches"], e18["max_1mF_delta"],
            e18["python_max_1mF"]))
if "E18 (v0.4.0)" not in md:
    md = md.replace(anchor, "\n" + rows + anchor)
with open(mpath, "w", encoding="utf-8") as f:
    f.write(md)
print("OK: e18 встроен в cross_language_validation.{json,md}")
