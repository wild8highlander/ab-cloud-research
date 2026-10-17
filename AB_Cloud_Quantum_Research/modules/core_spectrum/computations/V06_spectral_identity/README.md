# V6 · Spectral Identity

![version](https://img.shields.io/badge/version-1.2.0-298bbc) ![](https://img.shields.io/badge/series-V01--V19-3b4f58) ![](https://img.shields.io/badge/status-honest-3a6b4f)

> **Does the characteristic function coincide with ξ? A direct test and the positive control H_ξ.**

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

Does the characteristic function coincide with ξ? A direct test and the positive control H_ξ.

## Results

| Quantity | Value | Status |
|---|---|---|
| Campaign | V06 (plan Solution 6) | committed verdict |
| Key numbers | Gates: rank 0.036 — no identity; H_ξ: log residual 5.8e-10 — identity holds (trivially, by construction). | measured/proved |
| Verdict note | the spectral identity (n ↔ the zero n) for the lattice gates — YES at the zeros' own level (the D_nn bridge: 0.0079 = the level of shifted zero windows and the GUE class, v2.0.7); the rank branch is at the resolution limit; for H_ξ — YES by construction; the goal of V6 is the analytic identity, not polynomial fitting | honest |

## Method

rpbridge/spectral_identity.py: ranks vs zeros; the Hadamard control ln Π|z²−γ²| − ln|ξ| = const (a + b·z² regression); gaps and multiplicities.

## Figures

| File | Where |
|---|---|
| `fig06_ru.png` | 600 dpi — `../../figures_hires/ru/`; infographics — `figures/ru/` |

## Monographs

| File | Format |
|---|---|
| `monograph_ru.pdf` | PDF |
| `monograph_ru.docx` | DOCX |

## Data

| File | Content |
|---|---|
| `data/v06_verdict.json` | committed verdict of the campaign |
| `data/` | campaign artifacts |

## Reproduction

```bash
python3 campaigns/run_v06_*.py        # verdict tour (seconds)
python3 scripts/compute_all.py v06     # fresh recomputation
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

**Identity: YES for H_ξ; for gates — YES at the zeros' level (the D_nn bridge, v2.0.7)**

---

*AB Research Program v1.1.0 · V06 · Spectral Identity*
