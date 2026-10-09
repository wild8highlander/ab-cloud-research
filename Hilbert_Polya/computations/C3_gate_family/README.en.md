# C3 · The H7 gate family

![version](https://img.shields.io/badge/version-1.0.0-298bbc) ![](https://img.shields.io/badge/series-C1--C8-3b4f58) ![](https://img.shields.io/badge/statuses-honest-3a6b4f)

> **52 gates (Nv × q × W × α) on a 24×24 lattice with π flux; the spectral-identity question H2; permutation nulls; positive controls PC1/PC2; verdict: no identity, a 9–10 order gap.**

[← Back to the main README](../../README.md)

## Contents

1. [The campaign question](#the-campaign-question)
2. [Results](#results)
3. [Method](#method)
4. [Figures](#figures)
5. [Monographs](#monographs)
6. [Data](#data)
7. [Reproduction](#reproduction)
8. [Honest notes](#honest notes)
9. [Verdict](#verdict)

---

## The campaign question

Does a gate exist — a vortex-cloud configuration — whose spectrum is identical to the zeta zero spectrum under the correspondence level n ↔ zero n? Spectral identity is stronger than a statistics match: it requires correlation +1 between the unfolded sequences. The campaign builds null distributions (zero-list shifts, GUE matrices) and two positive controls on which the method must see identity: the spinor64 isospectral twins and the Z_id graph against the file.

## Results

| Quantity | Value | Status |
|---|---|---|
| Family | 52 unique configurations, master seed 96 | protocol C3 |
| Best r_H7 | 0.226 (p = 0.169, Bonferroni 0.80) | no identity |
| Decoys / GUE null | 0.026±0.140 / −0.014±0.127 | null zones |
| PC1 spinor64 twins | r = 1.000000000, D_nn = 2.7e-14 | method sees identity |
| PC2 graph ↔ file | r = 1.000000000000, D_nn = 1.2e-10 | method sees identity |
| Graph ↔ operator gap | 9–10 orders in D_nn | the series scale |

## Method

The pipeline: vortex configuration (cell centres, neutral charges) → Hermitian Hamiltonian (engine/hamiltonian.py) → eigvalsh → central band 0.6 (344 levels) → degree-6 polynomial unfolding → 200-level window. The zero side is the smooth Riemann–von Mangoldt count. Statistics: r_H7 (ramps removed), D_nn with a shift optimum, KS_sp. The ⟨r⟩ = 0.32 clustering of the clean lattice is a localization effect, not kinship with ζ.

## Figures

| File | Where |
|---|---|
| `fig05_gates_en.png` | 600 dpi — `figures_hires/en/fig05_gates_en.png`; экран — `figures/en/` |

## Monographs

`monograph_ru.docx` · `monograph_ru.pdf` · `monograph_en.docx` · `monograph_en.pdf`

Полная монография этого вычисления (постановка, теоремы, таблицы, рисунки,
честные ограничения): 7–9 страниц, один и тот же контент на двух языках.

## Data

| Файл | Содержание |
|---|---|
| `data/results.json` | закоммиченный вердикт кампании |
| `data/` (npz/csv) | кривые и таблицы |
| `../data/c3_*.json` | дубликат вердикта в общем реестре |

## Reproduction

```bash
# экскурсия по вердикту (~секунды, файл нулей не нужен)
python3 campaigns/run_c3_gates.py
```

Сид серии — 96; потоки RNG фиксированы (engine/hamiltonian.py). Все
зависимости — в `requirements.txt`.

## Honest notes

> H2 is a negative verdict, but the method earned it only after the positive controls: PC1/PC2 show the pipeline sees identity at the 1e-14 level when it exists.
> The term gate is a construct of this series; it denotes a parametrised family of Hermitian Hamiltonians, not a physical device.

## Verdict

**{'ru': 'Г2 — НЕТ (тождества нет), измерено с PC1/PC2', 'en': 'H2 — NO (no identity), measured with PC1/PC2'}** — подробности: `data/results.json`, монография, и
`independent_verification/` (IVP-проверки этой кампании).

---
*Hilbert Polya Bridge v1.0.0 · C3 · The H7 gate family*
