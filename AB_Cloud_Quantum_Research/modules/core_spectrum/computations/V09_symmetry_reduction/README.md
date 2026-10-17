# V9 · Symmetry Reduction (Th5)

![version](https://img.shields.io/badge/version-1.2.0-298bbc) ![](https://img.shields.io/badge/series-V01--V19-3b4f58) ![](https://img.shields.io/badge/status-honest-3a6b4f)

> **Does the spectrum decompose by symmetry? Magnetic torus translations and blocks.**

[← Back to the main README](../../README.md)

## Contents

1. [Campaign question](#campaign-question)
2. [Results](#results)
3. [Method](#method)
4. [Figures](#figures)
5. [Monographs](#monographs)
6. [Data](#data)
7. [Reproduction](#reproduction)
8. [Honest remarks](#honest-remarks)
9. [Verdict](#verdict)

---

## Campaign question

Does the spectrum decompose by symmetry? Magnetic torus translations and blocks.

## Results

| Quantity | Value | Status |
|---|---|---|
| Campaign | V09 (plan Solution 9) | committed verdict |
| Key numbers | ε_Ux = 0, ε_Uy = 9.4e-15; union of 6 blocks = spectrum (7.1e-15); vortices break the symmetry (ε_g = 5.1). | measured/proved |
| Verdict note | Th5 is proved and verified (the vortex-free torus: the spectrum = the union of character blocks, out-of-block elements are zero); the vortex placement breaks the symmetry (ε_g = O(1)) — the reduction explains the skeleton of the spectrum, not the arithmetic of the zeros | honest |

## Method

rpbridge/symmetry.py: A = U(2,0), B = U(0,2) — abelian G = ℤ_L×ℤ_L; the joint eigenbasis; blocks and their spectra.

## Figures

| File | Where |
|---|---|
| `fig09_ru.png` | 600 dpi — `../../figures_hires/ru/`; infographics — `figures/ru/` |

## Monographs

| File | Format |
|---|---|
| `monograph_ru.pdf` | PDF |
| `monograph_ru.docx` | DOCX |

## Data

| File | Content |
|---|---|
| `data/v09_verdict.json` | committed verdict of the campaign |
| `data/` | campaign artifacts |

## Reproduction

```bash
python3 campaigns/run_v09_*.py        # verdict tour (seconds)
python3 scripts/compute_all.py v09     # fresh recomputation
python3 -m pytest tests/ -q                     # theorem machinery
```

## Honest remarks

- Metrics are pre-registered; verdicts are committed and independent of
  fresh recomputation.
- The zero file is the only external data; no third-party research code
  is imported.
- Every claim of this campaign has a claim file (V14 audit) with the
  list of what it does NOT prove.

## Verdict

**Th5 proved and verified; vortices break the symmetry**

---

*AB Research Program v1.1.0 · V09 · Symmetry Reduction (Th5)*
