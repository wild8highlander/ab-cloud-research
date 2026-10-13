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

canon:           ## канонический том RU/EN × DOCX/PDF (единая версия)
	$(PY) scripts/make_monographs.py canon

workbook:
	$(PY) scripts/build_workbook.py

all: tour tests ivp

# ── v2.0 targets ──
C12SEG = computations/C12_band_5000/data

v2-campaigns:
	python3 campaigns/run_c9_nonlocal.py
	python3 campaigns/run_c10_phase_coded.py
	python3 campaigns/run_c11_alphathird.py
	python3 campaigns/run_c13_blind.py
	python3 campaigns/run_c14_anomaly.py
	python3 campaigns/run_c15_dirichlet.py
	python3 campaigns/run_c16_qinfo.py

v2-band:
	python3 campaigns/run_c12_band5000.py --segment 0 1000 $(C12SEG)/seg_1.npz
	python3 campaigns/run_c12_band5000.py --segment 1000 1500 $(C12SEG)/seg_2.npz
	python3 campaigns/run_c12_band5000.py --segment 1500 2000 $(C12SEG)/seg_3.npz
	python3 campaigns/run_c12_band5000.py --segment 2000 2500 $(C12SEG)/seg_4.npz
	python3 campaigns/run_c12_band5000.py --segment 2500 3000 $(C12SEG)/seg_5.npz
	python3 campaigns/run_c12_band5000.py --segment 3000 3250 $(C12SEG)/seg_6a.npz
	python3 campaigns/run_c12_band5000.py --segment 3250 3500 $(C12SEG)/seg_6b.npz
	python3 campaigns/run_c12_band5000.py --segment 3500 3750 $(C12SEG)/seg_7a.npz
	python3 campaigns/run_c12_band5000.py --segment 3750 4000 $(C12SEG)/seg_7b.npz
	python3 campaigns/run_c12_band5000.py --segment 4000 4250 $(C12SEG)/seg_8a.npz
	python3 campaigns/run_c12_band5000.py --segment 4250 4500 $(C12SEG)/seg_8b.npz
	python3 campaigns/run_c12_band5000.py --segment 4500 4750 $(C12SEG)/seg_9a.npz
	python3 campaigns/run_c12_band5000.py --segment 4750 5000 $(C12SEG)/seg_9b.npz
	python3 campaigns/run_c12_band5000.py --assemble

v2-figures:
	python3 scripts/make_figures_v2.py
	python3 scripts/make_animations_v2.py

v2-explorer:
	streamlit run explorer/streamlit_app.py

v2-challenge:
	python3 challenge/score_submission.py challenge/examples/example_gate.json

v2: v2-campaigns v2-figures
	bash independent_verification/RUN_ALL.sh
	python3 -m pytest tests/ -q
