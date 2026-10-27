<!-- AB-ENRICHED:v1 · sub -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venice&height=48&color=0:ff2ec4,100:05060f&section=header" alt="" width="100%"/>

**🧭 [⬆ realtime_spinor_memory/](README.md) · [🏠 Root README](../../../README.md)**

</div>
# ⚡ The Machine With No Long-Term Memory: Spinor Phase Real-Time Models

**Supplementary study of [AB Cloud Quantum Research](../../../README.md)
· v1.0.0** · 3 models (θ = π/2 · π/3 · π/7) · 5 pre-registered campaigns
(all PASS) · 3 theorems · 12 documents (RU/EN × PDF/DOCX) · 8 tiled
figures @600 dpi · 11 tests

> [!IMPORTANT]
> **Central claim.** The AB computer has no long-term memory — only
> volatile state executing steps in real time. This is not an
> implementation limitation but an architectural principle: the machine
> *reads* mathematics (the trace formula, spectra, ζ zeros) and carries
> nothing. This study reduces the claim to explicit models and proves
> three theorems: phase cycles close at N = 2k (TS1), erasure is
> irreversible (TS2), and an eternal log is incompatible with hard
> real time (TS3).

## The idea

The program's flagship result is a processor that *reads, does not
carry*: ζ zeros are reproduced from six constants of the trace formula,
and zero zeros remain in storage (V23 preview; blind reading of
649+639 zeros in E17). The strict formulation needed its own study:
*what does it mean for a computer to have no long-term memory, and why
is that compatible with real-time execution?*

The answer is built on spinor phases. The machine's only state is the
phase φ of a unit spinor on the circle S¹; one real-time step is a
rotation by the model angle θ. Nothing else exists — no log, no
history, no checkpoints. The phase is simultaneously the register, the
counter (mod N), and the output carrier. The contrast model — the
"eternal log machine" that honestly records every step and periodically
replays everything — demonstrates the price of long-term memory: linear
verification growth and deadline misses. Hence the main conclusion:
**volatility is not a defect but the condition of real-time
determinism.**

## The three models

| Model | Phase θ | Cycle N = 2k | Bits/step | Gap (robustness) |
|-------|---------|--------------|-----------|------------------|
| **S1** · quadrant | π/2 | 4 | 2.000 | π/2 = 1.571 rad |
| **S2** · sextant | π/3 | 6 | 2.585 | π/3 = 1.047 rad |
| **S3** · 14-phase | π/7 | 14 | 3.807 | π/7 = 0.449 rad |

The capacity-vs-robustness trade-off is published honestly: π/7 carries
almost twice the bits per step of π/2, but its gap is 3.5× narrower —
the readout-noise silence zone narrows accordingly (σ* = 0.135 / 0.089 /
0.038 rad).

## The theorems

| Theorem | Statement (short) | Certificate |
|---------|-------------------|-------------|
| **TS1** | the rotation cycle θ = π/k closes after exactly N = 2k steps; minimal gap = 2π/N; the lattice is uniform | ES1: periods 4/6/14 exactly; sweep k = 2…16 |
| **TS2** | after reset I(pre; post) = 0; pre-state reconstruction ≤ 1/N; time compressed to mod N | ES2: 0.2501/0.1674/0.0717 ≈ 1/N over 120k trials |
| **TS3** | the step is O(1) for all t; an eternal log ⇒ Ω(t) ⇒ deadline misses | ES3: slope −1.5e−12; 0/200,000 misses; ×129 growth |

Each theorem lives in its own folder under
[`theorems/`](theorems/): a README with the proof idea and boundaries +
**4 documents** (RU/EN × PDF/DOCX) with the embedded 2×2
"four-dimension" tile.

## Campaigns ES1–ES5

| Campaign | What it certifies | Pre-registered thresholds | Verdict |
|----------|-------------------|---------------------------|---------|
| **ES1** cycles | cycle periods, gaps, uniformity | C1–C4 | ✅ PASS |
| **ES2** volatility | reset irreversibility, I = 0, time → mod N | C1–C4 (+erratum ES2a) | ✅ PASS |
| **ES3** real time | flat step profile, deadlines, log Ω(t) | C1–C4 | ✅ PASS |
| **ES4** memoryless task | 300k-step modular counter, footprint = 1 register, zero storage | C1–C4 | ✅ PASS |
| **ES5** noise | silence zone σ*, robustness order, channel breakdown | C1–C5 (+erratum ES5a) | ✅ PASS |

House discipline applies: thresholds fixed before the run; all numbers
in figures and documents come only from committed verdicts; errata are
published (ES2a: threshold replaced by the 3σ band before acceptance;
ES5a: noise aligned to the pre-registered readout model, diffusion kept
as a threshold-free exploratory measurement).

## Link to the parent program

| Link | Mechanism |
|------|-----------|
| "Reads, does not carry" (V23 · E17) | this study formalizes the principle: TS2 proves storage = 0, TS3 — why real time demands it |
| Trace formula (Th6, V7) | the phase machine is the minimal reader of the trace: state = phase, output = symbol stream |
| AB-cloud ISA (V20) | phase rotations are the degenerate case of ISA PHASE gates; π/2, π/3, π/7 are admissible angles |
| Roadmap P1 (V21, memory) | TS3 gives P1 its theoretical footing: processor memory is volatile by architecture |
| O-J3 (QEC memory) | the "volatile phase vs eternal log" contrast is the zero point for the QEC comparison |

## Quick start

```bash
cd research/realtime_spinor_memory
python3 experiments/run_all.py     # ES1–ES5, ~2.5 min, all PASS
python3 make_figures.py            # 8 tiles @600 dpi from committed verdicts
python3 make_theorem_docs.py       # 12 documents
python3 -m pytest tests/ -q        # 11 invariants
```

## Honest boundaries

- The models are register-and-rotation abstractions; they do not model
  coherent spinor physics and claim no quantum advantage.
- TS2 is about information, not thermodynamics (no Landauer claims).
- ES5 certifies iid readout noise; phase diffusion was measured
  exploratorily (t* ~ gap²/σ²) without thresholds; systematic drift and
  decoherence are out of scope.
- The study is unrelated to the Riemann hypothesis; the RH conclusion
  is stated exactly by the V13 obligation machine (certified — unlocked, 0 assumptions).

The full Russian version: [`README.md`](README.md).

---

<!-- enriched 1.1.0 -->
<div align="center">

<img src="../../../assets/avatars/avatar_spinor.svg" width="84" alt="spinor">

*Part of the discipline: pre-registration · blind protocols · replication ·
negative results published*

**AB Cloud Quantum Research** · v1.1.0 · [license](../../../../LICENSE) · © Isaev Iskhak Khamzatovich

</div>

<div align="center">

<img src="../../../assets/svg/divider-magenta.svg" alt="—" width="100%" height="12"/>
</div>
