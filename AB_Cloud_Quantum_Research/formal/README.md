<!-- enriched 1.1.0 -->
<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/logo_abcloud_dark.png">
  <img src="../assets/logo_abcloud_light.png" width="92" alt="AB Cloud Quantum Research">
</picture>

### ⚖️ Formal layer — Lean 4 / Coq / Agda / Isabelle

`AB Cloud Quantum Research` · v1.1.0 · part of one machine

![badge](https://img.shields.io/badge/program-AB_Cloud_Quantum_Research-C96F4A?style=flat-square)
![badge](https://img.shields.io/badge/verdicts-all%20PASS-3A6B4F?style=flat-square)
![badge](https://img.shields.io/badge/license-proprietary-6B6455?style=flat-square)

</div>

> 🧭 **Navigation:** [↑ main README](../README.md) · [📚 monographs](../MONOGRAPH_ARCHIVE/README.md) · [🧪 hypothesis lab](../HYPOTHESIS_LAB/README.md) · [🎞 animations](../VISUAL_ANIMATIONS/README.md)
# ⚖️ formal/ — формальный слой единого пакета (мост)

Формальные исходники живут **в материнской программе**
[`modules/core_spectrum/formal/`](../modules/core_spectrum/formal/README.md)
— здесь их НЕ дублируют (единый источник правды). Этот файл — карта и
сводный статус.

## Что внутри core_spectrum/formal/

| Файл | Система | Содержание | Статус |
|------|---------|------------|--------|
| `lean/RPBasic.lean` | Lean 4 | скелет: сумма |ν|² ≥ 0, Tr(AB)=Tr(BA) | компиляция — O-lean |
| `coq/RPBasic.v` | Coq | те же факты в Gallina | компиляция — O-coq |
| `agda/RPBasic.agda` | Agda | неотрицательность типизацией | компиляция — O-agda |
| `isabelle/RPBasic.thy` | Isabelle/HOL | те же факты в HOL | компиляция — O-isa |
| `lean/RPTheorems.lean` | Lean 4 | **постановки Th1–Th6**, доказанные пропозициональные ядра, редукции к аксиомам A1–A6 | компиляция — O-lean; A1–A6 → Mathlib — O-lean-mathlib |
| `coq/RPTheorems.v` | Coq | те же постановки (intros/exact, без admit) | компиляция — O-coq |
| `obligations.json` | — | DAG обязательств V13 (зеркало rpbridge/formaloblig.py) | verdict: **blocked** |

## Реестр именованных редукций A1–A6

| Аксиома | Классика | Теорема |
|---------|----------|---------|
| A1 | спектральная теорема (эрмитовый случай) | Th1 |
| A2 | одновременная диагонализация (конечная абелева) | Th5 |
| A2b | ‖(H∓iI)ψ‖² = ‖Hψ‖²+‖ψ‖² | Th2 |
| A3 | произведение Адамара для ξ | Th6 |
| A4 | оценка Като–Темпл | Th3 |
| A5 | теорема Гершгорина | Th3 |
| A6 | абсолютная сходимость ряда Ли | Th4 |

Дисциплина: `sorry`/`admit` не используются нигде; каждая глубокая классика
— явно названная аксиома. Ни одна аксиома не является гипотезой RH.
Машина обязательств (V13) подтверждается тестом `test_formal_blocked.py`:
**вывод RH заблокирован**, пока O08/O09/O11/O12 — assumed. Формализация
гарантирует честную блокировку, а не доказательство RH.

## English summary

The formal sources live in `modules/core_spectrum/formal/` (single source
of truth); this folder is a map. Th1–Th6 are formally stated in Lean 4 and
Coq with named reductions A1–A6, no `sorry`/`admit` anywhere; the V13
obligation machine keeps the RH conclusion blocked — the layer guarantees
honest blocking, not a proof of RH.

---

<div align="center">

<img src="../assets/avatars/avatar_author.svg" width="84" alt="author">

*Part of the discipline: pre-registration · blind protocols · replication ·
negative results published*

**AB Cloud Quantum Research** · v1.1.0 ·
[license](../../LICENSE) · © Isaev Iskhak Khamzatovich

</div>
