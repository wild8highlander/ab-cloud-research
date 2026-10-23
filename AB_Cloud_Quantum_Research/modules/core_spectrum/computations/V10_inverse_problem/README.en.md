<!-- AB-ENRICHED:v1 · sub -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venice&height=48&color=0:ff2ec4,100:05060f&section=header" alt="" width="100%"/>

**🧭 [⬆ V10_inverse_problem/](README.md) · [🏠 Root README](../../../../../README.md)**

</div>
# V10 · The Inverse Problem

![version](https://img.shields.io/badge/version-1.2.0-298bbc) ![](https://img.shields.io/badge/series-V01--V19-3b4f58) ![](https://img.shields.io/badge/status-honest-3a6b4f)

> **Can the arithmetic be recovered from the spectrum? Power traces, the sensitivity matrix, optimization.**

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

Can the arithmetic be recovered from the spectrum? Power traces, the sensitivity matrix, optimization.

## Results

| Quantity | Value | Status |
|---|---|---|
| Campaign | V10 (plan Solution 10) | committed verdict |
| Key numbers | rank J = 6 (k=6), cond ≈ 8.7e4; recovery \|Δq\| = 0.077; separation 1.6–3.5; identifiability is rank-limited. | measured/proved |
| Verdict note | part of the arithmetic (the charges) is identifiable from the higher traces given a sufficient k; rank J < n_params ⇒ full identifiability of the positions is unreachable from the invariants of this class — measured | honest |

## Method

rpbridge/inverse.py: Φ = (Tr H, …, Tr H⁶); J numeric; Nelder–Mead from 3 starts; arithmetic/random separation.

## Figures

| File | Where |
|---|---|
| `fig10_en.png` | 600 dpi — `../../figures_hires/en/`; infographics — `figures/en/` |

## Monographs

| File | Format |
|---|---|
| `monograph_en.pdf` | PDF |
| `monograph_en.docx` | DOCX |

## Data

| File | Content |
|---|---|
| `data/v10_verdict.json` | committed verdict of the campaign |
| `data/` | campaign artifacts |

## Reproduction

```bash
python3 campaigns/run_v10_*.py        # verdict tour (seconds)
python3 scripts/compute_all.py v10     # fresh recomputation
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

**Part of the arithmetic is unidentifiable (rank-limited)**

---

*AB Research Program v1.1.0 · V10 · The Inverse Problem*

<div align="center">

<img src="../../../../../assets/svg/divider-magenta.svg" alt="—" width="100%" height="12"/>
</div>
