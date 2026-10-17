package main

import (
	"fmt"
	"math"
)

// SCRow is one frozen-anchor check (CANON_SPEC §8).
type SCRow struct {
	Name  string
	Skip  bool
	OK    bool
	Got   float64
	Exp   float64
	Delta float64
}

// Selfcheck compares computed values against the frozen golden anchors.
func Selfcheck(zeros []float64) (rows []SCRow, nPass, nFail int) {
	add := func(name string, got, exp, tol float64, rel bool) {
		d := math.Abs(got-exp) / 1.0
		if rel {
			d = math.Abs(got-exp) / math.Abs(exp)
		}
		ok := !math.IsNaN(got) && !math.IsNaN(got-exp) && d <= tol
		rows = append(rows, SCRow{Name: name, Got: got, Exp: exp, Delta: d, OK: ok})
		if ok {
			nPass++
		} else {
			nFail++
		}
	}
	skip := func(name string, need, have int) {
		rows = append(rows, SCRow{Name: name, Skip: true})
		_ = need
		_ = have
	}

	for _, a := range []struct {
		x, exp float64
	}{
		{0.5, 0.35173371124919584}, {1.0, 0.5671432904097838},
		{3.7, 1.1599531786120223}, {10.0, 1.7455280027406992},
		{271.8, 4.17576816800275}, {12345.6, 7.417247034540566},
	} {
		add(fmt.Sprintf("lambert_w(%g)", a.x), LambertW(a.x), a.exp, 1e-12, true)
	}
	for _, a := range []struct {
		n   int
		exp float64
	}{
		{1, 23.17028270133466}, {2, 27.670182217848343}, {3, 31.71797995477886},
		{10, 54.67523744685398}, {100, 238.58259051450293}, {1000, 1421.25638903275},
		{10000, 9878.910118894457}, {50000, 40434.6952780045},
	} {
		add(fmt.Sprintf("gram_point(n=%d)", a.n), GramPoint(a.n), a.exp, 1e-6, false)
	}
	for _, a := range []struct {
		n   int
		exp float64
	}{
		{100, 3.3321638710140165}, {500, 2.3912304957476382},
		{1000, 2.1072522951855435}, {5000, 1.6299485869022874},
		{10000, 1.4794053414584762}, {50000, 1.2125526772588608},
	} {
		if a.n <= len(zeros) {
			add(fmt.Sprintf("bN(N=%d)", a.n), ComputeBN(zeros, a.n), a.exp, 1e-6, false)
		} else {
			skip(fmt.Sprintf("bN(N=%d)", a.n), a.n, len(zeros))
		}
	}
	if len(zeros) >= 1500 {
		add("bN(N=1000,off=500)", ComputeBNOffset(zeros, 1000, 500), 624.6201618180231, 1e-6, false)
	} else {
		skip("bN(N=1000,off=500)", 1500, len(zeros))
	}
	if len(zeros) >= 50000 {
		z5 := zeros[:50000]
		sp := ComputeSpacings(z5)
		mean := 0.0
		for _, s := range sp {
			mean += s
		}
		mean /= float64(len(sp))
		variance := 0.0
		for _, s := range sp {
			variance += (s - mean) * (s - mean)
		}
		variance /= float64(len(sp) - 1)
		D, p := KSTestDP(sp)
		add("spacings.mean", mean, 0.999976001221201, 1e-9, false)
		add("spacings.var", variance, 0.1590654827835423, 1e-9, false)
		add("ks_zeros.D", D, 0.021619337032982328, 1e-9, false)
		add("ks_zeros.p", p, 9.567870399361496e-21, 1e-6, true)
		add("cvm_zeros.W2", CvmTest(sp), 8.177703317829403, 1e-9, true)
		add("ad_zeros.A2", AdStat(sp), 61.49242624209728, 1e-9, true)
		r, _ := MeanRatio(z5)
		add("rmean_zeros.r", r, 0.6118798907208398, 1e-9, false)
	} else {
		for _, nm := range []string{"spacings.mean/var", "ks_zeros.D/p", "cvm_zeros.W2", "ad_zeros.A2", "rmean_zeros.r"} {
			skip(nm, 50000, len(zeros))
		}
	}
	return rows, nPass, nFail
}
