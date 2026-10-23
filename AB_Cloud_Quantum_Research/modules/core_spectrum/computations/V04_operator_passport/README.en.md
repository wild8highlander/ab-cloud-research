<!-- AB-ENRICHED:v1 · sub -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venice&height=48&color=0:ff2ec4,100:05060f&section=header" alt="" width="100%"/>

**🧭 [⬆ V04_operator_passport/](README.md) · [🏠 Root README](../../../../../README.md)**

</div>
# V4 · Operator Passport (Th1)

![version](https://img.shields.io/badge/version-1.2.0-298bbc) ![](https://img.shields.io/badge/series-V01--V19-3b4f58) ![](https://img.shields.io/badge/status-honest-3a6b4f)

> **Is the operator strictly defined and what is proved about it? Passport P1–P4.**

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

Is the operator strictly defined and what is proved about it? Passport P1–P4.

## Results

| Quantity | Value | Status |
|---|---|---|
| Campaign | V04 (plan Solution 4) | committed verdict |
| Key numbers | ‖H−H†‖ = 0 (exact); ‖Hv−λv‖ = 8.8e-15; pairing λ↔−λ (W=0) 8.2e-15. Th1 proved. | measured/proved |
| Verdict note | Th1 is proved: hermiticity by construction, the spectrum is real, chirality α=½/W=0 — bipartiteness | honest |

## Method

rpbridge/operator.py: explicit element formulas, battery L ∈ {12,16,24,32} × handles; hermiticity/residuals/chirality.

## Figures

| File | Where |
|---|---|
| `fig04_en.png` | 600 dpi — `../../figures_hires/en/`; infographics — `figures/en/` |

## Monographs

| File | Format |
|---|---|
| `monograph_en.pdf` | PDF |
| `monograph_en.docx` | DOCX |

## Data

| File | Content |
|---|---|
| `data/v04_verdict.json` | committed verdict of the campaign |
| `data/` | campaign artifacts |

## Reproduction

```bash
python3 campaigns/run_v04_*.py        # verdict tour (seconds)
python3 scripts/compute_all.py v04     # fresh recomputation
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

**Th1: hermiticity and reality — proved**

---

*AB Research Program v1.1.0 · V04 · Operator Passport (Th1)*

<div align="center">

<img src="../../../../../assets/svg/divider-magenta.svg" alt="—" width="100%" height="12"/>
<sub>⚡ Part of <a href="../../../../../README.md">AB-Cloud Research</a> — numbers are verbatim from the unified registry; no result on this page is a claim about the Riemann hypothesis · <a href="README.md">⬆ parent section</a></sub>

</div>
