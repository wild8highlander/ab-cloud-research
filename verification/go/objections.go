package main

import "math"

// Structured objection results (CANON_SPEC §7) — language-agnostic payloads
// rendered by verify_en.go / verify_ru.go.

type Obj1Res struct {
        Ns         []int
        BN         []float64
        Converging bool
        HasFit     bool
        FitA       float64
        FitS       float64
        FitR2      float64
}

type Obj2Res struct {
        N        int
        Mean     float64
        Var      float64
        D        float64
        P        float64
        W2       float64
        A2       float64
        R        float64
        NR       int
        Rejected bool
}

type Obj3Res struct {
        Ns        []int
        BN        []float64
        Slope     float64
        Intercept float64
        R2        float64
        SE        float64
        CILO      float64
        CIHI      float64
        OK        bool
}

// RunObjection1: grid {100,500,1000,5000,10000,50000}, monotone verdict.
func RunObjection1(zeros []float64) Obj1Res {
        res := Obj1Res{Converging: true}
        maxZ := len(zeros)
        for _, N := range []int{100, 500, 1000, 5000, 10000, 50000} {
                if N <= maxZ {
                        res.Ns = append(res.Ns, N)
                }
        }
        if len(res.Ns) == 0 {
                n := maxZ
                if n > 100 {
                        n = 100
                }
                res.Ns = []int{n}
        }
        for i, N := range res.Ns {
                bn := ComputeBN(zeros, N)
                res.BN = append(res.BN, bn)
                if i > 0 && bn >= res.BN[i-1] {
                        res.Converging = false
                }
        }
        if len(res.Ns) >= 3 {
                var lx, ly []float64
                for i, N := range res.Ns {
                        if N > 1 && res.BN[i] > 0 {
                                lx = append(lx, math.Log(float64(N)))
                                ly = append(ly, math.Log(res.BN[i]))
                        }
                }
                if len(lx) >= 3 {
                        lr := LinregFit(lx, ly)
                        if lr.M >= 3 {
                                res.HasFit = true
                                res.FitA = math.Exp(lr.Intercept)
                                res.FitS = -lr.Slope
                                res.FitR2 = lr.R2
                        }
                }
        }
        return res
}

// RunObjection2: statistics on ALL loaded zeros.
func RunObjection2(zeros []float64) Obj2Res {
        sp := ComputeSpacings(zeros)
        res := Obj2Res{N: len(sp)}
        if len(sp) < 2 {
                return res
        }
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
        r, nr := MeanRatio(zeros)
        res.Mean, res.Var, res.D, res.P = mean, variance, D, p
        res.W2 = CvmTest(sp)
        res.A2 = AdStat(sp)
        res.R, res.NR = r, nr
        res.Rejected = p < 0.05
        return res
}

// RunObjection3: grid 50*2^k plus last, OLS log-log, honest -0.5 verdict.
func RunObjection3(zeros []float64) Obj3Res {
        maxZ := len(zeros)
        var Ns []int
        for N := 50; N <= maxZ; N *= 2 {
                Ns = append(Ns, N)
        }
        if len(Ns) > 0 && Ns[len(Ns)-1] != maxZ && maxZ > 100 {
                Ns = append(Ns, maxZ)
        }
        res := Obj3Res{Ns: Ns}
        var lx, ly []float64
        for _, N := range Ns {
                bn := ComputeBN(zeros, N)
                res.BN = append(res.BN, bn)
                if bn > 0 {
                        lx = append(lx, math.Log(float64(N)))
                        ly = append(ly, math.Log(bn))
                }
        }
        if len(lx) < 3 {
                return res
        }
        lr := LinregFit(lx, ly)
        res.Slope = lr.Slope
        res.Intercept = lr.Intercept
        res.R2 = lr.R2
        res.SE = lr.SE
        res.CILO = lr.Slope - 1.96*lr.SE
        res.CIHI = lr.Slope + 1.96*lr.SE
        res.OK = math.Abs(lr.Slope+0.5) < 0.1
        return res
}
