# Repository map

One page, the whole tree: what lives where, and which document explains it.
Every folder carries its own README with deeper detail.

## The pipeline

```mermaid
flowchart LR
    subgraph DATA["Frozen data layer"]
        Z["verification/data/<br/>2 001 058 ζ zeros · SHA-256"]
    end
    subgraph CORE["Canonical numerics"]
        J["code/ab_cloud_full.jl<br/>39 tests · two-pass"]
    end
    subgraph CROSS["Cross-language verification"]
        V["10 languages<br/>verification/"]
        S64["spinor64<br/>64/64 GUE-consistent"]
    end
    subgraph FORMAL["Formal layer"]
        L["Lean 4<br/>theorems + re-derivation"]
        C["Coq · Agda · Isabelle"]
    end
    subgraph OUT["Publications & apps"]
        M["projects/monographs/<br/>v22 RU/EN/ZH + v21 + v2.2.1"]
        R["results/<br/>flagship artifacts"]
        APP["apps/<br/>dashboard + 3D lab"]
    end
    Z --> J
    Z --> V
    Z --> L
    J --> R
    V --> S64
    J --> M
    R --> APP
    C -.-> L
```

## The tree

| Path | What lives there | Read this |
|------|------------------|-----------|
| `code/` | the canonical Julia suite (v23, 39 tests), RH sweep benches, the H-P audit battery | [`code/README.md`](https://github.com/wild8highlander/ab-cloud-research/blob/main/code/README.md) |
| `code/julia/` | the v23 provenance copy + version lineage notes | [`code/julia/README.md`](https://github.com/wild8highlander/ab-cloud-research/blob/main/code/julia/README.md) |
| `verification/` | the 10-language cross-verification suite, spinor64, ζ datasets, per-section micro-verifications | [`verification/README.md`](https://github.com/wild8highlander/ab-cloud-research/blob/main/verification/README.md) |
| `formal/` | **the formal layer** — Lean 4 (theorems + executable), Coq, Agda, Isabelle/HOL, all dependency-free | [`formal/README.md`](formal.md) |
| `formal/lean4/` | the flagship Lean project: exact layer, numeric port, `abcloud-verify` executable | [`formal/lean4/ABCloud/README.md`](https://github.com/wild8highlander/ab-cloud-research/blob/main/formal/lean4/ABCloud/README.md) |
| `projects/hilbert-polya/` | the Hilbert–Pólya bridge subproject: campaigns C1–C8, theorems T1–T10, monograph volumes | [`projects/hilbert-polya/README.md`](https://github.com/wild8highlander/ab-cloud-research/blob/main/projects/hilbert-polya/README.md) |
| `projects/monographs/` | five monograph editions (v22 RU/EN/ZH + original v21 RU/EN) + v2.2.1 corrections, 600-dpi figure apparatus | [`projects/monographs/README.md`](https://github.com/wild8highlander/ab-cloud-research/blob/main/projects/monographs/README.md) |
| `projects/lab-3d/` | the 3D lattice laboratory: code, committed outputs, preprint bundle | [`projects/lab-3d/README.md`](https://github.com/wild8highlander/ab-cloud-research/blob/main/projects/lab-3d/README.md) |
| `projects/dirac-lab/` | the Dirac laboratory: D1–D14 ledger, 96 checks, all PASS | [`projects/dirac-lab/README.md`](https://github.com/wild8highlander/ab-cloud-research/blob/main/projects/dirac-lab/README.md) |
| `projects/vortex-optimization/` | the Test 34-ext vortex-density optimization study (best D = 0.0318) | [`projects/vortex-optimization/README.md`](https://github.com/wild8highlander/ab-cloud-research/blob/main/projects/vortex-optimization/README.md) |
| `projects/wave-attractors/` | the hyperbolic wave-attractors reproduction study (W1) | [`projects/wave-attractors/README.md`](https://github.com/wild8highlander/ab-cloud-research/blob/main/projects/wave-attractors/README.md) |
| `projects/meridian-observatory/` | 24 standalone Julia spectral benches | [`projects/meridian-observatory/README.md`](https://github.com/wild8highlander/ab-cloud-research/blob/main/projects/meridian-observatory/README.md) |
| `apps/` | the React dashboard and the WebGL 3D laboratory (with prebuilt bundles) | [`apps/README.md`](https://github.com/wild8highlander/ab-cloud-research/blob/main/apps/README.md) |
| `results/` | the flagship run artifacts (453 files, 39 directories) + reference logs | [`results/README.md`](https://github.com/wild8highlander/ab-cloud-research/blob/main/results/README.md) |
| `docs/` | this MkDocs Material site | [`docs/README.md`](https://github.com/wild8highlander/ab-cloud-research/blob/main/docs/README.md) |
| `assets/` | the repo banner and shared art | [`assets/README.md`](https://github.com/wild8highlander/ab-cloud-research/blob/main/assets/README.md) |
| `.github/` | the nine CI workflows, templates, dependabot, labeler | [`.github/WORKFLOWS.md`](https://github.com/wild8highlander/ab-cloud-research/blob/main/.github/WORKFLOWS.md) |

## The one rule

**Every arrow in the pipeline reads the same frozen dataset.** The Julia
canon, the ten ports and the formal layer never re-download or regenerate
the ζ zeros — so a disagreement between any two boxes is immediately
visible rather than hidden by different inputs.
