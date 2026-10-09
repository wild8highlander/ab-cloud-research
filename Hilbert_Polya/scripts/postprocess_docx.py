#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""postprocess_docx.py — пост-обработка DOCX по правилам скилла:
1) add_toc_placeholders.py --auto (TOC-плейсхолдеры, updateFields);
2) патч футеров: PAGE → PAGE \\* ROMAN / \\* arabic (WPS-совместимость);
3) удаление пустых <w:pgNumType/> из секции обложки.
Использование: python3 postprocess_docx.py <file.docx>"""
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
import os

DOCX_SCRIPTS = "/home/z/my-project/skills/docx/scripts"


def main(path):
    # 1) TOC-плейсхолдеры
    r = subprocess.run([sys.executable, f"{DOCX_SCRIPTS}/add_toc_placeholders.py",
                        path, "--auto"], capture_output=True, text=True)
    print("toc_placeholders:", r.returncode, (r.stdout or r.stderr).strip()[-160:])
    # 2/3) XML-патчи
    tmp = tempfile.mkdtemp()
    with zipfile.ZipFile(path) as z:
        z.extractall(tmp)
    # футеры: 3 секции → footer1..N; определяем римскую/арабскую по порядку.
    footers = sorted(f for f in os.listdir(f"{tmp}/word")
                     if re.match(r"footer\d+\.xml", f))
    for i, f in enumerate(footers):
        p = f"{tmp}/word/{f}"
        xml = open(p, encoding="utf-8").read()
        fmt = "ROMAN" if i == 0 and len(footers) > 1 else "arabic"
        xml = re.sub(r"(<w:instrText[^>]*>)\s*PAGE\s*(</w:instrText>)",
                     rf"\1 PAGE \\* {fmt} \\* MERGEFORMAT \2", xml)
        open(p, "w", encoding="utf-8").write(xml)
    doc_xml_p = f"{tmp}/word/document.xml"
    xml = open(doc_xml_p, encoding="utf-8").read()
    xml = xml.replace("<w:pgNumType/>", "")
    open(doc_xml_p, "w", encoding="utf-8").write(xml)
    # пересборка
    tmp_out = path + ".new"
    with zipfile.ZipFile(tmp_out, "w", zipfile.ZIP_DEFLATED) as z:
        for root, _, files in os.walk(tmp):
            for f in files:
                full = os.path.join(root, f)
                z.write(full, os.path.relpath(full, tmp))
    shutil.move(tmp_out, path)
    shutil.rmtree(tmp)
    print(f"postprocess OK: {path}")


if __name__ == "__main__":
    main(sys.argv[1])
