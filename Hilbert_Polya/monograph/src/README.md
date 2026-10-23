# monograph/src/ — reserved slot for series template overrides

> **🧭 Navigation:** [monograph/](../README.md) · [Hilbert_Polya/](../../README.md) · [Root README](../../../README.md)

<p align="center"><img src="../../assets/illustrations/ill_montage_bench.png" width="600" alt="The render bench of the monograph series"/></p>

<p align="center"><img src="../../assets/avatars/hp_cast_strip.svg" width="720" alt="Bridge avatar cast"/></p>
<p align="center"><em>An empty bench, kept ready: the typesetters work elsewhere, but this is where their templates would be overridden.</em></p>

[← Back to the main README](../../README.md)

## What this folder is

A deliberately reserved directory. The renderers of the monograph series live
in `scripts/` — `render_pdf.py`, `render_docx.js`, `postprocess_docx.py`,
`make_monographs.py` — and they currently take their templates and styles
from their own defaults. This `src/` catalog is left for future overrides of
the series templates: first of all the cover recipes and the shared styles.

Today the folder holds only this README. Nothing in the build pipeline reads
from it yet, which is exactly what makes it safe: the pipeline works without
it, and any future override can be introduced here without touching the
renderers' code paths.

## Contents

| File | Role |
|------|------|
| `README.md` | this note — documents the reserved status of the folder |

## How the content flows around it

Although `src/` itself is empty, it sits on the main artery of the series:

1. content sources live in `../content/` (`ru_part1.py` … `ru_part4.py`,
   `en_part1.py` … `en_part4.py`, `parts_theorems_v2.py`);
2. `scripts/make_monographs.py` assembles them into content-JSON;
3. `scripts/render_pdf.py` (ReportLab + html2poster cover + pypdf) and
   `scripts/render_docx.js` (docx-js: R1 cover recipe, three-section
   numbering, TOC placeholders) render the volumes;
4. `scripts/postprocess_docx.py` resolves TOC placeholders and applies the
   ROMAN/arabic footers;
5. the finished `monograph_*.{pdf,docx}` land in `../theorems_volume/`,
   `../appendix_volume/`, `../v2_volume/`, `../theorems_v2_volume/`.

A future cover or style override would be placed here as template files
shadowing the series defaults — after which `make monographs` (run from the
repository root) would pick them up without any change to the scripts.

## Conventions

- Do not put data, verdicts, or numbers in this folder; it is for templates
  and styles only.
- Overrides must stay optional: the renderers must keep working if this
  folder is emptied again.
- Name any future template files after the default they override (cover
  recipe, style sheet), so the mapping stays obvious.

## See also

- [../README.md](../README.md) — the parent folder: volumes, content sources, preprint
- [../../scripts/README.md](../../scripts/README.md) — the renderers that would consume overrides from here
- [../../results/README.md](../../results/README.md) — the ledgers the volumes quote from

---

<!-- enriched-r3 -->

This folder holds the **pipeline scripts** of its module: the deterministic code paths that turn frozen inputs into reports, figures and verdicts. The scripts follow the repository's seed discipline — same input, same seed, same bytes out — so a re-run on the pinned platform reproduces the committed artifacts. Nothing here is executed at import time by other modules; they are entry points, documented in the module README.

A reserved slot for series template overrides: intentionally minimal — the default rendering templates live with the build pipeline.
