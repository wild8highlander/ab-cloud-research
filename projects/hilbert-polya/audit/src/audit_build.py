#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""audit_build.py — сборка аналитического отчёта (PDF, ReportLab).
Обложка — Template 01 (HUD) через html2poster.js; тело — ReportLab с TOC.
"""
import hashlib
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PDF_SKILL = os.environ.get('PDF_SKILL', '/home/z/my-project/skills/pdf')
# вывод — в audit/ репозитория (скрипт лежит в <repo>/Hilbert_Polya/audit/src)
AUDIT_DIR = os.path.dirname(HERE)
OUT_DIR = os.environ.get('AUDIT_OUT_DIR', AUDIT_DIR)
BODY_PDF = os.path.join(OUT_DIR, '_body.pdf')
COVER_PDF = os.path.join(OUT_DIR, '_cover.pdf')
FINAL_PDF = os.path.join(OUT_DIR, 'HPB_audit_canonization_2026-10-13_ru.pdf')

sys.path.insert(0, HERE)
from audit_content import BLOCKS as B1, TITLE, SUBTITLE, AUTHOR, DATE, BIBLIO
from audit_content2 import BLOCKS2
from audit_content3 import BLOCKS3

# ━━ Cascade Palette (design_engine.py palette-cascade, seed 96) ━━
from reportlab.lib import colors
PAGE_BG       = colors.HexColor('#f6f6f5')
SECTION_BG    = colors.HexColor('#f0efee')
CARD_BG       = colors.HexColor('#eaeae8')
TABLE_STRIPE  = colors.HexColor('#eeedeb')
HEADER_FILL   = colors.HexColor('#58513b')
COVER_BLOCK   = colors.HexColor('#5b543e')
BORDER        = colors.HexColor('#d9d4c7')
ICON          = colors.HexColor('#887642')
ACCENT        = colors.HexColor('#907422')
ACCENT_2      = colors.HexColor('#6f4fd0')
TEXT_PRIMARY  = colors.HexColor('#262522')
TEXT_MUTED    = colors.HexColor('#817f77')
SEM_SUCCESS   = colors.HexColor('#408c59')
SEM_WARNING   = colors.HexColor('#877248')
SEM_ERROR     = colors.HexColor('#a8554e')

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

# ━━ Платипус ━━
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
'quote': ParagraphStyle('quote', fontName='NotoSerifSC', fontSize=10.2,
                        leading=16.5, alignment=TA_LEFT, textColor=TEXT_PRIMARY,
                        leftIndent=24, rightIndent=12, spaceBefore=6,
                        spaceAfter=10, wordWrap='CJK',
                        borderColor=ACCENT, borderWidth=0, ),
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
                      'Hilbert Polya Bridge · аудит пакета')
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
    path = os.path.join(HERE, spec['path'])
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


def merge_blocks():
    """Вставка углублённых групп 5а/6а/7а в основной поток."""
    groups = {'6.': BLOCKS2[:13], }  # placeholder, пересобираем ниже
    # разбиваем BLOCKS2 на три группы по маркерам h1
    g5, g6, g7 = [], [], []
    cur = None
    for t, p in BLOCKS2:
        if t == 'h1':
            cur = '5' if p.startswith('5') else ('6' if p.startswith('6') else '7')
        {'5': g5, '6': g6, '7': g7}[cur].append((t, p))
    out = []
    for blk in B1:
        t, p = blk
        if t == 'h1':
            if p.startswith('6.'):
                out.extend(g5)
            elif p.startswith('7.'):
                out.extend(g6)
            elif p.startswith('8.'):
                out.extend(g7)
        out.append(blk)
    out.extend(BLOCKS3)
    return out


def build_story():
    story = []
    story.append(Paragraph('<b>Содержание</b>', S['toc_title']))
    toc = TableOfContents()
    toc.levelStyles = [S['toc0']]
    story.append(toc)
    story.append(PageBreak())

    H1_ORPHAN = AVAIL_H * 0.22
    first_h1 = True
    for t, p in merge_blocks():
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
                story.append(Paragraph(item, S['bullet'],
                                       bulletText='•'))
        elif t == 'table':
            story.extend(make_table(p))
        elif t == 'fig':
            story.extend(make_fig(p))
        elif t == 'callout':
            story.extend(make_callout(p))
        elif t == 'quote':
            story.extend(make_quote(p))
    # источники
    story.append(CondPageBreak(H1_ORPHAN))
    story.append(add_heading('Источники', S['h1'], level=0))
    for ref in BIBLIO:
        story.append(Paragraph(ref, S['biblio']))
    return story


def build_cover_html():
    title_lines = ('Hilbert Polya<br>Bridge'.split('<br>'))
    html = """<!DOCTYPE html><html><head><meta charset="utf-8"><style>
