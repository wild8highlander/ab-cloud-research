<!-- AB-ENRICHED:v2 · wave-deep-dive · monograph volumes -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=cylinder&height=72&color=0:05060f,50:ffd60a,100:05060f&section=header&text=W1%20MONOGRAPH%20VOLUMES&fontSize=22&fontColor=e5e7eb&fontAlignY=55&animation=fadeIn" alt="W1 monograph volumes" width="100%"/>

<img src="https://readme-typing-svg.demolab.com/?font=JetBrains+Mono&weight=500&size=14&duration=2600&pause=1000&color=ffd60a&center=true&vCenter=true&width=720&lines=the+W-1+monograph+in+RU+and+EN;twelve+chapter+figures+per+volume;generated+-+never+hand-edited" alt="Typing: monograph tagline"/>

**🧭 [⬆ wave_attractors/](../README.md) · [🏠 Root README](../../../README.md)**

</div>

<div align="center">

<img src="../../assets/visuals/glyph-monograph.svg" alt="Animated monograph glyph — two tomes with a glowing bookmark inside a golden medallion" width="72"/>

<img src="../../assets/ai/banner-monograph.webp" alt="AI banner: two massive scholarly tomes on a dark lectern with a glowing gold chiral-loop emblem (prompt P-W9)" width="100%"/>

</div>

<div align="center">

[![Shelf](https://img.shields.io/badge/Shelf-labs-7FC8A8?style=flat-square)](../README.md)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21825394-blue?style=flat-square)](https://doi.org/10.5281/zenodo.21825394)
[![Volumes](https://img.shields.io/badge/volumes-ru%20%C2%B7%20en-ffd60a?style=flat-square)](#-contents)

</div>

# 📕 `monograph/` — the W1 monograph in two editions

> **The W-1 monograph in RU and EN, one folder per edition.**

The publication layer of the wave-attractor study: [`ru/`](ru/) and [`en/`](en/) each hold that edition's assembled monograph — a `text/` folder with the DOCX/PDF volume and a `figures/` folder with the 12 chapter figures. The study itself is documented one level up (see the [package README](../README.md)), the numbers come from [`../data/`](../data/README.md) and the figures from [`../figures/`](../figures/README.md) — the volumes here are generated from those, never hand-edited.

<div align="center">

<img src="../../assets/visuals/book-flip.svg" alt="Animated book: pages turning from the RU edition towards the EN edition" width="100%"/>

</div>

> **🧭 Navigation:** [⬅ wave_attractors/](../README.md) · [→ report (RU)](../report/README.md) · [🏠 Repo root](../../../README.md)

## 📁 Contents

| Item | Kind | Size | What it is |
|---|---|---|---|
| `en/` | folder | 2 items | the English edition — `text/` (DOCX + PDF volume) + `figures/` (12 chapter figures) |
| `ru/` | folder | 2 items | the Russian edition — same structure, same numbers |

<details>
<summary><strong>🏭 How a volume is assembled (click)</strong></summary>

```mermaid
flowchart LR
    CEN["content_*_en.js<br/>chapters (EN)"] --> BUILD["build_monograph.js<br/>+ monograph_lib.js"]
    CRU["content_*_ru.js<br/>chapters (RU)"] --> BUILD
    META["content_meta_*.js<br/>title pages, TOC"] --> BUILD
    DATA["../data/<br/>frozen records"] --> FIG["../figures/<br/>12 canonical PNG"]
    FIG --> BUILD
    BUILD --> PP["postprocess_monograph.py<br/>+ add_toc_placeholders.py"]
    PP --> DOCX["DOCX volume"]
    DOCX --> PDF["PDF volume"]
```

The build chain lives in [`../scripts/monograph/`](../scripts/monograph/README.md); the
TOC placeholders and the post-processing pass are part of that pipeline, so the two
editions stay structurally identical. The cold-start audit reproduced the monograph
DOCX (RU/EN) with `word/document.xml` **bitwise identical**.

</details>

## 🧭 Navigation

[⬅ wave_attractors/](../README.md) · [→ report (RU)](../report/README.md) · [→ figures](../figures/README.md) · [🏠 Repo root](../../../README.md)

---

<div align="center">

<img src="../../assets/visuals/wave-divider-gold.svg" alt="Animated wave divider" width="100%" height="16"/>

<a href="../README.md"><img src="../../assets/ai/avatar.webp" alt="Study W1 avatar" width="56"/></a>

<sub>🌀 <strong>Hyperbolic Wave Attractors — study W1</strong> · part of the
<a href="../../../README.md">AB-Cloud Research</a> repository ·
DOI <a href="https://doi.org/10.5281/zenodo.21825394">10.5281/zenodo.21825394</a> ·
© 2026 Isaev Iskhak Khamzatovich — personal proprietary use, see the
<a href="../../../LICENSE">license terms</a></sub>

</div>
