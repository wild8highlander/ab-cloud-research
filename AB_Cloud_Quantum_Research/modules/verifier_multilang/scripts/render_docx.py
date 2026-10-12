#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""render_docx.py — рендер монографий серии в DOCX (python-docx, портабельно).

Правила обложки — рецепт R1 эталона: тёмный фон секции (margin 0),
3-секционная нумерация (обложка / TOC римские / тело арабские с 1),
заголовки Heading 1, таблицы с заливкой шапки, картинки с пропорциями,
TOC-поле с подсказкой обновления.
Использование: python3 render_docx.py <content.json> <out.docx> [lang]
"""
import json
import os
import re
import shutil
import sys
import tempfile
import zipfile

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Emu, Pt, RGBColor

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

P = dict(bg='2E3F49', titleColor='F0F4F5', subtitleColor='B7C6CC',
         metaColor='D7E2E6', footerColor='93A7AE', accent='298BBC',
         copper='C96F4A', ink='222526', muted='777E81', header='3B4F58',
         surface='EBEDEE', grid='C7D3D9')

LANG_TXT = {
    'ru': dict(toc='Содержание', update='Обновите поле (F9), чтобы собрать '
               'оглавление.', proof='Доказательство.', page='стр.',
               vol='Том'),
    'en': dict(toc='Contents', update='Update the field (F9) to build the '
               'table of contents.', proof='Proof.', page='p.',
               vol='Volume'),
}


def set_cell_bg(cell, hexcolor):
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:fill'), hexcolor)
    cell._tc.get_or_add_tcPr().append(shd)


def cell_borders(cell, color=P['grid']):
    tcPr = cell._tc.get_or_add_tcPr()
    borders = OxmlElement('w:tcBorders')
    for side in ('top', 'bottom', 'left', 'right'):
        el = OxmlElement(f'w:{side}')
        el.set(qn('w:val'), 'single')
        el.set(qn('w:sz'), '4')
        el.set(qn('w:color'), color)
        borders.append(el)
    tcPr.append(borders)


def add_toc_field(paragraph, lang):
    fldChar1 = OxmlElement('w:fldChar')
    fldChar1.set(qn('w:fldCharType'), 'begin')
    instr = OxmlElement('w:instrText')
    instr.set(qn('xml:space'), 'preserve')
    instr.text = ' TOC \\o "1-1" \\h \\z \\u '
    fldChar2 = OxmlElement('w:fldChar')
    fldChar2.set(qn('w:fldCharType'), 'separate')
    hint = OxmlElement('w:t')
    hint.text = LANG_TXT[lang]['update']
    fldChar3 = OxmlElement('w:fldChar')
    fldChar3.set(qn('w:fldCharType'), 'end')
    for el in (fldChar1, instr, fldChar2, hint, fldChar3):
        paragraph._p.append(el)


def page_number_footer(section, fmt_roman=False):
    footer = section.footer
    p = footer.paragraphs[0]
    p.text = ''
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run()
    fld1 = OxmlElement('w:fldChar')
    fld1.set(qn('w:fldCharType'), 'begin')
    instr = OxmlElement('w:instrText')
    instr.set(qn('xml:space'), 'preserve')
    instr.text = ' PAGE \\* ' + ('ROMAN' if fmt_roman else 'arabic') + \
        ' \\* MERGEFORMAT'
    fld2 = OxmlElement('w:fldChar')
    fld2.set(qn('w:fldCharType'), 'end')
    run._r.append(fld1)
    run._r.append(instr)
    run._r.append(fld2)
    run.font.size = Pt(9)
    run.font.color.rgb = RGBColor.from_string(P['muted'])


def cover_page(doc, meta, lang):
    LT = LANG_TXT[lang]
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Cm(21.0), Cm(29.7)
    for attr in ('top_margin', 'bottom_margin', 'left_margin',
                 'right_margin'):
        setattr(sec, attr, Cm(0))
    # фон секции — через table-обёртку (простейший надёжный тёмный фон)
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    cell.width = Cm(21.0)
    set_cell_bg(cell, P['bg'])
    cell.paragraphs[0].text = ''
    def para(text, size, color, bold=False, space_before=6, space_after=6,
             align=WD_ALIGN_PARAGRAPH.LEFT, indent_cm=2.0):
        p = cell.add_paragraph()
        p.alignment = align
        pf = p.paragraph_format
        pf.space_before = Pt(space_before)
        pf.space_after = Pt(space_after)
        pf.left_indent = Cm(indent_cm)
        r = p.add_run(text)
        r.font.size = Pt(size)
        r.font.bold = bold
        r.font.color.rgb = RGBColor.from_string(color)
        r.font.name = 'Arial'
        return p
    series = ('AB QUANTUM PROCESSOR · СЕРИЯ МОНОГРАФИЙ' if lang == 'ru'
              else 'AB QUANTUM PROCESSOR · MONOGRAPH SERIES')
    para(series, 9, '7FB6C9', space_before=64)
    para(f"{LT['vol']} {meta['volume']}", 10, P['copper'], bold=True,
         space_before=28)
    para(meta['title'], 26, P['titleColor'], bold=True, space_before=10)
    para(meta['subtitle'], 12, P['subtitleColor'], space_before=10)
    para(meta['author'], 12, P['metaColor'], space_before=140)
    para(meta['affil'], 10, P['metaColor'])
    para(f"{meta['series']} · v{meta['version']} · {meta['date']}", 9,
         P['footerColor'], space_before=64, space_after=48)
    doc.add_page_break()


def build_doc(content_path, out_path, lang='ru'):
    doc = json.load(open(content_path))
    meta = doc['meta']
    LT = LANG_TXT[lang]
    document = Document()
    # ── секция 1: обложка ──
    cover_page(document, meta, lang)
    # ── секция 2: TOC (римские) ──
    sec2 = document.add_section(WD_SECTION.NEW_PAGE)
    sec2.top_margin = sec2.bottom_margin = Cm(2.2)
    sec2.left_margin = sec2.right_margin = Cm(2.4)
    page_number_footer(sec2, fmt_roman=True)
    h = document.add_paragraph()
    r = h.add_run(LT['toc'])
    r.font.size = Pt(20)
    r.font.bold = True
    r.font.color.rgb = RGBColor.from_string(P['header'])
    r.font.name = 'Arial'
    toc_p = document.add_paragraph()
    add_toc_field(toc_p, lang)
    document.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
    # ── секция 3: тело (арабские с 1) ──
    sec3 = document.add_section(WD_SECTION.NEW_PAGE)
    sec3.top_margin = sec3.bottom_margin = Cm(2.2)
    sec3.left_margin = sec3.right_margin = Cm(2.4)
    page_number_footer(sec3, fmt_roman=False)
    # титульный блок тела
    t = document.add_paragraph()
    r = t.add_run(meta['title'])
    r.font.size = Pt(20)
    r.font.bold = True
    r.font.color.rgb = RGBColor.from_string(P['header'])
    r.font.name = 'Arial'
    for line in (meta['subtitle'], f"{meta['author']} · {meta['affil']}",
                 f"{meta['series']} · {LT['vol']} {meta['volume']} · "
                 f"v{meta['version']} · {meta['date']}"):
        p = document.add_paragraph()
        rr = p.add_run(line)
        rr.font.size = Pt(9.5)
        rr.font.color.rgb = RGBColor.from_string(P['muted'])
    # секции
    for sec in doc['sections']:
        h = document.add_heading(sec['h1'], level=1)
        for run in h.runs:
            run.font.color.rgb = RGBColor.from_string(P['header'])
            run.font.name = 'Arial'
        for i in range(1, 7):
            thm = sec.get('theorem' if i == 1 else f'theorem{i}')
            if not thm:
                continue
            pl = document.add_paragraph()
            pl.paragraph_format.space_before = Pt(8)
            rl = pl.add_run(thm['label'])
            rl.font.bold = True
            rl.font.color.rgb = RGBColor.from_string(P['copper'])
            rl.font.size = Pt(10.5)
            pt = document.add_paragraph(thm['text'])
            pt.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            pp = document.add_paragraph()
            pp.paragraph_format.left_indent = Cm(0.5)
            pp.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            r1 = pp.add_run(LT['proof'] + ' ')
            r1.font.bold = True
            r2 = pp.add_run(thm['proof'])
            for rr in (r1, r2):
                rr.font.italic = True
                rr.font.size = Pt(9.6)
        for para in sec.get('paras', []):
            p = document.add_paragraph(para)
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        tbl = sec.get('table')
        if tbl:
            cp = document.add_paragraph(tbl['caption'])
            cp.paragraph_format.space_before = Pt(8)
            table = document.add_table(rows=1 + len(tbl['rows']),
                                       cols=len(tbl['header']))
            table.alignment = WD_TABLE_ALIGNMENT.CENTER
            for j, htxt in enumerate(tbl['header']):
                cell = table.cell(0, j)
                cell.text = ''
                p = cell.paragraphs[0]
                run = p.add_run(htxt)
                run.font.bold = True
                run.font.size = Pt(8.6)
                run.font.color.rgb = RGBColor.from_string('FFFFFF')
                set_cell_bg(cell, P['header'])
                cell_borders(cell)
            for i, row in enumerate(tbl['rows']):
                for j, val in enumerate(row):
                    cell = table.cell(i + 1, j)
                    cell.text = ''
                    p = cell.paragraphs[0]
                    run = p.add_run(str(val))
                    run.font.size = Pt(8.6)
                    set_cell_bg(cell, 'FFFFFF' if i % 2 == 0 else P['surface'])
                    cell_borders(cell)
        for key in ('figure', 'figure2', 'figure3'):
            fig = sec.get(key)
            if not fig:
                continue
            path = os.path.join(ROOT, fig['path'].replace('{lang}', lang))
            if not os.path.exists(path):
                continue
            from PIL import Image as PILImage
            img = PILImage.open(path)
            w_px, h_px = img.size
            max_w = Cm(16.0)
            scale = min(max_w / Emu(int(w_px * 9525 * 0.264583)), 1.0) \
                if False else 16.0 / (w_px / 600 * 2.54)
            p = document.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run = p.add_run()
            run.add_picture(path, width=Cm(min(16.0, w_px / 600 * 2.54 * 4)))
            cap_txt = fig['caption']
            if isinstance(cap_txt, dict):
                cap_txt = cap_txt.get(lang, cap_txt.get('en', ''))
            cap = document.add_paragraph(cap_txt)
            cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            cr = cap.runs[0]
            cr.font.italic = True
            cr.font.size = Pt(8.5)
            cr.font.color.rgb = RGBColor.from_string(P['muted'])
        for para in sec.get('conclusion', []):
            p = document.add_paragraph(para)
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    document.save(out_path)
    postprocess(out_path)
    print(f'DOCX OK: {out_path}')


def postprocess(path):
    """TOC-плейсхолдеры уже вставлены; чистим пустые pgNumType обложки."""
    tmp = tempfile.mkdtemp()
    with zipfile.ZipFile(path) as z:
        z.extractall(tmp)
    doc_xml_p = os.path.join(tmp, 'word', 'document.xml')
    xml = open(doc_xml_p, encoding='utf-8').read()
    xml = xml.replace('<w:pgNumType/>', '')
    open(doc_xml_p, 'w', encoding='utf-8').write(xml)
    tmp_out = path + '.new'
    with zipfile.ZipFile(tmp_out, 'w', zipfile.ZIP_DEFLATED) as z:
        for root, _, files in os.walk(tmp):
            for f in files:
                full = os.path.join(root, f)
                z.write(full, os.path.relpath(full, tmp))
    shutil.move(tmp_out, path)
    shutil.rmtree(tmp)


if __name__ == '__main__':
    build_doc(sys.argv[1], sys.argv[2],
              sys.argv[3] if len(sys.argv) > 3 else 'ru')
