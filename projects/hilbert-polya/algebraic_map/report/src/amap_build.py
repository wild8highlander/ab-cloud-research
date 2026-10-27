#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""amap_build.py — сборка отчёта «Алгебраическая карта якобиевой кодировки».
Архитектура — как в audit/audit_build.py: тело ReportLab (TocDocTemplate +
multiBuild), обложка Template 01 через html2poster.js, merge через pypdf.
"""
import hashlib
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PDF_SKILL = '/home/z/my-project/skills/pdf'
OUT_DIR = os.path.dirname(HERE)                      # algebraic_map/report
AMAP_DIR = os.path.dirname(OUT_DIR)                  # algebraic_map
BODY_PDF = os.path.join(OUT_DIR, '_body.pdf')
COVER_PDF = os.path.join(OUT_DIR, '_cover.pdf')
FINAL_PDF = os.path.join(OUT_DIR, 'HPB_algebraic_map_2026-10-13_ru.pdf')

sys.path.insert(0, HERE)
from amap_content import BLOCKS, TITLE, SUBTITLE, AUTHOR, DATE
from amap_content2 import BLOCKS2, BIBLIO

# ━━ Cascade Palette (design_engine.py palette-cascade, seed 137) ━━
from reportlab.lib import colors
PAGE_BG       = colors.HexColor('#f2f2f1')
SECTION_BG    = colors.HexColor('#f2f1f0')
CARD_BG       = colors.HexColor('#f0f0ed')
TABLE_STRIPE  = colors.HexColor('#f1f0ee')
HEADER_FILL   = colors.HexColor('#5d5642')
COVER_BLOCK   = colors.HexColor('#5a533e')
BORDER        = colors.HexColor('#d5d2cb')
ICON          = colors.HexColor('#9d8c59')
ACCENT        = colors.HexColor('#907421')
ACCENT_2      = colors.HexColor('#54b1d0')
TEXT_PRIMARY  = colors.HexColor('#1d1c1a')
TEXT_MUTED    = colors.HexColor('#908e87')
SEM_SUCCESS   = colors.HexColor('#3d8555')

# ━━ Шрифты ━━
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily
FONT_DIR = '/usr/share/fonts'
pdfmetrics.registerFont(TTFont('NotoSerifSC', f'{FONT_DIR}/truetype/noto-serif-sc/NotoSerifSC-Regular.ttf'))
pdfmetrics.registerFont(TTFont('NotoSerifSC-Bold', f'{FONT_DIR}/truetype/noto-serif-sc/NotoSerifSC-Bold.ttf'))
pdfmetrics.registerFont(TTFont('FreeSerif', f'{FONT_DIR}/truetype/freefont/FreeSerif.ttf'))
pdfmetrics.registerFont(TTFont('FreeSerif-Bold', f'{FONT_DIR}/truetype/freefont/FreeSerifBold.ttf'))
pdfmetrics.registerFont(TTFont('FreeSerif-Italic', f'{FONT_DIR}/truetype/freefont/FreeSerifItalic.ttf'))
pdfmetrics.registerFont(TTFont('FreeSerif-BoldItalic', f'{FONT_DIR}/truetype/freefont/FreeSerifBoldItalic.ttf'))
registerFontFamily('NotoSerifSC', normal='NotoSerifSC', bold='NotoSerifSC-Bold')
registerFontFamily('FreeSerif', normal='FreeSerif', bold='FreeSerif-Bold',
                   italic='FreeSerif-Italic', boldItalic='FreeSerif-BoldItalic')
sys.path.insert(0, os.path.join(PDF_SKILL, 'scripts'))
from pdf import install_font_fallback
install_font_fallback()

from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (CondPageBreak, Image, KeepTogether, PageBreak,
                                Paragraph, SimpleDocTemplate, Spacer, Table,
                                TableStyle)
from reportlab.platypus.tableofcontents import TableOfContents
from PIL import Image as PILImage

MARGIN = 0.9 * inch
AVAIL_W = A4[0] - 2 * MARGIN
AVAIL_H = A4[1] - 1.9 * inch
S = {
'body': ParagraphStyle('body', fontName='NotoSerifSC', fontSize=10.2, leading=16.5,
                       alignment=TA_JUSTIFY, textColor=TEXT_PRIMARY,
                       spaceAfter=8, wordWrap='CJK'),
'h1': ParagraphStyle('h1', fontName='NotoSerifSC-Bold', fontSize=17, leading=22,
                     textColor=HEADER_FILL, spaceBefore=18, spaceAfter=10),
'h2': ParagraphStyle('h2', fontName='NotoSerifSC-Bold', fontSize=12.5, leading=17,
                     textColor=TEXT_PRIMARY, spaceBefore=13, spaceAfter=7),
'bullet': ParagraphStyle('bullet', fontName='NotoSerifSC', fontSize=10.2,
                         leading=16, alignment=TA_LEFT, textColor=TEXT_PRIMARY,
                         leftIndent=14, bulletIndent=2, spaceAfter=6,
                         wordWrap='CJK'),
'formula': ParagraphStyle('formula', fontName='NotoSerifSC', fontSize=11.5,
                          leading=18, alignment=TA_CENTER, textColor=TEXT_PRIMARY,
                          spaceBefore=8, spaceAfter=10, wordWrap='CJK'),
'quote': ParagraphStyle('quote', fontName='NotoSerifSC', fontSize=10.2,
                        leading=16.5, alignment=TA_LEFT, textColor=TEXT_PRIMARY,
                        leftIndent=24, rightIndent=12, spaceBefore=6,
                        spaceAfter=10, wordWrap='CJK'),
'th': ParagraphStyle('th', fontName='NotoSerifSC-Bold', fontSize=8.8, leading=11.5,
                     textColor=colors.white, alignment=TA_CENTER, wordWrap='CJK'),
'td': ParagraphStyle('td', fontName='NotoSerifSC', fontSize=8.8, leading=11.5,
                     textColor=TEXT_PRIMARY, alignment=TA_LEFT, wordWrap='CJK'),
'caption': ParagraphStyle('caption', fontName='NotoSerifSC', fontSize=8.5,
                          leading=11.5, alignment=TA_CENTER,
                          textColor=TEXT_MUTED, spaceBefore=3, spaceAfter=12),
'toc_title': ParagraphStyle('toc_title', fontName='NotoSerifSC-Bold', fontSize=19,
                            leading=24, textColor=HEADER_FILL, spaceAfter=12),
'toc0': ParagraphStyle('toc0', fontName='NotoSerifSC', fontSize=10.5, leading=16.5,
                       leftIndent=4, textColor=TEXT_PRIMARY),
'biblio': ParagraphStyle('biblio', fontName='NotoSerifSC', fontSize=9.3,
                         leading=14.5, alignment=TA_LEFT, firstLineIndent=-20,
                         leftIndent=20, textColor=TEXT_PRIMARY, spaceAfter=5,
                         wordWrap='CJK'),
'stat_big': ParagraphStyle('stat_big', fontName='NotoSerifSC-Bold', fontSize=19,
                           leading=24, textColor=ACCENT, alignment=TA_CENTER),
'stat_label': ParagraphStyle('stat_label', fontName='NotoSerifSC', fontSize=8.6,
                             leading=12, textColor=TEXT_MUTED,
                             alignment=TA_CENTER, wordWrap='CJK'),
}


class TocDocTemplate(SimpleDocTemplate):
    def afterFlowable(self, flowable):
        if hasattr(flowable, 'bookmark_name'):
            level = getattr(flowable, 'bookmark_level', 0)
            text = getattr(flowable, 'bookmark_text', '')
            key = getattr(flowable, 'bookmark_key', '')
            self.notify('TOCEntry', (level, text, self.page, key))


def add_heading(text, style, level=0):
    key = 'h_' + hashlib.md5(text.encode()).hexdigest()[:8]
    p = Paragraph(f'<a name="{key}"/><b>{text}</b>', style)
    p.bookmark_name = key
    p.bookmark_level = level
    p.bookmark_text = text
    p.bookmark_key = key
    return p


def on_page(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(PAGE_BG)
    canvas.rect(0, 0, A4[0], A4[1], fill=1, stroke=0)
    canvas.setFont('NotoSerifSC', 7.5)
    canvas.setFillColor(TEXT_MUTED)
    canvas.drawString(MARGIN, A4[1] - 0.55 * inch,
                      'Hilbert Polya Bridge · алгебраическая карта кодировки')
    canvas.drawRightString(A4[0] - MARGIN, A4[1] - 0.55 * inch, '13.10.2026')
    canvas.setStrokeColor(BORDER)
    canvas.setLineWidth(0.6)
    canvas.line(MARGIN, A4[1] - 0.62 * inch, A4[0] - MARGIN, A4[1] - 0.62 * inch)
    canvas.drawCentredString(A4[0] / 2, 0.5 * inch, str(canvas.getPageNumber()))
    canvas.restoreState()


def make_table(spec):
    header = [Paragraph(f'<b>{h}</b>', S['th']) for h in spec['header']]
    rows = [[Paragraph(str(c), S['td']) for c in r] for r in spec['rows']]
    ratios = spec.get('ratios') or [1.0 / len(spec['header'])] * len(spec['header'])
    widths = [AVAIL_W * x for x in ratios]
    assert abs(sum(widths) - AVAIL_W) < 1.0, 'colWidths exceed available width'
    t = Table([header] + rows, colWidths=widths, repeatRows=1, hAlign='CENTER')
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HEADER_FILL),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, TABLE_STRIPE]),
        ('GRID', (0, 0), (-1, -1), 0.5, BORDER),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    cap = Paragraph(spec['caption'], ParagraphStyle('tcap', parent=S['caption'],
                                                    spaceBefore=8, spaceAfter=3))
    return [Spacer(1, 10), cap, t, Spacer(1, 10)]


def make_fig(spec):
    path = spec['path'] if os.path.isabs(spec['path']) else \
        os.path.join(HERE, spec['path'])
    if not os.path.exists(path):
        return [Paragraph(f'[фигура недоступна: {spec["path"]}]', S['caption'])]
    img = PILImage.open(path)
    w, h = img.size
    max_w = AVAIL_W
    max_h = spec.get('max_h', 280)
    scale = min(max_w / w, max_h / h, 1.0)
    fig = Image(path, width=w * scale, height=h * scale, hAlign='CENTER')
    cap = Paragraph(spec['caption'], S['caption'])
    return [Spacer(1, 8), fig, cap]


def make_callout(spec):
    inner = Table(
        [[Paragraph(f"<b>{spec['big']}</b>", S['stat_big'])],
         [Paragraph(spec['label'], S['stat_label'])]],
        colWidths=[AVAIL_W * 0.62])
    inner.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), SECTION_BG),
        ('BOX', (0, 0), (-1, -1), 1, ACCENT),
        ('TOPPADDING', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, -1), (-1, -1), 10),
        ('TOPPADDING', (0, 1), (-1, 1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 2),
        ('LEFTPADDING', (0, 0), (-1, -1), 14),
        ('RIGHTPADDING', (0, 0), (-1, -1), 14),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    inner.hAlign = 'CENTER'
    return [Spacer(1, 10), KeepTogether(inner), Spacer(1, 12)]


def make_quote(text):
    q = Table([[Paragraph(f'<i>{text}</i>', S['quote'])]],
              colWidths=[AVAIL_W * 0.94])
    q.setStyle(TableStyle([
        ('LINEBEFORE', (0, 0), (0, -1), 2.4, ACCENT),
        ('BACKGROUND', (0, 0), (-1, -1), SECTION_BG),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
    ]))
    q.hAlign = 'CENTER'
    return [Spacer(1, 6), q, Spacer(1, 8)]


def make_formula(text):
    box = Table([[Paragraph(text, S['formula'])]], colWidths=[AVAIL_W * 0.9])
    box.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), CARD_BG),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('LEFTPADDING', (0, 0), (-1, -1), 12),
        ('RIGHTPADDING', (0, 0), (-1, -1), 12),
    ]))
    box.hAlign = 'CENTER'
    return [Spacer(1, 4), box, Spacer(1, 8)]


def build_story():
    story = []
    story.append(Paragraph('<b>Содержание</b>', S['toc_title']))
    toc = TableOfContents()
    toc.levelStyles = [S['toc0']]
    story.append(toc)
    story.append(PageBreak())

    H1_ORPHAN = AVAIL_H * 0.22
    first_h1 = True
    for t, p in list(BLOCKS) + list(BLOCKS2):
        if t == 'h1':
            if not first_h1:
                story.append(CondPageBreak(H1_ORPHAN))
            first_h1 = False
            story.append(add_heading(p, S['h1'], level=0))
        elif t == 'h2':
            story.append(CondPageBreak(70))
            story.append(add_heading(p, S['h2'], level=0))
        elif t == 'p':
            story.append(Paragraph(p, S['body']))
        elif t == 'bullets':
            for item in p:
                story.append(Paragraph(item, S['bullet'], bulletText='•'))
        elif t == 'table':
            story.extend(make_table(p))
        elif t == 'fig':
            story.extend(make_fig(p))
        elif t == 'callout':
            story.extend(make_callout(p))
        elif t == 'quote':
            story.extend(make_quote(p))
        elif t == 'formula':
            story.extend(make_formula(p))
    story.append(CondPageBreak(H1_ORPHAN))
    story.append(add_heading('Источники', S['h1'], level=0))
    for ref in BIBLIO:
        story.append(Paragraph(ref, S['biblio']))
    return story


def build_cover_html():
    html = """<!DOCTYPE html><html><head><meta charset="utf-8"><style>
