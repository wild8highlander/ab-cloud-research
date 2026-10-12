// verify_core.go — двойник Go ≥ 1.21: Γ-замыкание + Λ-сито
package main

import (
	"fmt"
	"math"
	"os"
)

func cgamma(x, y float64) complex128 {
	z := complex(x-1, y)
	s := complex(0.99999999999980993, 0)
	LC := []float64{676.5203681218851, -1259.1392167224028,
		771.32342877765313, -176.61502916214059, 12.507343278686905,
		-0.13857109526572012, 9.9843695780195716e-6, 1.5056327351493116e-7}
	for i, v := range LC {
		s += complex(v, 0) / (z + complex(float64(i+1), 0))
	}
	t := z + complex(7.5, 0)
	ln2pi := 0.5 * math.Log(2*math.Pi)
	return cmul(cexp(complex(ln2pi, 0)+(z+complex(0.5, 0))*cmlog(t)-t+cmlog(s)), 1)
}
func cmlog(z complex128) complex128 {
	return complex(math.Log(math.Hypot(real(z), imag(z))), math.Atan2(imag(z), real(z)))
}
func cexp(z complex128) complex128 {
	return complex(math.Exp(real(z))*math.Cos(imag(z)), math.Exp(real(z))*math.Sin(imag(z)))
}
func cmul(a, b complex128) complex128 { return a * b }

func main() {
	maxres := 0.0
	for _, u := range []float64{0.5, 1, 2, 3} {
		g := cgamma(0.5, u)
		lhs := real(g)*real(g) + imag(g)*imag(g)
		rhs := math.Pi / math.Cosh(math.Pi*u)
		if r := math.Abs(lhs-rhs) / rhs; r > maxres {
			maxres = r
		}
	}
	const N = 100000
	spf := make([]int, N+1)
	lsum := 0.0
	for i := 2; i <= N; i++ {
		if spf[i] == 0 {
			for p := i; p <= N; p *= i {
				lsum += math.Log(float64(i)) / math.Pow(float64(p), 1.5)
				for j := i; j <= N; j += i {
					if spf[j] == 0 {
						spf[j] = i
					}
				}
			}
		}
	}
	fmt.Printf("gamma_closure_max_res = %.3e\n", maxres)
	fmt.Printf("lambda_sum_check = %.10f\n", lsum)
	fmt.Printf("n_sieve = %d\n", N)
	if len(os.Args) > 1 {
		f, _ := os.Create(os.Args[1])
		fmt.Fprintf(f, "gamma_closure_max_res = %.3e\n", maxres)
		fmt.Fprintf(f, "lambda_sum_check = %.10f\n", lsum)
		fmt.Fprintf(f, "n_sieve = %d\n", N)
		f.Close()
	}
}
