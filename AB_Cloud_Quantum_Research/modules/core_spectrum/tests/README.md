# tests/ — pytest-сюит пакета

| Файл | Теорема/кампания | Тип источника |
|------|------------------|---------------|
| test_th1_passport.py | Th1 (эрмитовость) | живой пересчёт |
| test_th2_selfadjoint.py | Th2 (самосопряжённость) | живой пересчёт |
| test_th3_certificates.py | Th3 (сертификаты) | коммит V12 |
| test_th4_li.py | Th4 (формула Ли) | живой пересчёт (50k) |
| test_th5_block_reduction.py | Th5 (блочная редукция) | живой пересчёт |
| test_th6_trace_formula.py | Th6 (следовая формула) | живой пересчёт (20k) |
| test_blind_and_nulls.py | V1/V2 | коммиченные вердикты |
| test_formal_blocked.py | V13 | машина обязательств |
| test_audit.py | V14 | аудит claims |
| test_repro.py | воспроизводимость | 15 кампаний + meta |

Запуск: `python3 -m pytest tests/ -q` (~6 с). Ни один тест не требует
сети или внешних тулчейнов.
