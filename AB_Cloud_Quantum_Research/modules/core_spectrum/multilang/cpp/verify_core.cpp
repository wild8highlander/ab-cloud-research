// verify_core.cpp — двойник C++17: Γ-замыкание (комплексный Lanczos) + Λ-сито
#include <cmath>
#include <complex>
#include <cstdio>
#include <vector>
using C = std::complex<double>;
static const double LC[9] = {
  0.99999999999980993, 676.5203681218851, -1259.1392167224028,
  771.32342877765313, -176.61502916214059, 12.507343278686905,
  -0.13857109526572012, 9.9843695780195716e-6, 1.5056327351493116e-7};
static C cgamma(C z) {
  z -= C(1, 0);   // формула Ланцоша требует z = x − 1 + iy
  C s = LC[0];
  for (int i = 1; i < 9; i++) s += LC[i] / (z + C(i, 0));
  C t = z + C(7.5, 0);
  return std::exp(C(0.5 * std::log(2 * M_PI), 0) + (z + C(0.5, 0)) *
                  std::log(t) - t + std::log(s));
}
int main(int argc, char **argv) {
  double maxres = 0;
  for (double u : {0.5, 1.0, 2.0, 3.0}) {
    C g = cgamma(C(0.5, u));
    double lhs = std::norm(g), rhs = M_PI / std::cosh(M_PI * u);
    maxres = std::max(maxres, std::fabs(lhs - rhs) / rhs);
  }
  int N = 100000;
  std::vector<int> spf(N + 1, 0);
  double lsum = 0;
  for (int i = 2; i <= N; i++) if (!spf[i])
    for (long long p = i; p <= N; p *= i) { lsum += std::log((double)i) /
      std::pow((double)p, 1.5); for (int j = i; j <= N; j += i)
        if (!spf[j]) spf[j] = i; }
  printf("gamma_closure_max_res = %.3e\n", maxres);
  printf("lambda_sum_check = %.10f\n", lsum);
  printf("n_sieve = %d\n", N);
  if (argc > 1) { FILE *f = fopen(argv[1], "w");
    fprintf(f, "gamma_closure_max_res = %.3e\n", maxres);
    fprintf(f, "lambda_sum_check = %.10f\n", lsum);
    fprintf(f, "n_sieve = %d\n", N); fclose(f); }
  return 0;
}
