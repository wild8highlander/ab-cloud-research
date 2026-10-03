# W1 document generators

This directory makes study W1 **fully self-reproducing**: not only the
research data, but also the authored documents (report PDF, RU/EN monograph
DOCX) can be rebuilt from sources inside the repository.

## `monograph/` — RU/EN monographs (DOCX)

Pure Node.js builder with a single dependency (`docx`).

```bash
cd scripts/monograph
npm install          # installs docx@^9
npm run build        # -> wave_attractors/monograph/{ru,en}/text/*.docx
```

The content modules (`content_a_*.js`, `content_b_*.js`) embed the
per-language figure sets from `wave_attractors/monograph/<lang>/figures/`,
which are produced by `python3 make_figures.py --lang ru|en
--out ../monograph/<lang>/figures`. PDF copies of the monographs are
produced from the DOCX with LibreOffice:

```bash
soffice --headless --convert-to pdf --outdir monograph/ru/text \
    monograph/ru/text/AB_Cloud_Monograph_W1_RU.docx
```

`postprocess_monograph.py` performs the final PDF QA pass (footer band,
em-dash binding, page geometry).

## `report/` — Russian scientific report (PDF)

```bash
cd scripts/report
python3 w1_report_build.py   # body: ReportLab -> report/_body.pdf
python3 w1_merge.py          # + cover (w1_cover.pdf) -> final report PDF
```

Requires `reportlab`, `pypdf`, `pillow` (see `wave_attractors/requirements.txt`)
and the FreeSerif / Noto Serif SC / DejaVu system fonts. The cover source
(`w1_cover.html`) is committed and can be re-rendered to PDF with any
headless-Chromium print-to-PDF at A4; the rendered `w1_cover.pdf` is also
committed so the merge step needs no browser.
