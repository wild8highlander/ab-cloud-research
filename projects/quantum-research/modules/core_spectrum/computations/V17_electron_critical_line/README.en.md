<!-- AB-ENRICHED:v1 · sub -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venice&height=48&color=0:ff2ec4,100:05060f&section=header" alt="" width="100%"/>

**🧭 [⬆ V17_electron_critical_line/](README.md) · [🏠 Root README](../../../../../README.md)**

</div>
# V17 · Electron on the Critical Line

![version](https://img.shields.io/badge/version-1.2.0-298bbc) ![](https://img.shields.io/badge/series-V01--V19-3b4f58) ![](https://img.shields.io/badge/status-honest-3a6b4f)

> **Does an electron (a wave packet) pass coherently along the self-dual line channel α = ½, and does the ζ-cloud guide it? A 96×24 waveguide, T = 40, three clouds.**

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

Does an electron (a wave packet) pass coherently along the self-dual line channel α = ½, and does the ζ-cloud guide it? A 96×24 waveguide, T = 40, three clouds.

## Results

| Quantity | Value | Status |
|---|---|---|
| Campaign | V17 (plan Solution 17) | committed verdict |
| Key numbers | Energy 1.8e-15; transit: clean 0.160 / ζ 0.112 / random 0.069 (ζ/ran = ×1.62); D_y: ζ 2.81 vs 0.54; r_phase: ζ −0.96 vs random −0.52. | measured/proved |
| Verdict note | honest dynamics | honest |

## Method

rpbridge/electron.py: exact eigenbasis dynamics (2304×2304), packet σ=3, k₀=π/2; transit P(x≥88), deviation D_y, coherence C(t), θ-phase accompaniment along the trajectory.

## Figures

| File | Where |
|---|---|
| `fig18_en.png` | 600 dpi — `../../figures_hires/en/`; infographics — `figures/en/` |

## Monographs

| File | Format |
|---|---|
| `monograph_en.pdf` | PDF |
| `monograph_en.docx` | DOCX |

## Data

| File | Content |
|---|---|
| `data/results.json` | committed verdict of the campaign |
| `data/` | campaign artifacts |

## Reproduction

```bash
python3 campaigns/run_v17_*.py        # verdict tour (seconds)
python3 scripts/compute_all.py v17     # fresh recomputation
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

**Honest dynamics; the ζ-cloud guides ×1.62; the line½ = Re(s)½ bridge is a conjecture (H4 YES)**

---

*AB Research Program v1.1.0 · V17 · Electron on the Critical Line*

<div align="center">

<img src="../../../../../assets/svg/divider-magenta.svg" alt="—" width="100%" height="12"/>
<sub>⚡ Part of <a href="../../../../../README.md">AB-Cloud Research</a> — numbers are verbatim from the unified registry; no result on this page is a claim about the Riemann hypothesis · <a href="README.md">⬆ parent section</a></sub>

</div>
