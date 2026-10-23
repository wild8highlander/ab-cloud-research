<!-- AB-ENRICHED:v1 · sub -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venice&height=48&color=0:ff2ec4,100:05060f&section=header" alt="" width="100%"/>

**🧭 [⬆ research/](../README.md) · [🏠 Root README](../../../README.md)**

</div>
# ⚡ The machine without long-term memory: real-time spinor phase models


> **🧭 Navigation:** [research/](../README.md) · [AB_Cloud_Quantum_Research/](../../README.md) · [Root README](../../../README.md)

**A supplementary study of the [AB Cloud Quantum Research](../../../README.md)
program · v1.0.0** · 3 models (θ = π/2 · π/3 · π/7) · 5 campaigns with
pre-registered thresholds (all PASS) · 3 theorems · 12 documents
(RU/EN × PDF/DOCX) · 8 tiled figures @600 dpi · 11 tests

> [!IMPORTANT]
> **Central claim.** The AB computer has no long-term memory —
> only volatile state executing steps in real time. This is not an
> implementation limitation but an architectural principle: the machine
> **reads** mathematics (the trace formula, the spectrum, the ζ zeros) and
> carries nothing. This study reduces the claim to explicit models and
> proves three theorems: closure of the phase cycles (TS1), irreversibility
> of erasure (TS2), and the incompatibility of an eternal log with hard
> real time (TS3).

---

## 📖 Contents

