#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""make_release.py — сборка релизного ZIP пакета
AB_Cloud_Quantum_Research_v1.0.0.zip с SHA256SUMS.txt (все файлы,
кроме самих сумм и архива)."""
import hashlib
import os
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAME = "AB_Cloud_Quantum_Research_v1.0.0"
OUT_DIR = "/home/z/my-project/download"
os.makedirs(OUT_DIR, exist_ok=True)

EXCLUDE_DIRS = {"__pycache__", ".git", "julia_env"}
EXCLUDE_FILES = {"SHA256SUMS.txt", NAME + ".zip"}

files = []
for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS]
    for fn in filenames:
        if fn in EXCLUDE_FILES or fn.endswith((".pyc", ".jl.cov")):
            continue
        full = os.path.join(dirpath, fn)
        rel = os.path.relpath(full, ROOT)
        files.append(rel.replace(os.sep, "/"))

files.sort()

sums_path = os.path.join(ROOT, "SHA256SUMS.txt")
with open(sums_path, "w", encoding="utf-8", newline="\n") as f:
    for rel in files:
        h = hashlib.sha256()
        with open(os.path.join(ROOT, rel), "rb") as fh:
            for chunk in iter(lambda: fh.read(1 << 20), b""):
                h.update(chunk)
        f.write(f"{h.hexdigest()}  {rel}\n")

zip_path = os.path.join(OUT_DIR, NAME + ".zip")
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED,
                     compresslevel=9) as z:
    for rel in files:
        z.write(os.path.join(ROOT, rel), arcname=os.path.join(NAME, rel))
    z.write(sums_path, arcname=os.path.join(NAME, "SHA256SUMS.txt"))

n = len(files) + 1
size = os.path.getsize(zip_path)
print(f"Release OK: {zip_path}")
print(f"  файлов в SHA256SUMS: {len(files)} (+1 sums = {n} записей)")
print(f"  размер ZIP: {size / 1e6:.1f} MB")
