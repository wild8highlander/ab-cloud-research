# scripts/ — конвейер самосборки

| Скрипт | Назначение |
|--------|------------|
| compute_all.py | свежий полный прогон V1–V15 → data/ (~2 мин) |
| make_figures.py | 16 рисунков × ru/en @600 dpi |
| make_logo.py / make_infographics.py | эмблема и инфографики |
| make_monographs.py | все монографии RU/EN × DOCX/PDF + 6 теорем |
| render_pdf.py / render_docx.py | рендеры одного content-JSON |
| make_comp_readmes.py | билингвальные README 15 вычислений |
| make_claims.py | claim-файлы аудита V14 |
| build_workbook.py | tables/rp_workbook.xlsx |
| build_lab.py | web_lab/index.html (самодостаточная лаборатория) |
| new_experiment.py | скаффолд новой кампании V16+ |
| make_release.py | SHA256SUMS + zip-архив |
