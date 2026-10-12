# 📖 glossary/ — глоссарий программы

Термины AB Cloud Quantum Research в алфавитном порядке. Курсив —
английский эквивалент. Ссылки ведут в модули/папки.

## А–Я (RU)

**AB-облако** (*AB cloud*) — связная конфигурация связей оператора
H_L, в которой жёсткий вес реализует фазовые затворы; базовый «транзистор»
архитектуры. См. `modules/core_spectrum`, `modules/processor_ab`.

**AB-процессор** (*AB processor*) — процессорный уровень программы
(V20/P0): ISA AB-облаков, точный компилятор Givens-QR, принцип «читает,
а не несёт».

**Затвор AB2 / PHASE** (*AB2 / PHASE gate*) — два класса примитивов ISA:
двухуровневый блок Гивенса и фазовая лестница. Компилятор раскладывает
любую унитарную цель на эти примитивы точно.

**Кампания** (*campaign*) — верифицированный прогон одного направления
(V*, E*, ES*) с вердикт-файлом.

**Машина обязательств (V13)** (*obligation machine*) — формальный
механизм, который держит вывод RH **заблокированным**, пока аналитические
предпосылки O08/O09/O11/O12 имеют статус assumed. Гарантирует честность:
программа изучает модель, а не «доказывает» гипотезу.

**Нулевая модель** (*null model*) — контрастный ансамбль (пермутации,
Haar, GUE-подгонки), относительно которого измеряется сигнал.

**Предрегистрация** (*pre-registration*) — пороги и критерии
зафиксированы ДО прогона; вердикт сравнивается с ними механически.

**Плитка «4 измерения»** (*4-dimension tile*) — фигура 2×2: метрика ·
поведение по инстансам · контроль · порог; строится только из
закоммиченных вердиктов.

**Слепой протокол** (*blind protocol*) — детектор и валидатор разделены,
выходы детектора пинованы SHA256 до валидации (V01, E11, E17).

**Следовая формула (Th6)** (*trace formula*) — Гуинанд–Вейль для H_ξ:
вес простых Λ(n)/√n доказательно живёт в тепловом следе оператора
(r = 0.9996).

**Хранение = 0** (*zero storage*) — принцип «читает, а не несёт»:
результаты читаются из следовой структуры в реальном времени и не
записываются в долговременное хранилище; формализован в исследовании
`research/realtime_spinor_memory` (TS2/TS3).

**Эрратум** (*erratum*) — опубликованная ошибка с исправлением
(B/C₀ Th6; γ₁₂; пороги ES2a/ES5a). Ретуши отрицательных результатов нет.

## A–Z (EN)

**AB cloud** — a connected bond configuration of H_L where stiff weights
realize phase gates; the basic transistor of the architecture.

**AB processor** — the processor level (V20/P0): the AB-cloud ISA, the
exact Givens-QR compiler, "reads, does not carry".

**Campaign** — one verified run of a direction (V*, E*, ES*) with a
verdict file.

**Obligation machine (V13)** — keeps the RH conclusion **blocked** while
analytic prerequisites are assumed; the honesty guarantee of the program.

**Pre-registration** — thresholds fixed before the run; verdicts compare
mechanically.

**Blind protocol** — detector and validator separated; detector outputs
SHA256-pinned before validation (V01, E11, E17).

**4-dimension tile** — a 2×2 figure: metric · instance behaviour ·
control · threshold, built only from committed verdicts.

**Trace formula (Th6)** — Guinand–Weil for H_ξ: the prime weight
Λ(n)/√n provably lives in the heat trace (r = 0.9996).

**Zero storage** — "reads, does not carry": results are read from the
trace structure in real time and never written to long-term storage;
formalized in `research/realtime_spinor_memory` (TS2/TS3).

**Erratum** — a published, fixed mistake (B/C₀ of Th6; γ₁₂; ES2a/ES5a
thresholds). Negative results are never retouched.
