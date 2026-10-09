# AB-Cloud Research — Top-level Makefile
#
# Canonical numerics live in code/ab_cloud_v23.jl (dependency-free Julia).
# The 10-language verification stack lives in verification/.
# The formal layer (Lean 4 · Coq · Agda · Isabelle) lives in formal/.
# The 3D lattice laboratory lives in lab-3d/.

.PHONY: help smoke quick-test test-all menu verify formal formal-lean formal-coq \
        formal-agda formal-isabelle docs docs-serve lint clean clean-all

.DEFAULT_GOAL := help

JULIA  ?= julia
PYTHON ?= python3

help: ## Show help
	@echo "AB-Cloud Research — Makefile commands"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033%-18s\033 %s\n", $$1, $$2}'

smoke: ## One-test smoke run of the v23 suite (Test 1, embedded zeros, ~1 min)
	$(JULIA) code/ab_cloud_v23.jl --test 1

quick-test: ## Fast Julia check: 16x16 -> 32x32, zeta <= 5000, both passes (~3-5 min)
	$(JULIA) code/ab_cloud_v23.jl --test 1

test-all: ## Full two-pass 39-test Julia suite (30-60 min)
	$(JULIA) code/ab_cloud_v23.jl --test all

menu: ## Interactive Julia menu (tests + Physics Lab + 3D lab)
	$(JULIA) code/ab_cloud_v23.jl

verify: ## 10-language verification (Python reference implementation)
	cd verification/python && $(PYTHON) run_verify.py --zeros 5000 --objection all --lang en

formal: ## Formal layer: compile all four assistants + run the Lean re-derivation
	$(MAKE) formal-lean
	$(MAKE) formal-coq
	$(MAKE) formal-agda
	$(MAKE) formal-isabelle

formal-lean: ## Lean 4: lake build + the abcloud-verify re-derivation gate
	cd formal/lean4 && lake build && lake exe abcloud-verify

formal-coq: ## Coq: compile ABCloud/Core.v and print the certified computations
	cd formal/coq && coq_makefile -f _CoqProject -o Makefile.coq && $(MAKE) -f Makefile.coq -j2

formal-agda: ## Agda: type-check the builtins-only development
	cd formal/agda && agda -i . -i . ABCloud.agda

formal-isabelle: ## Isabelle/HOL: build the ABCloud session
	isabelle build -D formal/isabelle

docs: ## Build the MkDocs Material site into site/
	mkdocs build --strict

docs-serve: ## Live-reload documentation server on localhost:8000
	mkdocs serve

lint: ## Lint workflow YAML and the curated markdown surface
	$(PYTHON) -m yamllint -c .yamllint.yaml .github/workflows/ 2>/dev/null || echo "yamllint not installed - skipped"
	@markdownlint-cli2 2>/dev/null || echo "markdownlint-cli2 not installed - skipped (CI enforces it)"

clean: ## Remove generated reports/results of local runs
	rm -rf results/run_* code/reports code/*.log verification/*/objection*.png verification/*/verify_report*.txt 2>/dev/null || true

clean-all: clean ## Also remove the built documentation site
	rm -rf site
