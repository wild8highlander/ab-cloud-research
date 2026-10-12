# 🧪 tests/ — тесты целостности пакета AB Cloud Quantum Research

`test_unified.py` — smoke-тесты пакета (запуск: `python3 tests/test_unified.py`
или `make test`). Проверяют:

1. структуру (11 обязательных папок);
2. **12 документов теорем** (6 × RU/EN × PDF/DOCX) в `theorems_lemmas/`;
3. **12 плиточных фигур** в `figures_tiled/{ru,en}/`;
4. вердикты Julia-серии: `verdicts_master.json` — **все 18 PASS**;
5. машину обязательств core_rp: вердикт RH — `blocked`;
6. формальные файлы: `sorry`/`Admitted` отсутствуют в RPTheorems;
7. вкладку «Теоремы» в обеих веб-лабораториях + портал трёх программ;
8. полный `scripts/validate_package.py` (40+ проверок) завершается успехом.

Каждая программа-компонент несёт СВОИ тесты: core_rp — 42 pytest-теста
(`modules/core_spectrum/tests/`), QP — 19 (`test_v20_processor.py`),
Julia — собственные самотесты внутри экспериментов + независимая верификация
(`independent_verification/RUN_ALL.sh` в core_rp и QP).

## English summary

`test_unified.py` smoke-tests the package: structure, the 12 theorem documents,
12 tiled figures, 18/18 Julia verdicts, the blocked-RH obligation machine,
no `sorry`/`Admitted` in the formal statements, the theorems tab in both web
labs, and a full `validate_package.py` pass. Component packages keep their
own test suites (42/19/…).
