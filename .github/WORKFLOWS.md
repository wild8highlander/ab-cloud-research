# .github — CI, Automation and Community Health Files

Everything that configures how GitHub treats this repository. Nothing here
runs locally; it is read by GitHub Apps and Actions.

## Workflows (`workflows/`)

| Workflow | File | What it does |
|---|---|---|
| CI | `ci.yml` | markdownlint + basic link sanity on every PR/push; runs the section micro-verifications (`verification/sections/*/python/verify.py`) as smoke tests |
| Julia tests | `julia.yml` | `julia code/ab_cloud_v19.jl --quick` (16×16 → 32×32, ζ ≤ 5000, both passes, ~3–5 min) — proves the canonical suite still runs |
| Docs deploy | `deploy-docs.yml` | builds the MkDocs Material site (`docs/`) and publishes it to GitHub Pages |
| CodeQL | `codeql.yml` | static security analysis of the JavaScript/Python code |
| Link checker | `link-checker.yml` | crawls the repo markdown for dead links on a schedule |
| Release drafter | `release-drafter.yml` | assembles release notes from merged PRs, tags versions |
| Dependency review | `dependency-review.yml` | flags vulnerable/dependency changes on PRs |
| Stale | `stale.yml` | marks/removes abandoned issues and PRs |

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

## Local reproduction of CI checks

```bash
make lint                       # markdownlint + YAML sanity
julia code/ab_cloud_v19.jl --quick   # the same command julia.yml runs
python3 verification/sections/section3_ab_cloud/python/verify.py   # smoke test
```

## Кратко (по-русски)

- Служебная папка GitHub: 8 воркфлоу (CI, Julia --quick, сборка документации
  на Pages, CodeQL, проверка ссылок, release-drafter, dependency-review,
  stale), шаблоны issue/PR, dependabot, авторазметка, CODEOWNERS.
- Локально повторяются две проверки: `make lint` и
  `julia code/ab_cloud_v19.jl --quick`.
