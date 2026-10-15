# Аудит v2.0.9 — полнота распространения вердиктов v2.0.7/v2.0.8 по оставшимся прогонам

**Дата:** 2026-10-15 · **Статус:** применена · **Триггер:** указание
пользователя «продолжить поиск ошибок в остальных прогонах репозитория»
после синхронизации артефактов (CHANGELOG 2.0.9 / [1.3.7]).

## 1. Суть проблемы

Коррекции вердиктов v2.0.7 (H2 = ДА на уровне нулей) и v2.0.8 (H5 = ДА по
лестнице сходимости) были применены к центральным поверхностям (главные
README, C1–C6/C8, монографии v1-томов) — но **не дошли** до кампаний
C7/C9/C11/C13/C15/C16, генераторов, explorer, docs/v2, аудита канонизации
и пакета `AB_Cloud_Quantum_Research` (Th1, RESULTS, V07). Там сохранялись
формулировки эпохи «H2 = НЕТ»:

- «the H2 gap is universal / УНИВЕРСАЛЕН» (C15, preprint, streamlit,
  make_figures_v2, docs/v2, hpbridge, аудит-отчёт);
- «H2 is a wall of LOCALITY» без указания ветви (C9, fig25, streamlit);
- «identity does not» для моста α = ½ ↔ Re(s) = ½ (C7 ru/en, canon,
  en/ru_part2, генератор) — при том, что уровень нулей теперь ДА (v2.0.7);
- «Every other verdict in this package is a negative» (C11);
- «never through spectral identity» (C16);
- цитата старого вердикта C13 в README при обновлённом JSON;
- «negative verdicts (V1, V3, V6, V16)» в границах Th1 (json ru/en, README,
  генератор, монография core_spectrum) — при V6/V16 = ДА (мост D_nn);
- ряды 8 и 28 RESULTS.md core_spectrum: «rank 0.036 — НЕТ»,
  «тождество НЕ замыкается».

## 2. Реальные дефекты (не только текст)

1. **V07 `gap_orders` считался не той формулой.** В
   `rpbridge/arithmetic_trace.py`:
   `log10(pc0_r / max|r_EF|)` = **0.0027** — зазор в единицах корреляции,
   тогда как вся документация (README, RESULTS ряд 14, ROADMAP) заявляет
   «**0.63 порядка по невязке**» = log10(0.1153/0.0273). Формула исправлена
   на log10(min resid / pc0_resid); закоммиченный JSON перезаписан значением
   **0.6249913**, вычисленным из тех же закоммиченных чисел (измерения
   не тронуты).
2. **V07 verdict_note скрывал лучший затвор.** «Гребёнка невидима (r_EF в
   нулевых облаках)» — при батарее 8 затворов лучший (Nv = 16, рабочее
   окно, seed 96) даёт **r_EF = 0.993, z ≈ 2.4, невязку 11.5% против 2.7%**
   у эталона нулей — тот же паттерн консервативной (конечноразмерной)
   ветви лестницы сходимости, что и C4 (лучший затвор Nv=16, r_EF = 0.9978,
   z = 2.62). Вердикт переписан в чтение консервативной ветви; среднее
   семейства (0.76 ± 0.24 в нулевых облаках) сохранено в формулировке.
3. **C13 README ссылался на несуществующий раннер**
   `run_c13_blind_families.py` (реальный — `run_c13_blind.py`).
4. **`make_figures_v2.py` (fig25_map) писал «16 gates»** при 20 затворах
   C13 — и «H2 gap is UNIVERSAL», «H2 = wall of LOCALITY». Фигура
   перерисована (ru/en, 600 dpi, копии в кампанию), VLM-проверка чистая.
5. **`make_comp_readmes.py` отстал от собственных выходов** на ~12
   вердикт-строк: «H2 is a negative verdict», «нулевая — D_nn на уровне
   суррогата», «разрыв Г2 ≈ 1 порядок» (при закоммиченных 0.5),
   «the H2 gap is stable» и др. Прямые правки README сессий 1–3 не были
   внесены в генератор — перегенерация вернула бы README к «H2 — NO».
   Синхронизировано.
6. **`run_c13_blind.py` писал старый вердикт** («все в нулевой зоне…
   Разрыв Г2 устойчив») при обновлённом вручную JSON сессии 1 —
   рассинхрон источник/артефакт. Шаблон синхронизирован с закоммиченным
   вердиктом (C9/C15 раннеры — та же схема).

