# AB Quantum Processor Program

![version](https://img.shields.io/badge/version-0.1.0-298bbc) ![series](https://img.shields.io/badge/campaigns-V20--V26-3b4f58) ![status](https://img.shields.io/badge/P0-PROCESSOR_SPEC_EXECUTED-3a6b4f)

> **The AB cloud is a universal quantum processor.** Phase P0 is
> executed: an ISA with a phase continuum, an exact compiler for
> arbitrary unitary logic, memory, arithmetic, reading the Riemann
> zeros off direct algebraic functions, and holonomic nonlocality —
> all with pre-registered thresholds and committed verdicts.

**About.** A standalone companion program of the
[AB Research Program](https://github.com/wild8highlander/ab-cloud-research)
series (V1–V19; the processor specification was pre-registered in
`results/PROCESSOR_PROGRAM.md` of package v1.2.1). Campaign numbering
continues: V20–V26 = phases P0–P6 of the roadmap
[results/ROADMAP.md](results/ROADMAP.md) → Datasheet 1.0.

Russian version: [README.ru.md](README.ru.md)

---

## Contents

1. [New in v0.1.0](#new-in-v010)
2. [Headline results](#headline-results)
3. [Key thesis: reads, not carries](#key-thesis-reads-not-carries)
4. [Nonlocality: knows, does not signal](#nonlocality-knows-does-not-signal)
5. [Roadmap P0–P6](#roadmap-p0p6)
6. [Package structure](#package-structure)
7. [Reproduction](#reproduction)
8. [Honest boundaries](#honest-boundaries)
9. [Citation](#citation)

## New in v0.1.0

The zero (foundation) release of the program:

- **AB-cloud ISA**: {AB2 — a two-level block pulse, PHASE — a selective
  level detuning} + derived RZ/RX/CPHASE/CNOT; the phase continuum
  φ = 2πΦ/Φ₀; every primitive calibrated by block-Hamiltonian
  exponentiation (fidelity ≥ 1−1e-14);
- an **exact compiler** for arbitrary 4×4/8×8 unitary logic
  (Givens-QR → AB2 + PHASE, closed form, no optimization);
- **preview layers** of phases P1–P3: memory (RAM 64/64), ALU
  (256/256), zero reading (12/12, no table), nonlocality (CHSH 2√2,
  no-signaling);
- a 7-tab web laboratory; RU/EN monographs × PDF/DOCX; a workbook;
  claim audit; IVP01–IV05; self-build and clean ZIP validation.

## Headline results

| Result | Value | Threshold | Status |
|---|---|---|---|
| Compiler 4×4 (M=200, seed 96) | min F = 1−4.44e-16 | ≥ 1−1e-12 | PASS |
| Compiler 8×8 (M=100, seed 296) | min F = 1−6.66e-16 | ≥ 1−1e-10 | PASS |
| Controls identity/permutation/DFT4/CL(2) | exact | exact | PASS |
| Bit-exact replay | float64 identical | required | PASS |
| Depth (max) | 7 / 29 gates | recorded | recorded |
| Memory (P1 preview) | RAM 64/64; b = 4.0 | 64/64; b ≤ 6 (V21) | consistent |
| ALU (V22 preview) | 256/256 + 128/128 + 16/16 + 256/256 | 256/256 (V22) | consistent |
| Reading (V23 preview) | 12/12 zeros, dev 2.98e-3 | K=138 @ T=300 (V23) | mechanism confirmed |
| Nonlocality (V24 preview) | CHSH 2√2; protection 1000/1000 | S ≥ 2.8 (V24) | consistent |

Campaign V20 verdict: **PROCESSOR_SPEC_EXECUTED** (full verdict in
`data/v20_verdict.json`, tour in `campaigns/run_v20_processor.py`).

## Key thesis: reads, not carries

The point of the program is not that the cloud "carries" the Riemann
zeros, but that it **reads** the zeros off the critical line through
direct algebraic functions. Pipeline: the formula ζ(s) (O(1)
constants) → argument winding of arg ζ(½+it) → π-slips (the V19
monodromy) → zero positions. No zero table enters the input or the
state; the control (bisection of the real function Z(t)) is applied
only AFTER the reading is fixed — the V1 blind protocol. On the window
[2, 58]: 12/12 zeros exact, maximum deviation 2.98e-3, storage — 0
zeros and 6 formula constants. The full protocol (K = 138, T = 300,
dev ≤ 1e-8) is campaign V23 of phase P3.

## Nonlocality: knows, does not signal

"One particle knows the other" is a holonomic (topological)
correlation: each particle's phase is a functional of ONE global vortex
configuration, not the result of a signal exchange. Measured: the
joint correlation E(XX) = (1+cos Φ₁₂)/2 carries the cross phase
Φ₁₂ = 2πq₁₂L₁₂; the reduced state of a particle is invariant under the
partner's local operations (100 unitaries, ‖Δρ₁‖ = 3.3e-16) — no
communication channel; 1000 random local perturbations leave the phase
intact (max 5.6e-16) — the protection is topological; CHSH S = 2√2 ≥ 2.8
with exact commutation of the separated observables ([Aᵢ⊗I, I⊗Bⱼ] = 0).
The full protocol — V24 (phase P4).

## Roadmap P0–P6

| Phase | Version | Campaign | PASS threshold | Status |
|-------|---------|----------|---------------|--------|
| P0 | v0.1.0 | V20 Compiler | F ≥ 1−1e-12 / 1−1e-10 | **EXECUTED** |
| P1 | v0.2.0 | V21 Memory | RAM 64/64 (noise+ECC); b ≤ 6 | preview consistent |
| P2 | v0.3.0 | V22 ALU | 256/256; bigint via NTT; C/JS regression | preview consistent |
| P3 | v0.4.0 | V23 Reading | 16 numbers ≤ 1e-12; f∘g ≤ 1e-12; K=138 @ T=300 ≤ 1e-8 | mechanism confirmed |
| P4 | v0.5.0 | V24 Nonlocality | ≤ 1e-14; 1000/1000; S ≥ 2.8; [A,B]=0 | preview consistent |
| P5 | v0.6.0 | V25 Benchmarks | RB ≥ 0.999; transfer ≥ 0.99 | — |
| P6 | v1.0.0 | V26 Datasheet | {H,T,AB(π/4)} ≤ 12 gates @ 1e-8; Lean O-uni | — |

Full version with acceptance criteria, risks and the mother-series
link: [results/ROADMAP.md](results/ROADMAP.md).

## Package structure

```
ab_quantum_processor/
├── rpbridge/            core: isa, compiler, memory, alu,
│                        nonlocality, riemann_reader, ivp, audit
├── campaigns/           verdict tour (run_v20_processor.py)
├── computations/        V20_processor_compiler: README ru/en, data,
│                        monographs ru/en × pdf/docx, figures
├── data/                committed verdict v20_verdict.json
├── figures_hires/       600 dpi figures × ru/en (fig01–fig06)
├── monograph/           DOCS sources + _json
├── web_lab/             web laboratory (7 tabs, RU/EN)
├── tables/              qp_workbook.xlsx (6 sheets)
├── docs/                methods and theory
├── results/             ROADMAP.md (P0–P6), RESULTS.md
├── tests/               19 pytest tests
├── verification/        claim audit (V14 scheme)
├── independent_verification/  IV01–IV05
├── scripts/             self-build: compute, figures, monographs,
│                        workbook, release
├── README.md / README.ru.md
└── Makefile, VERSION, CHANGELOG, CITATION.cff, SHA256SUMS.txt
```

## Reproduction

```bash
pip install -r requirements.txt
python3 scripts/compute_v20.py           # fresh V20 recomputation (~2 s)
python3 campaigns/run_v20_processor.py   # verdict tour
python3 scripts/make_figures.py          # 600 dpi figures × ru/en
python3 scripts/make_monographs.py       # monographs PDF/DOCX × ru/en
python3 scripts/build_workbook.py        # workbook
python3 -m pytest tests/ -q              # 19/19
independent_verification/RUN_ALL.sh      # IV01–IV05
python3 scripts/make_release.py          # ZIP + SHA256SUMS
make tour                                # same, one command
```

## Honest boundaries

1. What is executed is the **mathematical specification of a
   processor** (exact linear algebra), not a physical chip; the carrier
   question is out of scope.
2. Circuit depth is recorded, not optimized (KAK/Solovay–Kitaev is a
   P6/V26 obligation).
3. The zero reading demonstrates a mechanism and does not prove RH.
4. Nonlocality is a holonomic correlation with an algebraically
   verified commutation of the separated observables; faster-than-light
   signaling is not claimed (on the contrary — it is excluded).
5. The preview layers (memory/ALU/reading/nonlocality) are preliminary
   measurements; the strict thresholds belong to V21–V24.
6. All numbers are deterministic (seeds 96/296); every claim has a file
   with does_not_prove and passes the audit.

## Citation

```bibtex
@misc{abqp2026,
  title  = {AB Quantum Processor Program 0.1.0: V20 — the AB-cloud
            compiler (ISA, exact compilation, memory, zero reading,
            holonomic nonlocality)},
  author = {AB Quantum Processor Program},
  year   = {2026},
  url    = {https://github.com/wild8highlander/ab-cloud-research}
}
```

---

*AB Quantum Processor Program v0.1.0 · V20 · The AB-processor compiler ·
phase P0 executed*
