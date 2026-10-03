#!/usr/bin/env python3
"""postprocess_monograph.py — WPS-safe post-processing per docx-skill toc.md:
   1) remove empty <w:pgNumType/> (cover section)
   2) patch footer instrText: bare PAGE -> PAGE \\* ROMAN / \\* arabic
      (front-matter footer = ROMAN, body footer = arabic; we patch by
       section association via footer order in document.xml relationships)
   3) verify TOC placeholders present
Usage: postprocess_monograph.py file.docx
"""
import re
import shutil
import sys
import zipfile

path = sys.argv[1]
tmp = path + ".tmp.docx"

with zipfile.ZipFile(path, "r") as zin:
    names = zin.namelist()
    data = {n: zin.read(n) for n in names}

doc = data["word/document.xml"].decode("utf-8")

# 1) drop empty pgNumType emitted for sections without pageNumbers
doc = doc.replace("<w:pgNumType/>", "")

# Map footers to sections: find sectPr blocks in order; the 2nd section
# (front matter) uses fmt="upperRoman", 3rd (body) fmt="decimal".
sect_fmts = re.findall(r'<w:pgNumType[^>]*w:fmt="([^"]+)"', doc)
print("pgNumType fmts found:", sect_fmts)

# Identify footer rIds per sectPr (in order of appearance)
sect_blocks = re.findall(r"<w:sectPr[^>]*>.*?</w:sectPr>", doc, re.S)
footer_fmt = {}   # footerN.xml -> 'roman' | 'arabic'
for blk in sect_blocks:
    m_f = re.search(r'w:footerReference[^>]*r:id="(rId\d+)"', blk)
    fmt = None
    m_fmt = re.search(r'w:pgNumType[^>]*w:fmt="([^"]+)"', blk)
    if m_fmt:
        fmt = m_fmt.group(1)
    if m_f:
        footer_fmt[m_f.group(1)] = fmt

# resolve rIds -> footer files
rels = data["word/_rels/document.xml.rels"].decode("utf-8")
rid2file = dict(re.findall(r'Id="(rId\d+)"[^>]*Target="(footer\d+\.xml)"', rels))

for rid, fmt in footer_fmt.items():
    fname = "word/" + rid2file.get(rid, "")
    if fname not in data or fmt is None:
        continue
    fx = data[fname].decode("utf-8")
    switch = "ROMAN" if "oman" in fmt else "arabic"
    fx2 = re.sub(
        r"(<w:instrText[^>]*>)\s*PAGE\s*(</w:instrText>)",
        r"\1 PAGE \\* " + switch + r" \\* MERGEFORMAT \2",
        fx)
    if fx2 != fx:
        data[fname] = fx2.encode("utf-8")
        print(f"patched {fname} -> \\* {switch}")

data["word/document.xml"] = doc.encode("utf-8")

with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
    for n in names:
        zout.writestr(n, data[n])
shutil.move(tmp, path)

# verify TOC placeholders
doc2 = data["word/document.xml"].decode("utf-8")
n_toc = doc2.count("PAGEREF")
print("TOC placeholder entries (PAGEREF):", n_toc)
print("postprocess done:", path)
