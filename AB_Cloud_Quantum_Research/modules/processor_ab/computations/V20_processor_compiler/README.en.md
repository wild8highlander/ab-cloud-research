# Campaign V20 · The AB-Processor Compiler

![version](https://img.shields.io/badge/version-0.1.0-298bbc) ![](https://img.shields.io/badge/phase-P0-3b4f58) ![](https://img.shields.io/badge/status-honest-3a6b4f)

> **Arbitrary 4×4/8×8 unitary logic compiles into the AB-cloud ISA
> exactly (machine floor) and executes bit-exactly reproducibly.
> Previews of memory, arithmetic, zero reading and nonlocality.**

[← Back to the main README](../../README.md)

## Contents

1. [Campaign question](#campaign-question)
2. [Results](#results)
3. [Method](#method)
4. [Figures](#figures)
5. [Monographs](#monographs)
6. [Data](#data)
7. [Reproduction](#reproduction)
8. [Honest remarks](#honest-remarks)
9. [Verdict](#verdict)

---

## Campaign question

What is the AB cloud as a computing device? The V20 specification
(pre-registered in the mother package, PROCESSOR_PROGRAM.md): ISA +
exact compilation of arbitrary unitary logic + bit-exact
reproducibility; plus the first measurements of memory, arithmetic,
zero reading and nonlocality.

## Results

| Quantity | Value | Status |
|---|---|---|
| Compilation 4×4 (M=200, seed 96) | min F = 1−4.44e-16 | threshold 1−1e-12: PASS |
| Compilation 8×8 (M=100, seed 296) | min F = 1−6.66e-16 | threshold 1−1e-10: PASS |
| Controls | identity/permutation/DFT4/CL(2) exact | PASS |
| Replay | bit-exact (float64) | PASS |
| Depth (max) | 7 / 29 gates | recorded |
| Memory P1 (preview) | RAM 64/64; b = 4.0; words 256/256 | consistent with V21 |
| ALU V22 (preview) | 256/256 + 128/128 + 16/16 + 256/256 | consistent with V22 |
| Reading V23 (preview) | 12/12 zeros, dev 2.98e-3, zero storage | "reads, not carries" |
| Nonlocality V24 (preview) | CHSH 2√2; protection 1000/1000; ρ₁ 3.3e-16 | consistent with V24 |

## Method

rpbridge/isa.py + rpbridge/compiler.py: Givens-QR → two-level
blocks → AB2 parametrization (closed form) → PHASE ladder; no
optimization. Previews: rpbridge/{memory,alu,riemann_reader,nonlocality}.py.
Protocol and thresholds: docs/methods.md, results/ROADMAP.md (P0).

## Figures

| File | Where |
|---|---|
| `fig01_en.png` … `fig06_en.png` | 600 dpi — `../../figures_hires/en/`; copies — `figures/en/` |

## Monographs

| File | Format |
|---|---|
| `monograph_ru.pdf` / `monograph_ru.docx` | PDF / DOCX |
| `monograph_en.pdf` / `monograph_en.docx` | PDF / DOCX |

## Data

| File | Content |
|---|---|
| `data/results.json` | the committed campaign verdict (= data/v20_verdict.json) |

## Reproduction

```bash
python3 campaigns/run_v20_processor.py   # verdict tour (seconds)
python3 scripts/compute_v20.py           # fresh recomputation
python3 -m pytest tests/ -q              # 19 tests
```

## Honest remarks

- Metrics are pre-registered; the verdict is committed and independent
  of fresh recomputation.
- Preview layers are labeled preliminary; their strict thresholds
  belong to V21–V24 (results/ROADMAP.md).
- The mathematical specification of a processor is executed; the
  physical carrier is out of scope. RH is not proven; FTL is not claimed.
- Every claim has a file (V14 scheme) with the list of non-implications.

## Verdict

**PROCESSOR_SPEC_EXECUTED: the P0 processor specification is executed — exact compiler, controls, bit-exact replay; P1–P3 previews match the thresholds**

---

*AB Quantum Processor Program v0.1.0 · V20 · The AB-processor compiler*
