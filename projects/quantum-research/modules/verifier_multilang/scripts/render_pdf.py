#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""render_pdf.py — рендер монографий серии (ReportLab, самодостаточный).

Отличие от эталона: обложка рисуется векторно в самом ReportLab (не требует
node/playwright) — полная портируемость самосборки.
Использование: python3 render_pdf.py <content.json> <out.pdf> [lang]
"""
import json
import os
import sys

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.platypus import (CondPageBreak, Image, KeepTogether, Paragraph,
                                PageBreak, SimpleDocTemplate, Spacer, Table,
                                TableStyle)
from reportlab.platypus.tableofcontents import TableOfContents
from PIL import Image as PILImage

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ━━ Палитра серии «Critical Line & Copper» ━━
PAGE_BG = colors.HexColor('#f5f6f6')
HEADER_FILL = colors.HexColor('#3b4f58')
BORDER = colors.HexColor('#c7d3d9')
ACCENT = colors.HexColor('#298bbc')
ACCENT_2 = colors.HexColor('#c96f4a')
TEXT_PRIMARY = colors.HexColor('#222526')
TEXT_MUTED = colors.HexColor('#777e81')
SURFACE = colors.HexColor('#ebedee')
COVER_BG = colors.HexColor('#2e3f49')

FONT_DIR = '/usr/share/fonts'
pdfmetrics.registerFont(TTFont('FreeSerif', f'{FONT_DIR}/truetype/freefont/FreeSerif.ttf'))
pdfmetrics.registerFont(TTFont('FreeSerif-Bold', f'{FONT_DIR}/truetype/freefont/FreeSerifBold.ttf'))
pdfmetrics.registerFont(TTFont('FreeSerif-Italic', f'{FONT_DIR}/truetype/freefont/FreeSerifItalic.ttf'))
pdfmetrics.registerFont(TTFont('FreeSerif-BoldItalic', f'{FONT_DIR}/truetype/freefont/FreeSerifBoldItalic.ttf'))
registerFontFamily('FreeSerif', normal='FreeSerif', bold='FreeSerif-Bold',
                   italic='FreeSerif-Italic', boldItalic='FreeSerif-BoldItalic')

MARGIN = 0.9 * inch
AVAIL_W = A4[0] - 2 * MARGIN

S = {
'body': ParagraphStyle('body', fontName='FreeSerif', fontSize=10.5,
                       leading=16, alignment=TA_JUSTIFY,
                       textColor=TEXT_PRIMARY, spaceAfter=8),
'h1': ParagraphStyle('h1', fontName='FreeSerif-Bold', fontSize=19,
                     leading=24, textColor=HEADER_FILL, spaceBefore=18,
                     spaceAfter=10),
'caption': ParagraphStyle('caption', fontName='FreeSerif-Italic',
                          fontSize=8.5, leading=11.5, alignment=TA_CENTER,
                          textColor=TEXT_MUTED, spaceBefore=3, spaceAfter=10),
'thm': ParagraphStyle('thm', fontName='FreeSerif', fontSize=10,
                      leading=15, alignment=TA_JUSTIFY,
                      textColor=TEXT_PRIMARY, spaceAfter=6),
'thlabel': ParagraphStyle('thlabel', fontName='FreeSerif-Bold', fontSize=10.5,
                          leading=14, textColor=ACCENT_2, spaceBefore=8,
                          spaceAfter=3),
'proof': ParagraphStyle('proof', fontName='FreeSerif-Italic', fontSize=9.6,
                        leading=14, alignment=TA_JUSTIFY, leftIndent=14,
                        textColor=TEXT_PRIMARY, spaceAfter=8),
'th': ParagraphStyle('th', fontName='FreeSerif-Bold', fontSize=8.6,
                     leading=11, textColor=colors.white, alignment=TA_CENTER),
'td': ParagraphStyle('td', fontName='FreeSerif', fontSize=8.6, leading=11,
                     textColor=TEXT_PRIMARY, alignment=TA_LEFT, wordWrap='CJK'),
'toc0': ParagraphStyle('toc0', fontName='FreeSerif-Bold', fontSize=11.5,
                       leading=17, textColor=TEXT_PRIMARY, leftIndent=6),
'toctitle': ParagraphStyle('toctitle', fontName='FreeSerif-Bold', fontSize=20,
                           leading=25, textColor=HEADER_FILL, spaceAfter=14),
'meta': ParagraphStyle('meta', fontName='FreeSerif', fontSize=9.5,
                       leading=13.5, textColor=TEXT_MUTED, alignment=TA_LEFT),
}

LANG_TXT = {
'ru': {'toc': 'Содержание', 'page': 'стр.', 'theorem': 'Формулировка.',
       'proof': 'Доказательство.', 'series': 'ABQP JULIA RESEARCH PROGRAM'},
'en': {'toc': 'Contents', 'page': 'p.', 'theorem': 'Statement.',
       'proof': 'Proof.', 'series': 'ABQP JULIA RESEARCH PROGRAM'},
}


class TocDocTemplate(SimpleDocTemplate):
    def afterFlowable(self, flowable):
        if isinstance(flowable, Paragraph):
            if flowable.style.name == 'h1':
                txt = flowable.getPlainText()
                self.notify('TOCEntry', (0, txt, self.page))
                self.canv.bookmarkPage(txt[:60])
                self.canv.addOutlineEntry(txt[:80], txt[:60], level=0)


def on_page(canvas, doc, series, vol):
    canvas.saveState()
    canvas.setFillColor(PAGE_BG)
    canvas.rect(0, 0, A4[0], A4[1], fill=1, stroke=0)
    canvas.setFont('FreeSerif', 7.5)
    canvas.setFillColor(TEXT_MUTED)
    canvas.drawString(MARGIN, A4[1] - 0.55 * inch, series)
    canvas.drawRightString(A4[0] - MARGIN, A4[1] - 0.55 * inch, vol)
    canvas.drawCentredString(A4[0] / 2, 0.5 * inch, str(canvas.getPageNumber()))
    canvas.setStrokeColor(BORDER)
    canvas.setLineWidth(0.6)
    canvas.line(MARGIN, A4[1] - 0.62 * inch, A4[0] - MARGIN, A4[1] - 0.62 * inch)
    canvas.restoreState()


def make_table(spec):
    header = [Paragraph(h, S['th']) for h in spec['header']]
    rows = [[Paragraph(str(c), S['td']) for c in r] for r in spec['rows']]
    ratios = spec.get('ratios') or [1.0 / len(spec['header'])] * len(spec['header'])
    widths = [AVAIL_W * x for x in ratios]
    t = Table([header] + rows, colWidths=widths, repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HEADER_FILL),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, SURFACE]),
        ('GRID', (0, 0), (-1, -1), 0.5, BORDER),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    return [Paragraph(spec['caption'],
                      ParagraphStyle('tcap', parent=S['caption'],
                                     spaceBefore=8, spaceAfter=3)),
            t, Spacer(1, 8)]


def embed_fig(path, max_w=None, max_h=None):
    max_w = max_w or AVAIL_W
    max_h = max_h or A4[1] * 0.42
    img = PILImage.open(path)
    w, h = img.size
    scale = min(max_w / w, max_h / h, 1.0)
    return Image(path, width=w * scale, height=h * scale)


def build_body(doc, lang):
    LT = LANG_TXT[lang]
    meta = doc['meta']
    story = []
    story.append(Paragraph(meta['title'], S['toctitle']))
    story.append(Paragraph(meta['subtitle'], S['meta']))
    story.append(Paragraph(f"{meta['author']} · {meta['affil']}", S['meta']))
    story.append(Paragraph(f"{meta['series']} · том {meta['volume']} · "
                           f"версия {meta['version']} · {meta['date']}",
                           S['meta']))
    story.append(Spacer(1, 14))
    story.append(Paragraph(LT['toc'], S['toctitle']))
    toc = TableOfContents()
    toc.levelStyles = [S['toc0']]
    story.append(toc)
    story.append(PageBreak())
    for sec in doc['sections']:
        story.append(CondPageBreak(120))
        story.append(Paragraph(sec['h1'], S['h1']))
        for i in range(1, 7):
            thm = sec.get('theorem' if i == 1 else f'theorem{i}')
            if thm:
                story.append(KeepTogether([
                    Paragraph(thm['label'], S['thlabel']),
                    Paragraph(thm['text'], S['thm']),
                    Paragraph(f"<b>{LT['proof']}</b> {thm['proof']}",
                              S['proof']),
                    Spacer(1, 4)]))
        for p in sec.get('paras', []):
            story.append(Paragraph(p, S['body']))
        tbl = sec.get('table')
        if tbl:
            story.extend(make_table(tbl))
        for key in ('figure', 'figure2', 'figure3'):
            fig = sec.get(key)
            if fig:
                path = os.path.join(ROOT, fig['path'].replace('{lang}', lang))
                cap = fig['caption']
                if isinstance(cap, dict):
                    cap = cap.get(lang, cap.get('en', ''))
                if os.path.exists(path):
                    story.append(KeepTogether([
                        embed_fig(path),
                        Paragraph(cap, S['caption'])]))
        concl = sec.get('conclusion')
        if concl:
            for p in concl:
                story.append(Paragraph(p, S['body']))
    return story


def build_cover(doc, lang, out_pdf):
    from reportlab.pdfgen import canvas as canvas_mod
    """Векторная обложка серии (тёмный блок + медная линия)."""
    meta = doc['meta']
    txt = {
    'ru': {'series': 'ABQP JULIA RESEARCH PROGRAM · СЕРИЯ ОТЧЁТОВ',
           'vol': f"ТОМ {meta['volume']}", 'footer':
           f"{meta['author']} · версия {meta['version']} · {meta['date']}"},
    'en': {'series': 'ABQP JULIA RESEARCH PROGRAM · REPORT SERIES',
           'vol': f"VOLUME {meta['volume']}", 'footer':
           f"{meta['author']} · version {meta['version']} · {meta['date']}"},
    }[lang]
    c = canvas_mod.Canvas(out_pdf, pagesize=A4)
    w, h = A4
    c.setFillColor(COVER_BG)
    c.rect(0, 0, w, h, fill=1, stroke=0)
    c.setFillColor(colors.HexColor('#38505c'))
    c.rect(0, h - 3.9 * inch, w, 3.9 * inch, fill=1, stroke=0)
    c.setFillColor(colors.HexColor('#c96f4a'))
    c.rect(0, h - 3.95 * inch, w, 0.05 * inch, fill=1, stroke=0)
    c.setFillColor(colors.HexColor('#7fb6c9'))
    c.setFont('FreeSerif', 8.5)
    c.drawString(0.75 * inch, h - 0.9 * inch, txt['series'])
    c.setStrokeColor(colors.HexColor('#7fb6c9'))
    c.setLineWidth(0.7)
    c.line(0.75 * inch, h - 1.05 * inch, w - 0.75 * inch, h - 1.05 * inch)
    c.setFillColor(colors.HexColor('#c96f4a'))
    c.setFont('FreeSerif-Bold', 9)
    c.drawString(0.75 * inch, h - 1.5 * inch, txt['vol'])
    # заголовок (перенос строк)
    from reportlab.lib.utils import simpleSplit
    c.setFillColor(colors.HexColor('#f0f4f5'))
    c.setFont('FreeSerif-Bold', 21)
    y = h - 2.0 * inch
    for ln in simpleSplit(meta['title'], 'FreeSerif-Bold', 21,
                          w - 2.4 * inch)[:4]:
        c.drawString(0.75 * inch, y, ln)
        y -= 0.34 * inch
    c.setFont('FreeSerif', 10)
    c.setFillColor(colors.HexColor('#b7c6cc'))
    for ln in simpleSplit(meta['subtitle'], 'FreeSerif', 10,
                          w - 2.4 * inch)[:4]:
        c.drawString(0.75 * inch, y - 0.1 * inch, ln)
        y -= 0.22 * inch
    c.setFillColor(colors.HexColor('#d7e2e6'))
    c.setFont('FreeSerif', 10.5)
    c.drawString(0.85 * inch, 1.9 * inch, meta['author'])
    c.setFont('FreeSerif', 9)
    c.drawString(0.85 * inch, 1.62 * inch, meta['affil'])
    c.setStrokeColor(colors.HexColor('#298bbc'))
    c.setLineWidth(2)
    c.line(0.75 * inch, 2.12 * inch, 0.75 * inch, 1.35 * inch)
    c.setFillColor(colors.HexColor('#93a7ae'))
    c.setFont('FreeSerif', 8)
    c.drawString(0.75 * inch, 0.75 * inch, txt['footer'])
    c.showPage()
    c.save()
    return out_pdf


def make_pdf(content_path, out_pdf, lang):
    from pypdf import PdfReader, PdfWriter
    doc = json.load(open(content_path))
    meta = doc['meta']
    body_pdf = out_pdf.replace('.pdf', '_body.pdf')
    tdoc = TocDocTemplate(body_pdf, pagesize=A4,
                          leftMargin=MARGIN, rightMargin=MARGIN,
                          topMargin=1.0 * inch, bottomMargin=0.85 * inch,
                          title=meta['title'], author=meta['author'])
    tdoc.multiBuild(build_body(doc, lang),
                    onFirstPage=lambda c, d: on_page(c, d, meta['series'],
                                                     f"vol. {meta['volume']}"),
                    onLaterPages=lambda c, d: on_page(c, d, meta['series'],
                                                      f"vol. {meta['volume']}"))
    cov_pdf = out_pdf.replace('.pdf', '_cover.pdf')
    build_cover(doc, lang, cov_pdf)
    w = PdfWriter()
    for r in (PdfReader(cov_pdf), PdfReader(body_pdf)):
        for pg in r.pages:
            pg.scale_to(595.3, 841.9)
            w.add_page(pg)
    w.add_metadata({'/Title': meta['title'], '/Author': meta['author'],
                    '/Subject': meta['subtitle'],
                    '/Creator': 'ABQP Julia Research Program 0.2.0'})
    with open(out_pdf, 'wb') as f:
        w.write(f)
    os.remove(body_pdf)
    os.remove(cov_pdf)
    print(f'PDF OK: {out_pdf}')


if __name__ == '__main__':
    from reportlab.pdfgen import canvas as canvas_mod  # noqa: F401
    make_pdf(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else 'ru')
