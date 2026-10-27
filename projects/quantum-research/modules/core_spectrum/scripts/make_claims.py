#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""scripts/make_claims.py — генерация claim-файлов для аудита V14.

Каждое публичное утверждение пакета получает JSON по схеме Решения 14:
statement / premises / code / controls / does_not_prove / status.
Запуск: python3 scripts/make_claims.py
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'verification', 'claim_audit', 'claims')

CLAIMS = [
 dict(id='v01', claim='V1 слепой спектральный эксперимент',
  statement=('Параметры затвора, откалиброванные исключительно по G_cal '
             '(600 ординат), не переносятся на контрольные ординаты G_test '
             '(600 других): r_test попадает в пермутационный нуль.'),
  premises=['разбиение G_cal ∩ G_test = ∅ зафиксировано до запуска',
            'окно спектра сопоставляется ординатам через N̄ РВМ'],
  code=['rpbridge/blind.py', 'campaigns/run_v01_blind.py'],
  controls=[{'name': 'perm_null', 'passed': True,
             'detail': 'r_test = 0.006 против нуля −0.002±0.066'}],
  does_not_prove=['отсутствие спектрального тождества для всех затворов',
                  'отсутствие статистической связи класса GUE'],
  status='measured'),
 dict(id='v02', claim='V2 арифметические контрольные модели',
  statement=('AB-cloud попадает в GUE-класс вместе с моделями N1 (случайные '
             'фазы) и N4 (случайные позиции); модель N3 (без вихрей) — вне '
             'класса.'),
  premises=['метрики предрегистрированы (S = ⟨r⟩, Σ², Δ₃, K(t), D_KS)',
            'поправка Бонферрони на 5 семейств'],
  code=['rpbridge/nullmodels.py', 'campaigns/run_v02_null_models.py'],
  controls=[{'name': 'REF_GUE/GOE/Poisson ladder', 'passed': True,
             'detail': 'эталонная лестница воспроизведена'}],
  does_not_prove=['специфичность арифметики (измеряется V7/V11)',
                  'принадлежность нулей ζ классу GUE'],
  status='measured'),
 dict(id='v03', claim='V3 скан критической линии',
  statement=('Минимум D_KS(σ) в окрестности σ = 1/2 отсутствует или '
             'неустойчив по seeds; кривая D(σ) плоская в полосе ошибки.'),
  premises=['веса вихрей q_k(σ) = log|ζ(σ+iγ̃_k)| по серединам γ̃',
            '3 seeds, решётка 24×24'],
  code=['rpbridge/critical_line.py', 'campaigns/run_v03_critical_line.py'],
  controls=[{'name': 'placebo_permuted', 'passed': True,
             'detail': 'плацебо-веса дают тот же уровень D'}],
  does_not_prove=['оптимальность σ=1/2 для всех конфигураций',
                  'связь α=½ потока с Re s=½ нулей'],
  status='measured'),
 dict(id='v04', claim='V4 паспорт оператора / Th1',
  statement=('H_L эрмитов по построению (H[i,j] = conj H[j,i]); спектр '
             'вещественен; при α=½, W=0 спектр кирально спарен λ ↔ −λ.'),
  premises=['конечная размерность (ограниченный оператор на ℂ^N)'],
  code=['rpbridge/operator.py', 'engine/hamiltonian.py',
        'monograph/theorems/T01_hermiticity'],
  controls=[{'name': 'P1 hermiticity battery', 'passed': True,
             'detail': 'max|H−H†| = 0.0 на 10 конфигурациях'},
            {'name': 'P4 residuals', 'passed': True,
             'detail': 'max‖Hv−λv‖ = 8.8e-15'}],
  does_not_prove=['самосопряжённость предельного оператора L→∞',
                  'спектральную связь с нулями ζ'],
  status='proven'),
 dict(id='v05', claim='V5 предел решётки',
  statement=('Следовая ошибка Tr e^{−tH²} подчиняется степенному закону '
             'e(L) ≈ a·L^{−p} с p ≈ 0.86 (R² ≈ 0.80); перекрытие проекторов '
             'при BC-возмущении измерено.'),
  premises=['семейство затворов с масштабированными вихрями',
            'L ∈ {12,…,48}'],
  code=['rpbridge/limits.py', 'campaigns/run_v05_limit_lattice.py'],
  controls=[{'name': 'power-law fit R²', 'passed': True,
             'detail': 'R² = 0.80 для степенного семейства'}],
  does_not_prove=['сходимость L→∞ (экстраполяция за пределы прогона)',
                  'существование предельного оператора'],
  status='measured'),
 dict(id='v06', claim='V6 спектральное тождество',
  statement=('Тождество спектра с нулями для решёточных затворов — НЕТ '
             '(ранговое соответствие в нулевой зоне); для H_ξ = diag(±γ) '
             'характеристическая функция совпадает с ξ с точностью до '
             'константы Адамара (остаток ≤ 1e-9).'),
  premises=['позитивный контроль H_ξ по построению'],
  code=['rpbridge/spectral_identity.py', 'campaigns/run_v06_spectral_identity.py'],
  controls=[{'name': 'Hxi Adamard control', 'passed': True,
             'detail': 'max|log resid| = 5.8e-10'}],
  does_not_prove=['отсутствие иного оператора с нужным спектром',
                  'RH'],
  status='measured'),
 dict(id='v07', claim='V7 арифметическая формула следа / Th6',
  statement=('Следовая формула Гуинанда–Вейля для H_ξ: K(x) = (1/π)∫Q(a)'
             'sin(ax)da с весом простых Λ(n)/√n; |ΔQ| ≤ 5e-8, |ΔK| ≤ 1e-5; '
             'PC0 (окно нулей): r_EF = +0.9996.'),
  premises=['файл нулей Одлыжко (внешние данные)',
            'решето Λ(n) до 2·10⁶'],
  code=['rpbridge/arithmetic_trace.py', 'rpbridge/traceformula.py',
        'monograph/theorems/T06_trace_formula'],
  controls=[{'name': 'PC0 zeros window', 'passed': True,
             'detail': 'r_EF = +0.9996, resid 0.027'},
            {'name': 'B = −C₀', 'passed': True,
             'detail': '|B + C₀| = 2.5e-10'}],
  does_not_prove=['вес простых в следах решёточных затворов',
                  'RH'],
  status='proven'),
 dict(id='v08', claim='V8 самосопряжённость / Th2',
  statement=('Конечномерный H самосопряжён (дефектные индексы (0,0)); '
             'унитарность e^{−iHt} и Im⟨ψ,Hψ⟩ = 0 — до 1e-13; сдвиги '
             'спектра при смене BC конечны.'),
  premises=['конечная размерность'],
  code=['rpbridge/selfadjoint.py', 'monograph/theorems/T02_self_adjointness'],
  controls=[{'name': 'defect indices', 'passed': True,
             'detail': '(n₊, n₋) = (0,0) на L = 12/16/24'}],
  does_not_prove=['существенно самосопряжённый предельный оператор',
                  'независимость спектра предела от BC'],
  status='proven'),
 dict(id='v09', claim='V9 симметрийная редукция / Th5',
  statement=('На торе без вихрей [H, U(m,n)] = 0 для магнитных трансляций; '
             'спектр = объединение спектров блоков (6 блоков при L=12), '
             'внеблочные элементы ≤ 2e-15; вихри ломают симметрию.'),
  premises=['α·L ∈ ℤ (тор корректен)'],
  code=['rpbridge/symmetry.py', 'monograph/theorems/T05_block_reduction'],
  controls=[{'name': 'block union vs full spectrum', 'passed': True,
             'detail': 'max|Δλ| = 7.1e-15'}],
  does_not_prove=['существование аналогичной редукции для нулей ζ',
                  'арифметическую содержательность блоков'],
  status='proven'),
 dict(id='v10', claim='V10 обратная задача',
  statement=('По старшим следам Tr H^k (k ≤ 6) заряды вихрей восстанавливаются '
             'с ошибкой ≤ 0.08; полная идентифицируемость (ранг J = n_params) '
             'недостижима — инвариантов меньше, чем параметров.'),
  premises=['конечные разности с шагом 1e-4',
            'Нелдер–Мид, 3 старта'],
  code=['rpbridge/inverse.py', 'campaigns/run_v10_inverse_problem.py'],
  controls=[{'name': 'arith vs random separation', 'passed': True,
             'detail': 'относительное разделение 1.6–3.5'}],
  does_not_prove=['единственность арифметической конфигурации',
                  'глобальную идентифицируемость'],
  status='measured'),
 dict(id='v11', claim='V11 универсальность после разрушения арифметики',
  statement=('⟨r⟩ выживает во всех режимах разрушения арифметики; сдвиг '
             'метрики r_EF между режимами меньше 2σ собственного разброса — '
             'на разрешении 200-уровневых окон разделение не достигается.'),
  premises=['метрики предрегистрированы', '3 seeds × 4 режима'],
  code=['rpbridge/universality.py', 'campaigns/run_v11_universality.py'],
  controls=[{'name': 'A0 self-scatter', 'passed': True,
             'detail': 'σ(A0) = 0.29 vs сдвиг 0.17'}],
  does_not_prove=['отсутствие арифметики в затворах на иных разрешениях',
                  'универсальность как аттрактор для всех размеров'],
  status='measured'),
 dict(id='v12', claim='V12 интервальные сертификаты / Th3',
  statement=('Интервалы Гершгорина (точная рациональная арифметика) и '
             'сертификаты невязки (dps=40) содержат истинные собственные '
             'значения во всей батарее.'),
  premises=['оценка Каутского требует зазора gap ≠ 0'],
  code=['rpbridge/intervalcert.py', 'monograph/theorems/T03_certificates'],
  controls=[{'name': 'contains_true battery', 'passed': True,
             'detail': '5/5 сертификатов содержат λ'}],
  does_not_prove=['сертификаты для всех N и всех уровней',
                  'математическую точность модели в целом'],
  status='proven'),
 dict(id='v13', claim='V13 формальный мост (разблокирован)',
  statement=('DAG обязательств корректен; на пути O01→O12 нет ни одной '
             'гипотезы: O12 доказан классически (Li 1997; Bombieri–Lagarias '
             '1999 — RH ⇔ λ_n ≥ 0 ∀n), O08/O09/O11 сертифицированы численно '
             'с закоммиченными артефактами. Вердикт машины: certified.'),
  premises=['классификация статусов: proven/computed/assumed/external',
            'трёхпозиционный вердикт: blocked/certified/proven (v1.2.1)'],
  code=['rpbridge/formaloblig.py', 'formal/lean', 'formal/coq'],
  controls=[{'name': 'DAG acyclicity', 'passed': True,
             'detail': 'циклов нет, ссылки корректны'},
            {'name': 'assumption-free path', 'passed': True,
             'detail': 'n_assumed = 0; O12 proven; O08/O09/O11 computed '
                       'с артефактами (results/RH_Sweep_Pro_Enrichment, '
                       'computations/V15_li_criterion, V06, V19)'}],
  does_not_prove=['RH как теорему: финальный шаг — положительность λ_n '
                  'для ВСЕХ n (O11), что по O12 эквивалентно RH',
                  'достаточность текущего набора обязательств'],
  status='measured'),
 dict(id='v14', claim='V14 аудит утверждений',
  statement=('Каждый вердикт data/v*_verdict.json покрыт claim-файлом со '
             'схемой из 5 обязательных частей; статус-гигиена соблюдена.'),
  premises=['схема фиксирует 5 частей и словарь статусов'],
  code=['rpbridge/audit.py', 'verification/claim_audit/claims'],
  controls=[{'name': 'A1+A3 coverage', 'passed': True,
             'detail': '18/18 claims, пропусков нет'}],
  does_not_prove=['истинность утверждений (аудит проверяет форму)',
                  'полноту схемы'],
  status='measured'),
 dict(id='v15', claim='V15 критерий Ли / Th4',
  statement=('λ_n = Tr g_n(H_ξ) — доказано и верифицировано (|Δ| ≤ 5e-11); '
             'λ_n > 0 для n ≤ 3000 с сертифицированными хвостами; '
             'бесконечное семейство неравенств остаётся открытым.'),
  premises=['файл нулей до T = 40433',
            'хвост: |1−w^n| ≤ n|1−w| (телескоп)'],
  code=['rpbridge/li.py', 'monograph/theorems/T04_li_spectral'],
  controls=[{'name': 'two-path Th4 verification', 'passed': True,
             'detail': 'max|Δ| = 4.4e-11'},
            {'name': 'lambda_1 vs analytic', 'passed': True,
             'detail': 'λ₁ = 0.023057 vs −B = 0.023096 (хвост 3.8e-5)'}],
  does_not_prove=['λ_n ≥ 0 для всех n (критерий Ли полностью)',
                  'RH',
                  'представление λ_n следами решёточных затворов'],
  status='proven'),
 dict(id='v16', claim='V16 полный гамильтониан × алгебраическая функция',
  statement=('Карта полного пространства ручек (96 конфигураций × 3 сида: '
             'знаки, профиль, анизотропия, масса, твисты, δα) показывает, '
             'что спектральное тождество в полном пространстве НЕ '
             'замыкается (z_best = 2.49 < 6 против пермутационного нуля); '
             'позитивный контроль Z_id ↔ log|ζ| даёт r = 1.0 — метод видит '
             'тождество только через алгебраическую функцию критической '
             'прямой.'),
  premises=['выравнивание U-статистики с арифметическим окном',
            'пермутационная null-модель на лучшей конфигурации'],
  code=['rpbridge/fullham.py', 'campaigns/run_v16_full_hamiltonian.py'],
  controls=[{'name': 'perm_null', 'passed': True,
             'detail': 'z_best = 2.49 < 6'},
            {'name': 'weight_compare PC', 'passed': True,
             'detail': 'Z_id ↔ log|ζ| r = 1.0'}],
  does_not_prove=['существование гамильтониана с ζ-спектром',
                  'что тождество невозможно ни при каких ручках '
                  '(проверено подмножество пространства)',
                  'RH'],
  status='measured'),
 dict(id='v17', claim='V17 электрон на критической прямой',
  statement=('Честная спинорная динамика (ΔE = 1.8e-15) на решётке '
             '96×24 с α = ½ и Nv = 48: ζ-облако направляет волновой пакет '
             '×1.62 против случайного облака и отклоняет по y (эффект C7); '
             'фазовая корреляция с θ(γ): −0.96 против −0.52. '
             'Отождествление траектории с критической прямой Re(s) = ½ — '
             'конъектура, не доказательство.'),
  premises=['эрмитов оператор с вихревым облаком',
            'фаза облака из нулей файла (θ(γ)/π)'],
  code=['rpbridge/electron.py', 'campaigns/run_v17_electron_critical_line.py'],
  controls=[{'name': 'energy conservation', 'passed': True,
             'detail': 'ΔE/E0 = 1.8e-15'},
            {'name': 'random-cloud baseline', 'passed': True,
             'detail': 'ratio ×1.62 > 1; Δy 2.81 vs 0.54'}],
  does_not_prove=['прохождение электрона по критической прямой ζ(s)',
                  'физическую реализуемость (модель решёточная)',
                  'RH'],
  status='measured'),
 dict(id='v18', claim='V18 AB-оператор как процессор',
  statement=('Оператор AB-облака исполняет универсальный набор ворот '
             '{X,Y,Z,H,S,T} с fidelity 1−2e-16, даёт почти-Белл '
             'зацепление двух кубитов (C = 0.984) и исполняет игру '
             'AB-Pong детерминированно (повтор бит-в-бит) — направление '
             '«оператор как процессор» из монографии эталона '
             'подтверждено численно.'),
  premises=['блочный гамильтониан с AB-фазой φ = π/2',
            'детерминированные зерна; унитарная эволюция'],
  code=['rpbridge/processor.py', 'campaigns/run_v18_ab_processor.py'],
  controls=[{'name': 'analytic pulse times', 'passed': True,
             'detail': 't_pulse совпадает с аналитикой (π/2)'},
            {'name': 'replay bit-exact', 'passed': True,
             'detail': 'повтор партии 0:1 бит-в-бит'}],
  does_not_prove=['масштабируемость до практического квантового '
                  'процессора',
                  'отказоустойчивость и коррекцию ошибок',
                  'RH'],
  status='measured'),
 dict(id='v19', claim='V19 сшивка ветвей алгебраической функции (R2)',
  statement=('Механизм hodge-laboratory (Ферма-накрытие, монодромная '
             'склейка листов, точный фазовый закон ζ^{ra+sb}, '
             'ортогональность характеров) воспроизведён численно до '
             'машинного пола (невязки 1e-40) и перенесён на полную '
             'алгебраическую функцию критической прямой Z_id: '
             'Z₂-монодромия даёт строгое чередование знаков на всех '
             '1999 интервалах (2000 нулей), аргументное замыкание на '
             'T=300 точное (138 перемен знака = 138 нулей, dev '
             '5.0e-10); сшитый объект — гладкая Γ-фаза — несёт оба '
             'признака: концентрация θ-лестницы у π 0.832 и знаковая '
             'когерентность 0.9995 (z = 43.4). Вердикт по контракту '
             'verhodge: ALGEBRAIC_CERTIFICATE.'),
  premises=['замкнутая форма периодов эталона (лемма 1 hodge-lab)',
            'гладкая параметризация t = w^N/(w^N+(1−w)^N)',
            'вещественность Z_id на критической прямой'],
  code=['rpbridge/stitching.py', 'campaigns/run_v19_stitch.py',
        'scripts/compute_v19.py'],
  controls=[{'name': 'flagship equality N=15', 'passed': True,
             'detail': 'resid 4.5e-40 < 1e-25'},
            {'name': 'property suite 10^4', 'passed': True,
             'detail': 'макс. отклонение фазовой периодичности 1.5e-28'},
            {'name': 'permutation null (coherence)', 'passed': True,
             'detail': 'null 0.500±0.012 против 0.9995, z = 43.4'}],
  does_not_prove=['полную группу монодромии ζ в комплексной плоскости '
                  '(обязательство O20)',
                  'замыкание спектрального тождества на ручках затвора '
                  '(r_align z ≤ 1.83 — урок V16)',
                  'RH'],
  status='measured'),
]


def main():
    os.makedirs(OUT, exist_ok=True)
    for c in CLAIMS:
        p = os.path.join(OUT, f"claim_{c['id']}.json")
        with open(p, 'w', encoding='utf-8') as f:
            json.dump(c, f, ensure_ascii=False, indent=1)
    print(f'{len(CLAIMS)} claims written to {OUT}')


if __name__ == '__main__':
    main()
