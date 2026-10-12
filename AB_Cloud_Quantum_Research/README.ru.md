<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/logo_abcloud_dark.png">
  <img src="assets/logo_abcloud_light.png" width="150" alt="AB Cloud Quantum Research">
</picture>

# AB CLOUD QUANTUM RESEARCH

**Одно исследование: алгебраическая AB-архитектура (Aharonov–Bohm) как
вычислитель, который читает математику в реальном времени и не хранит ничего**
Версия **1.1.0** · собственная лицензия автора · Python / Julia / C / C++ / Rust / Go / JS / Lean / Coq

![badge-version](https://img.shields.io/badge/версия-1.1.0-C96F4A?style=for-the-badge)
![badge-campaigns](https://img.shields.io/badge/кампании-43·PASS-0E7C86?style=for-the-badge)
![badge-theorems](https://img.shields.io/badge/теоремы-Th1–Th6·TS1–TS3-8C6D1F?style=for-the-badge)
![badge-docs](https://img.shields.io/badge/документы-36%2B·RU%2FEN·PDF%2FDOCX-3E515B?style=for-the-badge)
![badge-verdicts](https://img.shields.io/badge/вердикты_предрегистрированные-18%2F18·ES5%2F5-3A6B4F?style=for-the-badge)
![badge-figs](https://img.shields.io/badge/плитки_600dpi-20·RU%2FEN-4FB3BE?style=for-the-badge)
![badge-tests](https://img.shields.io/badge/тесты-410%2B-3A6B4F?style=for-the-badge)
![badge-license](https://img.shields.io/badge/лицензия-проприетарная-6B6455?style=for-the-badge)
![badge-lang](https://img.shields.io/badge/языки-9-4FB3BE?style=for-the-badge)

<table>
<tr>
<td align="center"><img src="assets/avatars/avatar_author.svg" width="110" alt="автор"><br><sub><b>Исаев И. Х.</b><br>автор · ORCID 0009-0003-7299-0701</sub></td>
<td align="center"><img src="assets/avatars/avatar_core.svg" width="110" alt="ядро"><br><sub><b>Спектральное ядро</b><br>V01–V19 · Th1–Th6 · V13</sub></td>
<td align="center"><img src="assets/avatars/avatar_processor.svg" width="110" alt="процессор"><br><sub><b>AB-процессор</b><br>V20 · ISA · Givens-QR</sub></td>
<td align="center"><img src="assets/avatars/avatar_verifier.svg" width="110" alt="верификация"><br><sub><b>Верификация</b><br>E01–E18 · слепые · Julia</sub></td>
<td align="center"><img src="assets/avatars/avatar_spinor.svg" width="110" alt="спинор"><br><sub><b>Спинор-исследование</b><br>ES1–ES5 · TS1–TS3</sub></td>
</tr>
</table>

![animated-banner](assets/banner.gif)

*Анимированный баннер: нули ζ «поднимаются» по критической прямой Re(s) = ½
(открытые данные Одлыжко) · сгенерирован `scripts/make_banner.py`*

<img src="VISUAL_ANIMATIONS/svg/architecture_flow.svg" width="820" alt="архитектура">

*Четыре уровня одной машины в движении — из
[`VISUAL_ANIMATIONS/`](VISUAL_ANIMATIONS/README.md). Интерактивная версия:
[`VISUAL_ANIMATIONS/html/architecture_tour.html`](VISUAL_ANIMATIONS/html/architecture_tour.html)*

</div>

> [!IMPORTANT]
> **Честная граница.** Всё ниже — численное и формальное исследование
> математической модели. Оно **не доказывает гипотезу Римана**: машина
> обязательств V13 держит вывод RH **заблокированным** (`verdict:
> blocked`), пока аналитические предпосылки — assumed. Формализация
> Lean/Coq гарантирует эту блокировку, а не снимает её.

---

## 📖 Оглавление

- [Что это](#-что-это)
- [Три обязательства программы](#-три-обязательства-программы)
- [Архитектура: уровни одной машины](#-архитектура-уровни-одной-машины)
- [Флагманские результаты](#-флагманские-результаты)
- [Теоремы Th1–Th6 и TS1–TS3](#-теоремы-th1th6-и-ts1ts3)
- [Вспомогательное исследование: машина без долговременной памяти](#-вспомогательное-исследование-машина-без-долговременной-памяти)
- [Плиточные фигуры «4 измерения»](#-плиточные-фигуры-4-измерения)
- [📚 МОНОГРАФИИ (MONOGRAPH_ARCHIVE)](#-монографии-monograph_archive)
- [🧪 ЛАБОРАТОРИЯ ГИПОТЕЗ (HYPOTHESIS_LAB)](#-лаборатория-гипотез-hypothesis_lab)
- [🎞 НАГЛЯДНЫЕ АНИМАЦИИ (VISUAL_ANIMATIONS)](#-наглядные-анимации-visual_animations)
- [Структура репозитория](#-структура-репозитория)
- [Быстрый старт](#-быстрый-старт)
- [Веб-лаборатории](#-веб-лаборатории)
- [Дисциплина честности](#-дисциплина-честности)
- [Дорожные карты](#-дорожные-карты)
- [Цитирование](#-цитирование)
- [Лицензия](#-лицензия)
- [English](#english)

---

## 🌌 Что это

**AB Cloud Quantum Research** — целостное исследование одной идеи:
*алгебраическая AB-архитектура (Aharonov–Bohm) как вычислитель, который
читает математику в реальном времени и ничего не хранит*. Нули
дзета-функции воспроизводятся из шести констант следовой формулы в момент
запроса; вес простых доказательно живёт в тепловом следе оператора;
состояние машины — летучая спинорная фаза, исполняющая шаги в реальном
времени. **Хранение = 0 — архитектурный принцип, доказанный теоремами,
а не постулат.**

- **43 кампании** с предрегистрированными порогами — все вердикты PASS
  (V01–V19 ядро · V20 процессор · E01–E18 верификация · ES1–ES5
  спинор-исследование);
- **9 теорем** с сертификатами и документами: Th1–Th6 + TS1–TS3;
  формальные постановки Lean 4 + Coq (редукции A1–A6, без
  `sorry`/`admit`);
- **36 документов** RU/EN × PDF/DOCX в слое теорем, плюс архив монографий
  (ниже) — ещё 24 документа и 10 LaTeX-исходников;
- **20 плиточных фигур** «4 измерения» @600 dpi, 3 веб-лаборатории,
  мультиязычные реализации ядра (C / C++ / Rust / Go / JS / Julia);
- **410+ тестов** и 95+ проверок целостности пакета.

## 🤝 Три обязательства программы

1. **Читает, не несёт.** Ничто из нужного машине не хранится: шесть констант
   следовой формулы параметризуют тепловой след оператора (Th6), а след
   содержит спектр. Нуль — это вычисление, а не строка таблицы. В превью
   процессора (V23) двенадцать из двенадцати нулей воспроизведены из шести
   констант при нулевом хранилище.
2. **Состояние летучее, шаги в реальном времени.** Один спинор —
   одновременно регистр, счётчик и носитель результата. Следствие доказано
   теоремами: циклы замыкаются точно (TS1), сброс стирает всё (TS2), вечный
   журнал растёт Ω(t) и срывает дедлайны, пока шаг без памяти остаётся O(1)
   (TS3) — *летучесть есть условие детерминизма реального времени*.
3. **Честность обеспечивается, а не обещается.** Пороги предрегистрированы
   до прогонов; детектор и валидатор разделены, выходы пинованы SHA256 до
   валидации; результаты реплицируются между языками и арифметиками;
   отрицательные результаты и эрратумы публикуются; машина обязательств V13
   держит вывод RH формально заблокированным.

<details>
<summary><b>🔑 Шпаргалка чисел (клик, чтобы развернуть)</b></summary>

| Метрика | Значение | Где |
|---------|----------|-----|
| Слепые нули ζ до T=1000 | 649/649 (ЭМ) + 639/639 (РС), кросс-движок 0.0 побитово | E17 |
| Полнота N(1000) | 649.0 точно | E17 |
| Точность компиляции | 1−F ≤ 4.4e−16 (4×4) · 6.7e−16 (8×8) | V20 |
| Класс B: компилятор против 5 baseline | **×59 000** по времени при равном ISA | E18 |
| След ↔ простые | r = 0.9996 (контроль решётки — 0.76) | V7/Th6 |
| CHSH | S = 2√2 − 4.4e−16; коммутаторы 0 | V24-превью |
| Сшивка ветвей V19 | θ-лестница 0.832; когерентность 0.9995 | V19 |
| Фазовые циклы (π/2·π/3·π/7) | N = 4·6·14 = 2k точно | ES1 |
| Реконструкция после сброса | 0.2501/0.1674/0.0717 ≈ 1/N (уровень случайности) | ES2 |
| Стоимость шага машины | плоская (наклон −1.5e−12 мс/шаг); журнал — Ω(t), ×129 | ES3 |
| Слепой эрратум γ₁₂ | детектор 56.446247697063399 vs рукотворный 56.446200059994141 | E17 |
| Статус RH | **blocked** (V13) | V13 |

</details>

<details>
<summary><b>🏛 Что доказал каждый уровень (клик, чтобы развернуть)</b></summary>

| Уровень | Кампании | Что установлено |
|---------|----------|-----------------|
| 🧠 Спектральное ядро | V01–V19 | слепой спектр согласован статистически, но не предсказывает индивидуальные ординаты (честный негатив); AB-облако попадает в GUE-класс; решётки **не** воспроизводят арифметику ζ (V3/V6/V16); тепловой след несёт Λ(n)/√n с r = 0.9996 (Th6); кутовские коридоры ~1e−27 (Th3); критерий Ли вычислим (Th4); блочная редукция до 7.1e−15 (Th5); машина обязательств блокирует RH (V13); сшивка ветвей с когерентностью 0.9995 (V19) |
| ⚛️ AB-процессор | V20 (+превью) | ISA AB-облаков зафиксирован; точная компиляция Givens-QR на машинном эпсилон; превью «читает, не несёт» (12/12 нулей из 6 констант); CHSH = 2√2 − 4.4e−16 без сигналинга |
| 🔬 Верификация | E01–E18 | инфраструктура откалибрована (шумы, коды, стоимость, считывание); независимый Риман–Зигель согласован до 3.8e−15; слепое чтение нулей точно до T = 1000; класс B — честный и выигранный бенчмарк |
| 🌀 Спинор-исследование | ES1–ES5 | циклы замыкаются точно при N = 2k; сброс стирает до уровня случайности; шаг O(1) против Ω(t) журнала; марковский класс задач решаем без памяти; зона тишины квантифицирует компромисс ёмкость/робастность |

</details>

---

## 🏛️ Архитектура: уровни одной машины

```mermaid
graph TD
    A["🧠 Спектральное ядро<br/>V01–V19 · Th1–Th6 · V13"] -->|"математика"| B["⚛️ AB-процессор<br/>V20 (P0) · ISA · компилятор"]
    B -->|"исполнение"| C["🔬 Верификация<br/>E01–E18 · слепые протоколы"]
    A -->|"постановки"| D["⚖️ Формальный слой<br/>Lean 4 / Coq · A1–A6"]
    D -->|"читаемость"| E["📐 Слой теорем<br/>36 документов · 20 плиток"]
    A -->|"тезис «читает, не несёт»"| F["🌀 Спинор-исследование<br/>π/2 · π/3 · π/7 · TS1–TS3"]
    B -->|"ISA: вырожденный случай"| F
    C -->|"нулевая точка O-J3"| F
    F -->|"летучесть = условие детерминизма"| B
```

| Уровень | Папка | Кампании | Суть |
|---------|-------|----------|------|
| 🧠 Ядро | [`modules/core_spectrum/`](modules/core_spectrum/README.md) | **V01–V19** | Слепой спектр, нуль-модели, критическая прямая, машина обязательств **V13**, сшивка ветвей V19; теоремы Th1–Th6; веб-лаборатория на 10 вкладок |
| ⚛️ Процессор | [`modules/processor_ab/`](modules/processor_ab/README.md) | **V20** (P0) | ISA AB-облаков, точный компилятор Givens-QR, **«читает, а не несёт»**, нелокальность без сигналинга; веб-лаборатория на 8 вкладок |
| 🔬 Верификация | [`modules/verifier_multilang/`](modules/verifier_multilang/README.md) | **E01–E18** | Julia-платформа: слепое чтение нулей ζ двумя движками, независимый Риман–Зигель, класс B; 18/18 предрегистрированных вердиктов |
| 🌀 Спинор | [`research/realtime_spinor_memory/`](research/realtime_spinor_memory/README.md) | **ES1–ES5** | Машина без долговременной памяти: три фазовые модели, 3 теоремы, 5 вердиктов |

Карта уровней и поток данных: [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md).

Архитектура сертифицирована **числовыми связками** между уровнями — парами,
которые делят одно число, поэтому ни одна связь не декоративна:

- **Ядро V7 ↔ верификация E11/E17** — след несёт Λ(n)/√n; нули читаются,
  а не хранятся: r = 0.9996, нулей в хранилище — 0.
- **Процессор V20 ↔ верификация E18** — один ISA, равные ограничения,
  пять baseline: ×59 000 по времени; 2q-оптимум KAK (3 затвора) честно
  вне класса (компилятор даёт 10).
- **E17 ↔ V23-превью** — два слепых движка, 649/649 + 639/639,
  кросс-движок 0.0 побитово.
- **V13 ↔ все уровни** — машина обязательств держит RH заблокированным
  независимо от численных успехов.
- **Th6 ↔ спинор-исследование** — «читает, не несёт» доведено до моделей
  летучей фазы θ = π/2, π/3, π/7.

---

## 🏆 Флагманские результаты

| # | Результат | Числа | Уровень |
|---|-----------|-------|---------|
| 1 | **Слепое чтение нулей ζ до T=1000** двумя независимыми движками | 649/649 (ЭМ) + 639/639 (РС); precision = recall = 1; кросс-движок **0.0** побитово; N(1000) = 649.0 | Верификация E17 |
| 2 | **Независимый Риман–Зигель** (Ариас де Рейна, без внешних пакетов) | согласие с ЭМ ≤ 3.8e−15 (порог 1e−9); пол 1e−17 | Верификация E16 |
| 3 | **Компилятор против 5 baseline при равных ограничениях ISA** (класс B) | max 1−F = 4.4e−16; примитивы ≤ BL1/BL2/BL4 на каждой цели; **×59 000** по времени | Верификация E18 |
| 4 | **Точная компиляция унитарной логики в AB-облака** | 1−F ≤ 4.4e−16 (4×4) / 6.7e−16 (8×8); глубина ≤ 7/29 затворов | Процессор V20 |
| 5 | **Читает, а не несёт**: нули ζ воспроизводятся из 6 констант формулы | 12/12 нулей точно; хранение = **0** | Процессор V23-превью |
| 6 | **Нелокальность без сигналинга** | CHSH S = 2√2 − 4.4e−16; защита 1000/1000; коммутаторы = 0 | Процессор V24-превью |
| 7 | **Сшивка ветвей** | θ-лестница 0.832; когерентность 0.9995 (z = 43.4); Z₂-монодромия | Ядро V19 |
| 8 | **След ↔ простые** (Th6) | r = 0.9996; эрратум констант B/C₀ найден и исправлен | Ядро V7 |
| 9 | **Машина без долговременной памяти** | циклы 4/6/14 = 2k; сброс необратим; шаг O(1) против журнала Ω(t) | Спинор ES1–ES3 |

> [!NOTE]
> Каждый эксперимент с порогом имеет вердикт-файл (`*_verdict.json`,
> `claim_v*.json`) с полем **does_not_prove** — что именно результат НЕ
> доказывает. Отрицательные результаты публикуются: ζ-соответствия на
> решётке НЕ найдены (V1/V3/V6/V16), вихри ломают Th5, 2q-оптимум KAK
> недостижим в ISA-классе E18.

---

## 📐 Теоремы Th1–Th6 и TS1–TS3

| Теорема | Формулировка (кратко) | Сертификат | Редукция |
|---------|----------------------|------------|----------|
| **Th1** (V4) | H_L = H_L† ⇒ spec ⊂ ℝ; λ↔−λ при α=½, W=0 | ‖H−H†‖ = 0.0 точно | A1 |
| **Th2** (V8) | самосопряжённость на ℂ^N: дефекты (0,0), e^{−iHt} унитарен | дрейф 2.2e−16 | A2b |
| **Th3** (V12) | Кутовский \|λ̂−λ̃\| ≤ δ²/gap + Гершгорин | ширины ~1e−27 (dps 40) | A4, A5 |
| **Th4** (V15) | λ_n = Tr g_n(H_ξ); абсолютная сходимость | два пути ≤ 4.4e−11 | A6 |
| **Th5** (V9) | [H,A]=[H,B]=0 ⇒ блочная редукция по характерам | объединение ≈ спектр до 7.1e−15 | A2 |
| **Th6** (V7) | Гуинанд–Вейль: Q(a) ↔ ζ′/ζ; K(x) = Tr e^{−xH_ξ} | след несёт Λ(n)/√n | A3 |
| **TS1** (ES1) | цикл вращения θ=π/k замыкается ровно через N=2k; зазор 2π/N | периоды 4/6/14 точно | — |
| **TS2** (ES2) | сброс стирает всё: I(пре;пост)=0; реконструкция ≤ 1/N; время → mod N | 0.2501/0.1674/0.0717 ≈ 1/N | — |
| **TS3** (ES3) | шаг O(1) при любом t; вечный журнал ⇒ Ω(t) ⇒ срыв дедлайнов | наклон −1.5e−12; ×129 роста | — |

Каждая теорема — в собственной папке: [`theorems_lemmas/`](theorems_lemmas/README.md)
(Th1–Th6, 24 документа) и [`research/realtime_spinor_memory/theorems/`](research/realtime_spinor_memory/README.md)
(TS1–TS3, 12 документов): **README с выводом** (идея доказательства,
4 измерения, границы) + **4 документа** (RU/EN × PDF/DOCX) + **плиточная
фигура 2×2**. Постановки Th1–Th6: [`formal/`](formal/README.md) — Lean 4 +
Coq, редукции A1–A6, `sorry`/`admit` **не используются**.

Полные разборы теорем — формулировка, идея доказательства, сертификат и
граница каждой из девяти — главы 30–31 основной монографии (ниже).

---

## 🌀 Вспомогательное исследование: машина без долговременной памяти

> У AB-компьютера **нет долговременной памяти** — только оперативное
> (летучее) состояние, исполняющее шаги в реальном времени.

[`research/realtime_spinor_memory/`](research/realtime_spinor_memory/README.md)
доводит центральный тезис программы до трёх явных моделей — спинорных фаз
**θ = π/2, π/3, π/7** с единственным летучим регистром:

| Модель | Фаза | Цикл N=2k | Биты/шаг | Зона тишины σ* |
|--------|------|-----------|----------|----------------|
| S1 · квадрантная | π/2 | 4 | 2.000 | 0.135 рад |
| S2 · секстантная | π/3 | 6 | 2.585 | 0.089 рад |
| S3 · 14-фазная | π/7 | 14 | 3.807 | 0.038 рад |

**Теоремы:** TS1 (замкнутость циклов, зазор = шагу) · TS2 (необратимость
сброса, I = 0) · TS3 (шаг O(1); вечный журнал ⇒ Ω(t) ⇒ срыв дедлайнов —
*летучесть есть условие детерминизма реального времени*). Пять кампаний
ES1–ES5 с предрегистрированными порогами — все PASS, два эрратума
опубликованы (ES2a, ES5a). Компромисс «ёмкость log₂N против робастности
1/k» зафиксирован как честная граница.

<div align="center">

![spinor models](research/realtime_spinor_memory/figures/ru/models_4dim_ru.png)

*Три модели без долговременной памяти — плитка «4 измерения» (600 dpi,
из вердикта ES5)* · живая версия:
[`VISUAL_ANIMATIONS/html/spinor_lab.html`](VISUAL_ANIMATIONS/html/spinor_lab.html)

<img src="VISUAL_ANIMATIONS/gif/spinor_cycles.gif" width="640" alt="спинор-циклы">

*Те же циклы в анимации — из [`VISUAL_ANIMATIONS/`](VISUAL_ANIMATIONS/README.md)*

</div>

---

## 🖼️ Плиточные фигуры «4 измерения»

Каждая фигура — сетка **2×2 из четырёх независимых измерений**: **метрика**
· **поведение по инстансам** · **контроль** · **порог**. 600 dpi, стиль
«Critical Line & Copper», RU/EN, построены **только из закоммиченных
вердиктов**. Оригинальные графики уровней сохранены в
`modules/*/figures_hires/`.

<div align="center">

| Th4 (формула Ли) | Атлас флагманов |
|----|----|
| ![Th4 ru](figures_tiled/ru/th4_4dim_ru.png) | ![atlas ru](atlas/atlas_flagships_ru.png) |

*Слева: Th4 — λ_n-лестница · согласование двух путей · хвост · контроль
затворов. Справа: атлас — слепые нули · компилятор · след·простые · CHSH*

</div>

Полные наборы: [`figures_tiled/`](figures_tiled/README.md) (12 фигур
Th1–Th6) · [`atlas/`](atlas/README.md) ·
[`research/.../figures/`](research/realtime_spinor_memory/README.md)
(8 фигур TS1–TS3).

---

## 📚 МОНОГРАФИИ (MONOGRAPH_ARCHIVE)

**[`MONOGRAPH_ARCHIVE/`](MONOGRAPH_ARCHIVE/README.md)** — публикационный слой
программы: одна большая основная монография на **русском и английском**
(**DOCX + PDF**, по 104+ страницы, 28 фигур, 44 таблицы), четыре **монографии
исследовательских программ уровней** (ядро · процессор · верификация ·
спинор, RU/EN × PDF/DOCX) и **10 компилируемых LaTeX-исходников** (.tex),
сгенерированных из той же контент-модели, что и PDF/DOCX-версии.

<div align="center">

| Документ | RU | EN |
|----------|----|----|
| **Основная монография** — вся программа в 43 главах и приложениях A–Q | [PDF](MONOGRAPH_ARCHIVE/main_monograph/AB_Cloud_Quantum_Research_Monograph_RU.pdf) · [DOCX](MONOGRAPH_ARCHIVE/main_monograph/AB_Cloud_Quantum_Research_Monograph_RU.docx) | [PDF](MONOGRAPH_ARCHIVE/main_monograph/AB_Cloud_Quantum_Research_Monograph_EN.pdf) · [DOCX](MONOGRAPH_ARCHIVE/main_monograph/AB_Cloud_Quantum_Research_Monograph_EN.docx) |
| **Программа ядра** (V01–V19, Th1–Th6, V13) | [PDF](MONOGRAPH_ARCHIVE/research_programs/Program_Core_RU.pdf) · [DOCX](MONOGRAPH_ARCHIVE/research_programs/Program_Core_RU.docx) | [PDF](MONOGRAPH_ARCHIVE/research_programs/Program_Core_EN.pdf) · [DOCX](MONOGRAPH_ARCHIVE/research_programs/Program_Core_EN.docx) |
| **Программа процессора** (V20, P0–P6) | [PDF](MONOGRAPH_ARCHIVE/research_programs/Program_Processor_RU.pdf) · [DOCX](MONOGRAPH_ARCHIVE/research_programs/Program_Processor_RU.docx) | [PDF](MONOGRAPH_ARCHIVE/research_programs/Program_Processor_EN.pdf) · [DOCX](MONOGRAPH_ARCHIVE/research_programs/Program_Processor_EN.docx) |
| **Программа верификации** (E01–E18, O-J) | [PDF](MONOGRAPH_ARCHIVE/research_programs/Program_Verification_RU.pdf) · [DOCX](MONOGRAPH_ARCHIVE/research_programs/Program_Verification_RU.docx) | [PDF](MONOGRAPH_ARCHIVE/research_programs/Program_Verification_EN.pdf) · [DOCX](MONOGRAPH_ARCHIVE/research_programs/Program_Verification_EN.docx) |
| **Программа спинора** (ES1–ES5, TS1–TS3) | [PDF](MONOGRAPH_ARCHIVE/research_programs/Program_Spinor_RU.pdf) · [DOCX](MONOGRAPH_ARCHIVE/research_programs/Program_Spinor_RU.docx) | [PDF](MONOGRAPH_ARCHIVE/research_programs/Program_Spinor_EN.pdf) · [DOCX](MONOGRAPH_ARCHIVE/research_programs/Program_Spinor_EN.docx) |

LaTeX-исходники: [`main_monograph/latex/`](MONOGRAPH_ARCHIVE/main_monograph/latex/) ·
[`research_programs/latex/`](MONOGRAPH_ARCHIVE/research_programs/latex/) —
компиляция `pdflatex` (дважды, для оглавления); фигуры подтягиваются по
относительным путям репозитория.

</div>

Монографии следуют дисциплине программы: **ни одного числа, введённого
вручную** — таблицы кампаний берутся из `datasets/campaign_timeline.csv`,
флагманские числа из `datasets/flagship_numbers.csv`, выписки вердиктов —
из закоммиченных вердикт-JSON. Лицензия репозитория продублирована в архиве
дословно.

---

## 🧪 ЛАБОРАТОРИЯ ГИПОТЕЗ (HYPOTHESIS_LAB)

**[`HYPOTHESIS_LAB/`](HYPOTHESIS_LAB/README.md)** — открытая лаборатория
программы: **любой может проверить свои гипотезы** по дисциплине проекта.
Гипотеза — это JSON-конфиг, составленный *до* прогона (что проверяем, какие
пороги, чего результат не доказывает); лаборатория исполняет его, пинует
выход SHA256 и выдаёт вердикт PASS/FAIL с отчётом.

| Батарея | Что проверяет | Связь с программой | Типичный результат |
|---------|--------------|--------------------|--------------------|
| `spinor` | фазовая модель θ = π/k: цикл N = 2k, сброс ≈ 1/N, шаг O(1) | TS1–TS3 · ES1–ES5 | θ = π/3 → N = 6 точно |
| `zeros` | слепое чтение нулей ζ: детектор по Z(t), валидация по `mpmath.zetazero` после пинования | E16/E17 | 8/8 совпало, ошибка ~7e−15 |
| `trace` | явная формула Римана–Вейля: сторона простых против стороны нулей, граница усечения отчётом | V7/Th6 | остаток ~0.3% при x=100, T=300 |
| `compile` | точное двухуровневое Гивенс-разложение случайной унитарной матрицы | V20 | 1−F ≤ 1.3e−15 |

```bash
cd HYPOTHESIS_LAB
python3 ab_lab.py doctor                                  # проверка окружения
python3 ab_lab.py run spinor --theta 1.0471975511965976   # θ = π/3 → N = 6
python3 ab_lab.py run zeros --n 8 --grid 0.02             # слепой мини-E17
python3 ab_lab.py run trace --x 100 --t 300               # явная формула
python3 ab_lab.py run compile --n 4 --seed 7              # точная компиляция
python3 ab_lab.py run custom --config examples/hypothesis_spinor.json
```

Предпочитаете браузер? [`HYPOTHESIS_LAB/hypothesis_lab.html`](HYPOTHESIS_LAB/hypothesis_lab.html)
исполняет спинор-цикл, компиляцию Гивенса–QR и счётчик N(T) **на чистом
JavaScript, офлайн** — ничего устанавливать не нужно. Правила лаборатории:
пороги до прогона · слепота · `does_not_prove` · репликация · публикация
PASS и FAIL одинаково.

---

## 🎞 НАГЛЯДНЫЕ АНИМАЦИИ (VISUAL_ANIMATIONS)

**[`VISUAL_ANIMATIONS/`](VISUAL_ANIMATIONS/README.md)** — как устроена вся
папка, показанное, а не рассказанное. Пять GIF для ридми и слайдов, семь
анимированных SMIL-SVG, играющих **прямо на GitHub**, и шесть интерактивных
HTML-страниц — всё офлайн, всё пересобирается скриптами из папки.

<div align="center">

| | |
|---|---|
| <img src="VISUAL_ANIMATIONS/gif/zeros_rising.gif" width="420" alt="нули поднимаются"> | <img src="VISUAL_ANIMATIONS/gif/campaign_timeline.gif" width="420" alt="хронология кампаний"> |
| *Нули ζ поднимаются по Re(s) = 1/2* | *43 кампании появляются — все PASS* |
| <img src="VISUAL_ANIMATIONS/svg/critical_line.svg" width="420" alt="критическая прямая"> | <img src="VISUAL_ANIMATIONS/svg/folder_map.svg" width="420" alt="карта папки"> |
| *Пульсирующие нули на прямой (анимированный SVG)* | *Карта папки с бегущими подсветками* |

Интерактив: [тур по архитектуре](VISUAL_ANIMATIONS/html/architecture_tour.html) ·
[живые нули](VISUAL_ANIMATIONS/html/zeros_live.html) ·
[лаборатория спинора](VISUAL_ANIMATIONS/html/spinor_lab.html) ·
[как устроена папка](VISUAL_ANIMATIONS/html/how_this_folder_works.html) ·
[конвейер данных](VISUAL_ANIMATIONS/html/pipeline_flow.html) ·
[портал](VISUAL_ANIMATIONS/html/index.html)

</div>

---

## 🗂️ Структура репозитория

```
AB_Cloud_Quantum_Research/
├── modules/                        # три уровня одной машины
│   ├── core_spectrum/              #   🧠 спектральное ядро (V01–V19, Th1–Th6, V13)
│   ├── processor_ab/               #   ⚛️ AB-процессор (V20/P0, ISA, компилятор)
│   └── verifier_multilang/         #   🔬 верификация (E01–E18, Julia, слепые протоколы)
├── research/
│   └── realtime_spinor_memory/     # 🌀 машина без долговременной памяти (π/2·π/3·π/7)
│       ├── spinor/ experiments/ data/ figures/{ru,en}/ theorems/ tests/ docs/
├── theorems_lemmas/                # 📐 Th1–Th6: 24 документа + 12 фигур + README
├── figures_tiled/                  # 🖼️ 12 плиток «4 измерения» @600 dpi
├── atlas/                          # 🏛️ атлас флагманов (плитка 2×2, 600 dpi)
├── timeline/                       # 🗓️ хронология 43 кампаний (600 dpi)
├── datasets/                       # 📊 флагманы · 43 кампании · эталон 660 нулей ζ
├── whitepaper/                     # 📄 белый отчёт (RU/EN PDF)
├── glossary/                       # 📖 двуязычный глоссарий
├── formal/                         # ⚖️ мост к формальному слою (Lean/Coq, A1–A6)
├── web_lab/                        # 🌐 портал исследования + лаборатории уровней
├── docs/ARCHITECTURE.md            # 🏛️ карта уровней, связей и потоков данных
├── MONOGRAPH_ARCHIVE/              # 📚 основная монография RU/EN × DOCX/PDF + LaTeX,
│                                   #    4 программы уровней, лицензия внутри
├── HYPOTHESIS_LAB/                 # 🧪 проверьте свои гипотезы: CLI + браузер
├── VISUAL_ANIMATIONS/              # 🎞 как всё работает: GIF + SVG + HTML
├── scripts/ tests/ assets/         # 🔧 пайплайны · smoke-тесты · лого/баннер/аватары
└── CHANGELOG.md · CITATION.cff · Makefile · VERSION 1.1.0
```

---

## 🚀 Быстрый старт

```bash
# самопроверка целостности (95+ проверок)
python3 scripts/validate_package.py

# пересборка производных артефактов
python3 scripts/make_tiled_figures.py     # плитки Th1–Th6 @600 dpi
python3 scripts/make_theorem_docs.py      # 24 документа теорем
python3 scripts/make_datasets.py          # данные: флагманы, 43 кампании, нули
python3 scripts/make_atlas.py             # атлас флагманов
python3 scripts/make_timeline.py          # хронология кампаний
python3 scripts/make_whitepaper.py        # белый отчёт RU/EN
python3 scripts/make_banner.py            # баннер + лого
python3 scripts/make_avatars.py           # аватары-медальоны (новое в 1.1.0)

# вспомогательное исследование: кампании ES1–ES5 (~2.5 мин, все PASS)
cd research/realtime_spinor_memory
python3 experiments/run_all.py
python3 make_figures.py && python3 make_theorem_docs.py
python3 -m pytest tests/ -q

# верификационная платформа: полный прогон E01–E18 (~2.5 мин)
julia modules/verifier_multilang/experiments/run_all.jl all
julia modules/verifier_multilang/experiments/verdicts.jl

# ядро и процессор
cd modules/core_spectrum && python3 -m pytest tests/ -q
python3 modules/processor_ab/scripts/compute_v20.py

# лаборатория гипотез
cd HYPOTHESIS_LAB && python3 ab_lab.py doctor
python3 ab_lab.py run spinor --theta 1.0471975511965976
```

> [!TIP]
> Требования: Python ≥ 3.10 (`requirements.txt`), Julia ≥ 1.10 (только
> стандартная библиотека). Никакой сети и внешних сервисов не нужно.

---

## 🌐 Веб-лаборатории

| Лаборатория | Вкладок | Что внутри |
|-------------|---------|------------|
| [`web_lab/index.html`](web_lab/index.html) — **портал** | 3 блока + теоремы | уровни исследования, слой Th1–Th6, формальный статус, спинор-исследование |
| [`modules/core_spectrum/web_lab/`](modules/core_spectrum/web_lab/index.html) | **10** | Z(t) Римана–Зигеля, конструктор затворов, след↔простые, критерий Ли, ψ-лестница, V16–V19, **Теоремы** |
| [`modules/processor_ab/web_lab/`](modules/processor_ab/web_lab/index.html) | **8** | ISA, компилятор V20, считывание нулей (V23·E11/E17), нелокальность, дорожная карта, данные, **Теоремы** |
| [`HYPOTHESIS_LAB/hypothesis_lab.html`](HYPOTHESIS_LAB/hypothesis_lab.html) | 4 батареи | спинор-циклы, компиляция Гивенса–QR, счётчик N(T), правила дисциплины — **ваши гипотезы** |

Все вычисления в лабораториях исполняются **локально в браузере** — без
сети и зависимостей.

---

## 🛡️ Дисциплина честности

1. **Предрегистрация** — все пороги зафиксированы ДО прогона
   (протоколы кампаний V*, E*, ES*; поле `pre_registered` цитирует их
   дословно в каждом вердикте).
2. **Слепые протоколы** — детектор и валидатор разделены; выходы
   пинованы SHA256 до валидации (E11/E17/V01/ES*).
3. **Кросс-языковая репликация** — Julia BigFloat ↔ Python mpmath (0.0
   расхождений, побитово), numpy-репликации компилятора (0 расхождений
   счётчиков), контрольные файлы мультиязычных реализаций (C/C++/Rust/Go/JS).
4. **Отрицательные результаты публикуются** — ζ-соответствия на решётке
   НЕ найдены (V1/V3/V6/V16), вихри ломают Th5, 2q-оптимум KAK вне
   ISA-класса.
5. **Эрратумы** — константы B/C₀ Th6 найдены и исправлены; γ₁₂ каркаса
   опровергнут слепым детектором; пороги ES2a/ES5a заменены до принятия
   вердиктов — всё опубликовано в вердиктах.
6. **Машина обязательств V13** — вывод RH заблокирован, пока
   аналитические гипотезы (O08/O09/O11/O12) не доказаны; ни одна численная
   проверка не повышает их статус.

---

## 🗺️ Дорожные карты (сцеплены)

| Уровень | Статус | Дальше |
|---------|--------|--------|
| Ядро (R2) | V19 сшивка — алгебраический сертификат | r_align ≤ 0.135; монодромия ζ; компиляция Lean/Coq (O-lean/O-coq) |
| Процессор (P0–P6) | **P0 исполнен** (V20) | P1 память V21 → P2 АЛУ V22 → P3 чтение V23 → P4 нелокальность V24 → P5 бенчмарки → P6 Datasheet 1.0 |
| Верификация (O-J) | **O-J1, O-J2 исполнены** | O-J3 QEC-память → O-J4 цифровой двойник → O-J5 интеграция; высоты T ≫ 1000 |
| Спинор | **ES1–ES5 исполнены** | фазы θ = π/k для k > 7; компиляция задач в фазовые циклы; диффузионный канал |

Сцепление: P3 (V23) опирается на E17; P4 (V24) — на E13/E14; O-J3 — на
E07 и V21; спинор-исследование формализует «читает, не несёт» для P1.
Полная карта — [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md).

---

## 📜 Цитирование

```bibtex
@misc{ab_cloud_quantum_research_2026,
  title  = {AB Cloud Quantum Research: an AB (Aharonov--Bohm) algebraic
            architecture that reads mathematics in real time and stores
            nothing},
  author = {Isaev, Iskhak Khamzatovich},
  year   = {2026},
  version= {1.1.0},
  url    = {https://github.com/wild8highlander/ab-cloud-research}
}
```

См. также `CITATION.cff` и CITATION.cff модулей.

---

## 📜 Лицензия

Все материалы этой папки — включая `MONOGRAPH_ARCHIVE/`, `HYPOTHESIS_LAB/`
и `VISUAL_ANIMATIONS/` — распространяются по **индивидуальной
проприетарной персональной лицензии автора** (© 2026 Исаев Исхак Хамзатович,
ORCID 0009-0003-7299-0701): разрешены чтение, клонирование для частного
некоммерческого изучения, локальные научные запуски кода и цитирование с
атрибуцией; переиздание существенных частей, коммерческое использование и
присвоение — только по письменному согласию автора. Лицензия продублирована
дословно в каждой новой папке. Полный текст: [`LICENSE`](../LICENSE).

<div align="center">
<img src="assets/avatars/avatar_author.svg" width="120" alt="аватар автора">
</div>

---

## English

**AB Cloud Quantum Research v1.1.0** is a single study of one idea: the
algebraic AB (Aharonov–Bohm) architecture as a computing fabric that *reads*
mathematics in real time and stores nothing. Four levels — the spectral core
(V01–V19, theorems Th1–Th6, the V13 obligation machine keeping RH honestly
blocked), the AB processor (V20/P0: exact Givens-QR compilation, 1−F ≤
4.4e−16; "reads, does not carry": 12/12 ζ zeros from six trace-formula
constants; no-signaling nonlocality), the cross-language verification
platform (E01–E18: blind reading of all 649+639 ζ zeros up to T = 1000 by
two engines with bit-exact agreement; the class-B compiler vs 5 baselines at
×59,000), and the supplementary spinor study (θ = π/2, π/3, π/7 — the
machine with no long-term memory). Nine theorems with certificates, 36
bilingual documents, 20 four-dimension tiles @600 dpi, 43 pre-registered
campaigns — all PASS.

**New in 1.1.0:** 📚 [`MONOGRAPH_ARCHIVE/`](MONOGRAPH_ARCHIVE/README.md) —
the main monograph in Russian and English (DOCX + PDF, 104+ pages, 28
figures, 44 tables) plus four level research program monographs and 10
LaTeX sources; 🧪 [`HYPOTHESIS_LAB/`](HYPOTHESIS_LAB/README.md) — the
hypothesis laboratory (CLI + browser, 4 batteries); 🎞
[`VISUAL_ANIMATIONS/`](VISUAL_ANIMATIONS/README.md) — how the whole folder
works (GIF + animated SVG + interactive HTML). The license is duplicated in
every new folder. Full English version — [`README.md`](README.md); every
folder carries bilingual READMEs.

---

<div align="center">

*Собрано дисциплиной: предрегистрация · слепые протоколы · репликация ·
отрицательные результаты публикуются*

<img src="VISUAL_ANIMATIONS/svg/logo_pulse.svg" width="130" alt="медальон AB cloud">

**AB Cloud Quantum Research** · v1.1.0 · © Исаев Исхак Хамзатович

</div>
