// ============================================================================
// abcloud — Go port of the meridian-spectral-observatory suite.
//
// Bit-faithful kernel port of ab_cloud_full.jl / hp_audit_standalone.jl /
// AB_Cloud_Monumental_v6_3.jl (computational core), mirroring abcloud_port.cpp
// and the Rust port. No external dependencies — standard library only.
//
// Build:  go build -o abcloud main.go
// Run:    ./abcloud selftest
//
// Eigenvalues: cyclic Jacobi for complex Hermitian matrices (no LAPACK;
// agrees with LAPACK to ~1e-12 — inside the golden tolerances).
// Disorder note: W>0 residual eps uses the portable classic MT19937 (Julia
// uses dSFMT — documented divergence; all golden anchors are W=0).
// ============================================================================
package main

import (
	"encoding/json"
	"fmt"
	"math"
	"math/cmplx"
	"os"
	"path/filepath"
	"sort"
	"strconv"
	"strings"
)

const PI = math.Pi

// ─────────────────────────────────────────────────────────────────────────────
// Classic MT19937 (init_genrand) — bit-identical in all language ports.
// ─────────────────────────────────────────────────────────────────────────────
type MT19937 struct {
	mt  [624]uint32
	idx int
}

func NewMT19937(seed uint32) *MT19937 {
	m := &MT19937{idx: 624}
	m.mt[0] = seed
	for i := 1; i < 624; i++ {
		prev := m.mt[i-1]
		m.mt[i] = 1812433253*(prev^(prev>>30)) + uint32(i)
	}
	return m
}

func (m *MT19937) NextU32() uint32 {
	if m.idx >= 624 {
		for kk := 0; kk < 624; kk++ {
			y := (m.mt[kk] & 0x80000000) | (m.mt[(kk+1)%624] & 0x7fffffff)
			nxt := m.mt[(kk+397)%624] ^ (y >> 1)
			if y&1 != 0 {
				nxt ^= 0x9908b0df
			}
			m.mt[kk] = nxt
		}
		m.idx = 0
	}
	y := m.mt[m.idx]
	m.idx++
	y ^= y >> 11
	y ^= (y << 7) & 0x9d2c5680
	y ^= (y << 15) & 0xefc60000
	y ^= y >> 18
	return y
}

func (m *MT19937) Random() float64 {
	a := float64(m.NextU32() >> 5)
	b := float64(m.NextU32() >> 6)
	return (a*67108864.0 + b) / 9007199254740992.0
}

// ─────────────────────────────────────────────────────────────────────────────
// Scalar special functions (see special.py / abcloud_port.cpp)
// ─────────────────────────────────────────────────────────────────────────────
var lanczosCoef = [9]float64{
	0.99999999999980993, 676.5203681218851, -1259.1392167224028,
	771.32342877765313, -176.61502916214059, 12.507343278686905,
	-0.13857109526572012, 9.9843695780195716e-6, 1.5056327351493116e-7,
}

func lgammaLanczos(x float64) float64 {
	if x < 0.5 {
		return math.Log(PI/math.Sin(PI*x)) - lgammaLanczos(1.0-x)
	}
	x -= 1.0
	a := lanczosCoef[0]
	t := x + 7.0 + 0.5
	for i := 1; i <= 7; i++ {
		a += lanczosCoef[i] / (x + float64(i))
	}
	return 0.5*math.Log(2*PI) + (x+0.5)*math.Log(t) - t + math.Log(a)
}

func gammpSeries(a, x float64) float64 {
	ap := a
	total := 1.0 / a
	delta := total
	for it := 0; it < 200; it++ {
		ap += 1.0
		delta *= x / ap
		total += delta
		if math.Abs(delta) < math.Abs(total)*1e-15 {
			break
		}
	}
	return total * math.Exp(-x+a*math.Log(x)-lgammaLanczos(a))
}

func gammqCf(a, x float64) float64 {
	const FPMIN = 1e-300
	b := x + 1.0 - a
	c := 1.0 / FPMIN
	d := 1.0 / b
	h := d
	for i := 1; i <= 200; i++ {
		an := -float64(i) * (float64(i) - a)
		b += 2.0
		d = an*d + b
		if math.Abs(d) < FPMIN {
			d = FPMIN
		}
		c = b + an/c
		if math.Abs(c) < FPMIN {
			c = FPMIN
		}
		d = 1.0 / d
		delta := d * c
		h *= delta
		if math.Abs(delta-1.0) < 1e-15 {
			break
		}
	}
	return math.Exp(-x+a*math.Log(x)-lgammaLanczos(a)) * h
}

func regularizedGammaP(a, x float64) float64 {
	if x <= 0.0 {
		return 0.0
	}
	if x < a+1.0 {
		return gammpSeries(a, x)
	}
	return 1.0 - gammqCf(a, x)
}

func chi2Cdf(x, df float64) float64 { return regularizedGammaP(df/2.0, x/2.0) }

func ksAsymptoticPvalue(lam float64) float64 {
	if lam <= 0.0 {
		return 1.0
	}
	if lam < 0.6 {
		s2 := 0.0
		for k := 1; k <= 1000; k++ {
			kk := 2.0*float64(k) - 1.0
			term2 := math.Exp(-(kk * kk * PI * PI) / (8.0 * lam * lam))
			s2 += term2
			if term2 < 1e-18 {
				break
			}
		}
		v := 1.0 - math.Sqrt(2*PI)/lam*s2
		if v < 0 {
			v = 0
		} else if v > 1 {
			v = 1
		}
		return v
	}
	s := 0.0
	sign := 1.0
	for k := 1; k <= 100; k++ {
		term := sign * math.Exp(-2.0*float64(k)*float64(k)*lam*lam)
		s += term
		sign = -sign
		if math.Abs(term) < 1e-18 {
			break
		}
	}
	v := 2.0 * s
	if v < 0 {
		v = 0
	} else if v > 1 {
		v = 1
	}
	return v
}

func goeSurmiseCdf(s float64) float64 { return 1.0 - math.Exp(-PI*s*s/4.0) }

func gue2SurmiseCdf(s float64) float64 {
	if s < 0 {
		return 0.0
	}
	x2 := 4.0 * s * s / PI
	return regularizedGammaP(0.5, x2) - (4.0*s/PI)*math.Exp(-x2)
}

func gue2SurmisePdf(s float64) float64 {
	return (32.0 / (PI * PI)) * s * s * math.Exp(-4.0*s*s/PI)
}

func lambertW(x float64) float64 {
	if x <= -1.0/math.E {
		return -1.0
	}
	w := x
	if x >= 1.5 {
		w = math.Log(x) - math.Log(math.Log(x))
	}
	for it := 0; it < 50; it++ {
		ew := math.Exp(w)
		f := w*ew - x
		fp := ew * (w + 1.0)
		fpp := ew * (w + 2.0)
		delta := -f / (fp - 0.5*f*fpp/fp)
		w += delta
		if math.Abs(delta) < 1e-15*math.Abs(w) {
			break
		}
	}
	return w
}

func gramPoint(n int64) float64 {
	if n <= 0 {
		return 0.0
	}
	t := 2 * PI * float64(n) / lambertW(float64(n)/math.E)
	for it := 0; it < 8; it++ {
		arg := t / (2 * PI)
		if arg <= 0 {
			break
		}
		theta := t/2*math.Log(arg) - t/2 - PI/8 + 1.0/(48*t) + 7.0/(5760*t*t*t)
		dtheta := 0.5*math.Log(arg) - 1.0/(48*t*t) - 21.0/(5760*t*t*t*t)
		if math.Abs(dtheta) < 1e-30 {
			break
		}
		t -= (theta - float64(n)*PI) / dtheta
	}
	return t
}

func computeBN(z []float64, n, offset int64) float64 {
	if n > int64(len(z)) {
		n = int64(len(z))
	}
	s := 0.0
	for k := int64(1); k <= n; k++ {
		s += math.Abs(z[k-1] - gramPoint(offset+k))
	}
	return s / float64(n)
}

// ─────────────────────────────────────────────────────────────────────────────
// RMT reference-law engine (see rmt_table.py)
// ─────────────────────────────────────────────────────────────────────────────
type RmtTable struct {
	table []float64
	quant []float64
}

func (r *RmtTable) tableCdf(s float64) float64 {
	if s < 0 {
		return 0
	}
	if len(r.table) == 0 {
		r.table = make([]float64, 32768)
		for i := range r.table {
			r.table[i] = gue2SurmiseCdf(float64(i) * 5.0 / 32767.0)
		}
	}
	if s >= 5.0 {
		return gue2SurmiseCdf(s)
	}
	x := s * 32767.0 / 5.0
	i := int(math.Floor(x))
	if i >= 32767 {
		return gue2SurmiseCdf(s)
	}
	t := x - float64(i)
	return (1.0-t)*r.table[i] + t*r.table[i+1]
}

func (r *RmtTable) gueCdf(s float64) float64 { return r.tableCdf(s) }

func (r *RmtTable) buildQuant() {
	smax := 5.0
	umax := r.gueCdf(smax)
	const M = 4096
	q := make([]float64, M+1)
	for j := 0; j <= M; j++ {
		u := umax * float64(j) / M
		lo, hi := 0.0, smax
		for it := 0; it < 48; it++ {
			mid := 0.5 * (lo + hi)
			if r.gueCdf(mid) < u {
				lo = mid
			} else {
				hi = mid
			}
		}
		q[j] = 0.5 * (lo + hi)
	}
	r.quant = q
}

func (r *RmtTable) Sample(rng *MT19937, out []float64) {
	if len(r.quant) == 0 {
		r.buildQuant()
	}
	const M = 4096
	for k := range out {
		x := rng.Random() * M
		j := int(math.Floor(x))
		if j > M-1 {
			j = M - 1
		}
		if j < 0 {
			j = 0
		}
		t := math.Min(x-float64(j), 1.0)
		out[k] = (1.0-t)*r.quant[j] + t*r.quant[j+1]
	}
}

// [PART2]
// ─────────────────────────────────────────────────────────────────────────────
// GOF + long-range statistics (see gof.py)
// ─────────────────────────────────────────────────────────────────────────────
func normalizedSpacings(z []float64) []float64 {
	sp := make([]float64, 0, len(z))
	for k := 0; k+1 < len(z); k++ {
		if z[k] > 0 {
			sp = append(sp, (z[k+1]-z[k])*math.Log(z[k]/(2*PI))/(2*PI))
		}
	}
	return sp
}

