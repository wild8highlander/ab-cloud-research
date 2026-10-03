#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
w1_report_build.py — сборка тела научного отчёта W1 (ReportLab,
TocDocTemplate + multiBuild, русский язык, FreeSerif для кириллицы).
Обложка рендерится отдельно (html2poster.js, Template 03) и подшивается
через pypdf.
"""
import hashlib
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer,
                                PageBreak, Table, TableStyle, Image,
                                KeepTogether, CondPageBreak, HRFlowable)
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.lib import colors
from PIL import Image as PILImage

from w1_palette import (PAGE_BG, SECTION_BG, CARD_BG, TABLE_STRIPE,
                        HEADER_FILL, COVER_BLOCK, BORDER, ICON, ACCENT,
                        ACCENT_2, TEXT_PRIMARY, TEXT_MUTED, SEM_INFO)
import w1_report_content as C

# ── fonts ───────────────────────────────────────────────────────────────────
FONT_DIR = '/usr/share/fonts'
pdfmetrics.registerFont(TTFont('NotoSerifSC', f'{FONT_DIR}/truetype/noto-serif-sc/NotoSerifSC-Regular.ttf'))
pdfmetrics.registerFont(TTFont('NotoSerifSC-Bold', f'{FONT_DIR}/truetype/noto-serif-sc/NotoSerifSC-Bold.ttf'))
pdfmetrics.registerFont(TTFont('FreeSerif', f'{FONT_DIR}/truetype/freefont/FreeSerif.ttf'))
pdfmetrics.registerFont(TTFont('FreeSerif-Bold', f'{FONT_DIR}/truetype/freefont/FreeSerifBold.ttf'))
pdfmetrics.registerFont(TTFont('FreeSerif-Italic', f'{FONT_DIR}/truetype/freefont/FreeSerifItalic.ttf'))
pdfmetrics.registerFont(TTFont('FreeSerif-BoldItalic', f'{FONT_DIR}/truetype/freefont/FreeSerifBoldItalic.ttf'))
pdfmetrics.registerFont(TTFont('DejaVuSans', f'{FONT_DIR}/truetype/dejavu/DejaVuSansMono.ttf'))
registerFontFamily('NotoSerifSC', normal='NotoSerifSC', bold='NotoSerifSC-Bold')
registerFontFamily('FreeSerif', normal='FreeSerif', bold='FreeSerif-Bold',
                   italic='FreeSerif-Italic', boldItalic='FreeSerif-BoldItalic')
registerFontFamily('DejaVuSans', normal='DejaVuSans', bold='DejaVuSans')

from report_font_fallback import install_font_fallback  # noqa: E402
install_font_fallback()

# ── layout constants ────────────────────────────────────────────────────────
OUT = os.path.normpath(os.path.join(_HERE, '..', '..', 'report'))
FIGDIR = os.path.normpath(os.path.join(_HERE, '..', '..', 'figures'))
os.makedirs(OUT, exist_ok=True)
BODY_PDF = os.path.join(OUT, '_body.pdf')

L_MARGIN = R_MARGIN = 0.9 * inch
T_MARGIN = 0.85 * inch
B_MARGIN = 0.85 * inch
AVAIL_W = A4[0] - L_MARGIN - R_MARGIN
AVAIL_H = A4[1] - T_MARGIN - B_MARGIN
MAX_KEEP = A4[1] * 0.4

# ── styles ──────────────────────────────────────────────────────────────────
st_body = ParagraphStyle('Body', fontName='FreeSerif', fontSize=10.5,
                         leading=16.5, alignment=TA_JUSTIFY,
                         textColor=TEXT_PRIMARY, spaceAfter=9)
st_h1 = ParagraphStyle('H1', fontName='FreeSerif-Bold', fontSize=17,
                       leading=23, textColor=HEADER_FILL,
                       spaceBefore=16, spaceAfter=10)
st_h2 = ParagraphStyle('H2', fontName='FreeSerif-Bold', fontSize=13,
                       leading=18, textColor=TEXT_PRIMARY,
                       spaceBefore=12, spaceAfter=7)
st_abstract = ParagraphStyle('Abstract', fontName='FreeSerif-Italic',
                             fontSize=10, leading=15.5, alignment=TA_JUSTIFY,
                             textColor=TEXT_PRIMARY,
                             leftIndent=14, rightIndent=14,
                             borderColor=BORDER, borderWidth=0.8,
                             borderPadding=9, spaceAfter=12)
st_bullet = ParagraphStyle('Bullet', fontName='FreeSerif', fontSize=10.5,
                           leading=16, alignment=TA_LEFT,
                           leftIndent=16, bulletIndent=4, spaceAfter=6)
st_caption = ParagraphStyle('Caption', fontName='FreeSerif', fontSize=8.8,
                            leading=12.5, alignment=TA_CENTER,
                            textColor=TEXT_MUTED, spaceBefore=4,
                            spaceAfter=6)
st_tbl_head = ParagraphStyle('TblHead', fontName='FreeSerif-Bold',
                             fontSize=9.6, leading=13, alignment=TA_CENTER,
                             textColor=colors.white)
st_tbl_cell = ParagraphStyle('TblCell', fontName='FreeSerif', fontSize=9.4,
                             leading=13, alignment=TA_LEFT,
                             textColor=TEXT_PRIMARY)
st_stat_big = ParagraphStyle('StatBig', fontName='FreeSerif-Bold',
                             fontSize=19, leading=23, textColor=ACCENT,
                             alignment=TA_CENTER)
st_stat_lbl = ParagraphStyle('StatLbl', fontName='FreeSerif', fontSize=8.2,
                             leading=11, textColor=TEXT_MUTED,
                             alignment=TA_CENTER)
st_bib = ParagraphStyle('Bib', fontName='FreeSerif', fontSize=9.6,
                        leading=14.5, alignment=TA_LEFT,
                        firstLineIndent=-20, leftIndent=20, spaceAfter=6)
st_toc_title = ParagraphStyle('TocTitle', fontName='FreeSerif-Bold',
                              fontSize=17, leading=23,
                              textColor=HEADER_FILL, spaceAfter=14)


class TocDocTemplate(SimpleDocTemplate):
    def afterFlowable(self, flowable):
        if hasattr(flowable, 'bookmark_name'):
            level = getattr(flowable, 'bookmark_level', 0)
            text = getattr(flowable, 'bookmark_text', '')
            key = getattr(flowable, 'bookmark_key', '')
            self.notify('TOCEntry', (level, text, self.page, key))


def add_heading(text, style, level=0):
    key = 'h_%s' % hashlib.md5(text.encode()).hexdigest()[:8]
    p = Paragraph('<a name="%s"/><b>%s</b>' % (key, text), style)
    p.bookmark_name = key
    p.bookmark_level = level
    p.bookmark_text = text
    p.bookmark_key = key
    return p


def safe_keep(elements):
    total = 0.0
    for el in elements:
        w, h = el.wrap(AVAIL_W, AVAIL_H)
        total += h
    if total <= MAX_KEEP:
        return [KeepTogether(elements)]
    if len(elements) >= 2:
        return [KeepTogether(elements[:2])] + list(elements[2:])
    return list(elements)


def embed_image(path, max_w=None, max_h=None):
    if max_w is None:
        max_w = AVAIL_W
    if max_h is None:
        max_h = AVAIL_H * 0.33
    im = PILImage.open(path)
    ow, oh = im.size
    ratio = min(max_w / ow, max_h / oh, 1.0)
    return Image(path, width=ow * ratio, height=oh * ratio)


def make_table(headers, rows, ratios):
    widths = [r * AVAIL_W * 0.98 for r in ratios]
    data = [[Paragraph('<b>%s</b>' % h, st_tbl_head) for h in headers]]
    for row in rows:
        data.append([Paragraph(str(c), st_tbl_cell) for c in row])
    t = Table(data, colWidths=widths, hAlign='CENTER', repeatRows=1)
    style = [
        ('BACKGROUND', (0, 0), (-1, 0), HEADER_FILL),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, BORDER),
        ('LEFTPADDING', (0, 0), (-1, -1), 7),
        ('RIGHTPADDING', (0, 0), (-1, -1), 7),
        ('TOPPADDING', (0, 0), (-1, -1), 5.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5.5),
    ]
    for i in range(1, len(data)):
        style.append(('BACKGROUND', (0, i), (-1, i),
                      colors.white if i % 2 else TABLE_STRIPE))
    t.setStyle(TableStyle(style))
    return t


def make_callouts(items):
    cells, labels = [], []
    for big, lbl in items:
        cells.append(Paragraph('<b>%s</b>' % big, st_stat_big))
        labels.append(Paragraph(lbl, st_stat_lbl))
    n = len(items)
    w = AVAIL_W * 0.94 / n
    t = Table([cells, labels], colWidths=[w] * n, hAlign='CENTER')
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), CARD_BG),
        ('BOX', (0, 0), (-1, -1), 0.8, BORDER),
        ('LINEBEFORE', (1, 0), (-1, -1), 0.8, BORDER),
        ('TOPPADDING', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 1), (-1, 1), 9),
        ('TOPPADDING', (0, 1), (-1, 1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 2),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    return t


def render_blocks(story, blocks):
    i = 0
    while i < len(blocks):
        b = blocks[i]
        kind = b[0]
        if kind == 'h1':
            head = add_heading(b[1], st_h1, level=0)
            rule = HRFlowable(width='100%', color=ACCENT, thickness=1.1,
                              spaceBefore=0, spaceAfter=8)
            story.append(CondPageBreak(AVAIL_H * 0.22))
            nxt = []
            if i + 1 < len(blocks) and blocks[i + 1][0] in ('body', 'abstract'):
                i += 1
                nb = blocks[i]
                para = Paragraph(nb[1], st_abstract if nb[0] == 'abstract'
                                 else st_body)
                nxt = [para]
            story.extend(safe_keep([head, rule] + nxt))
        elif kind == 'h2':
            head = add_heading(b[1], st_h2, level=1)
            nxt = []
            if i + 1 < len(blocks) and blocks[i + 1][0] == 'body':
                i += 1
                nxt = [Paragraph(blocks[i][1], st_body)]
            story.extend(safe_keep([head] + nxt))
        elif kind == 'body':
            story.append(Paragraph(b[1], st_body))
        elif kind == 'abstract':
            story.append(Paragraph(b[1], st_abstract))
        elif kind == 'bullet':
            for item in b[1]:
                story.append(Paragraph(item, st_bullet, bulletText='•'))
        elif kind == 'fig':
            path = os.path.join(FIGDIR, b[1])
            img = embed_image(path)
            cap = Paragraph(b[2], st_caption)
            story.append(Spacer(1, 10))
            story.extend(safe_keep([img, cap]))
            story.append(Spacer(1, 8))
        elif kind == 'table':
            headers, rows, ratios = b[1], b[2], b[3]
            story.append(Spacer(1, 10))
            story.append(make_table(headers, rows, ratios))
            story.append(Spacer(1, 12))
        elif kind == 'callouts':
            story.append(Spacer(1, 8))
            story.append(make_callouts(b[1]))
            story.append(Spacer(1, 12))
        elif kind == 'biblio':
            for item in b[1]:
                story.append(Paragraph(item, st_bib))
        i += 1


def main():
    doc = TocDocTemplate(
        BODY_PDF, pagesize=A4,
        leftMargin=L_MARGIN, rightMargin=R_MARGIN,
        topMargin=T_MARGIN, bottomMargin=B_MARGIN,
        title='Гиперболические волновые аттракторы — исследование W1',
        author='AB-Cloud Research / Z.ai', creator='Z.ai',
        subject='Численное воспроизведение самоорганизации волновых '
                'траекторий в анизотропной полости')

    story = []
    # ── TOC page ──
    story.append(Paragraph('<b>Содержание</b>', st_toc_title))
    toc = TableOfContents()
    toc.levelStyles = [
        ParagraphStyle('TOC1', fontName='FreeSerif-Bold', fontSize=11,
                       leading=17, leftIndent=6, textColor=TEXT_PRIMARY),
        ParagraphStyle('TOC2', fontName='FreeSerif', fontSize=10,
                       leading=15, leftIndent=24, textColor=TEXT_PRIMARY),
    ]
    story.append(toc)
    story.append(PageBreak())

    for ch in (C.CH1, C.CH2, C.CH3, C.CH4, C.CH5, C.CH6, C.CH7, C.CH8):
        render_blocks(story, ch)

    doc.multiBuild(story)
    print('body built:', BODY_PDF)


if __name__ == '__main__':
    main()
