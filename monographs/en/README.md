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
