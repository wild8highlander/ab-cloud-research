# V19 · Branch Stitching of the Algebraic Function

![version](https://img.shields.io/badge/version-1.2.0-298bbc) ![](https://img.shields.io/badge/series-V01--V19-3b4f58) ![](https://img.shields.io/badge/status-honest-3a6b4f)

> **How to stitch the branches of the full algebraic function of the critical line? The hodge-laboratory mechanism: monodromic sheet gluing and the exact phase law ζ^{ra+sb}.**

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

How to stitch the branches of the full algebraic function of the critical line? The hodge-laboratory mechanism: monodromic sheet gluing and the exact phase law ζ^{ra+sb}.

## Results

| Quantity | Value | Status |
|---|---|---|
| Campaign | V19 (plan Solution 19) | committed verdict |
| Key numbers | Phase law 1.3e-40; orthogonality 225/5.1e-30; alternation 1999/1999; closure 138=138 (dev 5.0e-10); θ ladder 0.832; coherence 0.9995 (z = 43.4); flagship 4.5e-40. | measured/proved |
| Verdict note | ALGEBRAIC_CERTIFICATE: the Γ-phase carries both signatures | honest |

## Method

rpbridge/stitching.py, four layers: A — the reference (the Fermat cover, tanh-sinh along the smooth parametrization t = w^N/(w^N+(1−w)^N)); B — the Z₂ monodromy of Z_id (sign alternation, the argument closure); C — the stitched object (the Γ-phase: the θ ladder + sign coherence); D — the R1/R2/R4 regression.

## Figures

| File | Where |
|---|---|
| `fig20_ru.png` | 600 dpi — `../../figures_hires/ru/`; infographics — `figures/ru/` |

## Monographs

| File | Format |
|---|---|
| `monograph_ru.pdf` | PDF |
| `monograph_ru.docx` | DOCX |

## Data

| File | Content |
|---|---|
| `data/results.json` | committed verdict of the campaign |
| `data/` | campaign artifacts |

## Reproduction

```bash
python3 campaigns/run_v19_*.py        # verdict tour (seconds)
python3 scripts/compute_all.py v19     # fresh recomputation
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

**ALGEBRAIC_CERTIFICATE: all exact layers closed, the Γ-phase carries both signatures**

---

*AB Research Program v1.1.0 · V19 · Branch Stitching of the Algebraic Function*
