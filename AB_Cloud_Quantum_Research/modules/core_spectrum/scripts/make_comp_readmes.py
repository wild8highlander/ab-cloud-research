#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""make_comp_readmes.py — генерация билингвальных README для 15 вычислений.

Формат эталона: 9 секций (Вопрос/Результаты/Метод/Рисунки/Монографии/
Данные/Воспроизведение/Честные замечания/Вердикт) + бейджи + футер.
Запуск: python3 scripts/make_comp_readmes.py
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, 'data')

VDIRS = {
    'V01': 'V01_blind_spectrum', 'V02': 'V02_null_models',
    'V03': 'V03_critical_line_scan', 'V04': 'V04_operator_passport',
    'V05': 'V05_limit_lattice', 'V06': 'V06_spectral_identity',
    'V07': 'V07_arithmetic_trace', 'V08': 'V08_self_adjoint',
    'V09': 'V09_symmetry_reduction', 'V10': 'V10_inverse_problem',
    'V11': 'V11_universality_split', 'V12': 'V12_interval_certificates',
    'V13': 'V13_formal_bridge', 'V14': 'V14_claim_audit',
    'V15': 'V15_li_criterion', 'V16': 'V16_full_hamiltonian',
    'V17': 'V17_electron_critical_line', 'V18': 'V18_ab_processor',
    'V19': 'V19_branch_stitching',
}

# fig16 — карта программы; кампании v1.1.0 — fig17–fig19
FIGMAP = {'V16': 17, 'V17': 18, 'V18': 19, 'V19': 20}

