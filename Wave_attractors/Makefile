# AB-Cloud Research — Top-level Makefile
#
# Canonical numerics live in code/ab_cloud_v19.jl (dependency-free Julia).
# The 10-language verification stack lives in verification/.
# The 3D lattice laboratory lives in lab-3d/.

.PHONY: help quick-test test-all menu verify docs docs-serve clean clean-all lint

.DEFAULT_GOAL := help

JULIA  ?= julia
PYTHON ?= python3
NODE   ?= node

help: ## Show help
	@echo "AB-Cloud Research — Makefile commands"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-18s\033[0m %s\n", $$1, $$2}'

quick-test: ## Fast Julia check: 16x16 -> 32x32, zeta <= 5000, both passes (~3-5 min)
	$(JULIA) code/ab_cloud_v19.jl --quick

test-all: ## Full two-pass 37-test Julia suite (30-60 min)
	$(JULIA) code/ab_cloud_v19.jl --test all

wave-attractors: ## Study W1: full hyperbolic wave attractors pipeline (experiments + waves + eta scan + TD + AB + cross-verify + figures)
	cd wave_attractors/scripts && \
	python3 run_experiments.py && \
	python3 e4_frequency.py && \
	python3 wave_directional.py && \
	python3 e6_eta_scan.py && \
	python3 e7_time_domain.py && \
	python3 ab_water.py && \
	python3 dump_reference_csv.py && \
	python3 make_figures.py --lang en --out ../figures && \
	python3 verify_cross.py || echo "verify_cross: run 'make wave-attractors-julia' first (julia output missing)"

wave-attractors-quick: ## Study W1: quick CI protocol (reduced statistics)
	cd wave_attractors/scripts && \
	python3 run_experiments.py --quick && \
	python3 e4_frequency.py && \
	python3 wave_directional.py --quick && \
	python3 e6_eta_scan.py --quick && \
	python3 e7_time_domain.py --quick && \
	python3 ab_water.py && \
	python3 dump_reference_csv.py

wave-attractors-julia: ## Study W1: run the Julia port + TD kernel check (needs julia >= 1.10)
	cd wave_attractors && \
	$$(JULIA) scripts/julia/wave_attractors.jl . && \
	$$(JULIA) scripts/julia/td_check.jl data/julia_td && \
	cd scripts && python3 verify_cross.py && python3 verify_td_cross.py ../data/julia_td_td_snapshots.csv

wave-attractors-verify: ## Study W1: verify reproduction - compare committed reference data vs CAND=<fresh data dir>
	cd wave_attractors/scripts && \
	python3 verify_repro.py --reference ../data --candidate $(CAND)

wave-attractors-docs: ## Study W1: rebuild authored documents (report PDF + RU/EN monograph DOCX) from in-repo sources
	cd wave_attractors/scripts && \
	python3 make_figures.py --lang ru --out ../monograph/ru/figures && \
	python3 make_figures.py --lang en --out ../monograph/en/figures
	cd wave_attractors/scripts/report && \
	python3 w1_report_build.py && python3 w1_merge.py && rm -f _body.pdf
	cd wave_attractors/scripts/monograph && \
	$(NODE) build_monograph.js --lang ru && $(NODE) build_monograph.js --lang en
	cd wave_attractors/monograph && \
	python3 ../../scripts/monograph/postprocess_monograph.py ru/text/AB_Cloud_Monograph_W1_RU.docx && \
	python3 ../../scripts/monograph/add_toc_placeholders.py ru/text/AB_Cloud_Monograph_W1_RU.docx --auto && \
	python3 ../../scripts/monograph/postprocess_monograph.py en/text/AB_Cloud_Monograph_W1_EN.docx && \
	python3 ../../scripts/monograph/add_toc_placeholders.py en/text/AB_Cloud_Monograph_W1_EN.docx --auto

menu: ## Interactive Julia menu (tests + Physics Lab + 3D lab)
	$(JULIA) code/ab_cloud_v19.jl

verify: ## 10-language verification (Python reference implementation)
	cd verification/python && $(PYTHON) ab_cloud_verify.py --zeros ../data/zeta_zeros_50000.txt

docs: ## Build the MkDocs Material site into site/
	mkdocs build --strict

docs-serve: ## Live-reload documentation server on localhost:8000
	mkdocs serve

lint: ## Lint workflow YAML and markdown basics
	$(PYTHON) -m yamllint -s .github/workflows/ 2>/dev/null || echo "yamllint not installed - skipped"
	@markdownlint . 2>/dev/null || echo "markdownlint not installed - skipped (CI enforces it)"

clean: ## Remove generated reports/results of local runs
	rm -rf results/run_* code/reports code/*.log 2>/dev/null || true

clean-all: clean ## Also remove the built documentation site
	rm -rf site
