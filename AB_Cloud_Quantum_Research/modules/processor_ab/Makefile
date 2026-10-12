# AB Quantum Processor Program 0.1.0 — самосборка
PY ?= python3

tour:        ## тур вердикта V20 (секунды)
	$(PY) campaigns/run_v20_processor.py

fresh:       ## свежий полный пересчёт V20
	$(PY) scripts/compute_v20.py

compute-all: ## пересчёт всех кампаний
	$(PY) scripts/compute_all.py

tests:       ## тесты
	$(PY) -m pytest tests/ -q

ivp:         ## независимая верификация IV01–IV05 + аудит
	bash independent_verification/RUN_ALL.sh

figures:     ## рисунки 600 dpi × ru/en
	$(PY) scripts/make_figures.py

monographs:  ## монографии PDF/DOCX × ru/en
	$(PY) scripts/make_monographs.py

workbook:    ## таблицы
	$(PY) scripts/build_workbook.py

zip:         ## релизный ZIP + SHA256SUMS
	$(PY) scripts/make_release.py

all: fresh tests ivp figures monographs workbook zip

.PHONY: tour fresh compute-all tests ivp figures monographs workbook zip all
