# scripts/ — the build pipelines

> **🧭 Navigation:** [Hilbert_Polya/](../README.md) · [Root README](../../README.md)

<p align="center"><img src="../assets/illustrations/ill_montage_bench.png" width="600" alt="Backstage bench where figures, covers and workbooks are assembled"/></p>

<p align="center"><img src="../assets/avatars/hp_cast_strip.svg" width="720" alt="Bridge avatar cast"/></p>
<p align="center"><em>Backstage of the series: the agents pose for the cover while these scripts do the typesetting.</em></p>

[← Back to the main README](../README.md)

## What this folder is

The generators. Every published artifact of the series — figures, logo,
infographics, campaign READMEs, monographs, the summary workbook — is
produced here from committed data, in both languages and both themes, so
that regenerating the whole presentation layer is a matter of one make
target rather than hand editing. The scripts are the reason `figures_hires/`,
`figures/`, `monograph/` and `tables/` can stay perfectly in sync with
`data/`.

## Contents

| Script | Purpose |
|--------|---------|
| `figstyle.py` | the "Critical Line & Copper" visual identity (2 themes × 2 languages) |
| `make_figures.py` | 16 figures × ru/en @ 600 dpi → figures_hires/ |
| `make_logo.py` | the logo (light/dark, PNG 600 dpi + SVG) |
| `make_infographics.py` | 5 infographics × ru/en × light/dark (Playwright+CSS) |
| `make_comp_readmes.py` | the giant READMEs of the computation folders (ru+en) |
| `make_monographs.py` | content-JSON → 13 monograph documents × ru/en × PDF/DOCX |
| `render_pdf.py` | ReportLab + html2poster cover + pypdf |
| `render_docx.js` | docx-js: R1 cover, 3 sections, TOC |
| `postprocess_docx.py` | TOC placeholders, ROMAN/arabic footers |
| `build_workbook.py` | tables/hp_workbook.xlsx |

The v2.0 generation adds two more generators in the same style:

| Script | Purpose |
|--------|---------|
| `make_figures_v2.py` | bilingual 600 dpi figures for campaigns C9–C16: fig17_nonlocal, fig18_coloc, fig19_alphathird, fig20_band5000, fig21_blind, fig22_anomaly, fig23_dirichlet, fig24_qinfo, fig25_map → figures_hires/{lang}/ + copies in computations/C*/figures/ |
| `make_animations_v2.py` | v2.0 animations (GIF + MP4, ffmpeg): anim_wavepacket — wave-packet transport on the ζ-cloud (a C7 continuation); anim_coloc — hard co-location of the prime flow, with β rotating so that (Φ_p,Φ_q) ≡ Φ_pq holds for any β (T12) → figures/animations/ + copies in computations/ |

## How to use it

All scripts are run from the repository root. The documented entry points are
the make targets:

```bash
make monographs   # content-JSON → 13 monograph documents × ru/en × PDF/DOCX
make workbook     # rebuild tables/hp_workbook.xlsx
python3 scripts/build_workbook.py   # same, without make
```

The figure generators write 600 dpi PNGs into `figures_hires/{lang}/` and
drop per-campaign copies into `computations/C*/figures/`; the logo generator
emits light/dark PNG (600 dpi) plus SVG into `figures/logo/`; the
infographics generator renders 5 panels × ru/en × light/dark through
Playwright+CSS. The DOCX branch is a chain: `render_docx.js` produces the
document (R1 cover recipe, three-section numbering, TOC placeholders), then
`postprocess_docx.py` resolves the placeholders and applies the
ROMAN/arabic footers, and `make_monographs.py` orchestrates the whole
content-JSON → PDF+DOCX run over the 13 monograph documents of the series.

## Conventions

- One visual identity: `figstyle.py` defines the "Critical Line & Copper"
  palette and rules; every figure, infographic and cover consumes it, and
  nothing hard-codes colors elsewhere.
- Everything is bilingual by construction: ru/en suffix pairs in file names,
  and language-specific text drawn from the same committed content.
- Regenerate, never hand-edit: outputs under `figures*/`, `monograph/` and
  `tables/` are build products; a manual tweak will be overwritten by the
  next run.
- Themes are paired: light and dark variants are always produced together,
  for PNG (matplotlib) and for CSS-rendered panels (Playwright) alike.

## Glossary

- **R1 cover recipe** — the cover layout used by the DOCX branch of the
  monographs; `render_docx.js` implements it over the content-JSON.
- **TOC placeholders** — markers left in a DOCX by `render_docx.js` and
  resolved by `postprocess_docx.py`, so the table of contents matches the
  final pagination.
- **ROMAN/arabic footers** — the two numbering regimes of the three-section
  monograph layout (front matter in Roman numerals, body in Arabic).
- **html2poster** — the HTML-to-image cover route feeding the PDF branch,
  merged into the final file by pypdf.
- **Playwright+CSS** — the rendering engine of `make_infographics.py`,
  chosen so the five infographic panels are laid out in CSS, not
  matplotlib.

## See also

- [../tables/README.md](../tables/README.md) — the workbook produced by `build_workbook.py`
- [../monograph/README.md](../monograph/README.md) — the volumes produced by the render chain
- [../figures/README.md](../figures/README.md) — the logo and infographic outputs
- [../figures_hires/README.md](../figures_hires/README.md) — the 600 dpi figure library

---

<!-- enriched-r3 -->

This folder holds the **pipeline scripts** of its module: the deterministic code paths that turn frozen inputs into reports, figures and verdicts. The scripts follow the repository's seed discipline — same input, same seed, same bytes out — so a re-run on the pinned platform reproduces the committed artifacts. Nothing here is executed at import time by other modules; they are entry points, documented in the module README.

The build pipelines of the series: rendering, checking and packaging entry points that turn the content source into the committed volumes.
