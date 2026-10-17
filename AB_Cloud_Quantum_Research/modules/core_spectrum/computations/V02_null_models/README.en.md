# V2 · Arithmetic Null Models

![version](https://img.shields.io/badge/version-1.2.0-298bbc) ![](https://img.shields.io/badge/series-V01--V19-3b4f58) ![](https://img.shields.io/badge/status-honest-3a6b4f)

> **Does lattice chaos alone produce the same statistics? Five model families against a pre-registered vector S.**

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

Does lattice chaos alone produce the same statistics? Five model families against a pre-registered vector S.

## Results

| Quantity | Value | Status |
|---|---|---|
| Campaign | V02 (plan Solution 2) | committed verdict |
| Key numbers | M0: ⟨r⟩ = 0.6093, D_KS = 0.0499 — GUE class; N3 (no vortices): 0.273 — outside; the reference ladder is reproduced. | measured/proved |
| Verdict note | the AB cloud falls into the GUE class together with N1/N4; the specificity of arithmetic is measured not by ⟨r⟩ but by the arithmetic-sensitive metrics V7/V11 | honest |

## Method

rpbridge/nullmodels.py: M0/N1/N3/N4 + GUE/GOE/Poisson references; ensemble GUE reference for D_KS (16 matrices); Bonferroni over 5 families.

## Figures

| File | Where |
|---|---|
| `fig02_en.png` | 600 dpi — `../../figures_hires/en/`; infographics — `figures/en/` |

## Monographs

| File | Format |
|---|---|
| `monograph_en.pdf` | PDF |
| `monograph_en.docx` | DOCX |

## Data

| File | Content |
|---|---|
| `data/v02_verdict.json` | committed verdict of the campaign |
| `data/` | campaign artifacts |

## Reproduction

```bash
python3 campaigns/run_v02_*.py        # verdict tour (seconds)
python3 scripts/compute_all.py v02     # fresh recomputation
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

**The GUE class is not specific; arithmetic lives in traces (V7)**

---

*AB Research Program v1.1.0 · V02 · Arithmetic Null Models*