type Linreg struct {
	A, B, R2, SeB float64
	Res           []float64
}

func linreg(x, y []float64) Linreg {
	n := len(x)
	var mx, my float64
	for i := 0; i < n; i++ {
		mx += x[i]
		my += y[i]
	}
	mx /= float64(n)
	my /= float64(n)
	var sxx, sxy float64
	for i := 0; i < n; i++ {
		sxx += (x[i] - mx) * (x[i] - mx)
		sxy += (x[i] - mx) * (y[i] - my)
	}
	if sxx == 0.0 || n < 2 {
		return Linreg{Res: make([]float64, n)}
	}
	b := sxy / sxx
	a := my - b*mx
	res := make([]float64, n)
	var ssRes, ssTot float64
	for i := 0; i < n; i++ {
		res[i] = y[i] - (a + b*x[i])
		ssRes += res[i] * res[i]
		ssTot += (y[i] - my) * (y[i] - my)
	}
	r2 := 0.0
	if ssTot > 0 {
		r2 = 1.0 - ssRes/ssTot
	}
	seB := math.NaN()
	if n > 2 && sxx > 0 {
		seB = math.Sqrt(ssRes / (float64(n-2) * sxx))
	}
	return Linreg{A: a, B: b, R2: r2, SeB: seB, Res: res}
}

func ksTest(r *RmtTable, sp []float64) (float64, float64) {
	n := len(sp)
	s := append([]float64(nil), sp...)
	sort.Float64s(s)
	D := 0.0
	for i := 1; i <= n; i++ {
		F := r.gueCdf(s[i-1])
		D = math.Max(D, math.Max(math.Abs(float64(i)/float64(n)-F),
			math.Abs(float64(i-1)/float64(n)-F)))
	}
	lam := (math.Sqrt(float64(n)) + 0.12 + 0.11/math.Sqrt(float64(n))) * D
	return D, ksAsymptoticPvalue(lam)
}

func cvmTest(r *RmtTable, sp []float64) float64 {
	n := len(sp)
	s := append([]float64(nil), sp...)
	sort.Float64s(s)
	W2 := 0.0
	for i := 1; i <= n; i++ {
		u := r.gueCdf(s[i-1])
		dev := u - (2.0*float64(i)-1.0)/(2.0*float64(n))
		W2 += dev * dev
	}
	return W2 + 1.0/(12.0*float64(n))
}

func andersonDarlingStat(r *RmtTable, sp []float64) float64 {
	n := len(sp)
	s := append([]float64(nil), sp...)
	sort.Float64s(s)
	acc := 0.0
	for i := 1; i <= n; i++ {
		fi := math.Min(math.Max(r.gueCdf(s[i-1]), 1e-300), 1.0-1e-16)
		fni := math.Min(math.Max(r.gueCdf(s[n-i]), 1e-300), 1.0-1e-16)
		acc += (2.0*float64(i) - 1.0) * (math.Log(fi) + math.Log(1.0-fni))
	}
	return -float64(n) - acc/float64(n)
}

func chi2GueTest(r *RmtTable, sp []float64, nbins int) (float64, int64, float64) {
	s := append([]float64(nil), sp...)
	sort.Float64s(s)
	sMax := math.Min(s[len(s)-1], 4.0)
	obs := make([]int64, nbins)
	for _, v := range s {
		if v >= sMax {
			obs[nbins-1]++
		} else {
			b := int(math.Floor(v/sMax*float64(nbins))) + 1
			if b > nbins {
				b = nbins
			}
			obs[b-1]++
		}
	}
	N := len(s)
	edges := make([]float64, nbins+1)
	for i := range edges {
		edges[i] = sMax * float64(i) / float64(nbins)
	}
	var chi2 float64
	var df int64
	for i := 1; i <= nbins; i++ {
		var ec float64
		if i < nbins {
			ec = float64(N) * (r.gueCdf(edges[i]) - r.gueCdf(edges[i-1]))
		} else {
			ec = float64(N) * (1.0 - r.gueCdf(edges[i-1]))
		}
		if ec < 5 {
			continue
		}
		chi2 += (float64(obs[i-1]) - ec) * (float64(obs[i-1]) - ec) / ec
		df++
	}
	if df-1 > 1 {
		df = df - 1
	} else {
		df = 1
	}
	p := 1.0 - chi2Cdf(chi2, float64(df))
	return chi2, df, p
}

func meanAdjacentSpacingRatio(eigs []float64) (float64, int64) {
	n := len(eigs)
	if n < 3 {
		return math.NaN(), 0
	}
	s := append([]float64(nil), eigs...)
	sort.Float64s(s)
	d := make([]float64, n-1)
	for i := 0; i+1 < n; i++ {
		d[i] = s[i+1] - s[i]
	}
	if len(d) < 2 {
		return math.NaN(), 0
	}
	acc := 0.0
	cnt := int64(0)
	for i := 0; i+1 < len(d); i++ {
		a, b := d[i], d[i+1]
		m := math.Max(a, b)
		if a == 0.0 && b == 0.0 {
			continue
		}
		acc += math.Min(a, b) / m
		cnt++
	}
	if cnt <= 0 {
		return math.NaN(), 0
	}
	return acc / float64(cnt), cnt
}

func smoothCountingFunction(T float64) float64 {
	if T <= 0 {
		return 0
	}
	x := T / (2 * PI)
	return x*math.Log(x) - x + 7.0/8.0
}

func unfoldedPositions(z []float64) []float64 {
	pos := make([]float64, len(z))
	for i, t := range z {
		pos[i] = smoothCountingFunction(t)
	}
	return pos
}

func lowerBound(pos []float64, x float64) int {
	return sort.Search(len(pos), func(i int) bool { return pos[i] >= x })
}

func numberVariance(pos []float64, L float64, nWindows int, rng *MT19937) float64 {
	Ltot := pos[len(pos)-1] - pos[0]
	if Ltot <= L {
		return math.NaN()
	}
	counts := make([]float64, nWindows)
	for w := 0; w < nWindows; w++ {
		x0 := pos[0] + rng.Random()*(Ltot-L)
		lo := lowerBound(pos, x0)
		hi := lowerBound(pos, x0+L)
		counts[w] = float64(hi - lo)
	}
	mean := 0.0
	for _, c := range counts {
		mean += c
	}
	mean /= float64(nWindows)
	variance := 0.0
	for _, c := range counts {
		variance += (c - mean) * (c - mean)
	}
	return variance / float64(nWindows-1)
}

func delta3Rigidity(pos []float64, L float64, nWindows, nGrid int, rng *MT19937) float64 {
	Ltot := pos[len(pos)-1] - pos[0]
	if Ltot <= L {
		return math.NaN()
	}
	xs := make([]float64, nGrid)
	for i := range xs {
		xs[i] = L * float64(i) / float64(nGrid-1)
	}
	total := 0.0
	for w := 0; w < nWindows; w++ {
		x0 := pos[0] + rng.Random()*(Ltot-L)
		idx0 := lowerBound(pos, x0)
		nv := make([]float64, nGrid)
		for gi := 0; gi < nGrid; gi++ {
			nv[gi] = float64(lowerBound(pos, x0+xs[gi]) - idx0)
		}
		lr := linreg(xs, nv)
		m2 := 0.0
		for _, e := range lr.Res {
			m2 += e * e
		}
		total += m2 / float64(nGrid)
	}
	return total / float64(nWindows)
}

func computeKSingleSeed(eigs []float64, tvals []float64) []float64 {
	n := len(eigs)
	K := make([]float64, len(tvals))
	if n < 10 {
		return K
	}
	s := append([]float64(nil), eigs...)
	sort.Float64s(s)
	window := int(math.Round(float64(n) * 0.05))
	if window < 3 {
		window = 3
	}
	u := make([]float64, n)
	for i := 1; i < n; i++ {
		iLo := i - window
		if iLo < 0 {
			iLo = 0
		}
		iHi := i + window
		if iHi > n-1 {
			iHi = n - 1
		}
		dens := float64(iHi-iLo+1) / (s[iHi] - s[iLo] + 1e-12)
		u[i] = u[i-1] + (s[i]-s[i-1])*dens
	}
	ms := (u[n-1] - u[0]) / float64(n-1)
	if ms > 1e-12 {
		for i := range u {
			u[i] /= ms
		}
	}
	for idx, t := range tvals {
		if t == 0.0 {
			K[idx] = 0.0
			continue
		}
		re, im := 0.0, 0.0
		for _, uu := range u {
			ph := 2 * PI * t * uu
			re += math.Cos(ph)
			im += math.Sin(ph)
		}
		K[idx] = math.Max(0.0, (re*re+im*im)/float64(n))
	}
	w := 3
	if len(K) > 2*w {
		Ks := append([]float64(nil), K...)
		for j := w; j < len(K)-w; j++ {
			if tvals[j] < 0.5 {
				continue
			}
			acc := 0.0
			for q := -w; q <= w; q++ {
				acc += K[j+q]
			}
			Ks[j] = acc / float64(2*w+1)
		}
		K = Ks
	}
	return K
}

func computeKFormFactor(eigs, tvals []float64) []float64 {
	return computeKSingleSeed(eigs, tvals)
}

func hpKgueEnvelope(t float64) float64 {
	if t < 1.0 {
		x := 2 * PI * t
		sn := 1.0
		if math.Abs(x) >= 1e-12 {
			sn = math.Sin(x) / x
		}
		return t * (1.0 - sn)
	}
	return 1.0
}

func hpUnfoldLocal(eigs []float64, winFrac float64) []float64 {
	s := append([]float64(nil), eigs...)
	sort.Float64s(s)
	n := len(s)
	if n < 10 {
		u := make([]float64, n)
		for i := range u {
			u[i] = float64(i)
		}
		return u
	}
	window := int(math.Round(float64(n) * winFrac))
	if window < 3 {
		window = 3
	}
	u := make([]float64, n)
	for i := 1; i < n; i++ {
		iLo := i - window
		if iLo < 0 {
			iLo = 0
		}
		iHi := i + window
		if iHi > n-1 {
			iHi = n - 1
		}
		dens := float64(iHi-iLo+1) / (s[iHi] - s[iLo] + 1e-12)
		u[i] = u[i-1] + (s[i]-s[i-1])*dens
	}
	ms := (u[n-1] - u[0]) / float64(n-1)
	if ms > 1e-12 {
		for i := range u {
			u[i] /= ms
		}
	}
	return u
}

