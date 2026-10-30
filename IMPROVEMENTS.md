# IMPROVEMENTS — редизайн веб‑проектов AB‑Cloud Research

**Версия:** 1.4.0 · **Дата:** 2026-10-30 · **Основа:** скилл `landing-page-design` (Part A — стратегия и структура, Part B — визуальная система)

Этот архив содержит **только изменённые и новые файлы** в структуре репозитория.

## Как применить (3 команды)

```bash
# 1. распакуйте содержимое архива в корень репозитория (с заменой файлов)
unzip ab-cloud-web-improvements.zip -d /путь/к/ab-cloud-research

# 2. проверьте и закоммитьте
cd /путь/к/ab-cloud-research
git add -A && git status   # старые dist-ассеты с хэшами удалятся сами — это норма

# 3. запушьте
git commit -m "web UI redesign: landing, dashboard, lab3d, docs — design system 1.4.0" && git push
```

Пуш в `main` автоматически запускает штатные процессы: Pxxl Static App пересобирает портал (`npm run build` → `dist/`), CI собирает docs. Ничего дополнительно настраивать не нужно. Файл `IMPROVEMENTS.md` после прочтения можно удалить — его содержание продублировано в `CHANGELOG.md` (запись 1.4.0).

---

## 1. Принятые допущения (intake скилла, A1)

Если ответа не было — допущение зафиксировано одной строкой и работа продолжена:

- **Одно главное действие (конверсия):** «Open the dashboard» — дашборд есть главный интерактивный артефакт проекта.
- **ICP:** исследователи, рецензенты, матфизики, студенты; возражение №1 — «почему я должен этому верить» → ответ структуры: всё пересчитывается в браузере из замороженных данных.
- **Трафик:** GitHub README, DOI, доклады → зеркалим тон баннеров репозитория (тёмный фон, циан).
- **Доказательства:** реальные числа из README и `results/` (⟨r⟩ = 0.5848 ± 0.0260; KS 0.047, p = 0.27; Byers–Yang 3.5e−15; Lean 4 8/8; 2,001,058 нулей; R² = 0.9997). Ничего не выдумано.
- **Снижение риска:** «No account, no install, no build step» + офлайн‑бандлы = risk reversal (A4).
- **Мобильный приоритет:** да — меню на всю высоту, таблицы со скроллом, брейкпоинты 640/768px.

## 2. Структура лендинга (A2) и выбор лейаута (A3)

**Лейаут A — «Classic hero plus sections»**: проект понятен с одного экрана (живая гистограмма и есть hero‑visual), а задача страницы — маршрут к инструментам (дашборд = verify, 3D‑лаборатория = explore).

1. Hero: заголовок с градиентом #FFFFFF→#9B9B9B, подзаголовок, primary CTA + ghost CTA, строка proof‑сигналов
2. Живой evidence‑панель: гистограмма отношений расстояний ζ‑нулей vs закон GUE — считается в браузере из **того же** замороженного датасета, что поставляет дашборд (`/dashboard/data/…`), с офлайн‑фолбэком на первые 300 нулей
3. Tagline reveal (B11, обязательный): пословная активация цвета по триггер‑линии
4. Problem → solution («A claim is only as good as its cheapest reproduction»)
5. Benefits: 4 карточки (verify / ten languages / re‑derived / frozen)
6. How it works: 3 шага (freeze → run suite → open the browser)
7. Numbers: 6 карточек метрик с трассировкой к артефактам
8. Apps: 2 карточки приложений
9. FAQ: 8 вопросов (`<details>`) + **FAQPage JSON‑LD** (AEO)
10. Final CTA + футер (GitHub, DOI, ζ API, Docs, License, BibTeX‑копирование, статус API)

**SEO/AEO (A7):** индексировать (evergreen‑контент). Title + description обновлены, OG‑теги сохранены (`og-cover.png`, контракт с `build-site.mjs` не нарушен), FAQ‑схема добавлена, `robots.txt` и генерация sitemap без изменений.

## 3. Визуальная система (Part B) — как применена

