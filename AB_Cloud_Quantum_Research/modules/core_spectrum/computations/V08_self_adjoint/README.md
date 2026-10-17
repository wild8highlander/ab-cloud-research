# V8 · Self-Adjointness (Th2)

![version](https://img.shields.io/badge/version-1.2.0-298bbc) ![](https://img.shields.io/badge/series-V01--V19-3b4f58) ![](https://img.shields.io/badge/status-honest-3a6b4f)

> **Is the operator self-adjoint and stable under boundary changes? Defect indices, the BC family, unitarity.**

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

Is the operator self-adjoint and stable under boundary changes? Defect indices, the BC family, unitarity.

## Results

| Quantity | Value | Status |
|---|---|---|
| Campaign | V08 (plan Solution 8) | committed verdict |
| Key numbers | Defects (0,0) at L = 12/16/24; drift 2.2e-16; BC shifts 0.21–0.27; the L→∞ limit is open (O03). | measured/proved |
| Verdict note | Th2 is proved for finite dimension; the stability of the limit model under BC changes is a measurement: the shifts are finite and decrease with L; the existence of a self-adjoint limit operator is open | honest |

## Method

rpbridge/selfadjoint.py: σ_min(H ∓ iI); BC open/torus/twists; unitarity e^{−iHt}; Im⟨ψ,Hψ⟩.

## Figures

| File | Where |
|---|---|
| `fig08_ru.png` | 600 dpi — `../../figures_hires/ru/`; infographics — `figures/ru/` |

## Monographs

| File | Format |
|---|---|
| `monograph_ru.pdf` | PDF |
| `monograph_ru.docx` | DOCX |

## Data

| File | Content |
|---|---|
| `data/v08_verdict.json` | committed verdict of the campaign |
| `data/` | campaign artifacts |

## Reproduction

```bash
python3 campaigns/run_v08_*.py        # verdict tour (seconds)
python3 scripts/compute_all.py v08     # fresh recomputation
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

**Th2 proved (finite-dim); the limit part is open**

---

*AB Research Program v1.1.0 · V08 · Self-Adjointness (Th2)*
