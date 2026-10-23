<!-- AB-ENRICHED:v1 · sub -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venice&height=48&color=0:ff2ec4,100:05060f&section=header" alt="" width="100%"/>

**🧭 [⬆ core_spectrum/](../../README.md) · [🏠 Root README](../../../../../README.md)**

</div>
# V1 · Blind Spectral Experiment

![version](https://img.shields.io/badge/version-1.2.0-298bbc) ![](https://img.shields.io/badge/series-V01--V19-3b4f58) ![](https://img.shields.io/badge/status-honest-3a6b4f)

> **Can the algorithm predict ordinates it has never seen? Split G_cal ⊔ G_test, calibrate on G_cal only, one blind run.**

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

Can the algorithm predict ordinates it has never seen? Split G_cal ⊔ G_test, calibrate on G_cal only, one blind run.

## Results

| Quantity | Value | Status |
|---|---|---|
| Campaign | V01 (plan Solution 1) | committed verdict |
| Key numbers | r_test = 0.006 against null −0.002 ± 0.066 (z = 0.09); r_cal = 0.085 (selection over 8); no identity on test. | measured/proved |
| Verdict note | the blind control is passed; individual ordinates are not predicted (r_test in the null zone), the statistical class is the subject of V2/V11 | honest |

## Method

rpbridge/blind.py: 8 calibration configurations (master seed 96…103), a 200-level window, rank correlation of increments via the RVM count, permutation null (200 shuffles).

## Figures

| File | Where |
|---|---|
| `fig01_ru.png` | 600 dpi — `../../figures_hires/ru/`; infographics — `figures/ru/` |

## Monographs

| File | Format |
|---|---|
| `monograph_ru.pdf` | PDF |
| `monograph_ru.docx` | DOCX |

## Data

| File | Content |
|---|---|
| `data/v01_verdict.json` | committed verdict of the campaign |
| `data/` | campaign artifacts |

## Reproduction

```bash
python3 campaigns/run_v01_*.py        # verdict tour (seconds)
python3 scripts/compute_all.py v01     # fresh recomputation
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

**Blind control passed: individual ordinates are not predicted**

---

*AB Research Program v1.1.0 · V01 · Blind Spectral Experiment*

<div align="center">

<img src="../../../../../assets/svg/divider-magenta.svg" alt="—" width="100%" height="12"/>
<sub>⚡ Part of <a href="../../../../../README.md">AB-Cloud Research</a> — numbers are verbatim from the unified registry; no result on this page is a claim about the Riemann hypothesis · <a href="../../README.md">⬆ parent section</a></sub>

</div>
