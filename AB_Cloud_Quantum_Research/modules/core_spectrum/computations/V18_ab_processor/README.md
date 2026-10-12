# Функция V18 · AB-оператор как процессор

![version](https://img.shields.io/badge/version-1.2.0-298bbc) ![](https://img.shields.io/badge/series-V01--V19-3b4f58) ![](https://img.shields.io/badge/status-honest-3a6b4f)

> **Работает ли AB-оператор как процессор — ворота, зацепление, игра? Три уровня вычислительности на строительных блоках гамильтониана.**

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

Работает ли AB-оператор как процессор — ворота, зацепление, игра? Три уровня вычислительности на строительных блоках гамильтониана.

## Results

| Quantity | Value | Status |
|---|---|---|
| Campaign | V18 (plan Solution 18) | committed verdict |
| Key numbers | Верность всех шести ворот 1.0 − 2e-16; concurrence 0.984 (t = 2.373); партия AB-Pong: счёт 0:1, 10 перехватов, 411 событий, повтор бит-в-бит. | measured/proved |
| Verdict note | Процессор — ДА: ворота точные, зацепление почти-Белл, игра исполняется детерминированно | honest |

## Method

rpbridge/processor.py: P1 — аналитические импульсы {X,Y,Z,H,S,T} на блоке H₂ = mσz − t·cosφ·σx − t·sinφ·σy; P2 — обменная связка −J, concurrence Вуттерса; P3 — AB-Pong: доска 64 с фазой π/3, калибровочно-ковариантные зеркала e^{−2iφx}ψ(2p−x), ИИ с опережением, голы на x≤5/x≥58.

## Figures

| File | Where |
|---|---|
| `fig19_ru.png` | 600 dpi — `figures_hires/ru/`; infographics — `figures/ru/` |

## Monographs

| File | Format |
|---|---|
| `monograph_ru.pdf` | PDF |
| `monograph_ru.docx` | DOCX |

## Data

| File | Content |
|---|---|
| `data/v18_verdict.json` | committed verdict of the campaign |
| `computations/V18_ab_processor/data/` | campaign artifacts |

## Reproduction

```bash
python3 campaigns/run_v18_*.py        # verdict tour (seconds)
python3 scripts/compute_all.py v18     # fresh recomputation
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

**{'ru': 'Процессор — ДА: ворота точные, зацепление почти-Белл, игра исполняется детерминированно', 'en': 'Processor — YES: exact gates, near-Bell entanglement, the game runs deterministically'}**

---

*AB Research Program v1.1.0 · V18 · AB-оператор как процессор*
