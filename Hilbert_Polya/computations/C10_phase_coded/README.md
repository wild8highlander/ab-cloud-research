<!-- AB-ENRICHED:v1 · sub -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venice&height=48&color=0:a78bfa,100:05060f&section=header" alt="" width="100%"/>

**🧭 [⬆ computations/](../README.md) · [🏠 Root README](../../../README.md)**

</div>
# C10 · Phase coding with hard co-location (R2, T12)

> **🧭 Navigation:** [computations/](../README.md) · [Hilbert_Polya/](../../README.md) · [Root README](../../../README.md)

<p align="center"><img src="../../assets/illustrations/ill_pixel_encoding.png" width="640" alt="Prime phases painted exactly onto the lattice shutters"/></p>

<p align="center"><img src="../../assets/avatars/hp_cast_strip.svg" width="760" alt="Bridge avatar cast"/></p>
<p align="center"><em>The phase painter's bench: the primes are written onto the shutters with machine-zero precision — and the spectrum, politely, does not look.</em></p>

> Gate configurations OBLIGED to satisfy (Φ_p,Φ_q) ≡ Φ_pq: site-linked phase overlay Φ_p = 2π{β ln p}. T12 classification: additive systems = β·ln p; {0,π}-valued systems (χ4) are gauge-trivial.

[← Back to the main README](../../README.md)

## The question

Version 1 established two facts that do not fit together comfortably. The prime-flow co-location kernel is exact — the identity (Φ_p,Φ_q) ≡ Φ_pq held to max ΔE = 1.35e-14 (T4, C6) — and the ψ-ladder built from it knows the zeros (corr = +0.972); yet every lattice gate stayed in the null zone of every prime metric. The stitching problem (roadmap R2) is whether some *hardened* version of the coding — imposed not approximately but as an exact algebraic constraint on the lattice itself — can force the spectrum to notice the primes.

C10 hardens the coding to its limit. The phase system Φ_p = 2π{β ln p} is completely additive, because ln p + ln q = ln pq and the fractional parts recombine modulo 1; the character system Φ_p = π·χ4(p) is completely multiplicative in the same sense. The co-location condition (Φ_p,Φ_q) ≡ Φ_pq is therefore an identity, not an approximation, for ANY β. Theorem T12 then classifies the survivors: among phase codings, the additive systems Φ_p = β·ln p are irreducible (non-gauge) in the overlay channel, while {0,π}-valued systems (χ4) are gauge-trivial — removable by a gauge transformation, hence invisible in principle. The measurement asks the sharpened question: does the spectrum see a coding that is exact at machine precision and, when non-gauge, irreducible?

## Where it sits in the v2 roadmap

C10 executes **R2** of the v1 roadmap — "the stitching problem: the flow (T4) knows the primes exactly, the ladder knows the zeros (0.972), make one object carry both" — and settles theorem **T12** (the classification of additive phase systems and the blindness of the spectrum). It is the second pillar of the v2 verdict: the coding layer is not what blocks the bridge. Together with C9 (the trace layer is not what blocks it either) it leaves locality as the only surviving suspect, and with C14 it feeds the taxonomy of the GUE attractor that does the erasing.

## Method in brief

- **Part 1 (T12, construction).** The co-location check evaluates the pairwise condition (Φ_p,Φ_q) ≡ Φ_pq over primes and the additive closure over triples, for β ∈ {0, 0.13, 0.23, 0.37, 0.5} in the committed verdict block and for the full gate scan grid; residuals are read in double precision, so "machine zero" means the 2⁻⁵¹ floor (≈ 4.4e-16).
- **Part 2 (measurement).** The phases are applied as a site-linked overlay on the y-links of the 24×24 Hofstadter gate at α = 0.5 (the self-dual line), Nv = 16 vortices, W = 0.5 — fourteen gates in all: eleven β-gates from 0.00 to 0.50 in steps of 0.05, the χ4 system, a random-phase control, and the v1 anchor Nv16 as a regression pin.
- **Metrics.** r_H7 under the v2 unfolded-vs-unfolded convention (64 cyclic shifts for the null), r_EF raw and on detrended fluctuations, the mean spacing ratio ⟨r⟩ and the GUE-class verdict from 40 GUE surrogates. Zeros: internal mpmath cache, n = 800.
- Runtime 5.9 s.

## Results

> Co-location residual 4.4e-16 for ANY β (by construction); the spectrum does not see it: r_H7 ≤ 0.092 over 11 β-values, GUE class unchanged.

