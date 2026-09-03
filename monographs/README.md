# Monographs — Five Editions, Trilingual Core

This directory contains **all written outcomes** of the project: the
rewritten trilingual monograph **v22** (Russian, English, Chinese), the
**original author monograph v21** with its English edition, and the
corrected **v21.1** editions that fix the "idx=38 uniqueness" claim.
Every number printed in any of these documents traces to a named test of the
37-test verification suite (`code/ab_cloud_v19.jl`) or to the spinor64
experiment (`verification/spinor64/`) with a full computation log.

## Edition map

| Edition | Path | Languages | Status |
|---|---|---|---|
| Monograph v22 (rewritten on the verified suite) | [`ru/`](ru) · [`en/`](en) · [`zh/`](zh) | RU, EN, ZH | canonical, cite these |
| Original author monograph v21 + verification | [`original-v21/`](original-v21) | RU, EN | preserved as supplied; **superseded** on the idx=38 point |
| Corrected v21.1 editions | [`original-v21/`](original-v21) (`*_corrected.*`) | RU, EN | errata of v21 — use instead of the originals |
| Rebuilt v22.1 (updated Appendix B, new Appendix D, LaTeX sources) | `*/text/*_v221.*` + `*/text/*.tex` | RU, EN, ZH | current build |

## What is stored in the editions (per language)

| Format | File pattern | Purpose |
|---|---|---|
| Markdown source | `text/AB_Cloud_Monograph_v22_<LANG>.md` | canonical text, figures referenced relatively — the file to diff/cite |
| LaTeX source | `text/AB_Cloud_Monograph_v22_<LANG>.tex` | typesettable source (added in v22.1) |
| Interactive HTML | `text/AB_Cloud_Monograph_v22_<LANG>.html` | sticky TOC, MathJax, figure lightbox, print stylesheet |
| Word | `text/AB_Cloud_Monograph_v22_<LANG>.docx` | editable manuscript with auto-TOC |
| PDF | `text/AB_Cloud_Monograph_v22_<LANG>.pdf` | typeset monograph (26–29 pp.), vector |
| Updated build | `text/AB_Cloud_Monograph_v22_<LANG>_v221.{docx,html,pdf}` | Appendix B → run `run_20260902_134759`; new Appendix D (spinor64) |
| Presentation | `text/AB_Cloud_Monograph_v22_<LANG>_presentation.pptx` | 14 slides, dark scientific theme |
| Preprint | `text/preprint/preprint_v22_<LANG>.{tex,pdf}` | arXiv-style preprint with bibliography |
| Figures | `figures/fig01…fig20_*.png` | 19–20 figures, 600 dpi, labels in the edition's language |

## The physics stored inside (what the documents actually claim)

1. **The AB-cloud mechanism** — a Hofstadter lattice with Aharonov–Bohm flux
   and topological vortices whose level spacings reproduce the GUE statistics
   of the Riemann-zero sequence (⟨r⟩, Σ²(L), Δ₃(L), K(τ) — all within
   Monte-Carlo error of GUE).
2. **The 37-test verification suite** — every headline number
   (Montgomery–Odlyzko KS = 0.047 with p = 0.27; Byers–Yang flux defect
   3.5·10⁻¹⁵; Connes self-duality zero modes; Dirac cone v_F ≈ 0.125 with
   R² = 0.9997; b(50000) = 1.2126 …) is bound to a named test and a log.
3. **Spinor structures of the Klein quartic** — v22 Appendix D (and corrected
   v21.1 §3.2.5) report the spinor64 result: all 64 structures GUE-consistent,
   PSL(2,7) orbits 28/21/7/7/1, exact isospectrality ≈ 1e-14; the v21 claim
   "only idx=38" is withdrawn (Arf(ε(38)) = 0 by the monograph's own formula).
4. **Two-pass protocol** — Appendix B documents the run
   `run_20260902_134759` (Julia 1.12.0, 50 000 Odlyzko zeros, 72×72 → 96×96
   HARDCORE pass 2), whose raw artifacts live in `results/`.

## Which file should I open?

- *Reading for the physics* → `text/AB_Cloud_Monograph_v22_EN.pdf`
  (or `_v221.pdf` for the updated appendices).
- *Editing / reusing text* → the `.md` or `.tex` source.
- *Citing the corrected spinor result* → v22.1 Appendix D, or
  `original-v21/*_corrected.pdf` §3.2.5.
- *The author's original narrative (V01–V115 runs, Appendix F)* →
  `original-v21/`.

## Rebuilding the formats

The `.md` → `.html/.docx` chain uses pandoc + a shared stylesheet
(`original-v21/*/text/mono.css` holds the CSS used for the HTML builds);
`.tex` → `.pdf` uses any LaTeX engine with `polyglossia`/`ctex` support
(`xelatex` recommended for the ZH edition; run twice for TOC/refs). The
committed binaries were produced with exactly these tools — no hidden
pre-processing step exists.

## Кратко (по-русски)

- Пять изданий: монография v22 на трёх языках (RU/EN/ZH), оригинальная v21
  автора с английским изданием, исправленные v21.1 и пересобранные v22.1.
- Форматы на язык: md/tex (исходники), html (интерактив), docx, pdf,
  14-слайдовая презентация, arXiv-препринт, 19–20 рисунков 600 dpi.
- Внутри — вся физика проекта с привязкой каждого числа к именному тесту
  37-тестового набора; Приложение D описывает spinor64 (все 64 структуры
  GUE-согласованы, «уникальность idx=38» снята).
- Цитировать v22/v22.1; v21 — только как оригинальное повествование автора.
