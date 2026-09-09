# =====================================================================
# Magic_Alpha_Points.jl
# =====================================================================
# 61 "магическая" точка α для тестирования универсальности RMT-класса
# AB-облака. Эти точки включают:
#   - π-фракции: π/30, π/29, ..., π/5, π/4
#   - π-множители: π×1, π×2, π×3, π×4, π×5
#   - Квадратные корни: √2, √3, ..., √15
#   - Рациональные: 1/12, 1/6, 1/4, 1/3, 1/2, 2/3, 3/4, 5/6, 2/5
#   - Константы: φ (золотое сечение), e, ln(2), 1/e, 1/π, e mod 1
#   - Специальные: √2-1, √12, √8
#
# Эти точки соответствуют "магическим" значениям α из оригинального
# RMT-исследования AB-облака (где α — поток Aharonov-Bohm).
# =====================================================================

struct AlphaPoint
    value::Float64
    label::String
    category::String  # "π-fraction", "π-multiplier", "√", "rational", "constant", "special"
end

"""
Список всех 61 магических точек α из оригинального исследования.
"""
const MAGIC_ALPHA_POINTS = AlphaPoint[
    # Порядок: 0.0 → 0.87298
    AlphaPoint(0.00000, "0", "zero"),
    AlphaPoint(1/12, "1/12", "rational"),
    AlphaPoint(π/30, "π/30", "π-fraction"),
    AlphaPoint(π/29, "π/29", "π-fraction"),
    AlphaPoint(π/28, "π/28", "π-fraction"),
    AlphaPoint(π/27, "π/27", "π-fraction"),
    AlphaPoint(π/26, "π/26", "π-fraction"),
    AlphaPoint(π/25, "π/25", "π-fraction"),
    AlphaPoint(π/24, "π/24", "π-fraction"),
    AlphaPoint(π/23, "π/23", "π-fraction"),
    AlphaPoint(0.137, "~√2-1", "special"),
    AlphaPoint(π*1, "π×1", "π-multiplier"),
    AlphaPoint(π/22, "π/22", "π-fraction"),
    AlphaPoint(π/21, "π/21", "π-fraction"),
    AlphaPoint(π/20, "π/20", "π-fraction"),
    AlphaPoint(√10, "√10", "√"),
    AlphaPoint(π/19, "π/19", "π-fraction"),
    AlphaPoint(1/6, "1/6", "rational"),
    AlphaPoint(π/18, "π/18", "π-fraction"),
    AlphaPoint(π/17, "π/17", "π-fraction"),
    AlphaPoint(π/16, "π/16", "π-fraction"),
    AlphaPoint(π/15, "π/15", "π-fraction"),
    AlphaPoint(π/14, "π/14", "π-fraction"),
    AlphaPoint(√5, "√5", "√"),
    AlphaPoint(π/13, "π/13", "π-fraction"),
    AlphaPoint(1/4, "1/4", "rational"),
    AlphaPoint(π/12, "π/12", "π-fraction"),
    AlphaPoint(π*2, "π×2", "π-multiplier"),
    AlphaPoint(π/11, "π/11", "π-fraction"),
    AlphaPoint(π/10, "π/10", "π-fraction"),
    AlphaPoint(√11, "√11", "√"),
    AlphaPoint(1/π, "~1/π", "constant"),
    AlphaPoint(1/3, "1/3", "rational"),
    AlphaPoint(π/9, "π/9", "π-fraction"),
    AlphaPoint(ℯ/2, "e/2", "constant"),
    AlphaPoint(1/ℯ, "1/e", "constant"),
    AlphaPoint(π/8, "π/8", "π-fraction"),
    AlphaPoint(2/5, "2/5", "rational"),
    AlphaPoint(√2, "√2", "√"),
    AlphaPoint(π*3, "π×3", "π-multiplier"),
    AlphaPoint(π/7, "π/7", "π-fraction"),
    AlphaPoint(√6, "√6", "√"),
    AlphaPoint(√12, "√12", "√"),
    AlphaPoint(1/2, "1/2", "rational"),
    AlphaPoint(π/6, "π/6", "π-fraction"),
    AlphaPoint(π*4, "π×4", "π-multiplier"),
    AlphaPoint(√13, "√13", "√"),
    AlphaPoint((1+√5)/2, "φ", "constant"),  # золотое сечение
    AlphaPoint(π/5, "π/5", "π-fraction"),
    AlphaPoint(√7, "√7", "√"),
    AlphaPoint(2/3, "2/3", "rational"),
    AlphaPoint(log(2), "ln(2)", "constant"),
    AlphaPoint(π*5, "π×5", "π-multiplier"),
    AlphaPoint(ℯ - 2, "e mod1", "constant"),
    AlphaPoint(√3, "√3", "√"),
    AlphaPoint(√14, "√14", "√"),
    AlphaPoint(3/4, "3/4", "rational"),
    AlphaPoint(π/4, "π/4", "π-fraction"),
    AlphaPoint(√8, "√8", "√"),
    AlphaPoint(5/6, "5/6", "rational"),
    AlphaPoint(√15, "√15", "√"),
]

# Количество точек
const N_MAGIC_POINTS = length(MAGIC_ALPHA_POINTS)

# Удобные векторы значений и меток
const MAGIC_ALPHA_VALUES = [p.value for p in MAGIC_ALPHA_POINTS]
const MAGIC_ALPHA_LABELS = [p.label for p in MAGIC_ALPHA_POINTS]

"""
    get_magic_alpha_values()

Возвращает вектор всех 61 значений α.
"""
get_magic_alpha_values() = copy(MAGIC_ALPHA_VALUES)

"""
    get_magic_alpha_labels()

Возвращает вектор всех 61 меток α (как String).
"""
get_magic_alpha_labels() = copy(MAGIC_ALPHA_LABELS)

"""
    get_magic_alpha_by_category(category::String)

Возвращает точки α заданной категории.
Категории: "zero", "rational", "π-fraction", "π-multiplier", "√", "constant", "special"
"""
function get_magic_alpha_by_category(category::String)
    return [p for p in MAGIC_ALPHA_POINTS if p.category == category]
end

# Вывод информации
println("Magic_Alpha_Points.jl загружен: $N_MAGIC_POINTS магических точек α")
println("  Категории:")
for cat in ["zero", "rational", "π-fraction", "π-multiplier", "√", "constant", "special"]
    n = count(p -> p.category == cat, MAGIC_ALPHA_POINTS)
    if n > 0
        println("    $cat: $n точек")
    end
end
println("  Диапазон α: от $(MAGIC_ALPHA_VALUES[1]) до $(MAGIC_ALPHA_VALUES[end])")
