# Monograph v22 — English Edition

The English edition of the rewritten monograph *"AB-Cloud: a phase resonator
for the zeros of the Riemann zeta function"*, built from scratch on the
verified 37-test suite (v18/v19). Every figure and every number in the text
is bound to a named test with a full computation log.

## Files (everything in `text/` unless noted)

| File | What it is |
|---|---|
| `AB_Cloud_Monograph_v22_EN.md` | canonical Markdown source (figures referenced relatively) |
| `AB_Cloud_Monograph_v22_EN.tex` | LaTeX source (added in v22.1) |
| `AB_Cloud_Monograph_v22_EN.html` | interactive version: sticky TOC, MathJax, figure lightbox, print stylesheet |
| `AB_Cloud_Monograph_v22_EN.docx` | editable manuscript with auto-TOC |
| `AB_Cloud_Monograph_v22_EN.pdf` | typeset monograph, vector PDF (26–29 pp.) |
| `AB_Cloud_Monograph_v22_EN_v221.docx / _v221.html / _v221.pdf` | v22.1 build: Appendix B updated to the `run_20260902_134759` two-pass run, new Appendix D (spinor64) |
| `AB_Cloud_Monograph_v22_EN_presentation.pptx` | 14-slide deck, dark scientific theme |
| `preprint/preprint_v22_EN.tex` + `.pdf` | arXiv-style preprint with bibliography |
| `figures/fig01…fig20_*.png` | 19–20 figures, 600 dpi, English labels |

## What the text contains

1. **The AB-cloud mechanism** — a Hofstadter lattice with AB flux and
   topological vortices; its spectrum reproduces the GUE statistics of the
   zeta zeros (⟨r⟩, Σ²(L), Δ₃(L), K(τ)).
2. **The 37-test suite narrative** — b(N) convergence (b(50000) = 1.2126),
   Montgomery test (KS = 0.047, p = 0.27), Byers–Yang defect 3.5·10⁻¹⁵,
   Connes self-duality, Dirac cone (v_F ≈ 0.125, R² = 0.9997).
3. **Appendix B (v22.1)** — the `run_20260902_134759` two-pass protocol:
   Julia 1.12.0, 50 000 Odlyzko zeros, HARDCORE pass 2 at 96×96.
4. **Appendix D (v22.1)** — spinor64: **all 64 spinor structures
   GUE-consistent**; PSL(2,7) orbits 28/21/7/7/1; isospectrality ≈ 1e-14;
   the v21 "idx=38 uniqueness" withdrawn (Arf(ε(38)) = 0 by the monograph's
   own formula).

## How to read / rebuild

- Read: `text/AB_Cloud_Monograph_v22_EN_v221.pdf` — the freshest build.
- Edit: `.md` (or `.tex`), then rebuild HTML/DOCX via pandoc; PDF via
  `xelatex` on the `.tex` (two passes).

## Кратко (по-русски)

- Английское издание монографии v22 + сборка v22.1 (Приложения B и D) и
  LaTeX-исходники.
- Свежий PDF: `text/AB_Cloud_Monograph_v22_EN_v221.pdf`.
- Каждое число привязано к именному тесту набора v19.

## 📁 Complete file inventory

| Entry | Size | Kind |
|---|---|---|
| `figures/` | 19 files, 5.2 MB | directory |
| `text/` | 11 files, 48.0 MB | directory |
| `README.md` | 2.6 KB | file |
| **Total (recursive)** | **31 files, 53.2 MB** | |

## 🔬 Deep dive — working with the English edition

Reading paths. For linear reading open
`text/AB_Cloud_Monograph_v22_EN.pdf`, or its updated build
`text/AB_Cloud_Monograph_v22_EN_v221.pdf` when you need the two-pass
Appendix B and the spinor64 Appendix D. For diffing, quoting and machine
processing use the canonical Markdown source; for typesetting edits use
the LaTeX source added in v22.1. The interactive HTML mirrors the PDF
one-to-one and adds a sticky TOC, MathJax rendering and a figure
lightbox, so it is the best format for on-screen review with comments.

What the text claims, in one paragraph. The monograph models the
Riemann-zero sequence as the spectrum of a Hofstadter lattice with
Aharonov–Bohm flux and topological vortices (the "AB cloud"), and
demonstrates GUE-level agreement on four independent statistics — ⟨r⟩,
Σ²(L), Δ₃(L) and K(τ) — with the pair-correlation KS distance 0.047
(p = 0.27), the Byers–Yang flux defect at 3.5e-15, Connes self-duality
via four zero modes, and the Dirac-cone slope v_F ≈ 0.125 with R² = 0.9997.
Each of these numbers is bound to a named test of the 37-test suite and
to a committed log under `results/`, so a referee can check any claim
without running anything.

Rebuilding the formats locally. The Markdown source is the single
upstream artifact: `pandoc` produces the HTML and DOCX, `xelatex` (run
twice) produces the PDF from the `.tex` source, and the presentation and
preprint are separate pandoc/LaTeX targets of the same text. Figures are
pre-rendered PNGs at 600 dpi under `figures/` (fig01–fig20), referenced
by relative paths, so no plotting step is required to rebuild any
format. Citation metadata lives in the repository-root `CITATION.cff`
and resolves to ORCID 0009-0003-7299-0701.

## Кратко (по-русски)

- Английское издание v22: читать — `_v221.pdf` (обновлённые приложения),
  сверять и цитировать — `.md`, править вёрстку — `.tex`.
- Все ключевые числа (KS = 0.047, p = 0.27; дефект потока 3.5e-15;
  v_F ≈ 0.125, R² = 0.9997) привязаны к именным тестам набора.
- Пересборка без сюрпризов: pandoc → html/docx, xelatex ×2 → pdf;
  рисунки уже отрендерены (600 dpi, относительные пути).
