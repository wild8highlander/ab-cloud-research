package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"path/filepath"
	"sort"
	"strconv"
	"strings"
)

// ---------------------------------------------------------------------------
// Data sources (CANON_SPEC §9)
// ---------------------------------------------------------------------------

type ZeroSource struct {
	Name     string
	Filename string
	MaxZeros int
}

var zeroSources = []ZeroSource{
	{"50k", "zeta_zeros_50000.txt", 13661},
	{"50k_full", "zeta_zeros_50000_embedded.txt", 50000},
	{"500k", "zeta_zeros_500k_odlyzko.txt", 500000},
	{"2M", "zeta_zeros_2M_odlyzko.txt", 2001052},
	{"highT", "zeta_zeros_highT_blocks.txt", 30000},
	{"csv", "zeta_zeros_50000.csv", 13661},
	{"zeros6", "zeros6.txt", 2001052},
}

// autoSelectSource picks the smallest source that can hold `count` zeros.
func autoSelectSource(count int) (ZeroSource, error) {
	best := -1
	var out ZeroSource
	for _, s := range zeroSources {
		if s.MaxZeros >= count && (best < 0 || s.MaxZeros < best) {
			best = s.MaxZeros
			out = s
		}
	}
	if best < 0 {
		return out, fmt.Errorf("no data source available for %d zeros", count)
	}
	return out, nil
}

func findSource(name string) (ZeroSource, error) {
	for _, s := range zeroSources {
		if s.Name == name {
			return s, nil
		}
	}
	return ZeroSource{}, fmt.Errorf("unknown source: %s", name)
}

// LoadZeros reads zeros from dataDir/source, truncating to count if > 0.
func LoadZeros(dataDir string, count int, source string) ([]float64, error) {
	var src ZeroSource
	var err error
	if source != "" && source != "auto" {
		src, err = findSource(source)
		if err != nil {
			return nil, err
		}
	} else {
		src, err = autoSelectSource(count)
		if err != nil {
			return nil, err
		}
	}

	path := filepath.Join(dataDir, src.Filename)
	zeros, err := parseZeroFile(path, src.Name == "csv", src.Name == "highT")
	if err != nil {
		return nil, fmt.Errorf("loading %s: %w", path, err)
	}
	sort.Float64s(zeros)
	if count > 0 && count < len(zeros) {
		zeros = zeros[:count]
	}
	return zeros, nil
}

// parseZeroFile reads a file of floats, skipping # comments and blanks.
// csv: second field is t; highT: "# BLOCK ... offset=<v>" headers shift values.
func parseZeroFile(path string, isCSV, isHighT bool) ([]float64, error) {
	f, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer f.Close()

	var zeros []float64
	blockOffset := 0.0
	sc := bufio.NewScanner(f)
	sc.Buffer(make([]byte, 1<<20), 1<<20)

	for sc.Scan() {
		line := strings.TrimSpace(sc.Text())
		if line == "" {
			continue
		}
		if strings.HasPrefix(line, "#") {
			if isHighT {
				if i := strings.Index(line, "offset="); i >= 0 {
					if v, e := strconv.ParseFloat(strings.TrimSpace(line[i+7:]), 64); e == nil {
						blockOffset = v
					}
				}
			}
			continue
		}
		var v float64
		if isCSV {
			fields := strings.Split(line, ",")
			if len(fields) < 2 {
				continue
			}
			v, err = strconv.ParseFloat(strings.TrimSpace(fields[1]), 64)
			if err != nil {
				continue
			}
		} else {
			v, err = strconv.ParseFloat(line, 64)
			if err != nil {
				continue
			}
		}
		val := v + blockOffset
		if val > 0 {
			zeros = append(zeros, val)
		}
	}
	return zeros, sc.Err()
}

// ---------------------------------------------------------------------------
// Canonical math kernel (CANON_SPEC §1–§6)
// ---------------------------------------------------------------------------

// LambertW computes the principal branch W0(z) (CANON_SPEC §1).
func LambertW(z float64) float64 {
	if z <= 0 {
		return 0
	}
	w := math.Log(z)
	if w < 0 {
		w = z // W(z) ~ z for 0 < z < 1; avoids the flat point at w = -1
	}
	for i := 0; i < 50; i++ {
		ew := math.Exp(w)
		f := w*ew - z
		fp := ew * (w + 1)
		if math.Abs(fp) < 1e-30 {
			break
		}
		delta := f / fp
		w -= delta
		if math.Abs(delta) < 1e-14*(1+math.Abs(w)) {
			break
		}
	}
	return w
}