## 3. Канонические формулировки волны

| Было | Стало |
|---|---|
| «The H2 gap is UNIVERSAL» (C15) | «The rank-metric resolution limit is UNIVERSAL: … the twisted weight and the ladder carry over to the whole class, and the rank projection stays at its limit» |
| «H2 is a wall of LOCALITY, not of the trace» (C9) | «The open bit-level branch is a wall of LOCALITY, not of the trace» (примитив существует — позитивное содержание) |
| «identity does not» (мост C7) | «the zeros' level — yes (H2), the bit-level branch open» |
| «Every other verdict … is a negative» (C11) | «…resolution-limited branch …: rank channel at its limit (gates at the zeros' level — H2 — YES via D_nn), codings invisible (M3), trace branch conservative (H5 — YES via the convergence ladder)» |
| «never through spectral identity» (C16) | «not through the rank channel (…the rank branch at its resolution limit, with the level identity at the zeros' band)» |
| «negative verdicts (V1, V3, V6, V16)» (Th1) | «level identity — YES … (V6/V16, D_nn bridge, v2.0.7); bit-level branch open (V16); blind-coding / σ-scan design claims refuted (V1, V3)» |
| «гребёнка невидима» (V07) | «следовая ветвь консервативна: лучший затвор (Nv = 16) r_EF = 0.993 при 11.5% против 2.7% — конечноразмерная ветвь лестницы сходимости» |

## 4. Объём изменений

- **Hilbert_Polya:** вердикты C9/C15 (JSON + раннеры + hpbridge),
  README кампаний C4/C6(en)/C7/C9/C11/C13/C15/C16, README.ru.md (4
  места), README.md (2), монографический контент (en/ru_part2, canon,
  ru/en_part4 — заголовки и вопрос C15, вердикт C9, мост C7, субтитул C5),
  preprint.tex (5 мест + абстракт), explorer (streamlit + README),
  data/README, docs/v2 (ru/en), аудит-контент (audit_content.py ×4,
  audit_content2.py ×2, audit_content3.py, content.json ×6), генераторы
  (make_comp_readmes.py, make_figures_v2.py).
- **Перегенерированы:** fig25_map (ru/en + копии), монографии C5/C7/
  canon/v2 × ru/en (8), preprint.pdf (tectonic), аудит-отчёт (PDF+DOCX).
- **AB_Cloud_Quantum_Research:** Th1 (json ru/en, README, генератор,
  монография ru/en), core_spectrum RESULTS.md (ряды 8, 28), ROADMAP.md,
  results/README.md, V07 (раннер + вердикт JSON + README ru/en + монография
  ru/en), en/ru_part4. Перегенерированы V7/theorems/appendix/Th1 × ru/en
  (8 документов).

## 5. Чего сознательно не меняли

- **Числовые данные** всех кампаний (единственное числовое изменение —
  `gap_orders` V07: пересчитан из тех же закоммиченных невязок).
- **Исторические журналы:** CHANGELOG всех уровней, docs/audit_v2.0.5–
  v2.0.8.md, docs/metric_correction_v2.0.1.md, «Note added» предпринта
  (датированная запись).
- **Легитимные отрицательные подрезультаты:** C17 фаза A (предзарегистри-
  рованный критерий, честный отказ), V3 (σ = ½ не оптимально в D_KS),
  V1 (слепой контроль), битовая ветвь V16 (z = 2.49 < 6), C14/C16
  (аттрактор/запутанность — там отрицание корректно).
- Формулировки «нулевая зона/облака» как **измеренный факт** ранговой
  ветви (с уточнением «ранговой ветви», где контекст вердиктный).

## 6. Верификация

- pytest: Hilbert_Polya **22/22**, core_spectrum **42/42**.
- fig25_map: VLM — строки C9/C13/C15 верны («rank limit = wall of
  LOCALITY», «20 gates», «rank-metric limit is UNIVERSAL»), без обрезки
  и наложений.
- Перегенерация всех производных артефактов прошла без ошибок
  (render_pdf/render_docx/postprocess, tectonic, audit_build,
  audit_docx.js).
- Финальный grep-свип репозитория: живых «H2 gap»/«identity does not»/
  «отрицательный вердикт (Г2)» не осталось (исторические журналы —
  сохранены намеренно).