RU = {
 'V01': dict(t='Функция V1 · Слепой спектральный эксперимент',
   q='Можно ли предсказать ординаты, которых алгоритм не видел? Разбиение '
     'G_cal ⊔ G_test, калибровка только по G_cal, один слепой прогон.',
   m='rpbridge/blind.py: 8 конфигураций калибровки (master-seed 96…103), '
     'окно 200 уровней, ранговая корреляция приращений через N̄ РВМ, '
     'пермутационный нуль (200 перестановок).',
   h='r_test = 0.006 против нуля −0.002 ± 0.066 (z = 0.09); r_cal = 0.085 '
     '(селекция по 8); тождества на контроле нет.',
   v="{'ru': 'Слепой контроль пройден: индивидуальные ординаты не "
     "предсказываются (Г2-согласовано)', 'en': 'Blind control passed: "
     "individual ordinates are not predicted'}"),
 'V02': dict(t='Функция V2 · Арифметические контрольные модели',
   q='Даёт ли хаотичность решётки ту же статистику без арифметики? Пять '
     'семейств моделей против предрегистрированного вектора S.',
   m='rpbridge/nullmodels.py: M0/N1/N3/N4 + эталоны GUE/GOE/Пуассон; '
     'ансамблевый GUE-эталон для D_KS (16 матриц); Бонферрони 5 семейств.',
   h='M0: ⟨r⟩ = 0.6093, D_KS = 0.0499 — GUE-класс; N3 без вихрей: 0.273 — '
     'вне класса; лестница эталонов воспроизведена.',
   v="{'ru': 'Класс GUE не специфичен; арифметика ищется в следах "
     "(V7)', 'en': 'GUE class is not specific; arithmetic lives in "
     "traces (V7)'}"),
 'V03': dict(t='Функция V3 · Скан критической линии',
   q='Оптимален ли σ = ½ по спектральной статистике? Скан D(σ) по 11 '
     'точкам с плацебо и тремя seeds.',
   m='rpbridge/critical_line.py: веса q_k(σ) = log|ζ(σ+iγ̃_k)| по '
     'серединам γ̃ (вне нулей); кривизна C_h; плацебо на переставленных '
     'ординатах.',
   h='Кривая плоская: argmin ≈ 0.8, C_h < 0, минимум в ½ отсутствует и '
     'не подтверждается плацебо.',
   v="{'ru': 'Заявление об оптимальности σ=½ снято (не "
     "подтверждено)', 'en': 'The σ=½ optimality claim is withdrawn "
     "(not confirmed)'}"),
 'V04': dict(t='Функция V4 · Паспорт оператора (Th1)',
   q='Определён ли оператор строго и что доказано о нём? Паспорт P1–P4.',
   m='rpbridge/operator.py: явные формулы элементов, батарея L ∈ '
     '{12,16,24,32} × ручки; эрмитовость/невязки/киральность.',
   h='‖H−H†‖ = 0 (точно); ‖Hv−λv‖ = 8.8e-15; спаривание λ↔−λ (W=0) '
     '8.2e-15. Th1 доказана.',
   v="{'ru': 'Th1: эрмитовость и вещественность — доказано', "
     "'en': 'Th1: hermiticity and reality — proved'}"),
 'V05': dict(t='Функция V5 · Контролируемый предел L → ∞',
   q='Сходится ли спектральный объект при росте решётки? Три вида '
     'сходимости и закон ошибки.',
   m='rpbridge/limits.py: вложимые вихри (масштабирование от L=12); '
     'C1 уровни, C2 проекторы (BC-возмущение), C3 след; МНК законов.',
   h='e(L) ≈ a·L^(−0.86), R² = 0.80; перекрытие проекторов при '
     'BC-возмущении 0.043; предел — открытое обязательство.',
   v="{'ru': 'Степенной закон ошибки измерен; сходимость L→∞ — "
     "оценка, не доказательство', 'en': 'Power error law measured; "
     "L→∞ convergence is an estimate'}"),
 'V06': dict(t='Функция V6 · Спектральное тождество',
   q='Совпадает ли характеристическая функция оператора с ξ? Прямой '
     'тест и позитивный контроль H_ξ.',
   m='rpbridge/spectral_identity.py: ранги vs нули; контроль Адамара '
     'ln Π|z²−γ²| − ln|ξ| = const (регрессия a + b·z²); зазоры/кратности.',
   h='Затворы: rank 0.036 — тождества нет; H_ξ: log-остаток 5.8e-10 — '
     'тождество есть (тривиально по построению).',
   v="{'ru': 'Тождество: ДА для H_ξ, НЕТ для затворов (измерено)', "
     "'en': 'Identity: YES for H_ξ, NO for gates (measured)'}"),
 'V07': dict(t='Функция V7 · Арифметическая формула следа (Th6)',
   q='Живёт ли вес простых в тепловом следе? Гуинанд–Вейль для H_ξ с '
     'контролируемым остатком.',
   m='rpbridge/arithmetic_trace.py + traceformula.py: произведение '
     'Адамара → Q(a) → синус-преобразование; решето Λ до 2·10⁶; PC0.',
   h='|ΔQ| ≤ 4.6e-8; |ΔK| ≤ 6.9e-6; B + C₀ = 2.5e-10; PC0 r = +0.9996 '
     '(resid 0.027); затворы: resid ≥ 0.115 — разрыв 0.63 порядка.',
   v="{'ru': 'Th6 доказана и верифицирована; вес простых — в H_ξ, не "
     "в затворах', 'en': 'Th6 proved and verified; prime weight in "
     "H_ξ, not gates'}"),
 'V08': dict(t='Функция V8 · Самосопряжённость (Th2)',
   q='Самосопряжён ли оператор и устойчив ли к смене границ? Дефектные '
     'индексы, BC-семейство, унитарность.',
   m='rpbridge/selfadjoint.py: σ_min(H ∓ iI); BC open/torus/твисты; '
     'унитарность e^{−iHt}; Im⟨ψ,Hψ⟩.',
   h='Дефекты (0,0) на L = 12/16/24; дрейф 2.2e-16; сдвиги BC 0.21–0.27; '
     'предел L→∞ — открыто (O03).',
   v="{'ru': 'Th2 доказана (конечномерно); предельная часть — "
     "открытое обязательство', 'en': 'Th2 proved (finite-dim); the "
     "limit part is open'}"),
 'V09': dict(t='Функция V9 · Симметрийная редукция (Th5)',
   q='Разлагается ли спектр по симметрии? Магнитные трансляции тора и '
     'блоки.',
   m='rpbridge/symmetry.py: A = U(2,0), B = U(0,2) — абелева G = ℤ_L×ℤ_L; '
     'совместный собственный базис; блоки и их спектры.',
   h='ε_Ux = 0, ε_Uy = 9.4e-15; объединение 6 блоков = спектр (7.1e-15); '
     'вихри ломают симметрию (ε_g = 5.1).',
   v="{'ru': 'Th5 доказана и верифицирована; вихри разрушают "
     "симметрию', 'en': 'Th5 proved and verified; vortices break the "
     "symmetry'}"),
 'V10': dict(t='Функция V10 · Обратная задача',
   q='Восстанавливается ли арифметика из спектра? Следы степеней, '
     'матрица чувствительности, оптимизация.',
   m='rpbridge/inverse.py: Φ = (Tr H, …, Tr H⁶); J численно; Нелдер–Мид '
     'с 3 стартов; разделение арифметика/случай.',
   h='rank J = 6 (k=6), cond ≈ 8.7e4; восстановление |Δq| = 0.077; '
     'разделение 1.6–3.5; идентифицируемость rank-limited.',
   v="{'ru': 'Часть арифметики неидентифицируема по инвариантам "
     "(ранг-лимит)', 'en': 'Part of the arithmetic is unidentifiable "
     "(rank-limited)'}"),
 'V11': dict(t='Функция V11 · Универсальность после разрушения',
   q='Что выживает при разрушении арифметики? Режимы D1/D2/D3 против '
     'универсальных и арифметических метрик.',
   m='rpbridge/universality.py: 3 seeds × 4 режима; ⟨r⟩ и r_EF; нулевой '
     'разбор — собственный scatter A0.',
   h='⟨r⟩ = 0.61 → 0.59 (выживает); сдвиг r_EF 0.17 < 2σ(A0) = 0.57 — '
     'шум-доминировано; разделение несёт V7.',
   v="{'ru': 'Универсальность — аттрактор; арифметика на окнах не "
     "видна', 'en': 'Universality is an attractor; arithmetic "
     "invisible on windows'}"),
 'V12': dict(t='Функция V12 · Интервальные сертификаты (Th3)',
   q='Гарантированы ли численные границы? Гершгорин в рациональной '
     'арифметике + невязка в dps=40.',
   m='rpbridge/intervalcert.py: fractions-радиусы; оценка Каутского '
     'δ²/gap; зазоры точно.',
   h='5/5 сертификатов содержат истинные λ; ширина ~1e-27; Гершгорин '
     '[−4.21, 4.21] накрывает спектр.',
   v="{'ru': 'Ключевые числа имеют гарантированные интервалы', "
     "'en': 'Key numbers carry guaranteed intervals'}"),
 'V13': dict(t='Функция V13 · Формальный мост',
   q='Заблокирован ли вывод RH формально? DAG обязательств и машина '
     'статусов.',
   m='rpbridge/formaloblig.py: 12 узлов proven/computed/assumed; '
     'ацикличность; блокировка пути O01→O12; formal/ (Lean/Coq/Agda/'
     'Isabelle).',
   h='RH: blocked; блокеров 7 (4 assumed, 3 computed); proven 5/12; DAG '
     'корректен.',
   v="{'ru': 'Вывод RH заблокирован честно и автоматически', "
     "'en': 'The RH conclusion is blocked honestly and automatically'}"),
 'V14': dict(t='Функция V14 · Аудит утверждений',
   q='Трассируется ли каждое утверждение к данным и контроля? Схема из '
     '5 частей + аудитор.',
   m='rpbridge/audit.py: claim-JSON (statement/premises/code/controls/'
     'does_not_prove); A1/A2/A3; запрет p-значений в роли доказательств.',
   h='19/19 claims по схеме (V1–V19); покрытие вердиктов полное; '
     'статус-гигиена '
     'соблюдена.',
   v="{'ru': 'Каждое утверждение трассируется; автоповышение статуса "
     "заблокировано', 'en': 'Every statement is traced; automatic "
     "promotion is blocked'}"),
 'V15': dict(t='Функция V15 · Критерий Ли (Th4)',
   q='Связаны ли коэффициенты Ли со спектром? Спектральная формула '
     'λ_n = Tr g_n(H_ξ) и сертифицированная положительность.',
   m='rpbridge/li.py: два пути (нулевой ряд w^n и след g_n); телескоп '
     '|1−w^n| ≤ n|1−w|; 50k нулей, T ≤ 40433.',
   h='Th4 |Δ| = 4.4e-11; λ₁ = 0.023057 (−B = 0.023096); λ_n > 0 для '
     'n ≤ 3000 (хвосты ≤ 0.115); мост к затворам — O09.',
   v="{'ru': 'Th4 доказана; λ_n > 0 до 3000 измерено; RH не "
     "следует', 'en': 'Th4 proved; λ_n > 0 to 3000 measured; RH does "
     "not follow'}"),
 'V16': dict(t='Функция V16 · Полный гамильтониан × алгебраическая функция',
   q='Связывает ли полное пространство ручек гамильтониана решётку с '
     'нулями ζ через θ-фазу Z_id — без редукции к GUE? Карта 96 '
     'конфигураций × 3 seeds.',
   m='rpbridge/fullham.py: вес q_k = θ(γ̃_k)/π (алгебраическая фаза), '
     'метрика r_align (корреляция приращений ΔU ↔ Δγ, мост по первым '
     '50 уровням, out-of-sample на 150); нулевая модель — 200 '
     'пермутаций; PC — нули Z_id против файла.',
   h='max r_align = +0.160 (z = 2.49 < 6 — тождества нет); веса '
     'θ/log|ζ|/none: −0.108/+0.092/−0.085 — все в нулевой зоне; PC '
     'Z_id↔файл r = 1.0 (38 нулей, 4.9e-10).',
   v="{'ru': 'Тождество не замыкается во всём пространстве ручек; "
     "алгебраическая функция — единственный объект с r=1', 'en': "
     "'Identity does not close over the full handle space; the "
     "algebraic function is the only r=1 object'}"),
 'V17': dict(t='Функция V17 · Электрон на критической прямой',
   q='Проходит ли электрон (волновой пакет) когерентно по каналу '
     'самодуальной линии α = ½ и направляет ли его ζ-облако? '
     'Волновод 96×24, T = 40, три облака.',
   m='rpbridge/electron.py: точная динамика в собственном базисе '
     '(2304×2304), пакет σ=3, k₀=π/2; транзит P(x≥88), отклонение '
     'D_y, когерентность C(t), фазовое сопровождение θ(траектория).',
   h='Энергия 1.8e-15; транзит: чистая 0.160 / ζ 0.112 / случайное '
     '0.069 (ζ/ran = ×1.62); D_y: ζ 2.81 против 0.54; r_phase: ζ '
     '−0.96 против random −0.52.',
   v="{'ru': 'Динамика честная; ζ-облако направляет ×1.62; мост "
     "«линия ½ = Re(s)½» — конъектура (Г4 ДА)', 'en': 'Honest "
     "dynamics; the ζ-cloud guides ×1.62; the line½ = Re(s)½ bridge "
     "is a conjecture (H4 YES)'}"),
 'V18': dict(t='Функция V18 · AB-оператор как процессор',
   q='Работает ли AB-оператор как процессор — ворота, зацепление, '
     'игра? Три уровня вычислительности на строительных блоках '
     'гамильтониана.',
   m='rpbridge/processor.py: P1 — аналитические импульсы {X,Y,Z,H,S,T} '
     'на блоке H₂ = mσz − t·cosφ·σx − t·sinφ·σy; P2 — обменная связка '
     '−J, concurrence Вуттерса; P3 — AB-Pong: доска 64 с фазой π/3, '
     'калибровочно-ковариантные зеркала e^{−2iφx}ψ(2p−x), ИИ с '
     'опережением, голы на x≤5/x≥58.',
   h='Верность всех шести ворот 1.0 − 2e-16; concurrence 0.984 (t = '
     '2.373); партия AB-Pong: счёт 0:1, 10 перехватов, 411 событий, '
     'повтор бит-в-бит.',
   v="{'ru': 'Процессор — ДА: ворота точные, зацепление почти-Белл, "
     "игра исполняется детерминированно', 'en': 'Processor — YES: "
     "exact gates, near-Bell entanglement, the game runs "
     "deterministically'}"),
 'V19': dict(t='Функция V19 · Сшивка ветвей алгебраической функции',
   q='Как сшить ветви полной алгебраической функции критической '
     'прямой? Механизм hodge-laboratory: монодромная склейка листов '
     'и точный фазовый закон ζ^{ra+sb}.',
   m='rpbridge/stitching.py, четыре слоя: A — эталон (Ферма-накрытие, '
     'tanh-sinh по гладкой параметризации t = w^N/(w^N+(1−w)^N)); '
     'B — Z₂-монодромия Z_id (чередование знаков, аргументное '
     'замыкание); C — сшитый объект (Γ-фаза: θ-лестница + знаковая '
     'когерентность); D — регрессия R1/R2/R4.',
   h='Фазовый закон 1.3e-40; ортогональность 225/5.1e-30; чередование '
     '1999/1999; замыкание 138=138 (dev 5.0e-10); θ-лестница 0.832; '
     'когерентность 0.9995 (z = 43.4); flagship 4.5e-40.',
   v="{'ru': 'ALGEBRAIC_CERTIFICATE: Γ-фаза несёт оба признака', "
     "'en': 'ALGEBRAIC_CERTIFICATE: the Γ-phase carries both "
     "signatures'}"),
}

