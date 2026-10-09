#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""render_pdf.py — рендер монографий серии (ReportLab + обложка + pypdf).

Один и тот же контент-JSON для DOCX и PDF (make_monographs.py).
Использование: python3 render_pdf.py <content.json> <out.pdf> [lang]
Обложка — html2poster.js (Template серии: тёмный блок, шапка серии,
заголовок, подзаголовок, метаданные, нижняя строка).
"""
import json
import os
import subprocess
import sys
import tempfile

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.platypus import (CondPageBreak, Image, KeepTogether,
                                Paragraph, PageBreak, SimpleDocTemplate,
                                Spacer, Table, TableStyle)
from reportlab.platypus.tableofcontents import TableOfContents
from PIL import Image as PILImage

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF_SKILL = "/home/z/my-project/skills/pdf"

# ━━ Палитра серии «Critical Line & Copper» ━━
PAGE_BG = colors.HexColor('#f5f6f6')
HEADER_FILL = colors.HexColor('#3b4f58')
BORDER = colors.HexColor('#c7d3d9')
ACCENT = colors.HexColor('#298bbc')
ACCENT_2 = colors.HexColor('#c96f4a')
TEXT_PRIMARY = colors.HexColor('#222526')
TEXT_MUTED = colors.HexColor('#777e81')
SURFACE = colors.HexColor('#ebedee')

# ━━ Шрифты (полная кириллица) ━━
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
'ru': {'toc': 'Содержание', 'page': 'стр.',
       'theorem': 'Формулировка.', 'proof': 'Доказательство.',
       'series': 'Hilbert Polya Bridge'},
'en': {'toc': 'Contents', 'page': 'p.',
       'theorem': 'Statement.', 'proof': 'Proof.',
       'series': 'Hilbert Polya Bridge'},
}


# ━━ шаблон с TOC ━━
class TocDocTemplate(SimpleDocTemplate):
    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)
        self._toc_entries = []

    def afterFlowable(self, flowable):
        if isinstance(flowable, Paragraph):
            st = flowable.style.name
            if st == 'h1':
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
    out = [Paragraph(spec['caption'],
                     ParagraphStyle('tcap', parent=S['caption'],
                                    spaceBefore=8, spaceAfter=3)),
           t, Spacer(1, 8)]
    return out


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
    # титульный блок тела
    story.append(Paragraph(meta['title'], S['toctitle']))
    story.append(Paragraph(meta['subtitle'], S['meta']))
    story.append(Paragraph(f"{meta['author']} · {meta['affil']}", S['meta']))
    story.append(Paragraph(f"{meta['series']} · том {meta['volume']} · "
                           f"версия {meta['version']} · {meta['date']}", S['meta']))
    story.append(Spacer(1, 14))
    # TOC
    story.append(Paragraph(LT['toc'], S['toctitle']))
    toc = TableOfContents()
    toc.levelStyles = [S['toc0']]
    story.append(toc)
    story.append(PageBreak())
    # секции
    for sec in doc['sections']:
        story.append(CondPageBreak(120))
        story.append(Paragraph(sec['h1'], S['h1']))
        thm = sec.get('theorem')
        if thm:
            story.append(KeepTogether([
                Paragraph(thm['label'], S['thlabel']),
                Paragraph(thm['text'], S['thm']),
                Paragraph(f"<b>{LT['proof']}</b> {thm['proof']}", S['proof']),
                Spacer(1, 4)]))
        elif sec.get('theorem2'):
            pass
        for p in sec.get('paras', []):
            story.append(Paragraph(p, S['body']))
        for i in range(2, 6):
            thm2 = sec.get(f'theorem{i}')
            if thm2:
                story.append(KeepTogether([
                    Paragraph(thm2['label'], S['thlabel']),
                    Paragraph(thm2['text'], S['thm']),
                    Paragraph(f"<b>{LT['proof']}</b> {thm2['proof']}", S['proof']),
                    Spacer(1, 4)]))
        tbl = sec.get('table')
        if tbl:
            story.extend(make_table(tbl))
        for key in ('figure', 'figure2', 'figure3'):
            fig = sec.get(key)
            if fig:
                path = os.path.join(ROOT, fig['path'].replace('{lang}', lang))
                if os.path.exists(path):
                    story.append(KeepTogether([
                        embed_fig(path),
                        Paragraph(fig['caption'], S['caption'])]))
        concl = sec.get('conclusion')
        if concl:
            for p in concl:
                story.append(Paragraph(p, S['body']))
    return story


def build_cover_html(doc, lang, out_html):
    meta = doc['meta']
    txt = {
    'ru': {'series': 'HILBERT POLYA BRIDGE · СЕРИЯ МОНОГРАФИЙ',
           'vol': f"ТОМ {meta['volume']}", 'footer':
           f"{meta['author']} · версия {meta['version']} · {meta['date']}"},
    'en': {'series': 'HILBERT POLYA BRIDGE · MONOGRAPH SERIES',
           'vol': f"VOLUME {meta['volume']}", 'footer':
           f"{meta['author']} · version {meta['version']} · {meta['date']}"},
    }[lang]
    html = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>
@page {{ size: 794px 1123px; margin: 0; }}
html, body {{ margin:0; padding:0; background:#2e3f49; }}
.poster {{ width:794px; height:1123px; background:#2e3f49; color:#f0f4f5;
  font-family:'DejaVu Sans',sans-serif; position:relative; overflow:hidden; }}
.deco {{ position:absolute; top:0; left:0; right:0; height:392px;
  background:linear-gradient(160deg,#38505c 0%,#2e3f49 62%,#28363e 100%); }}
.copperline {{ position:absolute; top:392px; left:0; right:0; height:4px;
  background:#c96f4a; }}
.wrap {{ position:absolute; inset:0; padding:56px 54px; display:flex;
  flex-direction:column; }}
.series {{ font-size:11px; letter-spacing:3.2px; color:#7fb6c9;
  border-bottom:1px solid rgba(127,182,201,.35); padding-bottom:14px; }}
.vol {{ margin-top:40px; font-size:12px; letter-spacing:2.6px; color:#c96f4a;
  font-weight:700; }}
h1 {{ margin:16px 0 0; font-size:37px; line-height:1.18; font-weight:800;
  color:#f0f4f5; max-width:470px; }}
.sub {{ margin-top:18px; font-size:14.5px; line-height:1.55; color:#b7c6cc;
  max-width:470px; }}
.meta {{ margin-top:auto; border-left:3px solid #298bbc; padding-left:16px;
  font-size:13px; line-height:1.9; color:#d7e2e6; }}
.footer {{ margin-top:30px; padding-top:14px; border-top:1px solid
  rgba(127,182,201,.3); font-size:11px; color:#93a7ae; letter-spacing:.6px; }}
</style></head><body><div class="poster"><div class="deco"></div>
<div class="copperline"></div><div class="wrap">
<div class="series">{txt['series']}</div>
<div class="vol">{txt['vol']}</div>
<h1>{meta['title']}</h1>
<div class="sub">{meta['subtitle']}</div>
<div class="meta">{meta['author']}<br>{meta['affil']}</div>
<div class="footer">{txt['footer']}</div>
</div></div></body></html>"""
    open(out_html, 'w').write(html)
    return out_html


def make_pdf(content_path, out_pdf, lang):
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
    # обложка
    with tempfile.TemporaryDirectory() as td:
        cov_html = os.path.join(td, 'cover.html')
        cov_pdf = os.path.join(td, 'cover.pdf')
        build_cover_html(doc, lang, cov_html)
        subprocess.run(['node', f'{PDF_SKILL}/scripts/html2poster.js',
                        cov_html, '--output', cov_pdf, '--width', '794px'],
                       check=True, capture_output=True)
        from pypdf import PdfReader, PdfWriter
        w = PdfWriter()
        for r in (PdfReader(cov_pdf), PdfReader(body_pdf)):
            for pg in r.pages:
                # нормализация к A4 (595.3 × 841.9 pt) — разные dpi обложки/тела
                pg.scale_to(595.3, 841.9)
                w.add_page(pg)
        w.add_metadata({'/Title': meta['title'], '/Author': meta['author'],
                        '/Subject': meta['subtitle'],
                        '/Creator': 'Hilbert Polya Bridge 1.0.0'})
        with open(out_pdf, 'wb') as f:
            w.write(f)
    os.remove(body_pdf)
    print(f"PDF OK: {out_pdf}")


if __name__ == '__main__':
    make_pdf(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else 'ru')
