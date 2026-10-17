# Bridge Explorer (Streamlit)

<p align="center"><img src="../assets/illustrations/ill_montage_bench.png" width="600" alt="The explorer bench: handles, spectrum and verdicts of the resonator side by side"/></p>

<p align="center"><img src="../assets/avatars/hp_agent_vera.svg" width="110" alt="Agent Vera, the interactive demonstrator"/></p>

*The interactive v2.0 companion to the committed verdicts — turn the
handles, watch the resonator rebuild, and see the three projections of the
H2 question react in real time.*

[← Back to the main README](../README.md)

## What this folder is

The explorer is the **hands-on instrument** of the package: a Streamlit
application (plan item 9) that turns the static evidence of `data/` and
`computations/*/data/` into a live laboratory. It is deliberately
conservative in what it claims: the committed verdicts are replayed
verbatim, and every live metric is computed by exactly the same protocol
the campaigns used — so what you see interactively is always comparable
with what the theorems and verdicts state.

The app identifies itself as the *Hilbert–Pólya Bridge Explorer v2.0* and
is wired to the same engine kernel as the campaigns: the live gate tab
rebuilds the resonator through `engine/` and `eigvalsh`, while the verdict
tabs read the committed JSONs of C9–C16 from their per-campaign
`computations/<ID>/data/` folders.

```bash
pip install streamlit
streamlit run explorer/streamlit_app.py
```

Three tabs:

1. **Live gate** — turn the handles (Nv, q, W, α, mass, δα, phase-coding β)
   → `eigvalsh` rebuilds the 576×576 resonator and re-measures the three
   projections of the H2 question (rank r_H7, heat r_EF fluct, statistics class
   ⟨r⟩) against the internal zero cache, with the positive controls stated.
2. **Verdicts C9–C16** — the committed campaign verdicts (RU/EN) and metadata.
3. **Bridge map** — the v2.0 map: eight new campaigns, eight new theorems.

Honesty discipline is inherited from v1: the explorer replays committed
data; every live metric is the same protocol as the campaigns
(unfolded-vs-unfolded convention, internal mpmath zero cache, PC0′ = 1.000
for isospectral twins).

## What you will see, tab by tab

- **Live gate.** The seven handles are exactly the dimensions of the
  resonator described in `engine/` and `docs/theory.md`: the vortex count
  Nv and charge q (the C3 protocol), the on-site disorder W, the flux
  α (the self-dual line ½), the staggered mass and the flux shift δα (C5
  handles), and the phase-coding β of C10. Each change triggers a fresh
  `eigvalsh` diagonalization of the 576×576 Hermitian matrix; the three
  projections — rank correlation r_H7, the heat projection r_EF on
  detrended fluctuations, and the statistics class ⟨r⟩ — are re-measured
  against the internal mpmath zero cache. The positive controls are shown
  alongside, so a visitor can verify the scale of the null: PC0′ demands
  r = 1.000 from an isospectral twin, and the GUE null cloud marks where
  "nothing special" lives.
- **Verdicts C9–C16.** The committed verdict JSONs of the eight v2
  campaigns — under `computations/`: `C9_nonlocal_trace`, `C10_phase_coded`,
  `C11_alpha_third`, `C12_band_5000`, `C13_blind_families`,
  `C14_anomaly_hunt`, `C15_dirichlet`, `C16_qinfo` — presented with their
  metadata in both languages. Nothing is recomputed here: this tab is a
  reader for `data/`-style evidence.
- **Bridge map.** The one-screen v2.0 map: the eight new campaigns
  C9–C16 and the eight new theorems T11–T18, from the nonlocal primitive
  (T11) through phase-coding blindness (T12), the α = 1/3 zero modes
  (T13), the T = 5000 band (T14), the blind families (T15), the anomaly
  hunt (T16), the Dirichlet trace formula (T17), to the qinfo layer
  (T18).

## How to use it

```bash
# from the repository root
pip install streamlit
streamlit run explorer/streamlit_app.py
```

- The Makefile exposes the same entry point as the v2 target:
  `make v2-explorer` runs the command above.
- Start with the **Bridge map** tab if you are new: it orients you in
  C9–C16 ↔ T11–T18 before you touch any handle.
- In the **Live gate** tab, reproduce a committed configuration by setting
  the handles to the values recorded in the verdict JSONs; the measured
  triplet (r_H7, r_EF, ⟨r⟩) must agree with the campaign's protocol.
- Compare the live null clouds with the positive controls: the distance
  between "a gate" and "an isospectral twin" *is* the measured resolution
  limit of the rank metric.
- The explorer is a viewer, not a verdict factory: fresh verdicts are
  produced by the campaign scripts and committed, never by the app.

## Conventions

- The explorer inherits the v2 metric conventions: unfolded-vs-unfolded
  windows, r_EF on detrended fluctuations, the internal mpmath zero cache
  (no external data files), and PC0′ = 1.000 for isospectral twins.
- All live numerics flow through `engine/` — the single source of the
  resonator — so the app cannot drift from the campaigns by construction.
- Verdict metadata is shown in RU/EN, matching the bilingual campaign
  folders; no number is reformatted or rounded before display.

## See also

- [../README.md](../README.md) — the main README and the v2 verdict table
- [../engine/README.md](../engine/README.md) — the kernel the live gate calls
- [../data/README.md](../data/README.md) — the evidence the verdict tab replays
- [../docs/v2/README.md](../docs/v2/README.md) — the v2.0 documents and metric conventions
- [../computations/](../computations/) — the per-campaign folders behind tabs 2 and 3