Committed co-location residuals (T12 block of `data/results.json`):

| System | Pairwise max resid | Closure max resid |
|---|---|---|
| β = 0.00 | 0.0 | 0.0 |
| β = 0.13 | 4.440892098500626e-16 | 1.78e-15 |
| β = 0.23 | 4.440892098500626e-16 | 2.66e-15 |
| β = 0.37 | 4.440892098500626e-16 | 3.55e-15 |
| β = 0.50 | 4.440892098500626e-16 | 3.55e-15 |
| χ4 | 0.0 | 3.55e-15 |

Gate scan (all fourteen gates are GUE class; ⟨r⟩ stays in the 0.58–0.63 band):

| Gate | β | r_H7 | ⟨r⟩ |
|---|---|---|---|
| PC-beta0.00 | 0.00 | 0.0299 | 0.6277 |
| PC-beta0.05 | 0.05 | 0.0194 | 0.6059 |
| PC-beta0.10 | 0.10 | 0.0444 | 0.6112 |
| PC-beta0.15 | 0.15 | 0.0174 | 0.6019 |
| PC-beta0.20 | 0.20 | 0.0384 | 0.6236 |
| PC-beta0.25 | 0.25 | 0.0863 | 0.6073 |
| PC-beta0.30 | 0.30 | 0.0678 | 0.6038 |
| PC-beta0.35 | 0.35 | 0.0923 | 0.6054 |
| PC-beta0.40 | 0.40 | 0.0073 | 0.5803 |
| PC-beta0.45 | 0.45 | 0.0286 | 0.5796 |
| PC-beta0.50 | 0.50 | 0.0129 | 0.5840 |
| PC-chi4 | — | 0.0299 | 0.6277 |
| PC-random-control | — | 0.0363 | 0.5804 |
| v1-anchor Nv16 | — | 0.0294 | 0.6229 |

The explanatory pattern is double. First, the coding is perfect and provably so: at β = 0 the co-location residual is literally zero, and for every other β it equals 4.440892098500626e-16 — one double-precision ulp — while the closure residuals stay below 3.6e-15. Second, the spectrum does not care. The largest rank correlation over the eleven β-gates is 0.0923 (at β = 0.35), whose uncorrected p_r = 0.0154 dies under any multiplicity correction across fourteen gates; everything else lies between 0.007 and 0.086, and the GUE class is unchanged everywhere. The most telling number is the χ4 row: PC-chi4 reproduces the β = 0.00 gate to twelve significant digits in r_H7 (0.0298948595933) and to thirteen in r_EF raw (0.951401720894) — the spectrum literally cannot distinguish the {0,π} character coding from no coding at all, which is the gauge-triviality of T12 made visible in data. The random-phase control behaves like the coded gates (0.0363), confirming that the null zone is not a signature of the primes but the default behaviour of the attractor.

## Why it matters (spectral blindness)

<p align="center">
  <img src="../../assets/avatars/hp_polya.svg" width="110" alt="Pólya"/>
  <img src="../../assets/avatars/hp_agent_lyra.svg" width="110" alt="Agent Lyra"/>
</p>
<p align="center"><em>Pólya: "We painted the primes on every site, exactly." Lyra: "And the GUE attractor repainted the picture in its own grey."</em></p>

This campaign closes the softest remaining loophole in the v1 verdict. One could argue that C6's codings failed because they were approximate; C10 shows that even a coding that is *exact by construction*, imposed site-by-site on the lattice, cannot push the spectrum out of the GUE universality class or toward the zero comb. Universality erases hard codings, not just soft ones — the attractor is an eraser with no exceptions. The constructive half of T12 matters as much as the negative half: it tells future designers which overlays are gauge-redundant (the {0,π}-valued, χ4-like systems — never test them again) and which are irreducible (the additive β·ln p systems — tested here, still null). After C10 the stitching problem is not abandoned, but it is rerouted: the phase channel alone cannot carry the primes into the spectrum, which is exactly why the v3 roadmap (N3) tries the index route of C11 instead of another overlay.

## Reproduction

```bash
python3 campaigns/run_c10_phase_coded.py
```

Fresh runs are self-contained: the zeta zeros come from the internal
mpmath cache (`../../data/zeros/`), no external files. Runtime: seconds to
minutes (C12 is segmented; see `campaigns/run_c12_band5000.py`).

