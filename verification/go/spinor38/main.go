// spinor38 (Go port) — Test 38: 64 spinor structures of the Klein quartic.
// Self-implemented cyclic Jacobi eigenvalue algorithm; std only.
// Build: go build -o spinor38 .   Run: ./spinor38 [repo-root]
package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"path/filepath"
	"strconv"
	"strings"
)

type clsRow struct {
	cls, orbit, arf int
	signs           []float64
}

func findDataDir(rootArg string) string {
	roots := []string{}
	if rootArg != "" {
		roots = append(roots, rootArg)
	}
	wd, _ := os.Getwd()
	roots = append(roots, wd)
	for _, r := range roots {
		b := r
		for up := 0; up < 6; up++ {
			cand := filepath.Join(b, "verification", "spinor64", "data",
				"spinor_classes.csv")
			if _, err := os.Stat(cand); err == nil {
				return filepath.Join(b, "verification", "spinor64", "data")
			}
			b = filepath.Join(b, "..")
		}
	}
	fmt.Fprintln(os.Stderr, "data dir not found; pass repo root as argument")
	os.Exit(2)
	return ""
}

func jacobiEigen(aIn [][]float64) []float64 {
	n := len(aIn)
	a := make([][]float64, n)
	for i := range aIn {
		a[i] = append([]float64(nil), aIn[i]...)
	}
	for sweep := 0; sweep < 200; sweep++ {
		off := 0.0
		for p := 0; p < n; p++ {
			for q := p + 1; q < n; q++ {
				off += a[p][q] * a[p][q]
			}
		}
		if off < 1e-24 {
			break
		}
		for p := 0; p < n; p++ {
			for q := p + 1; q < n; q++ {
				if math.Abs(a[p][q]) < 1e-15 {
					continue
				}
				tau := (a[q][q] - a[p][p]) / (2 * a[p][q])
				sign := 1.0
				if tau < 0 {
					sign = -1.0
				}
				t := sign / (math.Abs(tau) + math.Sqrt(1+tau*tau))
				c := 1 / math.Sqrt(1+t*t)
				s := t * c
				for k := 0; k < n; k++ {
					akp, akq := a[k][p], a[k][q]
					a[k][p] = c*akp - s*akq
					a[k][q] = s*akp + c*akq
				}
				for k := 0; k < n; k++ {
					apk, aqk := a[p][k], a[q][k]
					a[p][k] = c*apk - s*aqk
					a[q][k] = s*apk + c*aqk
				}
			}
		}
	}
	eig := make([]float64, n)
	for i := 0; i < n; i++ {
		eig[i] = a[i][i]
	}
	sortFloats(eig)
	return eig
}

func sortFloats(v []float64) {
	for i := 1; i < len(v); i++ {
		for j := i; j > 0 && v[j] < v[j-1]; j-- {
			v[j], v[j-1] = v[j-1], v[j]
		}
	}
}

func extractJSONNum(js, key string) float64 {
	pat := "\"" + key + "\":"
	i := strings.Index(js, pat)
	if i < 0 {
		return 0
	}
	rest := js[i+len(pat):]
	end := strings.IndexAny(rest, ",}] \n")
	if end < 0 {
		end = len(rest)
	}
	v, _ := strconv.ParseFloat(strings.Trim(rest[:end], " "), 64)
	return v
}

