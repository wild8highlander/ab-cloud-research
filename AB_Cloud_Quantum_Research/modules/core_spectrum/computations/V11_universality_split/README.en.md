# V11 · Universality after Destruction

![version](https://img.shields.io/badge/version-1.2.0-298bbc) ![](https://img.shields.io/badge/series-V01--V19-3b4f58) ![](https://img.shields.io/badge/status-honest-3a6b4f)

> **What survives destroying the arithmetic? Modes D1/D2/D3 against universal and arithmetic metrics.**

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

What survives destroying the arithmetic? Modes D1/D2/D3 against universal and arithmetic metrics.

## Results

| Quantity | Value | Status |
|---|---|---|
| Campaign | V11 (plan Solution 11) | committed verdict |
| Key numbers | ⟨r⟩ = 0.61 → 0.59 (survives); the r_EF shift 0.17 < 2σ(A0) = 0.57 — noise-dominated; the separation is carried by V7. | measured/proved |
| Verdict note | GUE universality survives all modes of arithmetic destruction (⟨r⟩ inside the class); the arithmetic-sensitive metric r_EF on 200-level windows is noise-dominated (the mode shifts are < 2σ of the own scatter of A0) — at this resolution no feature separation is achieved; the separation is carried by the trace level V7 (PC0) | honest |

## Method

rpbridge/universality.py: 3 seeds × 4 modes; ⟨r⟩ and r_EF; the null is the own scatter of A0.

## Figures

| File | Where |
|---|---|
| `fig11_en.png` | 600 dpi — `../../figures_hires/en/`; infographics — `figures/en/` |

## Monographs

| File | Format |
|---|---|
| `monograph_en.pdf` | PDF |
| `monograph_en.docx` | DOCX |

## Data

| File | Content |
|---|---|
| `data/v11_verdict.json` | committed verdict of the campaign |
| `data/` | campaign artifacts |

## Reproduction

```bash
python3 campaigns/run_v11_*.py        # verdict tour (seconds)
python3 scripts/compute_all.py v11     # fresh recomputation
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

**Universality is an attractor; arithmetic invisible on windows**

---

*AB Research Program v1.1.0 · V11 · Universality after Destruction*
