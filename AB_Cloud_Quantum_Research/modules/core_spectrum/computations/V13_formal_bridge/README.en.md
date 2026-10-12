# V13 · The Formal Bridge

![version](https://img.shields.io/badge/version-1.2.0-298bbc) ![](https://img.shields.io/badge/series-V01--V19-3b4f58) ![](https://img.shields.io/badge/status-honest-3a6b4f)

> **Is the RH conclusion formally blocked? The obligation DAG and the status machine.**

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

Is the RH conclusion formally blocked? The obligation DAG and the status machine.

## Results

| Quantity | Value | Status |
|---|---|---|
| Campaign | V13 (plan Solution 13) | committed verdict |
| Key numbers | RH: blocked; 7 blockers (4 assumed, 3 computed); proven 5/12; the DAG is valid. | measured/proved |
| Verdict note | формальная машина БЛОКИРУЕТ вывод RH: путь к заключению содержит гипотезы O08/O09/O11/O12; ни одна численная проверка не повышает статус | honest |

## Method

rpbridge/formaloblig.py: 12 nodes proven/computed/assumed; acyclicity; blocking of the path O01→O12; formal/ (Lean/Coq/Agda/Isabelle).

## Figures

| File | Where |
|---|---|
| `fig13_en.png` | 600 dpi — `figures_hires/en/`; infographics — `figures/en/` |

## Monographs

| File | Format |
|---|---|
| `monograph_en.pdf` | PDF |
| `monograph_en.docx` | DOCX |

## Data

| File | Content |
|---|---|
| `data/v13_verdict.json` | committed verdict of the campaign |
| `computations/V13_formal_bridge/data/` | campaign artifacts |

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

**{'ru': 'RH заблокирована честно', 'en': 'The RH conclusion is blocked honestly and automatically'}**

---

*AB Research Program v1.1.0 · V13 · The Formal Bridge*