// GramPoint returns the solution of theta(t) = pi*n (CANON_SPEC §2):
// seed 2*pi*n/W(n/e), then EXACTLY 8 Newton iterations on the 5-term
// Riemann–Siegel theta asymptotics.
func GramPoint(n int) float64 {
	if n <= 0 {
		return 0
	}
	nf := float64(n)
	t := 2 * math.Pi * nf / LambertW(nf/math.E)
	for i := 0; i < 8; i++ {
		arg := t / (2 * math.Pi)
		if arg <= 0 {
			break
		}
		theta := 0.5*t*math.Log(arg) - 0.5*t - math.Pi/8 +
			1.0/(48.0*t) + 7.0/(5760.0*t*t*t)
		dtheta := 0.5*math.Log(arg) - 1.0/(48.0*t*t) -
			21.0/(5760.0*t*t*t*t)
		if math.Abs(dtheta) < 1e-30 {
			break
		}
		t -= (theta - nf*math.Pi) / dtheta
	}
	return t
}

// gue table (CANON_SPEC §5)
const (
	gueTN   = 32768
	gueSMAX = 5.0
)

var gueTable []float64

func gueExact(s float64) float64 {
	if s <= 0 {
		return 0
	}
	return math.Erf(2*s/math.Sqrt(math.Pi)) - (4*s/math.Pi)*math.Exp(-4*s*s/math.Pi)
}

// GUECDF: Wigner–Dyson beta=2 surmise through the canonical 32768-point table.
// v2.0.3: was 1 - exp(-pi s^2/4), the GOE (beta=1) surmise — wrong ensemble.
func GUECDF(s float64) float64 {
	if s <= 0 {
		return 0
	}
	if s >= gueSMAX {
		return gueExact(s)
	}
	if len(gueTable) == 0 {
		gueTable = make([]float64, gueTN)
		for i := 0; i < gueTN; i++ {
			gueTable[i] = gueExact(float64(i) * gueSMAX / float64(gueTN-1))
		}
	}
	x := s * float64(gueTN-1) / gueSMAX
	i := int(math.Floor(x))
	if i < 0 || i >= gueTN-1 {
		return gueExact(s)
	}
	t := x - float64(i)
	return (1-t)*gueTable[i] + t*gueTable[i+1]
}

// ComputeBN: b(N) = (1/N) sum |zeros[k-1] - GramPoint(k)| (CANON_SPEC §3).
func ComputeBN(zeros []float64, N int) float64 {
	if N <= 0 || N > len(zeros) {
		return math.NaN()
	}
	sum := 0.0
	for k := 1; k <= N; k++ {
		sum += math.Abs(zeros[k-1] - GramPoint(k))
	}
	return sum / float64(N)
}

// ComputeBNOffset: zeros 1..N against Gram points offset+1..offset+N.
func ComputeBNOffset(zeros []float64, N, offset int) float64 {
	if N <= 0 || offset+N > len(zeros) {
		return math.NaN()
	}
	sum := 0.0
	for k := 1; k <= N; k++ {
		sum += math.Abs(zeros[k-1] - GramPoint(offset+k))
	}
	return sum / float64(N)
}

// ComputeSpacings: s_k = (z_{k+1}-z_k) * log(z_k/2pi)/(2pi) (CANON_SPEC §4).
func ComputeSpacings(zeros []float64) []float64 {
	var sp []float64
	for k := 0; k+1 < len(zeros); k++ {
		if zeros[k] <= 0 {
			continue
		}
		sp = append(sp, (zeros[k+1]-zeros[k])*math.Log(zeros[k]/(2*math.Pi))/(2*math.Pi))
	}
	return sp
}

// KSAsymptoticPValue: two-branch Kolmogorov p-value (CANON_SPEC §6).
func KSAsymptoticPValue(lam float64) float64 {
	if lam <= 0 {
		return 1
	}
	var v float64
	if lam < 0.6 {
		s2 := 0.0
		for k := 1; k <= 1000; k++ {
			term2 := math.Exp(-((2.0*float64(k) - 1.0) * (2.0*float64(k) - 1.0) * math.Pi * math.Pi) / (8.0 * lam * lam))
			s2 += term2
			if term2 < 1e-18 {
				break
			}
		}
		v = 1 - math.Sqrt(2*math.Pi)/lam*s2
	} else {
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
		v = 2 * s
	}
	if v < 0 {
		return 0
	}
	if v > 1 {
		return 1
	}
	return v
}

