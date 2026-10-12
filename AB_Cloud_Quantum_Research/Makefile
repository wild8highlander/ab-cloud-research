# AB Cloud Quantum Research v1.0.0
PY = python3

.PHONY: help validate figures docs readmes banner spinor spinor-figs spinor-docs datasets atlas timeline whitepaper test core-tests qp-campaign julia release clean

help:
	@echo "validate      — самопроверка целостности пакета (95+ проверок)"
	@echo "figures       — плиточные фигуры 2x2 (12 шт, 600 dpi)"
	@echo "docs          — 12 документов теорем Th1-Th6 (RU/EN x PDF/DOCX)"
	@echo "readmes       — README папок теорем"
	@echo "banner        — анимированный баннер + лого"
	@echo "spinor        — кампании ES1-ES5 вспомогательного исследования"
	@echo "spinor-figs   — 8 плиток исследования (600 dpi)"
	@echo "spinor-docs   — 12 документов теорем TS1-TS3"
	@echo "datasets      — курируемые данные (флагманы, хронология, нули)"
	@echo "atlas         — атлас флагманов (600 dpi)"
	@echo "timeline      — хронология 43 кампаний (600 dpi)"
	@echo "whitepaper    — белый отчёт (RU/EN PDF)"
	@echo "test          — smoke-тесты пакета"
	@echo "core-tests    — pytest ядра"
	@echo "qp-campaign   — пересчёт V20"
	@echo "julia         — полный прогон E01-E18"
	@echo "release       — SHA256SUMS + ZIP в download/"

validate:
	$(PY) scripts/validate_package.py
figures:
	$(PY) scripts/make_tiled_figures.py
docs:
	$(PY) scripts/make_theorem_docs.py
readmes:
	$(PY) scripts/make_theorem_readmes.py
banner:
	$(PY) scripts/make_banner.py
spinor:
	cd research/realtime_spinor_memory && $(PY) experiments/run_all.py
spinor-figs:
	cd research/realtime_spinor_memory && $(PY) make_figures.py
spinor-docs:
	cd research/realtime_spinor_memory && $(PY) make_theorem_docs.py
datasets:
	$(PY) scripts/make_datasets.py
atlas:
	$(PY) scripts/make_atlas.py
timeline:
	$(PY) scripts/make_timeline.py
whitepaper:
	$(PY) scripts/make_whitepaper.py
test:
	$(PY) tests/test_unified.py
core-tests:
	cd modules/core_spectrum && $(PY) -m pytest tests/ -q
spinor-tests:
	cd research/realtime_spinor_memory && $(PY) -m pytest tests/ -q
qp-campaign:
	$(PY) modules/processor_ab/scripts/compute_v20.py
julia:
	julia modules/verifier_multilang/experiments/run_all.jl all
release:
	$(PY) scripts/make_release.py
clean:
	find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null; true
