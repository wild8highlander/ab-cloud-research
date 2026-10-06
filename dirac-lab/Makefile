# AB-Cloud Dirac Laboratory — Makefile
#
# Canonical suite: code/dirac_lab.py (Python, D1–D8) +
#                  code/dirac_lab_extensions.py (v1.1 extensions, D9–D10) +
#                  code/dirac_lab_extensions2.py (v1.2 extensions II, D11) +
#                  code/dirac_lab_extensions3.py (v1.3 extensions III, D12–D14).
# Independent cross-verification: code/dirac_lab_cross.jl (core),
#                                 code/dirac_lab_cross_ext.jl (D9),
#                                 code/dirac_lab_cross_ext2.jl (D11),
#                                 code/dirac_lab_cross_ext3.jl (D12–D14).
# This folder is autonomous — it does not modify any parent-repository file.

.PHONY: help quick run run-ext run-ext2 run-ext3 test test-ext test-ext2 test-ext3 cross cross-ext cross-ext2 cross-ext3 all benchmark monograph monographs report web figures clean

.DEFAULT_GOAL := help

PYTHON ?= python3
JULIA  ?= julia

help: ## Show help
        @echo "AB-Cloud Dirac Laboratory — commands"
        @echo ""
        @grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
                awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-14s\033[0m %s\n", $$1, $$2}'

quick: ## Fast sanity pass of the core suite (~1 min, no figures)
        $(PYTHON) code/dirac_lab.py --quick --no-figures

run: ## Full core suite D1–D8 with 600-dpi figures (~2-4 min)
        $(PYTHON) code/dirac_lab.py

run-ext: ## Full extensions suite D9–D10 with figures (~3-5 min)
        $(PYTHON) code/dirac_lab_extensions.py

run-ext2: ## Full extensions-II suite D11 with figures (~1 min)
        $(PYTHON) code/dirac_lab_extensions2.py

run-ext3: ## Full extensions-III suite D12–D14 with figures (~5 min)
        $(PYTHON) code/dirac_lab_extensions3.py

all: ## Canonical full run: D1–D14 into one run directory (~8-12 min)
        $(PYTHON) code/dirac_lab.py --resdir results/run_full
        $(PYTHON) code/dirac_lab_extensions.py --resdir results/run_full
        $(PYTHON) code/dirac_lab_extensions2.py --resdir results/run_full
        $(PYTHON) code/dirac_lab_extensions3.py --resdir results/run_full

test: ## Run a single core test: make test D=D7
        $(PYTHON) code/dirac_lab.py --test $(D)

test-ext: ## Run a single extension test: make test-ext D=D9
        $(PYTHON) code/dirac_lab_extensions.py --test $(D)

test-ext2: ## Run the extensions-II test: make test-ext2 D=D11
        $(PYTHON) code/dirac_lab_extensions2.py --test $(D)

test-ext3: ## Run an extensions-III test: make test-ext3 D=D12
        $(PYTHON) code/dirac_lab_extensions3.py --test $(D)

cross: ## Independent Julia cross-verification (core D1/D2/D7/D8)
        $(JULIA) code/dirac_lab_cross.jl

cross-ext: ## Independent Julia cross-verification (D9 wall)
        $(JULIA) code/dirac_lab_cross_ext.jl

cross-ext2: ## Independent Julia cross-verification (D11 Berry–Keating)
        $(JULIA) code/dirac_lab_cross_ext2.jl

cross-ext3: ## Independent Julia cross-verification (D12–D14)
        $(JULIA) code/dirac_lab_cross_ext3.jl

benchmark: ## Measure quick-mode timings of all four modules -> results/PERFORMANCE.md
        $(PYTHON) scripts_gen/benchmark.py

monograph: ## Recompile one per-test monograph with Tectonic: make monograph D=tests/D07_zeta_decoration
        cd $(D) && tectonic monograph.tex

report: ## Open the latest run ledger
        @ls -t results/run_*/REPORT*.md | head -1 | xargs $${PAGER:-less}

web: ## Open both interactive applications in a browser
        $(PYTHON) -c "import webbrowser, pathlib; [webbrowser.open('file://' + str(p.resolve())) for p in [pathlib.Path('webapp/dirac_cone_explorer.html'), pathlib.Path('webapp/wave_packet_lab.html')]]"

figures: ## List the publication figures
        @ls -la figures/

monographs: ## List the monograph files (EN/RU × LaTeX-PDF + DOCX)
        @ls -la monographs/tex monographs/en monographs/ru

clean: ## Remove local run outputs (keeps the canonical committed run)
        rm -rf results/run_202[0-9]*_tmp 2>/dev/null || true
        @echo "note: the canonical committed runs are preserved"
