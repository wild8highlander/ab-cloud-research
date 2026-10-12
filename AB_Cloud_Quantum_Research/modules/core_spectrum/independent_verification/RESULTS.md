# independent_verification/RESULTS.md — закоммиченный вердикт прогона

**Прогон 2026-10-10 · AB Research Program 1.1.0 · Python 3.12 / numpy 2.x
/ scipy / mpmath**

| ID | Проверка | Вердикт | Факт |
|----|----------|---------|------|
| IVP01 | целостность релиза | **PASS** | все файлы на месте |
| IVP02 | паспорт Th1 | **PASS** | herm 0.0, resid 4.6e-15 |
| IVP03 | самосопряжённость Th2 | **PASS** | (0,0), дрейф 2.2e-16 |
| IVP04 | слепой r_test в нуле | **PASS** | 0.006 в коридоре ±0.066 |
| IVP05 | GUE-класс + лестница | **PASS** | KS 0.050; Poisson>GOE>GUE |
| IVP06 | следовая формула Th6 | **PASS** | \|ΔQ\|=4.2e-8, \|ΔK\|=6.9e-6 |
| IVP07 | Ли, два пути Th4 | **PASS** | \|Δ\|=2.9e-11, min λ_n = 0.0231 |
| IVP08 | блочная редукция Th5 | **PASS** | eps 0.0, union 7.1e-15 |
| IVP09 | сертификаты Th3 | **PASS** | 5/5 valid |
| IVP10 | RH заблокирована | **PASS** | 7 блокеров, proven 5/12 |
| IVP11 | аудит claims | **PASS** | 19/19, missing [] |
| IVP12 | кампании исполняются | **PASS** | 19/19 OK |
| IVP13 | карта ручек V16 | **PASS** | rows 288, z_best 2.49 < 6, identity_closed False |
| IVP14 | электрон V17 | **PASS** | ΔE 1.8e-15, ratio ×1.62, r_phase −0.96 vs −0.52 |
| IVP15 | процессор V18 | **PASS** | fidelity 1−2e-16, C 0.984, pong 0:1, replay True |
| IVP16 | сшивка ветвей V19 | **PASS** | verdict ALGEBRAIC_CERTIFICATE, resid A 1.3e-40, чередование 100%, замыкание 138 = 138, когерентность 0.9995 |

Управляющий блок C-двойника (IVP-слой мультиязычности):

```
gamma_closure_max_res = 1.133e-14
lambda_sum_check = 1.4989125716
n_sieve = 100000
```

## Что НЕ проверяет этот протокол

- Реплику верификации нулей Одлыжко (файл принимается по SHA-256).
- Компиляцию формального слоя (обязательства O-lean/O-coq/O-agda/O-isa).
- Гипотезы O08/O09/O11 (они честно assumed в DAG V13).
- Конкретную численную реализацию мультиязычных портов go/rust/julia
  (portable sources; тулчейны отсутствуют в среде сборки).
