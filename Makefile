# AB-Cloud Research — Top-level Makefile
#
# Canonical numerics live in code/ab_cloud_v19.jl (dependency-free Julia).
# The 10-language verification stack lives in verification/.
# The 3D lattice laboratory lives in lab-3d/.

.PHONY: help quick-test test-all menu verify docs docs-serve clean clean-all lint

.DEFAULT_GOAL := help

JULIA  ?= julia
PYTHON ?= python3

help: ## Show help
	@echo "AB-Cloud Research — Makefile commands"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-18s\033[0m %s\n", $$1, $$2}'

quick-test: ## Fast Julia check: 16x16 -> 32x32, zeta <= 5000, both passes (~3-5 min)
	$(JULIA) code/ab_cloud_v19.jl --quick

test-all: ## Full two-pass 37-test Julia suite (30-60 min)
	$(JULIA) code/ab_cloud_v19.jl --test all

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
