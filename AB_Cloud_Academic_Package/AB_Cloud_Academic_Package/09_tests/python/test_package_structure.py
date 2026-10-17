"""The package skeleton must match the unified specification."""
from pathlib import Path


REQUIRED_DIRS = [
    "00_meta", "01_monographs", "02_data", "03_figures", "04_reports",
    "05_logs", "06_code", "07_web_lab", "08_assets", "09_tests", "10_notebooks",
    "docs", "paper", "binder", "colab", "sbom",
    # NOTE: CI workflows live at the REPOSITORY root (.github/workflows/ of
    # ab-cloud-research), not inside the package: GitHub Actions only reads
    # workflows from the repository root, so a package-level .github/ would be
    # dead weight. Removed in the 2026-10 link-repair edition.
]
REQUIRED_FILES = [
    "README.md", "README.ru.md", "README.en.md", "README.zh.md", "README.de.md",
    "README.es.md", "README.fr.md", "README.ar.md",
    "CHANGELOG.md", "CONTRIBUTING.md", "CODE_OF_CONDUCT.md", "SECURITY.md",
    "ROADMAP.md", "AUTHORS.md", "ACKNOWLEDGEMENTS.md", "FAQ.md", "TROUBLESHOOTING.md",
    "LICENSE", "LICENSE-CODE", "LICENSE-TEXT", "LICENSE-DATA",
    "CITATION.cff", "CITATION.bib", "codemeta.json", ".zenodo.json",
    ".gitignore", ".gitattributes", ".editorconfig", ".pre-commit-config.yaml",
    ".dockerignore", ".env.example",
    "Makefile", "Taskfile.yml", "Justfile", "pyproject.toml",
    "config.yaml", "config.schema.json",
    "config.dev.yaml", "config.prod.yaml", "config.test.yaml",
    "reproduce.sh",
    "dataset_card.md", "model_card.md", "system_card.md",
    "datacite.xml", "ro-crate-metadata.json",
    "00_meta/manifest.json", "00_meta/provenance.jsonl", "00_meta/dossier.md",
    "00_meta/glossary/glossary.ru.md", "00_meta/glossary/glossary.en.md",
    "00_meta/glossary/glossary.zh.md", "00_meta/glossary/glossary.schema.json",
    "00_meta/taxonomy/ontology.ttl", "00_meta/governance/RACI.md",
    "02_data/processed/research_registry.json", "02_data/datacard.md",
    "02_data/codebook.md", "02_data/lineage.json", "02_data/checksums.sha256",
    "03_figures/captions.ru.md", "03_figures/captions.en.md",
    "03_figures/figure_index.csv", "03_figures/alt_texts.csv",
    "04_reports/report.md", "04_reports/report.pdf", "04_reports/report.docx",
    "04_reports/executive_summary.md", "04_reports/lay_summary.md",
    "04_reports/press_release.md", "04_reports/policy_brief.md",
    "04_reports/one_pager/one_pager.md", "04_reports/slides/deck.md",
    "05_logs/metrics.json", "05_logs/run.log",
    "06_code/python/run.py", "06_code/julia/run.jl", "06_code/rust/run.rs",
    "06_code/go/run.go", "06_code/js/run.js", "06_code/bash/run.sh",
    "06_code/shared/contract.json", "06_code/shared/metrics.json",
    "06_code/shared/i18n/ru.json", "06_code/shared/i18n/en.json",
    "06_code/cli/run.sh",
    "07_web_lab/index.html", "07_web_lab/app.py", "07_web_lab/api/main.py",
    "08_assets/logos/logo_unified.svg",
    "01_monographs/ru/monograph_ru.md", "01_monographs/ru/monograph_ru.pdf",
    "01_monographs/ru/monograph_ru.docx",
    "01_monographs/en/monograph_en.md", "01_monographs/en/monograph_en.pdf",
    "01_monographs/en/monograph_en.docx",
    "01_monographs/ru/monograph_ru_max.md", "01_monographs/ru/monograph_ru_max.pdf",
    "01_monographs/ru/monograph_ru_max.docx",
    "01_monographs/en/monograph_en_max.md", "01_monographs/en/monograph_en_max.pdf",
    "01_monographs/en/monograph_en_max.docx",
    "02_data/raw/results_run/FINAL_REPORT/final_report.md",
    "02_data/raw/meridian/zeros50k.txt",
    "02_data/raw/vortex_optimization/sweep_C_L96.csv",
    "02_data/raw/wave_attractors/E1_summary.json",
    "03_figures/static/meridian/ru/fig_M1_r_statistics_ru.png",
    "03_figures/static/results_run/ru/fig_R1_v19_verdict_map_ru.png",
    "03_figures/static/vortex_optimization/01_heatmap_D_Nv_q.png",
    "03_figures/static/wave_attractors/03_attractor_vs_control.png",
    "01_monographs/zh/README.md", "01_monographs/de/README.md",
    "01_monographs/es/README.md", "01_monographs/fr/README.md",
    "01_monographs/ar/README.md",
    "10_notebooks/exploration.ipynb",
]
NO_VERSION_MARKERS = [
    # the unified edition is versionless: these tokens must not appear in names
]


def test_dirs(pkg):
    missing = [d for d in REQUIRED_DIRS if not (pkg / d).is_dir()]
    assert not missing, f"missing directories: {missing}"


def test_files(pkg):
    missing = [f for f in REQUIRED_FILES if not (pkg / f).is_file()]
    assert not missing, f"missing files: {missing}"


def test_versionless(pkg):
    """No version numbers in artefact names (the unified edition contract)."""
    bad = []
    for p in pkg.rglob("*"):
        name = p.name.lower()
        if any(tok in name for tok in ("v23", "v34", "v1.0", "v2.0", "version-")):
            if "node_modules" not in str(p) and ".git" not in str(p):
                bad.append(str(p.relative_to(pkg)))
    assert not bad, f"version-marked artefacts found: {bad[:10]}"


def test_every_folder_has_readme(pkg):
    """Every top-level numbered section explains itself."""
    missing = []
    for d in REQUIRED_DIRS:
        if d[0].isdigit():
            if not (pkg / d / "README.md").is_file():
                missing.append(d)
    assert not missing, f"sections without README: {missing}"
