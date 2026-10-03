# `analysis_addendum/` — Post-Processing: Mixture Decomposition and Bootstrap
> The addendum's quantitative core: the effective GUE+Poisson mixture fit, the 500-resample bootstrap of d_GUE, and the two figures embedded in the manuscripts.

_Location: [unpacked/](../../../README.md) › [run_data/](../../README.md) › [run_20260917_080329_m2/](../README.md) › [analysis_addendum/](README.md)_

The pooled ensemble of the parent run (`../README.md`) measured a confrontation distance D = 0.0970 — small, but not zero, and the addendum's task was to account for the residual honestly rather than wave it away. This folder ships the post-processing that did exactly that, and its two JSON summaries are the cited sources for addendum chapter Add.5's numbers.

## The mixture fit (`pooled_mixture_fit_summary.json`)

The analysis decomposes the AB-side spacing distribution into an effective **GUE + Poisson mixture**: a pure GUE spectrum with a Poisson admixture of weight **w* = 0.281** (KS criterion; 0.2465 by the L² criterion). After the decomposition, the residual distance to ζ drops to **0.0241** — which equals, within its own error, the independent **GUE-matrix-versus-ζ calibration floor of 0.0242** measured for a pure GUE matrix ensemble against the same ζ reference. In other words: once the (documented, disorder-sweep-stable) Poisson admixture is priced in, the AB-cloud spectrum is statistically indistinguishable from a pure GUE spectrum in exactly the way the ζ comparison demands. The JSON also archives the differential-CDF extrema (max +0.0969 at s = 0.61; zero crossing s ≈ 1.044), the short-range repulsion fractions (P(s<0.5): AB 18.5% vs ζ 9.4%), and the 500-resample bootstrap of d_GUE with 95% CI [0.0744, 0.0798].

`m3_mixture_fit_summary.json` is the single-realization companion computed for the MODE 3 diagnostics run (`../../run_20260917_084900_m3/README.md`), letting the two runs' decompositions be compared side by side.

## The figures

`fig_add1_w_sweep_en.png` and `fig_add2_mixture_en.png` are the original-resolution English-labelled figures embedded in the monograph, the Academic Essence and both preprints (the preprints carry byte-identical copies with location codes `_P1A`/`_P2A`). Figure 1 is the disorder sweep (the residual is flat in W); Figure 2 is the mixture decomposition itself.

## Complete contents inventory

| File | Size | Description |
|---|---|---|
| `fig_add1_w_sweep_en_BA.png` | 472.0 KB · 3750x2580 | Addendum figure 1 — the disorder (W) sweep: the confrontation distance stays flat as disorder grows (Add.3). |
| `fig_add2_mixture_en_BA.png` | 426.8 KB · 3750x1560 | Addendum figure 2 — the effective GUE+Poisson mixture decomposition; post-fit residual 0.0241 vs the GUE-matrix calibration floor 0.0242 (Add.5). |
| `m3_mixture_fit_summary.json` | 902 B · 47 lines | Single-realization mixture-fit summary for the MODE 3 diagnostics run (companion to the pooled summary). |
| `pooled_mixture_fit_summary.json` | 990 B · 50 lines | Pooled mixture-fit summary: w* = 0.281 KS / 0.247 L2, residual 0.0241, bootstrap CI [0.0744, 0.0798], short-range fractions, differential extrema. |

---
_This README is part of the GitHub edition of the AB-Cloud v23 package (v34). Package overview: [../../../README.md](../../../README.md)._