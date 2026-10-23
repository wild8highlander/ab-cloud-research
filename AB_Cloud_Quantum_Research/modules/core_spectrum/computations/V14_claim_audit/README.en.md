<!-- AB-ENRICHED:v1 · sub -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venice&height=48&color=0:ff2ec4,100:05060f&section=header" alt="" width="100%"/>

**🧭 [⬆ V14_claim_audit/](README.md) · [🏠 Root README](../../../../../README.md)**

</div>
# V14 · Claim Audit

![version](https://img.shields.io/badge/version-1.2.0-298bbc) ![](https://img.shields.io/badge/series-V01--V19-3b4f58) ![](https://img.shields.io/badge/status-honest-3a6b4f)

> **Is every statement traced to data and controls? The 5-part schema + auditor.**

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

Is every statement traced to data and controls? The 5-part schema + auditor.

## Results

| Quantity | Value | Status |
|---|---|---|
| Campaign | V14 (plan Solution 14) | committed verdict |
| Key numbers | 19/19 claims per the schema (V1–V19); full verdict coverage; status hygiene observed. | measured/proved |
| Verdict note | every public statement of the package is traced to a computation, a control and a list of non-implications; automatic promotion of a hypothesis to a theorem is blocked | honest |

## Method

rpbridge/audit.py: claim JSON (statement/premises/code/controls/does_not_prove); A1/A2/A3; p-values banned as proofs.

## Figures

| File | Where |
|---|---|
| `fig14_en.png` | 600 dpi — `../../figures_hires/en/`; infographics — `figures/en/` |

## Monographs

| File | Format |
|---|---|
| `monograph_en.pdf` | PDF |
| `monograph_en.docx` | DOCX |

## Data

| File | Content |
|---|---|
| `data/v14_verdict.json` | committed verdict of the campaign |
| `data/` | campaign artifacts |

## Reproduction

```bash
python3 campaigns/run_v14_*.py        # verdict tour (seconds)
python3 scripts/compute_all.py v14     # fresh recomputation
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

**Every statement is traced; automatic promotion is blocked**

---

*AB Research Program v1.1.0 · V14 · Claim Audit*

<div align="center">

<img src="../../../../../assets/svg/divider-magenta.svg" alt="—" width="100%" height="12"/>
<sub>⚡ Part of <a href="../../../../../README.md">AB-Cloud Research</a> — numbers are verbatim from the unified registry; no result on this page is a claim about the Riemann hypothesis · <a href="README.md">⬆ parent section</a></sub>

</div>
