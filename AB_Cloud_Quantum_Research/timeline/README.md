<!-- enriched 1.1.0 -->
<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/logo_abcloud_dark.png">
  <img src="../assets/logo_abcloud_light.png" width="92" alt="AB Cloud Quantum Research">
</picture>

### 🗓️ Timeline — 43 campaigns

`AB Cloud Quantum Research` · v1.1.0 · part of one machine

![badge](https://img.shields.io/badge/program-AB_Cloud_Quantum_Research-C96F4A?style=flat-square)
![badge](https://img.shields.io/badge/verdicts-all%20PASS-3A6B4F?style=flat-square)
![badge](https://img.shields.io/badge/license-proprietary-6B6455?style=flat-square)

</div>

> 🧭 **Navigation:** [↑ main README](../README.md) · [📚 monographs](../MONOGRAPH_ARCHIVE/README.md) · [🧪 hypothesis lab](../HYPOTHESIS_LAB/README.md) · [🎞 animations](../VISUAL_ANIMATIONS/README.md)
# 🗓️ timeline/ — хронологическая карта кампаний

Фигура 600 dpi (RU/EN), построенная из `datasets/campaign_timeline.csv`:
**43 кампании** четырёх уровней исследования на единой ленте статусов —
ядро V01–V19, процессор V20, верификация E01–E18, спинор-исследование
ES1–ES5. Размер маркера подсвечивает каждую пятую кампанию; цвет —
статус (PASS/исполнена — цвет уровня, иначе — красный; красных нет).

| Файл | Описание |
|------|----------|
| `campaign_timeline_ru.png` | хронология, 600 dpi, русский |
| `campaign_timeline_en.png` | хронология, 600 dpi, английский |

Перестроить:

```bash
python3 scripts/make_datasets.py     # сначала данные
python3 scripts/make_timeline.py     # затем фигура
```

## English summary

`timeline/` holds the 600 dpi campaign timeline figure (RU/EN) built
from the committed `datasets/campaign_timeline.csv`: 43 campaigns across
the four levels with status markers. Rebuild with
`scripts/make_timeline.py`.

---

<div align="center">

<img src="../assets/avatars/avatar_author.svg" width="84" alt="author">

*Part of the discipline: pre-registration · blind protocols · replication ·
negative results published*

**AB Cloud Quantum Research** · v1.1.0 ·
[license](../../LICENSE) · © Isaev Iskhak Khamzatovich

</div>
