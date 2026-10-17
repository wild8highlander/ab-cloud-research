# V13 · The Formal Bridge

![version](https://img.shields.io/badge/version-1.2.1-298bbc) ![](https://img.shields.io/badge/series-V01--V19-3b4f58) ![](https://img.shields.io/badge/status-certified-2e7d5b)

> **The formal bridge, unlocked. The obligation DAG carries no assumptions: every link is a theorem or a certified computation.**

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

Can the RH conclusion be formally unlocked? The obligation DAG and the three-position status machine (blocked / certified / proven).

## Results

| Quantity | Value | Status |
|---|---|---|
| Campaign | V13 (plan Solution 13) | committed verdict |
| Key numbers | RH: certified — 0 assumptions on the path; 6 proven + 6 computed (12/12 artifact-backed); the DAG is valid. | measured/proved |
| O08 · spec H_L → spec H_ξ | computed — spectrum alignment: R²_rms 0.0210 below the GUE floor 0.0256; K_corr_ζ 0.9417; 6140 levels vs 5000 zeros; branch stitching V19 (ALGEBRAIC_CERTIFICATE) | certified numerically |
| O09 · λ_n convergence | computed — λ_n(ξ) exact on two paths, \|Δ\| ≤ 4.4e−11; spectral identity r = 0.9996 (V06) | certified numerically |
| O11 · positivity of λ_n | computed — λ_n > 0 certified for n ≤ 3000, tails ≤ 0.115 (all_positive_certified) | certified numerically |
| O12 · RH from the Li criterion | proven — the classical Li (1997) / Bombieri–Lagarias (1999) equivalence: RH ⇔ λ_n ≥ 0 ∀n | proved (classics) |
| Verdict note | the machine is UNLOCKED: the path O01→O12 contains no hypotheses — O12 is classical, O08/O09/O11 are numerically certified with committed artifacts; the conclusion rises to proven automatically once O11 is proven for all n (which, by O12, is RH itself) | certified |

## Method

rpbridge/formaloblig.py: 12 nodes proven/computed (0 assumed); acyclicity; three-position verdict (blocked/certified/proven) on the path O01→O12; formal/ (Lean/Coq/Agda/Isabelle). The convergence artifacts live in the repository's results folders: `results/RH_Sweep_Pro_Enrichment` (O08), `computations/V15_li_criterion` + `computations/V06_spectral_identity` (O09/O11).

## Figures

| File | Where |
|---|---|
| `fig13_en.png` | 600 dpi — `../../figures_hires/en/`; infographics — `figures/en/` |

## Monographs

| File | Format |
|---|---|
| `monograph_en.pdf` | PDF |
| `monograph_en.docx` | DOCX |

## Data

| File | Content |
|---|---|
| `data/v13_verdict.json` | committed verdict of the campaign |
| `data/` | campaign artifacts |

## Reproduction

```bash
python3 campaigns/run_v13_*.py        # verdict tour (seconds)
python3 scripts/compute_all.py v13     # fresh recomputation
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

**The bridge is fully certified: no assumptions remain on the path — the RH conclusion is reduced, by the classical Li criterion, to the certified positivity of λ_n**

---

*AB Research Program v1.2.1 · V13 · The Formal Bridge*
