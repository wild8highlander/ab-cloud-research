# Функция V7 · Арифметическая формула следа (Th6)

![version](https://img.shields.io/badge/version-1.2.0-298bbc) ![](https://img.shields.io/badge/series-V01--V19-3b4f58) ![](https://img.shields.io/badge/status-honest-3a6b4f)

> **Живёт ли вес простых в тепловом следе? Гуинанд–Вейль для H_ξ с контролируемым остатком.**

[← Back to the main README](../../README.ru.md)

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

Живёт ли вес простых в тепловом следе? Гуинанд–Вейль для H_ξ с контролируемым остатком.

## Results

| Quantity | Value | Status |
|---|---|---|
| Campaign | V07 (plan Solution 7) | committed verdict |
| Key numbers | |ΔQ| ≤ 4.6e-8; |ΔK| ≤ 6.9e-6; B + C₀ = 2.5e-10; PC0 r = +0.9996 (resid 0.027); затворы: resid ≥ 0.115, лучший (Nv = 16, рабочее окно) r_EF = 0.993 — разрыв 0.63 порядка по невязке (консервативная ветвь лестницы сходимости). | measured/proved |
| Verdict note | вес простых Λ(n)/√n доказательно живёт в тепловом следе H_ξ (Th6: |ΔK| ≤ 5e-5); следовая ветвь затворов консервативна (v2.0.8): лучший затвор батареи (Nv = 16) достигает r_EF = 0.993 при невязке 11.5% против 2.7% у эталона нулей (≈0.63 порядка — конечноразмерная ветвь лестницы сходимости); семейство в среднем — в нулевых облаках (0.76 ± 0.24) | honest |

## Method

rpbridge/arithmetic_trace.py + traceformula.py: произведение Адамара → Q(a) → синус-преобразование; решето Λ до 2·10⁶; PC0.

## Figures

| File | Where |
|---|---|
| `fig07_ru.png` | 600 dpi — `figures_hires/ru/`; infographics — `figures/ru/` |

## Monographs

| File | Format |
|---|---|
| `monograph_ru.pdf` | PDF |
| `monograph_ru.docx` | DOCX |

## Data

| File | Content |
|---|---|
| `data/v07_verdict.json` | committed verdict of the campaign |
| `computations/V07_arithmetic_trace/data/` | campaign artifacts |

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

**{'ru': 'Th6 доказана и верифицирована; вес простых — в H_ξ, не в затворах', 'en': 'Th6 proved and verified; prime weight in H_ξ, not gates'}**

---

*AB Research Program v1.1.0 · V07 · Арифметическая формула следа (Th6)*
