# Hilbert Polya Bridge — воспроизведение одним вызовом
PY ?= python3

.PHONY: tour tests ivp figures logo infographics monographs workbook all

tour:            ## минутная экскурсия по закоммиченным вердиктам
	$(PY) campaigns/run_c1_identity.py
	$(PY) campaigns/run_c2_argument.py
	$(PY) campaigns/run_c3_gates.py
	$(PY) campaigns/run_c4_trace_formula.py
	$(PY) campaigns/run_c5_gates_ext.py
	$(PY) campaigns/run_c6_primes.py
	$(PY) campaigns/run_c7_dynamics.py
	$(PY) campaigns/run_c8_stats_ladder.py

tests:           ## pytest-сюит
	$(PY) -m pytest tests/ -q

ivp:             ## протокол независимой верификации IVP01–IVP10
	bash independent_verification/RUN_ALL.sh

figures:         ## 16 рисунков × ru/en @ 600 dpi
	$(PY) scripts/make_figures.py

logo:
	$(PY) scripts/make_logo.py

infographics:
	$(PY) scripts/make_infographics.py

monographs:      ## все монографии RU/EN × DOCX/PDF
	$(PY) scripts/make_monographs.py

workbook:
	$(PY) scripts/build_workbook.py

all: tour tests ivp
