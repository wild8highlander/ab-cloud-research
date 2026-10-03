#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""w1_merge.py — подшивка обложки к телу отчёта W1 (pypdf, нормализация A4)."""
from pypdf import PdfReader, PdfWriter

A4_W, A4_H = 595.28, 841.89

import os
_HERE = os.path.dirname(os.path.abspath(__file__))
COVER = os.path.join(_HERE, 'w1_cover.pdf')
BODY = os.path.normpath(os.path.join(_HERE, '..', '..', 'report', '_body.pdf'))
OUT = os.path.normpath(os.path.join(
    _HERE, '..', '..', 'report',
    'Отчёт_W1_гиперболические_волновые_аттракторы.pdf'))


def normalize(page):
    box = page.mediabox
    w, h = float(box.width), float(box.height)
    if abs(w - A4_W) > 0.5 or abs(h - A4_H) > 0.5:
        page.scale_to(A4_W, A4_H)
    return page


def main():
    writer = PdfWriter()
    writer.add_page(normalize(PdfReader(COVER).pages[0]))
    for p in PdfReader(BODY).pages:
        writer.add_page(normalize(p))
    writer.add_metadata({
        '/Title': 'Гиперболические волновые аттракторы — исследование W1',
        '/Author': 'AB-Cloud Research / Z.ai',
        '/Creator': 'Z.ai',
        '/Subject': 'Численное воспроизведение самоорганизации волновых '
                    'траекторий в анизотропной полости',
    })
    with open(OUT, 'wb') as f:
        writer.write(f)
    print('merged:', OUT, '| pages:', len(writer.pages))


if __name__ == '__main__':
    main()
