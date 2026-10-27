# AB Research Program — воспроизведение одним вызовом
PY ?= python3

.PHONY: tour tests ivp figures logo infographics monographs workbook \
        claims all zip fresh

tour:            ## экскурсия по закоммиченным вердиктам V1–V19
        $(PY) campaigns/run_v01_blind_spectrum.py
        $(PY) campaigns/run_v02_null_models.py
        $(PY) campaigns/run_v03_critical_line_scan.py
        $(PY) campaigns/run_v04_operator_passport.py
        $(PY) campaigns/run_v05_lattice_limit.py
        $(PY) campaigns/run_v06_spectral_identity.py
        $(PY) campaigns/run_v07_arithmetic_trace.py
        $(PY) campaigns/run_v08_self_adjointness.py
        $(PY) campaigns/run_v09_symmetry_reduction.py
        $(PY) campaigns/run_v10_inverse_problem.py
        $(PY) campaigns/run_v11_universality_split.py
        $(PY) campaigns/run_v12_interval_certificates.py
        $(PY) campaigns/run_v13_formal_bridge.py
        $(PY) campaigns/run_v14_claim_audit.py
        $(PY) campaigns/run_v15_Li_criterion.py
        $(PY) campaigns/run_v16_full_hamiltonian.py
        $(PY) campaigns/run_v17_electron_critical_line.py
        $(PY) campaigns/run_v18_ab_processor.py
        $(PY) campaigns/run_v19_stitch.py

fresh:           ## свежий полный пересчёт всех кампаний V1–V19 (~12 мин)
        $(PY) scripts/compute_all.py
        $(PY) scripts/compute_v19.py

tests:           ## pytest-сюит (теоремная машинерия + коммиты)
        $(PY) -m pytest tests/ -q

ivp:             ## независимая верификация IVP01–IVP16
        bash independent_verification/RUN_ALL.sh

figures:         ## 20 рисунков × ru/en @600 dpi
        $(PY) scripts/make_figures.py

logo:
        $(PY) scripts/make_logo.py

infographics:
        $(PY) scripts/make_infographics.py

monographs:      ## все монографии RU/EN × DOCX/PDF + 6 теорем + V16–V19
        $(PY) scripts/make_monographs.py

workbook:
        $(PY) scripts/build_workbook.py

claims:
        $(PY) scripts/make_claims.py

readmes:
        $(PY) scripts/make_comp_readmes.py

all: tour tests ivp

zip:             ## самосборка релизного архива
        $(PY) scripts/make_release.py
