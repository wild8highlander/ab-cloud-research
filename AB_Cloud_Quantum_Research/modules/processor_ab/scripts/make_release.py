#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""make_release.py — самосборка релизного архива AB Quantum Processor.

Вычисляет SHA256SUMS.txt и собирает ZIP в ../download/ (или рядом).
Запуск: python3 scripts/make_release.py [out_dir]
"""
import hashlib
import os
import sys
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAME = 'AB_Quantum_Processor_v0.1.1'


def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def main():
    out_dir = sys.argv[1] if len(sys.argv) > 1 else \
        os.path.dirname(ROOT)
    # SHA256SUMS
    sums = []
    for root, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs
                   if d not in ('__pycache__', '.pytest_cache')]
        for fn in sorted(files):
            if fn == 'SHA256SUMS.txt':
                continue
            p = os.path.join(root, fn)
            rel = os.path.relpath(p, ROOT)
            sums.append((sha256(p), rel))
    with open(os.path.join(ROOT, 'SHA256SUMS.txt'), 'w') as f:
        for digest, rel in sorted(sums, key=lambda x: x[1]):
            f.write(f'{digest}  {rel}\n')
    print(f'SHA256SUMS.txt: {len(sums)} файлов')
    # zip (включая _json — DOCS-исходники монографий)
    out = os.path.join(out_dir, f'{NAME}.zip')
    with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED,
                         compresslevel=6) as z:
        for root, dirs, files in os.walk(ROOT):
            dirs[:] = [d for d in dirs
                       if d not in ('__pycache__', '.pytest_cache')]
            for fn in sorted(files):
                p = os.path.join(root, fn)
                z.write(p, os.path.join(NAME, os.path.relpath(p, ROOT)))
    size = os.path.getsize(out) / 1e6
    print(f'ZIP OK: {out} ({size:.1f} MB)')
    return 0


if __name__ == '__main__':
    sys.exit(main())
