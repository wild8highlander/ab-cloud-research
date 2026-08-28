# AB-Cloud Verification Suite

Верификационный пакет для AB-Cloud гипотезы Изсаева — 10 языков программирования,
3 возражения рецензентов, двуязычный интерфейс (RU/EN), параметрическая загрузка нулей.

---

## Структура / Structure

```
ab-cloud-verification/
├── data/                        # Нули дзета-функции Римана (8 файлов, до 2M нулей)
│   ├── zeta_zeros_50000.txt     #   13 661 нулей (по умолчанию)
│   ├── zeta_zeros_500k_odlyzko.txt  # 500 000 нулей
│   ├── zeta_zeros_2M_odlyzko.txt    # 2 000 000 нулей
│   ├── zeta_zeros_highT_blocks.txt  # Нули при высоких T
│   ├── zeros6.txt                   # 2M+ нулей (Odlyzko)
│   └── ...
├── python/       # Python 3.10+  — 4 файла (main, EN, RU, runner)
├── cpp/          # C++17         — 4 файла (main, EN, RU, runner)
├── fortran/      # Fortran 2018  — 4 файла
├── julia/        # Julia 1.9+    — 4 файла
├── rust/         # Rust 1.70+    — 4 файла (src/ + Cargo.toml)
├── r/            # R 4.3+        — 4 файла
├── matlab/       # MATLAB R2021b+ — 4 файла
├── javascript/   # Node.js 18+   — 4 файла
├── go/           # Go 1.21+      — 5 файлов (zeros.go, verify_en/ru.go, main.go)
├── haskell/      # Haskell 2010  — 5 файлов (ZerosLoader, VerifyEN/RU, Main)
└── README.md     # Этот файл
```

## Три возражения рецензентов / Three Reviewer Objections

### Возражение 1: Численная устойчивость b(N)
**Утверждение:** Поправка AB b(N) = (1/N) Σ|γ_k − γ̃_k| сходится при N → ∞.

**Верификация:** Вычисление b(N) для N = 100, 500, 1000, 5000, 10 000, 50 000, …
с выводом таблицы сходимости и графика.

### Возражение 2: Статистическая значимость (GUE)
**Утверждение:** Нормированные расстояния между нулями подчиняются GUE (Wigner–Dyson).

**Верификация:** KS-тест и Cramér–von Mises тест распределения
s_k = (γ_{k+1} − γ_k) · log(γ_k / 2π) / (2π)
против p(s) = (πs/2) exp(−πs²/4). Критерий: p-value > 0.05.

### Возражение 3: Скорость убывания при больших T
**Утверждение:** b(N) = O(1/√N), т.е. наклон log–log графика ≈ −0.5.

**Верификация:** Линейная регрессия log(b(N)) vs log(N), доверительный интервал 95%.

---

## Быстрый старт / Quick Start

### Python
```bash
cd python
python run_verify.py --zeros 5000 --objection all --lang ru
python run_verify.py --zeros 200000 --source 500k --objection 2 --lang en
```

### C++
```bash
cd cpp
chmod +x run_verify.sh
./run_verify.sh --zeros 50000 --source 50k --objection 1 --lang en
```

### Fortran
```bash
cd fortran
chmod +x run_verify.sh
./run_verify.sh --zeros 10000 --source 50k --objection all
```

### Julia
```bash
cd julia
julia run_verify.jl --zeros 500000 --source 500k --objection all --lang en
```

### Rust
```bash
cd rust
chmod +x run_verify.sh
./run_verify.sh --zeros 50000 --source 500k --objection 1 --lang ru
```

### R
```bash
cd r
Rscript run_verify.R --zeros 50000 --source 50k --objection all --lang en
```

### MATLAB
```matlab
cd matlab
run_verify('--zeros', 50000, '--source', '50k', '--objection', 'all')
```

### JavaScript (Node.js)
```bash
cd javascript
node run_verify.js --zeros 50000 --source 50k --objection all --lang en
```

### Go
```bash
cd go
chmod +x run_verify.sh
./run_verify.sh --zeros 50000 --source 500k --objection all --lang ru
```

### Haskell
```bash
cd haskell
chmod +x run_verify.sh
./run_verify.sh --zeros 50000 --source 50k --objection 1 --lang en
```

---

## Параметры командной строки / CLI Parameters

| Параметр | По умолч. | Описание |
|----------|-----------|----------|
| `--zeros N` | 5000 | Сколько нулей ζ(s) загрузить из файлов данных |
| `--source NAME` | auto | Имя файла: `50k`, `500k`, `2M`, `highT`, `zeros6`, `csv`, `2M_gz`, `auto` |
| `--objection 1|2|3|all` | all | Какое возражение верифицировать |
| `--lang en|ru` | auto | Язык вывода (auto = по переменной LANG) |
| `--data-dir PATH` | ../data | Путь к директории с нулями |

### Автоматический выбор файла данных

| Запрошено нулей | Выбранный файл |
|-----------------|----------------|
| ≤ 13 661 | `zeta_zeros_50000.txt` |
| ≤ 500 000 | `zeta_zeros_500k_odlyzko.txt` |
| ≤ 2 000 000 | `zeta_zeros_2M_odlyzko.txt` |
| > 2 000 000 | `zeros6.txt` |

---

## Структура каждого языка / Per-Language Structure

Каждый язык имеет **4 файла** по модели Python:

| Файл | Описание |
|------|----------|
| `ab_cloud_verify.*` | Основной модуль (двуязычный RU/EN) |
| `ab_cloud_verify_en.*` | Английская версия |
| `ab_cloud_verify_ru.*` | Русская версия |
| `run_verify.*` | Автономный CLI-раннер (один файл) |

Все файлы содержат функцию `load_zeros(data_dir, count, source)` для загрузки
нулей из `../data/` с автоматическим выбором файла.

---

## Автор / Author

**Isaev Iskhak Khamzatovich**
- ORCID: [0009-0003-7299-0701](https://orcid.org/0009-0003-7299-0701)
- Email: aslan08_05@mail.ru
- DOI: [10.5281/zenodo.21825394](https://doi.org/10.5281/zenodo.21825394)

## Лицензия / License

Распространяется вместе с основным репозиторием research-papers.

<!-- ab-cloud:v22-update (2026-08-28) -->

## Обновление v22 / Update v22 (2026-08-28)

- Latest verified run: [results/verification_run_v18_37tests_2026-08-28.txt](../results/verification_run_v18_37tests_2026-08-28.txt)
- Monograph (RU/EN/ZH; docx + pdf + html + pptx + tex): [docs/ab-cloud-v22/](../docs/ab-cloud-v22/)
- Suite: `julia code/ab_cloud_v19.jl --test all` (two-pass; report engine fixed, FIX-R1...R5b)
- Quick check: `julia code/ab_cloud_v19.jl --quick` (16x16 -> 32x32, zeta <= 5000, both passes)
- Legacy DOCX results of this folder removed (superseded by the v22 monograph package).
