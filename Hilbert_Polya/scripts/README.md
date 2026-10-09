# scripts/ — пайплайны сборки

| Скрипт | Назначение |
|--------|------------|
| `figstyle.py` | визуальная идентичность «Critical Line & Copper» (2 темы × 2 языка) |
| `make_figures.py` | 16 рисунков × ru/en @ 600 dpi → figures_hires/ |
| `make_logo.py` | логотип (light/dark, PNG 600 dpi + SVG) |
| `make_infographics.py` | 5 инфографик × ru/en × light/dark (Playwright+CSS) |
| `make_comp_readmes.py` | гигантские README папок вычислений (ru+en) |
| `make_monographs.py` | контент-JSON → 20 монографий (PDF+DOCX) |
| `render_pdf.py` | ReportLab + обложка html2poster + pypdf |
| `render_docx.js` | docx-js: обложка R1, 3 секции, TOC |
| `postprocess_docx.py` | TOC-плейсхолдеры, футеры ROMAN/arabic |
| `build_workbook.py` | tables/hp_workbook.xlsx |
