# Функция V10 · Обратная задача

![version](https://img.shields.io/badge/version-1.2.0-298bbc) ![](https://img.shields.io/badge/series-V01--V19-3b4f58) ![](https://img.shields.io/badge/status-honest-3a6b4f)

> **Восстанавливается ли арифметика из спектра? Следы степеней, матрица чувствительности, оптимизация.**

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

Восстанавливается ли арифметика из спектра? Следы степеней, матрица чувствительности, оптимизация.

## Results

| Quantity | Value | Status |
|---|---|---|
| Campaign | V10 (plan Solution 10) | committed verdict |
| Key numbers | rank J = 6 (k=6), cond ≈ 8.7e4; восстановление |Δq| = 0.077; разделение 1.6–3.5; идентифицируемость rank-limited. | measured/proved |
| Verdict note | часть арифметики (заряды) идентифицируема по старшим следам при достаточном k; ранг J < n_params ⇒ полная идентифицируемость позиций недостижима по инвариантам этого класса — измерено | honest |

## Method

rpbridge/inverse.py: Φ = (Tr H, …, Tr H⁶); J численно; Нелдер–Мид с 3 стартов; разделение арифметика/случай.

## Figures

| File | Where |
|---|---|
| `fig10_ru.png` | 600 dpi — `figures_hires/ru/`; infographics — `figures/ru/` |

## Monographs

| File | Format |
|---|---|
| `monograph_ru.pdf` | PDF |
| `monograph_ru.docx` | DOCX |

## Data

| File | Content |
|---|---|
| `data/v10_verdict.json` | committed verdict of the campaign |
| `computations/V10_inverse_problem/data/` | campaign artifacts |

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

**{'ru': 'Часть арифметики неидентифицируема по инвариантам (ранг-лимит)', 'en': 'Part of the arithmetic is unidentifiable (rank-limited)'}**

---

*AB Research Program v1.1.0 · V10 · Обратная задача*