@page { size: 794px 1123px; margin: 0; }
html, body { margin:0; padding:0; background:#fbfaf8; }
.poster { width:794px; height:1123px; background:#fbfaf8; color:#262522;
  font-family:'DejaVu Sans','FreeSerif',sans-serif; position:relative; }
.l1 { position:absolute; inset:0; overflow:hidden; z-index:1;
  background-image:
    linear-gradient(rgba(88,81,59,.05) .5px, transparent .5px),
    linear-gradient(90deg, rgba(88,81,59,.05) .5px, transparent .5px);
  background-size: 50px 50px; }
.l2 { position:absolute; inset:0; z-index:2; }
.anchor { position:absolute; left:95px; top:112px; width:6px; height:899px;
  background:#58513b; }
.l3 { position:absolute; inset:0; z-index:3; }
.kicker { position:absolute; left:135px; top:168px; font-size:16px;
  letter-spacing:3px; color:#262522; opacity:.6; text-transform:uppercase; }
.hero { position:absolute; left:135px; top:300px; font-size:58px;
  line-height:1.15; font-weight:800; color:#262522; max-width:560px; }
.hero .accent { color:#907422; }
.summary { position:absolute; left:135px; top:560px; font-size:16.5px;
  line-height:1.6; color:#262522; opacity:.85; max-width:476px; }
.meta { position:absolute; left:135px; top:842px; font-size:17px;
  line-height:1.75; color:#262522; }
.meta b { font-weight:700; }
.footer { position:absolute; left:135px; top:1006px; font-size:16px;
  letter-spacing:3px; color:#262522; opacity:.6; text-transform:uppercase; }
</style></head><body><div class="poster">
<div class="l1"></div>
<div class="l2"><div class="anchor"></div></div>
<div class="l3">
<div class="kicker">Аудит пакета · канонизация · дорожная карта</div>
<div class="hero">Hilbert Polya<br>Bridge:<br><span class="accent">аудит и
единая версия</span></div>
<div class="summary">Монографический слой и его унификация в канонический том,
полная проверка пиксельного протокола второго фильма, строго научный разбор
границ пакета и дорожная карта «оператор кодирует нули»: теоретический мост,
слепая независимость H, новые кампании и литературные якоря.</div>
<div class="meta"><b>Рабочая копия пакета:</b> коммит e913629 · v2.0.0<br>
<b>Дата отчёта:</b> 13 октября 2026<br>
<b>Статус:</b> аудит завершён; исправления внесены</div>
<div class="footer">Hilbert Polya Bridge · Research Audit</div>
</div></div></body></html>"""
    p = os.path.join(OUT_DIR, '_cover.html')
    open(p, 'w').write(html)
    return p


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    doc = TocDocTemplate(BODY_PDF, pagesize=A4,
                         leftMargin=MARGIN, rightMargin=MARGIN,
                         topMargin=1.0 * inch, bottomMargin=0.85 * inch,
                         title=TITLE, author=AUTHOR, creator='Z.ai',
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
    cov_html = os.path.join(OUT_DIR, '_cover.html')
    if os.path.exists(cov_html):
        os.remove(cov_html)
    print('PDF OK:', FINAL_PDF)


if __name__ == '__main__':
    main()
