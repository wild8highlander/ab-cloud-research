# V15 · The Li Criterion (Th4)

![version](https://img.shields.io/badge/version-1.2.0-298bbc) ![](https://img.shields.io/badge/series-V01--V19-3b4f58) ![](https://img.shields.io/badge/status-honest-3a6b4f)

> **Are the Li coefficients connected to the spectrum? The spectral formula λ_n = Tr g_n(H_ξ) and certified positivity.**

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

Are the Li coefficients connected to the spectrum? The spectral formula λ_n = Tr g_n(H_ξ) and certified positivity.

## Results

| Quantity | Value | Status |
|---|---|---|
| Campaign | V15 (plan Solution 15) | committed verdict |
| Key numbers | Th4 |Δ| = 4.4e-11; λ₁ = 0.023057 (−B = 0.023096); λ_n > 0 for n ≤ 3000 (tails ≤ 0.115); the gate bridge — O09. | measured/proved |
| Verdict note | Th4 доказана и верифицирована (два пути, |Δ| ≤ 1e-9); λ_n > 0 для n ≤ 3000 измерено с сертифицированными хвостами; бесконечное семейство неравенств остаётся открытым; представление λ_n следами ЗАТВОРОВ не найдено | honest |

## Method

rpbridge/li.py: two paths (the zero series w^n and the trace of g_n); the telescope |1−w^n| ≤ n|1−w|; 50k zeros, T ≤ 40433.

## Figures

| File | Where |
|---|---|
| `fig15_en.png` | 600 dpi — `figures_hires/en/`; infographics — `figures/en/` |

## Monographs

| File | Format |
|---|---|
| `monograph_en.pdf` | PDF |
| `monograph_en.docx` | DOCX |

## Data

| File | Content |
|---|---|
| `data/v15_verdict.json` | committed verdict of the campaign |
| `computations/V15_li_criterion/data/` | campaign artifacts |

## Reproduction

```bash
python3 campaigns/run_v15_*.py        # verdict tour (seconds)
python3 scripts/compute_all.py v15     # fresh recomputation
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

**{'ru': 'Th4 доказана', 'en': 'Th4 proved; λ_n > 0 to 3000 measured; RH does not follow'}**

---

*AB Research Program v1.1.0 · V15 · The Li Criterion (Th4)*
