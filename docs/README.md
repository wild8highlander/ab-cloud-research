<!-- AB-ENRICHED:v1 · section=docs -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&height=90&color=0:05060f,50:526CFE,100:05060f&section=header&text=DOCUMENTATION%20SITE&fontSize=26&fontColor=e5e7eb&fontAlignY=55&animation=fadeIn" alt="DOCUMENTATION SITE" width="100%"/>

<img src="https://readme-typing-svg.demolab.com/?font=JetBrains+Mono&weight=500&size=15&duration=2800&pause=1100&color=526CFE&center=true&vCenter=true&width=760&lines=MkDocs+Material+site;MathJax+everywhere;Deployed+to+GitHub+Pages" alt="Typing: section tagline"/>

</div>
<details>
<summary><strong>🗺️ How <code>docs/</code> connects to the repository (click)</strong></summary>

```mermaid
flowchart LR
    ROOT["🏠 Root README"] --> SEC["Documentation Site"]
    DATA["🧊 Frozen data<br/>verification/data/"] -.-> SEC
    SEC --> OUT["the deployed documentation site"]
    SEC <-.-> SIB["apps · monographs"]
```

</details>

<div align="center">

<img src="assets/banner.svg" alt="Docs — animated banner: the documentation-site browser window with the sidebar navigation filling in, the MathJax formula box glowing, the site cards and the pages rising into the site" width="100%"/>

# 📚 Docs — MkDocs Material Documentation Site

> **🧭 Navigation:** [Root README](../README.md) · [projects/monographs/](../projects/monographs/README.md)