- [The idea](#-the-idea)
- [Three models](#-three-models)
- [The theorems](#-the-theorems)
- [Campaigns ES1–ES5](#-campaigns-es1es5)
- [Relation to the parent program](#-relation-to-the-parent-program)
- [Folder structure](#-folder-structure)
- [Quick start](#-quick-start)
- [Boundaries](#-boundaries)

---

## 💡 The idea

The main result of the program is a processor that *reads, does not carry*:
the ζ zeros are reproduced from six constants of the trace formula, and no
zero remains in storage (the V23 preview; the blind reading of 649+639 zeros
in E17). But this principle has a strict formulation that must be proved
separately: **what does it mean for a computer to have no long-term memory,
and why is that compatible with real-time execution?**

The answer is built on spinor phases. The machine's only state is the phase
φ of a unit spinor on the circle S¹; one real-time step is a rotation by the
model angle θ. Nothing else exists: no log, no history, no checkpoints. The
phase is simultaneously the register, the counter (mod N), and the carrier
of the result.

The contrast model — the "eternal log machine", which honestly records every
step and periodically re-checks everything — demonstrates the price of
long-term memory: linear growth of the verification cost and deadline
misses. Hence the main conclusion: **volatility is not a defect but the
condition of real-time determinism**.

## 🧩 Three models

| Model | Phase θ | Cycle N = 2k | Bits/step | Gap (robustness) |
|--------|--------|-------------|----------|---------------------|
| **S1** · quadrant | π/2 | 4 | 2.000 | π/2 = 1.571 rad |
| **S2** · sextant | π/3 | 6 | 2.585 | π/3 = 1.047 rad |
| **S3** · 14-phase | π/7 | 14 | 3.807 | π/7 = 0.449 rad |

The "capacity vs robustness" trade-off is published honestly: π/7 carries
almost twice as many bits per step as π/2, but its gap is 3.5 times narrower —
the silence zone under readout noise is narrower accordingly (σ* = 0.135 / 0.089 /
0.038 rad).

## 📐 The theorems

| Theorem | Statement (short) | Certificate |
|---------|---------------------|------------|
| **TS1** | the rotation cycle θ = π/k closes exactly after N = 2k steps; the minimal gap = 2π/N; the lattice is uniform | ES1: periods 4/6/14 exactly; the series k = 2…16 |
| **TS2** | after a reset I(pre; post) = 0; the reconstruction of the pre-state ≤ 1/N; time is compressed to mod N | ES2: 0.2501/0.1674/0.0717 ≈ 1/N over 120k trials |
| **TS3** | the step is O(1) for any t; an eternal log ⇒ Ω(t) ⇒ deadline misses | ES3: slope −1.5e−12; 0/200 000 misses; ×129 growth |

Each theorem lives in its own folder under [`theorems/`](theorems/):
a README with the derivation idea and boundaries + **4 documents**
(RU/EN × PDF/DOCX) with the embedded "4 dimensions" tiled figure.

## 🔬 Campaigns ES1–ES5

| Campaign | What it checks | Pre-registered thresholds | Verdict |
|----------|---------------|------------------------------|---------|
| **ES1** cycles | periods of the phase cycles, gaps, uniformity | C1–C4 | ✅ PASS |
| **ES2** volatility | irreversibility of the reset, I = 0, time → mod N | C1–C4 (+erratum ES2a) | ✅ PASS |
| **ES3** realtime | flat step profile, deadlines, the Ω(t) of the log | C1–C4 | ✅ PASS |
| **ES4** memoryless task | the modular counter of 300k steps, trace = 1 register, storage = 0 | C1–C4 | ✅ PASS |
| **ES5** noise | the silence zone σ*, the robustness order, the channel breakdown | C1–C5 (+erratum ES5a) | ✅ PASS |

The discipline is the same as in the whole program: thresholds are fixed
before the run; all numbers in the figures and documents come only from
committed verdicts; errata are published (ES2a: the threshold replaced by
a 3σ band before the verdict was accepted; ES5a: the noise was aligned to
the readout noise by pre-registration, the diffusion is a separate
exploration without thresholds); negative results are not retouched.

## 🔗 Relation to the parent program

| Link | Mechanism |
|-------|----------|
| "Reads, does not carry" (V23 · E17) | this study formalizes the principle: TS2 proves storage = 0, TS3 — why it is mandatory for real time |
| Trace formula (Th6, V7) | the phase machine is the minimal "reader" of the trace: the state = phase, the output = a stream of symbols |
| ISA of the AB clouds (V20) | phase rotations are the degenerate case of the ISA PHASE gates; the model phases π/2, π/3, π/7 are admissible angles |
| Roadmap P1 (V21, memory) | TS3 gives theoretical support to stage P1: the processor memory is volatile by architecture |
| O-J3 (QEC memory) | the contrast "volatile phase vs eternal log" is the zero point for the QEC comparison |

## 🗂️ Folder structure

```
realtime_spinor_memory/
├── README.md · README.en.md        # this document (RU/EN)
├── docs/theory.md (+ .en.md)       # theory: the model, definitions, motivation
├── spinor/                         # the library (core, tasks) — 1 register, O(1)
├── experiments/                    # ES1–ES5 + run_all.py + common.py
├── data/                           # verdicts *_verdict.json + raw CSVs
├── figures/{ru,en}/                # 8 tiled 2×2 figures @600 dpi
├── theorems/TS1_cycle · TS2_volatility · TS3_realtime
│   └── README.md + 4 documents (RU/EN × PDF/DOCX) each
└── tests/test_spinor.py            # 11 fast invariants
```

## 🚀 Quick start

```bash
cd research/realtime_spinor_memory

# all campaigns ES1–ES5 (~2.5 min, all verdicts PASS)
python3 experiments/run_all.py

# regeneration of figures and documents (only from committed verdicts)
python3 make_figures.py
python3 make_theorem_docs.py

# fast invariants
python3 -m pytest tests/ -q
```

> [!TIP]
> Requirements: Python ≥ 3.10, numpy, matplotlib. No network, no
> Julia and no external services — the study is self-sufficient.

## 🛑 Boundaries

- The models are abstractions at the "register + rotation" level: they do
  not describe the coherent physics of spinors and claim no quantum
  advantage.
- TS2 is about information, not thermodynamics (the Landauer principle is
  not claimed).
- ES5 certifies iid readout noise; the phase diffusion was measured as an
  exploration (t* ~ gap²/σ²) without thresholds — systematic drifts and
  decoherence are outside the scope of the study.
- The study is not connected to the Riemann hypothesis and states nothing
  about it; the RH status is stated exactly by the obligation machine V13 (certified).

---

<!-- enriched 1.1.0 -->
<div align="center">

<img src="../../../assets/avatars/avatar_spinor.svg" width="84" alt="spinor">

*Part of the discipline: pre-registration · blind protocols · replication ·
negative results published*

**AB Cloud Quantum Research** · v1.1.0 · [license](../../../LICENSE) · © Isaev Iskhak Khamzatovich

</div>

---

<!-- enriched-r3 -->

This folder is a small but functional **shelf of its module**: it keeps a focused set of artifacts that the parent README references. The listing below is generated from the folder itself, so it is exact; the parent README explains how these pieces fit into the study. Nothing here is a compiled binary or an external download — everything is committed source, data or documentation.

A standing research thread: the machine **without long-term memory** — real-time spinor phase models in which the reading is recomputed from scratch and nothing is stored. The folder carries the model code and its own detailed note.

**Subfolders:** `data/` · `docs/` · `experiments/` · `figures/` · `spinor/` · `tests/` · `theorems/`

<div align="center">

<img src="../../../assets/svg/divider-magenta.svg" alt="—" width="100%" height="12"/>
</div>