// KSTestDP: two-sided D + lambda-corrected p (CANON_SPEC §6).
func KSTestDP(spacings []float64) (D, p float64) {
	s := append([]float64(nil), spacings...)
	sort.Float64s(s)
	n := float64(len(s))
	D = 0
	for i := 1; i <= len(s); i++ {
		F := GUECDF(s[i-1])
		D = math.Max(D, math.Max(math.Abs(float64(i)/n-F), math.Abs(float64(i-1)/n-F)))
	}
	lam := (math.Sqrt(n) + 0.12 + 0.11/math.Sqrt(n)) * D
	return D, KSAsymptoticPValue(lam)
}

// CvmTest: Cramér–von Mises W² (CANON_SPEC §6).
func CvmTest(spacings []float64) float64 {
	s := append([]float64(nil), spacings...)
	sort.Float64s(s)
	n := float64(len(s))
	if len(s) == 0 {
		return 0
	}
	W2 := 0.0
	for i := 1; i <= len(s); i++ {
		u := GUECDF(s[i-1])
		d := u - (2.0*float64(i) - 1.0) / (2.0 * n)
		W2 += d * d
	}
	return W2 + 1.0/(12.0*n)
}

// AdStat: Anderson–Darling A² with tail clamps (CANON_SPEC §6).
func AdStat(spacings []float64) float64 {
	s := append([]float64(nil), spacings...)
	sort.Float64s(s)
	n := float64(len(s))
	if len(s) < 2 {
		return math.NaN()
	}
	acc := 0.0
	for i := 1; i <= len(s); i++ {
		Fi := GUECDF(s[i-1])
		Fni := GUECDF(s[len(s)-i])
		Fi = math.Min(math.Max(Fi, 1e-300), 1.0-1e-16)
		Fni = math.Min(math.Max(Fni, 1e-300), 1.0-1e-16)
		acc += (2.0*float64(i) - 1.0) * (math.Log(Fi) + math.Log(1.0-Fni))
	}
	return -n - acc/n
}

// MeanRatio: <r> over adjacent gaps (CANON_SPEC §6).
func MeanRatio(zeros []float64) (r float64, n int) {
	if len(zeros) < 3 {
		return math.NaN(), 0
	}
	acc := 0.0
	cnt := 0
	for i := 0; i+2 < len(zeros); i++ {
		a := zeros[i+1] - zeros[i]
		b := zeros[i+2] - zeros[i+1]
		m := math.Max(a, b)
		if a == 0 && b == 0 {
			continue
		}
		acc += math.Min(a, b) / m
		cnt++
	}
	if cnt == 0 {
		return math.NaN(), 0
	}
	return acc / float64(cnt), cnt
}

// Linreg: OLS with slope stderr and R² (CANON_SPEC §7).
type Linreg struct {
	Slope, Intercept, SE, R2 float64
	M                        int
}

func LinregFit(x, y []float64) Linreg {
	n := float64(len(x))
	var sx, sy, sxx, sxy, syy float64
	for i := range x {
		sx += x[i]
		sy += y[i]
		sxx += x[i] * x[i]
		sxy += x[i] * y[i]
		syy += y[i] * y[i]
	}
	den := n*sxx - sx*sx
	if math.Abs(den) < 1e-30 {
		return Linreg{M: len(x)}
	}
	slope := (n*sxy - sx*sy) / den
	intercept := (sy - slope*sx) / n
	ssTot := syy - sy*sy/n
	ssRes := 0.0
	for i := range x {
		e := y[i] - (slope*x[i] + intercept)
		ssRes += e * e
	}
	r2 := 0.0
	if ssTot > 0 {
		r2 = 1 - ssRes/ssTot
	}
	se := 0.0
	if len(x) > 2 && den > 0 {
		se = math.Sqrt((ssRes / (n - 2)) * n / den)
	}
	return Linreg{Slope: slope, Intercept: intercept, SE: se, R2: r2, M: len(x)}
}
