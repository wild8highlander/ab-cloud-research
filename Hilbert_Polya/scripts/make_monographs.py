#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""make_monographs.py — дамп контента 12 документов × 2 языка в JSON и
запуск рендеров (PDF и DOCX). Запуск: python3 scripts/make_monographs.py"""
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, 'monograph'))
sys.path.insert(0, os.path.join(ROOT, 'monograph', 'content'))

from content import ru_part1, ru_part2, ru_part3  # noqa: E402
from content import en_part1, en_part2, en_part3  # noqa: E402

DOCS = {
    'ru': {**ru_part1.DOCS, **ru_part2.DOCS, **ru_part3.DOCS},
    'en': {**en_part1.DOCS, **en_part2.DOCS, **en_part3.DOCS},
}
# пути: C* → computations/C*/monograph_{lang}; theorems/appendix → monograph/
DEST = {
    'C1': 'computations/C1_identity_function',
    'C2': 'computations/C2_argument_principle',
    'C3': 'computations/C3_gate_family',
    'C4': 'computations/C4_trace_formula',
    'C5': 'computations/C5_gates_extended',
    'C6': 'computations/C6_prime_flow',
    'C7': 'computations/C7_wave_dynamics',
    'C8': 'computations/C8_stats_ladder',
    'theorems': 'monograph/theorems_volume',
    'appendix': 'monograph/appendix_volume',
}
STEM = {'theorems': 'monograph_theorems', 'appendix': 'monograph_appendix'}


def dest_for(key, lang, ext):
    d = DEST[key]
    if key.startswith('C'):
        return os.path.join(ROOT, d, f"monograph_{lang}.{ext}")
    return os.path.join(ROOT, d, f"{STEM[key]}_{lang}.{ext}")


def main():
    tmp = os.path.join(ROOT, 'monograph', 'content', '_json')
    os.makedirs(tmp, exist_ok=True)
    jobs = []
    for lang, docs in DOCS.items():
        for key, doc in docs.items():
            jp = os.path.join(tmp, f"{key}_{lang}.json")
            json.dump(doc, open(jp, 'w'), ensure_ascii=False, indent=1)
            jobs.append((key, lang, jp))
    only = sys.argv[1:] or None
    for key, lang, jp in jobs:
        if only and key not in only:
            continue
        out_pdf = dest_for(key, lang, 'pdf')
        os.makedirs(os.path.dirname(out_pdf), exist_ok=True)
        print(f"--- {key} [{lang}]")
        subprocess.run([sys.executable, os.path.join(HERE, 'render_pdf.py'),
                        jp, out_pdf, lang], check=True)
        subprocess.run(['node', os.path.join(HERE, 'render_docx.js'),
                        jp, dest_for(key, lang, 'docx'), lang], check=True)
        subprocess.run([sys.executable,
                        os.path.join(HERE, 'postprocess_docx.py'),
                        dest_for(key, lang, 'docx')], check=True)
    print("ALL MONOGRAPHS DONE")


if __name__ == '__main__':
    main()
