# The honesty layer

1. `rh_status = blocked` — the V13 obligation machine (Lean 4 / Coq) keeps
   the Riemann-hypothesis conclusion blocked while analytic prerequisites
   remain assumptions. No numerical result can change this; the formal layer
   *guarantees the blocking*.
2. Every verdict file carries `does_not_prove` — what the result does NOT
   establish. This field is part of the scientific record and must be
   preserved verbatim in derivatives (LICENSE §3).
3. Negative results are first-class: the locality wall (T18), the null
   zone at gates, the failed lattice ζ-correspondences (V1/V3/V6/V16).
4. Numbers are copied verbatim from verdict files — never re-typed,
   never recomputed; disagreements between sources are shown, not resolved.
5. The pre-registration discipline: verdict windows are fixed in
   `config.yaml` before runs and cannot be re-tuned after.

Index of every boundary: [`00_meta/dossier.md`](../00_meta/dossier.md).
