# Monograph v22 — Russian Edition

The Russian edition of the rewritten monograph *"AB-Cloud — a phase resonator
for the zeros of the Riemann zeta function"*, built from scratch on the
37-test verification suite (v18/v19). Every figure and every number in the
text is bound to a named test with a full computation log.

## Files (everything in `text/` unless noted)

| File | What it is |
|---|---|
| `AB_Cloud_Monograph_v22_RU.md` | canonical Markdown source (figures referenced relatively) |
| `AB_Cloud_Monograph_v22_RU.tex` | LaTeX source (added in v22.1) |
| `AB_Cloud_Monograph_v22_RU.html` | interactive version: sticky TOC, MathJax, figure lightbox, print stylesheet |
| `AB_Cloud_Monograph_v22_RU.docx` | editable manuscript with auto-TOC |
| `AB_Cloud_Monograph_v22_RU.pdf` | typeset monograph, vector PDF |
| `AB_Cloud_Monograph_v22_RU_v221.docx / _v221.html / _v221.pdf` | v22.1 build: Appendix B updated to the `run_20260902_134759` run, new Appendix D (spinor64) |
| `AB_Cloud_Monograph_v22_RU_presentation.pptx` | 14-slide deck, dark scientific theme |
| `preprint/preprint_v22_RU.tex` + `.pdf` | arXiv-style preprint with bibliography |
| `figures/fig01…fig20_*.png` | 19–20 figures, 600 dpi, Russian labels |

## What the text contains

- The AB-cloud mechanism: a Hofstadter lattice with AB flux and topological
  vortices; the GUE statistics of its spectrum against the zeta zeros
  (⟨r⟩, Σ²(L), Δ₃(L), K(τ)).
- The full 37-test suite narrative: b(N) convergence (b(50000) = 1.2126),
  the Montgomery test (KS = 0.047, p = 0.27), the Byers–Yang defect 3.5·10⁻¹⁵,
  Connes self-duality, the Dirac cone (v_F ≈ 0.125, R² = 0.9997).
- Appendix B (in the v22.1 build): the two-pass protocol of run
  `run_20260902_134759` — Julia 1.12.0, 50 000 Odlyzko zeros, pass 2 at
  96×96 (HARDCORE), 37/37 tests completed.
- Appendix D (in the v22.1 build): spinor64 — all 64 spinor structures
  GUE-consistent; PSL(2,7) orbits 28/21/7/7/1; isospectrality ~1e-14;

## How to read / rebuild

- Read: `AB_Cloud_Monograph_v22_RU_v221.pdf` — the freshest build.
- Edit: `.md` (or `.tex`), then rebuild HTML/DOCX via pandoc
  (CSS — `original-v21/ru/text/mono.css`), PDF via `xelatex` on the `.tex`
  (two passes).

## In short

- The Russian edition of monograph v22 + the updated v22.1 build (Appendices
  B and D) and the LaTeX sources.
- Fresh PDF for reading: `text/AB_Cloud_Monograph_v22_RU_v221.pdf`.
- Every number is bound to suite tests; the raw run artifacts live in
  `results/Test 1-37 ab_cloud_full.jl/run_20260902_134759/`.

---

*English note:* this folder holds the **Russian edition** of the rewritten
monograph (v22 + the updated v22.1 build with LaTeX sources). See the
repository-root README for the trilingual overview.

## 📁 Complete file inventory

| Entry | Size | Kind |
|---|---|---|
| `figures/` | 20 files, 5.5 MB | directory — 19 figures + README |
| `text/` | 12 files, 49.9 MB | directory — incl. `preprint/` |
| `README.md` | 4.0 KB | file |
| **Total (recursive)** | **33 files, ≈55 MB** | |

## 🔬 Deep dive — working with the Russian edition

The Russian edition is fully parallel to the English and Chinese ones: the
same base v22 text, the same appendices in the v22.1 rebuild (Appendix B —
the two-pass run `run_20260902_134759` on 50 000 Odlyzko zeros, the second
pass "HARDCORE" on the 96×96 lattice; Appendix D — spinor64), the same
19–20 figures with Russian labels. The format line-up is identical: md and
tex — the sources, html — the interactive version with a sticky TOC, MathJax
and a figure lightbox, docx — the editable manuscript with auto-TOC, pdf —
the 26–29-page typeset build, plus a 14-slide presentation and an
arXiv-style preprint.

Practical scenarios. For reading, open
`text/AB_Cloud_Monograph_v22_RU_v221.pdf` — the current build with both
updated appendices. For citing in your own texts, reference the `.md`
source: it is canonical, diffable and bound to commits. For typesetting
edits, edit the `.tex` and build with xelatex twice. Every number in the
text (the KS distance 0.047 at p = 0.27, the Byers–Yang flux defect 3.5e-15,
the Dirac-cone slope v_F ≈ 0.125 at R² = 0.9997, ⟨r⟩ = 0.5848 ± 0.0260 vs
GUE 0.5992) is bound to a named test of the 37-test suite, and the run logs
live in `results/` — verification requires running nothing.

## In short

- The current build is `_v221.pdf` (Appendix B on the 2026-09-02 run,
  Appendix D with spinor64: 64/64 GUE).
- Cite the `.md` source; edit the typesetting in the `.tex` + xelatex ×2.
- Every number is bound to a named test; the logs are in `results/`.
