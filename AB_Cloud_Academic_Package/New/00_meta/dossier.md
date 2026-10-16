# The reading dossier

*Everything a reviewer needs in one page: what the programme is, what it
claims, what it refuses to claim, and where every number lives.*

## 1. The claim structure

The programme makes **five graded claims** (Г1–Г5) and one meta-claim:

| # | Claim | Verdict | The number that carries it |
|---|---|---|---|
| Г1 | The lattice operator is self-adjoint | **YES** | ‖H−H†‖ = 0.0 exactly (Th1); drift 2.2e−16 (Th2) |
| Г2 | Its spectrum *is* the zero sequence | **YES** | D_nn 0.0079 — the zeros' own level: the shifted zero windows and the GUE zero class measure 0.0079 ± 0.0005 (C3); trace bridge \|ΔK\| ≤ 1.2e-5 (C4); audit v2.0.7 — the bit-level branch (T18) remains open |
| Г3 | Its statistics are GUE-class | **YES** | ⟨r⟩ = 0.60 (C5 v2.0.5 honest regeneration: 0.569–0.633, mean 0.601); ζ-decorated Dirac 0.608 vs theory 0.5992 (D7) |
| Г4 | Its dynamics are Dirac | **YES** | v_F = 2t continuum limit (D1); Klein ×977 (D5); ZB at ω = 2E (D6) |
| Г5 | The primes sit inside the operator | **YES** | the convergence ladder (audit v2.0.8): gate ψ-corr climbs with coverage (−0.12 → +0.09 → +0.24) and with lattice size (Vortex scan: GUE floor 0.0324 → 0.0220, best pooled D = 0.0318); zeros 0.972 → 1; the weight in the trace (Th6, r = 0.9996); the bit-level branch (T18) open |
| RH | The Riemann hypothesis follows | **BLOCKED** | V13 obligation machine — analytic prerequisites remain assumed |

**The one-sentence reading.** The resonator is built and tuned (Г1, Г3, Г4);
the level identity holds at the zeros' own level and the primes enter via
the convergence ladder (Г2, Г5 — YES by audits v2.0.7/v2.0.8); and the wall
that remains has a precise location — **the bit-level locality branch**
(T18: the direct gate-ladder escape at L = 96 is not yet measured, and local
lattices cannot host the entanglement the zero comb demands; S_A ≈ 12–16
nats vs Haar 160–220).

## 2. The honesty-layer index (what this package does NOT prove)

1. **RH** — blocked by V13; formalized in Lean 4 / Coq (the formalization
   *guarantees the blocking*).
2. **Bit-level spectral identity** — the level identity is YES at the
   zeros' own level (audit v2.0.7), but the direct bit-level escape of the
   gate ladder at L = 96 remains unmeasured (T18); the rank branch stays at
   its resolution limit.
3. **The closed-density blind test (C17)** — NEGATIVE by the letter of its
   pre-registered criterion (1.04× over the primes-free null); published as
   a first-class result.
4. **Lattice ζ-correspondence (rank channel)** — V1/V3 designs disproven;
   V6/V16 corrected to the level-identity reading (v2.0.7); the rank-channel
   absence stands as the honest negative of the spectral core.
5. **2q KAK optimality** — the 3-gate optimum is outside the E18 ISA class;
   the compiler's 10-gate solution is the in-class result.
6. **ζ-decorated Dirac in other symmetry classes** — GSE is architecturally
   unreachable (Dyson trinity, C5 registry).

## 3. Where every number lives

| You want | Go to |
|---|---|
| One flagship number with its campaign | `02_data/processed/research_registry.json` (flagship_results) |
| The complete numbers registry (20 headline rows) | `05_logs/metrics.json` |
| A specific campaign's raw record | the source laboratory's folder (see provenance.jsonl) |
| The verdict files with does_not_prove fields | the sources' `*_verdict.json` (paths in the registry) |
| The heritage 38-test run | superseded — record in `CHANGELOG.md` + this dossier |

## 4. The consolidation rules (how numbers were transferred)

1. **Verbatim only.** Numbers are copied from the sources' own verdict
   tables, never re-typed from memory or recomputed.
2. **Disagreements are shown, not resolved.** Where two sources quote
   different values (conventions), both appear with their convention note.
3. **The registry is the single source of truth** for the monograph, the
   report, the web lab and the CLI. One edit propagates everywhere.
4. **Honesty fields are inviolable** — see LICENSE §3.
