# C14 · Anomaly hunt outside the GUE attractor (T16)

<p align="center"><img src="../../assets/illustrations/ill_stats_ladder.png" width="640" alt="A census of 121 configurations across the GUE attractor"/></p>

<p align="center"><img src="../../assets/avatars/hp_cast_strip.svg" width="760" alt="Bridge avatar cast"/></p>
*The auditors take the census: 121 configurations sorted by their statistics — none by their rank against the zeros.*

> Systematic scan of 121 configurations (protocol family × Nv,q,W,α + blind representatives). Honest taxonomy, ⟨r⟩-criterion.

[← Back to the main README](../../README.md)

## The question

C8 established the ladder — Poisson for the clean lattice, GUE once vortices are present (⟨r⟩ = 0.60 at Nv ≥ 8) — but on a designed ladder, not the whole space. C14 asks the adversarial version: is there *any* configuration — a far corner of the (Nv, q, W, α) grid, a degenerate case, a blind representative — that escapes the GUE attractor, and does that escape route correlate with the zeta zeros? The protocol is built to catch a sensation: every configuration is classified by its spacing statistics and checked against the zero window. An anomaly only matters if it also codes the zeros.

## Where it sits in the v2 roadmap

This campaign settles **Theorem T16** and completes the two-sided universality check: C13 varies the *design* and finds no exit from the null zone; C14 varies the *statistics* and finds no exit from the attractor. Its answer to the roadmap question "is there a way out of universality?" is: none — the basin is structured.

## Method in brief

The scan covers 121 configurations: the protocol family P swept over Nv, q, W and α, plus the blind representatives of the C13 families (BF1–BF5). The ⟨r⟩-criterion is fixed before the scan: a configuration is flagged if **|r_mean − 0.5996| > 0.05 OR KS_p(GUE) < 0.01** — its mean gap ratio strays from the GUE attractor value by more than 0.05, or a Kolmogorov–Smirnov test rejects the GUE spacing law at the 1% level. Each row also carries r_H7 against the 800 internal-cache zeros, so statistics and coding are measured on the same objects. The committed run takes 11.4 s.

## Results

97 GUE / 18 integrable (Nv=0, expected per C8) / 6 intermediate (weak vortex). No rank outliers (|r_H7| ≤ 0.153). The attractor is global; its basin is structured.

The raw scan raises 24 flags; the taxonomy resolves them without residue. Eighteen are the clean-lattice column itself: Nv = 0 is integrable, Poisson, exactly as C8 predicted (the ledger records `n_poisson_expected_Nv0 = 18`). Six are weak-vortex configurations (four at Nv = 2, two at Nv = 8) whose mean gap ratio drifts to 0.47–0.53 — the *intermediate* shelf between Poisson and GUE, with the borderline KS signature of the quasiperiodic BF2 family at the criterion threshold. The remaining 97 are GUE. The rank projection seals the taxonomy: across all 121 configurations the largest |r_H7| is 0.153, the alarm line |r_H7| > 0.35 is never approached, and the six intermediate cases keep |r_H7| ≤ 0.053.

<p align="center"><img src="../../assets/avatars/hp_agent_vera.svg" width="110" alt="Agent Vera"/></p>

## Why it matters

Universality is an attractor, not a witness: it erases everything except the symmetry class, so a GUE verdict alone can never certify spectral identity. C14 adds the *map of the basin*: the only ways out of GUE are the integrable limit (no vortices) and the thin shelf at two weak vortices — and neither exit correlates with the zeros. Combined with C13 (new designs cannot leave the null zone), the loop closes: no statistics without vortices, no coding with or without them. The sensation the hunt was built to catch — a configuration outside the attractor whose spectrum remembers the zeros — does not exist in the scanned zoo; the boundary is rigid.

## Reproduction

```bash
python3 campaigns/run_c14_anomaly_hunt.py
```

Fresh runs are self-contained: the zeta zeros come from the internal
mpmath cache (`data/zeros/`), no external files. Runtime: seconds to
minutes (C12 is segmented; see `campaigns/run_c12_band5000.py`).
The committed run completes in 11.4 s.

## Data and figures

| File | Where |
|---|---|
| `fig22_anomaly.png` | 600 dpi — `figures_hires/ru|en/fig22_anomaly_ru|en.png`; copy in `figures/ru|en/` |
| `data/results.json` | committed verdict |
| `data/*.npz` / `*.csv` | curves and tables |

`data/results.json` stores the criterion, the per-configuration records (r_mean, KS statistics and p-values against GUE/GOE/Poisson, nearest ensemble, class, r_H7); `data/scan_table.csv` is the flat 121-row table behind `fig22_anomaly.png`.

## Verdict

See `data/results.json` (verdict, RU+EN), the v2 monograph
(`monograph/v2_volume/`) and `independent_verification/` (IVP11–18).

The committed English verdict reads: *"Scan of 121 configurations: 18 flags are the expected integrable clean lattice (Nv=0, Poisson, consistent with C8); among VORTEX configs anomalies: 6 (borderline KS signature of the quasiperiodic BF2 family, at the criterion threshold); no |r_H7| > 0.35 (max 0.153). The GUE attractor is global for all vortex-carrying configs; no sensation — the universality boundary is rigid."*

## FAQ

**Are the 18 integrable flags a failure of universality?**
No. They are the Nv = 0 clean lattice, integrable by construction; Poisson statistics there are the behaviour C8 already fixed. They are "anomalies" only relative to a criterion calibrated on the GUE attractor.

**What exactly is the ⟨r⟩-criterion?**
A configuration is flagged when its mean gap ratio deviates from the attractor value 0.5996 by more than 0.05, or when a KS test against the GUE spacing law returns p < 0.01 — two independent statistics, one verdict.

**Do the six intermediate cases change the H2 story?**
No. They sit at the weak-vortex edge of the basin (⟨r⟩ ≈ 0.47–0.53), and their rank correlations against the zeros stay at |r_H7| ≤ 0.053. They mark where the basin's boundary *is*, not a way out of it.

**Could an anomaly hide outside the scanned grid?**
T16 is scoped to the extended zoo as scanned — the protocol grid plus the blind representatives, with C13 covering designs beyond the v1 handles. Within that scope the attractor is global; the package reports measured boundaries.

## See also

- [C8 · Statistics ladder](../C8_stats_ladder/README.md) — the Poisson/GOE/GUE ladder and spinor64 (T8, T10).
- [C13 · Blind families](../C13_blind_families/README.md) — the design side of the same two-sided check (T15).
- [C5 · Gates extended](../C5_gates_extended/README.md) — ⟨r⟩ = 0.569–0.633 (mean 0.601) across the six-handle family (v2.0.5 regeneration).
- `docs/v2/overview.md`, `monograph/v2_volume/`, `results/RESULTS.md` (row 28).

---
*Hilbert Polya Bridge v2.0.0 · C14*
