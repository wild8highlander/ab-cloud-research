# Repo-wide GOE/GUE audit — v2.0.3 (2026-10-15)

Third round of the error-purge series (v2.0.1: the Hilbert_Polya D_nn
category error + np.roll bug; v2.0.2: the C3 false data + remaining
«9–10 orders» texts). This round audited **every GOE/GUE formula,
every committed rigidity dataset, and every committed theory-curve figure**
outside Hilbert_Polya, on request: «там такой же ужас… множество ещё ошибок
в формуле гое и гуе».

## Method

Every candidate formula was validated numerically before any edit:

1. **Poisson ground truth** — Δ₃ estimator must return L/15, Σ² must return L.
2. **Direct GUE/GOE matrix simulation** (400 matrices 120×120, analytic
   semicircle unfolding) — decides between candidate theory curves.
3. **Exact closed forms** derived and cross-checked to 1e-8 against the
   sine-kernel integral.
4. **Faithful Python replication of the Julia pipeline** — reproduced the
   committed false arrays *exactly* (proof the replication was correct),
   then quantified the bias on ground truth.
5. **Cross-validation**: two independent pipelines (lab-3d Julia replica and
   the Lean 4 reference re-derivation) agree on the corrected KS distance
   D = 0.031 on the same 5000 zeros.

## The canonical laws (for reference)

| Object | GOE (β=1) | GUE (β=2) |
|---|---|---|
| spacing PDF | (π/2)·s·e^(−πs²/4) | (32/π²)·s²·e^(−4s²/π) |
| spacing CDF | 1 − e^(−πs²/4) | erf(2s/√π) − (4s/π)e^(−4s²/π) |
| ⟨r⟩ (Atas 2012) | 0.5307 (surmise 0.5359) | 0.5996 (surmise 0.6027) |
| P(r) surmise | (27/4)(r+r²)/(1+r+r²)^(5/2) | (81√3/2π)(r+r²)²/(1+r+r²)⁴ |
| Σ²(L) asymptotic | (2/π²)(ln 2πL+γ+1−π²/8) | (1/π²)(ln 2πL+γ+1) |
| Δ₃(L) asymptotic | (1/π²)(ln 2πL+γ−5/4−π²/8) | **(1/2π²)**(ln 2πL+γ−5/4) |

GUE Σ² exact closed form (validated to 1e-8):
`Σ²(L) = L − (2/π²)[πL·Si(x) − ½(1−cos x) − ½(γ+ln x−Ci(x))], x = 2πL`.

## Finding 1 — the GOE surmise shipped as «GUE» in 14 implementations

`1 − exp(−πs²/4)` (and its PDF) is the **GOE** law. It was labeled GUE and
used as the Objection-2 reference in:

| Folder | Files | Fix |
|---|---|---|
| `verification/python/` | 4 | erf-based CDF |
| `verification/julia/` | 3 | PDF fixed (Simpson CDF auto-corrects) |
| `verification/cpp/` | 3 | erf-based CDF |
| `verification/fortran/` | 3 | PDF fixed (Simpson) |
| `verification/go/` | 3 | erf-based CDF |
| `verification/javascript/` | 3 | A&S-7.1.26 erf |
| `verification/rust/` | 3 | PDF fixed (Simpson) |
| `verification/matlab/` | 3 | erf-based CDF |
| `verification/r/` | 3 | erf via `2*pnorm(x√2)−1` |
| `verification/haskell/` | 1 | FFI `erf` |
| `formal/lean4/` | 1 | A&S erf (core-only, no Mathlib) |
| `lab-3d/code/` | 2 | erf-based CDF + PDFs |

Consequence before the fix: on the frozen first 500 zeros the KS test gave
D = 0.1165, p ≈ 0 — **a false rejection of the (true) GUE hypothesis**; the
corrected law gives D = 0.0495, p = 0.168. The v23 Julia reference suite
already used the correct law, which is why its pinned numbers (0.047/0.27)
never matched the folder verifiers — the README's «a language that drifts
from these numbers has a bug» was pointing at the ten folders themselves.

## Finding 2 — wrong Σ²/Δ₃ theory curves (4 implementations)

- Julia `sigma2_gue_theory`: (2/π²)(ln 2πL+γ+1−cos−Ci) — a garbled form,
  1.5–1.7× above the true GUE curve at all L (and not the GOE curve either).
- Julia `delta3_gue_theory`: (1/π²)(ln L+γ−5/4) — wrong prefactor and log
  argument (accidentally crosses the true curve near L≈10).
- Python twins: (2/π²)(ln 2πL+γ−π/2) and (1/π²)(ln 2πL+γ−3/4) — match
  neither ensemble; the Δ₃ form is ~2× too large.

Decided by simulation (GUE 120×120, Poisson-validated estimators):

| L | GUE measured | correct theory | old Julia | old Python |
|---|---|---|---|---|
| 5 | 0.535 | 0.509 | 0.816 | 0.497 |
| 10 | 0.584 | 0.579 | 0.956 | 0.638 |
| 20 | 0.617 | 0.650 | 1.097 | 0.778 |

| L | GUE Δ₃ measured | correct theory | old Julia | old Python |
|---|---|---|---|---|
| 5 | 0.150 | 0.141 | 0.095 | 0.332 |
| 10 | 0.185 | 0.176 | 0.165 | 0.402 |
| 20 | 0.219 | 0.211 | 0.235 | 0.472 |

