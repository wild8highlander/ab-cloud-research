#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""make_monographs.py — дамп контента и рендер монографий ABQP.

v0.1.0: V20 × {ru, en} → computations/V20_processor_compiler/
monograph_{lang}.{pdf,docx} + DOCS-исходники monograph/content/_json/.
Запуск: python3 scripts/make_monographs.py [V20]
"""
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, 'monograph'))
sys.path.insert(0, os.path.join(ROOT, 'monograph', 'content'))

from content import en_v20, ru_v20  # noqa: E402

DOCS = {'ru': {'V20': ru_v20.V20}, 'en': {'V20': en_v20.V20}}
VDIRS = {'V20': 'V20_processor_compiler'}
FIGNUM = {'V20': 1}


def _inject_figures(doc, key):
    """Вставляет рисунки кампании (fig01, fig05) по секциям; в DOC-схеме
    рисунки уже прописаны в контенте — здесь дублируем только путь
    figures_hires для переносимости."""
    return doc


def dest_for(key, lang, ext):
    return os.path.join(ROOT, 'computations', VDIRS[key],
                        f'monograph_{lang}.{ext}')


def main():
    only = sys.argv[1:] or None
    tmp = os.path.join(ROOT, 'monograph', 'content', '_json')
    os.makedirs(tmp, exist_ok=True)
    jobs = []
    for lang, docs in DOCS.items():
        for key, doc in docs.items():
            doc = _inject_figures(json.loads(json.dumps(doc)), key)
            jp = os.path.join(tmp, f'{key}_{lang}.json')
            json.dump(doc, open(jp, 'w', encoding='utf-8'),
                      ensure_ascii=False, indent=1)
            jobs.append((key, lang, jp))
    for key, lang, jp in jobs:
        if only and key not in only:
            continue
        out_pdf = dest_for(key, lang, 'pdf')
        out_docx = dest_for(key, lang, 'docx')
        os.makedirs(os.path.dirname(out_pdf), exist_ok=True)
        print(f'--- {key} [{lang}]')
        subprocess.run([sys.executable, os.path.join(HERE, 'render_pdf.py'),
                        jp, out_pdf, lang], check=True)
        subprocess.run([sys.executable, os.path.join(HERE, 'render_docx.py'),
                        jp, out_docx, lang], check=True)
    print('ALL MONOGRAPHS DONE')


if __name__ == '__main__':
    main()
