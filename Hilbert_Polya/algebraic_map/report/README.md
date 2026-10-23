<!-- AB-ENRICHED:v1 · sub -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venice&height=48&color=0:a78bfa,100:05060f&section=header" alt="" width="100%"/>

**🧭 [⬆ algebraic_map/](../README.md) · [🏠 Root README](../../../README.md)**

</div>
<div align="center">

[![Shelf](https://img.shields.io/badge/Shelf-hilbert-polya-FFB74D?style=flat-square)](../README.md)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21825394-blue?style=flat-square)](https://doi.org/10.5281/zenodo.21825394)

</div>

# 📄 algebraic map — report

> **The assembled bilingual report of the algebraic-map campaign (PDF + DOCX) and its build sources.**

The deliverable layer of the algebraic-map campaign: `HPB_algebraic_map_2026-10-13_ru.pdf` and the same report as `.docx` (Russian edition, dated 2026-10-13), an HTML cover, and [`src/`](src/) — the build sources that assemble the final document from content blocks. The numbers in the report come from [`../data/amap_results.json`](../data/amap_results.json) and the figures from [`../figures/`](../figures/); regenerate rather than edit if anything changes.

## 📁 Contents

| Item | Kind | Size | What it is |
|---|---|---|---|
| [`_cover.html`](_cover.html) | HTML | 2.9 KB | — |
| [`HPB_algebraic_map_2026-10-13_ru.docx`](HPB_algebraic_map_2026-10-13_ru.docx) | DOCX | 627.5 KB | — |
| [`HPB_algebraic_map_2026-10-13_ru.pdf`](HPB_algebraic_map_2026-10-13_ru.pdf) | PDF | 887.6 KB | — |
| `src/` | folder | 7 items | document build sources (content blocks, assembly scripts) |
| [`src/amap_build.py`](src/amap_build.py) | Python | — | assembles the PDF report: ReportLab body (TocDocTemplate + multiBuild), HTML cover via `html2poster.js`, merged with pypdf |
| [`src/amap_content.py`](src/amap_content.py) | Python | — | report content blocks (RU), sections 1–5; all numbers read from `../data/amap_results.json` |
| [`src/amap_content2.py`](src/amap_content2.py) | Python | — | report content blocks (RU), sections 6–11 + appendices (identities K1–K8, appendix table) |
| [`src/amap_docx.js`](src/amap_docx.js) | JavaScript | — | DOCX build of the report (docx-js), parsing `<b>`/`<sub>`/`<super>` tags and formula blocks |
| [`src/content_amap.json`](src/content_amap.json) | JSON | — | the serialized content payload (title, blocks, biblio) consumed by the DOCX build |
| [`src/gen_appendix_table.py`](src/gen_appendix_table.py) | Python | — | regenerates the appendix table A.1 rows from `amap_results.json` and patches `amap_content2.py` |
| [`src/gen_content_json.py`](src/gen_content_json.py) | Python | — | collects `content_amap.json` from `amap_content{,2}.py` for the DOCX build |

## 🧭 Navigation

[⬅ Back to the parent shelf](../README.md) · [🏠 Repo root](../../../README.md)

---

<div align="center">

*Part of the [AB-Cloud Research](../../../README.md) repository · DOI [10.5281/zenodo.21825394](https://doi.org/10.5281/zenodo.21825394) · © 2026 Isaev Iskhak Khamzatovich — personal proprietary use, see the [license terms](../../../LICENSE).*

</div>

---

<!-- enriched-r3 -->

This folder is a small but functional **shelf of its module**: it keeps a focused set of artifacts that the parent README references. The listing below is generated from the folder itself, so it is exact; the parent README explains how these pieces fit into the study. Nothing here is a compiled binary or an external download — everything is committed source, data or documentation.

The mini-module's report in three formats: DOCX, PDF and a standalone HTML rendering.

**Subfolders:** `src/`

<div align="center">

<img src="../../../assets/svg/divider-violet.svg" alt="—" width="100%" height="12"/>
</div>
