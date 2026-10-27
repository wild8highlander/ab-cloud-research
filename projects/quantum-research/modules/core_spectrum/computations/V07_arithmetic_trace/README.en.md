<!-- AB-ENRICHED:v1 · sub -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venice&height=48&color=0:ff2ec4,100:05060f&section=header" alt="" width="100%"/>

**🧭 [⬆ V07_arithmetic_trace/](README.md) · [🏠 Root README](../../../../../README.md)**

</div>
# V7 · The Arithmetic Trace Formula (Th6)

![version](https://img.shields.io/badge/version-1.2.0-298bbc) ![](https://img.shields.io/badge/series-V01--V19-3b4f58) ![](https://img.shields.io/badge/status-honest-3a6b4f)

> **Does the prime weight live in the heat trace? Guinand–Weil for H_ξ with a controlled remainder.**

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

Does the prime weight live in the heat trace? Guinand–Weil for H_ξ with a controlled remainder.

## Results

| Quantity | Value | Status |
|---|---|---|
| Campaign | V07 (plan Solution 7) | committed verdict |
| Key numbers | \|ΔQ\| ≤ 4.6e-8; \|ΔK\| ≤ 6.9e-6; B + C₀ = 2.5e-10; PC0 r = +0.9996 (resid 0.027); gates: resid ≥ 0.115, best (Nv = 16, the working window) r_EF = 0.993 — a 0.63-order gap by residual (the conservative branch of the convergence ladder). | measured/proved |
| Verdict note | the prime weight Λ(n)/√n provably lives in the heat trace of H_ξ (Th6: \|ΔK\| ≤ 5e-5); the trace branch of the gates is conservative (v2.0.8): the best gate of the battery (Nv = 16) reaches r_EF = 0.993 with an 11.5% residual against 2.7% for the zero reference (≈0.63 orders — the finite-size branch of the convergence ladder); on average the family sits in the zero clouds (0.76 ± 0.24) | honest |

## Method

rpbridge/arithmetic_trace.py + traceformula.py: the Hadamard product → Q(a) → the sine transform; Λ-sieve to 2·10⁶; PC0.

## Figures

| File | Where |
|---|---|
| `fig07_en.png` | 600 dpi — `../../figures_hires/en/`; infographics — `figures/en/` |

## Monographs

| File | Format |
|---|---|
| `monograph_en.pdf` | PDF |
| `monograph_en.docx` | DOCX |

## Data

| File | Content |
|---|---|
| `data/v07_verdict.json` | committed verdict of the campaign |
| `data/` | campaign artifacts |

## Reproduction

```bash
python3 campaigns/run_v07_*.py        # verdict tour (seconds)
python3 scripts/compute_all.py v07     # fresh recomputation
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

**Th6 proved and verified; prime weight in H_ξ, not gates**

---

*AB Research Program v1.1.0 · V07 · The Arithmetic Trace Formula (Th6)*

<div align="center">

<img src="../../../../../assets/svg/divider-magenta.svg" alt="—" width="100%" height="12"/>
<sub>⚡ Part of <a href="../../../../../README.md">AB-Cloud Research</a> — numbers are verbatim from the unified registry; no result on this page is a claim about the Riemann hypothesis · <a href="README.md">⬆ parent section</a></sub>

</div>
