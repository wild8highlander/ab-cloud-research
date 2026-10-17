# CANON SPEC — unified numerical kernel for all 10 languages (v3.0)

Every language implementation of the AB-Cloud Verification Suite MUST follow
this spec exactly. It is bit-compatible with the frozen golden reference
`data/abcloud_golden.json` (canon: meridian-spectral-observatory ports,
selftest 199/199, Julia 1.10.9, first 50 000 Odlyzko zeros).
Each implementation must embed the anchors below in a `selfcheck` that runs
before the objections and prints PASS/FAIL/Δ per anchor; exit code 1 if any
anchor fails. NO canned verdict strings: every conclusion must be printed
only in the branch chosen by the computed numbers.

## 1. Lambert W (principal branch)

```
lambert_w(x):  x <= 0 -> 0
  w = log(x);  if w > 0: w -= log(w)
  repeat up to 50 times:
    ew = exp(w); f = w*ew - x; fp = ew*(w+1)
    delta = f/fp                       # Newton; Halley also acceptable
    w -= delta
    if |delta| < 1e-14*(1+|w|): break
  return w
```

## 2. Gram point (CANON — the old seed-only formula is WRONG)

```
gram_point(k):  k <= 0 -> 0
  t = 2*pi*k / lambert_w(k/e)          # seed only
  repeat 8 times:                      # Newton on refined Riemann–Siegel theta
    arg = t/(2*pi);  if arg <= 0: break
    theta  = (t/2)*log(arg) - t/2 - pi/8 + 1/(48*t) + 7/(5760*t^3)
    dtheta = 0.5*log(arg) - 1/(48*t^2) - 21/(5760*t^4)
    if |dtheta| < 1e-30: break
    t -= (theta - pi*k)/dtheta
  return t
```

## 3. b(N)

```
bN(zeros, N)     = (1/N) * sum_{k=1..N} |zeros[k-1] - gram_point(k)|
bN_off(z,N,off)  = (1/N) * sum_{k=1..N} |zeros[k-1] - gram_point(off+k)|
```
Sequential accumulation in this exact order (bit-parity across languages).

## 4. Normalized spacings

```
for k in 0..n-2:  if zeros[k] > 0:
    s = (zeros[k+1]-zeros[k]) * log(zeros[k]/(2*pi)) / (2*pi)
```

## 5. GUE CDF — Wigner–Dyson β=2 surmise, via 32768-point table

```
exact(s) = erf(2s/sqrt(pi)) - (4s/pi)*exp(-4s^2/pi)
TN = 32768;  SMAX = 5.0
table[i] = exact(i*SMAX/(TN-1)),  i = 0..TN-1        (built lazily once)
gue_cdf(s):
  s <= 0    -> 0
  s >= SMAX -> exact(s)
  x = s*(TN-1)/SMAX;  i = floor(x)
  i < 0 or i >= TN-1 -> exact(s)
  t = x - i;  return (1-t)*table[i] + t*table[i+1]
```

## 6. Statistics (all on the loaded spacings; sort ascending first)

```
KS:  D = max_i max( |i/n - F(s_i)|, |(i-1)/n - F(s_i)| ),  i = 1..n
     lam = (sqrt(n) + 0.12 + 0.11/sqrt(n)) * D
     p(lam): lam <= 0 -> 1
       lam < 0.6:  v = 1 - sqrt(2*pi)/lam * sum_{k=1..1000} exp(-((2k-1)^2*pi^2)/(8*lam^2))
                   (break when term < 1e-18)
       else:       v = 2 * sum_{k=1..100} (-1)^(k+1) * exp(-2*k^2*lam^2)
                   (break when |term| < 1e-18)
       clamp v to [0,1]
CvM: W2 = 1/(12n) + sum_i ( F(s_i) - (2i-1)/(2n) )^2
AD:  A2 = -n - (1/n) * sum_i (2i-1) * ( ln(clamp(F_i)) + ln(clamp(1-F_{n+1-i})) )
     clamp(x) = min(max(x, 1e-300), 1-1e-16)
<r>: gaps d_i = z_{i+1}-z_i;  mean over adjacent pairs of min(d_i,d_{i+1})/max(d_i,d_{i+1}),
     skipping pairs where both are 0; n_r = number of counted pairs
mean/var: sample variance (divide by n-1)
```

