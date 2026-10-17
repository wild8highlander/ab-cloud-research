# V12 · Interval Certificates (Th3)

![version](https://img.shields.io/badge/version-1.2.0-298bbc) ![](https://img.shields.io/badge/series-V01--V19-3b4f58) ![](https://img.shields.io/badge/status-honest-3a6b4f)

> **Are the numerical bounds guaranteed? Gershgorin in rational arithmetic + residuals at dps=40.**

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

Are the numerical bounds guaranteed? Gershgorin in rational arithmetic + residuals at dps=40.

## Results

| Quantity | Value | Status |
|---|---|---|
| Campaign | V12 (plan Solution 12) | committed verdict |
| Key numbers | 5/5 certificates contain the true λ; width ~1e-27; Gershgorin [−4.21, 4.21] covers the spectrum. | measured/proved |
| Verdict note | all certificates contain the true values; the intervals are guaranteed, not decimal tolerances; 1e-15 accuracy in float ≠ the mathematical accuracy of the model (plan, Solution 12) | honest |

## Method

rpbridge/intervalcert.py: fractions radii; the Kato estimate δ²/gap; exact gaps.

## Figures

| File | Where |
|---|---|
| `fig12_ru.png` | 600 dpi — `../../figures_hires/ru/`; infographics — `figures/ru/` |

## Monographs

| File | Format |
|---|---|
| `monograph_ru.pdf` | PDF |
| `monograph_ru.docx` | DOCX |

## Data

| File | Content |
|---|---|
| `data/v12_verdict.json` | committed verdict of the campaign |
| `data/` | campaign artifacts |

## Reproduction

```bash
python3 campaigns/run_v12_*.py        # verdict tour (seconds)
python3 scripts/compute_all.py v12     # fresh recomputation
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

**Key numbers carry guaranteed intervals**

---

*AB Research Program v1.1.0 · V12 · Interval Certificates (Th3)*
