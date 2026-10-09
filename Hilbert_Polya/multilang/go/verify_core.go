// verify_core.go — Go-двойник ядра. Запуск: go run verify_core.go [out]
package main

import (
	"fmt"
	"math"
	"os"
	"strconv"
)

var G = 7.0
var C = [9]float64{0.99999999999980993, 676.5203681218851, -1259.1392167224028,
	771.32342877765313, -176.61502916214059, 12.507343278686905,
	-0.13857109526572012, 9.9843695780195716e-6, 1.5056327351493116e-7}

func modGamma(re, u float64) float64 {
	zr, zi := re-1.0, u
	xr, xi := C[0], 0.0
	for i := 1; i < 9; i++ {
		dr, di := zr+float64(i), zi
		den := dr*dr + di*di
		xr += C[i] * dr / den
		xi -= C[i] * di / den
	}
	tr, ti := zr+G+0.5, zi
	mt := 0.5 * math.Log(tr*tr+ti*ti)
	at := math.Atan2(ti, tr)
	pe := (zr+0.5)*mt - ti*at
	ph := ti*mt + (zr+0.5)*at
	ar, ai := math.Exp(pe)*math.Cos(ph), math.Exp(pe)*math.Sin(ph)
	e := math.Exp(-tr)
	br, bi := e*math.Cos(-ti), e*math.Sin(-ti)
	c1r, c1i := ar*xr-ai*xi, ar*xi+ai*xr
	d1r, d1i := c1r*br-c1i*bi, c1r*bi+c1i*br
	gr, gi := math.Sqrt(2*math.Pi)*d1r, math.Sqrt(2*math.Pi)*d1i
	return math.Sqrt(gr*gr + gi*gi)
}

func main() {
	out := "verify_control.txt"
	if len(os.Args) > 1 {
		out = os.Args[1]
	}
	maxRes := 0.0
	for _, u := range []float64{0.5, 1.0, 2.0, 3.0} {
		ref := math.Sqrt(math.Pi / math.Cosh(math.Pi*u))
		res := math.Abs(modGamma(0.5, u)-ref) / ref
		if res > maxRes {
			maxRes = res
		}
	}
	const N = 100000
	spf := make([]int, N+1)
	sum := 0.0
	for i := 2; i <= N; i++ {
		if spf[i] == 0 {
			for j := i; j <= N; j += i {
				if spf[j] == 0 {
					spf[j] = i
				}
			}
		}
	}
	for p := 2; p <= N; p++ {
		if spf[p] == p {
			for pk := p; pk <= N; pk *= p {
				pk64 := float64(pk)
				sum += math.Log(float64(p)) / math.Pow(pk64, 1.5)
			}
		}
	}
	f, _ := os.Create(out)
	fmt.Fprintf(f, "gamma_closure_max_res = %.3e\nlambda_sum_check = %.10f\nn_sieve = %d\n", maxRes, sum, N)
	f.Close()
	fmt.Println("go twin OK:", strconv.FormatFloat(maxRes, 'e', 2, 64), sum)
}
