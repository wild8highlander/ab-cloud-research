# AB-Cloud unified academic package - Makefile
SHELL := /bin/bash
PYTHON ?= python3
RUN := 06_code/python/run.py

.PHONY: help init doctor explain plan validate analyze visualize report monograph lab api test bench lint docs package cite clean checksums reproduce

help:            ## this help
	@grep -hE '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | awk 'BEGIN{FS=":.*?## "}{printf "  \033[36m%-14s\033[0m %s\n", $$1, $$2}'

init:            ## create a project from the template
	$(PYTHON) $(RUN) init

doctor:          ## check environment + package integrity
	$(PYTHON) $(RUN) doctor

explain:         ## human-readable explanation of every step
	$(PYTHON) $(RUN) explain

plan:            ## dry-run of the pipeline
	$(PYTHON) $(RUN) plan

validate:        ## validate config.yaml against config.schema.json
	$(PYTHON) $(RUN) validate

analyze:         ## recompute the consolidated metrics from the registry
	$(PYTHON) $(RUN) analyze

visualize:       ## render figures (600 dpi)
	$(PYTHON) $(RUN) visualize

report:          ## build all report formats
	$(PYTHON) $(RUN) report

monograph:       ## build monographs (PDF via tectonic, DOCX via node)
	bash 06_code/scripts/build_monograph.sh

lab:             ## serve the web laboratory
	cd 07_web_lab && $(PYTHON) -m http.server 8322 || open 07_web_lab/index.html

api:             ## raise the FastAPI service
	$(PYTHON) 07_web_lab/api/main.py

test:            ## run the package integrity suite
	$(PYTHON) -m pytest 09_tests/python -q

bench:           ## quick benchmarks of the six runners
	bash 09_tests/bench_runners.sh

lint:            ## ruff over the python tree
	$(PYTHON) -m ruff check 06_code/python 09_tests/python

docs:            ## build the docs site
	$(PYTHON) -m mkdocs build 2>/dev/null || echo "mkdocs not installed - docs/ holds the sources"

package:         ## build the distributable ZIP
	bash 06_code/scripts/release.sh

cite:            ## print the citation
	$(PYTHON) $(RUN) cite

clean:           ## remove build artefacts
	rm -rf out out_dev out_test .pytest_cache **/__pycache__ 2>/dev/null; true

checksums:       ## refresh data checksums
	$(PYTHON) 06_code/scripts/update_checksums.py

reproduce:       ## one-button reproduction
	bash reproduce.sh
