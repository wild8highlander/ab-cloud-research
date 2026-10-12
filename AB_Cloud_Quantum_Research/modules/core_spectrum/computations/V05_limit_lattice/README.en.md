# V5 · The Controlled Limit L → ∞

![version](https://img.shields.io/badge/version-1.2.0-298bbc) ![](https://img.shields.io/badge/series-V01--V19-3b4f58) ![](https://img.shields.io/badge/status-honest-3a6b4f)

> **Does the spectral object converge as the lattice grows? Three kinds of convergence and an error law.**

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

Does the spectral object converge as the lattice grows? Three kinds of convergence and an error law.

## Results

| Quantity | Value | Status |
|---|---|---|
| Campaign | V05 (plan Solution 5) | committed verdict |
| Key numbers | e(L) ≈ a·L^(−0.86), R² = 0.80; projector overlap under BC perturbation 0.043; the limit is an open obligation. | measured/proved |
| Verdict note | устойчивый степенной закон конечномерной ошибки обнаружен; экстраполяция за пределы прогона — оценка, а не доказательство сходимости | honest |

## Method

rpbridge/limits.py: nested vortices (scaled from L=12); C1 levels, C2 projectors (BC perturbation), C3 trace; law fitting.

## Figures

| File | Where |
|---|---|
| `fig05_en.png` | 600 dpi — `figures_hires/en/`; infographics — `figures/en/` |

## Monographs

| File | Format |
|---|---|
| `monograph_en.pdf` | PDF |
| `monograph_en.docx` | DOCX |

## Data

| File | Content |
|---|---|
| `data/v05_verdict.json` | committed verdict of the campaign |
| `computations/V05_limit_lattice/data/` | campaign artifacts |

## Reproduction

```bash
python3 campaigns/run_v05_*.py        # verdict tour (seconds)
python3 scripts/compute_all.py v05     # fresh recomputation
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

**{'ru': 'Закон ошибки измерен', 'en': 'Power error law measured; L→∞ convergence is an estimate'}**

---

*AB Research Program v1.1.0 · V05 · The Controlled Limit L → ∞*
