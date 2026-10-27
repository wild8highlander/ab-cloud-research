# .github — CI, Automation and Community Health Files

Everything that configures how GitHub treats this repository. Nothing here
runs locally; it is read by GitHub Apps and Actions.

## Workflows (`workflows/`)

| Workflow | File | What it does |
|---|---|---|
| CI | `ci.yml` | canonical-artifact presence checks (v23 suite, formal layer, monographs, frozen ζ-zero datasets, package registry, CITATION.cff), CITATION.cff validation (cffconvert), markdownlint (curated surface incl. the Academic Package's authored docs and Meridian docs, `.markdownlint-cli2.jsonc`), YAML lint over **every tracked YAML file** (yamllint, `.yamllint.yaml`), **JSON/TOML validity over every tracked file** + `bash -n` over every shell script (`check_data_formats.py`), **ruff** (real-defect gate: `ruff.toml`), **pytest** (all five Python test suites — the unified, processor, core-spectrum and Hilbert–Polya suites **+ the Academic Package contract suite** — plus smoke runs of the package's Python clone and the Vortex engine) |
| Docs health | `docs-health.yml` | documentation & sync integrity on every push: **internal links & anchors over every tracked `.md`** (GitHub annotations), **README coverage** (every documented directory), **package ⇄ canon sync-guard** (byte-copies of the Julia suite, HP audit, D-variants, formal layer, frozen zeros + verdict-layer ⇄ registry consistency) — plus a weekly **lychee** crawl of external links (report-only artifact) |
| Repo integrity | `repo-integrity.yml` | whole-repository file integrity on every push: **workflow trigger sanity** (every `push`/`pull_request` branch filter must include `main` — catches silently-dead CI), **SHA256 verification of every committed manifest** (`SHA256SUMS.txt`, `manifest.sha256`, `checksums.sha256`), **CSV parse**, **SVG/XML well-formedness** and **nbformat notebook validation** over every tracked file of the respective kind |
| Polyglot syntax gate | `polyglot.yml` | every code file in the repository must parse in its language: Julia (`Meta.parseall` over all `.jl`), Go (`go vet ./...` per module), Rust (`cargo check --offline` per crate — all dependency-free), C/C++ (`g++ -fsyntax-only`), Fortran (`gfortran -cpp -fsyntax-only`), Java (`javac`), JavaScript (`node --check`), R (`parse`); Python/shell are covered by ci.yml's ruff and data-formats jobs — see the matrix in the file header for the documented exclusions (matlab, haskell) |
| Julia suite | `julia.yml` | parse check of `code/ab_cloud_full.jl` + smoke run (`--test 1`, ~1 min) on every push/PR/week; the **full two-pass 39-test suite** runs on demand via `workflow_dispatch` |
| Formal verification | `formal.yml` | compiles the formal layer in **four proof assistants**: Lean 4 (`lean-action` → `lake build` + `lake exe abcloud-verify` — the 8/8 frozen-reference gate), Coq (`coq_makefile && make`), Agda (`agda -i . -i .`), Isabelle/HOL (`isabelle build -D formal/isabelle`, official docker image) |
| Docs deploy | `deploy-docs.yml` | builds the MkDocs Material site (`docs/`) with **pinned versions** (mkdocs 1.6.1 / material 9.7.7) and publishes it to GitHub Pages |
| CodeQL | `codeql.yml` | static security analysis of the Python code |
| Release drafter | `release-drafter.yml` | assembles release notes from merged PRs, tags versions |
| Dependency review | `dependency-review.yml` | flags vulnerable/dependency changes on PRs |
| Stale | `stale.yml` | marks/removes abandoned issues and PRs |
| PR labeler | `labeler.yml` | applies path-based labels from `.github/labeler.yml` (`julia-suite`, `verification`, `3d-lab`, `monographs`, `academic-package`, `core-modules`, `formal`, `web-lab`, `documentation`, `data`, `ci`) |
| First interaction | `first-interaction.yml` | greets first-time issue/PR authors with pointers to CONTRIBUTING.md and the PR checklist |
| Dependabot auto-merge | `dependabot-auto-merge.yml` | enables squash auto-merge for Dependabot **patch/minor** bumps once CI is green (major bumps stay manual) |

Action versions are kept current by Dependabot; the tree already incorporates
the 2026-10 bump wave (`checkout@v7`, `markdownlint-cli2-action@v24`,
`stale@v11`, `setup-julia@v3`, `release-drafter@v7`).

## Templates and bots