## Finding 3 — broken measurement estimators (the «false data» source)

The committed `outputs/full_verification_2026-07-31_15-33-39` rigidity data
was produced by structurally broken estimators:

- Julia `sigma2_curve` extrapolated the in-window regression line to the
  window end and took the variance of that endpoint residual. **Poisson
  sanity check: 262 instead of 2 at L=2** (a single tight spacing explodes
  the extrapolation). Committed ζ data: flat ≈ 0.45 nonsense.
- Julia `delta_3_curve` averaged knot-fit residuals over level-locked
  starts: ≈ 8× low on the zeta process.
- Python twins (both) fitted a line to the **cumulative sum of positions**
  (not the counting staircase) — measures density curvature, not rigidity.

All four were rewritten (staircase LSQ on a fine grid for Δ₃; windowed
count variance for Σ²) and validated on Poisson (L/15 and L exactly). One
more subtlety found and fixed during validation: the unfolded zeta process
is **lattice-locked** (uₙ ≈ n + bounded S(t)), so integer-stride window
starts alias the count variance (up to +50% at L=10/20); the stride is now
incommensurate (L/9.7).

## Finding 4 — regenerated committed data (the honest §2a)

Same frozen input (first 5000 zeros of `data/zeros1.txt`, RvM unfolding,
L = 2…20), corrected estimators + theory:

- Δ₃ data: 0.095, 0.124, 0.141, 0.151, 0.157, 0.160, 0.160, 0.160, 0.161,
  0.161 — tracks GUE at small L, **saturates ≈ 0.16** (Berry's rigidity
  saturation for zeros with T ≤ 5448).
- Σ² data: 0.36 → ≈ 0.3 plateau — consistent with the saturation scale
  (1/2π²)·ln ln T + c for T ≤ 5448.
- rel_err Δ₃ **0.972 → 0.126**; rel_err Σ² **0.481 → 0.412**; §2a verdict
  **false → true**; overall **4/6 → 5/6** (only the §1.1 surmise-KS still
  rejects, at n = 5000, as any KS-vs-surmise test eventually does).
- Figures `02_delta3_L` and `03_sigma2_L` regenerated (they previously drew
  the false data against the wrong theory curves).

## Finding 5 — the Lean 4 frozen references were self-consistently wrong

`REF_MAIND = 0.0991866230673718` was *generated by the Python suite* against
the GOE law and then reproduced by Lean against the same wrong law — a
cross-language agreement that validated nothing. Corrected references
(reproduced to 15 digits by an exact Python replication of the Lean
pipeline, then cross-validated against the lab-3d Julia pipeline):

| Constant | Old | New |
|---|---|---|
| REF_MAIND | 0.0991866230673718 | 0.0310483738268406 |
| REF_MAINW2 | 17.604855018865965 | 1.5383040904977836 |
| REF_EMBEDD | 0.13726831918538146 | 0.0702356425520416 |
| REF_EMBEDW2 | 1.1855661605530794 | 0.2059419746153673 |

## Finding 6 — the GUE P(r) ratio law (lab-3d)

`ab_cloud_advanced.py` used (81√3/2π)(r²+r⁴)/(1+r²+r⁴)^(5/2) — integrates
to 2.6 over [0,1] (not 1) and gives ⟨r⟩ = 0.636 after renormalization.
Correct Atas β=2 surmise: (81√3/2π)(r+r²)²/(1+r+r²)⁴ (∫ = 1.000000,
⟨r⟩ = 0.602658). Fixed in `r_ratio_gue_pdfa` and `r_cdf_comparison` (V83).

## Checked and found correct (not touched)

- `abcloud/core.py` (python_clone): all three surmises + ⟨r⟩ constants ✓
- `rpbridge/stats.py`: gue_surmise_cdf (erf form) ✓
- `spinor64_core.py`: wigner_gue_cdf ✓
- `ab_cloud_v23.jl` (both copies): v23.1 already split goe/gue2 surmises ✓
- `AB_CLOUD_ALL_HYPOTHESES.py`: wigner_dyson β=1/2/4 ✓ (incl. GSE
  (2¹⁸/3⁶π³)s⁴e^(−64s²/9π))
- `dirac-lab` tools: GOE/GUE curves in make_extra_figures.py ✓
- `ab_cloud_stats.py` / `ab_cloud_stats_v2.py`: surmises ✓
- `ab_cloud_advanced.py` `sigma2_GUE_high_precision`: exact Simpson of the
  sinc² kernel (was already correct) ✓
- ⟨r⟩ empirical values 0.60271 etc. (spinor64 measurements) — data, not
  theory constants ✓
- The «GUE reference 0.5992(3)» in run reports — an empirical GUE-pool
  reference (canon 0.5996); verdicts unaffected either way; documented,
  not churned.

## Reproduction

- Validation harness: `scripts/` of the fix series (Poisson/GUE ground
  truth, Julia-pipeline replication, closed-form checks).
- Data regeneration: the committed §2a numbers are byte-reproducible by
  running the **fixed** `lab-3d/code/ab_cloud_3d.py` estimators on
  `lab-3d/data/zeros1.txt[:5000]` with the RvM unfolding — the regeneration
  script imports the fixed module, so committed data = fixed code output.
- Lean references: exact Python replication of `Zeta.spacings` /
  `ksStatistic` / `cvmStatistic` reproduces both the old (wrong-law) and
  new (correct-law) values to 15 digits.
