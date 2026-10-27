// verify_core.cpp — C++-двойник ядра (см. multilang/README.md).
// Сборка: g++ -O2 -o /tmp/hpb_cpp verify_core.cpp
// Запуск: /tmp/hpb_cpp verify_control.txt
#include <cmath>
#include <cstdio>
#include <cstdlib>
static const double G = 7.0;
static const double C[9] = {0.99999999999980993, 676.5203681218851,
    -1259.1392167224028, 771.32342877765313, -176.61502916214059,
    12.507343278686905, -0.13857109526572012, 9.9843695780195716e-6,
    1.5056327351493116e-7};
static double mod_gamma(double re, double u) {
    double zr = re - 1.0, zi = u, xr = C[0], xi = 0.0;
    for (int i = 1; i < 9; i++) {
        double dr = zr + i, di = zi, den = dr*dr + di*di;
        xr += C[i] * dr / den; xi -= C[i] * di / den;
    }
    double tr = zr + G + 0.5, ti = zi;
    double mt = 0.5 * std::log(tr*tr + ti*ti), at = std::atan2(ti, tr);
    double pe = (zr + 0.5) * mt - ti * at, ph = ti * mt + (zr + 0.5) * at;
    double ar = std::exp(pe) * std::cos(ph), ai = std::exp(pe) * std::sin(ph);
    double e = std::exp(-tr), br = e * std::cos(-ti), bi = e * std::sin(-ti);
    double c1r = ar*xr - ai*xi, c1i = ar*xi + ai*xr;
    double d1r = c1r*br - c1i*bi, d1i = c1r*bi + c1i*br;
    double gr = std::sqrt(2*M_PI) * d1r, gi = std::sqrt(2*M_PI) * d1i;
    return std::sqrt(gr*gr + gi*gi);
}
int main(int argc, char **argv) {
    const char *out = argc > 1 ? argv[1] : "verify_control.txt";
    double max_res = 0; double us[4] = {0.5, 1.0, 2.0, 3.0};
    for (int i = 0; i < 4; i++) {
        double ref = std::sqrt(M_PI / std::cosh(M_PI * us[i]));
        double res = std::fabs(mod_gamma(0.5, us[i]) - ref) / ref;
        if (res > max_res) max_res = res;
    }
    const int N = 100000; int *spf = (int*)calloc(N+1, sizeof(int));
    double sum = 0;
    for (int i = 2; i <= N; i++) if (!spf[i])
        for (int j = i; j <= N; j += i) if (!spf[j]) spf[j] = i;
    for (int p = 2; p <= N; p++) if (spf[p] == p)
        for (long long pk = p; pk <= N; pk *= p)
            sum += std::log((double)p) / std::pow((double)pk, 1.5);
    FILE *f = fopen(out, "w");
    fprintf(f, "gamma_closure_max_res = %.3e\nlambda_sum_check = %.10f\nn_sieve = %d\n",
            max_res, sum, N);
    fclose(f); printf("cpp twin OK: %.2e %.10f\n", max_res, sum); return 0;
}
