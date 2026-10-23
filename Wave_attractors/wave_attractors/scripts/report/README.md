<!-- AB-ENRICHED:v2 · wave-deep-dive · report build chain -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=cylinder&height=72&color=0:05060f,50:ffd60a,100:05060f&section=header&text=W1%20REPORT%20BUILD&fontSize=22&fontColor=e5e7eb&fontAlignY=55&animation=fadeIn" alt="W1 report build" width="100%"/>

<img src="https://readme-typing-svg.demolab.com/?font=JetBrains+Mono&weight=500&size=14&duration=2600&pause=1000&color=ffd60a&center=true&vCenter=true&width=720&lines=content+%E2%86%92+build+%E2%86%92+cover+%E2%86%92+merge;14+pages+of+process+detail;the+seal+pressed+by+code" alt="Typing: report build tagline"/>

**🧭 [⬆ scripts/](../README.md) · [⬆⬆ wave_attractors/](../../README.md) · [🏠 Root README](../../../../README.md)**

</div>

<div align="center">

<img src="../../../assets/visuals/glyph-report-build.svg" alt="Animated build glyph — a stamp pressing a golden seal inside a medallion" width="72"/>

<img src="../../../assets/ai/banner-report-build.webp" alt="AI banner: a typographic compose room with glowing type blocks and a sealed sheet taking shape under a beam of light (prompt P-W14)" width="100%"/>

</div>

# 🏷 `scripts/report/` — building the RU report

> **The typography chain behind the 14-page Russian working report** of study W1:
> content in code, layout in a palette module, cover as HTML→PDF, everything merged
> into the committed document. The audit's verdict on this chain: rebuilt PDF came out
> with **extracted text identical** to the committed copy.

<div align="center">

<img src="../../../assets/visuals/stamp.svg" alt="Animated stamp: the seal is pressed onto the assembled report" width="100%"/>

</div>

[![Output](https://img.shields.io/badge/output-PDF%20%C2%B7%2014%20pages-ffd60a?style=flat-square)](../../report/README.md)
[![Cover](https://img.shields.io/badge/cover-HTML%20%E2%86%92%20PDF-ff2ec4?style=flat-square)](w1_cover.html)
[![Audit](https://img.shields.io/badge/audit-text%20identical-2EA043?style=flat-square)](../../README.md#reproducibility)

> **🧭 Navigation:** [⬆ scripts/](../README.md) · [⬆⬆ wave_attractors/](../../README.md) · [🏠 Root README](../../../../README.md)

## 📁 Inventory

| Item | What it is |
|---|---|
| [`w1_report_content.py`](w1_report_content.py) | the report text, structured as data |
| [`w1_report_build.py`](w1_report_build.py) | the builder — content + palette → PDF body |
| [`w1_palette.py`](w1_palette.py) | the report's color/typography system |
| [`report_font_fallback.py`](report_font_fallback.py) | font availability guards for reproducible rendering |
| [`w1_cover.html`](w1_cover.html) · [`w1_cover.pdf`](w1_cover.pdf) | the cover page (source and rendered) |
| [`w1_merge.py`](w1_merge.py) | merges cover + body into the final PDF |

```mermaid
flowchart LR
    C["w1_report_content.py"] --> B["w1_report_build.py"]
    P["w1_palette.py"] --> B
    FF["report_font_fallback.py"] --> B
    B --> BODY["PDF body"]
    H["w1_cover.html"] --> CPDF["w1_cover.pdf"]
    CPDF --> M["w1_merge.py"]
    BODY --> M
    M --> OUT{"../report/<br/>Отчёт W1 · 14 pages"}
```

<details>
<summary><strong>🎨 Why a dedicated palette module (click)</strong></summary>

Because reproducibility extends to *look*: `w1_palette.py` pins the report's colors and
typography so that a rebuild does not merely carry identical text — it renders with the
same visual system. The font-fallback module guards the pipeline against environment
differences (missing typefaces would silently change pagination), which is one of the
quiet ways otherwise-deterministic PDF chains drift.

</details>

## 🧭 Navigation

[⬅ scripts/](../README.md) · [→ monograph build](../monograph/README.md) · [→ julia port](../julia/README.md) · [🏠 Repo root](../../../../README.md)

---

<div align="center">

<img src="../../../assets/visuals/wave-divider-gold.svg" alt="Animated wave divider" width="100%" height="16"/>

<a href="../../README.md"><img src="../../../assets/ai/avatar.webp" alt="Study W1 avatar" width="56"/></a>

<sub>🌀 <strong>Hyperbolic Wave Attractors — study W1</strong> · part of the
<a href="../../../../README.md">AB-Cloud Research</a> repository ·
DOI <a href="https://doi.org/10.5281/zenodo.21825394">10.5281/zenodo.21825394</a> ·
© 2026 Isaev Iskhak Khamzatovich — personal proprietary use, see the
<a href="../../../../LICENSE">license terms</a></sub>

</div>
