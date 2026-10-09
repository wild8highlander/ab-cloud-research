# .github — CI, Automation and Community Health Files

Everything that configures how GitHub treats this repository. Nothing here
runs locally; it is read by GitHub Apps and Actions.

## Workflows (`workflows/`)

| Workflow | File | What it does |
|---|---|---|
| CI | `ci.yml` | canonical-artifact presence checks (v23 suite, formal layer, monographs, CITATION.cff), CITATION.cff validation (cffconvert), markdownlint (curated surface, `.markdownlint-cli2.jsonc`), workflow YAML lint (yamllint, `.yamllint.yaml`) |
| Julia suite | `julia.yml` | parse check of `code/ab_cloud_v23.jl` + smoke run (`--test 1`, ~1 min) on every push/PR/week; the **full two-pass 39-test suite** runs on demand via `workflow_dispatch` |
| Formal verification | `formal.yml` | compiles the formal layer in **four proof assistants**: Lean 4 (`lake build` + `lake exe abcloud-verify` — the 8/8 frozen-reference gate), Coq (`coq_makefile && make`), Agda (`agda -i . -i .`), Isabelle/HOL (`isabelle build -D formal/isabelle`, official docker image) |
| Docs deploy | `deploy-docs.yml` | builds the MkDocs Material site (`docs/`) with **pinned versions** (mkdocs 1.6.1 / material 9.7.7) and publishes it to GitHub Pages |
| CodeQL | `codeql.yml` | static security analysis of the Python code |
| Link checker | `link-checker.yml` | crawls the repo markdown for dead links on a schedule |
| Release drafter | `release-drafter.yml` | assembles release notes from merged PRs, tags versions |
| Dependency review | `dependency-review.yml` | flags vulnerable/dependency changes on PRs |
| Stale | `stale.yml` | marks/removes abandoned issues and PRs |

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
| `dependabot.yml` | weekly bumps for GitHub Actions and npm/pip ecosystems |
| `labeler.yml` | auto-labels PRs by touched paths (`monographs`, `verification`, `apps`, …) |
| `release-drafter.yml` | categories/labels → release-notes sections mapping |
| `CODEOWNERS` | default reviewers: `@wild8highlander` for everything |
| `FUNDING.yml` | funding links shown in the repo's Sponsor tab |

## Linter configs (repository root)

| File | Used by |
|---|---|
| `.yamllint.yaml` | the `yaml` job of `ci.yml` (workflow lint) |
| `.markdownlint-cli2.jsonc` | the `markdown` job of `ci.yml` (curated markdown surface) |

## Local reproduction of CI checks

```bash
make lint                                    # markdownlint + YAML sanity
julia code/ab_cloud_v23.jl --test 1          # the same smoke run julia.yml executes
cd formal/lean4 && lake build && lake exe abcloud-verify   # the formal gate
python3 verification/sections/section3_ab_cloud/python/verify.py   # smoke test
```

## Кратко (по-русски)

- Служебная папка GitHub: 9 воркфлоу (CI, Julia-сюит v23 со смоук-прогоном,
  формальная верификация Lean4/Coq/Agda/Isabelle, сборка документации на
  Pages с закреплёнными версиями, CodeQL, проверка ссылок, release-drafter,
  dependency-review, stale), шаблоны issue/PR, dependabot, авторазметка,
  CODEOWNERS.
- Локально повторяются: `make lint`, `julia code/ab_cloud_v23.jl --test 1`
  и `lake exe abcloud-verify` в `formal/lean4/`.
