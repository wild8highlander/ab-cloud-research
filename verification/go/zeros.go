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

// ZeroSource describes an available data file.
type ZeroSource struct {
	Name     string
	Filename string
	MaxZeros int
}

var zeroSources = []ZeroSource{
	{"50000", "zeta_zeros_50000.txt", 13661},
	{"500k", "zeta_zeros_500k_odlyzko.txt", 500000},
	{"2M", "zeta_zeros_2M_odlyzko.txt", 2000000},
	{"highT", "zeta_zeros_highT_blocks.txt", 0},
	{"zeros6", "zeros6.txt", 2000000},
}

// autoSelectSource picks the smallest source that can hold `count` zeros.
func autoSelectSource(count int) ZeroSource {
	for _, s := range zeroSources {
		if s.MaxZeros >= count || s.MaxZeros == 0 {
			return s
		}
	}
	return zeroSources[len(zeroSources)-1]
}

// findSource looks up a source by name.
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
	if source != "" && source != "auto" {
		var err error
		src, err = findSource(source)
		if err != nil {
			return nil, err
		}
	} else {
		src = autoSelectSource(count)
	}

	path := filepath.Join(dataDir, src.Filename)
	zeros, err := parseZeroFile(path)
	if err != nil {
		return nil, fmt.Errorf("loading %s: %w", path, err)
	}

	if count > 0 && count < len(zeros) {
		zeros = zeros[:count]
	}
	return zeros, nil
}

// parseZeroFile reads a file of floats, skipping # comments and blanks.
func parseZeroFile(path string) ([]float64, error) {
	f, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer f.Close()

	var zeros []float64
	sc := bufio.NewScanner(f)
	sc.Buffer(make([]byte, 1<<20), 1<<20)

	for sc.Scan() {
		line := strings.TrimSpace(sc.Text())
		if line == "" || strings.HasPrefix(line, "#") {
			continue
		}
		v, err := strconv.ParseFloat(line, 64)
		if err != nil {
			continue // skip unparseable lines
		}
		if v > 0 {
			zeros = append(zeros, v)
		}
	}
	return zeros, sc.Err()
}

// ---------- Lambert W & Gram-point math ----------

// LambertW computes the principal branch W₀(z) via Halley's iteration.
func LambertW(z float64) float64 {
	if z <= 0 {
		return 0
	}
	w := math.Log(z)
	if w < 0 {
		w = 0.01
	}
	for i := 0; i < 50; i++ {
		ew := math.Exp(w)
		f := w*ew - z
		fp := ew * (w + 1)
		fpp := ew * (w + 2)
		denom := 2*fp*fp - f*fpp
		if math.Abs(denom) < 1e-30 {
			break
		}
		delta := 2 * f * fp / denom
		w -= delta
		if math.Abs(delta) < 1e-15*math.Max(1, math.Abs(w)) {
			break
		}
	}
	return w
}

// rsTheta is the Riemann-Siegel theta function (asymptotic).
func rsTheta(t float64) float64 {
	return 0.5*t*math.Log(t/(2*math.Pi)) - 0.5*t - math.Pi/8
}

// rsThetaPrime is the derivative of theta.
func rsThetaPrime(t float64) float64 {
	return 0.5 * math.Log(t/(2*math.Pi))
}

// GramPoint returns γ̃_n solving θ(γ̃_n) = nπ via Lambert W + Newton.
func GramPoint(n int) float64 {
	if n <= 0 {
		return 17.44 // γ̃₀ ≈ 17.44
	}
	nf := float64(n)
	w := LambertW(nf / math.E)
	t0 := 2 * math.Pi * math.E * math.Exp(w)

	target := nf * math.Pi
	t := t0
	for i := 0; i < 30; i++ {
		f := rsTheta(t) - target
		fp := rsThetaPrime(t)
		if math.Abs(fp) < 1e-30 {
			break
		}
		delta := f / fp
		t -= delta
		if math.Abs(delta) < 1e-12*t {
			break
		}
	}
	return t
}

// GUECDF returns 1 - exp(-πs²/4).
func GUECDF(s float64) float64 {
	return 1 - math.Exp(-math.Pi*s*s/4)
}
