<!-- AB-ENRICHED:v2 · wave-deep-dive · CI workflows -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venice&height=60&color=0:05060f,50:ff2ec4,100:05060f&section=header&text=W1%20CI%20WORKFLOWS&fontSize=22&fontColor=e5e7eb&fontAlignY=55&animation=twoline" alt="W1 CI workflows" width="100%"/>

<img src="https://readme-typing-svg.demolab.com/?font=JetBrains+Mono&weight=500&size=14&duration=2600&pause=1000&color=ff2ec4&center=true&vCenter=true&width=720&lines=wave-attractors.yml+%C2%B7+two+jobs+one+verdict;Quick+protocol+on+every+push;Julia+replays+what+Python+wrote" alt="Typing: workflow tagline"/>

**🧭 [⬆ .github/](../README.md) · [⬆⬆ Wave_attractors/](../../README.md) · [🏠 Root README](../../../README.md)**

</div>

<div align="center">

<img src="../../assets/visuals/glyph-workflows.svg" alt="Animated workflows glyph — a pulsing directed graph inside a magenta medallion" width="72"/>

<img src="../../assets/ai/banner-workflows.webp" alt="AI banner: automated workflow machinery made of light, a wavefront passing through branching graph nodes (prompt P-W3)" width="100%"/>

</div>

# 🔁 `.github/workflows` — the W1 study workflow

> **One YAML file, two jobs, one verdict.** [`wave-attractors.yml`](wave-attractors.yml)
> is the automated conscience of the hyperbolic wave-attractor study: it replays the
> quick experimental protocol on every push, then makes the Julia port prove that it
> still agrees with Python to machine precision.

[![Workflow](https://img.shields.io/badge/workflow-wave--attractors.yml-ff2ec4?style=flat-square)](wave-attractors.yml)
[![CI](https://img.shields.io/github/actions/workflow/status/wild8highlander/ab-cloud-research/wave-attractors.yml?branch=main&style=flat-square&label=status)](https://github.com/wild8highlander/ab-cloud-research/actions/workflows/wave-attractors.yml)
[![Trigger](https://img.shields.io/badge/trigger-push%20%C2%B7%20PR%20%C2%B7%20manual-1c2740?style=flat-square)](wave-attractors.yml)

> **🧭 Navigation:** [⬆ .github/](../README.md) · [⬆⬆ Wave_attractors/](../../README.md) · [🏠 Root README](../../../README.md)

---

## 🗺 Job graph

```mermaid
flowchart TB
    TRIGGER["push / PR touching wave_attractors/**<br/>or manual workflow_dispatch"] --> J1

    subgraph J1["job 1 · python-pipeline · ubuntu-latest · ≤ 25 min"]
        S1["ray-core self-tests<br/>(≤ 5 min)"] --> S2["quick protocol E1/E2/E3/E5<br/>(≤ 10 min)"]
        S2 --> S3["E4 frequency + ray density<br/>(≤ 6 min)"]
        S3 --> S4["Helmholtz wave maps --quick<br/>(≤ 6 min)"]
        S4 --> S5["E6 eta scan --quick<br/>(≤ 6 min)"]
        S5 --> S6["E7 time-domain --quick<br/>(≤ 10 min)"]
        S6 --> S7["AB water companion<br/>(≤ 5 min)"]
        S7 --> S8["dump_reference_csv.py<br/>reference for the port"]
    end

    S8 --> ART1["📦 artifact w1-data"]
    ART1 --> J2

    subgraph J2["job 2 · julia-cross-verification · needs job 1 · ≤ 20 min"]
        T1["setup Julia 1.10"] --> T2["wave_attractors.jl<br/>ray port (≤ 10 min)"]
        T2 --> T3["td_check.jl · E7 TD kernel<br/>(≤ 5 min)"]
        T3 --> T4["verify_cross.py + verify_td_cross.py<br/>(≤ 5 min)"]
        T4 --> T5["verify_repro.py<br/>verifier sanity"]
    end

    J2 --> ART2["📦 artifact w1-cross-verification"]
```

## ⏱ Step budgets at a glance

| Job | Step | Command (condensed) | Timeout |
|---|---|---|---:|
| python-pipeline | Ray-core self-tests | `ray_billiard.py` | 5 min |
| | Quick protocol | `run_experiments.py --quick` | 10 min |
| | E4 | `e4_frequency.py` | 6 min |
| | Wave maps | `wave_directional.py --quick` | 6 min |
| | E6 η-scan | `e6_eta_scan.py --quick` | 6 min |
| | E7 time-domain | `e7_time_domain.py --quick` | 10 min |
| | AB companion | `ab_water.py` | 5 min |
| | Reference dump | `dump_reference_csv.py` | — |
| julia-cross-verification | Julia ray port | `julia wave_attractors.jl wave_attractors` | 10 min |
| | Julia TD kernel | `julia td_check.jl …/julia_td` | 5 min |
| | Cross-verification | `verify_cross.py` · `verify_td_cross.py` | 5 min |
| | Reproducibility sanity | `verify_repro.py --reference … --candidate …` | 5 min |

<details>
<summary><strong>📦 Artifacts & permissions (click)</strong></summary>

| Artifact | Contents | Retention |
|---|---|---|
| `w1-data` | the regenerated `wave_attractors/data/` tree | 14 days |
| `w1-cross-verification` | `cross_verification.json` + `td_cross_verification.json` | 14 days |

The workflow declares `permissions: contents: read` — it can read the repository and
nothing else. Both jobs upload their artifacts `if: always()`, so even a red run
leaves an inspectable trail.

</details>

<details>
<summary><strong>🔬 Why the two-job split (click)</strong></summary>

The split mirrors the study's own reproducibility doctrine: **job 1 produces**, **job 2
disproves**. The Python pipeline is allowed to be fast and approximate (`--quick`
protocol); the Julia job then re-derives the same physics from the frozen reference
dump with an independent implementation. If the two ever disagree beyond floating-point
noise — the study's measured identity is *3.45·10⁻¹⁵* over 1200 bounce points for rays
and *2.4·10⁻¹⁵* over 400 steps for the TD kernel — the run goes red, and no number on
this folder's READMEs is trusted until it is green again.

</details>

## 🧭 Where to go next

[🏗 .github shelf](../README.md) · [📦 Package README](../../wave_attractors/README.md) ·
[⚙️ Julia port](../../wave_attractors/scripts/julia/README.md)

---

<div align="center">

<img src="../../assets/visuals/wave-divider-magenta.svg" alt="Animated wave divider" width="100%" height="16"/>

<a href="../../README.md"><img src="../../assets/ai/avatar.webp" alt="Study W1 avatar" width="56"/></a>

<sub>🌀 <strong>Hyperbolic Wave Attractors — study W1</strong> · part of
<a href="../../../README.md">AB-Cloud Research</a> ·
DOI <a href="https://doi.org/10.5281/zenodo.21825394">10.5281/zenodo.21825394</a> ·
<a href="../README.md">⬆ parent</a></sub>

</div>
