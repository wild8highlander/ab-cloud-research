# 05_logs — logs, provenance, metrics

| File | What it is |
|---|---|
| [`metrics.json`](metrics.json) | the machine-readable numbers registry (every entry names its campaign) |
| [`run.log`](run.log) | the package build/doctor run log (human-readable) |
| [`errors.log`](errors.log) | errors only (empty on a clean build) |
| [`warnings.log`](warnings.log) | warnings (typography notes, font fallbacks) |
| [`debug.log`](debug.log) | debug detail of the build pipeline |
| [`audit.log`](audit.log) | audit trail of package operations |
| [`provenance.jsonl`](provenance.jsonl) | step-by-step provenance of the build |
| [`sessions/`](sessions/) | per-run session records |

`metrics.json` is generated from `02_data/processed/research_registry.json` —
the funnel rule applies: displays derive from the registry, never from
hand-typed copies.
