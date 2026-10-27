<!-- AB-ENRICHED:v1 · sub -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venice&height=48&color=0:ff2ec4,100:05060f&section=header" alt="" width="100%"/>

**🧭 [⬆ core_spectrum/](../../README.md) · [🏠 Root README](../../../../../README.md)**

</div>
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
| Verdict note | a stable power law of the finite-dimensional error is found; extrapolation beyond the run is an estimate, not a proof of convergence | honest |

## Method

rpbridge/limits.py: nested vortices (scaled from L=12); C1 levels, C2 projectors (BC perturbation), C3 trace; law fitting.

## Figures

| File | Where |
|---|---|
| `fig05_ru.png` | 600 dpi — `../../figures_hires/ru/`; infographics — `figures/ru/` |

## Monographs

| File | Format |
|---|---|
| `monograph_ru.pdf` | PDF |
| `monograph_ru.docx` | DOCX |

## Data

| File | Content |
|---|---|
| `data/v05_verdict.json` | committed verdict of the campaign |
| `data/` | campaign artifacts |

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

**Power error law measured; L→∞ convergence is an estimate**

---

*AB Research Program v1.1.0 · V05 · The Controlled Limit L → ∞*

<div align="center">

<img src="../../../../../assets/svg/divider-magenta.svg" alt="—" width="100%" height="12"/>
<sub>⚡ Part of <a href="../../../../../README.md">AB-Cloud Research</a> — numbers are verbatim from the unified registry; no result on this page is a claim about the Riemann hypothesis · <a href="../../README.md">⬆ parent section</a></sub>

</div>
