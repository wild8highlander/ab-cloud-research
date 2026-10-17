# 06_code — the unified CLI (six languages, one contract) + the research cores + the formal layer

| Runner | Language | Entry | Status |
|---|---|---|---|
| **reference** | Python 3.10+ (typer/rich) | [`python/run.py`](python/run.py) | full command surface |
| cross | Julia 1.10+ (LinearAlgebra only) | [`julia/run.jl`](julia/run.jl) | analyze/doctor/version/cite + delegation |
| cross | Rust (std only) | [`rust/run.rs`](rust/run.rs) | same contract subset |
| cross | Go (std only) | [`go/run.go`](go/run.go) | same contract subset |
| cross | Node.js (zero deps) | [`js/run.js`](js/run.js) | same contract subset |
| cross | Bash (tput) | [`bash/run.sh`](bash/run.sh) | same contract subset |

All six read the same [`config.yaml`](../config.yaml) and emit the same
metrics from [`shared/metrics.json`](shared/metrics.json) — the canonical
cross-language metric set. The contract is binding:
[`shared/contract.json`](shared/contract.json) (+ schema). The Python runner
carries the full aesthetic (banner, 9 themes, progress, quotes, ASCII
charts, i18n ru/en, `--output=json|yaml|table|md`, `--dry-run`, `--explain`,
`-v..-vvv`, hidden `secret`); the other runners mirror its core.

## Quick start

```bash
./cli/run.sh --lang=ru --theme=neon analyze      # unified entry (any impl)
python3 python/run.py --output=json analyze      # clean JSON for pipes
AB_CLOUD_IMPL=js ./cli/run.sh analyze             # pick a runner
```

## Command surface (the contract)

`init · doctor · explain · plan · fetch · validate · preprocess · analyze ·
visualize · report · monograph · lab · api · test · bench · lint · docs ·
package · publish · clean · version · cite` (+ one hidden command).

Orchestration commands (`monograph`, `lab`, `api`, `package`, `publish`) live
in the Python reference; the cross-language runners delegate to it (exit 2)
— mirroring the sources' canonical-implementation + ports culture.

## Layout

```
06_code/
├── python/    run.py (reference CLI) + python_clone/ (the Python reimplementation of the suite)
├── julia/     run.jl
├── rust/      run.rs + Cargo.toml
├── go/        run.go + go.mod
├── js/        run.js + package.json
├── bash/      run.sh
├── shared/    contract.json + metrics.json + errors.json + constants.json + i18n/
├── cli/       run.sh (dispatcher) + completions (bash/zsh/fish)
├── plugins/   example plugin + API
├── hooks/     pre_run.sh (the honesty gate) + post_run.sh
├── scripts/   bootstrap, smoke_test, release, update_checksums, update_manifest, build_monograph
├── lab_standalone/   the standalone Julia research programs (see lab_standalone/README.md)
├── meridian/    the two Meridian D-variants of the canon (RH_Unified_D.jl, RH_Sweep_Pro_D.jl) — byte copies of `code/RH_*_D.jl`
├── formal/      the four proof-assistant ports (lean4 · coq · agda · isabelle) — byte copies of the repo's `formal/` tree
├── Makefile · Dockerfile · requirements*.txt · environment.yml
```

## Canon sync policy

`lab_standalone/ab_cloud_full.jl` and `lab_standalone/hp_audit_standalone.jl`
are **byte copies of the canonical suite** (`code/ab_cloud_full.jl` — the
Aurora edition the CI Julia job runs — and `code/hp_audit_standalone.jl`,
HP·MERIDIAN 25.2-NUMINA). The CI `sync-guard` job
(see `.github/workflows/docs-health.yml`) re-checks this on every push and
flags the package the moment its copies drift from the canon. Do not edit
these files inside the package: change the canon, then re-copy.

## The formal layer inside the package

`formal/` carries the four independent proof assistants verbatim from the
repository: `lean4` (lake build + the executable `abcloud-verify`
re-derivation), `coq`, `agda` and `isabelle`. They type-check against the
same frozen anchors (see `formal/lean4/ABCloud/Embed.lean`) and are exercised
by the repo's `Formal verification` workflow — the package keeps them so the
formal layer travels with the data and the code it verifies.

## The honesty gate

`hooks/pre_run.sh` refuses to run if `rh_status` is anything but `blocked`.
The same invariant is tested in
[`09_tests/python/test_contract.py`](../09_tests/python/test_contract.py).