| Правило скилла | Реализация |
|---|---|
| Шрифты: Geist / Manrope / Geist Mono, не более 1 гарнитуры + моно для данных | **Manrope Variable** + **Geist Mono Variable**, самохостинг: `site/fonts/` для лендинга, `@fontsource-variable` для приложений; OFL‑лицензии в `site/fonts/` |
| Запрет Inter/Roboto/Arial/Open Sans/Helvetica, italics, weight 900 | Segoe UI удалён везде; italics нет; максимум weight 600–700 |
| Type scale — только шаги Tailwind | 12/16, 14/20, 16/24, 18/28, 20/28, 24/32, 30/36, 36/40, 48–60/1 (hero) — ни одного произвольного размера |
| Spacing‑токены 0…96 | Все отступы/гэпы из таблицы (24/32/48/64/96…); кнопки: 8px вертикально × 12px горизонтально |
| Радиусы Tailwind + формула вложенности | Карточки 16, панели‑чипы 12 (16−4), скруглённые «таблетки» full; вложенности с результатом ≤2 не созданы |
| Тёмные фоны только из списка | #000000 (фон страницы) · #181818 (карточки/панели) · #1F1F1F (приподнятые блоки, hover карточек) · #272727 (hover строк и ссылок‑чипов) · #313131 — цвет границ, а не фон; заливок вне списка нет |
| Без градиентов на фоне; единственный градиент — текст hero | Свечение/сетка/ζ‑водяной знак (были градиентами) удалены; градиент только на H1 и цифре 404 |
| B5: hero 680px, осмысленные переносы | `<br>` после «as physics,» / «in front of you» — там, где ломается мысль |
| Иконки Phosphor/Solar/Iconamoon | Точные SVG‑path из `@phosphor-icons/core` (проверено скриптом на побайтовое совпадение) |
| B7 motion: базовая кривая, только transform/opacity | `cubic-bezier(0.22,1,0.36,1)` 500мс; hover‑цвета 300мс; reveal 32px/700мс через IntersectionObserver, один раз; активация `scale(0.98)`; `prefers-reduced-motion` — только opacity |
| B7 навигация | Плавающая «таблетка» с blur по центру; мобильное меню — панель на всю высоту, ссылки въезжают по 60мс (суммарно ≤400мс); иконка меню превращается в крестик трансформом |
| B11 tagline reveal | Секция после hero‑visual, 2 строки, слова из 30% непрозрачности активируются по одному при пересечении триггер‑линии |
| B9 состояния | Hover/active/focus‑ring везде; **skeleton‑лоадеры** в форме реального лейаута (статы, строки таблицы, график); **пустое состояние** фильтра вердиктов; ошибки — inline‑карточки, без `window.alert`; текущий раздел в навигации подсвечен (scrollspy + aria-current) |
| B10 ship | Skip‑link, семантика (`nav/main/section/footer`, `role=alert/status`), `<title>`+description+OG+theme‑color, favicon, alt/aria‑label, брендированный 404 и offline (CSP‑безопасные: без inline‑скриптов), links в футере на License, авто‑retry оффлайн‑страницы |
| B8 реализм | Весь копирайт — реальные числа и названия; запрещённые слова‑паразиты отсутствуют; sentence case; `text-wrap: balance/pretty` |

**Копирайт‑гигиена (B1):** дефисы в тексте устранены переписыванием фраз («live» вместо real‑time, «in the browser» вместо in‑browser). Исключение сохранено осознанно: **SHA‑256** — нормативное написание стандарта, а также дефисы внутри кода/URL/BibTeX (код, а не копирайт).

## 4. Изменённые и новые файлы

```
site/                        — лендинг портала (полная замена каталога)
  index.html                 — новая структура по A2 + FAQ JSON‑LD
  portal.js                  — навигация, scrollspy, B11‑reveal, гистограмма, FAQ, BibTeX
  particles.js               — поле «нулей»: reduced‑motion, пауза в фоне, DPR cap
  404.html, offline.html     — в новой системе (offline без inline‑обработчиков + авто‑retry)
  manifest.json              — theme/background #000000
  sw.js                      — precache v3: + шрифты
  fonts/                     — Manrope/Geist Mono woff2 + OFL‑лицензии (НОВОЕ)
apps/ab-cloud-dashboard/     — тёмная тема, Manrope+Geist Mono, скелетоны, empty state,
                               floating‑таб‑бар, OG‑мета; package.json 1.2.0; dist/ пересобран
apps/ab-cloud-lab3d/         — та же система; фон WebGL‑сцены #000000; dist/ пересобран
docs/monographs.md           — НОВЫЙ (нав ссылался на несуществующий файл)
docs/monograph-v21.md        — НОВЫЙ
docs/audit_v2.0.3.md         — НОВЫЙ
docs/audit_v2.0.4.md         — НОВЫЙ
mkdocs.yml                   — slate+black+cyan по умолчанию, Manrope/Geist Mono
CHANGELOG.md                 — запись 1.4.0
package-lock.json            — корневой: + @fontsource-variable/*, @phosphor-icons/react
```

## 5. Что НЕ тронуто

Вся численная логика: `stats.worker.js`, `zeta.js`, `scenes.js` (кроме цвета фона), формулы, данные, API‑функции `api/`, контракты `build-site.mjs`/`serve.mjs`/`pxxl.toml` (файлы `og-cover.png`, `robots.txt`, `register-sw.js`, иконки, screenshots сохранены). Каждый номер на странице по‑прежнему трассируется к замороженным артефактам.

## 6. Проверки, выполненные перед упаковкой

- `npm install` + `npm run build -w …` для обоих приложений и `npm run build` портала — без ошибок;
- `node --check` для всех JS лендинга;
- `mkdocs build --strict` (пин mkdocs 1.6.1 + material 9.7.7, как в CI) — **зелёный** (раньше падал на 4 битых nav‑ссылках);
- headless‑браузер: hero, evidence‑панель (живой датасет fetched, ⟨r⟩ = 0.6160 на первых 5 000 нулей), tagline, benefits, numbers, FAQ, финальный CTA, футер (API ONLINE), дашборд (3 таба, Web Worker считает), 3D‑лаборатория (сцена Хофштадтера), мобильное меню, 404 — скриншоты проверены, ошибок в консоли нет.
