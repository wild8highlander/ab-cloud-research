<!-- AB-ENRICHED:v1 · sub -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venice&height=48&color=0:ffd60a,100:05060f&section=header" alt="" width="100%"/>

**🧭 [⬆ AB_Cloud_Academic_Package/](../README.md) · [🏠 Root README](../../../README.md)**

</div>
# 05_logs — logs, provenance, metrics

> **🧭 Navigation:** [Package root](../README.md) · [AB_Cloud_Academic_Package/](../../README.md) · [Repo root](../../../README.md)

```mermaid
flowchart LR
    A["04_reports<br/>the report suite"] --> B["05_logs<br/>logs · provenance · metrics"] --> C["06_code<br/>unified CLI · six languages, one contract"]
    style B fill:#1f6feb,color:#fff
```

*Layer map of the unified package — the highlighted node is this layer.*

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

<div align="center">

<img src="../../../assets/svg/divider-gold.svg" alt="—" width="100%" height="12"/>
<sub>⚡ Part of <a href="../../../README.md">AB-Cloud Research</a> — numbers are verbatim from the unified registry; no result on this page is a claim about the Riemann hypothesis · <a href="../README.md">⬆ parent section</a></sub>

</div>