func unitSpacings(u []float64) []float64 {
	d := make([]float64, 0, len(u))
	for i := 0; i+1 < len(u); i++ {
		d = append(d, u[i+1]-u[i])
	}
	if len(d) == 0 {
		return d
	}
	m := 0.0
	for _, v := range d {
		m += v
	}
	m /= float64(len(d))
	if m > 1e-300 {
		for i := range d {
			d[i] /= m
		}
	}
	return d
}

func ks2(a, b []float64) float64 {
	xs := append([]float64(nil), a...)
	ys := append([]float64(nil), b...)
	sort.Float64s(xs)
	sort.Float64s(ys)
	n, m := len(xs), len(ys)
	i, j := 0, 0
	D := 0.0
	for i < n && j < m {
		if xs[i] < ys[j] {
			i++
		} else if ys[j] < xs[i] {
			j++
		} else {
			xv := xs[i]
			for i < n && xs[i] == xv {
				i++
			}
			for j < m && ys[j] == xv {
				j++
			}
		}
		D = math.Max(D, math.Abs(float64(i)/float64(n)-float64(j)/float64(m)))
	}
	return D
}

// [PART3]
// ─────────────────────────────────────────────────────────────────────────────
// Lattice + cyclic Jacobi Hermitian eigensolver (see lattice.py)
// ─────────────────────────────────────────────────────────────────────────────
type Vortex struct {
	X, Y, Q float64
}

type AbCloudConfig struct {
	Nx, Ny       int
	Vortices     []Vortex
	Alpha, T, W  float64
	Lattice      string // "open" | "torus"
	DisorderSeed uint32
	Model        string // "monumental" | "dirac"
}

func NewConfig(nx, ny int, vortices []Vortex, alpha, t float64, lattice string, w float64) AbCloudConfig {
	return AbCloudConfig{Nx: nx, Ny: ny, Vortices: vortices, Alpha: alpha, T: t,
		Lattice: lattice, W: w, DisorderSeed: 96, Model: "monumental"}
}

func (c AbCloudConfig) With(seed uint32, model string) AbCloudConfig {
	c.DisorderSeed = seed
	c.Model = model
	return c
}

func abPhaseVortexMonumental(ri, rj [2]float64, vort []Vortex) float64 {
	phase := 0.0
	for _, vk := range vort {
		dx1, dy1 := ri[0]-vk.X, ri[1]-vk.Y
		dx2, dy2 := rj[0]-vk.X, rj[1]-vk.Y
		a1 := 0.0
		if dx1 != 0 || dy1 != 0 {
			a1 = math.Atan2(dy1, dx1)
		}
		a2 := 0.0
		if dx2 != 0 || dy2 != 0 {
			a2 = math.Atan2(dy2, dx2)
		}
		phase += vk.Q * (a2 - a1) * 0.5
	}
	return phase
}

func abPhase2d(ri, rj, rk [2]float64, qk float64) float64 {
	ti := math.Atan2(ri[1]-rk[1], ri[0]-rk[0])
	tj := math.Atan2(rj[1]-rk[1], rj[0]-rk[0])
	return qk * (ti - tj)
}

func diracStringPhase(ri, rj, rk [2]float64, qk float64, torus bool, nx int) float64 {
	if math.Abs(ri[0]-rj[0]) > 1e-12 {
		return 0
	}
	yLo, yHi := math.Min(ri[1], rj[1]), math.Max(ri[1], rj[1])
	if !(yLo < rk[1] && rk[1] < yHi) {
		return 0
	}
	if torus {
		if math.Abs(ri[0]-math.Floor(rk[0])) < 0.5 {
			return 0
		}
	} else if ri[0] <= rk[0] {
		return 0
	}
	_ = nx
	if ri[1] < rj[1] {
		return -2 * PI * qk
	}
	return 2 * PI * qk
}

func abPhase2dFull(ri, rj, rk [2]float64, qk float64, torus bool, nx int) float64 {
	return abPhase2d(ri, rj, rk, qk) + diracStringPhase(ri, rj, rk, qk, torus, nx)
}

func vortexOnsitePotential(ri [2]float64, vort []Vortex, W float64, N int, rng *MT19937) float64 {
	if len(vort) == 0 && W == 0.0 {
		return 0
	}
	v := 0.0
	ninv := 1.0 / float64(N)
	for _, vk := range vort {
		dx, dy := ri[0]-vk.X, ri[1]-vk.Y
		v += vk.Q * W / ((dx*dx+dy*dy)*ninv + 1.0)
	}
	if W > 0 {
		v += (rng.Random() - 0.5) * 0.02
	}
	return v
}

func buildAbCloudHamiltonian(cfg AbCloudConfig) []complex128 {
	nx, ny := cfg.Nx, cfg.Ny
	N := nx * ny
	torus := cfg.Lattice == "torus"
	if torus && math.Abs(cfg.Alpha*float64(ny)-math.Round(cfg.Alpha*float64(ny))) >= 1e-10 {
		fmt.Fprintln(os.Stderr, "ASSERT: torus needs alpha*Ny integer")
		os.Exit(2)
	}
	rng := NewMT19937(cfg.DisorderSeed)
	H := make([]complex128, N*N)
	for iy := 1; iy <= ny; iy++ {
		for ix := 1; ix <= nx; ix++ {
			i := (iy - 1) * nx + ix - 1
			ri := [2]float64{float64(ix), float64(iy)}
			// right neighbour
			{
				jx, wrap := ix+1, false
				if jx > nx {
					if torus {
						jx, wrap = 1, true
					} else {
						jx = 0
					}
				}
				if jx != 0 {
					j := (iy - 1) * nx + jx - 1
					phi := 2 * PI * cfg.Alpha * float64(iy)
					if cfg.Model == "dirac" {
						x := float64(jx)
						if wrap {
							x = float64(nx + 1)
						}
						rjp := [2]float64{x, float64(iy)}
						for _, v := range cfg.Vortices {
							phi += abPhase2dFull(ri, rjp, [2]float64{v.X, v.Y}, v.Q, torus, nx)
						}
					}
					hop := -complex(cfg.T, 0) * cmplx.Exp(complex(0, phi))
					H[i*N+j] += hop
					H[j*N+i] += cmplx.Conj(hop)
				}
			}
			// up neighbour
			{
				jy, wrap := iy+1, false
				if jy > ny {
					if torus {
						jy, wrap = 1, true
					} else {
						jy = 0
					}
				}
				if jy != 0 {
					j := (jy - 1) * nx + ix - 1
					phi := 0.0
					if wrap {
						phi = 2 * PI * cfg.Alpha * float64(ny)
					}
					rjp := [2]float64{float64(ix), float64(iy + 1)} // unwrapped top
					if cfg.Model == "monumental" {
						phi += abPhaseVortexMonumental(ri, rjp, cfg.Vortices)
					} else {
						for _, v := range cfg.Vortices {
							phi += abPhase2dFull(ri, rjp, [2]float64{v.X, v.Y}, v.Q, torus, nx)
						}
					}
					hop := -complex(cfg.T, 0) * cmplx.Exp(complex(0, phi))
					H[i*N+j] += hop
					H[j*N+i] += cmplx.Conj(hop)
				}
			}
			H[i*N+i] += complex(vortexOnsitePotential(ri, cfg.Vortices, cfg.W, N, rng), 0)
		}
	}
	// Hermitian symmetrization (H + H†)/2
	for r := 0; r < N; r++ {
		for c := r + 1; c < N; c++ {
			m := 0.5 * (H[r*N+c] + cmplx.Conj(H[c*N+r]))
			H[r*N+c] = m
			H[c*N+r] = cmplx.Conj(m)
		}
	}
	return H
}

func offNorm(H []complex128, n int) float64 {
	acc := 0.0
	for r := 0; r < n; r++ {
		for c := r + 1; c < n; c++ {
			acc += real(H[r*n+c] * cmplx.Conj(H[r*n+c]))
		}
	}
	return acc
}

func jacobiEigvals(H []complex128, n int) []float64 {
	maxSweeps := 60
	off0 := offNorm(H, n)
	thresh := 1e-15 * math.Sqrt(2.0*off0+1e-300)
	for sweep := 0; sweep < maxSweeps; sweep++ {
		off := offNorm(H, n)
		if math.Sqrt(2.0*off) < thresh {
			break
		}
		for p := 0; p < n-1; p++ {
			for q := p + 1; q < n; q++ {
				apq := H[p*n+q]
				if cmplx.Abs(apq) <= thresh {
					continue
				}
				app := real(H[p*n+p])
				aqq := real(H[q*n+q])
				tau := (aqq - app) / (2.0 * cmplx.Abs(apq))
				sgn := 1.0
				if tau < 0 {
					sgn = -1.0
				}
				t := sgn / (math.Abs(tau) + math.Sqrt(1.0+tau*tau))
				c := 1.0 / math.Sqrt(1.0+t*t)
				s := t * c // normalized rotation
				phase := apq / complex(cmplx.Abs(apq), 0)
				se := phase * complex(s, 0)
				sec := cmplx.Conj(se)
				for k := 0; k < n; k++ {
					if k == p || k == q {
						continue
					}
					akp := H[k*n+p]
					akq := H[k*n+q]
					nkp := akp*complex(c, 0) - sec*akq
					nkq := se*akp + akq*complex(c, 0)
					H[k*n+p] = nkp
					H[p*n+k] = cmplx.Conj(nkp)
					H[k*n+q] = nkq
					H[q*n+k] = cmplx.Conj(nkq)
				}
				npp := app - t*cmplx.Abs(apq)
				nqq := aqq + t*cmplx.Abs(apq)
				H[p*n+p] = complex(npp, 0)
				H[q*n+q] = complex(nqq, 0)
				H[p*n+q] = 0
				H[q*n+p] = 0
			}
		}
	}
	ev := make([]float64, n)
	for r := 0; r < n; r++ {
		ev[r] = real(H[r*n+r])
	}
	sort.Float64s(ev)
	return ev
}