@page { size: 794px 1123px; margin: 0; }
html, body { margin:0; padding:0; background:#fbfaf8; }
.poster { width:794px; height:1123px; background:#fbfaf8; color:#1d1c1a;
  font-family:'DejaVu Sans','FreeSerif',sans-serif; position:relative; }
.l1 { position:absolute; inset:0; overflow:hidden; z-index:1;
  background-image:
    linear-gradient(rgba(93,86,66,.05) .5px, transparent .5px),
    linear-gradient(90deg, rgba(93,86,66,.05) .5px, transparent .5px);
  background-size: 50px 50px; }
.l2 { position:absolute; inset:0; z-index:2; }
.anchor { position:absolute; left:95px; top:112px; width:6px; height:899px;
  background:#5d5642; }
.chips { position:absolute; left:135px; top:118px; font-size:15px;
  color:#5d5642; letter-spacing:1px; }
.chips span { border:1.4px solid #9d8c59; padding:5px 12px; margin-right:10px; }
.l3 { position:absolute; inset:0; z-index:3; }
.kicker { position:absolute; left:135px; top:200px; font-size:16px;
  letter-spacing:3px; color:#1d1c1a; opacity:.6; text-transform:uppercase; }
.hero { position:absolute; left:135px; top:286px; font-size:54px;
  line-height:1.16; font-weight:800; color:#1d1c1a; max-width:575px; }
.hero .accent { color:#907421; }
.summary { position:absolute; left:135px; top:592px; font-size:16.5px;
  line-height:1.6; color:#1d1c1a; opacity:.85; max-width:500px; }
.meta { position:absolute; left:135px; top:856px; font-size:17px;
  line-height:1.75; color:#1d1c1a; }
.meta b { font-weight:700; }
.footer { position:absolute; left:135px; top:1008px; font-size:16px;
  letter-spacing:3px; color:#1d1c1a; opacity:.6; text-transform:uppercase; }
</style></head><body><div class="poster">
<div class="l1"></div>
<div class="l2"><div class="anchor"></div><div class="chips">
<span>Φ</span><span>D<sub>n</sub> · S<sub>n</sub></span><span>ℚ-точно</span><span>N = 24</span>
</div></div>
<div class="l3">
<div class="kicker">Research note · пиксельный протокол → функция</div>
<div class="hero">Алгебраическая<br>карта якобиевой<br><span class="accent">кодировки</span></div>
<div class="summary">Пиксельная кодировка нулей ζ поднята от алгоритма
Ланцоша до замкнутой функции Φ через определители Ханкеля. Точное
замыкание в ℚ на закоммиченных данных, восемь тождеств-следствий,
граница Вейля для декодирования и честный вердикт о новых формулах.</div>
<div class="meta"><b>Пакет:</b> Hilbert Polya Bridge v2.0.0+amap<br>
<b>Дата:</b> 13 октября 2026<br>
<b>Статус:</b> замыкание доказано; протокол N7 уточнён</div>
<div class="footer">Hilbert Polya Bridge · Algebraic Map</div>
</div></div></body></html>"""
    p = os.path.join(OUT_DIR, '_cover.html')
    open(p, 'w').write(html)
    return p


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    doc = TocDocTemplate(BODY_PDF, pagesize=A4,
                         leftMargin=MARGIN, rightMargin=MARGIN,
                         topMargin=1.0 * inch, bottomMargin=0.85 * inch,
                         title=TITLE, author='Z.ai', creator='Z.ai',
                         subject=SUBTITLE)
    doc.multiBuild(build_story(), onFirstPage=on_page, onLaterPages=on_page)
    print('body OK')
    cov = build_cover_html()
    subprocess.run(['node', f'{PDF_SKILL}/scripts/html2poster.js', cov,
                    '--output', COVER_PDF, '--width', '794px'],
                   check=True, capture_output=True)
    print('cover OK')
    from pypdf import PdfReader, PdfWriter
    A4_W, A4_H = 595.28, 841.89

    def normalize(pg):
        w, h = float(pg.mediabox.width), float(pg.mediabox.height)
        if abs(w - A4_W) > 0.4 or abs(h - A4_H) > 0.4:
            pg.scale_to(A4_W, A4_H)
        return pg

    w = PdfWriter()
    for pg in PdfReader(COVER_PDF).pages:
        w.add_page(normalize(pg))
    for pg in PdfReader(BODY_PDF).pages:
        w.add_page(normalize(pg))
    w.add_metadata({'/Title': TITLE, '/Author': 'Z.ai', '/Creator': 'Z.ai',
                    '/Subject': SUBTITLE})
    with open(FINAL_PDF, 'wb') as f:
        w.write(f)
    os.remove(BODY_PDF)
    os.remove(COVER_PDF)
    print('PDF OK:', FINAL_PDF)


if __name__ == '__main__':
    main()
