# Функция V14 · Аудит утверждений

![version](https://img.shields.io/badge/version-1.2.0-298bbc) ![](https://img.shields.io/badge/series-V01--V19-3b4f58) ![](https://img.shields.io/badge/status-honest-3a6b4f)

> **Трассируется ли каждое утверждение к данным и контроля? Схема из 5 частей + аудитор.**

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

Трассируется ли каждое утверждение к данным и контроля? Схема из 5 частей + аудитор.

## Results

| Quantity | Value | Status |
|---|---|---|
| Campaign | V14 (plan Solution 14) | committed verdict |
| Key numbers | 19/19 claims по схеме (V1–V19); покрытие вердиктов полное; статус-гигиена соблюдена. | measured/proved |
| Verdict note | каждое публичное утверждение пакета трассируется к вычислению, контролю и перечню не-следствий; автоповышение гипотезы до теоремы заблокировано | honest |

## Method

rpbridge/audit.py: claim-JSON (statement/premises/code/controls/does_not_prove); A1/A2/A3; запрет p-значений в роли доказательств.

## Figures

| File | Where |
|---|---|
| `fig14_ru.png` | 600 dpi — `figures_hires/ru/`; infographics — `figures/ru/` |

## Monographs

| File | Format |
|---|---|
| `monograph_ru.pdf` | PDF |
| `monograph_ru.docx` | DOCX |

## Data

| File | Content |
|---|---|
| `data/v14_verdict.json` | committed verdict of the campaign |
| `computations/V14_claim_audit/data/` | campaign artifacts |

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

**{'ru': 'Каждое утверждение трассируется; автоповышение статуса заблокировано', 'en': 'Every statement is traced; automatic promotion is blocked'}**

---

*AB Research Program v1.1.0 · V14 · Аудит утверждений*
