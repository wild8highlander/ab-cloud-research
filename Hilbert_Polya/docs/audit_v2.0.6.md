# docs/audit_v2.0.6.md — аудит языковой гигиены инфографик и добивки табелей

**Дата: 15.10.2026 · охват: Hilbert_Polya + AB_Cloud_Quantum_Research/modules/core_spectrum · патч v2.0.6 (репозиторий) = 2.0.6 (HP) + 1.2.3 (core_spectrum)**

Повод: после v2.0.5 пользователь указал, что в английском README под
английской таблицей вердиктов стояла русская картинка табеля, и попросил
перегенерировать английскую версию с правильными данными и поискать ещё
ошибочные картинки с табелями по всему репозиторию.

## Диагностика

### HP: английский README вставлял русский табель

README.md:184 содержал `![the scorecard](figures/ru/light/
info_scorecard_ru.png)` — русский PNG под английской таблицей H1–H5.
Английский двойник с правильными данными v2.0.5 существовал
(figures/en/light/info_scorecard_en.png, проверен VLM-вычиткой: H2 NO,
H3 YES, ⟨r⟩ = 0.57–0.63, футер v2.0.5), но не был подключён. README.ru.md
(Extended English Research Edition) картинки не вставляет.

### HP: языковая гигиена инфографик

- `info_handles_en.png` (light+dark) нёс **русский футер** — строка
  «data/c5_gates_ext_verdict.json (v2.0.5) · ⟨r⟩ = 0.57–0.63 по всей
  семье (полоса GUE 0.5996±0.03, среднее 0.60) · |r_H7| max = 0.097
  (Бонферрони 0.57)» была захардкожена в html_handles для обоих языков.
- `info_map`: одна и та же легенда «T = theorem · K = criterion · Г/Н =
  Hilbert–Pólya scorecard item · C = campaign» для обоих языков —
  английские слова в русской картинке и кириллический гомоглиф «Н»
  (вместо латинской H) в английской.

### core_spectrum: табель застрял в эпохе 15 решений

Пакет давно на 19 кампаний (V16–V19, живой data/v14_verdict.json: 19
claims, IVP11 «claims 19, missing []», монографии и workbook уже говорят
19/19), но:

- `info_scorecard_*.png` (все 4): заголовок «Табель 15 решений /
  Scorecard of 15 solutions», карточка V14 «15/15 claims», карточка V6
  «остаток 6e-10» (данные: 5.8e-10 = v06_verdict.json →
  Hxi_control.max_abs_log_resid 5.82e-10), карточек V16–V19 нет.
- **Два дефекта вёрстки**: (а) заголовок накладывался на первый ряд
  карточек — строки начинались с y=7.0 при ylim=9 и заголовке на y=8.55
  (пиксельная проверка: верх карточек 9.08 > 9 — обрезка); (б) текст
  карточки V14 «15/15 claims per schema; full verdict coverage; status
  hygiene observed.» выходил за границу карточки и налезал на V15
  (сканограмма: тёмные пиксели текста до x=14.0 при границе карточки
  13.44).
- `info_map_*.png` (все 4): «Карта пяти направлений / Map of five
  directions» с карточками A–E — при семи направлениях A–G в README.
- `fig16_*.png` (обе): «Карта программы · proven: 6 / measured: 9» — 15
  столбцов вместо 19 (6/13).
- Тексты: README ×2 «15 solutions / 15 кампаний / 15 проверок IVP (факт
  16) / 15-solution program», V14 README ×2 «15/15 claims»,
  docs/validation.md «15/15», docs/plan15.md, docs/theory.md «пяти
  направлений», figures/README.md «16 сюжетов» (факт 20),
  results/RESULTS.md.
- data/v14_verdict.json: meta.package «1.1.0» при 19 claims (V19
  появился только в 1.2.0).

Ложные срабатывания отвергнуты: «15/15 sources resolved» в латексе
MONOGRAPH_ARCHIVE — о флагманских числах, не о claim-аудите; CHANGELOG
1.1.0 «прогон 15/15 PASS» — историческая запись; архив
computations/V14_claim_audit/data (15 claims, 1.0.0) — замороженный
снапшот по конвенции архивов; «87 gate-equivalent configurations» в
science-brief EN — формулировка заменена на выровненную с RU «полный
факторный план ручек (288 спектров V16)».

## Исправления

- HP README.md:184 → figures/en/light/info_scorecard_en.png.
- HP scripts/make_infographics.py: map_foot/handles_foot локализованы;
  20 PNG перегенерированы (изменились ровно 6: map ×4, handles EN ×2 —
  рендер детерминирован, остальные 14 побайтово идентичны).
- core_spectrum scripts/make_infographics.py: табель 19 решений (карточки
  V16–V19 + итоговая «АУДИТ 19/19»), геометрия 4 ряда (figsize 17×10.1,
  заголовок без наложений, тексты в границах карточек); карта семи
  направлений (4+3, F/G добавлены); 12 PNG перегенерированы (trace
  побайтово идентична).
- core_spectrum figstyle.py + make_figures.py fig16: 19 столбцов
  (6 proven / 13 measured); fig16 ×2 перегенерированы, остальные 18 фигур
  данных побайтово идентичны.
- Тексты: HP README.md; core_spectrum README ×2, V14 README ×2 +
  make_comp_readmes.py, docs/{validation,plan15,theory,README}.md,
  figures/README.md, results/RESULTS.md.
- data/v14_verdict.json: meta.package → 1.2.0.

## Верификация

- pytest: HP 22/22, core_spectrum 42/42.
- IVP core_spectrum: 16/16 PASS (IVP11 claims 19; IVP12 19/19).
- VLM-вычитка: EN/RU табели (заголовок, 4×5 карточек, V6 5.8e-10,
  V14 19/19, итог АУДИТ 19/19, отсутствие наложений/обрезок), карта
  A–G ×2 языка, fig16 (19 столбцов, 6/13), EN футеры HP (без кириллицы).
- Монографии V14 (PDF, pdftotext): 19/19; workbook: 19/19.
- Патч: инкремент поверх da22057, применяется на чистом клоне
  побайтово (write-tree совпадение).
