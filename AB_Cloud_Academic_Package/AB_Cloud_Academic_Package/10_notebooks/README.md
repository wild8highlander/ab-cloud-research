# 10_notebooks

> **🧭 Navigation:** [Package root](../README.md) · [AB_Cloud_Academic_Package/](../../README.md) · [Repo root](../../../README.md)

```mermaid
flowchart LR
    A["09_tests<br/>package integrity suite"] --> B["10_notebooks<br/>notebooks"]
    style B fill:#1f6feb,color:#fff
```

*Layer map of the unified package — the highlighted node is this layer.*

| Notebook | What it does |
|---|---|
| [`exploration.ipynb`](exploration.ipynb) | load the registry, view levels & verdicts |
| [`analysis.ipynb`](analysis.ipynb) | the decisive quantities drawn; flagship results by level |
| [`report.ipynb`](report.ipynb) | regenerate the report tables as dataframes |
| [`tutorial.ipynb`](tutorial.ipynb) | five minutes with the programme (+ CLI from the notebook) |
| [`glossary.ipynb`](glossary.ipynb) | the glossary, live |

All notebooks read only from the funnel
(`02_data/processed/research_registry.json`); reruns are identical.
