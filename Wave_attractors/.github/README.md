<!-- AB-ENRICHED:v2 · wave-deep-dive · .github infrastructure -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=cylinder&height=72&color=0:05060f,50:ffd60a,100:05060f&section=header&text=STUDY%20W1%20%C2%B7%20INFRASTRUCTURE&fontSize=22&fontColor=e5e7eb&fontAlignY=55&animation=fadeIn" alt="Study W1 infrastructure" width="100%"/>

<img src="https://readme-typing-svg.demolab.com/?font=JetBrains+Mono&weight=500&size=14&duration=2600&pause=1000&color=ffd60a&center=true&vCenter=true&width=720&lines=CI+plumbing+for+the+wave-attractor+study;Every+push+replays+the+quick+protocol;Julia+cross-verification+watches+the+port" alt="Typing: infrastructure tagline"/>

**🧭 [⬆ Wave_attractors/](../README.md) · [🏠 Root README](../../README.md)**

</div>

<div align="center">

<img src="../assets/visuals/glyph-ci.svg" alt="Animated infrastructure glyph — a slowly turning gear inside a golden medallion" width="72"/>

<img src="../assets/ai/banner-ci.webp" alt="AI banner: the CI pipeline as a luminous circuit board with wave pulses flowing through checkmarked stages (prompt P-W2)" width="100%"/>

</div>

# 🏗 Wave_attractors/.github

> **Repository infrastructure for study W1** — the configuration shelf that keeps the
> hyperbolic wave-attractor study honest: automated checks, pipelines and validation
> that run without human attention. This folder is operational plumbing rather than
> research content; the scientific claims live in the [section README](../README.md),
> the docs and the committed verdicts.

[![Tier](https://img.shields.io/badge/tier-infrastructure-ffd60a?style=flat-square)](../README.md)
[![Study](https://img.shields.io/badge/study-W1-0E7C86?style=flat-square)](../README.md)
[![CI](https://img.shields.io/github/actions/workflow/status/wild8highlander/ab-cloud-research/wave-attractors.yml?branch=main&style=flat-square&label=wave--attractors%20CI)](https://github.com/wild8highlander/ab-cloud-research/actions/workflows/wave-attractors.yml)

> **🧭 Navigation:** [⬆ Wave_attractors/](../README.md) · [🏠 Root README](../../README.md)

---

## 🗂 What lives here

| Item | What it controls |
|---|---|
| [`workflows/wave-attractors.yml`](workflows/wave-attractors.yml) | the W1 study workflow — quick ray/wave/AB protocol + Julia cross-verification, triggered on every push or PR touching `wave_attractors/**` |

Everything else in the study (experiments, figures, monographs) is invoked *by* this
configuration, never the other way around. Editing files here changes what is checked
and when — it never changes a single number of the study itself. The pipeline that the
workflow drives is documented one level up, in the
[package README](../wave_attractors/README.md).

<details>
<summary><strong>⚙️ How a push becomes a verdict (click)</strong></summary>

```mermaid
flowchart LR
    P["push / PR<br/>wave_attractors/**"] --> W["wave-attractors.yml"]
    W --> J1["python-pipeline<br/>quick protocol E1–E7"]
    J1 --> A1["artifact: w1-data<br/>(14 days retention)"]
    J1 --> J2["julia-cross-verification<br/>port + TD kernel"]
    J2 --> A2["artifact:<br/>cross-verification reports"]
    J2 --> V["verify_repro.py<br/>sanity check"]
```

The full job-by-job breakdown, with every step and its time budget, is described in the
[workflows README](workflows/README.md).

</details>

<details>
<summary><strong>🧪 What this CI actually protects (click)</strong></summary>

* **Regression safety** — the quick protocol (E1/E2/E3/E5 + E4 + E6 + E7 in fast mode)
  re-runs on every push, so a change that breaks the ray core, the Helmholtz solver or
  the ADE-FDTD time-domain kernel is caught before it can contaminate committed data.
* **Cross-language identity** — the Julia port must keep reproducing the Python
  trajectories: the reference dump is rebuilt, replayed in Julia and compared, guarding
  the *3.45·10⁻¹⁵* short-horizon parity claim of the study.
* **Artifact provenance** — every run uploads the regenerated data and the
  cross-verification reports as downloadable artifacts, so any CI verdict can be
  inspected post-mortem.

</details>

## 🧭 Where to go next

[📦 Package & results](../wave_attractors/README.md) · [⚙️ Workflow details](workflows/README.md) ·
[📚 Docs shelf](../docs/README.md) · [🎨 Assets shelf](../assets/README.md)

---

<div align="center">

<img src="../assets/visuals/wave-divider-gold.svg" alt="Animated wave divider" width="100%" height="16"/>

<a href="../README.md"><img src="../assets/ai/avatar.webp" alt="Study W1 avatar" width="56"/></a>

<sub>🌀 <strong>Hyperbolic Wave Attractors — study W1</strong> · part of
<a href="../../README.md">AB-Cloud Research</a> ·
DOI <a href="https://doi.org/10.5281/zenodo.21825394">10.5281/zenodo.21825394</a> ·
<a href="../../README.md">⬆ section</a></sub>

</div>
