<!-- AB-ENRICHED:v2 · wave-deep-dive · monograph build chain -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venice&height=60&color=0:05060f,50:00e5ff,100:05060f&section=header&text=W1%20MONOGRAPH%20BUILD&fontSize=22&fontColor=e5e7eb&fontAlignY=55&animation=twoline" alt="W1 monograph build" width="100%"/>

<img src="https://readme-typing-svg.demolab.com/?font=JetBrains+Mono&weight=500&size=14&duration=2600&pause=1000&color=00e5ff&center=true&vCenter=true&width=720&lines=npm-managed+document+assembly;content+js+%E2%86%92+DOCX+%E2%86%92+PDF;two+editions+one+structure" alt="Typing: monograph build tagline"/>

**🧭 [⬆ scripts/](../README.md) · [⬆⬆ wave_attractors/](../../README.md) · [🏠 Root README](../../../../README.md)**

</div>

<div align="center">

<img src="../../../assets/visuals/glyph-monograph-build.svg" alt="Animated build glyph — a press compressing pages inside a cyan medallion" width="72"/>

<img src="../../../assets/ai/banner-monograph-build.webp" alt="AI banner: an automated printing atelier — glowing pages assembling into a book block (prompt P-W13)" width="100%"/>

</div>

# 🖨 `scripts/monograph/` — assembling the volumes

> **The npm-managed build chain that turns JavaScript chapter sources into the DOCX and
> PDF monograph volumes** of study W1 (RU and EN). The chapters are code, not
> word-processor files — which is exactly why the assembled volumes came out bitwise
> reproducible in the cold-start audit.

<div align="center">

<img src="../../../assets/visuals/press.svg" alt="Animated press: pages travel through the press and assemble into the DOCX+PDF book block" width="100%"/>

</div>

[![Build](https://img.shields.io/badge/build-npm%20managed-00e5ff?style=flat-square)](build_monograph.js)
[![Output](https://img.shields.io/badge/output-DOCX%20%2B%20PDF-ffd60a?style=flat-square)](../../monograph/README.md)
[![Audit](https://img.shields.io/badge/audit-document.xml%20bitwise--identical-2EA043?style=flat-square)](../../README.md#reproducibility)

> **🧭 Navigation:** [⬆ scripts/](../README.md) · [⬆⬆ wave_attractors/](../../README.md) · [🏠 Root README](../../../../README.md)

## 📁 Inventory

| Item | What it is |
|---|---|
| [`add_toc_placeholders.py`](add_toc_placeholders.py) | inserts TOC placeholders before final assembly |
| [`build_monograph.js`](build_monograph.js) | the assembler — chapters + figures → DOCX |
| [`content_a_en.js`](content_a_en.js) · [`content_b_en.js`](content_b_en.js) | English chapter sources (parts A and B) |
| [`content_a_ru.js`](content_a_ru.js) · [`content_b_ru.js`](content_b_ru.js) | Russian chapter sources (parts A and B) |
| [`content_meta_en.js`](content_meta_en.js) · [`content_meta_ru.js`](content_meta_ru.js) | title pages, abstracts, TOC metadata per edition |
| [`monograph_lib.js`](monograph_lib.js) | shared layout/formatting library |
| [`package.json`](package.json) | npm manifest of the build chain |
| [`postprocess_monograph.py`](postprocess_monograph.py) | the final pass over the assembled documents |

```mermaid
flowchart LR
    A["content_a_{en,ru}.js<br/>chapters part A"] --> B["build_monograph.js"]
    Bm["content_b_{en,ru}.js<br/>chapters part B"] --> B
    M["content_meta_{en,ru}.js<br/>titles · TOC"] --> B
    LIB["monograph_lib.js"] --> B
    B --> TOC["add_toc_placeholders.py"]
    TOC --> PP["postprocess_monograph.py"]
    PP --> OUT{"../monograph/<br/>ru/ · en/"}
```

<details>
<summary><strong>📐 Why chapters-as-code (click)</strong></summary>

Because the numbers must be **verbatim from the frozen data**: chapter sources reference
the experiment records, so a change in any result propagates through a rebuild, not
through hand-editing prose. The structure of both editions is fixed by the same builder,
which is why `ru/` and `en/` volumes stay chapter-aligned and why the audit could demand
— and obtain — a `word/document.xml` bitwise match for both languages.

</details>

## 🧭 Navigation

[⬅ scripts/](../README.md) · [→ report build](../report/README.md) · [→ julia port](../julia/README.md) · [🏠 Repo root](../../../../README.md)

---

<div align="center">

<img src="../../../assets/visuals/wave-divider-cyan.svg" alt="Animated wave divider" width="100%" height="16"/>

<a href="../../README.md"><img src="../../../assets/ai/avatar.webp" alt="Study W1 avatar" width="56"/></a>

<sub>🌀 <strong>Hyperbolic Wave Attractors — study W1</strong> · part of the
<a href="../../../../README.md">AB-Cloud Research</a> repository ·
DOI <a href="https://doi.org/10.5281/zenodo.21825394">10.5281/zenodo.21825394</a> ·
© 2026 Isaev Iskhak Khamzatovich — personal proprietary use, see the
<a href="../../../../LICENSE">license terms</a></sub>

</div>
