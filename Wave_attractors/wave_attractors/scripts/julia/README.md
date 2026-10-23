<!-- AB-ENRICHED:v2 · wave-deep-dive · julia port -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venice&height=60&color=0:05060f,50:a78bfa,100:05060f&section=header&text=W1%20%C2%B7%20JULIA%20PORT&fontSize=22&fontColor=e5e7eb&fontAlignY=55&animation=twoline" alt="W1 Julia port" width="100%"/>

<img src="https://readme-typing-svg.demolab.com/?font=JetBrains+Mono&weight=500&size=14&duration=2600&pause=1000&color=a78bfa&center=true&vCenter=true&width=720&lines=an+independent+implementation+that+must+agree;stdlib+only+%C2%B7+Julia+%3E%3D+1.10;parity+at+3.45e-15" alt="Typing: julia tagline"/>

**🧭 [⬆ scripts/](../README.md) · [⬆⬆ wave_attractors/](../../README.md) · [🏠 Root README](../../../../README.md)**

</div>

<div align="center">

<img src="../../../assets/visuals/glyph-julia.svg" alt="Animated julia glyph — two waves converging into one identical line" width="72"/>

<img src="../../../assets/ai/banner-julia.webp" alt="AI banner: two intertwined light streams in cyan and violet converging into one identical waveform (prompt P-W12)" width="100%"/>

</div>

# 🟣 `scripts/julia/` — the independent port

> **Two languages, one physics.** This folder holds the Julia re-implementation of the
> wave-attractor core — an *independent* code path whose only job is to disagree with
> Python if Python is wrong. It never does: the measured short-horizon identity is
> **3.45·10⁻¹⁵** over 1200 bounce points (rays) and **2.4·10⁻¹⁵** over 400 steps (TD kernel).

<div align="center">

<img src="../../../assets/visuals/parity.svg" alt="Animated parity: the Python and Julia trajectories converge into one identical line, max deviation 3.45e-15" width="720"/>

</div>

[![Language](https://img.shields.io/badge/julia-%3E%3D%201.10-a78bfa?style=flat-square)](wave_attractors.jl)
[![Deps](https://img.shields.io/badge/dependencies-stdlib%20only-00e5ff?style=flat-square)](wave_attractors.jl)
[![Parity](https://img.shields.io/badge/ray%20parity-3.45e--15-2EA043?style=flat-square)](../../data/cross_verification.json)

> **🧭 Navigation:** [⬆ scripts/](../README.md) · [⬆⬆ wave_attractors/](../../README.md) · [🏠 Root README](../../../../README.md)

## 📁 Inventory

| Item | What it is |
|---|---|
| [`wave_attractors.jl`](wave_attractors.jl) | the Julia ray port (stdlib only, Julia ≥ 1.10) — replays the frozen reference dump and writes the comparison trajectories |
| [`td_check.jl`](td_check.jl) | the Julia E7 time-domain kernel — the TD counterpart used by `verify_td_cross.py` |

```mermaid
flowchart LR
    PY["dump_reference_csv.py<br/>launch states"] --> JL["wave_attractors.jl<br/>ray port"]
    JL --> CMP["verify_cross.py<br/>3.45e-15 over 1200 points"]
    E7["e7_time_domain.py<br/>TD snapshots"] --> JTD["td_check.jl<br/>TD kernel"]
    JTD --> CMP2["verify_td_cross.py<br/>2.4e-15 over 400 steps"]
    CMP --> CERT["data/cross_verification.json"]
    CMP2 --> CERT
```

<details>
<summary><strong>🧪 What is verified — and what deliberately is not (click)</strong></summary>

* **Verified bitwise-comparably:** short-horizon trajectories (the deterministic cascade
  phase before chaos amplifies round-off), the TD kernel step response, and the
  statistical attractor observables — lock fraction, period set, cascade scale.
* **Deliberately not compared:** individual long-horizon (1600-bounce) trajectories —
  they are chaotic during the cascade phase, so any floating-point operation-order
  difference grows exponentially. Cross-language agreement is claimed and checked on
  the levels above, and both pass.
* The port is **stdlib-only** on purpose: no package ecosystem in the verification path,
  nothing to pin beyond the Julia version itself.

</details>

## 🧭 Navigation

[⬅ scripts/](../README.md) · [→ monograph build](../monograph/README.md) · [→ report build](../report/README.md) · [🏠 Repo root](../../../../README.md)

---

<div align="center">

<img src="../../../assets/visuals/wave-divider-violet.svg" alt="Animated wave divider" width="100%" height="16"/>

<a href="../../README.md"><img src="../../../assets/ai/avatar.webp" alt="Study W1 avatar" width="56"/></a>

<sub>🌀 <strong>Hyperbolic Wave Attractors — study W1</strong> · part of the
<a href="../../../../README.md">AB-Cloud Research</a> repository ·
DOI <a href="https://doi.org/10.5281/zenodo.21825394">10.5281/zenodo.21825394</a> ·
© 2026 Isaev Iskhak Khamzatovich — personal proprietary use, see the
<a href="../../../../LICENSE">license terms</a></sub>

</div>