**The sources of the GitHub Pages documentation site
(<https://wild8highlander.github.io/ab-cloud-research>) — the narrative layer of the project,
built with MkDocs Material and auto-deployed on every push to `main`.**

[![MkDocs](https://img.shields.io/badge/MkDocs-Material-1F4E79?style=flat-square&logo=materialformkdocs&logoColor=white)](https://squidfunk.github.io/mkdocs-material/)
[![Pages](https://img.shields.io/badge/site-wild8highlander.github.io-00B8D4?style=flat-square)](https://wild8highlander.github.io/ab-cloud-research)
[![Pages](https://img.shields.io/badge/pages-15-0E7C86?style=flat-square)](#-pages)
[![Math](https://img.shields.io/badge/math-MathJax-8C6D1F?style=flat-square)](#-conventions)
[![Deploy](https://img.shields.io/github/actions/workflow/status/wild8highlander/ab-cloud-research/deploy-docs.yml?branch=main&style=flat-square&label=auto--deploy)](https://github.com/wild8highlander/ab-cloud-research/actions/workflows/deploy-docs.yml)
[![Link check](https://img.shields.io/github/actions/workflow/status/wild8highlander/ab-cloud-research/link-checker.yml?branch=main&style=flat-square&label=link--checker)](https://github.com/wild8highlander/ab-cloud-research/actions/workflows/link-checker.yml)
[![Nav](https://img.shields.io/badge/nav-mkdocs.yml%20%C2%B7%20orphan--free-3A6B4F?style=flat-square)](../mkdocs.yml)

[Pages](#-pages) · [Build locally](#-build-locally) · [Conventions](#-conventions) · [Deep dive](#-deep-dive--the-mkdocs-material-site) · [Summary](#-summary)

</div>

---

## 🗂 Table of contents

<details open>
<summary><strong>Expand / collapse</strong></summary>

1. [📄 Pages](#-pages)
2. [🔧 Build locally](#-build-locally)
3. [📐 Conventions](#-conventions)
4. [🔬 Deep dive — the MkDocs Material site](#-deep-dive--the-mkdocs-material-site)
5. [📁 Complete file inventory](#-complete-file-inventory)
6. [📌 Summary](#-summary)
7. [🔗 Related layers of the project](#-related-layers-of-the-project)

</details>

---

## 📄 Pages

<div align="center">

<img src="assets/avatars.svg" alt="The docs cast: the 12 pages, the MathJax formulas, the GitHub Pages deployment and the mkdocs.yml navigation" width="620"/>

</div>

| Page | Contents |
|---|---|
| [`index.md`](index.md) | landing: what the project is, headline results |
| [`quickstart.md`](quickstart.md) | fastest paths: Julia suite, Python verification, apps |
| [`julia-suite.md`](julia-suite.md) | the 39-test two-pass suite explained (modes, flags, outputs) |
| [`verification.md`](verification.md) | the 10-language verification suite and the three objections |
| [`monographs.md`](monographs.md) | the trilingual v22 monograph package and formats |
| [`monograph-v21.md`](monograph-v21.md) | the original v21 monograph and the v21.1 corrections |
| [`results.md`](results.md) | how to read `results/Test 1-37 ab_cloud_full.jl/run_20260902_134759/` and the reference logs |
| [`audit_v2.0.3.md`](audit_v2.0.3.md) | the repo-wide GOE/GUE audit — v2.0.3 of the error-purge series |
| [`audit_v2.0.4.md`](audit_v2.0.4.md) | the rigidity-slope audit — v2.0.4, a full pass over every README and table |
| [`formal.md`](formal.md) | the formal verification layer: Lean 4 · Coq · Agda · Isabelle |
| [`map.md`](map.md) | one-page map of the whole repository tree |
| [`lab3d.md`](lab3d.md) | the 3D laboratory: modes A–J, committed runs |
| [`citation.md`](citation.md) | citation formats, DOI, ORCID |
| [`faq.md`](faq.md) | frequent questions and misconceptions |
| [`license.md`](license.md) | CC BY-NC-SA 4.0 summary |
| [`javascripts/mathjax.js`](javascripts/mathjax.js) | MathJax bootstrap for inline formulas |

Navigation is defined in [`../mkdocs.yml`](../mkdocs.yml); deployment is automated by the
`deploy-docs` workflow (`.github/workflows/deploy-docs.yml`).

---

## 🔧 Build locally

```bash
pip install mkdocs mkdocs-material
mkdocs serve        # live-reload on http://localhost:8000
mkdocs build        # static site into site/
```

Or from the repository root: `make docs` / `make docs-serve`.

---

## 📐 Conventions

- Pages stay short and link into the repository (the deep documentation lives next to the
  code, in the per-folder READMEs).
- Math is rendered by MathJax; keep formulas in `$…$` / `$$…$$`.
- New pages must be registered in `../mkdocs.yml` `nav:` — otherwise they are orphaned and
  the link-checker workflow flags them.

```mermaid
flowchart LR
    S["docs/*.md<br/>short narrative pages"] -->|"mkdocs build<br/>(make docs)"| B["site/<br/>static bundle"]
    B -->|"deploy-docs.yml<br/>on push to main"| P["GitHub Pages<br/>wild8highlander.github.io"]
    S -.->|"every quoted number<br/>links its artifact"| R["repository artifacts<br/>runs · logs · monographs"]
```

---

## 🔬 Deep dive — the MkDocs Material site

The `docs/` folder is the source of the hosted documentation site
([wild8highlander.github.io/ab-cloud-research](https://wild8highlander.github.io/ab-cloud-research)),
built with MkDocs Material and published automatically by the `deploy-docs.yml` workflow on
every push to `main`. The site is the *narrative* layer of the project: where the README
gives the ledger, the site gives the tour — install guides, theory walkthroughs, per-language
instructions and the gallery, all cross-linked and searchable.

Working with it:

```bash
make docs          # build into site/
make docs-serve    # live-reload preview on localhost:8000
```

Content rules: the site never introduces a number that is not already in a committed
artifact; every page that quotes a result links the artifact, not the other way around.
Navigation order mirrors the reading paths of the root README, so a reader can switch between
README and site without losing their place. The built output (`site/`) is disposable —
`make clean-all` removes it — while sources here are versioned with everything else.

---

## 📁 Complete file inventory

| Entry | Size | Kind |
|---|---|---|
| `assets/` | directory, 3 files inside | folder |
| `javascripts/` | directory, 1 file inside | folder |
| `README.md` | 6.7 KB | markdown guide |
| `audit_v2.0.3.md` | 8.7 KB | markdown guide |
| `audit_v2.0.4.md` | 8.3 KB | markdown guide |
| `citation.md` | 983 B | markdown guide |
| `faq.md` | 1.7 KB | markdown guide |
| `formal.md` | 5.6 KB | markdown guide |
| `index.md` | 1.8 KB | markdown guide |
| `julia-suite.md` | 1.4 KB | markdown guide |
| `lab3d.md` | 875 B | markdown guide |
| `license.md` | 1.2 KB | markdown guide |
| `map.md` | 4.6 KB | markdown guide |
| `monograph-v21.md` | 1.1 KB | markdown guide |
| `monographs.md` | 1.6 KB | markdown guide |
| `quickstart.md` | 1.5 KB | markdown guide |
| `results.md` | 1.2 KB | markdown guide |
| `verification.md` | 1.3 KB | markdown guide |
| **Total (files)** | **49.0 KB** | 16 files + 2 subdirectories |

---

## 📌 Summary

This folder is the source of the MkDocs Material documentation site published to GitHub
Pages by the `deploy-docs` workflow; build it locally with `pip install mkdocs
mkdocs-material && mkdocs serve`. The pages mirror the repository's reading paths, and the
content rule is strict: the site never introduces a number that is not already in a
committed artifact — every page links the artifact, not the other way around.

---

## 🔗 Related layers of the project

| Layer | What it adds |
|---|---|
| [`apps/`](../apps/README.md) | the interactive layer — dashboard + WebGL 3-D laboratory |
| [`projects/monographs/`](../projects/monographs/README.md) | the trilingual monograph editions |
| [`results/`](../results/README.md) | the committed run artifacts the pages link into |
| [`code/`](../code/README.md) | the canonical Julia suite |

---

<p align="center">
  <sub><em>The README gives the ledger; the site gives the tour.</em></sub>
</p>

<div align="center">
<img src="../assets/svg/divider-blue.svg" alt="—" width="100%" height="14"/>

<!-- AI end-cap — prompt P-16, registry: assets/prompts/AI_PROMPTS.md -->
<img src="../assets/banners/banner-docs.webp" alt="AI-rendered section art (prompt P-16)" width="100%"/>

<sub>🖼️ Section art: <a href="../assets/prompts/AI_PROMPTS.md">P-16</a> · palette <code>#05060f · #00e5ff · #ff2ec4 · #a78bfa · #ffd60a</code></sub>

<sub>⚡ Part of <a href="../README.md">AB-Cloud Research</a> — phase resonator for the zeros of the Riemann zeta function · <a href="../README.md">🏠 Root README</a></sub>
</div>