func plaquetteFlux(H []complex128, nx, ny, ix, iy int, torus bool) float64 {
	N := nx * ny
	ixR, iyT := ix+1, iy+1
	if torus {
		ixR = (ix % nx) + 1
		iyT = (iy % ny) + 1
	}
	iBl := (iy - 1) * nx + ix - 1
	iBr := (iy - 1) * nx + ixR - 1
	iTr := (iyT - 1) * nx + ixR - 1
	iTl := (iyT - 1) * nx + ix - 1
	fb := cmplx.Phase(-H[iBr*N+iBl])
	fr := cmplx.Phase(-H[iTr*N+iBr])
	ft := cmplx.Phase(-H[iTl*N+iTr])
	fl := cmplx.Phase(-H[iBl*N+iTl])
	return fb + fr + ft + fl
}

func fluxCircdist(a, b float64) float64 {
	m := math.Mod(a-b+PI, 2*PI)
	if m < 0 {
		m += 2 * PI
	}
	return math.Abs(m - PI)
}

func centralBandEigs(s []float64, frac float64) []float64 {
	n := len(s)
	if n == 0 {
		return nil
	}
	frac = math.Min(math.Max(frac, 0.05), 1.0)
	if frac >= 1.0 {
		return append([]float64(nil), s...)
	}
	half := int64(math.Floor(float64(n) * frac / 2.0))
	jLo := int64(n)/2 - half
	if jLo < 1 {
		jLo = 1
	}
	jHi := int64(n)/2 + half
	if jHi > int64(n) {
		jHi = int64(n)
	}
	return s[jLo-1 : jHi]
}

func chiralSymmetryDefect(H []complex128, nx, ny int) float64 {
	N := nx * ny
	var num, den float64
	for r := 0; r < N; r++ {
		sr := -1.0
		if (((r%nx)+1)+(r/nx+1))%2 == 0 {
			sr = 1.0
		}
		for c := 0; c < N; c++ {
			sc := -1.0
			if (((c%nx)+1)+(c/nx+1))%2 == 0 {
				sc = 1.0
			}
			v := H[r*N+c] * complex(sr*sc, 0) + H[r*N+c]
			num += real(v * cmplx.Conj(v))
			den += real(H[r*N+c] * cmplx.Conj(H[r*N+c]))
		}
	}
	return math.Sqrt(num) / math.Max(math.Sqrt(den), 1e-30)
}

func verifyHermitian(H []complex128, n int) bool {
	maxErr, norm := 0.0, 0.0
	for r := 0; r < n; r++ {
		for c := 0; c < n; c++ {
			norm += real(H[r*n+c] * cmplx.Conj(H[r*n+c]))
			maxErr = math.Max(maxErr, cmplx.Abs(H[r*n+c]-cmplx.Conj(H[c*n+r])))
		}
	}
	return maxErr/math.Max(math.Sqrt(norm), 1e-30) < 1e-12
}

func timeReversalAsymmetry(H []complex128) float64 {
	var diff, norm float64
	for _, v := range H {
		norm += real(v * cmplx.Conj(v))
		diff += real((v - cmplx.Conj(v)) * cmplx.Conj(v-cmplx.Conj(v)))
	}
	return math.Sqrt(diff) / math.Max(math.Sqrt(norm), 1e-30)
}

// [PART4]
// ─────────────────────────────────────────────────────────────────────────────
// Golden selftest (compute_all — 1:1 with gen_golden.jl / golden.py)
// ─────────────────────────────────────────────────────────────────────────────
func shortest(v float64) string {
	for prec := 1; prec <= 17; prec++ {
		s := strconv.FormatFloat(v, 'g', prec, 64)
		if !strings.ContainsAny(s, "eE") {
			if back, err := strconv.ParseFloat(s, 64); err == nil && back == v {
				if !strings.Contains(s, ".") {
					s += ".0"
				}
				return s
			}
		}
	}
	for prec := 1; prec <= 17; prec++ {
		s := strconv.FormatFloat(v, 'g', prec, 64)
		if back, err := strconv.ParseFloat(s, 64); err == nil && back == v {
			return s
		}
	}
	return strconv.FormatFloat(v, 'g', 17, 64)
}

func loadZeros(path string) []float64 {
	data, err := os.ReadFile(path)
	if err != nil {
		fmt.Fprintf(os.Stderr, "ERROR: cannot open zeros file: %s\n", path)
		os.Exit(2)
	}
	fields := strings.Fields(string(data))
	z := make([]float64, 0, len(fields))
	for _, f := range fields {
		if v, err := strconv.ParseFloat(f, 64); err == nil {
			z = append(z, v)
		}
	}
	sort.Float64s(z)
	return z
}

type Sec map[string]float64

