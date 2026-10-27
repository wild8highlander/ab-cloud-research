<!-- AB-ENRICHED:v1 · sub -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venice&height=48&color=0:ff2ec4,100:05060f&section=header" alt="" width="100%"/>

**🧭 [⬆ core_spectrum/](../README.md) · [🏠 Root README](../../../../README.md)**

</div>
# data/ — committed verdicts of the V1–V19 series

Each campaign publishes a verdict `vNN_verdict.json` (for example,
`v01_verdict.json` … `v19_verdict.json`; plus a `meta` block with the
date, time and package version). The campaign tours
(`campaigns/run_v*.py`) read these files; a fresh recomputation is done
by `scripts/compute_all.py`. Campaigns V16–V19 additionally commit raw
artifacts: `v16_rows.csv`, `v17_trajectories.csv`, `v18_pong_log.csv`,
`v19_stitch_log.csv`.

## The only external data file

- `zeta_zeros_50000_embedded.txt` — 50,000 real ζ zeros (the Odlyzko
  table, extracted from the parent repository ab-cloud-research).
  SHA-256:
  `2cf6a84e9da69ee27cf165f03bbc3b8bb2e33fa9afdaeba4ecb529aea9509db6`.

## Rules

1. Verdicts are committed; a mismatch of a fresh run against the
   committed verdict is a release stopper (test_repro).
2. The zero file ships inside the package — the package is
   self-contained and works offline.
3. No third-party research code is imported.
4. The JSON verdicts are read by campaigns/run_v*.py and rpbridge/ivp.py.

<div align="center">

<img src="../../../../assets/svg/divider-magenta.svg" alt="—" width="100%" height="12"/>
<sub>⚡ Part of <a href="../../../../README.md">AB-Cloud Research</a> — numbers are verbatim from the unified registry; no result on this page is a claim about the Riemann hypothesis · <a href="../README.md">⬆ parent section</a></sub>

</div>