Top-level quick start (v2 list in the main README): `python3 campaigns/run_c10_phase_coded.py`.

## Data and figures

| File | Where |
|---|---|
| `fig18_coloc_{ru,en}.png` | this folder's `figures/{ru,en}/`; 600 dpi mirrors — top-level `figures_hires/{ru,en}/fig18_coloc_{ru,en}.png` |

| File | Content |
|---|---|
| `data/results.json` | committed verdict |
| `data/*.npz` / `*.csv` | curves and tables |

In this campaign folder the committed payload is `data/results.json` (co-location residuals, the fourteen-gate table with r_H7, r_EF, ⟨r⟩ and GUE flags, and the bilingual verdict) together with `data/gates_table.csv` (the same gate table in flat form).

## Verdict

See `data/results.json` (verdict, RU+EN), the v2 monograph
(`../../monograph/v2_volume/`) and `../../independent_verification/` (IVP11–18).

Committed verdict (EN, verbatim): "Hard co-location (Φ_p,Φ_q) ≡ Φ_pq holds by construction at machine zero for any beta (T12); the spectrum does not see the coding: r_H7 in the null zone, GUE class unchanged — universality erases even hard codings." The statement and proof of T12 (additivity ⇒ co-location; the gauge classification) are in `../../monograph/theorems_v2_volume/`.

## FAQ

1. **What is "hard" co-location, as opposed to C6?** In C6 the co-location kernel was verified as an identity of energies to 1.35e-14; here the phase system itself is *defined* so that (Φ_p,Φ_q) ≡ Φ_pq is an algebraic identity — the lattice is obliged to satisfy it, and the committed residuals (0.0 at β = 0, 4.4e-16 otherwise) confirm it at machine level for any β.
2. **If the coding is exact, why is the spectrum blind?** Spectral statistics are invariant under the kind of site-linked phase overlay used here up to universality: the overlay reshuffles eigenvectors while the level repulsion of the GUE class averages out the Λ-comb. The result is consistent with C6/M3 and with C14's taxonomy — the attractor erases everything but symmetry.
3. **What is gauge-trivial about χ4?** A {0,π}-valued phase on bonds can be removed by a diagonal gauge transformation; T12 classifies such systems out of the coding game. The data agrees: PC-chi4 and PC-beta0.00 agree to twelve significant digits in r_H7 — the two "different" codings are the same spectrum.
4. **Does any phase coding move the needle at all?** Only the additive systems Φ_p = β·ln p are non-gauge (T12), and their eleven gates were measured here: max r_H7 = 0.092, inside the null zone. The phase channel is closed; the surviving routes are the index bridge (C11) and nonlocal constructions (C9).

## See also

- [C6 · Prime flow (T4)](../C6_prime_flow/README.md) — the co-location kernel (max ΔE = 1.35e-14) and the ψ-ladder (+0.972).
- [C9 · Nonlocal trace (T11)](../C9_nonlocal_trace/README.md) — the trace layer is innocent too.
- [C14 · Anomaly hunt (T16)](../C14_anomaly_hunt/README.md) — the taxonomy of the attractor that does the erasing.
- `../../results/ROADMAP.md` — R2 as written and as executed; N3, the index route.
- [Back to the main README](../../README.md).

---
*Hilbert Polya Bridge v2.0.0 · C10*

---

<!-- enriched-r3 -->

This folder documents one **campaign of the Hilbert–Pólya Bridge series**. The computational kernel is shared — every campaign builds its Hamiltonians and spectra through [`engine/`](../../engine/README.md) — while the committed verdicts for all campaigns live in [`data/`](../../data/README.md). This page narrates the campaign's question, method and measured outcome; the numbers it quotes are frozen in the evidence base and are reproducible bit-for-bit. The campaign map of the whole series is in [`computations/`](../README.md).

## Folder contents

| File | Size | What it is |
|---|---|---|
| `anim_coloc.gif` | 346 KB | animation |
| `anim_coloc.mp4` | 197 KB | video |

**Subfolders:** `data/` · `figures/`


**Where next:** [engine/](../../engine/README.md) · [data/](../../data/README.md)

<div align="center">

<img src="../../../assets/svg/divider-violet.svg" alt="—" width="100%" height="12"/>
<sub>⚡ Part of <a href="../../../README.md">AB-Cloud Research</a> — numbers are verbatim from the unified registry; no result on this page is a claim about the Riemann hypothesis · <a href="../README.md">⬆ parent section</a></sub>

</div>
