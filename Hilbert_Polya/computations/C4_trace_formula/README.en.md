# C4 · The trace formula: Tr e^{−uH} versus the explicit formula

![version](https://img.shields.io/badge/version-1.0.0-298bbc) ![](https://img.shields.io/badge/series-C1--C8-3b4f58) ![](https://img.shields.io/badge/statuses-honest-3a6b4f)

<p align="center"><img src="../../assets/illustrations/ill_spectrum_emerge.png" width="720" alt="A discrete spectrum emerging into a continuous curve: the heat trace of H_ξ as the bridge between zeta zeros and the prime comb"/></p>

<p align="center"><img src="../../assets/avatars/hp_cast_strip.svg" width="860" alt="Bridge avatar cast"/></p>

*Curated by the Bridge avatar cast — Agent Atlas directed, Agent Lyra traced the heat kernel, Agent Vera verified T6.*

> **Deriving the Q(a) identity from the Hadamard product; the trace formula K(x) = (1/π)∫Q sin with the prime weight Λ(n)/√n; calibration 1.7e-12; H_ξ verified to 1.2e-5; gates in the null zone (residual gap ≈0.5 order).**

[← Back to the main README](../../README.md)

This is the **international quick-reference edition** of campaign C4: a ten-minute tour of the trace-formula campaign, written to be read top to bottom. The deep, definitive guide — with the full method narrative, per-row result commentary and expanded interpretation — is [README.md](README.md) in this folder. Every number, table, file name and command below is preserved exactly as committed.

## Contents

1. C4 in five numbers
2. The question
3. The two sides in one screen: explicit formula ↔ trace formula
4. H_ξ in one paragraph: identity by construction
5. The derivation in four steps
6. B = −C₀: the control that keeps the derivation honest
7. The gates at fixed scale
8. Results
9. Honest notes
10. How to read the numbers
11. Interpretation: proves / does not prove
12. Reproduction
13. Data and figures
14. Verdict
15. FAQ
16. Mini-glossary
17. A five-minute tour of the explicit formula
18. See also

---

## 1. C4 in five numbers

| # | Number | One-line meaning |
|---|---|---|
| 1 | \|ΔQ\| ≤ 1.7e-12 | the Q(a) identity, derived from the Hadamard product, is calibrated on a ∈ [0.1, 3] |
| 2 | \|ΔK\| ≤ 1.2e-5 | the trace formula holds for H_ξ — theorem T6 verified against the direct spectral sum |
| 3 | r = +0.9998, residual 2.1% | positive control PC0: the method sees the prime weight where it must |
| 4 | r_EF −0.93…+1.00, 52 gates | the lattice gates sit in the null clouds — no prime weight |
| 5 | ≈ 0.5 orders | the measured gap: best gate residual 6.7% vs the zeros' 2.1% (H2 — NO, measured) |

Everything else in this file explains where these five numbers come from, what they certify, and what they deliberately do not claim.

## 2. The question

<p align="center"><img src="../../assets/avatars/hp_riemann.svg" width="120" alt="Riemann avatar"/></p>

The Hilbert–Pólya programme asks whether the imaginary parts γ_n of the zeta zeros are the eigenvalues of a self-adjoint operator H; if so, the Riemann hypothesis follows from the reality of spectra. Rather than hunt for a candidate, campaign C4 derives a **necessary consequence** and measures it: if a Hilbert–Pólya operator existed, its heat trace would have to carry the prime weight,

    Tr e^{−xH} = smooth Γ-terms − ΣΛ(n)/√n·x/(x²+ln²n),

where Λ(n) = ln p on prime powers and 0 elsewhere. The campaign derives this rigorously (**theorem T6**), verifies it for the zero-coded operator H_ξ = diag(±γ_n), and then measures what survives for the lattice gates. This is the **third projection of the H2 gap** — after the rank correlation (C3) and the ψ-ladder (C6) — and the only one equipped with a proven positive control.

A heat trace, Tr e^{−xH} = Σ_n e^{−xλ_n}, is the Laplace transform of the spectral density: each level contributes one exponentially damped term, high levels suppressed first. That damping is the point — it smooths a discrete list of levels into a continuous curve, and curves can be matched against the continuous prime side of number theory.

## 3. The two sides in one screen: explicit formula ↔ trace formula

| | Primes side | Zeros side |
|---|---|---|
| Object | explicit formula, Weil (1952) test-function form | heat trace K(x) = Σ_{γ>0} e^{−xγ} = Tr e^{−xH_ξ} |
| Generator | ζ'/ζ(½+a) = −Σ_n Λ(n)/n^{½+a} for a > 1.5 | Q(a) = Σ_{γ>0} 2a/(a²+γ²) |
| Thermal shape | comb P(u) = Σ Λ(n)/√n · u/(u²+ln²n) | fluctuation D(u) of the unfolded heat trace |
| What it encodes | *which* numbers are prime (Λ ≠ 0 only at prime powers) | *where* the zeros sit |

The two sides are joined by the sine transform: Q(a) = 2∫₀^∞ K(x) sin(ax) dx and K(x) = (1/π)∫₀^∞ Q(a) sin(ax) da. This is the **Guinand–Weil trace formula** quoted in the title — Tr e^{−xH_ξ} = (1/π)∫₀^∞ Q(a) sin(ax) da — with the thermal test function e^{−xγ}; the Hadamard product (J. Hadamard, 1893) feeds Q(a), Guinand's transform viewpoint organizes the zero side, and the heat-kernel reading is consonant with A. Connes (1999).

The weight Λ(n)/√n is the **fingerprint of the primes**, and it is forced, not chosen: the primes enter through ζ'/ζ on the half-line a > 1.5, and integrating n^{−½−a} sin(ax) da = n^{−½}·Im[e^{−1.5(ln n − ix)}/(ln n − ix)] leaves exactly the 1/√n factor — the residue of shifting prime powers to the line Re s = ½. A spectrum whose heat-trace fluctuation tracks this comb is hearing primes; one that does not, is not. No amount of level-statistics can fake the comb, because the comb encodes arithmetic, not merely density.

## 4. H_ξ in one paragraph: identity by construction

<p align="center"><img src="../../assets/avatars/hp_hilbert.svg" width="120" alt="Hilbert avatar"/></p>

    H_ξ = diag(±γ_n)

is the diagonal, self-adjoint operator built directly **from** the zeros file (2 001 052 zeros; `zeros6.txt` in the committed verdict): its eigenvalues are ± the imaginary parts of the nontrivial zeros, the ± reflecting the conjugate symmetry of the zero set. For this one operator "spectrum = zeros" is a definition, not a conjecture — and that is precisely its role. Verifying T6 for H_ξ does not test the Riemann hypothesis; it tests the **derivation pipeline** end to end, from the Hadamard product down to the prime comb, at |ΔK| ≤ 1.2e-5. And because the pipeline is thereby certified, the zeros supply the calibrated benchmark (2.1% residual) against which the 87 gates of the package — 52 of them measured in this campaign — are judged with identical code and identical protocol. The package's theory map calls this its most precise place: clause Г5/H5 ("primes in the operator") is proven YES for H_ξ and measured NO for every gate.

## 5. The derivation in four steps

All constants derived in-project; none fitted. (Full detail: `docs/trace_formula.md`.)

**Step 1 — Hadamard product.** ξ(s) = ½s(s−1)π^{−s/2}Γ(s/2)ζ(s) is entire of order 1 with zeros exactly the nontrivial zeros ρ; its canonical product gives

    ξ'/ξ(s) = B + Σ_ρ [ 1/(s−ρ) + 1/ρ ],        B := ξ'(0)/ξ(0),

while differentiating the defining factors gives ξ'/ξ(s) = 1/s + 1/(s−1) − ½lnπ + ½ψ(s/2) + ζ'/ζ(s) (the 1/s and ½ψ(s/2) ≈ −1/s terms cancel at s = 0, so B is finite).

**Step 2 — the identity (★) for Q(a).** Pairing ρ ↔ ρ̄ (1/(½+iγ) + 1/(½−iγ) = 1/(¼+γ²)) and setting s = ½ + a with Q(a) := Σ_{γ>0} 2a/(a²+γ²) and C₀ := Σ_{γ>0} 1/(¼+γ²):

    Q(a) = ζ'/ζ(½+a) + 1/(½+a) + 1/(a−½) − ½lnπ + ½ψ(¼+a/2) − B − C₀.

Q(a) is analytic for a > 0: the pole of ζ'/ζ at s = 1 is cancelled by 1/(a−½), the Γ-pole at s = 0 by 1/s — so the quadrature is stable near a = ½ at sufficient dps.

**Step 3 — the sine transform.** The Laplace–sine pair 2a/(a²+γ²) = 2∫₀^∞ e^{−γt} sin(at) dt, summed over γ > 0 (absolute convergence justifies the interchange), gives Q(a) = 2∫₀^∞ K(x) sin(ax) dx, and inversion gives the **trace formula (★★)**:

    K(x) = (1/π) ∫₀^∞ Q(a) sin(ax) da,      x > 0.

Convergence is conditional — Q(a) ~ ½ln(a/2) − ½lnπ − B − C₀ as a → ∞ — so the axis is split at a = 1.5.

**Step 4 — three parts and the prime weight.** For a > 1.5 the Dirichlet series ζ'/ζ(½+a) = −Σ_n Λ(n)/n^{½+a} converges absolutely, and term-by-term integration produces the comb with weight Λ(n)/√n. The computed decomposition: **T1** (Γ-part), the closed-form integral of (★) on [0, 1.5] via a spline of the dense mpmath grid (601 nodes); **T2** (prime part), the exact series transform (sieve to 10⁷, 665 134 carriers; tail ≤ 1e-6·x⁻¹); **T3** (smooth part), exact Si/Ci forms with ½ψ(z) = ½ln z − 1/(4z) + R₂, R₂ numeric on [1.5, 600], the constant contributing cos(Ax)/x (the Abelian value).

**The two metrics.** M0: direct Q(a) sum (tail analytic from the smooth density N̄′) vs (★) through mpmath — max \|ΔQ\| = 1.7e-12 on a ∈ {0.10, …, 3.00}. M1: direct Σ e^{−xγ} vs (★★) on x ∈ [0.08, 3] — max abs \|ΔK\| = 1.2e-5 (a quadrature floor: at x ≥ 1, K(x) itself is ~1e-6); relative agreement 1e-6…1e-4 in the informative range x ≤ 0.35. **The gate metric:** for a window of 200 unfolded levels x_n (unit mean density), D(u) = Σ_n e^{−u x_n} − (1 − e^{−u x_K})/u against the comb P(u) via r_EF = corr(D, c·P), amplitude c by least squares, **scale fixed at s = 1** (rank matching of windows sets the dual axis; scale optimisation is excluded as a source of r-inflation). Committed thermal grid: 40 points, u ∈ [0.05, 1.0].

## 6. B = −C₀: the control that keeps the derivation honest

Two constants could have been silently tuned; instead both are derived and cross-checked. From ζ(0) = −½ and ζ'(0) = −½ln(2π):

    B = ln(2π) − 1 − ½lnπ − γ/2 = ½ln(4π) − 1 − γ/2 = −0.023095708966…

while C₀ = Σ_{γ>0} 1/(¼+γ²) is a pure zero-file sum. Evaluating the same Hadamard series at s = 0 gives Σ_ρ Re(1/ρ) = 1 + γ/2 − ½ln(4π), whence the classical identity **C₀ = −B**. The file sum over 2 001 052 zeros confirms it to twelve digits: **0.023095708966** (committed: C₀ = 0.02309570896635358, B = −0.023095708966121065). The two routes share no machinery — elementary constants on one side, raw zero data on the other — so any slip in the derivation or corruption of the file would break the agreement. The registry of `results/RESULTS.md` records that a shipped constant (`B_HADAMARD` in `hpbridge/constants.py`, ln(2π) instead of ln(4π)) was later found and fixed with committed v1 verdicts unaffected — precisely the failure mode this control exists to catch.

## 7. The gates at fixed scale

The 52-gate protocol family of C3 (the package's full population is 87 gates; extended families live in C5) is pushed through the identical pipeline. Results, all committed:

- **PC0 (zeros):** r = +0.9998 (0.9997876852323586) at scale 1.0, amplitude 0.0206 (0.02057568817900069), relative residual **2.1%** (0.02060544728275674); a posteriori scale scan r = 0.99986 at scale 0.738; z ≈ 2.59 against the surrogate null cloud 0.00±0.39 (committed 0.000113 ± 0.386); Poisson null 0.08±0.80.
- **Gates (M2):** r_EF spans **−0.93 … +1.00** (min −0.9285, max 0.9978; mean −0.159, sd 0.708), 35 of 52 negative — **null clouds**, no prime weight; median relative residual ≈ 71%; best gate (index 41: Nv = 16, q = 0.5, W = 1.0, α = 0.5) r_EF = 0.9978 with residual **6.7%** (0.06658217196806708), z = 2.62.
- **The gap:** ≈ 0.5 orders by residual (committed gap_orders = 0.509375911913711 ≈ log₁₀(6.7/2.1)) — H2 — NO, measured.

Why the null verdict is **conservative**: the scale knob was removed (fixed s = 1, so r could not be inflated by axis tuning); the null clouds are broad and the honesty registry says so (±0.39 — the trace projection is conservative); the best gate's correlation z-score (2.62) actually *exceeds* the zeros' own (2.59), so correlation alone cannot separate gate from operator — only the residual does; and the ruler is calibrated by PC0, the zeros run through the identical pipeline, so the gates are measured against a working example (2.1%), not an ideal. One reading note: the committed table measures ≈ 0.5 orders; the headline verdict string and `docs/trace_formula.md` §5 (a recorded sweep with best residual 28.7%, gap ≈ 1.1 orders) use the coarse "≈ 1 order" thermal phrasing. All formulations are quoted as committed; the table is the number to cite.

## 8. Results

| Quantity | Value | Status |
|---|---|---|
| M0: the Q(a) identity | |ΔQ| ≤ 1.7e-12 on the grid a ∈ [0.1, 3] | calibrated |
| Built-in control B = −C₀ | 0.023095708966 — 12 digits | classical identity confirmed |
| M1: trace formula for H_ξ | |ΔK| ≤ 1.2e-5 (abs), 1e-6…1e-4 rel. at x ≤ 0.35 | T6 verified |
| PC0: zeros window vs the comb | r = +0.9998, relative residual 2.1% | method sees the prime weight |
| M2: 52 gates | r_EF −0.93…+1.00, null clouds | no prime weight |
| Gap in the trace metric | ≈ 0.5 orders by residual (best 6.7% vs 2.1%) | H2 — NO, measured |
| C3 protocol reproduction | |Δ mean_spacing| = 1.45e-16 | bit-for-bit |

Row takeaways, one line each: **M0** — the closed form (★) is certified as a stand-in for the direct zero-file sum (worst point 1.73e-12 at a = 3.0; the diff grows smoothly with a, the signature of a quadrature floor). **B = −C₀** — derivation and zero data cross-certified at twelve digits. **M1** — theorem T6 verified (max abs 1.2039516971052964e-05 at x = 2.0; relative 1.37e-6 at x = 0.08 to 1.67e-4 at x = 0.35). **PC0** — the metric, comb and pipeline demonstrably detect the prime weight when present. **M2** — the gates do not carry the weight. **Gap** — the third measurement of the H2 gap, consistent with 9–10 orders (C3, rank metric) and C5's stability. **C3 reproduction** — the shared engine reproduces C3's committed mean spacing at float64 round-off (1.4477981779965596e-16): campaigns audit each other bit-for-bit.

## 9. Honest notes

> The 1.2e-5 floor is the quadrature floor, not the precision limit of the identity: for x ≥ 1 the value of K(x) itself is ~1e-6 and the relative metric loses meaning; in the informative range the agreement is 1e-6…1e-4.
> The zero file is needed only for fresh recomputations; the committed verdict is self-contained.

## 10. How to read the numbers

- **M0/M1/M2/PC0 name metrics, not physics magnitudes:** M0 calibrates the identity (★), M1 verifies the trace formula (★★) for H_ξ, M2 applies the thermal metric to the 52 gates, PC0 certifies the metric against the zeros themselves.
- **Quote M1 absolutely:** at x = 2.0 the committed absolute diff is 1.2e-5 while the relative diff reaches 1.2e7 — the identity is intact; the relative denominator (K(x) ~ 1e-6) has simply vanished.
- **"≈ 0.5 orders" = log₁₀ of the residual ratio** (6.7% / 2.1% ≈ 3.2×); it is the measured, reproducible distance between the best gate and the target, far outside quadrature noise.
- **Verdict string vs table:** the verbatim verdict dictionary below keeps the coarse "≈ 1 order" headline; the precise committed measurement is ≈ 0.5 orders (gap_orders = 0.509). Cite the table.

## 11. Interpretation: proves / does not prove

**T6 proves** — the Hadamard → Q(a) → sine-transform chain at |ΔQ| ≤ 1.7e-12 and |ΔK| ≤ 1.2e-5; that the prime weight Λ(n)/√n sits in the heat trace of the zero-coded operator **as a theorem** (clause Г5/H5: proven YES for H_ξ, measured NO for every gate); and that a calibrated benchmark exists — 2.1% residual is what "seeing the primes" costs at fixed scale.

**T6 does not prove** — the Riemann hypothesis (H_ξ is built from the zeros; identity by construction, so the verification is a consistency check of the pipeline, not a step toward RH); it provides no candidate operator (clause Г2/H2 answered NO, measured three ways: 9–10 orders rank metric (C3), ≈ 0.5 orders thermal metric (C4), stable across extended families (C5)); and it does not close the door on nonlocal constructions — the negative verdicts cover the class of *local* lattice Hamiltonians with vortex phases, with nonlocal questions moved to the roadmap (`docs/theory.md`, §4). The package's cycle formula: *the resonator is built and tuned (Г1+Г3+Г4); the zeros are coded, not generated (Г2+Г5); the prime weight is verified only for the zero operator (T6).*

## 12. Reproduction

```bash
# tour of the verdict (~seconds, no zeros file needed)
python3 campaigns/run_c4_trace_formula.py
```

Series seed — 96; RNG streams are fixed (`engine/hamiltonian.py`). All dependencies are in `requirements.txt`. The committed verdict is self-contained; the zeros file is needed only for fresh recomputations. Independent checks: `independent_verification/` (IVP checks of this campaign).

## 13. Data and figures

| File | Where |
|---|---|
| `fig06_trace_en.png` | 600 dpi — `figures_hires/en/fig06_trace_en.png`; screen — `figures/en/` |
| `fig07_parts_en.png` | 600 dpi — `figures_hires/en/fig07_parts_en.png`; screen — `figures/en/` |
| `fig08_rEF_en.png` | 600 dpi — `figures_hires/en/fig08_rEF_en.png`; screen — `figures/en/` |

`fig06_trace` — the trace formula (direct sum vs (★★)); `fig07_parts` — the T1 + T2 + T3 decomposition and the prime share; `fig08_rEF` — the gates' heat projection against the null clouds. Russian-named variants (`fig06_trace.png`, `fig07_parts.png`, `fig08_rEF.png`) live under `figures_hires/ru/` and `figures/ru/`.

| File | Contents |
|---|---|
| `data/results.json` | committed verdict of the campaign |
| `data/` (npz/csv) | curves and tables |
| `../data/c4_*.json` | duplicate of the verdict in the shared registry |

The committed verdict file in this package is `data/task9a_trace_formula.json` (meta: zeros file `zeros6.txt`, n_zeros = 2 001 052, sieve bound 10⁷, split a = 1.5; blocks: M0 grid, M1 grid, prime share, PC0, 52 gate rows, verdict dictionary); the curves are in `data/curves.npz` (arrays `U`, `P_ref`, `D_xi`, `gates_D` — 52×40). **Monographs:** `monograph_ru.docx` · `monograph_ru.pdf` · `monograph_en.docx` · `monograph_en.pdf` — the full monograph of this computation (set-up, theorems, tables, figures, honest limitations): 7–9 pages, the same content in the two languages.

## 14. Verdict

**{'ru': 'T6 верифицирована; разрыв Г2 ≈ 1 порядок в тепловой метрике', 'en': 'T6 verified; the H2 gap ≈ 1 order in the trace metric'}** — details: `data/results.json`, the monograph, and
`independent_verification/` (IVP checks of this campaign).

## 15. FAQ

**1. What is the Guinand–Weil trace formula, in one sentence?**
An exact identity — Tr e^{−xH_ξ} = (1/π)∫₀^∞ Q(a) sin(ax) da — equating a spectral sum over the zeta zeros (the heat trace of the zero-coded operator) with the transform of a function Q(a) that contains ζ'/ζ and therefore, for a > 1.5, the prime comb with weight Λ(n)/√n; it is Weil's explicit formula with the thermal test function e^{−xγ}.

**2. Is C4 a step toward proving RH?**
Not toward RH itself: H_ξ is manufactured from the zeros, so nothing about a natural operator follows. The campaign's yield is different — a proven theorem (T6) about what any Hilbert–Pólya operator's heat trace must contain, a certified pipeline, and a calibrated benchmark (2.1%) that turns the gates' failure into a measurement.

**3. Which gap number should be cited — ≈ 0.5 or ≈ 1 order?**
Cite the table: ≈ 0.5 orders by residual (best gate 6.7% vs the zeros' 2.1%; gap_orders = 0.509). The "≈ 1 order" phrasing belongs to the committed headline verdict string and to the sweep recorded in `docs/trace_formula.md` §5 (best residual 28.7%, gap ≈ 1.1 orders); both are preserved verbatim, but the campaign table is the authoritative measurement.

**4. What would change the H2 verdict?**
A gate family whose heat-trace fluctuation tracks the comb P(u) at a relative residual near the zeros' 2.1% at fixed scale — not a high r_EF, which the broad null clouds (±0.39) produce by chance. The metric's decisive component is the residual, which is exactly why the campaign fixes the scale and calibrates with PC0.

**5. Where do the counts 52 and 87 come from?**
C4 measures the 52-gate protocol family of C3 with the shared engine and protocol (reproduced bit-for-bit: |Δ mean_spacing| = 1.45e-16); 87 is the package's total gate population including the extended families of C5, which are measured separately in that campaign. The trace-formula benchmark of C4 is what the other 35 gates are judged against elsewhere.

**6. Do I need the zeros file to reproduce?**
No — the committed verdict is self-contained and the tour command runs in seconds. The zeros file (`zeros6.txt`, 2 001 052 zeros) is required only for fresh recomputations of the direct sums.

## 16. Mini-glossary

| Term | Meaning |
|---|---|
| Heat trace | Tr e^{−xH} = Σ_n e^{−xλ_n}: the Laplace transform of the spectrum; exponential damping smooths discrete levels into a curve |
| Explicit formula | the classical identity expressing prime sums through zeta zeros (Weil 1952, test-function form) |
| Test function | the even function applied to the zeros; here h(γ) = e^{−xγ} |
| H_ξ | the zero-coded operator diag(±γ_n), built from the zeros file — identity by construction |
| Q(a) | Σ_{γ>0} 2a/(a²+γ²); the sine-transform dual of K(x); contains ζ'/ζ(½+a) via identity (★) |
| K(x) | Σ_{γ>0} e^{−xγ} = Tr e^{−xH_ξ}; recovered from Q(a) by the trace formula (★★) |
| Λ(n)/√n comb | P(u) = Σ Λ(n)/√n · u/(u²+ln²n); the thermal fingerprint of primes and prime powers |
| Unfolded levels | levels rescaled to unit mean density; windows of 200 levels feed D(u) |
| D(u) | heat-trace fluctuation of a window: Σ_n e^{−u x_n} − (1 − e^{−u x_K})/u |
| r_EF | corr(D, c·P) at fixed scale s = 1, amplitude c by least squares — the projection metric |
| Null cloud | the spread of r_EF for spectra with no prime weight (surrogate 0.00±0.39, Poisson 0.08±0.80) |
| PC0 | positive control: the zeros' own window through the identical pipeline (r = +0.9998, residual 2.1%) |
| H2 / Г2 | the "spectral identity" clause of the Hilbert–Pólya checklist (level n ↔ zero n) — verdict NO |
| T6 | the theorem of this campaign: the trace formula with prime weight for H_ξ |
| M0 / M1 / M2 | calibration of (★); verification of (★★) for H_ξ; the 52-gate thermal projection |

## 17. A five-minute tour of the explicit formula

A compact walk through the two sides, using four committed numbers as stepping stones.

**Stand on the primes side and read identity (★) term by term.**

    Q(a) = ζ'/ζ(½+a) + 1/(½+a) + 1/(a−½) − ½lnπ + ½ψ(¼+a/2) − B − C₀.

Six terms, each with a fixed role and none with a free parameter: the first term carries the primes (through ζ'/ζ, whose Dirichlet series at a > 1.5 is exactly −Σ_n Λ(n)/n^{½+a}); the two pole terms 1/(½+a) and 1/(a−½) are the echoes of the 1/s and 1/(s−1) factors in ξ'/ξ; −½lnπ is the archimedean density; ½ψ(¼+a/2) is the Γ-part; and −B − C₀ subtracts the two Hadamard normalization constants derived in section 6. The identity is an equality between the raw zero-file sum Q(a) = Σ_{γ>0} 2a/(a²+γ²) and this closed form — which is why it can serve as a calibration, not a fit.

**Stone one — the M0 grid at a = 0.10.** Direct sum over the file: Q = 0.004620924280814972. Closed form (★): Q = 0.004620924280536055. Difference: 2.79e-13. Across the grid a ∈ {0.10, …, 3.00} the difference never exceeds 1.73e-12 (attained at a = 3.0). The primes side and the zeros side already agree before any transform is taken.

**Cross the bridge and land on the operator side.** The same Q(a) feeds the trace formula (★★). At x = 0.08 the direct spectral sum over the file gives K = 1.0352618292269251, while the three-part formula gives T1 + T2 + T3 = 0.0013190607 − 0.0322335884 + 1.0661749357 = 1.0352604080544578 — agreement to 1.42e-6. Note who dominates at small x: the smooth archimedean bulk T3 (1.066) dwarfs everything; the prime part T2 is already present (−0.0322) but sits on top of the bulk. This is the optical problem of the whole subject: the prime weight is real but buried in a smooth background.

**Stone two — why the fluctuation, and only the fluctuation, can see the comb.** The gate metric of section 5 subtracts exactly that smooth background — D(u) = Σ_n e^{−u x_n} − (1 − e^{−u x_K})/u — so what remains is the spectral fine structure, which is then correlated against the comb P(u) at fixed scale. On the zeros' own window the residual of that comparison is 2.1%; on the best of the 52 gates it is 6.7% — a factor ≈ 3.2, the ≈ 0.5-order gap. That is the campaign in miniature: derive (Hadamard → (★)), verify (M0, M1), calibrate (PC0), and only then aim the same ruler at the candidates.

## 18. See also

- [../C3_gate_family/README.md](../C3_gate_family/README.md) — the gate family measured here; the rank-correlation projection of the H2 gap.
- [../../docs/trace_formula.md](../../docs/trace_formula.md) — the complete derivation of T6 with every constant derived.
- [../../results/RESULTS.md](../../results/RESULTS.md) — the committed registry of numbers, the Г1–Г5/H1–H5 verdicts, and the honesty registry.

---
*Hilbert Polya Bridge v1.0.0 · C4 · The trace formula: Tr e^{−uH} versus the explicit formula*

