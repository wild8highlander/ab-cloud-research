<!-- AB-ENRICHED:v1 · sub -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venice&height=48&color=0:ffd60a,100:05060f&section=header" alt="" width="100%"/>

**🧭 [⬆ 02_data/](../README.md) · [🏠 Root README](../../../../README.md)**

</div>
# 🗃 Processed Data — `research_registry.json`

The single machine-readable register of the academic package. Every number
quoted in the New-package monographs resolves to an entry here — with its
source level, provenance and verdict — so that citations can be checked
programmatically instead of by eyeball.

| File | What it holds |
|---|---|
| [`research_registry.json`](research_registry.json) | 8 top-level blocks: `programme` (the Hilbert–Pólya framing), `sources` (code + data provenance), `levels` (the package's claim levels), `flagship_results`, `theorems`, `verdicts` (incl. honest WARN-class rows), `numbers_registry` (the quoted constants and their origin runs), `statistics` |

**How it is used.** The monograph chapters in [`../01_monographs/`](../../01_monographs/)
reference registry keys rather than bare literals; the JSON is the join table
between the committed run artifacts of
[`../../../../results/`](../../../../results/) (v19 flagship, H1–H8 audit) and
the prose. Update flow: a number changes → the owning run folder and registry
entry change in the same commit → monographs re-cite.

> [!NOTE]
> This file is part of the academic package's honesty protocol: numbers that
> exist only in prose, without a registry entry pointing to a committed
> artifact, are treated as mistakes, not as shortcuts.

Part of [`AB_Cloud_Academic_Package/02_data/`](../) · see the package root [README](../../README.md)

<div align="center">

<img src="../../../../assets/svg/divider-gold.svg" alt="—" width="100%" height="12"/>
</div>