func main() {
	rootArg := ""
	if len(os.Args) > 1 {
		rootArg = os.Args[1]
	}
	dd := findDataDir(rootArg)

	classes := []clsRow{}
	f, _ := os.Open(filepath.Join(dd, "spinor_classes.csv"))
	sc := bufio.NewScanner(f)
	first := true
	for sc.Scan() {
		line := sc.Text()
		if first {
			first = false
			continue
		}
		if line == "" {
			continue
		}
		parts := strings.SplitN(line, ",", 4)
		var row clsRow
		row.cls, _ = strconv.Atoi(parts[0])
		row.orbit, _ = strconv.Atoi(parts[1])
		row.arf, _ = strconv.Atoi(parts[2])
		for _, tok := range strings.Fields(parts[3]) {
			v, _ := strconv.ParseFloat(tok, 64)
			row.signs = append(row.signs, v)
		}
		classes = append(classes, row)
	}
	f.Close()

	edges := [][2]int{}
	f, _ = os.Open(filepath.Join(dd, "klein_graph_edges.csv"))
	sc = bufio.NewScanner(f)
	first = true
	for sc.Scan() {
		line := sc.Text()
		if first {
			first = false
			continue
		}
		if line == "" {
			continue
		}
		p := strings.Split(line, ",")
		u, _ := strconv.Atoi(p[1])
		v, _ := strconv.Atoi(p[2])
		edges = append(edges, [2]int{u, v})
	}
	f.Close()

	jsB, _ := os.ReadFile(filepath.Join(dd, "reference_stats.json"))
	js := string(jsB)
	rRef := extractJSONNum(js, "r_mean_reference")
	nZeroRef := int(extractJSONNum(js, "n_zero_modes"))
	representative := int(extractJSONNum(js, "representative_class"))

	const N = 56
	nOdd := 0
	for i := range classes {
		if classes[i].orbit == 0 {
			nOdd++
		}
	}

	var spectra [][]float64
	var repSpectrum []float64
	for i := range classes {
		if classes[i].orbit != 0 {
			continue
		}
		a := make([][]float64, N)
		for j := range a {
			a[j] = make([]float64, N)
		}
		for k, e := range edges {
			s := classes[i].signs[k]
			a[e[0]][e[1]] = s
			a[e[1]][e[0]] = s
		}
		w := jacobiEigen(a)
		if classes[i].cls == representative {
			repSpectrum = w
		}
		spectra = append(spectra, w)
	}

	isomax := 0.0
	for a := 0; a < len(spectra); a++ {
		for b := a + 1; b < len(spectra); b++ {
			for i := 0; i < N; i++ {
				d := math.Abs(spectra[a][i] - spectra[b][i])
				if d > isomax {
					isomax = d
				}
			}
		}
	}

	nZero := 0
	lam := make([]float64, 0, N)
	for i := 0; i < N; i++ {
		v := math.Abs(repSpectrum[i])
		if v < 1e-8 {
			nZero++
		}
		lam = append(lam, v)
	}
	sortFloats(lam)
	dsp := []float64{}
	for i := 0; i+1 < len(lam); i++ {
		d := lam[i+1] - lam[i]
		if d > 1e-8 {
			dsp = append(dsp, d)
		}
	}
	rsum := 0.0
	for i := 0; i+1 < len(dsp); i++ {
		mn, mx := dsp[i], dsp[i+1]
		if mn > mx {
			mn, mx = mx, mn
		}
		rsum += mn / mx
	}
	rMean := rsum / float64(len(dsp)-1)

	fmt.Println("Test 38 - 64 spinor structures of the Klein quartic (Go port)")
	fmt.Printf("classes loaded: %d | odd-orbit members: %d\n", len(classes), nOdd)
	verdict := "FAIL"
	if isomax < 1e-9 {
		verdict = "PASS"
	}
	fmt.Printf("isospectrality within the odd orbit: max|dlambda| = %.3e -> %s\n", isomax, verdict)
	fmt.Printf("zero modes (representative): %d (expected %d)\n", nZero, nZeroRef)
	rOk := math.Abs(rMean-rRef) < 1e-6
	rVerdict := "FAIL"
	if rOk {
		rVerdict = "PASS"
	}
	fmt.Printf("<r> (representative): %.10f (reference 0.4515710793) -> %s\n", rMean, rVerdict)
	ok := isomax < 1e-9 && nZero == nZeroRef && rOk
	final := "FAIL"
	if ok {
		final = "PASS"
	}
	fmt.Println("VERDICT: " + final)
	if !ok {
		os.Exit(1)
	}
}