EN = {
 'V01': dict(t='V1 · Blind Spectral Experiment',
   q='Can the algorithm predict ordinates it has never seen? Split '
     'G_cal ⊔ G_test, calibrate on G_cal only, one blind run.',
   m='rpbridge/blind.py: 8 calibration configurations (master seed '
     '96…103), a 200-level window, rank correlation of increments via '
     'the RVM count, permutation null (200 shuffles).',
   h='r_test = 0.006 against null −0.002 ± 0.066 (z = 0.09); r_cal = '
     '0.085 (selection over 8); no identity on test.',
   v="{'ru': 'Слепой контроль пройден', 'en': 'Blind control passed: "
     "individual ordinates are not predicted'}"),
 'V02': dict(t='V2 · Arithmetic Null Models',
   q='Does lattice chaos alone produce the same statistics? Five model '
     'families against a pre-registered vector S.',
   m='rpbridge/nullmodels.py: M0/N1/N3/N4 + GUE/GOE/Poisson references; '
     'ensemble GUE reference for D_KS (16 matrices); Bonferroni over 5 '
     'families.',
   h='M0: ⟨r⟩ = 0.6093, D_KS = 0.0499 — GUE class; N3 (no vortices): '
     '0.273 — outside; the reference ladder is reproduced.',
   v="{'ru': 'Класс GUE не специфичен', 'en': 'The GUE class is not "
     "specific; arithmetic lives in traces (V7)'}"),
 'V03': dict(t='V3 · Critical Line Scan',
   q='Is σ = ½ optimal for the spectral statistics? An 11-point D(σ) '
     'scan with placebo and three seeds.',
   m='rpbridge/critical_line.py: weights q_k(σ) = log|ζ(σ+iγ̃_k)| at '
     'midpoints γ̃ (off the zeros); curvature C_h; placebo on permuted '
     'ordinates.',
   h='The curve is flat: argmin ≈ 0.8, C_h < 0, no minimum at ½ and no '
     'placebo confirmation.',
   v="{'ru': 'Оптимальность σ=½ снята', 'en': 'The σ=½ optimality "
     "claim is withdrawn (not confirmed)'}"),
 'V04': dict(t='V4 · Operator Passport (Th1)',
   q='Is the operator strictly defined and what is proved about it? '
     'Passport P1–P4.',
   m='rpbridge/operator.py: explicit element formulas, battery L ∈ '
     '{12,16,24,32} × handles; hermiticity/residuals/chirality.',
   h='‖H−H†‖ = 0 (exact); ‖Hv−λv‖ = 8.8e-15; pairing λ↔−λ (W=0) '
     '8.2e-15. Th1 proved.',
   v="{'ru': 'Th1 доказана', 'en': 'Th1: hermiticity and reality — "
     "proved'}"),
 'V05': dict(t='V5 · The Controlled Limit L → ∞',
   q='Does the spectral object converge as the lattice grows? Three '
     'kinds of convergence and an error law.',
   m='rpbridge/limits.py: nested vortices (scaled from L=12); C1 levels, '
     'C2 projectors (BC perturbation), C3 trace; law fitting.',
   h='e(L) ≈ a·L^(−0.86), R² = 0.80; projector overlap under BC '
     'perturbation 0.043; the limit is an open obligation.',
   v="{'ru': 'Закон ошибки измерен', 'en': 'Power error law measured; "
     "L→∞ convergence is an estimate'}"),
 'V06': dict(t='V6 · Spectral Identity',
   q='Does the characteristic function coincide with ξ? A direct test '
     'and the positive control H_ξ.',
   m='rpbridge/spectral_identity.py: ranks vs zeros; the Hadamard '
     'control ln Π|z²−γ²| − ln|ξ| = const (a + b·z² regression); gaps '
     'and multiplicities.',
   h='Gates: rank 0.036 — no identity; H_ξ: log residual 5.8e-10 — '
     'identity holds (trivially, by construction).',
   v="{'ru': 'Тождество: ДА для H_ξ', 'en': 'Identity: YES for H_ξ, NO "
     "for gates (measured)'}"),
 'V07': dict(t='V7 · The Arithmetic Trace Formula (Th6)',
   q='Does the prime weight live in the heat trace? Guinand–Weil for '
     'H_ξ with a controlled remainder.',
   m='rpbridge/arithmetic_trace.py + traceformula.py: the Hadamard '
     'product → Q(a) → the sine transform; Λ-sieve to 2·10⁶; PC0.',
   h='|ΔQ| ≤ 4.6e-8; |ΔK| ≤ 6.9e-6; B + C₀ = 2.5e-10; PC0 r = +0.9996 '
     '(resid 0.027); gates: resid ≥ 0.115 — a 0.63-order gap.',
   v="{'ru': 'Th6 доказана', 'en': 'Th6 proved and verified; prime "
     "weight in H_ξ, not gates'}"),
 'V08': dict(t='V8 · Self-Adjointness (Th2)',
   q='Is the operator self-adjoint and stable under boundary changes? '
     'Defect indices, the BC family, unitarity.',
   m='rpbridge/selfadjoint.py: σ_min(H ∓ iI); BC open/torus/twists; '
     'unitarity e^{−iHt}; Im⟨ψ,Hψ⟩.',
   h='Defects (0,0) at L = 12/16/24; drift 2.2e-16; BC shifts 0.21–0.27; '
     'the L→∞ limit is open (O03).',
   v="{'ru': 'Th2 доказана', 'en': 'Th2 proved (finite-dim); the limit "
     "part is open'}"),
 'V09': dict(t='V9 · Symmetry Reduction (Th5)',
   q='Does the spectrum decompose by symmetry? Magnetic torus '
   'translations and blocks.',
   m='rpbridge/symmetry.py: A = U(2,0), B = U(0,2) — abelian G = '
     'ℤ_L×ℤ_L; the joint eigenbasis; blocks and their spectra.',
   h='ε_Ux = 0, ε_Uy = 9.4e-15; union of 6 blocks = spectrum (7.1e-15); '
     'vortices break the symmetry (ε_g = 5.1).',
   v="{'ru': 'Th5 доказана', 'en': 'Th5 proved and verified; vortices "
     "break the symmetry'}"),
 'V10': dict(t='V10 · The Inverse Problem',
   q='Can the arithmetic be recovered from the spectrum? Power traces, '
     'the sensitivity matrix, optimization.',
   m='rpbridge/inverse.py: Φ = (Tr H, …, Tr H⁶); J numeric; Nelder–Mead '
     'from 3 starts; arithmetic/random separation.',
   h='rank J = 6 (k=6), cond ≈ 8.7e4; recovery |Δq| = 0.077; separation '
     '1.6–3.5; identifiability is rank-limited.',
   v="{'ru': 'Ранг-лимит идентифицируемости', 'en': 'Part of the "
     "arithmetic is unidentifiable (rank-limited)'}"),
 'V11': dict(t='V11 · Universality after Destruction',
   q='What survives destroying the arithmetic? Modes D1/D2/D3 against '
     'universal and arithmetic metrics.',
   m='rpbridge/universality.py: 3 seeds × 4 modes; ⟨r⟩ and r_EF; the '
     'null is the own scatter of A0.',
   h='⟨r⟩ = 0.61 → 0.59 (survives); the r_EF shift 0.17 < 2σ(A0) = '
     '0.57 — noise-dominated; the separation is carried by V7.',
   v="{'ru': 'Универсальность — аттрактор', 'en': 'Universality is an "
     "attractor; arithmetic invisible on windows'}"),
 'V12': dict(t='V12 · Interval Certificates (Th3)',
   q='Are the numerical bounds guaranteed? Gershgorin in rational '
     'arithmetic + residuals at dps=40.',
   m='rpbridge/intervalcert.py: fractions radii; the Kato estimate '
     'δ²/gap; exact gaps.',
   h='5/5 certificates contain the true λ; width ~1e-27; Gershgorin '
     '[−4.21, 4.21] covers the spectrum.',
   v="{'ru': 'Гарантированные интервалы', 'en': 'Key numbers carry "
     "guaranteed intervals'}"),
 'V13': dict(t='V13 · The Formal Bridge',
   q='Is the RH conclusion formally blocked? The obligation DAG and the '
     'status machine.',
   m='rpbridge/formaloblig.py: 12 nodes proven/computed/assumed; '
     'acyclicity; blocking of the path O01→O12; formal/ (Lean/Coq/Agda/'
     'Isabelle).',
   h='RH: blocked; 7 blockers (4 assumed, 3 computed); proven 5/12; the '
     'DAG is valid.',
   v="{'ru': 'RH заблокирована честно', 'en': 'The RH conclusion is "
     "blocked honestly and automatically'}"),
 'V14': dict(t='V14 · Claim Audit',
   q='Is every statement traced to data and controls? The 5-part schema '
     '+ auditor.',
   m='rpbridge/audit.py: claim JSON (statement/premises/code/controls/'
     'does_not_prove); A1/A2/A3; p-values banned as proofs.',
   h='19/19 claims per the schema (V1–V19); full verdict coverage; '
     'status '
     'hygiene observed.',
   v="{'ru': 'Утверждения трассируются', 'en': 'Every statement is "
     "traced; automatic promotion is blocked'}"),
 'V15': dict(t='V15 · The Li Criterion (Th4)',
   q='Are the Li coefficients connected to the spectrum? The spectral '
     'formula λ_n = Tr g_n(H_ξ) and certified positivity.',
   m='rpbridge/li.py: two paths (the zero series w^n and the trace of '
     'g_n); the telescope |1−w^n| ≤ n|1−w|; 50k zeros, T ≤ 40433.',
   h='Th4 |Δ| = 4.4e-11; λ₁ = 0.023057 (−B = 0.023096); λ_n > 0 for '
     'n ≤ 3000 (tails ≤ 0.115); the gate bridge — O09.',
   v="{'ru': 'Th4 доказана', 'en': 'Th4 proved; λ_n > 0 to 3000 "
     "measured; RH does not follow'}"),
 'V16': dict(t='V16 · Full Hamiltonian × Algebraic Function',
   q='Does the full handle space couple the lattice to the ζ zeros via '
     'the θ-phase of Z_id — no GUE reduction? A map of 96 '
     'configurations × 3 seeds.',
   m='rpbridge/fullham.py: the weight q_k = θ(γ̃_k)/π (algebraic '
     'phase), the r_align metric (ΔU ↔ Δγ increments, bridge on the '
     'first 50 levels, out-of-sample on 150); the null — 200 '
     'permutations; PC — Z_id zeros against the file.',
   h='max r_align = +0.160 (z = 2.49 < 6 — no identity); weights '
     'θ/log|ζ|/none: −0.108/+0.092/−0.085 — all inside the null zone; '
     'PC Z_id↔file r = 1.0 (38 zeros, 4.9e-10).',
   v="{'ru': 'Тождество не замыкается', 'en': 'Identity does not close "
     "over the full handle space; the algebraic function is the only "
     "r=1 object'}"),
 'V17': dict(t='V17 · Electron on the Critical Line',
   q='Does an electron (a wave packet) pass coherently along the '
     'self-dual line channel α = ½, and does the ζ-cloud guide it? '
     'A 96×24 waveguide, T = 40, three clouds.',
   m='rpbridge/electron.py: exact eigenbasis dynamics (2304×2304), '
     'packet σ=3, k₀=π/2; transit P(x≥88), deviation D_y, coherence '
     'C(t), θ-phase accompaniment along the trajectory.',
   h='Energy 1.8e-15; transit: clean 0.160 / ζ 0.112 / random 0.069 '
     '(ζ/ran = ×1.62); D_y: ζ 2.81 vs 0.54; r_phase: ζ −0.96 vs '
     'random −0.52.',
   v="{'ru': 'Динамика честная', 'en': 'Honest dynamics; the ζ-cloud "
     "guides ×1.62; the line½ = Re(s)½ bridge is a conjecture (H4 "
     "YES)'}"),
 'V18': dict(t='V18 · The AB Operator as a Processor',
   q='Does the AB operator work as a processor — gates, entanglement, '
     'a game? Three levels of computability on the Hamiltonian '
     'building blocks.',
   m='rpbridge/processor.py: P1 — analytic pulses {X,Y,Z,H,S,T} on '
     'the block H₂ = mσz − t·cosφ·σx − t·sinφ·σy; P2 — the exchange '
     'link −J, the Wootters concurrence; P3 — AB-Pong: a 64-site '
     'board at phase π/3, gauge-covariant mirrors e^{−2iφx}ψ(2p−x), '
     'lead-following AI, goals at x≤5/x≥58.',
   h='All six gate fidelities 1.0 − 2e-16; concurrence 0.984 (t = '
     '2.373); an AB-Pong game: score 0:1, 10 intercepts, 411 events, '
     'bit-exact replay.',
   v="{'ru': 'Процессор — ДА', 'en': 'Processor — YES: exact gates, "
     "near-Bell entanglement, the game runs deterministically'}"),
 'V19': dict(t='V19 · Branch Stitching of the Algebraic Function',
   q='How to stitch the branches of the full algebraic function of '
     'the critical line? The hodge-laboratory mechanism: monodromic '
     'sheet gluing and the exact phase law ζ^{ra+sb}.',
   m='rpbridge/stitching.py, four layers: A — the reference (the '
     'Fermat cover, tanh-sinh along the smooth parametrization '
     't = w^N/(w^N+(1−w)^N)); B — the Z₂ monodromy of Z_id (sign '
     'alternation, the argument closure); C — the stitched object '
     '(the Γ-phase: the θ ladder + sign coherence); D — the R1/R2/R4 '
     'regression.',
   h='Phase law 1.3e-40; orthogonality 225/5.1e-30; alternation '
     '1999/1999; closure 138=138 (dev 5.0e-10); θ ladder 0.832; '
     'coherence 0.9995 (z = 43.4); flagship 4.5e-40.',
   v="{'ru': 'ALGEBRAIC_CERTIFICATE: все точные слои закрыты', "
     "'en': 'ALGEBRAIC_CERTIFICATE: all exact layers closed, the "
     "Γ-phase carries both signatures'}"),
}


