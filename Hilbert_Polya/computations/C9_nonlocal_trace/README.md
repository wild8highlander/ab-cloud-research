# C9 · Nonlocal trace primitive (R1, T11)

<p align="center"><img src="../../assets/illustrations/ill_trace_formula.png" width="640" alt="The Guinand–Weil heat trace carrying the prime weight Λ(n)/√n"/></p>

<p align="center"><img src="../../assets/avatars/hp_cast_strip.svg" width="760" alt="Bridge avatar cast"/></p>
<p align="center"><em>The trace bench: Hilbert supplies the heat kernel, Riemann the zeros, Pólya the operator question — and the five-member family N1–N5 is weighed on a single beam.</em></p>

> Does an operator exist whose heat trace carries Λ(n)/√n BY CONSTRUCTION (directly from Guinand–Weil, not through the lattice)? Family N1–N5: H_ξ control, DCT/QR isospectral twins, Berry–Keating xp, LCM kernel.

[← Back to the main README](../../README.md)

## The question

By Theorem T6 (v1, campaign C4) the heat trace of the zero-coded operator H_ξ satisfies the Guinand–Weil trace formula in heat-kernel form, K(x) = (1/π)∫₀^∞ Q(a) sin(ax) da, and the kernel Q(a) carries the von Mangoldt weight Λ(n)/√n through ζ'/ζ. Among all 87 lattice gates the same comb is provably absent — their heat traces sit in null clouds. C9 asks the question that decides how that contrast must be read: is the prime weight a fragile property of the one object built from zeros, or does it belong to the zero spectrum itself, so that any operator sharing that spectrum inherits it?

If some operator — any operator — carries Λ(n)/√n in its heat trace BY CONSTRUCTION, then the silence of the gates is a statement about what all gates have in common (their locality), not about the trace side of the bridge. The family N1–N5 is designed to settle exactly this:

| Member | Construction | Role |
|---|---|---|
| N1 | H_ξ — eigenvalues γ_1..γ_400, positive branches | positive control PC0'/PC0 |
| N2 | DCT twin — O·diag(γ)·Oᵀ, O dense orthogonal (cosine seed) | isospectral nonlocal twin |
| N3 | QR twin — O·diag(γ)·Oᵀ, O dense orthogonal (QR seed) | isospectral nonlocal twin |
| N4 | Berry–Keating xp, truncated | off-lattice candidate |
| N5 | LCM kernel Λ(lcm(m,n))/√(mn) | prime weight placed in the kernel itself |

## Where it sits in the v2 roadmap