func computeAll(zeta []float64, golden map[string]interface{}) map[string]Sec {
	sec := map[string]Sec{}
	put := func(name, key string, v float64) {
		if sec[name] == nil {
			sec[name] = Sec{}
		}
		sec[name][key] = v
	}
	rmt := &RmtTable{}

	for _, x := range []float64{0.5, 1.0, 3.7, 10.0, 271.8, 12345.6} {
		put("lambert_w", "x="+shortest(x), lambertW(x))
	}
	for _, n := range []int64{1, 2, 3, 10, 100, 1000, 10000, 50000} {
		put("gram_point", fmt.Sprintf("n=%d", n), gramPoint(n))
	}
	for _, n := range []int64{100, 500, 1000, 5000, 10000, 50000} {
		put("bN", fmt.Sprintf("N=%d", n), computeBN(zeta, n, 0))
	}
	put("bN", "N=1000_off500", computeBN(zeta, 1000, 500))

	sp := normalizedSpacings(zeta)
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
	put("spacings", "n", float64(len(sp)))
	put("spacings", "mean", mean)
	put("spacings", "var", variance)

	for _, s := range []float64{0.05, 0.1, 0.25, 0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 4.9} {
		k := "s=" + shortest(s)
		put("gue2_cdf", k, gue2SurmiseCdf(s))
		put("goe_cdf", k, goeSurmiseCdf(s))
		put("gue2_pdf", k, gue2SurmisePdf(s))
	}
	for _, gx := range [][2]float64{{0.5, 0.1}, {0.5, 2.0}, {1.0, 1.0}, {2.0, 3.0}, {0.5, 12.0}} {
		put("gamma_p", "a="+shortest(gx[0])+"_x="+shortest(gx[1]), regularizedGammaP(gx[0], gx[1]))
	}
	for _, cx := range [][2]float64{{3.84, 1.0}, {16.92, 29.0}, {25.0, 10.0}} {
		put("chi2_cdf", "x="+shortest(cx[0])+"_df="+shortest(cx[1]), chi2Cdf(cx[0], cx[1]))
	}
	for _, lam := range []float64{0.5, 1.3, 0.02} {
		put("ks_pvalue", "lam="+shortest(lam), ksAsymptoticPvalue(lam))
	}

	D, p := ksTest(rmt, sp)
	put("ks_zeros", "D", D)
	put("ks_zeros", "p", p)
	put("cvm_zeros", "W2", cvmTest(rmt, sp))
	put("ad_zeros", "A2", andersonDarlingStat(rmt, sp))
	chi2v, dfv, pchi := chi2GueTest(rmt, sp, 30)
	put("chi2_zeros", "chi2", chi2v)
	put("chi2_zeros", "df", float64(dfv))
	put("chi2_zeros", "p", pchi)
	rMean, nR := meanAdjacentSpacingRatio(zeta)
	put("rmean_zeros", "r", rMean)
	put("rmean_zeros", "n_r", float64(nR))

	pos := unfoldedPositions(zeta)
	rng := NewMT19937(777) // one stream shared across S2→D3 (as gen_golden.jl)
	for _, L := range []float64{5.0, 10.0, 20.0, 50.0, 100.0} {
		put("S2", "L="+shortest(L), numberVariance(pos, L, 3000, rng))
	}
	for _, L := range []float64{5.0, 10.0, 20.0, 50.0} {
		put("D3", "L="+shortest(L), delta3Rigidity(pos, L, 300, 300, rng))
	}

	// grids from golden
	var tvals, omega []float64
	if g, ok := golden["grids"].(map[string]interface{}); ok {
		if arr, ok := g["tvals"].([]interface{}); ok {
			for _, v := range arr {
				tvals = append(tvals, v.(float64))
			}
		}
		if arr, ok := g["omega"].([]interface{}); ok {
			for _, v := range arr {
				omega = append(omega, v.(float64))
			}
		}
	}
	K := computeKFormFactor(zeta, tvals)
	for i, t := range tvals {
		if t == 0.2 || t == 0.5 || t == 1.0 || t == 2.0 || t == 3.0 {
			put("K_zeros", "t="+shortest(t), K[i])
		}
	}
	acc, cnt := 0.0, 0
	for i, t := range tvals {
		if t >= 0.3 {
			e := hpKgueEnvelope(t)
			acc += (K[i] - e) * (K[i] - e)
			cnt++
		}
	}
	put("K_zeros", "rms_env", math.Sqrt(acc/float64(cnt)))

	zs := zeta
	if len(zs) > 20000 {
		zs = zs[:20000]
	}
	n := len(zs)
	w := make([]float64, n)
	for i := 0; i < n; i++ {
		w[i] = 0.5 * (1.0 - math.Cos(2*PI*float64(i)/float64(n-1)))
	}
	sw2 := 0.0
	for _, wi := range w {
		sw2 += wi * wi
	}
	P := make([]float64, len(omega))
	for fi, om := range omega {
		re, im := 0.0, 0.0
		for i := 0; i < n; i++ {
			re += w[i] * math.Cos(om*zs[i])
			im -= w[i] * math.Sin(om*zs[i])
		}
		P[fi] = (re*re + im*im) / sw2
	}
	Ps := append([]float64(nil), P...)
	sort.Float64s(Ps)
	med := 0.5 * (Ps[len(Ps)/2-1] + Ps[len(Ps)/2])
	put("h1_zeta", "median", med)
	for _, pr := range []int{2, 3, 5, 7, 11, 13} {
		tgt := math.Log(float64(pr))
		best, bd := 0, math.Inf(1)
		for i, o := range omega {
			d := math.Abs(o - tgt)
			if d < bd {
				bd, best = d, i
			}
		}
		put("h1_zeta", fmt.Sprintf("snr_log%d", pr), P[best]/med)
	}

	storeEigs := func(name string, ev []float64) {
		nE := len(ev)
		put(name, "eig1", ev[0])
		put(name, "eig2", ev[1])
		put(name, "eig3", ev[2])
		put(name, "eigmid", ev[nE/2-1])
		// Julia: eigend3 = max, eigend2 = second-max, eigend1 = third-max
		put(name, "eigend1", ev[nE-3])
		put(name, "eigend2", ev[nE-2])
		put(name, "eigend3", ev[nE-1])
	}
	e1 := jacobiEigvals(buildAbCloudHamiltonian(NewConfig(8, 8, nil, 0.5, 1.0, "open", 0.0).With(96, "monumental")), 64)
	storeEigs("ham_L8_open_a05_clean", e1)
	e2 := jacobiEigvals(buildAbCloudHamiltonian(NewConfig(8, 8,
		[]Vortex{{3.5, 3.5, 1.0}, {6.5, 6.5, -1.0}}, 0.25, 1.0, "open", 0.0).With(96, "monumental")), 64)
	storeEigs("ham_L8_open_a025_2vort", e2)
	e3 := jacobiEigvals(buildAbCloudHamiltonian(NewConfig(10, 10, nil, 0.2, 1.0, "torus", 0.0).With(96, "monumental")), 100)
	storeEigs("ham_L10_torus_a02_clean", e3)

	ey1 := jacobiEigvals(buildAbCloudHamiltonian(NewConfig(8, 8,
		[]Vortex{{3.5, 3.5, 1.0}, {6.5, 6.5, -1.0}}, 0.3, 1.0, "open", 0.0).With(96, "dirac")), 64)
	ey2 := jacobiEigvals(buildAbCloudHamiltonian(NewConfig(8, 8,
		[]Vortex{{3.5, 3.5, 2.0}, {6.5, 6.5, 0.0}}, 0.3, 1.0, "open", 0.0).With(96, "dirac")), 64)
	dMax := 0.0
	for i := range ey1 {
		dMax = math.Max(dMax, math.Abs(ey1[i]-ey2[i]))
	}
	put("byers_yang", "L8_max_diff", dMax)

	ea := jacobiEigvals(buildAbCloudHamiltonian(NewConfig(12, 12, nil, 0.5, 1.0, "open", 0.0)), 144)
	eb := jacobiEigvals(buildAbCloudHamiltonian(NewConfig(12, 12, nil, 2.0, 1.0, "open", 0.0)), 144)
	na, nb := 0.0, 0.0
	for i := range ea {
		na += ea[i] * ea[i]
		nb += (ea[i] - eb[i]) * (ea[i] - eb[i])
	}
	put("connes", "L12_a05_defect_W0", math.Sqrt(nb)/math.Max(math.Sqrt(na), 1e-30))

	Hch := buildAbCloudHamiltonian(NewConfig(12, 12, nil, 0.5, 1.0, "open", 0.0).With(96, "monumental"))
	put("chiral", "L12_a05_defect", chiralSymmetryDefect(Hch, 12, 12))

	Hf := buildAbCloudHamiltonian(NewConfig(8, 8, []Vortex{{3.5, 3.5, 1.0}}, 0.25, 1.0, "open", 0.0).With(96, "dirac"))
	maxdev := 0.0
	for iy := 1; iy <= 7; iy++ {
		for ix := 1; ix <= 7; ix++ {
			flux := plaquetteFlux(Hf, 8, 8, ix, iy, false)
			tgt := 2*PI*0.25 + 0.0
			if ix == 3 && iy == 3 {
				tgt += 2 * PI
			}
			maxdev = math.Max(maxdev, fluxCircdist(flux, tgt))
		}
	}
	put("dirac_flux", "L8_max_dev", maxdev)

	u := hpUnfoldLocal(zeta[:2000], 0.05)
	put("unfold", "u2", u[1])
	put("unfold", "u1000", u[999])
	put("unfold", "u2000", u[1999])

	xs := make([]float64, 20)
	ys := make([]float64, 20)
	for i := 0; i < 20; i++ {
		xs[i] = float64(i + 1)
		ys[i] = 2.0 + 0.5*xs[i] + 0.1*math.Sin(xs[i])
	}
	lr := linreg(xs, ys)
	put("linreg", "a", lr.A)
	put("linreg", "b", lr.B)
	put("linreg", "R2", lr.R2)

	// AICc n=40 rss=10 k=3
	denom := 40 - 3 - 1
	aic := 40.0*math.Log(math.Max(10.0, 1e-300)/40.0) + 6.0
	if denom > 0 {
		aic += 6.0 * 4.0 / float64(denom)
	}
	put("aicc", "n40_rss10_k3", aic)

	pWald := 7.0 / 20.0
	hWald := 1.96 * math.Sqrt(pWald*(1-pWald)/20.0)
	put("wald", "p", pWald)
	put("wald", "lo", math.Min(math.Max(pWald-hWald, 0), 1))
	put("wald", "hi", math.Min(math.Max(pWald+hWald, 0), 1))

	rankdata := func(v []float64) []float64 {
		ord := make([]int, len(v))
		for i := range ord {
			ord[i] = i
		}
		sort.Slice(ord, func(a, b int) bool { return v[ord[a]] < v[ord[b]] })
		ranks := make([]float64, len(v))
		i := 0
		for i < len(ord) {
			j := i
			for j+1 < len(ord) && v[ord[j+1]] == v[ord[i]] {
				j++
			}
			avg := (float64(i) + float64(j)) / 2.0 + 1.0
			for kk := i; kk <= j; kk++ {
				ranks[ord[kk]] = avg
			}
			i = j + 1
		}
		return ranks
	}
	xr := []float64{1, 2, 3, 4, 5, 6, 7, 8}
	yr := []float64{1.1, 2.3, 2.9, 4.2, 5.1, 5.8, 7.2, 7.9}
	rx, ry := rankdata(xr), rankdata(yr)
	mxr, myr := 0.0, 0.0
	for i := range rx {
		mxr += rx[i]
		myr += ry[i]
	}
	mxr /= float64(len(rx))
	myr /= float64(len(ry))
	sxy, sxx, syy := 0.0, 0.0, 0.0
	for i := range rx {
		sxy += (rx[i] - mxr) * (ry[i] - myr)
		sxx += (rx[i] - mxr) * (rx[i] - mxr)
		syy += (ry[i] - myr) * (ry[i] - myr)
	}
	put("spearman", "xy", sxy/math.Sqrt(sxx*syy))

	sp2 := normalizedSpacings(zeta)
	put("test11", "A2_full", andersonDarlingStat(rmt, sp2))
	return sec
}

func runSelftest(zeta []float64, goldenPath string) bool {
	data, err := os.ReadFile(goldenPath)
	if err != nil {
		fmt.Fprintf(os.Stderr, "ERROR: golden file not found: %s\n", goldenPath)
		os.Exit(2)
	}
	var golden map[string]interface{}
	if err := json.Unmarshal(data, &golden); err != nil {
		fmt.Fprintf(os.Stderr, "ERROR: golden JSON parse: %v\n", err)
		os.Exit(2)
	}
	results := computeAll(zeta, golden)
	tol := map[string][2]float64{
		"lambert_w": {1e-9, 0}, "gram_point": {1e-9, 0}, "bN": {1e-9, 0},
		"spacings": {1e-9, 0}, "gue2_cdf": {1e-7, 0}, "goe_cdf": {1e-9, 0},
		"gue2_pdf": {1e-9, 0}, "gamma_p": {1e-7, 0}, "chi2_cdf": {1e-7, 0},
		"ks_pvalue": {1e-9, 0}, "ks_zeros": {1e-6, 0}, "cvm_zeros": {1e-6, 0},
		"ad_zeros": {1e-6, 0}, "chi2_zeros": {1e-6, 0}, "rmean_zeros": {1e-9, 0},
		"S2": {1e-7, 1e-12}, "D3": {1e-7, 1e-12}, "K_zeros": {1e-6, 0},
		"h1_zeta": {1e-6, 0}, "ham_L8_open_a05_clean": {1e-7, 1e-8},
		"ham_L8_open_a025_2vort": {1e-7, 1e-8}, "ham_L10_torus_a02_clean": {1e-7, 1e-8},
		"byers_yang": {1e-6, 1e-10}, "connes": {1e-5, 1e-8}, "chiral": {1e-5, 1e-9},
		"dirac_flux": {1e-6, 1e-10}, "unfold": {1e-8, 0}, "linreg": {1e-8, 0},
		"aicc": {1e-8, 0}, "wald": {1e-9, 0}, "spearman": {1e-8, 0}, "test11": {1e-6, 0},
	}
	fmt.Println("==============================================================================")
	fmt.Println("ABCLOUD GO PORT — GOLDEN SELFTEST")
	fmt.Println("==============================================================================")
	nOK, nAll := 0, 0
	sections := make([]string, 0, len(results))
	for name := range golden {
		if name == "meta" || name == "grids" {
			continue
		}
		sections = append(sections, name)
	}
	sort.Strings(sections)
	for _, section := range sections {
		gsec, ok := golden[section].(map[string]interface{})
		if !ok {
			continue
		}
		tl, has := tol[section]
		if !has {
			tl = [2]float64{1e-6, 0}
		}
		keys := make([]string, 0, len(gsec))
		for k := range gsec {
			keys = append(keys, k)
		}
		sort.Strings(keys)
		for _, key := range keys {
			nAll++
			gv, isNum := gsec[key].(float64)
			cv, hasCV := results[section][key]
			if !isNum || !hasCV {
				fmt.Printf(" [FAIL] %-28s %-18s missing\n", section, key)
				continue
			}
			var e float64
			var ok bool
			if gv == 0.0 && cv == 0.0 {
				e, ok = 0.0, true
			} else if gv == 0.0 {
				e = math.Abs(cv)
				ok = e <= tl[1]+tl[0]
			} else {
				e = math.Abs(cv-gv) / math.Abs(gv)
				ok = e <= tl[0] || math.Abs(cv-gv) <= tl[1]
			}
			if ok {
				nOK++
			}
			fmt.Printf(" [%s] %-28s %-18s g=%-22.17g p=%-22.17g rel=%.2e\n",
				map[bool]string{true: "PASS", false: "FAIL"}[ok], section, key, gv, cv, e)
		}
	}
	fmt.Println("------------------------------------------------------------------------------")
	fmt.Printf(" RESULT: %d/%d checks passed\n", nOK, nAll)
	fmt.Println("==============================================================================")
	if nOK == nAll {
		fmt.Println("SELFTEST: PASS — Go kernel matches the Julia golden references.")
	} else {
		fmt.Println("SELFTEST: FAIL")
	}
	return nOK == nAll
}

