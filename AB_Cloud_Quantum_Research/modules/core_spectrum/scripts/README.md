# scripts/ — the self-assembly pipeline

| Script | Purpose |
|--------|------------|
| compute_all.py | a fresh full run V1–V19 → data/ (~2 min) |
| make_figures.py | 20 figures × ru/en @600 dpi |
| make_logo.py / make_infographics.py | the emblem and the infographics |
| make_monographs.py | all monographs RU/EN × DOCX/PDF + 6 theorems |
| render_pdf.py / render_docx.py | renderers of one content-JSON |
| make_comp_readmes.py | bilingual READMEs of the computations |
| make_claims.py | the claim files of the V14 audit |
| build_workbook.py | tables/rp_workbook.xlsx |
| build_lab.py | web_lab/index.html (a self-contained laboratory) |
| new_experiment.py | a scaffold for a new campaign V16+ |
| make_release.py | SHA256SUMS + the zip archive |
