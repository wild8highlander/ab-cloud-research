<!-- AB-ENRICHED:v1 · sub -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venice&height=48&color=0:ff2ec4,100:05060f&section=header" alt="" width="100%"/>

**🧭 [⬆ core_spectrum/](../../README.md) · [🏠 Root README](../../../../../README.md)**

</div>
# V3 · Critical Line Scan

![version](https://img.shields.io/badge/version-1.2.0-298bbc) ![](https://img.shields.io/badge/series-V01--V19-3b4f58) ![](https://img.shields.io/badge/status-honest-3a6b4f)

> **Is σ = ½ optimal for the spectral statistics? An 11-point D(σ) scan with placebo and three seeds.**

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

Is σ = ½ optimal for the spectral statistics? An 11-point D(σ) scan with placebo and three seeds.

## Results

| Quantity | Value | Status |
|---|---|---|
| Campaign | V03 (plan Solution 3) | committed verdict |
| Key numbers | The curve is flat: argmin ≈ 0.8, C_h < 0, no minimum at ½ and no placebo confirmation. | measured/proved |
| Verdict note | the minimum of D(σ) near σ = 1/2 is absent or unstable — the specificity of the line is measured, not postulated (see honest remarks) | honest |

## Method

rpbridge/critical_line.py: weights q_k(σ) = log|ζ(σ+iγ̃_k)| at midpoints γ̃ (off the zeros); curvature C_h; placebo on permuted ordinates.

## Figures

| File | Where |
|---|---|
| `fig03_ru.png` | 600 dpi — `../../figures_hires/ru/`; infographics — `figures/ru/` |

## Monographs

| File | Format |
|---|---|
| `monograph_ru.pdf` | PDF |
| `monograph_ru.docx` | DOCX |

## Data

| File | Content |
|---|---|
| `data/v03_verdict.json` | committed verdict of the campaign |
| `data/` | campaign artifacts |

## Reproduction

```bash
python3 campaigns/run_v03_*.py        # verdict tour (seconds)
python3 scripts/compute_all.py v03     # fresh recomputation
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

**The σ=½ optimality claim is withdrawn (not confirmed)**

---

*AB Research Program v1.1.0 · V03 · Critical Line Scan*

<div align="center">

<img src="../../../../../assets/svg/divider-magenta.svg" alt="—" width="100%" height="12"/>
<sub>⚡ Part of <a href="../../../../../README.md">AB-Cloud Research</a> — numbers are verbatim from the unified registry; no result on this page is a claim about the Riemann hypothesis · <a href="../../README.md">⬆ parent section</a></sub>

</div>
