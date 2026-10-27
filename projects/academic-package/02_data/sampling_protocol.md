# Sampling protocol

The statistical layer of the programme samples **vortex configurations** of
the AB cloud and **gate families** of the bridge. Protocol (mirrored from the
sources; parameters in `config.yaml`):

1. **Vortex ensembles** (V-series, D-series): $N_v \ge 8$ vortices per
   realization, $n_{\mathrm{realizations}} = 400$ (production) / 8 (test),
   seed = 42; statistics computed over the bulk band with the boundary
   convention documented per source.
2. **Gate families** (C-series): 52 gates (C3) → 87 (C5 extended) → +20
   blind (C13); every gate is a pre-registered perturbation of the base
   operator, not a search.
3. **Blind zero reading** (E17): windows fixed ($T \le 1000$) before runs;
   two engines with independent code paths.
4. **Pre-registration discipline**: GUE/GOE/GSE windows fixed in
   `config.yaml: gue_windows`; no post-hoc re-tuning.

The ζ-zero inputs themselves are **frozen datasets, not samples**: the
byte-identical copies the suite reads live in `frozen/` (50k / 100k /
13 661 / high-T blocks); the two large Odlyzko bulk tables are pinned by
checksum under the `external/` link-and-notes policy. Nothing in this
package re-samples, re-truncates or re-derives them.

The unified package itself samples nothing: it consolidates. The protocol
above documents how the numbers it carries were obtained.
