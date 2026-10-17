# monograph/ — monographs of the series

| Folder | Content |
|-------|------------|
| `theorems_volume/` | the combined Th1–Th6 volume (RU/EN × DOCX/PDF) |
| `appendix_volume/` | the appendix: methods, data, reproducibility |
| `theorems/T01…T06/` | **separate theorem folders** — each with its own monograph (RU/EN × DOCX/PDF) and README |
| `content/` | the content source (`__init__.py`, `common.py`, `ru/en_part1–6` → DOCS) |
| `src/` | the place for custom render templates |

The content schema: `DOCS = {key: {meta, sections}}`; a section: h1, paras,
theorem1..6 {label,text,proof}, table {caption,header,rows,ratios},
figure/figure2/figure3 {path,caption}, conclusion. One content-JSON
is rendered to PDF (ReportLab, a vector cover) and DOCX (python-docx,
the R1 cover recipe, 3-section numbering, a TOC field) — fully
offline, without node or a browser.

Rebuild: `make monographs` / `python3 scripts/make_monographs.py`.
