# C4 · The trace formula: Tr e^{−uH} versus the explicit formula

![version](https://img.shields.io/badge/version-1.0.0-298bbc) ![](https://img.shields.io/badge/series-C1--C8-3b4f58) ![](https://img.shields.io/badge/statuses-honest-3a6b4f)

> **Deriving the Q(a) identity from the Hadamard product; the trace formula K(x) = (1/π)∫Q sin with the prime weight Λ(n)/√n; calibration 1.7e-12; H_ξ verified to 1.2e-5; gates in the null zone (residual gap ≈0.5 order).**

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

If a Hilbert–Pólya operator existed, its heat trace would have to carry the prime weight: Tr e^{−xH} = smooth Γ-terms − ΣΛ(n)/√n·x/(x²+ln²n). The campaign derives this rigorously (theorem T6), verifies it for the operator H_ξ = diag(±γ_n), and then measures what survives for the lattice gates. This is the third projection of the H2 gap — after the rank correlation (C3) and the ψ-ladder (C6).

## Results

| Quantity | Value | Status |
|---|---|---|
| M0: the Q(a) identity | |ΔQ| ≤ 1.7e-12 on the grid a ∈ [0.1, 3] | calibrated |
| Built-in control B = −C₀ | 0.023095708966 — 12 digits | classical identity confirmed |
| M1: trace formula for H_ξ | |ΔK| ≤ 1.2e-5 (abs), 1e-6…1e-4 rel. at x ≤ 0.35 | T6 verified |
| PC0: zeros window vs the comb | r = +0.9998, relative residual 2.1% | method sees the prime weight |
| M2: 52 gates | r_EF −0.93…+1.00, null clouds | no prime weight |
| Gap in the trace metric | ≈ 0.5 orders by residual (best 6.7% vs 2.1%) | H2 — NO, measured |
| C3 protocol reproduction | |Δ mean_spacing| = 1.45e-16 | bit-for-bit |

## Method

Derivation: Hadamard ξ'/ξ = B + Σ_ρ[1/(s−ρ)+1/ρ] → pairing ρ ↔ ρ̄ → Q(a) = ζ'/ζ(½+a) + 1/(½+a) + 1/(a−½) − ½lnπ + ½ψ(¼+a/2) − B − C₀. Trace: 2a/(a²+γ²) = 2∫e^{−γt}sin(at)dt → K(x) = (1/π)∫Q(a)sin(ax)da. For a > ½ the series ζ'/ζ = −ΣΛ(n)/n^{½+a} — the prime part T2 is computed by the exact series transform; the smooth part T3 by closed Si/Ci forms (pole, ψ expansion, constants); the Γ-part T1 on [0, 1.5] through the spline of the mpmath grid. The gate metric: the fluctuation of the unfolded heat trace against the comb P(u) at fixed scale (scale optimisation is excluded as a source of r-inflation).

## Figures

| File | Where |
|---|---|
| `fig06_trace_en.png` | 600 dpi — `figures_hires/en/fig06_trace_en.png`; экран — `figures/en/` |
| `fig07_parts_en.png` | 600 dpi — `figures_hires/en/fig07_parts_en.png`; экран — `figures/en/` |
| `fig08_rEF_en.png` | 600 dpi — `figures_hires/en/fig08_rEF_en.png`; экран — `figures/en/` |

## Monographs

`monograph_ru.docx` · `monograph_ru.pdf` · `monograph_en.docx` · `monograph_en.pdf`

Полная монография этого вычисления (постановка, теоремы, таблицы, рисунки,
честные ограничения): 7–9 страниц, один и тот же контент на двух языках.

## Data

| Файл | Содержание |
|---|---|
| `data/results.json` | закоммиченный вердикт кампании |
| `data/` (npz/csv) | кривые и таблицы |
| `../data/c4_*.json` | дубликат вердикта в общем реестре |

## Reproduction

```bash
# экскурсия по вердикту (~секунды, файл нулей не нужен)
python3 campaigns/run_c4_trace_formula.py
```

Сид серии — 96; потоки RNG фиксированы (engine/hamiltonian.py). Все
зависимости — в `requirements.txt`.

## Honest notes

> The 1.2e-5 floor is the quadrature floor, not the precision limit of the identity: for x ≥ 1 the value of K(x) itself is ~1e-6 and the relative metric loses meaning; in the informative range the agreement is 1e-6…1e-4.
> The zero file is needed only for fresh recomputations; the committed verdict is self-contained.

## Verdict

**{'ru': 'T6 верифицирована; разрыв Г2 ≈ 1 порядок в тепловой метрике', 'en': 'T6 verified; the H2 gap ≈ 1 order in the trace metric'}** — подробности: `data/results.json`, монография, и
`independent_verification/` (IVP-проверки этой кампании).

---
*Hilbert Polya Bridge v1.0.0 · C4 · The trace formula: Tr e^{−uH} versus the explicit formula*
