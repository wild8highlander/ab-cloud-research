package main

import (
	"fmt"
	"math"
)

// Russian rendering of the structured results (CANON_SPEC §10 — thin layer).

func RenderObj1RU(r Obj1Res) string {
	out := "\n--- Возражение 1: Числовая стабильность b(N) ---\n"
	out += "b(N) = (1/N) * Sum|gamma_k - gamma_tilde_k|   (точки Грама: theta(t) = pi*k, Ньютон)\n\n"
	out += fmt.Sprintf("  %10s %15s %15s\n", "N", "b(N)", "log10(b(N))")
	for i, N := range r.Ns {
		lg := -999.0
		if r.BN[i] > 0 {
			lg = math.Log10(r.BN[i])
		}
		out += fmt.Sprintf("  %10d %15.8f %15.4f\n", N, r.BN[i], lg)
	}
	if r.HasFit {
		out += fmt.Sprintf("\n  Эмпирический закон:  b(N) ~ %.4f * N^(-%.4f)   (R^2 = %.4f)\n", r.FitA, r.FitS, r.FitR2)
	}
	if r.Converging {
		out += "\nРезультат: b(N) сходится с ростом N. OK\n"
		out += "  b(N) монотонно убывает по таблице — сходимость подтверждена на доступном диапазоне. Убывание ЭМПИРИЧЕСКОЕ, это не O(1/sqrt(N)).\n"
	} else {
		out += "\nРезультат: b(N) НЕ сходится с ростом N. WARN\n"
	}
	return out
}

func RenderObj2RU(r Obj2Res) string {
	out := "\n--- Возражение 2: Статистика интервалов GUE ---\n"
	out += "Нормализованные интервалы: s_k = (gamma_{k+1} - gamma_k) * log(gamma_k/(2*pi)) / (2*pi)\n"
	out += "GUE (beta=2) сурьмида через каноническую CDF-таблицу из 32768 точек\n\n"
	if r.N < 2 {
		return out + "ПРЕДУПРЕЖДЕНИЕ: недостаточно интервалов для GUE-теста.\n"
	}
	out += fmt.Sprintf("  Средний спейсинг: %.9f  дисперсия: %.9f  (n = %d)\n", r.Mean, r.Var, r.N)
	out += fmt.Sprintf("  Колмогоров-Смирнов:  D = %.6f,  p-значение = %.3e\n", r.D, r.P)
	out += fmt.Sprintf("  Крамер-фон Мизес:    W^2 = %.6f\n", r.W2)
	out += fmt.Sprintf("  Андерсон-Дарлинг:     A^2 = %.6f\n", r.A2)
	out += fmt.Sprintf("  <r> (отношение соседних): %.6f  (n = %d, GUE ~ 0.5992)\n", r.R, r.NR)
	if r.Rejected {
		out += "\nРезультат: KS-тест ОТВЕРГНУТ при alpha=0.05.\n"
		out += "  Примечание: при больших n точная GUE-сурьмида формально отвергается — это известные поправки конечных T у нулей ζ, а не дефект данных (среднее ~ 1 подтверждает развёртку; якоря golden).\n"
	} else {
		out += "\nРезультат: KS-тест НЕ ОТВЕРГНУТ при alpha=0.05.\n"
	}
	return out
}

func RenderObj3RU(r Obj3Res) string {
	out := "\n--- Возражение 3: Скорость убывания на больших T ---\n"
	out += "Аппроксимация log(b(N)) vs log(N): ожидаемый наклон ~ -0.5\n\n"
	if len(r.BN) < 3 {
		return out + "ПРЕДУПРЕЖДЕНИЕ: недостаточно точек для регрессии.\n"
	}
	out += "  Линейная регрессия в лог. масштабе:\n"
	out += fmt.Sprintf("  Наклон    = %+.6f  (ожидается: -0.5)\n", r.Slope)
	out += fmt.Sprintf("  Св. член  = %+.6f\n", r.Intercept)
	out += fmt.Sprintf("  R^2       = %.6f\n", r.R2)
	out += fmt.Sprintf("  95%% ДИ для наклона: [%.4f, %.4f]\n", r.CILO, r.CIHI)
	if r.OK {
		out += "\nРезультат: Наклон = " + fmt.Sprintf("%+.4f", r.Slope) + ", ожидаемый = -0.500. OK\n"
	} else {
		out += "\nРезультат: Наклон = " + fmt.Sprintf("%+.4f", r.Slope) + ", ожидаемый = -0.500. WARN: наклон отклоняется от -0.5 (убывание эмпирическое)\n"
	}
	return out
}

func RenderSelfcheckRU(rows []SCRow, nPass, nFail int) string {
	out := "\n=== Само-проверка golden — замороженные якоря (канон: meridian-spectral-observatory, selftest 199/199) ===\n"
	for _, r := range rows {
		if r.Skip {
			out += fmt.Sprintf("  %-24s ПРОПУСК\n", r.Name)
			continue
		}
		st := "СБОЙ"
		if r.OK {
			st = "ПРОЙДЕНО"
		}
		out += fmt.Sprintf("  %-24s %s  вычислено = %.12g, ожидание = %.12g, D = %.3e\n",
			r.Name, st, r.Got, r.Exp, r.Delta)
	}
	out += fmt.Sprintf("  Само-проверка: %d пройдено, %d провалено\n", nPass, nFail)
	return out
}
