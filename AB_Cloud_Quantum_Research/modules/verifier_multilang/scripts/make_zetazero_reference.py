#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""make_zetazero_reference.py — эталонная таблица нулей ζ (слой валидатора E17).
Источник: mpmath.zetazero(n), 40 значащих цифр. Генерируется НЕЗАВИСИМО от
детектора (детектор не содержит эталонных нулей); SHA256 выхода фиксируется
и проверяется Julia-валидатором перед использованием."""
import hashlib
import os

import mpmath as mp

mp.mp.dps = 40

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RES = os.path.join(ROOT, "results")
os.makedirs(RES, exist_ok=True)
N_MAX = 660

out_path = os.path.join(RES, "e17_zetazero_reference.csv")
with open(out_path, "w", encoding="utf-8", newline="\n") as f:
    f.write("n,gamma\n")
    for n in range(1, N_MAX + 1):
        g = mp.im(mp.zetazero(n))
        f.write("%d,%s\n" % (n, mp.nstr(g, 30)))
        if n % 100 == 0:
            print("  n=%d done" % n)

h = hashlib.sha256()
with open(out_path, "rb") as f:
    for chunk in iter(lambda: f.read(65536), b""):
        h.update(chunk)
sha = h.hexdigest()
with open(os.path.join(RES, "e17_zetazero_reference_sha256.txt"), "w") as f:
    f.write(sha + "  e17_zetazero_reference.csv\n")
print("OK:", out_path)
print("SHA256:", sha)
