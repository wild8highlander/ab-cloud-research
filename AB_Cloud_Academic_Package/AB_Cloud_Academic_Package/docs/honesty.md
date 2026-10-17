# The honesty layer

1. `rh_status = certified` — the V13 obligation machine (Lean 4 / Coq)
   states the Riemann-hypothesis conclusion exactly: since v1.2.1 the path
   O01→O12 carries no assumptions (O12 classical; O08/O09/O11 certified
   numerically). The verdict rises to `proven` only via a proof of O11 for
   all n; the formal layer *guarantees the exact accounting*.
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
