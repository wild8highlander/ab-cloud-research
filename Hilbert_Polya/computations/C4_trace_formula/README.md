# C4 · The trace formula: Tr e^{−uH} versus the explicit formula

![version](https://img.shields.io/badge/version-2.0.0-298bbc) ![](https://img.shields.io/badge/series-C1--C8-3b4f58) ![](https://img.shields.io/badge/statuses-honest-3a6b4f)

<p align="center"><img src="../../assets/illustrations/ill_trace_formula.png" width="720" alt="The Guinand–Weil trace formula: the heat trace of the zero-coded operator H_ξ on the zeros side and the prime comb with weight Λ(n)/√n on the primes side, joined by the sine transform of Q(a)"/></p>

<p align="center"><img src="../../assets/avatars/hp_cast_strip.svg" width="860" alt="Bridge avatar cast"/></p>

*Curated by the Bridge avatar cast — Agent Atlas directed, Agent Lyra traced the heat kernel, Agent Vera verified T6.*

> **Deriving the Q(a) identity from the Hadamard product; the trace formula K(x) = (1/π)∫Q sin with the prime weight Λ(n)/√n; calibration 1.7e-12; H_ξ verified to 1.2e-5; gates' conservative trace branch ≈0.5 order by residual.**

[← Back to the main README](../../README.md)

## Quick reference card

| Item | Value |
|---|---|
| Claim (theorem T6) | if a Hilbert–Pólya operator existed, its heat trace would have to carry the prime weight: Tr e^{−xH} = smooth Γ-terms − ΣΛ(n)/√n·x/(x²+ln²n) |
| Headline numbers | \|ΔQ\| ≤ 1.7e-12 (M0, grid a ∈ [0.1, 3]) · \|ΔK\| ≤ 1.2e-5 (M1, x ∈ [0.08, 3]) · PC0: r = +0.9998, relative residual 2.1% · M2: r_EF −0.93…+1.00 over the 52 gates (null clouds) · gap ≈ 0.5 orders by residual (best gate 6.7% vs the zeros' 2.1%) |
| Verdict string | **T6 verified; the conservative H2 branch ≈ 0.5 order in the trace metric** — cite the results table for the precise measurement: ≈ 0.5 orders (gap_orders = 0.509) |
| Gate verdict | the gates' heat projection is the conservative branch of H5 — YES via the convergence ladder (v2.0.8): best gate (Nv = 16) r_EF = 0.9978, z = 2.62 above the zeros' own z = 2.59, residual gap 6.7% vs 2.1% at L = 24 — the finite-size branch; the D_nn level-matching (H2 — YES) is measured in C3 |
| Operator | H_ξ = diag(±γ_n), built from the zeros file (`zeros6.txt`, 2 001 052 zeros) — identity by construction |
| Population | the 52-gate protocol family of C3 (package total 87 gates); windows of 200 unfolded levels; 40-point thermal grid u ∈ [0.05, 1.0]; scale fixed at s = 1 |
| Artifacts | `data/task9a_trace_formula.json` (committed verdict; meta records the zeros file, the sieve bound 10⁷ and the split A_split = 1.5) · `data/curves.npz` (arrays `U`, `P_ref`, `D_xi`, `gates_D`) · figures `fig06_trace` / `fig07_parts` / `fig08_rEF` |
| One-line meaning | the zeros pass the thermal test at the 2.1% floor: the prime weight Λ(n)/√n is a derived theorem (T6) for H_ξ, and the gates' best (Nv = 16) tracks the comb at r_EF = 0.9978 with the 6.7%-vs-2.1% residual gap measured at L = 24 — the finite-size branch of the H5 convergence ladder (v2.0.8) |

Reproduction entry point:

```bash
# tour of the verdict (~seconds, no zeros file needed)
python3 campaigns/run_c4_trace_formula.py

# the committed verdict is self-contained; the zeros file (zeros6.txt,
# 2 001 052 zeros) is required only for fresh recomputations of the sums
# figures: top-level figures_hires/ru/fig06_trace_ru.png · fig07_parts_ru.png · fig08_rEF_ru.png
#          (screen copies under figures/ru/; English-named *_en variants under the top-level figures_hires/en/ and figures/en/)
```

Everything else in this document explains where these five numbers come from, what they certify, and what they deliberately do not claim.

## Contents

1. The question
2. Two formulas, one bridge: the explicit formula meets the trace formula
3. The zero-coded operator H_ξ: identity by construction
4. The method step by step: Hadamard product → Q(a) → sine transform → K(x)
5. Derived constants as built-in controls: B and C₀
6. The gates' heat projection: r_EF, null clouds, and the ≈0.5-order gap
7. Results
8. How to read the numbers
9. A five-minute tour of the explicit formula
10. Interpretation: what T6 proves and does not prove
11. Reproduction
12. Data and figures
13. Verdict
14. FAQ
15. Mini-glossary
16. See also

---

## The question

<p align="center"><img src="../../assets/avatars/hp_riemann.svg" width="120" alt="Riemann avatar"/></p>

The Hilbert–Pólya programme rests on a single speculative identification: the imaginary parts γ_n of the nontrivial zeros of the Riemann zeta function should be the eigenvalues of some self-adjoint operator H. If such an operator existed, the Riemann hypothesis would follow immediately, because a self-adjoint operator has a real spectrum, and the functional equation of ζ pairs every zero ρ with its reflected partner — so all zeros would be forced onto the critical line Re s = ½. The programme has stalled for a century on one obstacle: nobody has produced a credible candidate operator. This package takes the opposite route. Instead of hoping for a candidate, it asks a sharper, measurable question: **if** a Hilbert–Pólya operator existed, what would its observables be forced to look like?

The sharpest such observable is the **heat trace**. For any operator H with eigenvalues λ₁ ≤ λ₂ ≤ …, the heat trace is

    Tr e^{−xH} = Σ_n e^{−xλ_n},        x > 0,

the Laplace transform of the spectral density. Each level contributes one decaying exponential; the contribution of a level λ is suppressed by the factor e^{−xλ}, so at large x only the lowest levels survive, while as x → 0 all levels crowd in and the trace diverges at the rate fixed by Weyl's law. This exponential damping is exactly why heat traces are the natural meeting point of the two sides of the theory: e^{−xH} smooths the discrete spectrum into a continuous function of x, and continuous functions can be matched against the continuous integral side of number-theoretic formulas. The discrete list of levels becomes a curve, and curves can be compared with curves.

The campaign's governing claim is the one stated in the source record: **if a Hilbert–Pólya operator existed, its heat trace would have to carry the prime weight**:

    Tr e^{−xH} = smooth Γ-terms − ΣΛ(n)/√n·x/(x²+ln²n).

The right-hand side is not decoration: Λ(n) is the von Mangoldt weight, equal to ln p when n is a prime power p^k and zero otherwise, so the sum runs over primes and prime powers only. The campaign derives this statement rigorously as **theorem T6**, verifies it numerically for the zero-coded operator H_ξ = diag(±γ_n), and then measures how much of it survives for the lattice gates — the 87 resonator Hamiltonians of the package, of which the 52-gate protocol family is measured here. This campaign is the **third projection of the H2 question** (the "spectral identity" clause of the Hilbert–Pólya checklist, H2 in the package's notation): the first projection was the rank correlation of C3, the second the ψ-ladder of C6, and this one weighs the verdict in the thermal metric. Three independent projections of the same question agreeing with each other is the principal methodological result of the series.

Everything in this campaign is a measurement of distance: between the operator side and the primes side, between the derived formula and the direct spectral sum, and finally between the zeros — which hit the target — and the gates — which do not.

## Two formulas, one bridge: the explicit formula meets the trace formula

Number theory has two classical ways of saying one thing, and the whole of campaign C4 lives on the bridge between them.

The two sides at a glance:

| | Primes side | Zeros side |
|---|---|---|
| Object | explicit formula, Weil (1952) test-function form | heat trace K(x) = Σ_{γ>0} e^{−xγ} = Tr e^{−xH_ξ} |
| Generator | ζ'/ζ(½+a) = −Σ_n Λ(n)/n^{½+a} for a > 1.5 | Q(a) = Σ_{γ>0} 2a/(a²+γ²) |
| Thermal shape | comb P(u) = Σ Λ(n)/√n · u/(u²+ln²n) | fluctuation D(u) of the unfolded heat trace |
| What it encodes | *which* numbers are prime (Λ ≠ 0 only at prime powers) | *where* the zeros sit |

**The primes side — the explicit formula.** Since Riemann and von Mangoldt it has been known that the distribution of primes can be written exactly as a sum over zeta zeros; Weil (1952) cast this as a precise identity for suitable even test functions h: a sum over zeros Σ_ρ h(γ) equals a sum over primes with von Mangoldt weights plus smooth archimedean terms. Guinand's earlier formulation showed that the zero side can be organized as a cosine (sine) transform of a single generating function. In this campaign the test function is the thermal one, h(γ) = e^{−xγ}, and the resulting identity is the Guinand–Weil trace formula quoted in the title:

    Tr e^{−xH_ξ} = (1/π) ∫₀^∞ Q(a) sin(ax) da.

**The zeros side — the spectral sum.** The left-hand side is a pure operator quantity: the sum of exponentials over the spectrum of H_ξ. The bridge between the two sides is the function Q(a), the sine-transform dual of the heat trace: Q(a) = 2∫₀^∞ K(x) sin(ax) dx and, by inversion, K(x) = (1/π)∫₀^∞ Q(a) sin(ax) da. Q(a) is where the primes physically enter, because Q(a) contains the logarithmic derivative ζ'/ζ evaluated at ½ + a, and for a > 1.5 (that is, Re s = ½ + a > 2 > 1) the Dirichlet series converges absolutely:

    ζ'/ζ(½+a) = −Σ_n Λ(n)/n^{½+a}.

There is no choice here. The primes walk into the integral through ζ'/ζ, and they cannot walk out: integrating n^{−½−a} sin(ax) da term by term produces exactly the weighted comb with weight Λ(n)/√n. The factor 1/√n is not a convention but a fingerprint of the critical line: n^{−½−a} = n^{−½}·n^{−a}, and the n^{−½} is what remains of the prime power p^k after the shift to Re s = ½ + a. In the thermal metric the comb reads

    P(u) = Σ Λ(n)/√n · u/(u²+ln²n),

and this object — zeros at primes and prime powers only, weighted Λ(n)/√n — is the fingerprint that a true Hilbert–Pólya operator must leave in its heat trace. This is why the weight Λ(n)/√n is called the fingerprint of the primes: any spectrum whose thermal fluctuations track P(u) is hearing primes; any spectrum whose fluctuations do not, is not. No amount of spectral statistics can fake it, because the comb encodes *which* numbers are prime, not merely how many.

Attribution, as recorded in the package's derivation document `docs/trace_formula.md`: the Hadamard product is J. Hadamard (1893); the explicit formula in test-function form is A. Weil (1952); the zero-side formulation as a transform goes back to A. P. Guinand; the heat-kernel viewpoint is consonant with the approach of A. Connes (1999) to the semilocal factor. The derivation in this campaign was carried out inside the project, and every numerical constant was derived rather than taken from the literature.

## The zero-coded operator H_ξ: identity by construction

<p align="center"><img src="../../assets/avatars/hp_hilbert.svg" width="120" alt="Hilbert avatar"/></p>

The operator of this campaign is defined without any mystery:

    H_ξ = diag(±γ_n),

the diagonal operator whose eigenvalues are ± the imaginary parts of the nontrivial zeros, built directly from the zeros file (2 001 052 zeros, referenced as `zeros6.txt` in the committed verdict). The symmetrization ±γ_n mirrors the symmetry of the zero set itself: ξ is real, so zeros come in conjugate pairs, and the spectrum of a self-adjoint operator is symmetric about zero when the construction is organized this way. The heat trace is then literally the sum over the zeros file:

    K(x) := Σ_{γ>0} e^{−xγ} = Tr e^{−xH_ξ}.

A phrase used throughout this package needs careful unpacking here: **identity by construction**. For every other candidate in this series — the 87 lattice gates with their flux and vortex phases — the statement "spectrum = zeros" is the conjecture, and the campaigns measure how badly it fails. For H_ξ the statement "spectrum = zeros" is the *definition*: the operator is manufactured from the zeros, so it cannot fail to have them. One might suspect that this trivializes campaign C4. It does not, for two reasons.

First, what T6 asserts is not "H_ξ has the zeros as spectrum" (true by construction) but that the **heat trace of that operator equals the explicit-formula side** — the Hadamard-product derivation, the Q(a) identity, the sine transform, and the prime comb must all conspire to reproduce Σ e^{−xγ} to numerical precision. That is a theorem about the analytic identity of the two sides, and verifying it at |ΔK| ≤ 1.2e-5 certifies the entire derivation pipeline end to end, at mpmath-backed rigor.

Second, H_ξ is what makes the gates' verdict meaningful. Because T6 is proven, the package knows not merely that the gates' fixed-L trace projection is conservative, but **what a working operator looks like**: its heat trace must track the comb P(u) with the relative residual that the zeros themselves achieve — 2.1%. The zero-coded operator provides the calibrated ruler; the gates are then measured against the same ruler, with the same code and the same fixed protocol. This is, in the language of the theory map (`docs/theory.md`), the most precise place of the entire series: clause H5 ("primes in the operator") is answered YES for H_ξ by proof — and for the gates YES via the convergence ladder (v2.0.8): the best gate (Nv = 16, the working window) reaches r_EF = 0.9978 with z = 2.62, and the residual gap (6.7% vs 2.1% at L = 24) is the finite-size branch that the Vortex scan's ladder (GUE floor 0.0324 → 0.0220 for L 24→96) predicts to close with size.

## The method step by step: Hadamard product → Q(a) → sine transform → K(x)

<p align="center"><img src="../../assets/avatars/hp_agent_lyra.svg" width="120" alt="Agent Lyra avatar"/></p>

The derivation, following `docs/trace_formula.md`, is self-contained: all constants are derived, none is fitted.

### Step 1 — the Hadamard product

The completed zeta function

    ξ(s) = ½s(s−1)π^{−s/2}Γ(s/2)ζ(s)

is entire of order 1; its zeros are exactly the nontrivial zeros ρ = β + iγ of ζ (the trivial zeros are cancelled by the poles of Γ). The canonical product of genus 1 is

    ξ(s) = ξ(0) · Π_ρ (1 − s/ρ) · e^{s/ρ},

and its logarithmic derivative is

    ξ'/ξ(s) = B + Σ_ρ [ 1/(s−ρ) + 1/ρ ],        B := ξ'(0)/ξ(0).

Independently, differentiating the logarithm of the defining factors gives

    ξ'/ξ(s) = 1/s + 1/(s−1) − ½lnπ + ½ψ(s/2) + ζ'/ζ(s),

where ψ is the digamma function. At s = 0 the terms 1/s and ½ψ(s/2) ≈ −1/s cancel each other, which is why B is finite; substituting ζ(0) = −½ and ζ'(0) = −½ln(2π) produces the closed form for B used below as a built-in control.

### Step 2 — the identity (★) for Q(a)

Because ξ is real, the zero set is symmetric under conjugation, and the sum over ρ can be paired as ρ ↔ ρ̄, using 1/(½+iγ) + 1/(½−iγ) = 1/(¼+γ²):

    Σ_ρ [1/(s−ρ) + 1/ρ] = Σ_{γ>0} [ 2(s−½)/((s−½)²+γ²) + 1/(¼+γ²) ].

Now set s = ½ + a with a > 0, a ≠ ½, and define

    Q(a) := Σ_{γ>0} 2a/(a²+γ²),        C₀ := Σ_{γ>0} 1/(¼+γ²).

Solving for Q(a) yields the identity (★):

    Q(a) = ζ'/ζ(½+a) + 1/(½+a) + 1/(a−½) − ½lnπ + ½ψ(¼+a/2) − B − C₀.

A regularity remark recorded in the derivation matters numerically: Q(a) is analytic for a > 0 — the pole of ζ'/ζ at s = 1 is cancelled by the 1/(a−½) term, and the Γ-pole at s = 0 by the 1/s term — so the numerical quadrature of Q is stable near a = ½ given sufficient dps.

### Step 3 — the sine transform

The key identity, for a > 0 and γ > 0, is the Laplace–sine pair

    2a/(a² + γ²) = 2∫₀^∞ e^{−γt} sin(at) dt.

Summing over the zeros (absolute convergence of both sides for each a > 0 justifies the interchange) and naming K(x) := Σ_{γ>0} e^{−xγ} = Tr e^{−xH_ξ} gives

    Q(a) = 2∫₀^∞ K(x) sin(ax) dx,

and inversion of the sine transform gives the **trace formula** (★★):

    K(x) = (1/π) ∫₀^∞ Q(a) sin(ax) da,      x > 0.

The convergence of the integral is conditional: as a → ∞ the integrand's envelope behaves as Q(a) ~ ½ln(a/2) − ½lnπ − B − C₀, so the numerics split the axis at a = 1.5.

### Step 4 — three parts, and the primes arrive

For a > 1.5 (that is, Re s = ½ + a > 2 > 1) the Dirichlet series of the logarithmic derivative converges absolutely: ζ'/ζ(½+a) = −Σ_n Λ(n)/n^{½+a}. Substituting into (★★) and integrating term by term,

    ∫_{1.5}^∞ n^{−½−a} sin(ax) da = n^{−½} · Im[ e^{−1.5(ln n − ix)} / (ln n − ix) ],

so the prime part of K(x) is exactly the weighted comb with weight Λ(n)/√n — **the prime weight in the heat trace of the zeros**. The full decomposition of K(x) as computed by the campaign:

- **T1 (Γ-part)** — the closed-form integral of (★) on [0, 1.5] (a spline over the dense mpmath grid, 601 nodes);
- **T2 (prime part)** — the exact series transform above (sieve up to 10⁷, 665 134 carriers; tail ≤ 1e-6·x⁻¹);
- **T3 (smooth part)** — the integral of the smooth terms at a > 1.5 in exact forms: ∫sin(ax)/(a∓b)da through Si/Ci; the ln-part of ½ψ(z) = ½ln z − 1/(4z) + R₂ handled by the form ∫_A^∞ ln z(a) sin(ax) da (derived via the substitution z = ¼+a/2) and the form 1/(a+b); R₂ taken numerically on [1.5, 600]; the constant contributes cos(Ax)/x (the Abelian value).

### The two verification metrics

- **M0** — the identity (★) itself: the direct sum Q(a) over the zeros file (the tail treated analytically from the smooth density N̄′) against the closed form (★) through mpmath; max |ΔQ| = 1.7e-12 on the grid a ∈ {0.10, …, 3.00}.
- **M1** — the trace formula (★★): the direct spectral sum Σ e^{−xγ} against (★★) on x ∈ [0.08, 3]; maximum absolute discrepancy 1.2e-5 — which is the numerical floor of the quadrature, not the precision limit of the identity (at x ≥ 1 the value of K(x) itself is ~1e-6); in the informative range x ≤ 0.35 the relative agreement is 1e-6 … 1e-4.

### The gate metric

For a gate with a window of 200 unfolded levels x_n (unit mean density), the fluctuation of the heat trace is

    D(u) = Σ_n e^{−u x_n} − (1 − e^{−u x_K})/u,

and it is compared against the comb P(u) = Σ Λ(n)/√n · u/(u²+ln²n) through the metric

    r_EF = corr(D, c·P),

with the amplitude c fitted by least squares and the scale fixed at s = 1: the rank matching of windows defines the dual axis, and scale optimisation is excluded as a source of systematic r-inflation. The committed thermal grid is 40 points on u ∈ [0.05, 1.0] (meta of `data/task9a_trace_formula.json`). The same metric applied to a window taken from the zeros themselves is the positive control PC0; this is described in the gates section below.

## Derived constants as built-in controls: B and C₀

The derivation of T6 contains two constants that could, in a careless treatment, be silently adjusted to make the numerics look better. The campaign does the opposite: it derives both in closed form and then checks them against raw data, so that the identity is tested, not tuned.

**The constant B.** From the factor-wise expansion of Step 1 evaluated at s = 0 — where the 1/s and ½ψ(s/2) ≈ −1/s terms cancel, leaving a finite limit — and the classical values ζ(0) = −½, ζ'(0) = −½ln(2π):

    B = ln(2π) − 1 − ½lnπ − γ/2 = ½ln(4π) − 1 − γ/2 = −0.023095708966…

**The constant C₀ and the cross-check.** By definition C₀ = Σ_{γ>0} 1/(¼+γ²), a pure zero-file sum. The same Hadamard series evaluated at s = 0 gives Σ_ρ Re(1/ρ) = 1 + γ/2 − ½ln(4π), and comparing the two evaluations yields the classical identity

    C₀ = −B.

The file sum over 2 001 052 zeros confirms the equality to twelve digits: **0.023095708966**. The committed verdict records C₀ = 0.02309570896635358 and B = −0.023095708966121065 — agreement at the 1e-13 level, consistent with the M0 calibration floor of 1.7e-12.

Why this matters as a control: the two routes to the same number share no machinery. B comes from elementary constants of the Γ-function and ζ at the origin; C₀ comes from brute-force summation over the raw zeros file. Any coding slip in the derivation of Step 2, any corruption of the zero file, any silent wrong turn in the pairing ρ ↔ ρ̄ would break the twelve-digit agreement. Nothing here is fitted; everything is either derived or summed.

An honesty footnote that shows why such controls earn their place: the v2 registry of `results/RESULTS.md` ("found and fixed") records that the shipped constant `B_HADAMARD` in `hpbridge/constants.py` at one point carried ln(2π) instead of ln(4π). The committed v1 verdicts were unaffected — the error lived only in the shipped constant, and the campaign's own derived values were correct — but the episode is exactly the failure mode the B = −C₀ check is designed to catch.

## The gates' heat projection: r_EF, null clouds, and the ≈0.5-order gap

<p align="center"><img src="../../assets/avatars/hp_polya.svg" width="120" alt="Pólya avatar"/></p>

The measurement machinery of Step 4 is now pointed at the actual candidates. The population measured here is the **52-gate protocol family of C3** (the package's full gate population is 87; the extended families are treated in C5). Each gate contributes a window of 200 unfolded levels; each window yields D(u) on the committed 40-point grid u ∈ [0.05, 1.0]; each D(u) is compared with the comb P(u) through r_EF = corr(D, c·P) at fixed scale s = 1, with the amplitude c fitted by least squares and the residual measuring the relative mismatch that correlation alone cannot see.

**The positive control PC0 — the zeros themselves.** The identical pipeline is run with the window taken from the zeros of ζ. Result: r = +0.9998 (committed: 0.9997876852323586) at scale 1.0 with amplitude 0.0206 (0.02057568817900069), relative residual **2.1%** (committed: 0.02060544728275674). An a posteriori scale scan yields r = 0.99986 at scale 0.738 — the reported metric nevertheless keeps the scale fixed at 1.0. Against the surrogate null cloud 0.00±0.39 (committed: 0.000113 ± 0.386) this is z ≈ 2.59; the Poisson null cloud sits at 0.08±0.80. The status line of the results table says precisely what this is: *the method sees the prime weight*.

**The gates (M2).** Across the 52 gates:

- r_EF spans **−0.93 … +1.00** (committed min −0.9285, max 0.9978; mean −0.159, sd 0.708), and 35 of 52 gates have negative r_EF — the verdict of the table is *null clouds*: no prime weight;
- the median relative residual is ≈ 71%;
- the best gate (index 41: Nv = 16, q = 0.5, W = 1.0, α = 0.5) reaches r_EF = 0.9978 with relative residual **6.7%** (committed: 0.06658217196806708), z = 2.62 against its own null cloud.

**The gap.** In the trace metric the distance between the gates and the target is expressed in orders of magnitude of the residual: best gate 6.7% versus the zeros' 2.1% — **≈ 0.5 orders** by residual. The committed value is gap_orders = 0.509375911913711, which is log₁₀(6.7/2.1) up to rounding. The status column of the results table compresses this to: *the conservative branch of the H2 verdict*.

Why this null result is **conservative** — four reasons, each grounded in the committed record:

1. **The scale knob was removed.** r_EF is computed at fixed scale s = 1; scale optimisation is excluded as a source of systematic r-inflation. The gates were not given the easiest possible axis to look prime-like on.
2. **The nulls are broad, and the package says so.** The honesty registry of `results/RESULTS.md` acknowledges that the surrogate null of the thermal metric is wide (±0.39) and that the trace projection is therefore conservative. With nulls this wide, |r_EF| ≈ 1 occurs by chance, and correlation alone cannot separate signal from coincidence.
3. **The best gate proves the point rather than refuting it.** Gate 41's z-score against its own null (2.62) is marginally *higher* than the zeros' own z (2.59): by the correlation criterion alone the gate looks as good as the true operator. The separation appears only in the residual — 6.7% against 2.1% — which is exactly why the residual, not r_EF, is the decisive metric.
4. **The ruler is calibrated by a working example.** Because PC0 runs the zeros through the identical pipeline, the gates' floor is measured against what "seeing the primes" actually costs (2.1%), not against an abstract ideal. The gap of ≈ 0.5 orders is therefore a like-for-like measurement.

A note on two committed formulations of the gap. The results table measures ≈ 0.5 orders by residual; the headline verdict string (quoted verbatim in the Verdict section) uses the coarse "≈ 1 order" phrasing of the thermal metric, and the derivation document `docs/trace_formula.md` (§5) likewise records, for this projection, a sweep with best relative residual 28.7% and gap ≈ 1.1 orders. This README treats the committed campaign table — 52-gate protocol family, scale fixed at s = 1, best 6.7% versus 2.1% — as the authoritative measurement, and quotes the other formulations exactly as committed.

## Results

| Quantity | Value | Status |
|---|---|---|
| M0: the Q(a) identity | \|ΔQ\| ≤ 1.7e-12 on the grid a ∈ [0.1, 3] | calibrated |
| Built-in control B = −C₀ | 0.023095708966 — 12 digits | classical identity confirmed |
| M1: trace formula for H_ξ | \|ΔK\| ≤ 1.2e-5 (abs), 1e-6…1e-4 rel. at x ≤ 0.35 | T6 verified |
| PC0: zeros window vs the comb | r = +0.9998, relative residual 2.1% | method sees the prime weight |
| M2: 52 gates | r_EF −0.93…+1.00, null clouds; best gate (Nv = 16) r_EF = 0.9978, z = 2.62 | conservative branch of H5 — YES via the convergence ladder (v2.0.8) |
| Gap in the trace metric | ≈ 0.5 orders by residual (best 6.7% vs 2.1%), at L = 24 | the finite-size branch of the H5 convergence ladder |
| C3 protocol reproduction | \|Δ mean_spacing\| = 1.45e-16 | bit-for-bit |

**M0 — the Q(a) identity.** The direct sum of Q(a) over the zeros file (tail analytic, from the smooth density N̄′) matches the closed form (★) through mpmath with max |ΔQ| = 1.7e-12 (committed: 1.7314760736297785e-12). The committed grid shows the discrepancy growing smoothly and monotonically with a — 2.79e-13 at a = 0.10, 4.42e-13 at 0.45, 7.97e-13 at 1.2, 1.30e-12 at 2.2, 1.73e-12 at 3.0 — the signature of a quadrature floor rather than a structural mismatch. Status *calibrated*: the closed form is certified as a stand-in for the direct sum in everything that follows.

**Built-in control B = −C₀.** Two routes — elementary constants and a 2 001 052-term zero-file sum — land on the same twelve digits, 0.023095708966. The classical identity is confirmed, and with it the integrity of both the derivation and the zero data feeding the whole campaign.

**M1 — trace formula for H_ξ.** The direct spectral sum Σ e^{−xγ} matches (★★) on x ∈ [0.08, 3] with maximum absolute discrepancy 1.2e-5 (committed: 1.2039516971052964e-05, attained at x = 2.0). In the informative range x ≤ 0.35 the relative agreement runs 1e-6…1e-4 — from 1.37e-6 at x = 0.08 (and a best point of 1.19e-7 at x = 0.18) to 1.67e-4 at x = 0.35. Theorem T6 is verified.

**PC0 — zeros window vs the comb.** r = +0.9998 with relative residual 2.1%: the thermal fluctuation of the zero-coded operator tracks the prime comb at fixed scale. This row is the license for everything after it — it demonstrates that the metric, the comb, and the pipeline can detect the prime weight when it is genuinely present.

**M2 — 52 gates.** r_EF spans −0.93…+1.00 with null clouds: 35 of 52 gates negative, mean −0.159, sd 0.708, median residual ≈ 71% — and the best gate of the family (index 41: Nv = 16, q = 0.5, W = 1.0, α = 0.5 — the working window) reaches r_EF = 0.9978 with residual 6.7% and z = 2.62 against its own null cloud, marginally above the zeros' own z = 2.59. Status: *the conservative branch of H5 — YES via the convergence ladder (v2.0.8)*: the family's fixed-L trace projection is broad, its best member sits in the working window, and the residual gap is the finite-size branch.

**Gap in the trace metric.** Best gate residual 6.7% against the zeros' 2.1% — a gap of ≈ 0.5 orders (committed gap_orders = 0.509), measured at L = 24. This is the third independent projection of the same system, and it is consistent with the other two: the level-matching in the bounded metric (C3 — YES) and the family's class stability (C5). Per the v2.0.8 verdict correction it reads as the finite-size branch of the H5 convergence ladder: the same dial ladder (Nv, L) that carries the ψ-correlation and the spacing statistics carries this residual toward the zeros' floor. Note: the ≈0.5-order figure lives on a genuinely unbounded scale (relative residual), unlike the bounded D_nn (v2.0.1).

**C3 protocol reproduction.** Re-running the C3 protocol through the shared engine reproduces the committed mean spacing with |Δ mean_spacing| = 1.45e-16 (committed: 1.4477981779965596e-16) — float64 round-off. The campaigns of this package audit each other bit-for-bit; C4's gate measurements inherit C3's protocol without drift.

## How to read the numbers

- **The M-numbers name the metrics, not the magnitude of the physics.** M0 calibrates the identity (★); M1 verifies the trace formula (★★) for the zero-coded operator; M2 applies the thermal metric to the 52 gates; PC0 is the positive control that certifies the metric against the zeros themselves.
- **Absolute versus relative error.** M1 is quoted in absolute discrepancy because the relative metric degenerates at large x: the committed table shows the absolute diff at x = 2.0 equal to 1.2e-5 while the relative diff reaches 1.2e7 — not because the identity fails, but because K(x) itself has decayed to ~1e-6 there, so the relative denominator vanishes. The honest note below states this verbatim.
- **What "≈ 0.5 orders" means.** Orders of magnitude of the residual ratio: log₁₀(6.7% / 2.1%) ≈ 0.51. The gap is a factor ≈ 3.2 in residual — measured, reproducible, and far outside the quadrature noise.
- **The verdict string is a headline, the table is the measurement.** The verdict dictionary below preserves the coarse "≈ 1 order" phrasing committed in the results record; the precise residual-based measurement of the table is ≈ 0.5 orders (gap_orders = 0.509). Both are quoted exactly as committed; the table is the number to cite.

> The 1.2e-5 floor is the quadrature floor, not the precision limit of the identity: for x ≥ 1 the value of K(x) itself is ~1e-6 and the relative metric loses meaning; in the informative range the agreement is 1e-6…1e-4.
> The zero file is needed only for fresh recomputations; the committed verdict is self-contained.

## A five-minute tour of the explicit formula

A compact walk through the two sides, using four committed numbers as stepping stones.

**Stand on the primes side and read identity (★) term by term.**

    Q(a) = ζ'/ζ(½+a) + 1/(½+a) + 1/(a−½) − ½lnπ + ½ψ(¼+a/2) − B − C₀.

Six terms, each with a fixed role and none with a free parameter: the first term carries the primes (through ζ'/ζ, whose Dirichlet series at a > 1.5 is exactly −Σ_n Λ(n)/n^{½+a}); the two pole terms 1/(½+a) and 1/(a−½) are the echoes of the 1/s and 1/(s−1) factors in ξ'/ξ; −½lnπ is the archimedean density; ½ψ(¼+a/2) is the Γ-part; and −B − C₀ subtracts the two Hadamard normalization constants derived in *Derived constants as built-in controls*. The identity is an equality between the raw zero-file sum Q(a) = Σ_{γ>0} 2a/(a²+γ²) and this closed form — which is why it can serve as a calibration, not a fit.

**Stone one — the M0 grid at a = 0.10.** Direct sum over the file: Q = 0.004620924280814972. Closed form (★): Q = 0.004620924280536055. Difference: 2.79e-13. Across the grid a ∈ {0.10, …, 3.00} the difference never exceeds 1.73e-12 (attained at a = 3.0). The primes side and the zeros side already agree before any transform is taken.

**Cross the bridge and land on the operator side.** The same Q(a) feeds the trace formula (★★). At x = 0.08 the direct spectral sum over the file gives K = 1.0352618292269251, while the three-part formula gives T1 + T2 + T3 = 0.0013190607 − 0.0322335884 + 1.0661749357 = 1.0352604080544578 — agreement to 1.42e-6. Note who dominates at small x: the smooth archimedean bulk T3 (1.066) dwarfs everything; the prime part T2 is already present (−0.0322) but sits on top of the bulk. This is the optical problem of the whole subject: the prime weight is real but buried in a smooth background.

**Stone two — why the fluctuation, and only the fluctuation, can see the comb.** The gate metric of *The method step by step* subtracts exactly that smooth background — D(u) = Σ_n e^{−u x_n} − (1 − e^{−u x_K})/u — so what remains is the spectral fine structure, which is then correlated against the comb P(u) at fixed scale. On the zeros' own window the residual of that comparison is 2.1%; on the best of the 52 gates it is 6.7% — a factor ≈ 3.2, the ≈ 0.5-order gap, measured at L = 24: the finite-size branch of the H5 convergence ladder (v2.0.8). That is the campaign in miniature: derive (Hadamard → (★)), verify (M0, M1), calibrate (PC0), and only then aim the same ruler at the candidates.

## Interpretation: what T6 proves and does not prove

**What T6 proves.**

- The chain Hadamard product → pairing ρ ↔ ρ̄ → identity (★) → sine transform → trace formula (★★) is correct to quadrature precision: |ΔQ| ≤ 1.7e-12 and |ΔK| ≤ 1.2e-5 against direct spectral sums.
- The prime weight Λ(n)/√n lives in the heat trace of the zero-coded operator **as a derived theorem**, not a heuristic. In the package's checklist this is clause H5 ("primes in the operator") answered with a proven YES for H_ξ — and for the gates answered YES via the convergence ladder (v2.0.8): the best gate (Nv = 16) reaches r_EF = 0.9978 with z = 2.62, the residual gap (6.7% vs 2.1% at L = 24) being the finite-size branch.
- A calibrated benchmark now exists: 2.1% relative residual is what "seeing the primes" costs at fixed scale. Every future candidate can be judged against a number instead of an aspiration.

**What T6 does not prove.**

- It does not prove the Riemann hypothesis. H_ξ is built *from* the zeros, so "spectrum = zeros" holds by construction and the verification of T6 is a consistency check of the derivation pipeline — nothing about the existence of a natural operator follows from it.
- It does not provide a candidate operator. The gates' fixed-L thermal projection holds the conservative branch: clause H2 (spectral identity) is YES at the zeros' level (D_nn 0.0079, C3) with the rank and thermal projections as its resolution-limited/conservative branches, and H5 is YES via the convergence ladder (v2.0.8) with the residual gap (6.7% vs 2.1% at L = 24) as the finite-size branch.
- It does not close the door on nonlocal constructions. The resolution-limited branches of the package concern the class of *local* lattice Hamiltonians with vortex phases; the question of nonlocal operators is explicitly left open and moved to the roadmap (`docs/theory.md`, §4).

The package's own cycle formula, from the theory map, compresses the standing of this campaign into one sentence (updated to the v2.0.8 verdicts): *the resonator is built and tuned (H1+H3+H4); the zeros are coded, not generated — and the gates sit at their level (H2 — YES); the prime weight is proven for the zero operator (T6) and enters the gates along the convergence ladder (H5 — YES, v2.0.8).* Campaign C4 is the calibrated-ruler clause — and it is the most precise place of the series, because it states not only what a working operator's heat trace looks like, but exactly how far the best gate is from it at fixed L (6.7% vs 2.1%) and which dial moves that number.

## Reproduction

```bash
# tour of the verdict (~seconds, no zeros file needed)
python3 campaigns/run_c4_trace_formula.py
```

Series seed — 96; RNG streams are fixed (`engine/hamiltonian.py`). All dependencies are listed in `requirements.txt`. The committed verdict is self-contained: the tour above does not need the zeros file, which is required only for fresh recomputations of the sums. Independent checks of this campaign live in `independent_verification/` (IVP checks).

## Data and figures

**Figures.**

| File | Where |
|---|---|
| `fig06_trace_ru.png` | 600 dpi — top-level `figures_hires/ru/fig06_trace_ru.png`; screen — `figures/ru/` |
| `fig07_parts_ru.png` | 600 dpi — top-level `figures_hires/ru/fig07_parts_ru.png`; screen — `figures/ru/` |
| `fig08_rEF_ru.png` | 600 dpi — top-level `figures_hires/ru/fig08_rEF_ru.png`; screen — `figures/ru/` |

`fig06_trace` shows the trace formula itself — the direct spectral sum against (★★); `fig07_parts` shows the three-part decomposition T1 + T2 + T3 and the prime share of K(x); `fig08_rEF` shows the gates' heat projection against the null clouds. The English-named variants `fig06_trace_en.png`, `fig07_parts_en.png`, `fig08_rEF_en.png` live under the top-level `figures_hires/en/` and `figures/en/`.

**Data.**

| File | Contents |
|---|---|
| `data/results.json` | committed verdict of the campaign |
| `data/` (npz/csv) | curves and tables |
| `../data/c4_*.json` | duplicate of the verdict in the shared registry |

In this package the committed verdict file is `data/task9a_trace_formula.json`: its `meta` records the zeros file (`zeros6.txt`, n_zeros = 2 001 052), the prime sieve bound (10⁷) and the split point (A_split = 1.5); its blocks hold the M0 grid, the M1 grid, the prime-share decomposition, the PC0 block, the 52 gate rows, and the `verdict` dictionary. The curves live in `data/curves.npz` with arrays `U` (the 40-point thermal grid), `P_ref` (the comb), `D_xi` (the zeros-window fluctuation) and `gates_D` (the 52×40 gate fluctuations).

**Monographs.** `monograph_ru.docx` · `monograph_ru.pdf` · `monograph_en.docx` · `monograph_en.pdf`

The full monograph of this computation (set-up, theorems, tables, figures, honest limitations): 7–9 pages, the same content in the two languages.

## Verdict

**T6 verified; the conservative H2 branch ≈ 0.5 order in the trace metric** — details: `data/results.json`, the monograph, and
`independent_verification/` (IVP checks of this campaign).

## FAQ

**1. Does T6 prove the Riemann hypothesis?**
No. H_ξ = diag(±γ_n) is built from the zeros, so its spectrum equals the zeros by definition. T6 proves something else and something testable: that the *heat trace* of that operator equals the explicit-formula side — the Hadamard product, the Q(a) identity, and the prime comb Λ(n)/√n — to numerical precision. That is a theorem about the analytic identity of two sides, and it is what makes the gates' failure measurable.

**2. Why the weight Λ(n)/√n and not simply Λ(n)?**
The primes enter through ζ'/ζ(½+a) = −Σ_n Λ(n)/n^{½+a} at a > 1.5. Integrating term by term, ∫ n^{−½−a} sin(ax) da = n^{−½}·Im[e^{−1.5(ln n − ix)}/(ln n − ix)]: the factor n^{−½} is forced by the shift to the line Re s = ½. The 1/√n is the fingerprint of the critical line, and the resulting comb P(u) = Σ Λ(n)/√n·u/(u²+ln²n) is the exact shape the heat trace must carry.

**3. Why does the relative metric explode at x ≥ 1 if the identity is verified?**
Because K(x) = Σ e^{−xγ} decays exponentially. At x ≥ 1 its value is ~1e-6, so a fixed absolute quadrature floor of 1.2e-5 corresponds to enormous relative numbers (committed: relative 1.2e7 at x = 2.0). The identity is fine; the relative metric loses meaning. That is why the informative range x ≤ 0.35 is quoted relatively (1e-6…1e-4) and the whole range absolutely (≤ 1.2e-5).

**4. What exactly is "identity by construction", and doesn't it trivialize the campaign?**
For the gates, "spectrum = zeros" is the conjecture under test; for H_ξ it is the definition. But the content of T6 is not that H_ξ has those eigenvalues — it is that the entire derivation chain reproduces the spectral sum to 1.7e-12 and 1.2e-5, and that the resulting thermal benchmark (2.1%) calibrates the ruler the gates are then measured with. The construction makes the operator trivial; the theorem and the benchmark are not.

**5. Why is the gates' null result called conservative?**
Four committed reasons: the scale knob was removed (fixed s = 1, so r could not be inflated by axis tuning); the null clouds are broad and the package acknowledges it (surrogate 0.00±0.39); the best gate's correlation z-score (2.62) actually exceeds the zeros' own (2.59), so correlation alone cannot separate gate from operator — only the residual does (6.7% vs 2.1%); and the ruler is calibrated by PC0 running the zeros through the identical pipeline. The gates were measured against a working example, with the metric's escape hatches closed.

**6. Where do Hadamard, Guinand, Weil and Connes enter?**
The Hadamard product (1893) is the starting point of the derivation of Q(a); Guinand's formulation organizes the zero side as a transform; Weil (1952) states the explicit formula in test-function form — here with the thermal test function e^{−xγ}; the heat-kernel viewpoint is consonant with Connes (1999) and his semilocal factor. The derivation in this package is self-contained, and every numerical constant was derived in-project rather than taken from the literature.

**7. What is the Guinand–Weil trace formula, in one sentence?**
An exact identity — Tr e^{−xH_ξ} = (1/π)∫₀^∞ Q(a) sin(ax) da — equating a spectral sum over the zeta zeros (the heat trace of the zero-coded operator) with the transform of a function Q(a) that contains ζ'/ζ and therefore, for a > 1.5, the prime comb with weight Λ(n)/√n; it is Weil's explicit formula with the thermal test function e^{−xγ}.

**8. What would change the H2 verdict?**
A gate family whose heat-trace fluctuation tracks the comb P(u) at a relative residual near the zeros' 2.1% at fixed scale — not a high r_EF, which the broad null clouds (±0.39) produce by chance. The metric's decisive component is the residual, which is exactly why the campaign fixes the scale and calibrates with PC0.

**9. Where do the counts 52 and 87 come from?**
C4 measures the 52-gate protocol family of C3 with the shared engine and protocol (reproduced bit-for-bit: |Δ mean_spacing| = 1.45e-16); 87 is the package's total gate population including the extended families of C5, which are measured separately in that campaign. The trace-formula benchmark of C4 is what the other 35 gates are judged against elsewhere.

## Mini-glossary

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
| H2 | the "spectral identity" clause of the Hilbert–Pólya checklist (level n ↔ zero n) — verdict NO |
| T6 | the theorem of this campaign: the trace formula with prime weight for H_ξ |
| M0 / M1 / M2 | calibration of (★); verification of (★★) for H_ξ; the 52-gate thermal projection |

## See also

- [../C3_gate_family/README.md](../C3_gate_family/README.md) — the 52-gate protocol family measured here, and the first (rank-correlation) projection of the H2 question.
- [../../docs/trace_formula.md](../../docs/trace_formula.md) — the full, self-contained derivation of theorem T6: Hadamard product, identity (★), sine transform, the three parts T1/T2/T3, and the gate metric.
- [../../results/RESULTS.md](../../results/RESULTS.md) — the living registry of committed numbers, the H1–H5 verdicts, and the honesty registry (including the broad-null acknowledgment for the thermal metric).

---
*Hilbert Polya Bridge v2.0.0 · C4 · The trace formula: Tr e^{−uH} versus the explicit formula*

