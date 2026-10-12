# monograph/ — монографии серии

| Папка | Содержание |
|-------|------------|
| `theorems_volume/` | сводный том Th1–Th6 (RU/EN × DOCX/PDF) |
| `appendix_volume/` | приложение: методы, данные, воспроизводимость |
| `theorems/T01…T06/` | **отдельные папки теорем** — каждая со своей монографией (RU/EN × DOCX/PDF) и README |
| `content/` | источник контента (ru/en_part1–4 → DOCS) |
| `src/` | место для пользовательских шаблонов рендера |

Схема контента: `DOCS = {key: {meta, sections}}`; секция: h1, paras,
theorem1..6 {label,text,proof}, table {caption,header,rows,ratios},
figure/figure2/figure3 {path,caption}, conclusion. Один content-JSON
рендерится в PDF (ReportLab, векторная обложка) и DOCX (python-docx,
рецепт обложки R1, 3-секционная нумерация, TOC-поле) — полностью
автономно, без node и браузера.

Пересборка: `make monographs` / `python3 scripts/make_monographs.py`.
