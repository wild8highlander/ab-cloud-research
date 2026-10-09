# tests/ — pytest-сюит серии

| Файл | Теорема/критерий | Источник |
|------|------------------|----------|
| test_gamma_closures.py | T1 | живой пересчёт (dps 40) |
| test_zid_reality.py | T2 | живой пересчёт |
| test_trace_formula.py | T6 | закоммиченный C4 |
| test_gates_gue.py | T7 | закоммиченная C5 |
| test_protocol_repro.py | база C3 | живой пересчёт (бит-в-бит) |
| test_colocation.py | T4 | закоммиченная C6 |

Запуск: `python3 -m pytest tests/ -q`. Ни один тест не требует файла нулей.
