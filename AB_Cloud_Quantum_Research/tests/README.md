<!-- enriched 1.1.0 -->
<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/logo_abcloud_dark.png">
  <img src="../assets/logo_abcloud_light.png" width="92" alt="AB Cloud Quantum Research">
</picture>

### 🧪 Tests — smoke integrity

`AB Cloud Quantum Research` · v1.1.0 · part of one machine

![badge](https://img.shields.io/badge/program-AB_Cloud_Quantum_Research-C96F4A?style=flat-square)
![badge](https://img.shields.io/badge/verdicts-all%20PASS-3A6B4F?style=flat-square)
![badge](https://img.shields.io/badge/license-proprietary-6B6455?style=flat-square)

</div>

> 🧭 **Navigation:** [↑ main README](../README.md) · [📚 monographs](../MONOGRAPH_ARCHIVE/README.md) · [🧪 hypothesis lab](../HYPOTHESIS_LAB/README.md) · [🎞 animations](../VISUAL_ANIMATIONS/README.md)
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

---

<div align="center">

<img src="../assets/avatars/avatar_author.svg" width="84" alt="author">

*Part of the discipline: pre-registration · blind protocols · replication ·
negative results published*

**AB Cloud Quantum Research** · v1.1.0 ·
[license](../../LICENSE) · © Isaev Iskhak Khamzatovich

</div>
