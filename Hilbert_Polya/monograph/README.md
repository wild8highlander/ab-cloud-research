# monograph/ — сводные тома и источники контента

```
theorems_volume/  monograph_theorems_{ru,en}.{docx,pdf}  — том теорем T1–T10
appendix_volume/  monograph_appendix_{ru,en}.{docx,pdf}  — протоколы воспроизведения
content/          единый источник контента (ru_part1-3.py, en_part1-3.py)
```

Монографии отдельных вычислений — в computations/C*/monograph_{ru,en}.{docx,pdf}.
Один и тот же контент-JSON рендерится в PDF (ReportLab + html2poster-обложка
+ pypdf) и DOCX (docx-js: обложка-рецепт R1, трёхсекционная нумерация,
TOC-плейсхолдеры). Пересборка: `make monographs`.