C9 executes **R1** of the v1 roadmap — "nonlocal trace constructions: the T6 lesson applied to candidate operators beyond the lattice" — and settles theorem **T11** (heat-trace uniqueness). It is the first pillar of the v2 verdict *The Operator That Almost Exists*: the primitive with the prime weight in its trace exists and can be made arbitrarily nonlocal at will; what the lattice family cannot supply is a *local* realization of it. Within the volume it works in tandem with C10 (the phase-coding layer is equally blameless) and C13 (fresh local designs stay in the rank branch's null zone), so that the wall is triangulated from three independent sides.

<p align="center">
  <img src="../../assets/avatars/hp_hilbert.svg" width="110" alt="Hilbert"/>
  <img src="../../assets/avatars/hp_riemann.svg" width="110" alt="Riemann"/>
</p>
<p align="center"><em>Hilbert: "If the trace knows the primes without any lattice, stop blaming the trace." Riemann: "My zeros carry the comb wherever they go — the twins merely follow."</em></p>

## Method in brief

- **v2 metric convention — unfolded-vs-unfolded.** The object's unfolded central band is correlated against the unfolded zero window inside one pipeline; the isospectral control is thereby *obliged* to return r_H7 = 1.000 (in v1 the control was a weaker file-vs-file pair). Zero reference: the internal mpmath cache, n = 800 zeros, no external files; zero-window convention k0 = 224; K = 200 matched levels; shift search on the U grid [0.05, 1.0] × 40.
- **r_H7_matched** — rank correlation against the zeros, maximized over the shift grid; null distribution from 64 cyclic shifts (p_r).
- **r_EF** — the heat-trace projection: raw correlation and correlation on detrended fluctuations (the v2 repair for two smooth curves correlating through their shared trend); surrogate null = 64 shifts + 40 GUE surrogates, giving the band ≈ [0.006, 0.387].
- **GUE classification** from the mean spacing ratio ⟨r⟩, decided independently of the coding metrics so that class and coding are never conflated.
- **Built-in trace re-verification.** The T6 identity is recomputed inside the same run on the internal cache: max ΔQ = 1.746e-6, max ΔK = 1.849e-6 (RESULTS.md row 23 rounds this to |ΔK| ≤ 1.8e-6), and the derived-constant control B + C0 closes at 4.36e-7 with C0 = 0.023096 — no constant is fitted anywhere.
- Runtime 5.4 s.

## Results

> N2/N3 twins: r_H7 = 1.000, r_EF(fluct) = 0.999 — the primitive exists; xp and LCM kernel stay in the rank branch's null zones. T11: heat-trace uniqueness ⇒ the open bit-level branch is a wall of LOCALITY, not of the trace.

| Member | r_H7 (matched) | r_EF raw | r_EF (fluct) | Class / reading |
|---|---|---|---|---|
| N1 H_ξ | 1.000 (shift 8.9e-16) | 0.9880 | 0.9986 | isospectral by construction — PC0'/PC0 |
| N2 DCT twin | 0.9999999999999996 | 0.9880 | 0.9986 | isospectral nonlocal; deviation 6.8e-13 |
| N3 QR twin | 0.9999999999999997 | 0.9880 | 0.9986 | isospectral nonlocal; deviation 6.8e-13 |
| N4 xp (truncated) | 0.047 | 0.9994 | 0.838 | null zone on ranks; ⟨r⟩ = 0.992 — not GUE |
| N5 LCM kernel | unfold impossible | −0.910 | −0.959 | degeneracy 0.8; prime weight in the kernel, not the spectrum |

The twins reach the control values because the heat trace is a spectral invariant: conjugation by a dense orthogonal matrix moves eigenvectors and never eigenvalues, so Tr e^(−uH) — and with it the Λ(n)/√n comb inside Q(a) — survives the passage to a spatially dense, maximally nonlocal operator. The measured r_H7 = 1.000 and r_EF(fluct) = 0.999 are therefore not an achievement of the twins but a property of the zero spectrum itself: every member of its isospectrality class inherits the primitive automatically. The two off-class candidates demonstrate the converse. Truncated xp is Poisson-like (⟨r⟩ = 0.992, gue_class = false); its raw heat-trace correlation 0.9994 is precisely the smooth-trend artifact that the v2 detrending was built to remove — on fluctuations it drops to 0.838, and its rank correlation with the zeros collapses to 0.047, deep inside the null zone. The LCM kernel writes Λ(lcm(m,n))/√(mn) directly into the matrix entries and produces a spectrum so degenerate (degeneracy 0.8) that unfolding — the entry ticket to every metric in this package — is impossible; its fluctuation correlation is even negative (−0.959). Prime weight in a kernel does not propagate to prime weight in a spectrum.

## Why it matters (the locality wall)

In v1 the H2 verdict rested on three projections of one gap: rank correlation (C3, surrogate-null level), the ψ-ladder (C6, null zone), and the heat trace (C4, ≈0.5 order). A skeptic could still object that the heat-trace projection was merely weak — that the ruler lacked the dynamic range to register a prime weight even if some construction carried one. C9 removes that escape route. The isospectral twins drive the very same metric to r_H7 = 1.000 and r_EF(fluct) = 0.999 — the PC0 ceiling — while remaining utterly nonlocal (dense conjugation, no meaningful site structure at all). The metric therefore has full dynamic range, and the gates' residence in the null clouds is a property of their shared architecture, not of the ruler.

That is Theorem T11, heat-trace uniqueness: the Λ(n)/√n comb belongs to the zero spectrum, so an operator that misses the comb is missing the spectrum — and the gate family demonstrably misses it. The wall through which no candidate has passed is the wall of LOCALITY. Practically this reroutes the search: purely local, architectural modifications (C13's blind families) are pre-failed by this result; the directions that survive are index-based (C11's zero modes, roadmap items N1/N3) or avowedly nonlocal, outside the lattice picture altogether.

## Reproduction

```bash
python3 campaigns/run_c9_nonlocal_trace.py
```

Fresh runs are self-contained: the zeta zeros come from the internal
mpmath cache (`data/zeros/`), no external files. Runtime: seconds to
minutes (C12 is segmented; see `campaigns/run_c12_band5000.py`).

Top-level quick start (v2 list in the main README): `python3 campaigns/run_c9_nonlocal.py`.

## Data and figures

| File | Where |
|---|---|
| `fig17_nonlocal.png` | 600 dpi — `figures_hires/ru|en/fig17_nonlocal_ru|en.png`; copy in `figures/ru|en/` |

| File | Content |
|---|---|
| `data/results.json` | committed verdict |
| `data/*.npz` / `*.csv` | curves and tables |

In this campaign folder the committed payload is `data/results.json` (the N1–N5 table, the trace re-check, the null statistics and the bilingual verdict) together with `data/curves.npz` (rank-correlation and heat-trace curves for the five family members).

## Verdict

See `data/results.json` (verdict, RU+EN), the v2 monograph
(`monograph/v2_volume/`) and `independent_verification/` (IVP11–18).

Committed verdict (EN, verbatim): "The primitive exists: any isospectral nonlocal operator carries Λ(n)/√n in its trace by construction (r_EF at PC0 level, r_H7 = 1); off-class candidates (xp, LCM kernel) stay in the rank branch's null zones. The open bit-level branch is a wall of LOCALITY, not of the trace (T11)." The full statement and proof sketch of T11 live in `monograph/theorems_v2_volume/`; the independent protocol re-derives the twin construction and the trace re-check as IVP11–18.

## FAQ

1. **If an operator with the prime trace exists, is the Hilbert–Pólya programme solved?** No. The twins carry the trace *because* they are isospectral to the zero-coded H_ξ — their spectra are the zeros by fiat. The programme asks for an operator that *generates* the zeros; T11 says the trace side of that problem is already solved and identifies locality as the unsolved part.
2. **Is the twin result circular?** No. N2/N3 are constructed by conjugating diag(γ) with dense orthogonal matrices; the heat trace is a spectral invariant, so the identity for them is a theorem-level consequence measured at machine precision (isospectral deviation 6.8e-13), not a fit — and the two off-class candidates, which are *not* built from zeros, fail exactly as T11 predicts.
3. **What exactly does "heat-trace uniqueness" (T11) assert?** That the Λ(n)/√n weight in the heat trace is a certificate of the zero spectrum: any operator whose heat trace carries the comb is isospectral to H_ξ, and conversely any isospectral operator carries the comb. The gates fail the forward direction of the certificate.
4. **What changed relative to v1's PC0?** Three things: the control is now an unfolded-vs-unfolded pair inside one pipeline (obliged to give exactly 1.000), r_EF is evaluated on detrended fluctuations rather than raw curves, and the whole T6 identity was re-verified on the internal zero cache (max ΔK = 1.849e-6) so that no external file enters the verdict.

## See also

- [C4 · Trace formula (T6)](../C4_trace_formula/README.md) — the parent identity, abs ΔK ≤ 1.2e-5 in v1.
- [C3 · Gate family](../C3_gate_family/README.md) — the 52-gate measurement in which the wall was first quantified.
- [C13 · Blind families (T15)](../C13_blind_families/README.md) — twenty gates with new designs, same null zone of the rank branch.
- `../../docs/trace_formula.md` — the full T6 derivation (Hadamard product → Q(a) → sine transform).
- `../../results/ROADMAP.md` — R1 as written and as executed.
- [Back to the main README](../../README.md).

---
*Hilbert Polya Bridge v2.0.0 · C9*
