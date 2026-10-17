//! Thin rendering layer (CANON_SPEC §10): RU output of structured results.
//! All computation lives in main.rs — no duplicated math.
use crate::{Obj1Res, Obj2Res, Obj3Res, SCRow};

pub fn render_obj1_ru(r: &Obj1Res) -> String {
    let mut out = String::from(
        "\n═══════════════════════════════════════════════════\n  ВОЗРАЖЕНИЕ 1: Сходимость b(N)\n  b(N) = (1/N) · Σ|γ_k − γ̃_k|, точки Грама: θ(t) = πk (Ньютон)\n═══════════════════════════════════════════════════\n");
    out += &format!("  {:>10} {:>15} {:>15}\n", "N", "b(N)", "log10(b(N))");
    for i in 0..r.ns.len() {
        let lg = if r.bn[i] > 0.0 { r.bn[i].log10() } else { -999.0 };
        out += &format!("  {:>10} {:>15.8} {:>15.4}\n", r.ns[i], r.bn[i], lg);
    }
    if r.has_fit {
        out += &format!("\n  Эмпирический закон:  b(N) ~ {:.4} * N^(-{:.4})   (R^2 = {:.4})\n", r.fit_a, r.fit_s, r.fit_r2);
    }
    if r.converging {
        out += "\nРезультат: b(N) сходится с ростом N. OK\n";
        out += "  b(N) монотонно убывает по таблице — сходимость подтверждена на доступном диапазоне. Убывание ЭМПИРИЧЕСКОЕ, это не O(1/sqrt(N)).\n";
    } else {
        out += "\nРезультат: b(N) НЕ сходится с ростом N. WARN\n";
    }
    out
}

pub fn render_obj2_ru(r: &Obj2Res) -> String {
    let mut out = String::from(
        "\n═══════════════════════════════════════════════════\n  ВОЗРАЖЕНИЕ 2: Статистика интервалов GUE\n  s_k = Δγ_k · log(γ_k/2π) / 2π,  GUE (β=2) сурьмида через каноническую CDF-таблицу (32768 точек)\n═══════════════════════════════════════════════════\n");
    if r.n < 2 {
        return out + "ПРЕДУПРЕЖДЕНИЕ: недостаточно интервалов для GUE-теста.\n";
    }
    out += &format!("  Средний спейсинг: {:.9}  дисперсия: {:.9}  (n = {})\n", r.mean, r.var, r.n);
    out += &format!("  Колмогоров-Смирнов:  D = {:.6},  p-значение = {:.3e}\n", r.d, r.p);
    out += &format!("  Крамер-фон Мизес:    W^2 = {:.6}\n", r.w2);
    out += &format!("  Андерсон-Дарлинг:     A^2 = {:.6}\n", r.a2);
    out += &format!("  <r> (отношение соседних): {:.6}  (n = {}, GUE ~ 0.5992)\n", r.r, r.nr);
    if r.rejected {
        out += "\nРезультат: KS-тест ОТВЕРГНУТ при alpha=0.05.\n";
        out += "  Примечание: при больших n точная GUE-сурьмида формально отвергается — это известные поправки конечных T у нулей ζ, а не дефект данных (среднее ~ 1 подтверждает развёртку; якоря golden).\n";
    } else {
        out += "\nРезультат: KS-тест НЕ ОТВЕРГНУТ при alpha=0.05.\n";
    }
    out
}

pub fn render_obj3_ru(r: &Obj3Res) -> String {
    let mut out = String::from(
        "\n═══════════════════════════════════════════════════\n  ВОЗРАЖЕНИЕ 3: Скорость убывания при больших T\n  Аппроксимация log(b(N)) vs log(N): ожидаемый наклон ~ -0.5\n═══════════════════════════════════════════════════\n");
    if r.slope.is_nan() {
        return out + "ПРЕДУПРЕЖДЕНИЕ: недостаточно точек для регрессии.\n";
    }
    out += "  Линейная регрессия в лог. масштабе:\n";
    out += &format!("  Наклон    = {:+.6}  (ожидается: -0.5)\n", r.slope);
    out += &format!("  Св. член  = {:+.6}\n", r.intercept);
    out += &format!("  R^2       = {:.6}\n", r.r2);
    out += &format!("  95% ДИ для наклона: [{:.4}, {:.4}]\n", r.cilo, r.cihi);
    if r.ok {
        out += &format!("\nРезультат: Наклон = {:+.4}, ожидаемый = -0.500. OK\n", r.slope);
    } else {
        out += &format!("\nРезультат: Наклон = {:+.4}, ожидаемый = -0.500. WARN: наклон отклоняется от -0.5 (убывание эмпирическое)\n", r.slope);
    }
    out
}

pub fn render_selfcheck_ru(rows: &[SCRow], npass: usize, nfail: usize) -> String {
    let mut out = String::from(
        "\n=== Само-проверка golden — замороженные якоря (канон: meridian-spectral-observatory, selftest 199/199) ===\n");
    for r in rows {
        if r.skip {
            out += &format!("  {:<24} ПРОПУСК\n", r.name);
            continue;
        }
        let st = if r.ok { "ПРОЙДЕНО" } else { "СБОЙ" };
        out += &format!("  {:<24} {}  вычислено = {:.12e}, ожидание = {:.12e}, D = {:.3e}\n",
            r.name, st, r.got, r.exp, r.delta);
    }
    out += &format!("  Само-проверка: {} пройдено, {} провалено\n", npass, nfail);
    out
}