// [PART5]
// ─────────────────────────────────────────────────────────────────────────────
// Suite (portable subset — same 25 tests) + CLI main
// ─────────────────────────────────────────────────────────────────────────────
func runSuite(zeta []float64) {
	fmt.Println("==============================================================================")
	fmt.Println("ABCLOUD SUITE (portable subset, Go)")
	fmt.Println("==============================================================================")
	rmt := &RmtTable{}
	sp := normalizedSpacings(zeta)
	ladder := []int64{100, 500, 1000, 5000, 10000, 50000}
	nPass, nFail, nWarn, nInfo := 0, 0, 0, 0

	verdict := func(v string, tid int, title string, lines []string) {
		mark := "[INFO]"
		switch v {
		case "PASS":
			mark = "[PASS]"
			nPass++
		case "FAIL":
			mark = "[FAIL]"
			nFail++
		case "WARN":
			mark = "[WARN]"
			nWarn++
		default:
			nInfo++
		}
		fmt.Printf("%s TEST %2d — %s\n", mark, tid, title)
		for _, l := range lines {
			fmt.Println(l)
		}
	}

	// 1,2,3
	vals := make([]float64, len(ladder))
	for i, n := range ladder {
		vals[i] = computeBN(zeta, n, 0)
	}
	{
		ok := vals[len(vals)-1] < vals[0]
		lad := make([]string, len(vals))
		for i, v := range vals {
			lad[i] = fmt.Sprintf("%.4f", v)
		}
		verdict(map[bool]string{true: "PASS", false: "FAIL"}[ok], 1, "b(N) convergence table",
			[]string{"  ladder: " + strings.Join(lad, "  "),
				fmt.Sprintf("  b(50000) = %.6f (audit anchor 1.2126)", vals[len(vals)-1])})
	}
	{
		mono := true
		for i := 0; i+1 < len(vals); i++ {
			if vals[i+1] > vals[i]+1e-9 {
				mono = false
			}
		}
		lad := make([]string, len(vals))
		for i, v := range vals {
			lad[i] = fmt.Sprintf("%.4f", v)
		}
		verdict(map[bool]string{true: "PASS", false: "FAIL"}[mono], 2, "b(N) monotonicity",
			[]string{"  ladder: " + strings.Join(lad, " ")})
	}
	{
		lx := make([]float64, len(ladder))
		ly := make([]float64, len(vals))
		for i, n := range ladder {
			lx[i] = math.Log(float64(n))
			ly[i] = math.Log(vals[i])
		}
		r := linreg(lx, ly)
		ok := r.B > -1.5 && r.B < -0.05 && r.R2 > 0.9
		verdict(map[bool]string{true: "PASS", false: "FAIL"}[ok], 3,
			"b(N) convergence rate (power law)",
			[]string{fmt.Sprintf("  slope=%+.4f  R2=%.6f  (asymptotic -0.5, 1/log T correction)", r.B, r.R2)})
	}
	// 4,5
	{
		D, p := ksTest(rmt, sp)
		verdict(map[bool]string{true: "PASS", false: "FAIL"}[D < 0.10], 4, "GUE KS test (full range)",
			[]string{fmt.Sprintf("  KS D=%.6f  p=%.3e  n=%d  (effect-size gate D<0.10)", D, p, len(sp))})
	}
	{
		sp2 := normalizedSpacings(zeta[len(zeta)/2:])
		D, p := ksTest(rmt, sp2)
		verdict(map[bool]string{true: "PASS", false: "FAIL"}[D < 0.10], 5, "GUE KS test (high-T half)",
			[]string{fmt.Sprintf("  high-T half: D=%.6f  p=%.3e  n=%d", D, p, len(sp2))})
	}
	// 6
	{
		chi2v, dfv, pchi := chi2GueTest(rmt, sp, 30)
		verdict("INFO", 6, "spacing chi2 histogram",
			[]string{fmt.Sprintf("  chi2=%.2f  df=%d  p=%.3e  (low p = finite-data GUE miss)", chi2v, dfv, pchi)})
	}
	// 7
	{
		tail := []int64{5000, 10000, 50000}
		lx := make([]float64, len(tail))
		ly := make([]float64, len(tail))
		for i, n := range tail {
			lx[i] = math.Log(float64(n))
			ly[i] = math.Log(computeBN(zeta, n, 0))
		}
		r := linreg(lx, ly)
		ok := r.B > -0.9 && r.B < -0.05 && r.R2 > 0.9
		verdict(map[bool]string{true: "PASS", false: "FAIL"}[ok], 7, "decay slope (large-T)",
			[]string{fmt.Sprintf("  tail slope=%+.4f  R2=%.6f", r.B, r.R2)})
	}
	// 8
	{
		lx := make([]float64, len(ladder))
		ly := make([]float64, len(vals))
		for i, n := range ladder {
			lx[i] = math.Log(float64(n))
			ly[i] = math.Log(vals[i])
		}
		r := linreg(lx, ly)
		maxRel := 0.0
		for i, e := range r.Res {
			maxRel = math.Max(maxRel, math.Abs(e)/math.Max(math.Abs(ly[i]), 1e-12))
		}
		verdict(map[bool]string{true: "PASS", false: "WARN"}[maxRel < 0.2], 8,
			"residual analysis of fit",
			[]string{fmt.Sprintf("  max |relative residual| = %.4f", maxRel)})
	}
	// 9
	{
		rng := NewMT19937(777)
		lo, hi := math.Inf(1), math.Inf(-1)
		for b := 0; b < 200; b++ {
			lx := make([]float64, len(ladder))
			ly := make([]float64, len(ladder))
			for i, n := range ladder {
				lx[i] = math.Log(float64(n))
				noise := (rng.Random() - 0.5) * 2
				ly[i] = math.Log(vals[i] * math.Sqrt(1.0+0.02*noise))
			}
			r := linreg(lx, ly)
			lo = math.Min(lo, r.B)
			hi = math.Max(hi, r.B)
		}
		ok := lo > -1.5 && hi < -0.1
		verdict(map[bool]string{true: "PASS", false: "WARN"}[ok], 9, "bootstrap CI for slope",
			[]string{fmt.Sprintf("  bootstrap slope CI [%+.4f, %+.4f] (200 resamples, seed 777)", lo, hi)})
	}
	// 10
	{
		half := len(zeta) / 2
		lad := []int64{100, 500, 1000, 5000}
		v1 := make([]float64, len(lad))
		v2 := make([]float64, len(lad))
		for i, n := range lad {
			v1[i] = computeBN(zeta, n, 0)
			v2[i] = computeBN(zeta[half:], n, int64(half))
		}
		lx := make([]float64, len(lad))
		for i, n := range lad {
			lx[i] = math.Log(float64(n))
		}
		r1 := linreg(lx, lyLog(v1))
		r2 := linreg(lx, lyLog(v2))
		mono := true
		for i := 0; i+1 < len(v1); i++ {
			if v1[i+1] > v1[i]+1e-9 || v2[i+1] > v2[i]+1e-9 {
				mono = false
			}
		}
		ok := mono && r1.R2 > 0.85 && r2.R2 > 0.85
		verdict(map[bool]string{true: "PASS", false: "FAIL"}[ok], 10, "cross-validation stability",
			[]string{fmt.Sprintf("  slopes %+.3f/%+.3f, R2 %.3f/%.3f; both monotone (height gap = 1/log T offset)",
				r1.B, r2.B, r1.R2, r2.R2)})
	}
	// 11
	{
		A2 := andersonDarlingStat(rmt, sp)
		rng := NewMT19937(777)
		buf := make([]float64, len(sp))
		count := 0
		for it := 0; it < 200; it++ {
			rmt.Sample(rng, buf)
			if andersonDarlingStat(rmt, buf) >= A2 {
				count++
			}
		}
		verdict("INFO", 11, "Anderson-Darling (honest)",
			[]string{fmt.Sprintf("  A2 = %.4f  law-exact MC p = %.4f (200 draws, seed 777)", A2, float64(count+1)/201.0)})
	}
	// 12
	{
		nMat := 200
		rng := NewMT19937(4242)
		gauss := func() float64 {
			u1 := math.Max(rng.Random(), 1e-300)
			return math.Sqrt(-2.0*math.Log(u1)) * math.Cos(2*PI*rng.Random())
		}
		H := make([]complex128, nMat*nMat)
		for r := 0; r < nMat; r++ {
			H[r*nMat+r] = complex(gauss(), 0)
			for c := r + 1; c < nMat; c++ {
				v := complex(gauss()/math.Sqrt2, gauss()/math.Sqrt2)
				H[r*nMat+c] = v
				H[c*nMat+r] = cmplx.Conj(v)
			}
		}
		for r := 0; r < nMat; r++ {
			for c := r; c < nMat; c++ {
				m := H[r*nMat+c] * 0.5
				H[r*nMat+c] = m
				H[c*nMat+r] = cmplx.Conj(m)
			}
		}
		ev := jacobiEigvals(H, nMat)
		band := ev[nMat/10 : 9*nMat/10]
		gp := unitSpacings(band)
		D := ks2(sp, gp)
		verdict(map[bool]string{true: "PASS", false: "FAIL"}[D < 0.10], 12,
			"two-sample KS vs GUE matrix",
			[]string{fmt.Sprintf("  two-sample KS (zeta n=%d vs GUE n=%d): D=%.6f", len(sp), len(gp), D)})
	}
	// 13,14
	{
		pos := unfoldedPositions(zeta)
		rng := NewMT19937(777)
		ok := true
		lines := []string{}
		for _, L := range []float64{5.0, 10.0, 20.0, 50.0} {
			s2 := numberVariance(pos, L, 3000, rng)
			ok = ok && s2 < L
			lines = append(lines, fmt.Sprintf("  S2(L=%5.1f) = %.4f   [Poisson %.1f]", L, s2, L))
		}
		lines = append(lines, "  gate: S2(L) << L (GUE rigidity)")
		verdict(map[bool]string{true: "PASS", false: "FAIL"}[ok], 13, "number variance S2(L)", lines)
	}
	{
		pos := unfoldedPositions(zeta)
		rng := NewMT19937(777)
		ok := true
		lines := []string{}
		for _, L := range []float64{5.0, 10.0, 20.0, 50.0} {
			d3 := delta3Rigidity(pos, L, 300, 300, rng)
			ok = ok && d3 < L/15.0
			lines = append(lines, fmt.Sprintf("  D3(L=%5.1f) = %.4f   [Poisson %.4f]", L, d3, L/15.0))
		}
		verdict(map[bool]string{true: "PASS", false: "FAIL"}[ok], 14, "spectral rigidity D3(L)", lines)
	}
	// 15,16
	{
		H := buildAbCloudHamiltonian(NewConfig(16, 16, []Vortex{{4.5, 4.5, 1.0}}, 0.5, 1.0, "open", 0.0))
		herm := verifyHermitian(H, 256)
		tau := timeReversalAsymmetry(H)
		ev := jacobiEigvals(H, 256)
		band := centralBandEigs(ev, 0.6)
		r, nR := meanAdjacentSpacingRatio(band)
		ok := herm && tau > 1e-12
		verdict(map[bool]string{true: "PASS", false: "FAIL"}[ok], 15, "AB-cloud construction",
			[]string{fmt.Sprintf("  hermitian=%v  tau_TRB=%.3e  <r>(central 60%%)=%.4f (n_r=%d)", herm, tau, r, nR)})
	}
	{
		H := buildAbCloudHamiltonian(NewConfig(24, 24,
			[]Vortex{{6.5, 6.5, 1.0}, {17.5, 17.5, -1.0}}, 0.5, 1.0, "open", 0.0))
		ev := jacobiEigvals(H, 576)
		band := centralBandEigs(ev, 0.6)
		r, nR := meanAdjacentSpacingRatio(band)
		ok := math.Abs(r-0.5992) < 0.06
		verdict(map[bool]string{true: "PASS", false: "WARN"}[ok], 16, "AB-cloud GUE classification",
			[]string{fmt.Sprintf("  <r> = %.4f vs GUE 0.5992 +/- 0.06 (n_r=%d; L=24 finite-size band)", r, nR)})
	}
	// 17,18
	{
		ea := jacobiEigvals(buildAbCloudHamiltonian(NewConfig(12, 12, nil, 0.5, 1.0, "open", 0.0)), 144)
		eb := jacobiEigvals(buildAbCloudHamiltonian(NewConfig(12, 12, nil, 2.0, 1.0, "open", 0.0)), 144)
		na, nb := 0.0, 0.0
		for i := range ea {
			na += ea[i] * ea[i]
			nb += (ea[i] - eb[i]) * (ea[i] - eb[i])
		}
		verdict("INFO", 17, "Connes self-duality",
			[]string{fmt.Sprintf("  alpha<->1/alpha relative L2 defect (open 12x12, W=0) = %.6f", math.Sqrt(nb)/math.Sqrt(na)),
				"  finite open lattice: duality is boundary-spoiled (documented)"})
	}
	{
		H := buildAbCloudHamiltonian(NewConfig(12, 12, nil, 0.5, 1.0, "open", 0.0).With(96, "monumental"))
		Hw := buildAbCloudHamiltonian(NewConfig(12, 12, nil, 0.5, 1.0, "open", 4.0).With(96, "monumental"))
		d0 := chiralSymmetryDefect(H, 12, 12)
		dw := chiralSymmetryDefect(Hw, 12, 12)
		verdict(map[bool]string{true: "PASS", false: "FAIL"}[d0 < 1e-10], 18, "chiral AIII at alpha=1/2",
			[]string{fmt.Sprintf("  defect(W=0) = %.3e (gate <1e-10)   defect(W=4, breaker) = %.4f", d0, dw)})
	}
	// 24,25,26
	{
		H := buildAbCloudHamiltonian(NewConfig(8, 8, []Vortex{{3.5, 3.5, 1.0}}, 0.25, 1.0, "open", 0.0).With(96, "dirac"))
		maxdev := 0.0
		for iy := 1; iy <= 7; iy++ {
			for ix := 1; ix <= 7; ix++ {
				flux := plaquetteFlux(H, 8, 8, ix, iy, false)
				tgt := 2*PI*0.25 + 0.0
				if ix == 3 && iy == 3 {
					tgt += 2 * PI
				}
				maxdev = math.Max(maxdev, fluxCircdist(flux, tgt))
			}
		}
		verdict(map[bool]string{true: "PASS", false: "FAIL"}[maxdev < 1e-9], 24, "Dirac-string flux",
			[]string{fmt.Sprintf("  max circular deviation from 2pa + 2q = %.3e (:dirac)", maxdev)})
	}
	{
		e1 := jacobiEigvals(buildAbCloudHamiltonian(NewConfig(16, 16,
			[]Vortex{{4.5, 4.5, 1.0}, {11.5, 11.5, -1.0}}, 0.3, 1.0, "open", 0.0).With(96, "dirac")), 256)
		e2 := jacobiEigvals(buildAbCloudHamiltonian(NewConfig(16, 16,
			[]Vortex{{4.5, 4.5, 2.0}, {11.5, 11.5, 0.0}}, 0.3, 1.0, "open", 0.0).With(96, "dirac")), 256)
		e3 := jacobiEigvals(buildAbCloudHamiltonian(NewConfig(16, 16,
			[]Vortex{{4.5, 4.5, 0.3}, {11.5, 11.5, -0.3}}, 0.3, 1.0, "open", 0.0).With(96, "dirac")), 256)
		dInt, dFrac := 0.0, 0.0
		for i := range e1 {
			dInt = math.Max(dInt, math.Abs(e1[i]-e2[i]))
			dFrac = math.Max(dFrac, math.Abs(e1[i]-e3[i]))
		}
		ok := dInt < 1e-9 && dFrac > 1e-4
		verdict(map[bool]string{true: "PASS", false: "FAIL"}[ok], 25, "Byers-Yang theorem",
			[]string{fmt.Sprintf("  integer q->q+1: %.3e   fractional q=0.3 control: %.3e (must differ)", dInt, dFrac)})
	}
	{
		H := buildAbCloudHamiltonian(NewConfig(12, 12, nil, 0.25, 1.0, "torus", 0.0))
		maxdev := 0.0
		for iy := 1; iy <= 12; iy++ {
			for ix := 1; ix <= 12; ix++ {
				maxdev = math.Max(maxdev, fluxCircdist(plaquetteFlux(H, 12, 12, ix, iy, true), 2*PI*0.25))
			}
		}
		verdict(map[bool]string{true: "PASS", false: "FAIL"}[maxdev < 1e-9], 26, "PBC torus flux",
			[]string{fmt.Sprintf("  torus 12x12 alpha=0.25: max flux deviation = %.3e", maxdev)})
	}
	// 34
	{
		H := buildAbCloudHamiltonian(NewConfig(28, 28,
			[]Vortex{{7.5, 7.5, 1.0}, {20.5, 20.5, -1.0}}, 0.5, 1.0, "open", 0.0).With(96, "monumental"))
		ev := jacobiEigvals(H, 784)
		band := centralBandEigs(ev, 0.6)
		absp := unitSpacings(hpUnfoldLocal(band, 0.05))
		zsp := unitSpacings(sp)
		D := ks2(absp, zsp)
		verdict(map[bool]string{true: "PASS", false: "WARN"}[D < 0.10], 34, "DIRECT AB-cloud vs zeta",
			[]string{fmt.Sprintf("  DIRECT AB-cloud (L=28, n=%d) vs zeta: KS D=%.6f", len(absp), D)})
	}
	// 35
	{
		tvals := make([]float64, 30)
		for i := range tvals {
			tvals[i] = 0.1 * float64(i+1)
		}
		K := computeKFormFactor(zeta, tvals)
		acc, cnt := 0.0, 0
		for i, t := range tvals {
			if t >= 0.3 {
				e := hpKgueEnvelope(t)
				acc += (K[i] - e) * (K[i] - e)
				cnt++
			}
		}
		rms := math.Sqrt(acc / float64(cnt))
		verdict(map[bool]string{true: "PASS", false: "FAIL"}[rms < 1.0], 35, "form factor K(t)",
			[]string{fmt.Sprintf("  RMS(K - K_box) over t>=0.3 = %.4f  (gate <1.0)", rms)})
	}
	// 36
	{
		H := buildAbCloudHamiltonian(NewConfig(16, 16, []Vortex{{4.5, 4.5, 1.0}}, 0.5, 1.0, "open", 0.0))
		ev := jacobiEigvals(H, 256)
		band := centralBandEigs(ev, 0.6)
		r0, _ := meanAdjacentSpacingRatio(band)
		lo, span := band[0], band[len(band)-1]-band[0]
		nlev := 4096
		quant := make([]float64, len(band))
		for i, e := range band {
			quant[i] = lo + math.Round((e-lo)/span*float64(nlev-1))/float64(nlev-1)*span
		}
		rq, _ := meanAdjacentSpacingRatio(quant)
		dr := math.Abs(rq - r0)
		rng := NewMT19937(12345)
		counts := make([]int64, 256)
		nb := 200000
		for i := 0; i < nb; i++ {
			counts[rng.NextU32()&0xFF]++
		}
		exp := float64(nb) / 256.0
		ent, chi2z := 0.0, 0.0
		for _, c := range counts {
			if c > 0 {
				pp := float64(c) / float64(nb)
				ent -= pp * math.Log2(pp)
			}
			chi2z += (float64(c) - exp) * (float64(c) - exp) / exp
		}
		z := (chi2z - 255.0) / math.Sqrt(2.0*255.0)
		ok := dr < 0.02 && math.Abs(ent-8.0) < 0.01 && math.Abs(z) < 3.0
		verdict(map[bool]string{true: "PASS", false: "FAIL"}[ok], 36, "byte-level robustness",
			[]string{fmt.Sprintf("  |d<r>| under %d-level quantization = %.5f (gate 0.02)", nlev, dr),
				fmt.Sprintf("  RNG entropy = %.6f bits/byte, chi2 z = %+.2f (|z|<3)", ent, z)})
	}
	// 37
	{
		e1 := math.Abs(math.Exp(lgammaLanczos(0.5)) - math.Sqrt(PI))
		e2 := math.Abs(math.Exp(lgammaLanczos(1.5)) - math.Sqrt(PI)/2.0)
		n, smax := 2000, 10.0
		h := smax / float64(n)
		integ, m2 := 0.0, 0.0
		for i := 0; i <= n; i++ {
			wgt := 2.0
			if i == 0 || i == n {
				wgt = 1.0
			} else if i%2 == 1 {
				wgt = 4.0
			}
			p := gue2SurmisePdf(float64(i) * h)
			integ += wgt * p
			m2 += wgt * p * float64(i) * h * float64(i) * h
		}
		integ *= h / 3.0
		m2 *= h / 3.0
		ok := e1 < 1e-9 && e2 < 1e-9 && math.Abs(integ-1.0) < 1e-4 && math.Abs(m2-3.0*PI/8.0) < 5e-3
		verdict(map[bool]string{true: "PASS", false: "FAIL"}[ok], 37, "(1/2)! via Gamma + GUE normalization",
			[]string{fmt.Sprintf("  G(1/2)-sqrt(pi) = %.2e   G(3/2)-sqrt(pi)/2 = %.2e   int p2 = %.6f   <s2> = %.6f", e1, e2, integ, m2)})
	}

	notPorted := []struct {
		id   int
		note string
	}{
		{19, "four-pass Dirac-cone audit"}, {20, "TKNN Chern number"},
		{21, "spinorial phase"}, {22, "AB phase identity"}, {23, "fractal factor"},
		{27, "binary chiral + zeta-dictionary"}, {28, "f_GUE merit"}, {29, "DOS dip"},
		{30, "v_F scaling ladder"}, {31, "Hatano-Nelson skin"},
		{32, "multi-realization <r> bootstrap (dSFMT parity)"},
		{33, "L-scaling <r> (dSFMT parity)"}, {38, "Curie point three-pass"},
		{39, "Test-34G geometry sweep"},
	}
	fmt.Println("------------------------------------------------------------------------------")
	for _, np := range notPorted {
		fmt.Printf("[SKIP] TEST %2d — not ported: %s\n", np.id, np.note)
	}
	fmt.Println("------------------------------------------------------------------------------")
	fmt.Printf("SUITE RESULT: %d PASS, %d FAIL, %d WARN, %d INFO\n", nPass, nFail, nWarn, nInfo)
	fmt.Println("==============================================================================")
}

