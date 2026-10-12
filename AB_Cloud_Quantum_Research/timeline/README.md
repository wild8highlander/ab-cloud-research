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
