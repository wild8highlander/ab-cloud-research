# AB-Cloud Monograph Package v22.1 (RU / EN / ZH + original v21)

Replacement package for the AB-cloud section of the
[research-papers](https://github.com/wild8highlander/research-papers) repository,
written from scratch on the basis of the 37-test verification suite (v18/v19,
August 2026). Every number in every document traces to a named test with a full
computation log. Package v22.1 additionally ships the **original author monograph
v21** (with verification) and its full **English edition**.

```
ab-cloud-monograph-v22/
├── README.md                        ← this file
├── REPLACE_GUIDE.md                 ← step-by-step GitHub replacement instructions
├── code/
│   └── ab_cloud_v19.jl              ← FIXED verification suite (see FIX-R1…R5 below)
├── results/
│   └── verification_run_v18_37tests_2026-08-28.txt   ← the full 37-test run this monograph is based on
├── monographs/
│   ├── ru/  ┐
│   ├── en/  ├─ text/    AB_Cloud_Monograph_v22_<LANG>.{md,html,docx,pdf}
│   │       │            AB_Cloud_Monograph_v22_<LANG>_presentation.pptx  (14 slides)
│   │       │            preprint/preprint_v22_<LANG>.{tex,pdf}
│   │       └─ figures/  19 PNG figures, 600 dpi, captions in the language of the edition
│   └── zh/  ┘
└── monograph_v21_original/          ← ORIGINAL author monograph v21 + English edition
    ├── ru/text/    AB_Cloud_Monograph_v21_RU_with_Verification.{docx,pdf} + .html + .md
    ├── en/text/    AB_Cloud_Monograph_v21_EN_with_Verification.{docx,pdf} + .html + .md
    ├── {ru,en}/presentation/  AB_Cloud_Monograph_v21_{RU,EN}_presentation.pptx (16 slides)
    ├── media/      monograph figures (shared by the html/md files)
    └── README.md   contents and citation notes (RU/EN)
```

## Contents per language

| Format | File | Purpose |
|---|---|---|
| Markdown source | `text/*_<LANG>.md` | canonical text, all figures referenced relatively |
| Interactive HTML | `text/*_<LANG>.html` | sticky TOC, MathJax, figure lightbox, print stylesheet |
| Word | `text/*_<LANG>.docx` | editable manuscript with auto-TOC |
| PDF | `text/*_<LANG>.pdf` | typeset monograph (26–29 pp.), vector |
| Presentation | `text/*_<LANG>_presentation.pptx` | 14-slide deck, dark scientific theme |
| Preprint | `text/preprint/preprint_v22_<LANG>.tex` + `.pdf` | arXiv-style preprint with bibliography |
| Figures | `figures/fig01…fig20_*.png` | 600 dpi, per-language labels |

## The original v21 monograph (monograph_v21_original/)

The author's original text with its own analytical interpretations is preserved
unmodified (RU docx) and accompanied by a complete English edition produced for
this package. Every format is provided per language: DOCX (source), PDF, an
interactive HTML (sticky TOC, lightbox), and a Markdown source; plus a 16-slide
deck per language. The v21 editions and the rewritten v22 editions are independent
works that share the same underlying verified numerics — cite v22 for the
37-test suite numbers, v21 for the V01–V115 narrative (Appendix F) and the
author's analytical interpretations.

## What changed in the code (v18 → v19)

* **FIX-R1 (critical)** — `report_blocks_to_pdf` pushed `(kind, text)` tuples into a
  `String[]`, raising `MethodError` after *every* test: all 37 verdicts degraded to
  FAIL/WARN, per-test PDFs were never produced, and the two-pass second leg
  (the QUICK CHECK 32×32 pass) never ran. The quick check therefore appeared to work
  while silently verifying nothing in pass 2.
* **FIX-R2** — a report-writer failure can no longer invalidate a completed verdict.
* **FIX-R3/3b** — Test 28 (Berry R₂(0)): `last_R2`/`berry_ref` moved to function scope
  (was `UndefVarError` after the two-pass zero loop).
* **FIX-R4** — Test 18 (AIII): lattice snaps to a multiple of 6 when
  $\alpha\in\{1/2,1/3\}$ (was `AssertionError` on 16×16).
* **FIX-R5/5b** — QUICK CHECK: ζ sample capped at 5 000 zeros, GIF disabled,
  new `--quick` CLI flag; both passes now really run.

## Reproduction

```bash
julia code/ab_cloud_v19.jl --test all     # full two-pass suite
julia code/ab_cloud_v19.jl --test 33 --no-two-pass
julia code/ab_cloud_v19.jl --quick        # 16×16 → 32×32, ζ ≤ 5000
```

Author: Isaev Iskhak Khamzatovich · ORCID 0009-0003-7299-0701 ·
DOI 10.5281/zenodo.21825394
