# C1 · The identity function and the Γ-ladder

![version](https://img.shields.io/badge/version-1.0.0-298bbc) ![](https://img.shields.io/badge/series-C1--C8-3b4f58) ![](https://img.shields.io/badge/statuses-honest-3a6b4f)

> **Assembling the identity function Z_id(t) = e^{iθ(t)}ζ(½+it) from the algebraic closures of the Γ-frame; criteria K1–K4, K7; one honest refutation — the single modulus on the line is not elementary.**

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

Can one assemble, on the critical line, a function whose zeros coincide with those of ζ without using any zero data — only elementary identities of the Γ-frame and ζ itself? This campaign answers yes, and that answer is the graph of the whole series: Z_id(t) = e^{iθ(t)}ζ(½+it). But the answer fixes the boundary as well: the algebraic envelope does not generate zeros — it merely wraps ζ in a smooth phase. Whatever is true of Z_id is true by identity; whatever Z_id cannot do, no rearrangement of the phase can do either.

## Results

| Quantity | Value | Status |
|---|---|---|
| Closure |Γ(½+iu)|² = π/cosh πu | residual 2.59e-39 (dps 40) | proven |
| Closure |Γ(iu)|² = π/(u·sinh πu) | residual 2.57e-39 | proven |
| Product |Γ(¼+iu)|·|Γ(¾+iu)| (Legendre) | residual 1.27e-39 | proven |
| Candidate form of the single modulus | structural mismatch 0.765 | refuted |
| Reality of Z_id (K2) | max|Im Z_id| = 4.9e-29 | proven |
| Z_id zeros on [0,200] vs mpmath (K3) | 79 zeros, max|Δγ| = 2.8e-14 | confirmed |
| Gram points (K7) | 220 points, 4 violations (classical) | reproduced |

## Method

The campaign core is hpbridge/identity.py: θ(t) via Im ln Γ(¼+it/2), the Z_id assembly in two arithmetics (float64 and mpmath dps 25–40), zero bisection on sign changes with 80 refinement steps, Gram points via findroot. The Γ-closures are verified on a 401-point grid at dps = 40 against the 1e-30 threshold. The whole campaign is deterministic and runs in about two seconds.

## Figures

| File | Where |
|---|---|
| `fig01_zid_en.png` | 600 dpi — `figures_hires/en/fig01_zid_en.png`; экран — `figures/en/` |
| `fig02_gamma_ladder_en.png` | 600 dpi — `figures_hires/en/fig02_gamma_ladder_en.png`; экран — `figures/en/` |

## Monographs

`monograph_ru.docx` · `monograph_ru.pdf` · `monograph_en.docx` · `monograph_en.pdf`

Полная монография этого вычисления (постановка, теоремы, таблицы, рисунки,
честные ограничения): 7–9 страниц, один и тот же контент на двух языках.

## Data

| Файл | Содержание |
|---|---|
| `data/results.json` | закоммиченный вердикт кампании |
| `data/` (npz/csv) | кривые и таблицы |
| `../data/c1_*.json` | дубликат вердикта в общем реестре |

## Reproduction

```bash
# экскурсия по вердикту (~секунды, файл нулей не нужен)
python3 campaigns/run_c1_identity.py
```

Сид серии — 96; потоки RNG фиксированы (engine/hamiltonian.py). Все
зависимости — в `requirements.txt`.

## Honest notes

> Terminological hygiene: Riemann relations in neighbouring projects refers to bilinear relations for period matrices, not to the Riemann Hypothesis. The series keeps the two subjects strictly apart.
> The K1 refutation is not a defeat but a calibration: the ladder closes elementarily only at the strip edges and through the Legendre pair product — exactly the product that enters the phase θ(t).

## Verdict

**{'ru': 'композитный вердикт K1–K4, K7: PASS (одно опровержение опубликовано)', 'en': 'composite verdict K1–K4, K7: PASS (one refutation published)'}** — подробности: `data/results.json`, монография, и
`independent_verification/` (IVP-проверки этой кампании).

---
*Hilbert Polya Bridge v1.0.0 · C1 · The identity function and the Γ-ladder*
