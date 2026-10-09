/* verify_core.c — C-двойник ядра Hilbert Polya Bridge.
 * Пересчитывает: (1) замыкание Γ-лестницы |Γ(½+iu)|² = π/cosh(πu)
 * через реализацию Ланцоша; (2) Λ-сумму Σ Λ(n)/n^{3/2} до 1e5 решетом.
 * Печатает управляющий блок verify_control.txt (сверяется IVP10).
 * Сборка: cc -O2 multilang/c/verify_core.c -lm -o /tmp/hpb_c
 * Запуск: /tmp/hpb_c multilang/c/verify_control.txt
 */
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* Ланцош g=7, n=9 (коэффициенты — классические, пересчитаны в hpbridge) */
static const double LANCS_G = 7.0;
static const double LANCS_C[9] = {
    0.99999999999980993, 676.5203681218851, -1259.1392167224028,
    771.32342877765313, -176.61502916214059, 12.507343278686905,
    -0.13857109526572012, 9.9843695780195716e-6, 1.5056327351493116e-7};

static double gamma_re(double z) { /* Re Г(z) для Re z > 0.5 */
    z -= 1.0;
    double x = LANCS_C[0];
    for (int i = 1; i < 9; i++) x += LANCS_C[i] / (z + i);
    double t = z + LANCS_G - 0.5;
    return sqrt(2.0 * M_PI) * pow(t, z + 0.5) * exp(-t) * x;
}

static double mod_gamma_half_plus_iu(double u) { /* |Γ(½+iu)| = √(π/cosh πu) */
    return sqrt(M_PI / cosh(M_PI * u));
}

static double mod_gamma_lanczos(double re, double u) {
    /* |Г(re+iu)| — комплексный Ланцош (порт эталонной реализации) */
    double zr = re - 1.0, zi = u;
    double xr = LANCS_C[0], xi = 0.0;
    for (int i = 1; i < 9; i++) {
        double dr = zr + i, di = zi;
        double den = dr * dr + di * di;
        xr += LANCS_C[i] * dr / den;
        xi -= LANCS_C[i] * di / den;
    }
    double tr = zr + LANCS_G + 0.5, ti = zi;
    double mt = 0.5 * log(tr * tr + ti * ti);  /* ln|t| */
    double at = atan2(ti, tr);                 /* arg t */
    /* t^{z+1/2}: модуль exp(Re·ln|t| − Im·arg), фаза Im·ln|t| + Re·arg */
    double pe = (zr + 0.5) * mt - ti * at;
    double ph = ti * mt + (zr + 0.5) * at;
    double ar = exp(pe) * cos(ph), ai = exp(pe) * sin(ph);
    /* e^{-t} */
    double e = exp(-tr);
    double br = e * cos(-ti), bi = e * sin(-ti);
    /* произведения */
    double c1r = ar * xr - ai * xi, c1i = ar * xi + ai * xr;
    double d1r = c1r * br - c1i * bi, d1i = c1r * bi + c1i * br;
    double gr = sqrt(2.0 * M_PI) * d1r, gi = sqrt(2.0 * M_PI) * d1i;
    return sqrt(gr * gr + gi * gi);
}

int main(int argc, char **argv) {
    const char *out = (argc > 1) ? argv[1] : "verify_control.txt";
    /* (1) Γ-замыкание: |Γ(½+iu)| через Ланцош против π/cosh(πu) */
    double max_res = 0.0;
    double us[4] = {0.5, 1.0, 2.0, 3.0};
    for (int i = 0; i < 4; i++) {
        double u = us[i];
        double ml = mod_gamma_lanczos(0.5, u);
        double ref = mod_gamma_half_plus_iu(u);
        double res = fabs(ml - ref) / ref;
        if (res > max_res) max_res = res;
    }
    /* (2) Λ-сумма решетом до 1e5 */
    const int N = 100000;
    int *spf = calloc(N + 1, sizeof(int));
    double sum = 0.0;
    for (int i = 2; i <= N; i++) {
        if (spf[i] == 0) {
            for (int j = i; j <= N; j += i) if (spf[j] == 0) spf[j] = i;
        }
    }
    for (int p = 2; p <= N; p++) {
        if (spf[p] == p) { /* простое */
            for (long long pk = p; pk <= N; pk *= p) sum += log((double)p) / pow((double)pk, 1.5);
        }
    }
    FILE *f = fopen(out, "w");
    fprintf(f, "gamma_closure_max_res = %.3e\n", max_res);
    fprintf(f, "lambda_sum_check = %.10f\n", sum);
    fprintf(f, "n_sieve = %d\n", N);
    fclose(f);
    printf("C twin OK: gamma_res=%.2e lambda_sum=%.10f -> %s\n", max_res, sum, out);
    free(spf);
    return 0;
}
