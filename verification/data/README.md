# Данные: Нули дзета-функции Римана / Data: Riemann Zeta Zeros

## Файлы / Files

| Файл | Нули | Формат | Описание |
|------|------|--------|----------|
| `zeta_zeros_50000.txt` | 13 661 | txt, один нуль на строку | Основной набор (по умолчанию) |
| `zeta_zeros_500k_odlyzko.txt` | 500 000 | txt, один нуль на строку | Расширенный набор (Odlyzko) |
| `zeta_zeros_2M_odlyzko.txt` | 2 000 000 | txt, один нуль на строку | Полный набор (Odlyzko) |
| `zeta_zeros_2M_odlyzko.txt.gz` | 2 000 000 | txt.gz (сжатый) | Сжатая копия 2M нулей |
| `zeta_zeros_highT_blocks.txt` | 30 000+ | txt, блоки с заголовком | Нули при высоких T (блоки около 10¹²) |
| `zeros6.txt` | 2 001 051 | txt, с пробелами | Оригинальная таблица Odlyzko zeros6 |
| `zeta_zeros_50000.csv` | 13 661 | CSV | Формат: index, t, s_real, s_imag, zero_number |
| `Zeta_Zeros_50000.jl` | 13 661 | Julia array | Массив Julia `zeta_zeros_table` |

## Формат / Format

Каждый файл содержит мнимые части `t` нулей ζ(s) на критической линии Re(s) = 1/2,
т.е. ζ(1/2 + it) = 0.

Строки, начинающиеся с `#`, являются комментариями. Пустые строки игнорируются.

## Источники / Sources

- **Odlyzko tables**: [https://www-users.cse.umn.edu/~odlyzko/zeta_tables/](https://www-users.cse.umn.edu/~odlyzko/zeta_tables/)
- **Вычисления автора**: Isaev Iskhak Khamzatovich (ORCID: 0009-0003-7299-0701)

## Использование в кодах / Usage in Codes

Все верификационные коды в `../python/`, `../cpp/` и т.д. обращаются к этим файлам
через функцию `load_zeros(data_dir, count, source)`, где:

- `data_dir` — путь к этой директории (по умолчанию `../data/`)
- `count` — сколько нулей загрузить (например, 200 000)
- `source` — имя файла: `"50k"`, `"500k"`, `"2M"`, `"highT"`, `"zeros6"`, `"csv"`, `"2M_gz"`, `"auto"`

При `source="auto"` автоматически выбирается наименьший файл, содержащий `count` нулей.

### Примеры / Examples

```bash
# Python: загрузить 200 000 нулей из 500k файла
python python/run_verify.py --zeros 200000 --source 500k --objection all

# C++: верификация Objection 1 с 50 000 нулей
./cpp/run_verify.sh --zeros 50000 --source 50k --objection 1

# Julia: все возражения с 500 000 нулей
julia julia/run_verify.jl --zeros 500000 --source 500k --objection all
```
