# docs — MkDocs Material Documentation Site

The sources of the GitHub Pages documentation site
(<https://wild8highlander.github.io/ab-cloud-research>), built with
**MkDocs Material**. Navigation is defined in `../mkdocs.yml`; deployment
is automated by the `deploy-docs` workflow (`.github/workflows/deploy-docs.yml`).

## Pages

| Page | Contents |
|---|---|
| `index.md` | landing: what the project is, headline results |
| `quickstart.md` | fastest paths: Julia suite, Python verification, apps |
| `julia-suite.md` | the 37-test two-pass suite explained (modes, flags, outputs) |
| `verification.md` | the 10-language verification suite and the three objections |
| `monographs.md` | the trilingual v22 monograph package and formats |
| `monograph-v21.md` | the original v21 monograph and the v21.1 corrections |
| `results.md` | how to read `results/run_20260902_134759/` and the reference logs |
| `lab3d.md` | the 3D laboratory: modes A–J, committed runs |
| `citation.md` | citation formats, DOI, ORCID |
| `faq.md` | frequent questions and misconceptions |
| `license.md` | CC BY-NC-SA 4.0 summary |
| `javascripts/mathjax.js` | MathJax bootstrap for inline formulas |

## Build locally

```bash
pip install mkdocs mkdocs-material
mkdocs serve        # live-reload on http://localhost:8000
mkdocs build        # static site into site/
```

Or from the repository root: `make docs` / `make docs-serve`.

## Conventions

- Pages stay short and link into the repository (the deep documentation
  lives next to the code, in the per-folder READMEs).
- Math is rendered by MathJax; keep formulas in `$…$` / `$$…$$`.
- New pages must be registered in `../mkdocs.yml` `nav:` — otherwise they
  are orphaned and the link-checker workflow flags them.

## Кратко (по-русски)

- Исходники сайта документации (MkDocs Material), публикуемого на GitHub
  Pages воркфлоу `deploy-docs`.
- Локально: `pip install mkdocs mkdocs-material && mkdocs serve`.
- Страницы: quickstart, julia-suite, verification, monographs (+v21),
  results, lab3d, citation, faq, license; навигация — в `mkdocs.yml`.
