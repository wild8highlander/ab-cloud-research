/* verify_core.c — мультиязычный двойник (C11): Γ-замыкание + Λ-сито.
   Сверяется с Python-эталоном IVP-слоем (расхождение Λ C↔Python ≤ 1e-11). */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/* Lanczos g=7, n=9 (классические коэффициенты) */
static const double LC[9] = {
  0.99999999999980993, 676.5203681218851, -1259.1392167224028,
  771.32342877765313, -176.61502916214059, 12.507343278686905,
  -0.13857109526572012, 9.9843695780195716e-6, 1.5056327351493116e-7};

static void cgamma(double x, double y, double *re, double *im) {
  /* Комплексный Lanczos g=7, n=9: Log Γ(x+iy) для Re x ≥ 0.5 */
  double zr = x - 1.0, zi = y;
  double sr = LC[0], si = 0.0;
  for (int i = 1; i < 9; i++) {
    double dr = zr + i, di = zi;
    double d = dr*dr + di*di;
    sr += LC[i] * dr / d;
    si += LC[i] * (-di) / d;
  }
  double tr = zr + 7.5, ti = zi;
  double lt_r = 0.5 * log(tr*tr + ti*ti), lt_i = atan2(ti, tr);
  double ls_r = 0.5 * log(sr*sr + si*si), ls_i = atan2(si, sr);
  double ar = zr + 0.5, ai = zi;
  double Lr = 0.5 * log(2 * M_PI) + (ar*lt_r - ai*lt_i) - tr + ls_r;
  double Li = (ar*lt_i + ai*lt_r) + ls_i;
  *re = exp(Lr) * cos(Li);
  *im = exp(Lr) * sin(Li);
}

int main(int argc, char **argv) {
  /* 1) Γ-замыкание |Γ(1/2+iu)|² = π/cosh(πu) на u ∈ {0.5, 1, 2, 3} */
  double maxres = 0.0;
  double us[4] = {0.5, 1.0, 2.0, 3.0};
  for (int k = 0; k < 4; k++) {
    double u = us[k];
    double gr, gi;
    cgamma(0.5, u, &gr, &gi);
    double lhs = gr*gr + gi*gi;
    double rhs = M_PI / cosh(M_PI * u);
    double res = fabs(lhs - rhs) / rhs;
    if (res > maxres) maxres = res;
  }
  /* 2) Λ-сито до 100000 + Σ Λ(n)/n^{3/2} */
  int N = 100000;
  int *spf = (int *)calloc(N + 1, sizeof(int));
  double lsum = 0.0;
  int npc = 0;
  for (int i = 2; i <= N; i++) {
    if (spf[i] == 0) { spf[i] = i; npc++; }
    for (int p = 2; p <= spf[i] && (long long)i * p <= N; p++)
      if (spf[i*p] == 0) spf[i*p] = p;
  }
  for (int p = 2; p <= N; p++)
    if (spf[p] == p)
      for (long long pk = p; pk <= N; pk *= p) {
        double lam = log((double)p);
        lsum += lam / pow((double)pk, 1.5);
      }
  FILE *f = NULL;
  if (argc > 1) f = fopen(argv[1], "w");
  printf("gamma_closure_max_res = %.3e\n", maxres);
  printf("lambda_sum_check = %.10f\n", lsum);
  printf("n_sieve = %d\n", N);
  if (f) {
    fprintf(f, "gamma_closure_max_res = %.3e\n", maxres);
    fprintf(f, "lambda_sum_check = %.10f\n", lsum);
    fprintf(f, "n_sieve = %d\n", N);
    fclose(f);
  }
  free(spf);
  return 0;
}