| File | Purpose |
|---|---|
| `ISSUE_TEMPLATE/bug_report.yml` | structured bug form (component, version, steps) |
| `ISSUE_TEMPLATE/feature_request.yml` | structured feature form |
| `ISSUE_TEMPLATE/config.yml` | disables blank issues, adds contact links |
| `PULL_REQUEST_TEMPLATE.md` | PR checklist (tests run, docs updated, CHANGELOG entry) |
| `dependabot.yml` | weekly bumps for GitHub Actions; monthly bumps for pip (`lab-3d`, `modules/core_spectrum`, `modules/processor_ab`, `projects/hilbert-polya`, the package's `06_code`), npm (`scripts/monograph`, both `apps/`), gomod and cargo (every module/crate in the repo) |
| `labeler.yml` | path → label mapping consumed by the `labeler.yml` workflow |
| `docs-health-allowlist.json` | the docs-health ratchet: known-broken link classes in auto-generated/historical artifacts (keep short and shrinking) |
| `release-drafter.yml` | categories/labels → release-notes sections mapping |
| `CODEOWNERS` | default reviewers: `@wild8highlander` for everything |
| `FUNDING.yml` | funding links shown in the repo's Sponsor tab |

## Linter configs (repository root)

| File | Used by |
|---|---|
| `.yamllint.yaml` | the `yaml` job of `ci.yml` (every tracked YAML file) |
| `.markdownlint-cli2.jsonc` | the `markdown` job of `ci.yml` (curated markdown surface — the glob list itself lives in this config) |
| `.github/scripts/docs_health.py` | the three gates of `docs-health.yml` (`links`, `readmes`, `sync`) |
| `.github/scripts/check_data_formats.py` | the `data-formats` job of `ci.yml` (JSON/TOML validity + `bash -n`) |
| `ruff.toml` | the `ruff` job of `ci.yml` (Python real-defect gate: E9, F821, F402, F404, F811) |
| `projects/lab-3d/pyproject.toml → [tool.ruff.lint]` | same rule set for the `projects/lab-3d/` subtree (nearest-config discovery) |
| `.editorconfig` | editor/IDE whitespace consistency for all file types |

## Local reproduction of CI checks

```bash
make lint                                    # markdownlint + YAML sanity
ruff check .                                 # Python real-defect gate
python3 .github/scripts/docs_health.py all   # links + readmes + package⇄canon sync
python3 .github/scripts/check_data_formats.py  # JSON/TOML validity + bash -n
python3 -m pytest projects/quantum-research/tests -q     # unified suite
python3 -m pytest projects/quantum-research/modules -q   # module suites
python3 -m pytest projects/academic-package/09_tests/python -q  # package contract suite
python3 -m pytest projects/hilbert-polya/tests -q      # Hilbert-Polya suite
julia code/ab_cloud_full.jl --test 1          # the same smoke run julia.yml executes
cd formal/lean4 && lake build && lake exe abcloud-verify   # the formal gate
python3 verification/sections/section3_ab_cloud/python/verify.py   # smoke test
```

## Repo settings to enable once (web UI)

Some GitHub features are repository settings, not files — flip them once in
**Settings**:

- **Branch protection** for `main`: require the `CI`, `Julia suite`, `CodeQL`,
  `Docs health`, `Polyglot syntax gate` and `Formal verification` checks,
  require branches up to date, allow Dependabot auto-merge to take effect.
- **Security → Code security**: secret scanning + push protection.
- **General → Pull requests**: allow squash merging (auto-merge uses it),
  enable automatically delete head branches (cleans up stale Dependabot
  branches after merge).

## Кратко (по-русски)

- Служебная папка GitHub: 14 воркфлоу (CI с ruff, pytest по всем сюитам пакета,
  валидацией каждого JSON/TOML и bash-скрипта, markdownlint по авторской
  документации, yamllint по всему репозиторию; **docs-health** — битые ссылки и
  якоря во всех `.md` при каждом пуше + покрытие README + sync-guard
  «пакет ⇄ канон» + недельный lychee-обход внешних ссылок; **polyglot** —
  синтаксис-гейт каждого кодового файла: Julia/Go/Rust/C-C++/Fortran/Java/JS/R;
  **repo-integrity** — sanity триггеров воркфлоу, проверка всех SHA256-манифестов,
  парсинг каждого CSV, SVG/XML и ноутбука; Julia-сюит со смоук-прогоном,
  формальная верификация
  Lean4/Coq/Agda/Isabelle, сборка документации на Pages, CodeQL,
  release-drafter, dependency-review, stale, авторазметка PR, приветствие
  новичков, авто-мерж Dependabot), шаблоны issue/PR, dependabot (actions +
  pip + npm + gomod + cargo по всем модулям), авторазметка, CODEOWNERS.
- Локально повторяются: `make lint`, `ruff check .`,
  `python3 .github/scripts/docs_health.py all`, `pytest`,
  `julia code/ab_cloud_full.jl --test 1` и `lake exe abcloud-verify`
  в `formal/lean4/`.
- Разово в Settings: защита ветки `main` (теперь требует также Docs health
  и Polyglot), secret scanning, squash-merge и авто-удаление головных веток.