func lyLog(v []float64) []float64 {
	out := make([]float64, len(v))
	for i, x := range v {
		out[i] = math.Log(x)
	}
	return out
}

func main() {
	if len(os.Args) < 2 {
		fmt.Fprintln(os.Stderr, "usage: abcloud <selftest|zeros|suite|bN|gram|test11|hp|sweep> [options]")
		os.Exit(2)
	}
	cmd := os.Args[1]
	data, golden := "", ""
	ns := []int64{}
	offset := int64(0)
	mc, seed := 200, 777
	for i := 2; i < len(os.Args); i++ {
		a := os.Args[i]
		switch a {
		case "--data":
			if i+1 < len(os.Args) {
				i++
				data = os.Args[i]
			}
		case "--golden":
			if i+1 < len(os.Args) {
				i++
				golden = os.Args[i]
			}
		case "--N", "--n":
			for i+1 < len(os.Args) && !strings.HasPrefix(os.Args[i+1], "-") {
				i++
				if v, err := strconv.ParseInt(os.Args[i], 10, 64); err == nil {
					ns = append(ns, v)
				}
			}
		case "--offset":
			if i+1 < len(os.Args) {
				i++
				offset, _ = strconv.ParseInt(os.Args[i], 10, 64)
			}
		case "--mc":
			if i+1 < len(os.Args) {
				i++
				mc, _ = strconv.Atoi(os.Args[i])
			}
		case "--seed":
			if i+1 < len(os.Args) {
				i++
				seed, _ = strconv.Atoi(os.Args[i])
			}
		}
	}
	exe, _ := os.Executable()
	exeDir := filepath.Dir(exe)
	// exe at ports/go/ (or build dir) — resolve repo-relative defaults
	zerosPath := data
	goldenPath := golden
	if zerosPath == "" {
		for _, cand := range []string{"../../zeros50k.txt", "../../../zeros50k.txt", "../../../../zeros50k.txt", "zeros50k.txt"} {
			if _, err := os.Stat(filepath.Join(exeDir, cand)); err == nil {
				zerosPath = filepath.Join(exeDir, cand)
				break
			}
		}
	}
	if goldenPath == "" {
		for _, cand := range []string{"../golden/abcloud_golden.json", "../../../golden/abcloud_golden.json", "../../../../golden/abcloud_golden.json", "abcloud_golden.json"} {
			if _, err := os.Stat(filepath.Join(exeDir, cand)); err == nil {
				goldenPath = filepath.Join(exeDir, cand)
				break
			}
		}
	}

	switch cmd {
	case "selftest":
		z := loadZeros(zerosPath)
		if !runSelftest(z, goldenPath) {
			os.Exit(1)
		}
	case "suite":
		z := loadZeros(zerosPath)
		runSuite(z)
	case "bN":
		z := loadZeros(zerosPath)
		if len(ns) == 0 {
			ns = []int64{100, 1000, 10000}
		}
		for _, n := range ns {
			fmt.Printf("b(N=%6d, offset=%d) = %.10f\n", n, offset, computeBN(z, n, offset))
		}
	case "gram":
		if len(ns) == 0 {
			ns = []int64{1, 10, 100}
		}
		for _, n := range ns {
			fmt.Printf("g_%d = %.10f\n", n, gramPoint(n))
		}
	case "test11":
		z := loadZeros(zerosPath)
		sp := normalizedSpacings(z)
		rmt := &RmtTable{}
		A2 := andersonDarlingStat(rmt, sp)
		fmt.Printf("Test 11 (honest): exact A2 on n=%d spacings: %.6f\n", len(sp), A2)
		if mc > 0 {
			rng := NewMT19937(uint32(seed))
			buf := make([]float64, len(sp))
			count := 0
			for it := 0; it < mc; it++ {
				rmt.Sample(rng, buf)
				if andersonDarlingStat(rmt, buf) >= A2 {
					count++
				}
			}
			fmt.Printf("MC null (%d draws): p = %.6f  (%d/%d >= A2)\n", mc,
				float64(count+1)/float64(mc+1), count, mc)
		}
	case "hp":
		z := loadZeros(zerosPath)
		n := len(z)
		om := make([]float64, 726)
		for k := range om {
			om[k] = 0.3 + 0.004*float64(k)
		}
		w := make([]float64, n)
		for i := 0; i < n; i++ {
			w[i] = 0.5 * (1.0 - math.Cos(2*PI*float64(i)/float64(n-1)))
		}
		sw2 := 0.0
		for _, wi := range w {
			sw2 += wi * wi
		}
		P := make([]float64, len(om))
		for fi, omv := range om {
			re, im := 0.0, 0.0
			for i := 0; i < n; i++ {
				re += w[i] * math.Cos(omv*z[i])
				im -= w[i] * math.Sin(omv*z[i])
			}
			P[fi] = (re*re + im*im) / sw2
		}
		Ps := append([]float64(nil), P...)
		sort.Float64s(Ps)
		med := 0.5 * (Ps[len(Ps)/2-1] + Ps[len(Ps)/2])
		fmt.Printf("H1 primary detector on %d positions:\n", n)
		hits := 0
		for _, pr := range []int{2, 3, 5, 7, 11, 13} {
			tgt := math.Log(float64(pr))
			best, bd := 0, math.Inf(1)
			for i, o := range om {
				d := math.Abs(o - tgt)
				if d < bd {
					bd, best = d, i
				}
			}
			snr := P[best] / med
			if snr >= 10.0 {
				hits++
			}
			mark := "-"
			if snr >= 10.0 {
				mark = "PEAK"
			}
			fmt.Printf("  SNR(log %2d) = %.6e  [%s]\n", pr, snr, mark)
		}
		fmt.Printf("  verdict: %d/6 prime harmonics above SNR 10\n", hits)
	case "sweep":
		z := loadZeros(zerosPath)
		if len(ns) == 0 {
			ns = []int64{100, 500, 1000, 5000, 10000, 50000}
		}
		fmt.Println("  N        b(N)")
		for _, n := range ns {
			fmt.Printf("%6d  %.8f\n", n, computeBN(z, n, 0))
		}
	case "zeros":
		z := loadZeros(zerosPath)
		sp := normalizedSpacings(z)
		rmt := &RmtTable{}
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
		D, p := ksTest(rmt, sp)
		fmt.Printf("zeros: n=%d  g1=%.6f  gN=%.6f\n", len(z), z[0], z[len(z)-1])
		fmt.Printf("spacings: n=%d  mean=%.6f  var=%.6f\n", len(sp), mean, variance)
		fmt.Printf("KS  : D=%.6f  p=%.6e\n", D, p)
		fmt.Printf("CvM : W2=%.6f\n", cvmTest(rmt, sp))
		fmt.Printf("A2  : %.6f\n", andersonDarlingStat(rmt, sp))
		chi2v, dfv, pchi := chi2GueTest(rmt, sp, 30)
		fmt.Printf("chi2: %.4f  df=%d  p=%.6e\n", chi2v, dfv, pchi)
		r, nR := meanAdjacentSpacingRatio(z)
		fmt.Printf("<r> : %.6f  (n_r=%d)\n", r, nR)
		pos := unfoldedPositions(z)
		rng := NewMT19937(777)
		for _, L := range []float64{5.0, 10.0, 20.0, 50.0, 100.0} {
			fmt.Printf("S2(L=%6.1f) = %.6f\n", L, numberVariance(pos, L, 3000, rng))
		}
		for _, L := range []float64{5.0, 10.0, 20.0, 50.0} {
			fmt.Printf("D3(L=%6.1f) = %.6f\n", L, delta3Rigidity(pos, L, 300, 300, rng))
		}
	default:
		fmt.Fprintf(os.Stderr, "unknown command: %s\n", cmd)
		os.Exit(2)
	}
}
