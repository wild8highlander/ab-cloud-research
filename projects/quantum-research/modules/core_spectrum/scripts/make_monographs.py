#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""make_monographs.py — дамп контента и рендер всех монографий серии.

34 документа: V1–V15 × {ru,en} → computations/V*/monograph_{lang}.{pdf,docx};
theorems, appendix × {ru,en} → monograph/*_volume/;
плюс 6 отдельных папок теорем monograph/theorems/T0K_*/theorem_T0K_{lang}.
Запуск: python3 scripts/make_monographs.py [ключи...]
"""
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, 'monograph'))
sys.path.insert(0, os.path.join(ROOT, 'monograph', 'content'))

from content import ru_part1, ru_part2, ru_part3, ru_part4, ru_part5, \
    ru_part6  # noqa: E402
from content import en_part1, en_part2, en_part3, en_part4, en_part5, \
    en_part6  # noqa: E402

DOCS = {
    'ru': {**ru_part1.DOCS, **ru_part2.DOCS, **ru_part3.DOCS,
           **ru_part4.DOCS, **ru_part5.DOCS, **ru_part6.DOCS},
    'en': {**en_part1.DOCS, **en_part2.DOCS, **en_part3.DOCS,
           **en_part4.DOCS, **en_part5.DOCS, **en_part6.DOCS},
}

VDIRS = {
    'V1': 'V01_blind_spectrum', 'V2': 'V02_null_models',
    'V3': 'V03_critical_line_scan', 'V4': 'V04_operator_passport',
    'V5': 'V05_limit_lattice', 'V6': 'V06_spectral_identity',
    'V7': 'V07_arithmetic_trace', 'V8': 'V08_self_adjoint',
    'V9': 'V09_symmetry_reduction', 'V10': 'V10_inverse_problem',
    'V11': 'V11_universality_split', 'V12': 'V12_interval_certificates',
    'V13': 'V13_formal_bridge', 'V14': 'V14_claim_audit',
    'V15': 'V15_li_criterion', 'V16': 'V16_full_hamiltonian',
    'V17': 'V17_electron_critical_line', 'V18': 'V18_ab_processor',
    'V19': 'V19_branch_stitching',
}
# fig16 — карта программы; кампании v1.1.0 используют fig17–fig19,
# v1.2.0 — fig20
FIGNUM = {**{f'V{i}': i for i in range(1, 16)},
          'V16': 17, 'V17': 18, 'V18': 19, 'V19': 20}
THM_DIRS = [
    ('Th1', 'T01_hermiticity'), ('Th2', 'T02_self_adjointness'),
    ('Th3', 'T03_certificates'), ('Th4', 'T04_li_spectral'),
    ('Th5', 'T05_block_reduction'), ('Th6', 'T06_trace_formula'),
]


def _inject_figure(doc, key):
    """Добавляет рисунок кампании в раздел «Результаты» (или последний)."""
    n = FIGNUM.get(key)
    if n is None:
        return doc
    fig = {'path': f'figures_hires/{{lang}}/fig{n:02d}_{{lang}}.png',
           'caption': {'ru': f'Рис. 1. Данные кампании {key} (600 dpi, '
                             f'файл figures_hires).',
                       'en': f'Fig. 1. Campaign {key} data (600 dpi, '
                             f'file figures_hires).'}}
    for sec in doc['sections']:
        if sec['h1'].startswith(('Результаты', 'Метод и результат',
                                 'Results', 'Method and result')):
            sec.setdefault('figure', fig)
            return doc
    doc['sections'][-1]['figure'] = fig
    return doc


def dest_for(key, lang, ext):
    if key in VDIRS:
        return os.path.join(ROOT, 'computations', VDIRS[key],
                            f'monograph_{lang}.{ext}')
    return os.path.join(ROOT, 'monograph', f'{key}_volume',
                        f'monograph_{key}_{lang}.{ext}')


def thm_doc(base, thm_key, lang):
    """Монография одной теоремы: ВСЕ секции с префиксом ключа
    (формулировка + сертификат/границы)."""
    secs = [s for s in base['sections'] if s['h1'].startswith(thm_key)]
    sec = secs[0]
    name = {'Th1': 'Эрмитовость', 'Th2': 'Самосопряжённость',
            'Th3': 'Сертификаты', 'Th4': 'Формула Ли',
            'Th5': 'Блочная редукция', 'Th6': 'Следовая формула'}
    name_en = {'Th1': 'Hermiticity', 'Th2': 'Self-adjointness',
               'Th3': 'Certificates', 'Th4': 'The Li formula',
               'Th5': 'Block reduction', 'Th6': 'The trace formula'}
    nm = name[thm_key] if lang == 'ru' else name_en[thm_key]
    meta = dict(base['meta'])
    meta['title'] = f'{thm_key}. {nm}'
    meta['subtitle'] = base['meta']['subtitle']
    meta['volume'] = thm_key
    return {'meta': meta, 'sections': secs}


def main():
    only = sys.argv[1:] or None
    tmp = os.path.join(ROOT, 'monograph', 'content', '_json')
    os.makedirs(tmp, exist_ok=True)
    jobs = []
    for lang, docs in DOCS.items():
        for key, doc in docs.items():
            doc = _inject_figure(json.loads(json.dumps(doc)), key)
            jp = os.path.join(tmp, f'{key}_{lang}.json')
            json.dump(doc, open(jp, 'w', encoding='utf-8'),
                      ensure_ascii=False, indent=1)
            jobs.append((key, lang, jp))
    # отдельные теоремы
    for lang in ('ru', 'en'):
        base = DOCS[lang]['theorems']
        for thm_key, dirname in THM_DIRS:
            d = thm_doc(base, thm_key, lang)
            jp = os.path.join(tmp, f'{thm_key}_{lang}.json')
            json.dump(d, open(jp, 'w', encoding='utf-8'),
                      ensure_ascii=False, indent=1)
            jobs.append((f'{thm_key}:{dirname}', lang, jp))
    for key, lang, jp in jobs:
        short = key.split(':')[0]
        if only and short not in only and key not in only:
            continue
        if ':' in key:
            thm_key, dirname = key.split(':')
            out_pdf = os.path.join(ROOT, 'monograph', 'theorems', dirname,
                                   f'theorem_{thm_key.lower()}_{lang}.pdf')
            out_docx = os.path.join(ROOT, 'monograph', 'theorems', dirname,
                                    f'theorem_{thm_key.lower()}_{lang}.docx')
        else:
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