def render(lang, vid, L, figdir, backref):
    vnum = int(vid[1:])
    figname = f"fig{FIGMAP.get(vid, vnum):02d}_{lang}.png"
    monos = '\n'.join(
        f'| `monograph_{lang}.{ext}` | '
        + ('PDF' if ext == 'pdf' else 'DOCX') + ' |'
        for ext in ('pdf', 'docx'))
    return f"""# {L['t']}

![version](https://img.shields.io/badge/version-1.2.0-298bbc) ![](https://img.shields.io/badge/series-V01--V19-3b4f58) ![](https://img.shields.io/badge/status-honest-3a6b4f)

> **{L['q']}**

[← Back to the main README]({backref})

## Contents

1. [Campaign question](#campaign-question)
2. [Results](#results)
3. [Method](#method)
4. [Figures](#figures)
5. [Monographs](#monographs)
6. [Data](#data)
7. [Reproduction](#reproduction)
8. [Honest remarks](#honest-remarks)
9. [Verdict](#verdict)

---

## Campaign question

{L['q']}

## Results

| Quantity | Value | Status |
|---|---|---|
| Campaign | {vid} (plan Solution {vnum}) | committed verdict |
| Key numbers | {L['h']} | measured/proved |
| Verdict note | {json.load(open(f'{DATA}/{vid.lower()}_verdict.json')).get('verdict_note', L['v'].split("'")[3][:120])} | honest |

## Method

{L['m']}

## Figures

| File | Where |
|---|---|
| `{figname}` | 600 dpi — `figures_hires/{lang}/`; infographics — `figures/{lang}/` |

## Monographs

| File | Format |
|---|---|
{monos}

## Data

| File | Content |
|---|---|
| `data/{vid.lower()}_verdict.json` | committed verdict of the campaign |
| `computations/{VDIRS[vid]}/data/` | campaign artifacts |

## Reproduction

```bash
python3 campaigns/run_{vid.lower()}_*.py        # verdict tour (seconds)
python3 scripts/compute_all.py {vid.lower()}     # fresh recomputation
python3 -m pytest tests/ -q                     # theorem machinery
```

## Honest remarks

- Metrics are pre-registered; verdicts are committed and independent of
  fresh recomputation.
- The zero file is the only external data; no third-party research code
  is imported.
- Every claim of this campaign has a claim file (V14 audit) with the
  list of what it does NOT prove.

## Verdict

**{L['v']}**

---

*AB Research Program v1.1.0 · {vid} · {L['t'].split('·')[-1].strip()}*
"""


def main():
    for vid, d in VDIRS.items():
        vnum = int(vid[1:])
        fig_ru = f'fig{vnum:02d}_ru.png'
        figdir = 'figures_hires'
        ru = render('ru', vid, RU[vid], figdir, '../../README.ru.md')
        en = render('en', vid, EN[vid], figdir, '../../README.md')
        base = os.path.join(ROOT, 'computations', d)
        os.makedirs(base, exist_ok=True)
        open(os.path.join(base, 'README.md'), 'w', encoding='utf-8').write(ru)
        open(os.path.join(base, 'README.en.md'), 'w', encoding='utf-8').write(en)
        print(vid, 'README OK')
    print('ALL COMP READMES DONE')


if __name__ == '__main__':
    main()