## 7. Objection protocol

- **Obj 1**: grid N = {100, 500, 1000, 5000, 10000, 50000} filtered to N <= n.
  Print b(N) table (prefix-sum allowed: prefix[N]/N is bit-identical to the
  direct sum). Verdict = monotone decrease across the table (honest criterion)
  + optional empirical power-law fit on the printed grid; state explicitly
  that the decay is EMPIRICAL, not O(1/sqrt(N)).
- **Obj 2**: statistics on ALL loaded zeros: mean/var, KS D+p, CvM W2, AD A2,
  <r> vs GUE reference 0.5992. Verdict: p < 0.05 -> H0 rejected, and when
  rejected print the honest note (finite-T corrections, mean ~= 1 validates
  the unfolding). NEVER print "GUE confirmed" unconditionally.
- **Obj 3**: grid N = 50*2^k while <= n, plus n itself if not already there;
  OLS of log b(N) vs log N -> slope, intercept, R2, slope stderr
  (se^2 = (SSres/(m-2)) * m / (m*Sxx - Sx^2)), 95% CI = ±1.96*se.
  Verdict: |slope-(-0.5)| <= 0.1 -> consistent, else INCONSISTENT (honest).
- **Summary**: selfcheck n/n first, then per-objection status.

## 8. selfcheck anchors (frozen, embed as literals)

Tolerances: lambert_w 1e-12 rel; gram_point/bN 1e-6 abs; spacings.mean/var,
ks.D, cvm, ad, rmean 1e-9 (ks.p 1e-6 rel). Stats anchors computed on the
FIRST 50000 zeros only (skip with a printed SKIP if fewer are loaded).
bN anchors need N <= n; bN_off needs n >= 1500.

```
lambert_w: 0.5->0.35173371124919584  1.0->0.5671432904097838
           3.7->1.1599531786120223  10.0->1.7455280027406992
           271.8->4.17576816800275  12345.6->7.417247034540566
gram_point: 1->23.17028270133466     2->27.670182217848343
            3->31.71797995477886     10->54.67523744685398
            100->238.58259051450293  1000->1421.25638903275
            10000->9878.910118894457 50000->40434.6952780045
bN:  100->3.3321638710140165   500->2.3912304957476382
     1000->2.1072522951855435  5000->1.6299485869022874
     10000->1.4794053414584762 50000->1.2125526772588608
bN_off(1000,500) -> 624.6201618180231
spacings.mean -> 0.999976001221201      spacings.var -> 0.1590654827835423
ks.D -> 0.021619337032982328            ks.p -> 9.567870399361496e-21
cvm.W2 -> 8.177703317829403             ad.A2 -> 61.49242624209728
rmean.r -> 0.6118798907208398           (n_r = 49998)
```

## 9. CLI / defaults (all languages)

```
--zeros N      default 50000
--source NAME  auto|50k|50k_full|500k|2M|highT|2M_gz|csv|zeros6
--objection X  1|2|3|all
--lang L       en|ru   (default en; auto-detect optional)
--data-dir D   default ../data relative to the language folder
```
Source registry (name, file, approx count): 50k zeta_zeros_50000.txt 13661;
50k_full zeta_zeros_50000_embedded.txt 50000; 500k zeta_zeros_500k_odlyzko.txt
500000; 2M zeta_zeros_2M_odlyzko.txt 2001052; highT zeta_zeros_highT_blocks.txt
30000 (BLOCK offset format); 2M_gz gzipped 2M; csv zeta_zeros_50000.csv 13661;
zeros6 zeros6.txt 2001052. auto = smallest file with count >= zeros.

## 10. Deduplication rule

`*_en` / `*_ru` files must be THIN wrappers pinning the language (import the
main module / include the main source with a language macro). No duplicated
math — duplicated kernels are how the old suite drifted apart.
