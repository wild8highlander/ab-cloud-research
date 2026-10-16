// ============================================================================
// abcloud_port.cpp — C++17 port of the meridian-spectral-observatory suite.
//
// Bit-faithful kernel port of ab_cloud_full.jl / hp_audit_standalone.jl /
// AB_Cloud_Monumental_v6_3.jl (computational core). Golden-reference
// verification: ports/golden/abcloud_golden.json generated from the
// UNMODIFIED Julia originals by ports/golden/gen_golden.jl.
//
// Build:  g++ -O2 -std=c++17 -o abcloud abcloud_port.cpp
// Run:    ./abcloud selftest | zeros | suite | ham | bN | gram | test11 | hp | sweep
//
// Eigenvalues: cyclic Jacobi for complex Hermitian matrices (no LAPACK
// dependency; agrees with LAPACK zheevr to ~1e-12 on these spectra, which
// is inside the golden tolerances for the eigen-anchored sections).
// Disorder note: W>0 residual ε uses the portable classic MT19937 (the
// Julia original uses dSFMT — documented divergence, goldens are all W=0).
// ============================================================================

#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdint>
#include <cstdlib>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <complex>
#include <fstream>
#include <sstream>
#include <iostream>
#include <unistd.h>

typedef std::complex<double> cd;
static const double PI = 3.14159265358979323846;

// ─────────────────────────────────────────────────────────────────────────────
// Classic MT19937 (init_genrand) — bit-identical in all language ports.
// ─────────────────────────────────────────────────────────────────────────────
struct MT19937 {
    uint32_t mt[624];
    int idx;
    explicit MT19937(uint32_t seed) : idx(624) {
        mt[0] = seed;
        for (int i = 1; i < 624; ++i)
            mt[i] = (uint32_t)(1812433253u * (mt[i-1] ^ (mt[i-1] >> 30)) + (uint32_t)i);
    }
    uint32_t next_u32() {
        if (idx >= 624) {
            for (int kk = 0; kk < 624; ++kk) {
                uint32_t y = (mt[kk] & 0x80000000u) | (mt[(kk + 1) % 624] & 0x7fffffffu);
                uint32_t nxt = mt[(kk + 397) % 624] ^ (y >> 1);
                if (y & 1u) nxt ^= 0x9908b0dfu;
                mt[kk] = nxt;
            }
            idx = 0;
        }
        uint32_t y = mt[idx++];
        y ^= y >> 11;
        y ^= (y << 7) & 0x9d2c5680u;
        y ^= (y << 15) & 0xefc60000u;
        y ^= y >> 18;
        return y;
    }
    double random() {  // [0,1), identical to CPython random.random()
        uint32_t a = next_u32() >> 5, b = next_u32() >> 6;
        return ((double)a * 67108864.0 + (double)b) / 9007199254740992.0;
    }
};

// ─────────────────────────────────────────────────────────────────────────────
// Scalar special functions — 1:1 with ab_cloud_full.jl §3 (see special.py)
// ─────────────────────────────────────────────────────────────────────────────
static const double _LANCZOS_COEF[9] = {
    0.99999999999980993, 676.5203681218851, -1259.1392167224028,
    771.32342877765313, -176.61502916214059, 12.507343278686905,
    -0.13857109526572012, 9.9843695780195716e-6, 1.5056327351493116e-7
};

static double lgamma_lanczos(double x) {
    if (x < 0.5)
        return std::log(PI / std::sin(PI * x)) - lgamma_lanczos(1.0 - x);
    x -= 1.0;
    double a = _LANCZOS_COEF[0];
    double t = x + 7.0 + 0.5;
    for (int i = 1; i <= 7; ++i) a += _LANCZOS_COEF[i] / (x + i);
    return 0.5 * std::log(2 * PI) + (x + 0.5) * std::log(t) - t + std::log(a);
}

static double gammp_series(double a, double x) {
    double ap = a, total = 1.0 / a, delta = total;
    for (int it = 0; it < 200; ++it) {
        ap += 1.0;
        delta *= x / ap;
        total += delta;
        if (std::fabs(delta) < std::fabs(total) * 1e-15) break;
    }
    return total * std::exp(-x + a * std::log(x) - lgamma_lanczos(a));
}

static double gammq_cf(double a, double x) {
    const double FPMIN = 1e-300;
    double b = x + 1.0 - a, c = 1.0 / FPMIN, d = 1.0 / b, h = d;
    for (int i = 1; i <= 200; ++i) {
        double an = -(double)i * (i - a);
        b += 2.0;
        d = an * d + b;
        if (std::fabs(d) < FPMIN) d = FPMIN;
        c = b + an / c;
        if (std::fabs(c) < FPMIN) c = FPMIN;
        d = 1.0 / d;
        double delta = d * c;
        h *= delta;
        if (std::fabs(delta - 1.0) < 1e-15) break;
    }
    return std::exp(-x + a * std::log(x) - lgamma_lanczos(a)) * h;
}

static double regularized_gamma_p(double a, double x) {
    if (x <= 0.0) return 0.0;
    return x < a + 1.0 ? gammp_series(a, x) : 1.0 - gammq_cf(a, x);
}
static double chi2_cdf(double x, double df) {
    return regularized_gamma_p(df / 2.0, x / 2.0);
}

static double ks_asymptotic_pvalue(double lam) {
    if (lam <= 0.0) return 1.0;
    if (lam < 0.6) {
        double s2 = 0.0;
        for (int k = 1; k <= 1000; ++k) {
            double term2 = std::exp(-(((2.0*k - 1.0)*(2.0*k - 1.0)) * PI * PI) / (8.0 * lam * lam));
            s2 += term2;
            if (term2 < 1e-18) break;
        }
        double v = 1.0 - std::sqrt(2 * PI) / lam * s2;
        return v < 0.0 ? 0.0 : (v > 1.0 ? 1.0 : v);
    }
    double s = 0.0, sign = 1.0;
    for (int k = 1; k <= 100; ++k) {
        double term = sign * std::exp(-2.0 * k * k * lam * lam);
        s += term;
        sign = -sign;
        if (std::fabs(term) < 1e-18) break;
    }
    double v = 2.0 * s;
    return v < 0.0 ? 0.0 : (v > 1.0 ? 1.0 : v);
}

static double goe_surmise_cdf(double s) { return 1.0 - std::exp(-PI * s * s / 4.0); }
static double gue2_surmise_cdf(double s) {
    if (s < 0) return 0.0;
    double x2 = 4.0 * s * s / PI;
    return regularized_gamma_p(0.5, x2) - (4.0 * s / PI) * std::exp(-x2);
}
static double gue2_surmise_pdf(double s) {
    return (32.0 / (PI * PI)) * s * s * std::exp(-4.0 * s * s / PI);
}

static double lambert_w(double x) {  // W0 branch, Halley — verbatim
    if (x <= -1.0 / std::exp(1.0)) return -1.0;
    double w = x < 1.5 ? x : std::log(x) - std::log(std::log(x));
    for (int it = 0; it < 50; ++it) {
        double ew = std::exp(w);
        double f = w * ew - x, fp = ew * (w + 1.0), fpp = ew * (w + 2.0);
        double delta = -f / (fp - 0.5 * f * fpp / fp);
        w += delta;
        if (std::fabs(delta) < 1e-15 * std::fabs(w)) break;
    }
    return w;
}

static double gram_point(long n) {
    if (n <= 0) return 0.0;
    double t = 2 * PI * (double)n / lambert_w((double)n / std::exp(1.0));
    for (int it = 0; it < 8; ++it) {
        double arg = t / (2 * PI);
        if (arg <= 0) break;
        double theta = t/2*std::log(arg) - t/2 - PI/8 + 1.0/(48*t) + 7.0/(5760*t*t*t);
        double dtheta = 0.5*std::log(arg) - 1.0/(48*t*t) - 21.0/(5760*t*t*t*t);
        if (std::fabs(dtheta) < 1e-30) break;
        t -= (theta - (double)n * PI) / dtheta;
    }
    return t;
}

static double compute_bN(const std::vector<double>& z, long N, long offset = 0) {
    N = std::min<long>(N, (long)z.size());
    double s = 0.0;
    for (long k = 1; k <= N; ++k)
        s += std::fabs(z[k-1] - gram_point(offset + k));
    return s / (double)N;
}

// ─────────────────────────────────────────────────────────────────────────────
// RMT reference-law engine (see rmt_table.py)
// ─────────────────────────────────────────────────────────────────────────────
struct RmtTable {
    int law = 0;  // 0 = gue2, 1 = goe
    bool table_on = true;
    std::vector<double> cdf;
    std::vector<double> quant;
    double quant_umax = 0.0;
    static const int TN = 32768;
    static const int QN = 4096;
    static const double SMAX;

    double gue2_exact(double s) const { return gue2_surmise_cdf(s); }
    void build_cdf() {
        cdf.resize(TN);
        for (int i = 0; i < TN; ++i) cdf[i] = gue2_exact(i * SMAX / (TN - 1));
    }
    double table_cdf(double s) {
        if (s < 0) return 0.0;
        if (law == 1) return goe_surmise_cdf(s);
        if (cdf.empty()) build_cdf();
        if (s >= SMAX) return gue2_exact(s);
        double x = s * (TN - 1) / SMAX;
        int i = (int)std::floor(x);
        if (i < 0 || i >= TN - 1) return gue2_exact(s);
        double t = x - i;
        return (1.0 - t) * cdf[i] + t * cdf[i + 1];
    }
    double gue_cdf(double s) {
        if (law == 1) return goe_surmise_cdf(s);
        if (table_on) return table_cdf(s);
        return gue2_exact(s);
    }
    void build_quant() {
        quant.resize(QN + 1);
        double smax_q = SMAX;
        quant_umax = gue_cdf(smax_q);
        for (int j = 0; j <= QN; ++j) {
            double u = quant_umax * (double)j / QN, lo = 0.0, hi = smax_q;
            for (int it = 0; it < 48; ++it) {
                double mid = 0.5 * (lo + hi);
                if (gue_cdf(mid) < u) lo = mid; else hi = mid;
            }
            quant[j] = 0.5 * (lo + hi);
        }
    }
    void sample(MT19937& rng, std::vector<double>& out) {
        if (quant.empty()) build_quant();
        for (size_t k = 0; k < out.size(); ++k) {
            double x = rng.random() * QN;
            int j = (int)std::floor(x);
            if (j > QN - 1) j = QN - 1;
            if (j < 0) j = 0;
            double t = std::min(x - j, 1.0);
            out[k] = (1.0 - t) * quant[j] + t * quant[j + 1];
        }
    }
};
const double RmtTable::SMAX = 5.0;
static RmtTable RMT;  // active reference law (process-wide, like the Julia Ref)

// ─────────────────────────────────────────────────────────────────────────────
// GOF + long-range statistics (see gof.py)
// ─────────────────────────────────────────────────────────────────────────────
static void normalized_spacings(const std::vector<double>& z, std::vector<double>& sp) {
    sp.clear();
    for (size_t k = 0; k + 1 < z.size(); ++k) {
        if (z[k] <= 0) continue;
        sp.push_back((z[k+1] - z[k]) * std::log(z[k] / (2 * PI)) / (2 * PI));
    }
}

struct Linreg { double a, b, R2, se_b; std::vector<double> res; };
static Linreg linreg(const std::vector<double>& x, const std::vector<double>& y) {
    Linreg r{};
    size_t n = x.size();
    double mx = 0, my = 0;
    for (size_t i = 0; i < n; ++i) { mx += x[i]; my += y[i]; }
    mx /= n; my /= n;
    double Sxx = 0, Sxy = 0;
    for (size_t i = 0; i < n; ++i) { Sxx += (x[i]-mx)*(x[i]-mx); Sxy += (x[i]-mx)*(y[i]-my); }
    if (Sxx == 0.0 || n < 2) {
        r.a = r.b = r.R2 = 0.0; r.se_b = std::nan("");
        r.res.assign(n, 0.0);
        return r;
    }
    r.b = Sxy / Sxx;
    r.a = my - r.b * mx;
    r.res.resize(n);
    double ss_res = 0, ss_tot = 0;
    for (size_t i = 0; i < n; ++i) {
        r.res[i] = y[i] - (r.a + r.b * x[i]);
        ss_res += r.res[i] * r.res[i];
        ss_tot += (y[i]-my)*(y[i]-my);
    }
    r.R2 = ss_tot > 0 ? 1.0 - ss_res / ss_tot : 0.0;
    r.se_b = (n > 2 && Sxx > 0) ? std::sqrt(ss_res / ((double)(n - 2) * Sxx)) : std::nan("");
    return r;
}

static void ks_test(const std::vector<double>& sp, double& D, double& p) {
    size_t n = sp.size();
    std::vector<double> s(sp);
    std::sort(s.begin(), s.end());
    D = 0.0;
    for (size_t i = 1; i <= n; ++i) {
        double F = RMT.gue_cdf(s[i-1]);
        D = std::max(D, std::max(std::fabs((double)i/n - F), std::fabs((double)(i-1)/n - F)));
    }
    double lam = (std::sqrt((double)n) + 0.12 + 0.11 / std::sqrt((double)n)) * D;
    p = ks_asymptotic_pvalue(lam);
}

static double cvm_test(const std::vector<double>& sp) {
    size_t n = sp.size();
    std::vector<double> s(sp);
    std::sort(s.begin(), s.end());
    double W2 = 0.0;
    for (size_t i = 1; i <= n; ++i) {
        double u = RMT.gue_cdf(s[i-1]);
        W2 += (u - (2.0*i - 1.0) / (2.0*n)) * (u - (2.0*i - 1.0) / (2.0*n));
    }
    return W2 + 1.0 / (12.0 * n);
}

static double anderson_darling_stat(const std::vector<double>& sp) {
    size_t n = sp.size();
    std::vector<double> s(sp);
    std::sort(s.begin(), s.end());
    double acc = 0.0;
    for (size_t i = 1; i <= n; ++i) {
        double Fi = RMT.gue_cdf(s[i-1]);
        double Fni = RMT.gue_cdf(s[n - i]);
        Fi = std::min(std::max(Fi, 1e-300), 1.0 - 1e-16);
        Fni = std::min(std::max(Fni, 1e-300), 1.0 - 1e-16);
        acc += (2.0*i - 1.0) * (std::log(Fi) + std::log(1.0 - Fni));
    }
    return -(double)n - acc / (double)n;
}

static void chi2_gue_test(const std::vector<double>& sp, int nbins,
                          double& chi2, int& df, double& p) {
    std::vector<double> s(sp);
    std::sort(s.begin(), s.end());
    double s_max = std::min(s.back(), 4.0);
    std::vector<int> obs(nbins, 0);
    for (double v : s) {
        if (v >= s_max) { obs[nbins-1]++; }
        else {
            int b = std::min((int)std::floor(v / s_max * nbins) + 1, nbins);
            obs[b-1]++;
        }
    }
    size_t N = s.size();
    std::vector<double> edges(nbins + 1);
    for (int i = 0; i <= nbins; ++i) edges[i] = s_max * i / nbins;
    chi2 = 0.0; df = 0;
    for (int i = 1; i <= nbins; ++i) {
        double ec = (i < nbins) ? N * (RMT.gue_cdf(edges[i]) - RMT.gue_cdf(edges[i-1]))
                                : N * (1.0 - RMT.gue_cdf(edges[i-1]));
        if (ec < 5) continue;
        chi2 += (obs[i-1] - ec) * (obs[i-1] - ec) / ec;
        df++;
    }
    df = std::max(df - 1, 1);
    p = 1.0 - chi2_cdf(chi2, df);
}

static void mean_adjacent_spacing_ratio(const std::vector<double>& eigs,
                                        double& r_mean, long& n_r) {
    size_t n = eigs.size();
    r_mean = std::nan(""); n_r = 0;
    if (n < 3) return;
    std::vector<double> s(eigs);
    std::sort(s.begin(), s.end());
    std::vector<double> d(n - 1);
    for (size_t i = 0; i + 1 < n; ++i) d[i] = s[i+1] - s[i];
    if (d.size() < 2) return;
    double acc = 0; long cnt = 0;
    for (size_t i = 0; i + 1 < d.size(); ++i) {
        double a = d[i], b = d[i+1], m = std::max(a, b);
        if (a == 0.0 && b == 0.0) continue;
        acc += std::min(a, b) / m;
        cnt++;
    }
    if (cnt <= 0) return;
    r_mean = acc / (double)cnt;
    n_r = cnt;
}

static double smooth_counting_function(double T) {
    if (T <= 0.0) return 0.0;
    double x = T / (2 * PI);
    return x * std::log(x) - x + 7.0 / 8.0;
}
static void unfolded_positions(const std::vector<double>& z, std::vector<double>& pos) {
    pos.clear();
    for (double t : z) pos.push_back(smooth_counting_function(t));
}

static double number_variance(const std::vector<double>& pos, double L,
                              int n_windows, MT19937& rng) {
    double Ltot = pos.back() - pos.front();
    if (Ltot <= L) return std::nan("");
    std::vector<double> counts(n_windows);
    for (int w = 0; w < n_windows; ++w) {
        double x0 = pos.front() + rng.random() * (Ltot - L);
        long lo = (long)(std::lower_bound(pos.begin(), pos.end(), x0) - pos.begin());
        long hi = (long)(std::lower_bound(pos.begin(), pos.end(), x0 + L) - pos.begin());
        counts[w] = (double)(hi - lo);
    }
    double mean = 0; for (double c : counts) mean += c; mean /= n_windows;
    double var = 0; for (double c : counts) var += (c - mean) * (c - mean);
    return var / (n_windows - 1);
}

static double delta3_rigidity(const std::vector<double>& pos, double L,
                              int n_windows, int n_grid, MT19937& rng) {
    double Ltot = pos.back() - pos.front();
    if (Ltot <= L) return std::nan("");
    std::vector<double> xs(n_grid);
    for (int i = 0; i < n_grid; ++i) xs[i] = L * (double)i / (n_grid - 1);
    double total = 0; int n_ok = 0;
    for (int w = 0; w < n_windows; ++w) {
        double x0 = pos.front() + rng.random() * (Ltot - L);
        long idx0 = (long)(std::lower_bound(pos.begin(), pos.end(), x0) - pos.begin());
        std::vector<double> Nv(n_grid);
        for (int gi = 0; gi < n_grid; ++gi) {
            long hi = (long)(std::lower_bound(pos.begin(), pos.end(), x0 + xs[gi]) - pos.begin());
            Nv[gi] = (double)(hi - idx0);
        }
        Linreg r = linreg(xs, Nv);
        double m2 = 0; for (double e : r.res) m2 += e * e;
        total += m2 / n_grid;
        n_ok++;
    }
    return total / n_ok;
}

// two-level form factor K(t) — verbatim (see gof.py)
static void compute_K_single_seed(const std::vector<double>& eigs,
                                  const std::vector<double>& tvals,
                                  std::vector<double>& K) {
    size_t n = eigs.size();
    K.assign(tvals.size(), 0.0);
    if (n < 10) return;
    std::vector<double> s(eigs);
    std::sort(s.begin(), s.end());
    int window = std::max(3, (int)std::lround((double)n * 0.05));
    std::vector<double> u(n, 0.0);
    for (size_t i = 1; i < n; ++i) {
        long i_lo = std::max(0L, (long)i - window);
        long i_hi = std::min((long)n - 1, (long)i + window);
        double dens = (double)(i_hi - i_lo + 1) / (s[i_hi] - s[i_lo] + 1e-12);
        u[i] = u[i-1] + (s[i] - s[i-1]) * dens;
    }
    double ms = (u.back() - u.front()) / (double)(n - 1);
    if (ms > 1e-12) for (double& v : u) v /= ms;
    for (size_t idx = 0; idx < tvals.size(); ++idx) {
        double t = tvals[idx];
        if (t == 0.0) { K[idx] = 0.0; continue; }
        double re = 0, im = 0;
        for (size_t k = 0; k < n; ++k) {
            double ph = 2 * PI * t * u[k];
            re += std::cos(ph); im += std::sin(ph);
        }
        K[idx] = std::max(0.0, (re*re + im*im) / (double)n);
    }
    int w = 3;  // smooth_window (callers use 3)
    if ((long)K.size() > 2 * w) {
        std::vector<double> Ks(K);
        for (size_t j = (size_t)w; j + w < K.size(); ++j) {
            if (tvals[j] < 0.5) continue;
            double acc = 0; int cnt = 0;
            for (int q = -w; q <= w; ++q) { acc += K[j + q]; cnt++; }
            Ks[j] = acc / cnt;
        }
        K = Ks;
    }
}
static void compute_K_form_factor(const std::vector<double>& eigs,
                                  const std::vector<double>& tvals,
                                  std::vector<double>& K) {
    compute_K_single_seed(eigs, tvals, K);
}

// ─────────────────────────────────────────────────────────────────────────────
// Lattice — AB-cloud Hofstadter Hamiltonian (see lattice.py)
// ─────────────────────────────────────────────────────────────────────────────
struct Vortex { double x, y, q; };

struct ABCloudConfig {
    int Nx, Ny;
    std::vector<Vortex> vortices;
    double alpha, t, W;
    std::string lattice;         // "open" | "torus"
    long disorder_seed = 96;
    std::string model;           // "monumental" | "dirac"
    ABCloudConfig(int nx, int ny, std::vector<Vortex> v, double a, double tt,
                  std::string lat, double w, long seed = 96,
                  std::string m = "monumental")
        : Nx(nx), Ny(ny), vortices(std::move(v)), alpha(a), t(tt),
          lattice(std::move(lat)), W(w), disorder_seed(seed), model(std::move(m)) {}
};

static double ab_phase_vortex_monumental(const double ri[2], const double rj[2],
                                         const std::vector<Vortex>& vort) {
    double phase = 0.0;
    for (const Vortex& vk : vort) {
        double dx1 = ri[0] - vk.x, dy1 = ri[1] - vk.y;
        double dx2 = rj[0] - vk.x, dy2 = rj[1] - vk.y;
        double a1 = (dx1 != 0 || dy1 != 0) ? std::atan2(dy1, dx1) : 0.0;
        double a2 = (dx2 != 0 || dy2 != 0) ? std::atan2(dy2, dx2) : 0.0;
        phase += vk.q * (a2 - a1) * 0.5;
    }
    return phase;
}

static double ab_phase_2d(const double ri[2], const double rj[2],
                          const double rk[2], double qk) {
    double ti = std::atan2(ri[1] - rk[1], ri[0] - rk[0]);
    double tj = std::atan2(rj[1] - rk[1], rj[0] - rk[0]);
    return qk * (ti - tj);
}

static double dirac_string_phase(const double ri[2], const double rj[2],
                                 const double rk[2], double qk,
                                 bool torus, int Nx) {
    if (std::fabs(ri[0] - rj[0]) > 1e-12) return 0.0;
    double y_lo = std::min(ri[1], rj[1]), y_hi = std::max(ri[1], rj[1]);
    if (!(y_lo < rk[1] && rk[1] < y_hi)) return 0.0;
    if (torus) {
        if (std::fabs(ri[0] - std::floor(rk[0])) < 0.5) return 0.0;
    } else {
        if (ri[0] <= rk[0]) return 0.0;
    }
    return ri[1] < rj[1] ? -2 * PI * qk : 2 * PI * qk;
}

static double ab_phase_2d_full(const double ri[2], const double rj[2],
                               const double rk[2], double qk, bool torus, int Nx) {
    return ab_phase_2d(ri, rj, rk, qk) +
           dirac_string_phase(ri, rj, rk, qk, torus, Nx);
}

static double vortex_onsite_potential(const double ri[2],
                                      const std::vector<Vortex>& vort,
                                      double W, long N, MT19937& rng) {
    if (vort.empty() && W == 0.0) return 0.0;
    double v = 0.0, ninv = 1.0 / (double)std::max<long>(N, 1);
    for (const Vortex& vk : vort) {
        double dx = ri[0] - vk.x, dy = ri[1] - vk.y;
        v += vk.q * W / ((dx*dx + dy*dy) * ninv + 1.0);
    }
    if (W > 0) v += (rng.random() - 0.5) * 0.02;
    return v;
}

static void build_ab_cloud_hamiltonian(const ABCloudConfig& cfg,
                                       std::vector<cd>& H) {
    int Nx = cfg.Nx, Ny = cfg.Ny;
    long N = (long)Nx * Ny;
    H.assign((size_t)N * N, cd(0.0, 0.0));
    bool torus = cfg.lattice == "torus";
    if (torus && std::fabs(cfg.alpha * Ny - std::round(cfg.alpha * Ny)) >= 1e-10) {
        std::fprintf(stderr, "ASSERT: torus needs alpha*Ny integer\n");
        std::exit(2);
    }
    MT19937 rng((uint32_t)cfg.disorder_seed);
    for (int iy = 1; iy <= Ny; ++iy) {
        for (int ix = 1; ix <= Nx; ++ix) {
            long i = (long)(iy - 1) * Nx + ix - 1;
            double ri[2] = {(double)ix, (double)iy};
            // right neighbour
            {
                int jx = ix + 1, jy = iy; bool wrap = false;
                if (jx > Nx) { if (torus) { jx = 1; wrap = true; } else jx = 0; }
                if (jx != 0) {
                    long j = (long)(jy - 1) * Nx + jx - 1;
                    double phi = 2 * PI * cfg.alpha * iy;
                    if (cfg.model == "dirac") {
                        double rjp[2] = {wrap ? (double)(Nx + 1) : (double)jx, (double)jy};
                        for (const Vortex& v : cfg.vortices) {
                            double rk[2] = {v.x, v.y};
                            phi += ab_phase_2d_full(ri, rjp, rk, v.q, torus, Nx);
                        }
                    }
                    cd hop = -cfg.t * std::exp(cd(0.0, phi));
                    H[i * N + j] += hop;
                    H[j * N + i] += std::conj(hop);
                }
            }
            // up neighbour
            {
                int jx = ix, jy = iy + 1; bool wrap = false;
                if (jy > Ny) { if (torus) { jy = 1; wrap = true; } else jy = 0; }
                if (jy != 0) {
                    long j = (long)(jy - 1) * Nx + jx - 1;
                    double phi = wrap ? 2 * PI * cfg.alpha * Ny : 0.0;
                    double rjp[2] = {(double)ix, (double)iy + 1};  // unwrapped top
                    if (cfg.model == "monumental") {
                        phi += ab_phase_vortex_monumental(ri, rjp, cfg.vortices);
                    } else {
                        for (const Vortex& v : cfg.vortices) {
                            double rk[2] = {v.x, v.y};
                            phi += ab_phase_2d_full(ri, rjp, rk, v.q, torus, Nx);
                        }
                    }
                    cd hop = -cfg.t * std::exp(cd(0.0, phi));
                    H[i * N + j] += hop;
                    H[j * N + i] += std::conj(hop);
                }
            }
            H[i * N + i] += vortex_onsite_potential(ri, cfg.vortices, cfg.W, N, rng);
        }
    }
    // Hermitian symmetrization (H + H†)/2
    for (long r = 0; r < N; ++r)
        for (long c = r + 1; c < N; ++c) {
            cd a = H[r * N + c], b = H[c * N + r];
            cd m = 0.5 * (a + std::conj(b));
            H[r * N + c] = m;
            H[c * N + r] = std::conj(m);
        }
}

// Cyclic Jacobi for complex Hermitian matrices → sorted real eigenvalues.
static void jacobi_eigvals(std::vector<cd> H, long N, std::vector<double>& ev) {
    const int MAX_SWEEPS = 60;
    double off_norm0 = 0.0;
    for (long r = 0; r < N; ++r)
        for (long c = r + 1; c < N; ++c) off_norm0 += std::norm(H[r * N + c]);
    double thresh = 1e-15 * std::sqrt(2.0 * off_norm0 + 1e-300);
    for (int sweep = 0; sweep < MAX_SWEEPS; ++sweep) {
        double off = 0.0;
        for (long r = 0; r < N; ++r)
            for (long c = r + 1; c < N; ++c) off += std::norm(H[r * N + c]);
        if (std::sqrt(2.0 * off) < thresh) break;
        for (long p = 0; p < N - 1; ++p) {
            for (long q = p + 1; q < N; ++q) {
                cd apq = H[p * N + q];
                if (std::abs(apq) <= thresh) continue;
                double app = H[p * N + p].real(), aqq = H[q * N + q].real();
                double tau = (aqq - app) / (2.0 * std::abs(apq));
                double t = (tau >= 0 ? 1.0 : -1.0) /
                           (std::fabs(tau) + std::sqrt(1.0 + tau * tau));
                double c = 1.0 / std::sqrt(1.0 + t * t);
                double s = t * c;  // normalized rotation (tan = t)
                cd phase = apq / std::abs(apq);           // e^{iφ}
                cd se = s * phase;                        // s·e^{iφ}
                cd sec = std::conj(se);
                // rows/cols p,q update: A' = G† A G
                for (long k = 0; k < N; ++k) {
                    if (k == p || k == q) continue;
                    cd akp = H[k * N + p], akq = H[k * N + q];
                    cd nkp = c * akp - sec * akq;
                    cd nkq = se * akp + c * akq;
                    H[k * N + p] = nkp; H[p * N + k] = std::conj(nkp);
                    H[k * N + q] = nkq; H[q * N + k] = std::conj(nkq);
                }
                double npp = app - t * std::abs(apq);
                double nqq = aqq + t * std::abs(apq);
                H[p * N + p] = cd(npp, 0.0);
                H[q * N + q] = cd(nqq, 0.0);
                H[p * N + q] = cd(0.0, 0.0);
                H[q * N + p] = cd(0.0, 0.0);
            }
        }
    }
    ev.resize(N);
    for (long r = 0; r < N; ++r) ev[r] = H[r * N + r].real();
    std::sort(ev.begin(), ev.end());
}

static void safe_eigvals(const std::vector<cd>& H, long N, std::vector<double>& ev) {
    jacobi_eigvals(H, N, ev);
}

// ─────────────────────────────────────────────────────────────────────────────
// §8 numpy/LAPACK tier: Jacobi WITH eigenvector accumulation + observables
// ─────────────────────────────────────────────────────────────────────────────

// Cyclic Jacobi for complex Hermitian matrices → (sorted eigenvalues, U)
// with H = U·diag(ev)·U†.  Same rotation sequence as jacobi_eigvals, plus
// column update U ← U·G (column-major storage U[j*N + k] = k-th component
// of eigenvector j).  Observables of this tier depend only on |ψ_i|, so the
// phase convention of the columns is irrelevant (PORT_SPEC §8.2).
static void jacobi_eig_full(std::vector<cd> H, long N, std::vector<double>& ev,
                            std::vector<cd>& U) {
    const int MAX_SWEEPS = 60;
    U.assign((size_t)N * N, cd(0.0, 0.0));
    for (long i = 0; i < N; ++i) U[(size_t)i * N + i] = cd(1.0, 0.0);
    double off_norm0 = 0.0;
    for (long r = 0; r < N; ++r)
        for (long c = r + 1; c < N; ++c) off_norm0 += std::norm(H[r * N + c]);
    double thresh = 1e-15 * std::sqrt(2.0 * off_norm0 + 1e-300);
    for (int sweep = 0; sweep < MAX_SWEEPS; ++sweep) {
        double off = 0.0;
        for (long r = 0; r < N; ++r)
            for (long c = r + 1; c < N; ++c) off += std::norm(H[r * N + c]);
        if (std::sqrt(2.0 * off) < thresh) break;
        for (long p = 0; p < N - 1; ++p) {
            for (long q = p + 1; q < N; ++q) {
                cd apq = H[p * N + q];
                if (std::abs(apq) <= thresh) continue;
                double app = H[p * N + p].real(), aqq = H[q * N + q].real();
                double tau = (aqq - app) / (2.0 * std::abs(apq));
                double t = (tau >= 0 ? 1.0 : -1.0) /
                           (std::fabs(tau) + std::sqrt(1.0 + tau * tau));
                double c = 1.0 / std::sqrt(1.0 + t * t);
                double s = t * c;  // normalized rotation (tan = t)
                cd phase = apq / std::abs(apq);           // e^{iφ}
                cd se = s * phase;                        // s·e^{iφ}
                cd sec = std::conj(se);
                for (long k = 0; k < N; ++k) {
                    if (k == p || k == q) continue;
                    cd akp = H[k * N + p], akq = H[k * N + q];
                    cd nkp = c * akp - sec * akq;
                    cd nkq = se * akp + c * akq;
                    H[k * N + p] = nkp; H[p * N + k] = std::conj(nkp);
                    H[k * N + q] = nkq; H[q * N + k] = std::conj(nkq);
                }
                double npp = app - t * std::abs(apq);
                double nqq = aqq + t * std::abs(apq);
                H[p * N + p] = cd(npp, 0.0);
                H[q * N + q] = cd(nqq, 0.0);
                H[p * N + q] = cd(0.0, 0.0);
                H[q * N + p] = cd(0.0, 0.0);
                // accumulate U ← U·G (columns p,q)
                for (long k = 0; k < N; ++k) {
                    cd ukp = U[(size_t)p * N + k], ukq = U[(size_t)q * N + k];
                    U[(size_t)p * N + k] = c * ukp - sec * ukq;
                    U[(size_t)q * N + k] = se * ukp + c * ukq;
                }
            }
        }
    }
    std::vector<double> diag(N);
    for (long r = 0; r < N; ++r) diag[r] = H[r * N + r].real();
    std::vector<long> idx(N);
    for (long i = 0; i < N; ++i) idx[i] = i;
    std::sort(idx.begin(), idx.end(), [&](long a, long b) { return diag[a] < diag[b]; });
    ev.resize(N);
    std::vector<cd> Us((size_t)N * N);
    for (long j = 0; j < N; ++j) {
        ev[j] = diag[idx[j]];
        for (long i = 0; i < N; ++i) Us[(size_t)j * N + i] = U[(size_t)idx[j] * N + i];
    }
    U.swap(Us);
}

// Julia round(Int, x) — round-half-to-EVEN (PORT_SPEC §8.4).
// 2.5→2, 3.5→4; forbidden: llround / floor(x+0.5).
static long round_half_even(double x) { return (long)std::nearbyint(x); }

// von_neumann_entropy 1:1 (Monumental V77): rank-1 C_A = ψ_A ψ_A†, clamps
// [1e-12, 1−1e-12], natural log.  psi = L·L components (column-major grid:
// column c = psi[c*L .. c*L+L-1]); subsystem A = first L_A rows × all L cols.
static double vne_rank1(const std::vector<cd>& psi, int L, double frac) {
    long N = (long)L * L;
    long LA = round_half_even((double)L * frac);
    if (LA < 1) LA = 1;
    if (LA > L - 1) LA = L - 1;
    long nA = (long)L * LA;
    std::vector<cd> psiA((size_t)nA);
    for (int c = 0; c < L; ++c)
        for (long r = 0; r < LA; ++r)
            psiA[(size_t)c * LA + r] = psi[(size_t)c * L + r];
    std::vector<cd> CA((size_t)nA * nA);
    for (long i = 0; i < nA; ++i)
        for (long j = 0; j < nA; ++j)
            CA[(size_t)i * nA + j] = psiA[i] * std::conj(psiA[j]);
    std::vector<double> evA;
    jacobi_eigvals(CA, nA, evA);           // full Jacobi pass — no rank-1 shortcut
    double S = 0.0;
    for (long i = 0; i < nA; ++i) {
        double lam = evA[i];
        if (lam < 1e-12) lam = 1e-12;
        if (lam > 1.0 - 1e-12) lam = 1.0 - 1e-12;
        S += lam * std::log(lam) + (1.0 - lam) * std::log(1.0 - lam);
    }
    return -S;
}

// IPR of a state: Σᵢ (|ψᵢ|²)²
static double ipr_vec(const std::vector<cd>& psi) {
    double acc = 0.0;
    for (auto& z : psi) { double p2 = std::norm(z); acc += p2 * p2; }
    return acc;
}

// Least squares [b, 1]·x ≈ s via Householder QR (n×2) — PORT_SPEC §8.6.
// (Normal equations lose ~5 digits at cond ~5e4 and break the 1e-6 gate.)
static void lsfit2(const std::vector<double>& b, const std::vector<double>& s,
                   double& slope, double& intercept) {
    long n = (long)b.size();
    std::vector<double> A1(n, 1.0), rhs(s);
    double normx = 0.0;
    for (double v : b) normx += v * v;
    normx = std::sqrt(normx);
    if (normx == 0.0) {
        double m = 0; for (double v : s) m += v; m /= (double)n;
        slope = 0.0; intercept = m; return;
    }
    double alpha = (b[0] >= 0.0) ? -normx : normx;
    std::vector<double> v(n);
    v[0] = b[0] - alpha;
    for (long i = 1; i < n; ++i) v[i] = b[i];
    double vtv = 0.0; for (double vi : v) vtv += vi * vi;
    auto house = [&](std::vector<double>& x) {
        double dot = 0.0; for (long i = 0; i < n; ++i) dot += v[i] * x[i];
        double w = 2.0 * dot / vtv;
        for (long i = 0; i < n; ++i) x[i] -= w * v[i];
    };
    house(A1); house(rhs);
    // second reflection zeroes A1[2..n-1] via the ACTUAL subcolumn values
    double c1 = A1[1];
    double normy = 0.0;
    for (long i = 1; i < n; ++i) normy += A1[i] * A1[i];
    normy = std::sqrt(normy);
    if (normy == 0.0) {                    // constant b — columns collinear
        intercept = rhs[0] / alpha;
        slope = 0.0;
        return;
    }
    double alpha2 = (c1 >= 0.0) ? -normy : normy;
    std::vector<double> u((size_t)n - 1);
    u[0] = c1 - alpha2;
    for (long i = 2; i < n; ++i) u[i - 1] = A1[i];
    double utu = 0.0; for (double ui : u) utu += ui * ui;
    double dot = u[0] * rhs[1];
    for (long i = 2; i < n; ++i) dot += u[i - 1] * rhs[i];
    double w2 = 2.0 * dot / utu;
    rhs[1] -= w2 * u[0];
    for (long i = 2; i < n; ++i) rhs[i] -= w2 * u[i - 1];
    double r01 = A1[0];
    intercept = rhs[1] / alpha2;
    slope = (rhs[0] - r01 * intercept) / alpha;
}

// TEST 16 local-mean unfolding → KS (D, p) for a lattice central band.
// NOT normalized_spacings (that kernel is the ζ-specific von-Mangoldt form).
static void rh_band_ks(const std::vector<double>& central, double& D, double& p) {
    long n_c = (long)central.size();
    D = std::nan(""); p = std::nan("");
    if (n_c == 0) return;
    long win = round_half_even(0.05 * (double)n_c);
    if (win < 5) win = 5;
    std::vector<double> usp;
    for (long i = 0; i + 1 < n_c; ++i) {
        long j_lo = i - win; if (j_lo < 0) j_lo = 0;
        long j_hi = i + win; if (j_hi > n_c - 2) j_hi = n_c - 2;
        double acc = 0; long cnt = 0;
        for (long j = j_lo; j <= j_hi; ++j) { acc += central[j + 1] - central[j]; ++cnt; }
        double lm = acc / (double)cnt;
        if (lm > 1e-12) usp.push_back((central[i + 1] - central[i]) / lm);
    }
    std::vector<double> f;
    for (double s : usp) if (s > 0 && s < 10) f.push_back(s);
    if ((long)f.size() > 10) ks_test(f, D, p);
}

// §8 vector-tier orchestrator: eigen(H) + central 3 states + entropy/IPR
// + full 53-fraction TEE fit.  Fractions — verbatim list from Monumental V90.
struct HamTier {
    std::vector<double> ev;                // full sorted spectrum
    std::vector<std::vector<cd>> psi;      // 3 central eigenvectors
    std::vector<double> S;                 // 3 states × 3 fractions (0.25/0.5/0.75)
    std::vector<double> ipr;               // 3 states
    std::vector<double> S_mean, S_std;     // per fraction (53)
    std::vector<double> boundaries;        // L·f (53)
    double slope = 0.0, gamma_top = 0.0;
};

static const double TEE_FRACS[53] = {
    0.25, 0.35, 0.5, 0.65, 0.75, 0.76, 0.77, 0.78, 0.79, 0.80,
    0.81, 0.82, 0.83, 0.84, 0.85, 0.86, 0.87, 0.88, 0.89, 0.9,
    0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99, 1.0,
    2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 12.0,
    14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0, 36.0, 40.0, 44.0,
    48.0, 56.0, 64.0
};
static const double MON_FRACS[3] = {0.25, 0.5, 0.75};
// indices of 0.25/0.5/0.75 inside TEE_FRACS
static const long MON_TEE_IDX[3] = {0, 2, 4};

static void ham_tier_compute(const ABCloudConfig& cfg, int L, HamTier& T) {
    long N = (long)cfg.Nx * cfg.Ny;
    std::vector<cd> H;
    build_ab_cloud_hamiltonian(cfg, H);
    std::vector<cd> U;
    jacobi_eig_full(H, N, T.ev, U);
    double mean = 0.0;
    for (double e : T.ev) mean += e;
    mean /= (double)N;
    std::vector<std::pair<double, long>> ord;
    for (long i = 0; i < N; ++i) ord.push_back({std::fabs(T.ev[i] - mean), i});
    std::sort(ord.begin(), ord.end());     // distinct values (§8.3 guard in gen)
    for (int c = 0; c < 3; ++c) {
        long k = ord[c].second;
        std::vector<cd> psi(U.begin() + (size_t)k * N, U.begin() + (size_t)(k + 1) * N);
        T.psi.push_back(psi);
        T.ipr.push_back(ipr_vec(psi));
        for (int fi = 0; fi < 3; ++fi)
            T.S.push_back(vne_rank1(psi, L, MON_FRACS[fi]));
    }
    T.S_mean.resize(53); T.S_std.resize(53);
    T.boundaries.resize(53);
    for (int fi = 0; fi < 53; ++fi) {
        double v0 = vne_rank1(T.psi[0], L, TEE_FRACS[fi]);
        double v1 = vne_rank1(T.psi[1], L, TEE_FRACS[fi]);
        double v2 = vne_rank1(T.psi[2], L, TEE_FRACS[fi]);
        double m = (v0 + v1 + v2) / 3.0;
        T.S_mean[fi] = m;
        T.S_std[fi] = std::sqrt(((v0 - m) * (v0 - m) + (v1 - m) * (v1 - m) +
                                 (v2 - m) * (v2 - m)) / 2.0);   // sample std, n−1
        T.boundaries[fi] = (double)L * TEE_FRACS[fi];
    }
    double intercept;
    lsfit2(T.boundaries, T.S_mean, T.slope, intercept);
    T.gamma_top = -intercept;
}


static double plaquette_flux(const std::vector<cd>& H, int Nx, int Ny,
                             int ix, int iy, bool torus = false) {
    int ix_r = torus ? (ix % Nx) + 1 : ix + 1;
    int iy_t = torus ? (iy % Ny) + 1 : iy + 1;
    long i_bl = (long)(iy - 1) * Nx + ix - 1;
    long i_br = (long)(iy - 1) * Nx + ix_r - 1;
    long i_tr = (long)(iy_t - 1) * Nx + ix_r - 1;
    long i_tl = (long)(iy_t - 1) * Nx + ix - 1;
    long N = (long)Nx * Ny;
    double fb = std::arg(-H[i_br * N + i_bl]);
    double fr = std::arg(-H[i_tr * N + i_br]);
    double ft = std::arg(-H[i_tl * N + i_tr]);
    double fl = std::arg(-H[i_bl * N + i_tl]);
    return fb + fr + ft + fl;
}
static double flux_circdist(double a, double b) {
    double m = std::fmod(a - b + PI, 2 * PI);
    if (m < 0) m += 2 * PI;
    return std::fabs(m - PI);
}

static void central_band_eigs(const std::vector<double>& s, double frac,
                              std::vector<double>& out) {
    out.clear();
    long n = (long)s.size();
    if (n == 0) return;
    frac = std::min(std::max(frac, 0.05), 1.0);
    if (frac >= 1.0) { out = s; return; }
    long half = (long)std::floor((double)n * frac / 2.0);
    long j_lo = std::max(1L, n / 2 - half);
    long j_hi = std::min(n, n / 2 + half);
    for (long j = j_lo; j <= j_hi; ++j) out.push_back(s[j - 1]);
}

static double chiral_symmetry_defect(const std::vector<cd>& H, int Nx, int Ny) {
    long N = (long)Nx * Ny;
    double norm_h = 0.0, num = 0.0;
    // ||S·H·S + H||_F / ||H||_F — computed streaming (no S matrix needed)
    for (long r = 0; r < N; ++r) {
        int sr = (((r % Nx) + 1) + (r / Nx + 1)) % 2 == 0 ? 1 : -1;
        for (long c = 0; c < N; ++c) {
            int sc = (((c % Nx) + 1) + (c / Nx + 1)) % 2 == 0 ? 1 : -1;
            cd v = (double)(sr * sc) * H[r * N + c] + H[r * N + c];
            num += std::norm(v);
            norm_h += std::norm(H[r * N + c]);
        }
    }
    return std::sqrt(num) / std::max(std::sqrt(norm_h), 1e-30);
}

static bool verify_hermitian(const std::vector<cd>& H, long N) {
    double max_err = 0.0, norm_m = 0.0;
    for (long r = 0; r < N; ++r)
        for (long c = 0; c < N; ++c) {
            norm_m += std::norm(H[r * N + c]);
            max_err = std::max(max_err, std::abs(H[r * N + c] - std::conj(H[c * N + r])));
        }
    return max_err / std::max(std::sqrt(norm_m), 1e-30) < 1e-12;
}
static double time_reversal_asymmetry(const std::vector<cd>& H, long N) {
    double diff = 0.0, norm_m = 0.0;
    for (size_t k = 0; k < H.size(); ++k) {
        norm_m += std::norm(H[k]);
        diff += std::norm(H[k] - std::conj(H[k]));
    }
    return std::sqrt(diff) / std::max(std::sqrt(norm_m), 1e-30);
}

// ─────────────────────────────────────────────────────────────────────────────
// Minimal JSON reader for the golden file (objects of numbers/strings/arrays)
// ─────────────────────────────────────────────────────────────────────────────
struct JsonValue;
using JsonObject = std::map<std::string, JsonValue>;
struct JsonValue {
    enum Type { OBJ, ARR, NUM, STR, BOOL, NUL } type = NUL;
    JsonObject obj;
    std::vector<JsonValue> arr;
    double num = 0.0;
    std::string str;
    bool b = false;
};

struct JsonParser {
    const char* p;
    explicit JsonParser(const char* s) : p(s) {}
    void ws() { while (*p == ' ' || *p == '\n' || *p == '\r' || *p == '\t') ++p; }
    [[noreturn]] void fail(const char* m) {
        std::fprintf(stderr, "JSON parse error: %s near: %.20s\n", m, p);
        std::exit(2);
    }
    JsonValue parse() {
        JsonValue v;
        ws();
        if (*p == '{') { v.type = JsonValue::OBJ; ++p;
            ws();
            if (*p == '}') { ++p; return v; }
            while (true) {
                ws();
                if (*p != '"') fail("expected key");
                std::string key = parse_string();
                ws();
                if (*p != ':') fail("expected :");
                ++p;
                v.obj[key] = parse();
                ws();
                if (*p == ',') { ++p; continue; }
                if (*p == '}') { ++p; break; }
                fail("expected , or }");
            }
            return v;
        }
        if (*p == '[') { v.type = JsonValue::ARR; ++p;
            ws();
            if (*p == ']') { ++p; return v; }
            while (true) {
                v.arr.push_back(parse());
                ws();
                if (*p == ',') { ++p; continue; }
                if (*p == ']') { ++p; break; }
                fail("expected , or ]");
            }
            return v;
        }
        if (*p == '"') { v.type = JsonValue::STR; v.str = parse_string(); return v; }
        if (strncmp(p, "true", 4) == 0) { v.type = JsonValue::BOOL; v.b = true; p += 4; return v; }
        if (strncmp(p, "false", 5) == 0) { v.type = JsonValue::BOOL; v.b = false; p += 5; return v; }
        if (strncmp(p, "null", 4) == 0) { v.type = JsonValue::NUL; p += 4; return v; }
        // number
        char* end = nullptr;
        double d = std::strtod(p, &end);
        if (end == p) fail("bad value");
        v.type = JsonValue::NUM; v.num = d; p = end;
        return v;
    }
    std::string parse_string() {
        ++p;  // opening quote
        std::string out;
        while (*p && *p != '"') {
            if (*p == '\\' && p[1]) {
                char c = p[1];
                if (c == 'n') out += '\n';
                else if (c == 't') out += '\t';
                else if (c == 'r') out += '\r';
                else if (c == '"') out += '"';
                else if (c == '\\') out += '\\';
                else if (c == '/') out += '/';
                else if (c == 'u') {
                    // \uXXXX → UTF-8 (basic plane)
                    unsigned code = (unsigned)std::strtol(std::string(p + 2, 4).c_str(), nullptr, 16);
                    if (code < 0x80) out += (char)code;
                    else if (code < 0x800) {
                        out += (char)(0xC0 | (code >> 6));
                        out += (char)(0x80 | (code & 0x3F));
                    } else {
                        out += (char)(0xE0 | (code >> 12));
                        out += (char)(0x80 | ((code >> 6) & 0x3F));
                        out += (char)(0x80 | (code & 0x3F));
                    }
                    p += 4;
                }
                p += 2;
            } else out += *p++;
        }
        if (*p == '"') ++p;
        return out;
    }
};

// ─────────────────────────────────────────────────────────────────────────────
// Golden selftest — compute_all (1:1 with gen_golden.jl / golden.py)
// ─────────────────────────────────────────────────────────────────────────────
struct Result {
    std::map<std::string, std::map<std::string, double>> sec;
    std::vector<double> tvals, omega;
};

static void load_zeros(const std::string& path, std::vector<double>& z) {
    std::ifstream f(path);
    if (!f) { std::fprintf(stderr, "ERROR: cannot open zeros file: %s\n", path.c_str()); std::exit(2); }
    double v;
    while (f >> v) z.push_back(v);
    std::sort(z.begin(), z.end());
}

// Julia string(Float64) semantics: shortest round-trip repr, always with a
// decimal point (1.0 → "1.0", 0.05 → "0.05"). Used for golden key names.
static std::string shortest(double v) {
    char buf[64];
    // pass 1: shortest fixed-notation round-trip (Julia/Python repr style)
    for (int prec = 1; prec <= 17; ++prec) {
        snprintf(buf, 64, "%.*g", prec, v);
        if (!strchr(buf, 'e') && strtod(buf, nullptr) == v) {
            std::string s(buf);
            if (s.find('.') == std::string::npos
                && s.find('n') == std::string::npos && s.find('i') == std::string::npos)
                s += ".0";
            return s;
        }
    }
    // pass 2: allow exponent form
    for (int prec = 1; prec <= 17; ++prec) {
        snprintf(buf, 64, "%.*g", prec, v);
        if (strtod(buf, nullptr) == v) return std::string(buf);
    }
    snprintf(buf, 64, "%.17g", v);
    return std::string(buf);
}

// forward declarations (defined below compute_all)
static double tvals_envelope(double t);
static std::vector<double> hp_unfold_local(const std::vector<double>& eigs,
                                           double win_frac = 0.05);
static double hp_aicc(int n, double rss, int k);
static void hp_wald_ci(int k, int n, double& p, double& lo, double& hi);
static std::vector<double> rankdata(const std::vector<double>& x);
static double pearson_cor(const std::vector<double>& x, const std::vector<double>& y);

static void compute_all(const std::vector<double>& zeta, const JsonValue& golden,
                        Result& R) {
    auto& sec = R.sec;
    // 1. Lambert W / Gram points
    { double xs[] = {0.5, 1.0, 3.7, 10.0, 271.8, 12345.6};
      for (double x : xs) sec["lambert_w"]["x=" + shortest(x)] = lambert_w(x); }
    { long ns[] = {1, 2, 3, 10, 100, 1000, 10000, 50000};
      char k[64];
      for (long n : ns) { snprintf(k, 64, "n=%ld", n); sec["gram_point"][k] = gram_point(n); } }
    // 2. b(N)
    { long ns[] = {100, 500, 1000, 5000, 10000, 50000};
      char k[64];
      for (long n : ns) { snprintf(k, 64, "N=%ld", n); sec["bN"][k] = compute_bN(zeta, n); }
      sec["bN"]["N=1000_off500"] = compute_bN(zeta, 1000, 500); }
    // 3. spacings
    std::vector<double> sp;
    normalized_spacings(zeta, sp);
    { double mean = 0; for (double s : sp) mean += s; mean /= sp.size();
      double var = 0; for (double s : sp) var += (s - mean) * (s - mean);
      var /= (sp.size() - 1);
      sec["spacings"]["n"] = (double)sp.size();
      sec["spacings"]["mean"] = mean;
      sec["spacings"]["var"] = var; }
    // 4. surmises / special
    { double ss[] = {0.05, 0.1, 0.25, 0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 4.9};
      for (double s : ss) {
          std::string k = "s=" + shortest(s);
          sec["gue2_cdf"][k] = gue2_surmise_cdf(s);
          sec["goe_cdf"][k] = goe_surmise_cdf(s);
          sec["gue2_pdf"][k] = gue2_surmise_pdf(s);
      }
      struct GP { double a, x; } gps[] = {{0.5,0.1},{0.5,2.0},{1.0,1.0},{2.0,3.0},{0.5,12.0}};
      for (auto& g : gps) sec["gamma_p"]["a=" + shortest(g.a) + "_x=" + shortest(g.x)] =
                               regularized_gamma_p(g.a, g.x);
      struct CX { double x, df; } cxs[] = {{3.84,1.0},{16.92,29.0},{25.0,10.0}};
      for (auto& c : cxs) sec["chi2_cdf"]["x=" + shortest(c.x) + "_df=" + shortest(c.df)] =
                                  chi2_cdf(c.x, c.df);
      double lams[] = {0.5, 1.3, 0.02};
      for (double lam : lams) sec["ks_pvalue"]["lam=" + shortest(lam)] =
                                      ks_asymptotic_pvalue(lam); }
    // 5. GOF
    { double D, p; ks_test(sp, D, p);
      sec["ks_zeros"]["D"] = D; sec["ks_zeros"]["p"] = p;
      sec["cvm_zeros"]["W2"] = cvm_test(sp);
      sec["ad_zeros"]["A2"] = anderson_darling_stat(sp);
      double chi2, pp; int df;
      chi2_gue_test(sp, 30, chi2, df, pp);
      sec["chi2_zeros"]["chi2"] = chi2; sec["chi2_zeros"]["df"] = (double)df;
      sec["chi2_zeros"]["p"] = pp;
      double r; long n_r;
      mean_adjacent_spacing_ratio(zeta, r, n_r);
      sec["rmean_zeros"]["r"] = r; sec["rmean_zeros"]["n_r"] = (double)n_r; }
    // 6. S2 / D3 — one classic MT19937(777) stream shared across S2→D3,
    // exactly like gen_golden.jl (rngS reused) and golden.py.
    std::vector<double> pos;
    unfolded_positions(zeta, pos);
    { MT19937 rng(777);
      double Ls[] = {5.0, 10.0, 20.0, 50.0, 100.0};
      for (double L : Ls) sec["S2"]["L=" + shortest(L)] = number_variance(pos, L, 3000, rng);
      double Ld[] = {5.0, 10.0, 20.0, 50.0};
      for (double L : Ld) sec["D3"]["L=" + shortest(L)] = delta3_rigidity(pos, L, 300, 300, rng); }
    // 7. K form factor
    { auto it = golden.obj.at("grids").obj.find("tvals");
      for (auto& v : it->second.arr) R.tvals.push_back(v.num);
      std::vector<double> K;
      compute_K_form_factor(zeta, R.tvals, K);
      for (size_t i = 0; i < R.tvals.size(); ++i) {
          double t = R.tvals[i];
          if (t == 0.2 || t == 0.5 || t == 1.0 || t == 2.0 || t == 3.0) {
              sec["K_zeros"]["t=" + shortest(t)] = K[i];
          }
      }
      double acc = 0; int cnt = 0;
      for (size_t i = 0; i < R.tvals.size(); ++i) {
          if (R.tvals[i] >= 0.3) {
              double e = tvals_envelope(R.tvals[i]);
              acc += (K[i] - e) * (K[i] - e); cnt++;
          }
      }
      sec["K_zeros"]["rms_env"] = std::sqrt(acc / cnt); }
    // 8. H1 ζ positive control
    { auto it = golden.obj.at("grids").obj.find("omega");
      for (auto& v : it->second.arr) R.omega.push_back(v.num);
      std::vector<double> zs(zeta.begin(), zeta.begin() + std::min<size_t>(zeta.size(), 20000));
      size_t n = zs.size();
      std::vector<double> w(n);
      for (size_t i = 0; i < n; ++i)
          w[i] = 0.5 * (1.0 - std::cos(2 * PI * (double)i / (double)std::max<size_t>(n - 1, 1)));
      double sw2 = 0; for (double wi : w) sw2 += wi * wi;
      std::vector<double> P(R.omega.size());
      for (size_t fi = 0; fi < R.omega.size(); ++fi) {
          double om = R.omega[fi], re = 0, im = 0;
          for (size_t i = 0; i < n; ++i) {
              re += w[i] * std::cos(om * zs[i]);
              im -= w[i] * std::sin(om * zs[i]);
          }
          P[fi] = (re * re + im * im) / sw2;
      }
      std::vector<double> Ps(P);
      std::sort(Ps.begin(), Ps.end());
      double med = (Ps.size() % 2 == 1) ? Ps[Ps.size()/2]
                                        : 0.5 * (Ps[Ps.size()/2 - 1] + Ps[Ps.size()/2]);
      sec["h1_zeta"]["median"] = med;
      int primes[] = {2, 3, 5, 7, 11, 13};
      char k[64];
      for (int pr : primes) {
          double tgt = std::log((double)pr);
          size_t best = 0; double bd = 1e300;
          for (size_t i = 0; i < R.omega.size(); ++i) {
              double d = std::fabs(R.omega[i] - tgt);
              if (d < bd) { bd = d; best = i; }
          }
          snprintf(k, 64, "snr_log%d", pr);
          sec["h1_zeta"][k] = P[best] / med;
      } }
    // 9. Hamiltonian goldens
    auto eigs_of = [](ABCloudConfig cfg, std::vector<double>& ev) {
        std::vector<cd> H;
        build_ab_cloud_hamiltonian(cfg, H);
        safe_eigvals(H, (long)cfg.Nx * cfg.Ny, ev);
    };
    { std::vector<double> ev;
      eigs_of(ABCloudConfig(8, 8, {}, 0.5, 1.0, "open", 0.0, 96, "monumental"), ev);
      auto& d = sec["ham_L8_open_a05_clean"];
      d["eig1"] = ev[0]; d["eig2"] = ev[1]; d["eig3"] = ev[2];
      d["eigmid"] = ev[ev.size()/2 - 1];
      // Julia: for k in 0:2 put!("eigend$(3-k)", ev[n-k]) → eigend3 = max
      d["eigend1"] = ev[ev.size()-3]; d["eigend2"] = ev[ev.size()-2]; d["eigend3"] = ev[ev.size()-1]; }
    { std::vector<double> ev;
      eigs_of(ABCloudConfig(8, 8, {{3.5,3.5,1.0},{6.5,6.5,-1.0}}, 0.25, 1.0, "open",
                            0.0, 96, "monumental"), ev);
      auto& d = sec["ham_L8_open_a025_2vort"];
      d["eig1"] = ev[0]; d["eig2"] = ev[1]; d["eig3"] = ev[2];
      d["eigmid"] = ev[ev.size()/2 - 1];
      // Julia: for k in 0:2 put!("eigend$(3-k)", ev[n-k]) → eigend3 = max
      d["eigend1"] = ev[ev.size()-3]; d["eigend2"] = ev[ev.size()-2]; d["eigend3"] = ev[ev.size()-1]; }
    { std::vector<double> ev;
      eigs_of(ABCloudConfig(10, 10, {}, 0.2, 1.0, "torus", 0.0, 96, "monumental"), ev);
      auto& d = sec["ham_L10_torus_a02_clean"];
      d["eig1"] = ev[0]; d["eig2"] = ev[1]; d["eig3"] = ev[2];
      d["eigmid"] = ev[ev.size()/2 - 1];
      // Julia: for k in 0:2 put!("eigend$(3-k)", ev[n-k]) → eigend3 = max
      d["eigend1"] = ev[ev.size()-3]; d["eigend2"] = ev[ev.size()-2]; d["eigend3"] = ev[ev.size()-1]; }
    // 9d Byers–Yang (:dirac)
    { std::vector<double> e1, e2;
      eigs_of(ABCloudConfig(8, 8, {{3.5,3.5,1.0},{6.5,6.5,-1.0}}, 0.3, 1.0, "open",
                            0.0, 96, "dirac"), e1);
      eigs_of(ABCloudConfig(8, 8, {{3.5,3.5,2.0},{6.5,6.5,0.0}}, 0.3, 1.0, "open",
                            0.0, 96, "dirac"), e2);
      double d = 0; for (size_t i = 0; i < e1.size(); ++i) d = std::max(d, std::fabs(e1[i]-e2[i]));
      sec["byers_yang"]["L8_max_diff"] = d; }
    // 9e Connes (relative L² defect, W=0)
    { std::vector<double> ea, eb;
      eigs_of(ABCloudConfig(12, 12, {}, 0.5, 1.0, "open", 0.0), ea);
      eigs_of(ABCloudConfig(12, 12, {}, 2.0, 1.0, "open", 0.0), eb);
      double na = 0, nb = 0;
      for (size_t i = 0; i < ea.size(); ++i) { na += ea[i]*ea[i]; nb += (ea[i]-eb[i])*(ea[i]-eb[i]); }
      sec["connes"]["L12_a05_defect_W0"] = std::sqrt(nb) / std::max(std::sqrt(na), 1e-30); }
    // 9f chiral
    { std::vector<cd> H;
      build_ab_cloud_hamiltonian(ABCloudConfig(12, 12, {}, 0.5, 1.0, "open", 0.0, 96, "monumental"), H);
      sec["chiral"]["L12_a05_defect"] = chiral_symmetry_defect(H, 12, 12); }
    // 9g Dirac flux (:dirac)
    { std::vector<cd> H;
      build_ab_cloud_hamiltonian(ABCloudConfig(8, 8, {{3.5,3.5,1.0}}, 0.25, 1.0, "open",
                                              0.0, 96, "dirac"), H);
      double maxdev = 0;
      for (int iy = 1; iy <= 7; ++iy)
          for (int ix = 1; ix <= 7; ++ix) {
              double flux = plaquette_flux(H, 8, 8, ix, iy);
              double tgt = 2 * PI * 0.25 + ((ix == 3 && iy == 3) ? 2 * PI : 0.0);
              maxdev = std::max(maxdev, flux_circdist(flux, tgt));
          }
      sec["dirac_flux"]["L8_max_dev"] = maxdev; }
    // 10. unfold / linreg / aicc / wald / spearman
    { std::vector<double> zs(zeta.begin(), zeta.begin() + 2000);
      std::vector<double> u = hp_unfold_local(zs);
      sec["unfold"]["u2"] = u[1]; sec["unfold"]["u1000"] = u[999]; sec["unfold"]["u2000"] = u[1999]; }
    { std::vector<double> x, y;
      for (int i = 1; i <= 20; ++i) { x.push_back((double)i);
          y.push_back(2.0 + 0.5 * i + 0.1 * std::sin((double)i)); }
      Linreg r = linreg(x, y);
      sec["linreg"]["a"] = r.a; sec["linreg"]["b"] = r.b; sec["linreg"]["R2"] = r.R2; }
    sec["aicc"]["n40_rss10_k3"] = hp_aicc(40, 10.0, 3);
    { double p, lo, hi; hp_wald_ci(7, 20, p, lo, hi);
      sec["wald"]["p"] = p; sec["wald"]["lo"] = lo; sec["wald"]["hi"] = hi; }
    { double xr[] = {1,2,3,4,5,6,7,8}, yr[] = {1.1,2.3,2.9,4.2,5.1,5.8,7.2,7.9};
      std::vector<double> x(xr, xr+8), y(yr, yr+8);
      sec["spearman"]["xy"] = pearson_cor(rankdata(x), rankdata(y)); }
    // 11. test11
    { std::vector<double> sp2;
      normalized_spacings(zeta, sp2);
      sec["test11"]["A2_full"] = anderson_darling_stat(sp2); }
    // 12. numpy/LAPACK tier (PORT_SPEC §8): mon_entropy / topo_tee / rh_metrics
    { struct Scn { const char* name; ABCloudConfig cfg; int L; };
      std::vector<Scn> scns = {
          {"L8_open_a025_2vort", ABCloudConfig(8, 8, {{3.5, 3.5, 1.0}, {6.5, 6.5, -1.0}},
                                               0.25, 1.0, "open", 0.0, 96, "monumental"), 8},
          {"L10_open_a03_clean", ABCloudConfig(10, 10, {}, 0.3, 1.0, "open", 0.0, 96, "monumental"), 10},
          {"L12_open_a03_clean", ABCloudConfig(12, 12, {}, 0.3, 1.0, "open", 0.0, 96, "monumental"), 12},
      };
      for (auto& scn : scns) {
          HamTier T;
          ham_tier_compute(scn.cfg, scn.L, T);
          std::string sn = scn.name;
          for (int c = 0; c < 3; ++c) {
              for (int fi = 0; fi < 3; ++fi)
                  sec["mon_entropy"][sn + "_c" + std::to_string(c) + "_f" +
                                     shortest(MON_FRACS[fi])] = T.S[(size_t)c * 3 + fi];
              sec["mon_entropy"][sn + "_ipr_c" + std::to_string(c)] = T.ipr[c];
          }
          sec["topo_tee"][sn + "_slope_alpha"] = T.slope;
          sec["topo_tee"][sn + "_gamma_top"] = T.gamma_top;
          for (int fi = 0; fi < 3; ++fi)
              sec["topo_tee"][sn + "_S_mean_f" + shortest(MON_FRACS[fi])] =
                  T.S_mean[MON_TEE_IDX[fi]];
          sec["topo_tee"][sn + "_S_std_f0.5"] = T.S_std[MON_TEE_IDX[1]];
          std::vector<double> cb;
          central_band_eigs(T.ev, 0.6, cb);
          double D, p; rh_band_ks(cb, D, p);
          double r; long ncb;
          mean_adjacent_spacing_ratio(cb, r, ncb);
          sec["rh_metrics"][sn + "_D"] = D;
          sec["rh_metrics"][sn + "_p"] = p;
          sec["rh_metrics"][sn + "_r"] = r;
          sec["rh_metrics"][sn + "_n_cb"] = (double)ncb;
      } }
}

static double tvals_envelope(double t) {  // hp_kgue_envelope
    if (t < 1.0) {
        double x = 2 * PI * t;
        double sn = std::fabs(x) < 1e-12 ? 1.0 : std::sin(x) / x;
        return t * (1.0 - sn);
    }
    return 1.0;
}

static std::vector<double> hp_unfold_local(const std::vector<double>& eigs,
                                           double win_frac) {
    std::vector<double> s(eigs);
    std::sort(s.begin(), s.end());
    size_t n = s.size();
    if (n < 10) { std::vector<double> u(n); for (size_t i = 0; i < n; ++i) u[i] = (double)i; return u; }
    int window = std::max(3, (int)std::lround((double)n * win_frac));
    std::vector<double> u(n, 0.0);
    for (size_t i = 1; i < n; ++i) {
        long i_lo = std::max(0L, (long)i - window);
        long i_hi = std::min((long)n - 1, (long)i + window);
        double dens = (double)(i_hi - i_lo + 1) / (s[i_hi] - s[i_lo] + 1e-12);
        u[i] = u[i-1] + (s[i] - s[i-1]) * dens;
    }
    double ms = (u.back() - u.front()) / (double)std::max<long>((long)n - 1, 1);
    if (ms > 1e-12) for (double& v : u) v /= ms;
    return u;
}
static double hp_aicc(int n, double rss, int k) {
    int denom = n - k - 1;
    double aic = n * std::log(std::max(rss, 1e-300) / n) + 2.0 * k;
    return denom > 0 ? aic + 2.0 * k * (k + 1) / denom : aic;
}
static void hp_wald_ci(int k, int n, double& p, double& lo, double& hi) {
    if (n == 0) { p = lo = hi = 0.0; return; }
    p = (double)k / n;
    double h = 1.96 * std::sqrt(p * (1 - p) / n);
    lo = std::min(std::max(p - h, 0.0), 1.0);
    hi = std::min(std::max(p + h, 0.0), 1.0);
}
static std::vector<double> rankdata(const std::vector<double>& x) {
    size_t n = x.size();
    std::vector<size_t> ord(n);
    for (size_t i = 0; i < n; ++i) ord[i] = i;
    std::sort(ord.begin(), ord.end(), [&](size_t a, size_t b){ return x[a] < x[b]; });
    std::vector<double> ranks(n);
    size_t i = 0;
    while (i < n) {
        size_t j = i;
        while (j + 1 < n && x[ord[j+1]] == x[ord[i]]) ++j;
        double avg = ((double)i + (double)j) / 2.0 + 1.0;
        for (size_t k2 = i; k2 <= j; ++k2) ranks[ord[k2]] = avg;
        i = j + 1;
    }
    return ranks;
}
static double pearson_cor(const std::vector<double>& x, const std::vector<double>& y) {
    size_t n = x.size();
    double mx = 0, my = 0;
    for (size_t i = 0; i < n; ++i) { mx += x[i]; my += y[i]; }
    mx /= n; my /= n;
    double sxy = 0, sxx = 0, syy = 0;
    for (size_t i = 0; i < n; ++i) {
        sxy += (x[i]-mx)*(y[i]-my);
        sxx += (x[i]-mx)*(x[i]-mx);
        syy += (y[i]-my)*(y[i]-my);
    }
    if (sxx <= 0 || syy <= 0) return std::nan("");
    return sxy / std::sqrt(sxx * syy);
}

static void run_selftest(const std::vector<double>& zeta, const std::string& golden_path) {
    std::ifstream f(golden_path);
    if (!f) { std::fprintf(stderr, "ERROR: golden file not found: %s\n", golden_path.c_str()); std::exit(2); }
    std::stringstream ss; ss << f.rdbuf();
    std::string src = ss.str();
    JsonParser jp(src.c_str());
    JsonValue golden = jp.parse();

    Result R;
    compute_all(zeta, golden, R);

    // tolerances: (rtol, atol) — same table as golden.py
    std::map<std::string, std::pair<double,double>> TOL = {
        {"lambert_w", {1e-9, 0}}, {"gram_point", {1e-9, 0}}, {"bN", {1e-9, 0}},
        {"spacings", {1e-9, 0}}, {"gue2_cdf", {1e-7, 0}}, {"goe_cdf", {1e-9, 0}},
        {"gue2_pdf", {1e-9, 0}}, {"gamma_p", {1e-7, 0}}, {"chi2_cdf", {1e-7, 0}},
        {"ks_pvalue", {1e-9, 0}}, {"ks_zeros", {1e-6, 0}}, {"cvm_zeros", {1e-6, 0}},
        {"ad_zeros", {1e-6, 0}}, {"chi2_zeros", {1e-6, 0}}, {"rmean_zeros", {1e-9, 0}},
        {"S2", {1e-7, 1e-12}}, {"D3", {1e-7, 1e-12}}, {"K_zeros", {1e-6, 0}},
        {"h1_zeta", {1e-6, 0}}, {"ham_L8_open_a05_clean", {1e-7, 1e-8}},
        {"ham_L8_open_a025_2vort", {1e-7, 1e-8}}, {"ham_L10_torus_a02_clean", {1e-7, 1e-8}},
        {"byers_yang", {1e-6, 1e-10}}, {"connes", {1e-5, 1e-8}},
        {"chiral", {1e-5, 1e-9}}, {"dirac_flux", {1e-6, 1e-10}},
        {"unfold", {1e-8, 0}}, {"linreg", {1e-8, 0}}, {"aicc", {1e-8, 0}},
        {"wald", {1e-9, 0}}, {"spearman", {1e-8, 0}}, {"test11", {1e-6, 0}},
        {"mon_entropy", {1e-6, 1e-10}}, {"topo_tee", {1e-6, 1e-10}},
        {"rh_metrics", {1e-7, 0}},
    };
    printf("==============================================================================\n");
    printf("ABCLOUD C++ PORT — GOLDEN SELFTEST\n");
    printf("==============================================================================\n");
    int n_ok = 0, n_all = 0;
    for (auto& [section, gsec] : golden.obj) {
        if (section == "meta" || section == "grids") continue;
        if (!R.sec.count(section)) {
            printf(" [FAIL] %-28s (section missing)\n", section.c_str());
            n_all++; continue;
        }
        auto tol = TOL.count(section) ? TOL[section] : std::make_pair(1e-6, 0.0);
        for (auto& [key, gv] : gsec.obj) {
            n_all++;
            if (gv.type != JsonValue::NUM || !R.sec[section].count(key)) {
                printf(" [FAIL] %-28s %-18s missing\n", section.c_str(), key.c_str());
                continue;
            }
            double cv = R.sec[section][key];
            double g = gv.num;
            bool ok;
            double err;
            if (g == 0.0 && cv == 0.0) { err = 0.0; ok = true; }
            else if (g == 0.0) { err = std::fabs(cv); ok = err <= tol.second + tol.first; }
            else {
                err = std::fabs(cv - g) / std::fabs(g);
                ok = err <= tol.first || std::fabs(cv - g) <= tol.second;
            }
            if (ok) n_ok++;
            printf(" [%s] %-28s %-18s g=%-22.17g p=%-22.17g rel=%.2e\n",
                   ok ? "PASS" : "FAIL", section.c_str(), key.c_str(), g, cv, err);
        }
    }
    printf("------------------------------------------------------------------------------\n");
    printf(" RESULT: %d/%d checks passed\n", n_ok, n_all);
    printf("==============================================================================\n");
    if (n_ok == n_all) printf("SELFTEST: PASS — C++ kernel matches the Julia golden references.\n");
    else printf("SELFTEST: FAIL\n");
}

// suite helpers (defined in PART5)
static bool filter_all(const std::string& filter, int tid);
static std::string join_nums(const std::vector<double>& v);
static double gauss(MT19937& rng);
static double ks2(const std::vector<double>& a, const std::vector<double>& b);
static std::vector<double> unit_spacings(const std::vector<double>& u);

// ─────────────────────────────────────────────────────────────────────────────
// Suite (portable subset — same 25 tests as suite.py)
// ─────────────────────────────────────────────────────────────────────────────
struct SuiteReport { int n_pass = 0, n_fail = 0, n_warn = 0, n_info = 0; };

static void verdict(SuiteReport& rep, const char* v, int tid, const char* title,
                    const std::vector<std::string>& lines) {
    const char* mark = strcmp(v, "PASS") == 0 ? "[PASS]" :
                       strcmp(v, "FAIL") == 0 ? "[FAIL]" :
                       strcmp(v, "WARN") == 0 ? "[WARN]" : "[INFO]";
    if (!strcmp(v, "PASS")) rep.n_pass++;
    else if (!strcmp(v, "FAIL")) rep.n_fail++;
    else if (!strcmp(v, "WARN")) rep.n_warn++;
    else rep.n_info++;
    printf("%s TEST %2d — %s\n", mark, tid, title);
    for (auto& l : lines) printf("%s\n", l.c_str());
}

static void loglog_fit(const std::vector<double>& xs, const std::vector<double>& ys,
                       double& slope, double& R2) {
    std::vector<double> lx, ly;
    for (double v : xs) lx.push_back(std::log(v));
    for (double v : ys) ly.push_back(std::log(v));
    Linreg r = linreg(lx, ly);
    slope = r.b; R2 = r.R2;
}

static void run_suite(const std::vector<double>& zeta, const std::string& filter) {
    printf("==============================================================================\n");
    printf("ABCLOUD SUITE (portable subset, C++)\n");
    printf("==============================================================================\n");
    SuiteReport rep;
    std::vector<double> sp;
    normalized_spacings(zeta, sp);

    std::vector<long> ladder = {100, 500, 1000, 5000, 10000, 50000};
    // 1
    if (filter_all(filter, 1)) {
        std::vector<double> vals;
        for (long N : ladder) vals.push_back(compute_bN(zeta, N));
        bool ok = std::isfinite(vals.back()) && vals.back() < vals.front();
        char buf[256];
        snprintf(buf, 256, "  b(50000) = %.6f (audit anchor 1.2126)", vals.back());
        verdict(rep, ok ? "PASS" : "FAIL", 1, "b(N) convergence table",
                {std::string("  ladder: ") + join_nums(vals), buf});
    }
    // 2
    if (filter_all(filter, 2)) {
        std::vector<double> vals;
        for (long N : ladder) vals.push_back(compute_bN(zeta, N));
        bool mono = true;
        for (size_t i = 0; i + 1 < vals.size(); ++i)
            if (vals[i+1] > vals[i] + 1e-9) mono = false;
        verdict(rep, mono ? "PASS" : "FAIL", 2, "b(N) monotonicity",
                {"  ladder: " + join_nums(vals)});
    }
    // 3
    if (filter_all(filter, 3)) {
        std::vector<double> vals;
        for (long N : ladder) vals.push_back(compute_bN(zeta, N));
        double slope, R2;
        loglog_fit(std::vector<double>(ladder.begin(), ladder.end()), vals, slope, R2);
        bool ok = (-1.5 < slope && slope < -0.05) && R2 > 0.9;
        char buf[192];
        snprintf(buf, 192, "  slope=%+.4f  R2=%.6f  (asymptotic -0.5 with 1/log T correction)", slope, R2);
        verdict(rep, ok ? "PASS" : "FAIL", 3, "b(N) convergence rate (power law)", {buf});
    }
    // 4,5
    if (filter_all(filter, 4)) {
        double D, p; ks_test(sp, D, p);
        char buf[192];
        snprintf(buf, 192, "  KS D=%.6f  p=%.3e  n=%zu  (effect-size gate D<0.10)", D, p, sp.size());
        verdict(rep, D < 0.10 ? "PASS" : "FAIL", 4, "GUE KS test (full range)", {buf});
    }
    if (filter_all(filter, 5)) {
        std::vector<double> z2(zeta.begin() + zeta.size()/2, zeta.end());
        std::vector<double> sp2; normalized_spacings(z2, sp2);
        double D, p; ks_test(sp2, D, p);
        char buf[192];
        snprintf(buf, 192, "  high-T half: D=%.6f  p=%.3e  n=%zu", D, p, sp2.size());
        verdict(rep, D < 0.10 ? "PASS" : "FAIL", 5, "GUE KS test (high-T half)", {buf});
    }
    // 6
    if (filter_all(filter, 6)) {
        double chi2, p; int df;
        chi2_gue_test(sp, 30, chi2, df, p);
        char buf[192];
        snprintf(buf, 192, "  chi2=%.2f  df=%d  p=%.3e  (bins=30; low p = finite-data GUE miss)", chi2, df, p);
        verdict(rep, "INFO", 6, "spacing chi2 histogram", {buf});
    }
    // 7
    if (filter_all(filter, 7)) {
        std::vector<long> tail = {5000, 10000, 50000};
        std::vector<double> vals;
        for (long N : tail) vals.push_back(compute_bN(zeta, N));
        double slope, R2;
        loglog_fit(std::vector<double>(tail.begin(), tail.end()), vals, slope, R2);
        bool ok = (-0.9 < slope && slope < -0.05) && R2 > 0.9;
        char buf[192];
        snprintf(buf, 192, "  tail slope=%+.4f  R2=%.6f  (1/log T flattens local slope)", slope, R2);
        verdict(rep, ok ? "PASS" : "FAIL", 7, "decay slope (large-T)", {buf});
    }
    // 8
    if (filter_all(filter, 8)) {
        std::vector<double> vals;
        for (long N : ladder) vals.push_back(compute_bN(zeta, N));
        std::vector<double> lx, ly;
        for (long N : ladder) lx.push_back(std::log((double)N));
        for (double v : vals) ly.push_back(std::log(v));
        Linreg r = linreg(lx, ly);
        double max_rel = 0;
        for (size_t i = 0; i < r.res.size(); ++i)
            max_rel = std::max(max_rel, std::fabs(r.res[i]) / std::max(std::fabs(ly[i]), 1e-12));
        char buf[160];
        snprintf(buf, 160, "  max |relative residual| = %.4f", max_rel);
        verdict(rep, max_rel < 0.2 ? "PASS" : "WARN", 8, "residual analysis of fit", {buf});
    }
    // 9
    if (filter_all(filter, 9)) {
        std::vector<double> base;
        for (long N : ladder) base.push_back(compute_bN(zeta, N));
        MT19937 rng(777);
        double lo = 1e9, hi = -1e9;
        for (int b = 0; b < 200; ++b) {
            std::vector<double> bs;
            for (double v : base) bs.push_back(v * std::sqrt(1.0 + 0.02 * (rng.random() - 0.5) * 2));
            std::vector<double> lb;
            for (long N : ladder) lb.push_back(std::log((double)N));
            for (double& v : bs) v = std::log(v);
            Linreg r = linreg(lb, bs);
            lo = std::min(lo, r.b); hi = std::max(hi, r.b);
        }
        bool ok = (-1.5 < lo) && (hi < -0.1);
        char buf[192];
        snprintf(buf, 192, "  bootstrap slope CI [%+.4f, %+.4f] (200 resamples, seed 777)", lo, hi);
        verdict(rep, ok ? "PASS" : "WARN", 9, "bootstrap CI for slope", {buf});
    }
    // 10
    if (filter_all(filter, 10)) {
        size_t half = zeta.size() / 2;
        std::vector<long> lad = {100, 500, 1000, 5000};
        std::vector<double> v1, v2;
        std::vector<double> zh2(zeta.begin() + half, zeta.end());
        for (long N : lad) { v1.push_back(compute_bN(zeta, N)); v2.push_back(compute_bN(zh2, N, (long)half)); }
        double s1, R1, s2, R2;
        loglog_fit(std::vector<double>(lad.begin(), lad.end()), v1, s1, R1);
        loglog_fit(std::vector<double>(lad.begin(), lad.end()), v2, s2, R2);
        bool mono = true;
        for (size_t i = 0; i + 1 < v1.size(); ++i)
            if (v1[i+1] > v1[i] + 1e-9 || v2[i+1] > v2[i] + 1e-9) mono = false;
        bool ok = mono && R1 > 0.85 && R2 > 0.85;
        char buf[320];
        snprintf(buf, 320, "  slopes %+.3f/%+.3f, R2 %.3f/%.3f; both monotone (height gap = documented 1/log T offset)", s1, s2, R1, R2);
        verdict(rep, ok ? "PASS" : "FAIL", 10, "cross-validation stability", {buf});
    }
    // 11
    if (filter_all(filter, 11)) {
        double A2 = anderson_darling_stat(sp);
        MT19937 rng(777);
        std::vector<double> mcbuf(sp.size());
        int count = 0;
        for (int it = 0; it < 200; ++it) {
            RMT.sample(rng, mcbuf);
            if (anderson_darling_stat(mcbuf) >= A2) count++;
        }
        double p_mc = (count + 1.0) / 201.0;
        char buf[224];
        snprintf(buf, 224, "  A2 = %.4f  law-exact MC p = %.4f (200 draws, seed 777)", A2, p_mc);
        verdict(rep, "INFO", 11, "Anderson-Darling (honest)", {buf,
                "  (tail-sensitive statistic; low MC p = honest GUE miss on low-T data)"});
    }
    // 12
    if (filter_all(filter, 12)) {
        // GUE matrix spectrum via the same Jacobi solver (N=200: no LAPACK in
        // the C++ port — Jacobi cost O(n^3); statistical test, size documented)
        int n_mat = 200;
        MT19937 rng(4242);
        std::vector<cd> H((size_t)n_mat * n_mat, cd(0, 0));
        for (int r = 0; r < n_mat; ++r) {
            H[(size_t)r * n_mat + r] = cd(gauss(rng), 0.0);
            for (int c = r + 1; c < n_mat; ++c) {
                cd h(gauss(rng) / std::sqrt(2.0), gauss(rng) / std::sqrt(2.0));
                H[(size_t)r * n_mat + c] = h;
                H[(size_t)c * n_mat + r] = std::conj(h);
            }
        }
        for (int r = 0; r < n_mat; ++r)
            for (int c = r; c < n_mat; ++c)
                H[(size_t)r * n_mat + c] *= 0.5 * (r == c ? 2.0 : 1.0);
        std::vector<cd> Hs((size_t)n_mat * n_mat, cd(0, 0));
        for (int r = 0; r < n_mat; ++r)
            for (int c = 0; c < n_mat; ++c)
                Hs[(size_t)r * n_mat + c] = 0.5 * (H[(size_t)r * n_mat + c] + std::conj(H[(size_t)c * n_mat + r]));
        std::vector<double> ev;
        safe_eigvals(Hs, n_mat, ev);
        std::vector<double> band(ev.begin() + n_mat/10, ev.begin() + 9 * n_mat / 10);
        std::vector<double> gp;
        double m = 0; for (size_t i = 0; i + 1 < band.size(); ++i) m += band[i+1] - band[i];
        m /= (band.size() - 1);
        for (size_t i = 0; i + 1 < band.size(); ++i) gp.push_back((band[i+1] - band[i]) / m);
        double D = ks2(sp, gp);
        char buf[192];
        snprintf(buf, 192, "  two-sample KS (zeta n=%zu vs GUE-matrix n=%zu): D=%.6f", sp.size(), gp.size(), D);
        verdict(rep, D < 0.10 ? "PASS" : "FAIL", 12, "two-sample KS vs GUE matrix", {buf});
    }
    // 13,14
    if (filter_all(filter, 13)) {
        std::vector<double> pos;
        unfolded_positions(zeta, pos);
        MT19937 rng(777);
        bool ok = true;
        std::vector<std::string> lines;
        double Ls[] = {5.0, 10.0, 20.0, 50.0};
        char buf[128];
        for (double L : Ls) {
            double s2 = number_variance(pos, L, 3000, rng);
            ok = ok && s2 < L;
            snprintf(buf, 128, "  S2(L=%5.1f) = %.4f   [Poisson %.1f]", L, s2, L);
            lines.push_back(buf);
        }
        lines.push_back("  gate: S2(L) << L (GUE rigidity)");
        verdict(rep, ok ? "PASS" : "FAIL", 13, "number variance S2(L)", lines);
    }
    if (filter_all(filter, 14)) {
        std::vector<double> pos;
        unfolded_positions(zeta, pos);
        MT19937 rng(777);
        bool ok = true;
        std::vector<std::string> lines;
        double Ls[] = {5.0, 10.0, 20.0, 50.0};
        char buf[128];
        for (double L : Ls) {
            double d3 = delta3_rigidity(pos, L, 300, 300, rng);
            ok = ok && d3 < L / 15.0;
            snprintf(buf, 128, "  D3(L=%5.1f) = %.4f   [Poisson %.4f]", L, d3, L / 15.0);
            lines.push_back(buf);
        }
        verdict(rep, ok ? "PASS" : "FAIL", 14, "spectral rigidity D3(L)", lines);
    }
    // 15,16
    if (filter_all(filter, 15)) {
        std::vector<cd> H;
        ABCloudConfig cfg(16, 16, {{4.5,4.5,1.0}}, 0.5, 1.0, "open", 0.0);
        build_ab_cloud_hamiltonian(cfg, H);
        bool herm = verify_hermitian(H, 256);
        double tau = time_reversal_asymmetry(H, 256);
        std::vector<double> ev;
        safe_eigvals(H, 256, ev);
        std::vector<double> band;
        central_band_eigs(ev, 0.6, band);
        double r; long n_r;
        mean_adjacent_spacing_ratio(band, r, n_r);
        char buf[224];
        snprintf(buf, 224, "  hermitian=%s  tau_TRB=%.3e  <r>(central 60%%)=%.4f (n_r=%ld)",
                 herm ? "true" : "false", tau, r, n_r);
        verdict(rep, (herm && tau > 1e-12) ? "PASS" : "FAIL", 15, "AB-cloud construction", {buf});
    }
    if (filter_all(filter, 16)) {
        std::vector<cd> H;
        ABCloudConfig cfg(24, 24, {{6.5,6.5,1.0},{17.5,17.5,-1.0}}, 0.5, 1.0, "open", 0.0);
        build_ab_cloud_hamiltonian(cfg, H);
        std::vector<double> ev;
        safe_eigvals(H, 576, ev);
        std::vector<double> band;
        central_band_eigs(ev, 0.6, band);
        double r; long n_r;
        mean_adjacent_spacing_ratio(band, r, n_r);
        bool ok = std::fabs(r - 0.5992) < 0.06;
        char buf[224];
        snprintf(buf, 224, "  <r> = %.4f vs GUE 0.5992 +/- 0.06 (n_r=%ld; L=24 finite-size band)", r, n_r);
        verdict(rep, ok ? "PASS" : "WARN", 16, "AB-cloud GUE classification", {buf});
    }
    // 17,18
    if (filter_all(filter, 17)) {
        std::vector<double> ea, eb;
        { std::vector<cd> H; ABCloudConfig c(12, 12, {}, 0.5, 1.0, "open", 0.0);
          build_ab_cloud_hamiltonian(c, H); safe_eigvals(H, 144, ea); }
        { std::vector<cd> H; ABCloudConfig c(12, 12, {}, 2.0, 1.0, "open", 0.0);
          build_ab_cloud_hamiltonian(c, H); safe_eigvals(H, 144, eb); }
        double na = 0, nb = 0;
        for (size_t i = 0; i < ea.size(); ++i) { na += ea[i]*ea[i]; nb += (ea[i]-eb[i])*(ea[i]-eb[i]); }
        char buf[192];
        snprintf(buf, 192, "  alpha<->1/alpha relative L2 defect (open 12x12, W=0) = %.6f", std::sqrt(nb)/std::sqrt(na));
        verdict(rep, "INFO", 17, "Connes self-duality", {buf,
                "  finite open lattice: duality is boundary-spoiled (documented)"});
    }
    if (filter_all(filter, 18)) {
        std::vector<cd> H, Hw;
        build_ab_cloud_hamiltonian(ABCloudConfig(12, 12, {}, 0.5, 1.0, "open", 0.0, 96, "monumental"), H);
        build_ab_cloud_hamiltonian(ABCloudConfig(12, 12, {}, 0.5, 1.0, "open", 4.0, 96, "monumental"), Hw);
        double d0 = chiral_symmetry_defect(H, 12, 12);
        double dw = chiral_symmetry_defect(Hw, 12, 12);
        char buf[224];
        snprintf(buf, 224, "  defect(W=0) = %.3e (gate <1e-10)   defect(W=4, honest breaker) = %.4f", d0, dw);
        verdict(rep, d0 < 1e-10 ? "PASS" : "FAIL", 18, "chiral AIII at alpha=1/2", {buf});
    }
    // 24,25,26
    if (filter_all(filter, 24)) {
        std::vector<cd> H;
        build_ab_cloud_hamiltonian(ABCloudConfig(8, 8, {{3.5,3.5,1.0}}, 0.25, 1.0, "open", 0.0, 96, "dirac"), H);
        double maxdev = 0;
        for (int iy = 1; iy <= 7; ++iy)
            for (int ix = 1; ix <= 7; ++ix) {
                double flux = plaquette_flux(H, 8, 8, ix, iy);
                double tgt = 2 * PI * 0.25 + ((ix == 3 && iy == 3) ? 2 * PI : 0.0);
                maxdev = std::max(maxdev, flux_circdist(flux, tgt));
            }
        char buf[160];
        snprintf(buf, 160, "  max circular deviation from 2*pa + 2*q = %.3e (:dirac model)", maxdev);
        verdict(rep, maxdev < 1e-9 ? "PASS" : "FAIL", 24, "Dirac-string flux", {buf});
    }
    if (filter_all(filter, 25)) {
        std::vector<double> e1, e2, e3;
        { std::vector<cd> H; ABCloudConfig c(16, 16, {{4.5,4.5,1.0},{11.5,11.5,-1.0}}, 0.3, 1.0, "open", 0.0, 96, "dirac");
          build_ab_cloud_hamiltonian(c, H); safe_eigvals(H, 256, e1); }
        { std::vector<cd> H; ABCloudConfig c(16, 16, {{4.5,4.5,2.0},{11.5,11.5,0.0}}, 0.3, 1.0, "open", 0.0, 96, "dirac");
          build_ab_cloud_hamiltonian(c, H); safe_eigvals(H, 256, e2); }
        { std::vector<cd> H; ABCloudConfig c(16, 16, {{4.5,4.5,0.3},{11.5,11.5,-0.3}}, 0.3, 1.0, "open", 0.0, 96, "dirac");
          build_ab_cloud_hamiltonian(c, H); safe_eigvals(H, 256, e3); }
        double d_int = 0, d_frac = 0;
        for (size_t i = 0; i < e1.size(); ++i) {
            d_int = std::max(d_int, std::fabs(e1[i]-e2[i]));
            d_frac = std::max(d_frac, std::fabs(e1[i]-e3[i]));
        }
        bool ok = d_int < 1e-9 && d_frac > 1e-4;
        char buf[256];
        snprintf(buf, 256, "  integer q->q+1: max|dE| = %.3e   fractional q=0.3 control: %.3e (must differ)", d_int, d_frac);
        verdict(rep, ok ? "PASS" : "FAIL", 25, "Byers-Yang theorem", {buf});
    }
    if (filter_all(filter, 26)) {
        std::vector<cd> H;
        build_ab_cloud_hamiltonian(ABCloudConfig(12, 12, {}, 0.25, 1.0, "torus", 0.0), H);
        double maxdev = 0;
        for (int iy = 1; iy <= 12; ++iy)
            for (int ix = 1; ix <= 12; ++ix)
                maxdev = std::max(maxdev,
                        flux_circdist(plaquette_flux(H, 12, 12, ix, iy, true), 2 * PI * 0.25));
        char buf[160];
        snprintf(buf, 160, "  torus 12x12 alpha=0.25: max flux deviation = %.3e", maxdev);
        verdict(rep, maxdev < 1e-9 ? "PASS" : "FAIL", 26, "PBC torus flux", {buf});
    }
    // 34
    if (filter_all(filter, 34)) {
        std::vector<cd> H;
        build_ab_cloud_hamiltonian(ABCloudConfig(28, 28,
                {{7.5,7.5,1.0},{20.5,20.5,-1.0}}, 0.5, 1.0, "open", 0.0, 96, "monumental"), H);
        std::vector<double> ev;
        safe_eigvals(H, 784, ev);
        std::vector<double> band;
        central_band_eigs(ev, 0.6, band);
        std::vector<double> u = hp_unfold_local(band);
        std::vector<double> absp = unit_spacings(u);
        std::vector<double> zs = unit_spacings(sp);
        double D = ks2(absp, zs);
        char buf[256];
        snprintf(buf, 256, "  DIRECT AB-cloud (L=28 alpha=0.5 monumental, 2 vortices, n=%zu) vs zeta: KS D=%.6f", absp.size(), D);
        verdict(rep, D < 0.10 ? "PASS" : "WARN", 34, "DIRECT AB-cloud vs zeta", {buf});
    }
    // 35
    if (filter_all(filter, 35)) {
        std::vector<double> tvals;
        for (int i = 1; i <= 30; ++i) tvals.push_back(0.1 * i);
        std::vector<double> K;
        compute_K_form_factor(zeta, tvals, K);
        double acc = 0; int cnt = 0;
        for (size_t i = 0; i < tvals.size(); ++i)
            if (tvals[i] >= 0.3) {
                double e = tvals_envelope(tvals[i]);
                acc += (K[i]-e)*(K[i]-e); cnt++;
            }
        double rms = std::sqrt(acc / cnt);
        char buf[192];
        snprintf(buf, 192, "  RMS(K - K_box) over t>=0.3 = %.4f  (calibrated gate <1.0)", rms);
        verdict(rep, rms < 1.0 ? "PASS" : "FAIL", 35, "form factor K(t)", {buf});
    }
    // 36
    if (filter_all(filter, 36)) {
        std::vector<cd> H;
        build_ab_cloud_hamiltonian(ABCloudConfig(16, 16, {{4.5,4.5,1.0}}, 0.5, 1.0, "open", 0.0), H);
        std::vector<double> ev;
        safe_eigvals(H, 256, ev);
        std::vector<double> band;
        central_band_eigs(ev, 0.6, band);
        double r0, rr; long nn;
        mean_adjacent_spacing_ratio(band, r0, nn);
        double lo = band.front(), span = band.back() - band.front();
        int nlev = 4096;
        std::vector<double> quant;
        for (double e : band)
            quant.push_back(lo + std::round((e - lo) / span * (nlev - 1)) / (double)(nlev - 1) * span);
        mean_adjacent_spacing_ratio(quant, rr, nn);
        double dr = std::fabs(rr - r0);
        MT19937 rng(12345);
        int counts[256] = {0};
        int nb2 = 200000;
        for (int i = 0; i < nb2; ++i) counts[rng.next_u32() & 0xFF]++;
        double ent = 0, exp2 = nb2 / 256.0, chi2z = 0;
        for (int c : counts) {
            if (c > 0) { double p = (double)c / nb2; ent -= p * std::log(p) / std::log(2.0); }
            chi2z += (c - exp2) * (c - exp2) / exp2;
        }
        double z = (chi2z - 255.0) / std::sqrt(2.0 * 255.0);
        bool ok = dr < 0.02 && std::fabs(ent - 8.0) < 0.01 && std::fabs(z) < 3.0;
        char buf[256];
        snprintf(buf, 256, "  |d<r>| under %d-level quantization = %.5f (gate 0.02)", nlev, dr);
        char buf2[160];
        snprintf(buf2, 160, "  RNG entropy = %.6f bits/byte (ideal 8.0), chi2 z = %+.2f (|z|<3)", ent, z);
        verdict(rep, ok ? "PASS" : "FAIL", 36, "byte-level robustness", {buf, buf2});
    }
    // 37
    if (filter_all(filter, 37)) {
        double err1 = std::fabs(std::exp(lgamma_lanczos(0.5)) - std::sqrt(PI));
        double err2 = std::fabs(std::exp(lgamma_lanczos(1.5)) - std::sqrt(PI) / 2.0);
        int n = 2000; double smax = 10.0, h = smax / n;
        double integ = 0, m2 = 0;
        for (int i = 0; i <= n; ++i) {
            double wgt = (i == 0 || i == n) ? 1.0 : (i % 2 == 1 ? 4.0 : 2.0);
            double p = gue2_surmise_pdf(i * h);
            integ += wgt * p;
            m2 += wgt * p * (i * h) * (i * h);
        }
        integ *= h / 3.0; m2 *= h / 3.0;
        bool ok = err1 < 1e-9 && err2 < 1e-9 && std::fabs(integ - 1) < 1e-4
                  && std::fabs(m2 - 3 * PI / 8) < 5e-3;
        char buf[256];
        snprintf(buf, 256, "  G(1/2)-sqrt(pi) = %.2e   G(3/2)-sqrt(pi)/2 = %.2e   int p2 = %.6f   <s2> = %.6f (3pi/8)",
                 err1, err2, integ, m2);
        verdict(rep, ok ? "PASS" : "FAIL", 37, "(1/2)! via Gamma + GUE normalization", {buf});
    }

    // not-ported notices
    int not_ported[] = {19, 20, 21, 22, 23, 27, 28, 29, 30, 31, 32, 33, 38, 39};
    const char* notes[] = {
        "four-pass Dirac-cone audit", "TKNN Chern number", "spinorial phase",
        "AB phase identity", "fractal factor", "binary chiral + zeta-dictionary",
        "f_GUE merit", "DOS dip", "v_F scaling ladder", "Hatano-Nelson skin",
        "multi-realization <r> bootstrap (dSFMT-disorder parity)",
        "L-scaling <r> (dSFMT-disorder parity)", "Curie point three-pass",
        "Test-34G geometry sweep"};
    printf("------------------------------------------------------------------------------\n");
    for (int i = 0; i < 14; ++i)
        if (filter_all(filter, not_ported[i]))
            printf("[SKIP] TEST %2d — not ported: %s\n", not_ported[i], notes[i]);
    printf("------------------------------------------------------------------------------\n");
    printf("SUITE RESULT: %d PASS, %d FAIL, %d WARN, %d INFO\n",
           rep.n_pass, rep.n_fail, rep.n_warn, rep.n_info);
    printf("==============================================================================\n");
}

// ─────────────────────────────────────────────────────────────────────────────
// Suite helpers + CLI
// ─────────────────────────────────────────────────────────────────────────────
static bool filter_all(const std::string& filter, int tid) {
    if (filter == "all") return true;
    std::stringstream ss(filter);
    std::string tok;
    while (std::getline(ss, tok, ',')) {
        if (atoi(tok.c_str()) == tid) return true;
    }
    return false;
}

static std::string join_nums(const std::vector<double>& v) {
    std::ostringstream os;
    for (size_t i = 0; i < v.size(); ++i) {
        if (i) os << "  ";
        os << v[i];
    }
    return os.str();
}

// Box–Muller from the portable MT19937 (for the Test 12 GUE matrix)
static double gauss(MT19937& rng) {
    double u1 = rng.random(), u2 = rng.random();
    if (u1 < 1e-300) u1 = 1e-300;
    return std::sqrt(-2.0 * std::log(u1)) * std::cos(2 * PI * u2);
}

// Two-sample KS with tie discipline (see gof.py ks_test_2sample)
static double ks2(const std::vector<double>& a, const std::vector<double>& b) {
    std::vector<double> xs(a), ys(b);
    std::sort(xs.begin(), xs.end());
    std::sort(ys.begin(), ys.end());
    size_t n = xs.size(), m = ys.size(), i = 0, j = 0;
    double D = 0.0;
    while (i < n && j < m) {
        if (xs[i] < ys[j]) { i++; }
        else if (ys[j] < xs[i]) { j++; }
        else {
            double xv = xs[i];
            while (i < n && xs[i] == xv) i++;
            while (j < m && ys[j] == xv) j++;
        }
        D = std::max(D, std::fabs((double)i / n - (double)j / m));
    }
    return D;
}

static std::vector<double> unit_spacings(const std::vector<double>& u) {
    std::vector<double> d;
    for (size_t i = 0; i + 1 < u.size(); ++i) d.push_back(u[i+1] - u[i]);
    if (d.empty()) return d;
    double m = 0; for (double v : d) m += v; m /= d.size();
    if (m > 1e-300) for (double& v : d) v /= m;
    return d;
}

int main(int argc, char** argv) {
    if (argc < 2) {
        std::fprintf(stderr,
            "usage: abcloud <command> [options]\n"
            "commands:\n"
            "  selftest [--golden P] [--data P]   golden-reference parity check\n"
            "  zeros [--data P] [--n N]           full zero-analysis battery\n"
            "  suite [--test N|all] [--data P]    portable subset of the 39-test suite\n"
            "  ham                                vector-tier scenarios: entropy/TEE/IPR/RH\n"
            "  bN --N n... [--offset k]           b(N) statistic\n"
            "  gram --n n...                      Gram points\n"
            "  test11 [--mc n] [--seed s]         Anderson-Darling honest test\n"
            "  hp [--data P] [--n N]              H1 primary detector\n"
            "  sweep                              b(N) ladder sweep\n");
        return 2;
    }
    std::string cmd = argv[1];
    std::string data, golden, test = "all";
    std::vector<long> Ns;
    long offset = 0, ncut = 0;
    int mc = 200, seed = 777;
    for (int i = 2; i < argc; ++i) {
        std::string a = argv[i];
        auto next = [&]() -> std::string { return (i + 1 < argc) ? argv[++i] : ""; };
        if (a == "--data") data = next();
        else if (a == "--golden") golden = next();
        else if (a == "--test") test = next();
        else if (a == "--N") { while (i + 1 < argc && argv[i+1][0] != '-') Ns.push_back(atol(argv[++i])); }
        else if (a == "--n") { while (i + 1 < argc && argv[i+1][0] != '-') Ns.push_back(atol(argv[++i])); }
        else if (a == "--offset") offset = atol(next().c_str());
        else if (a == "--mc") mc = atoi(next().c_str());
        else if (a == "--seed") seed = atoi(next().c_str());
    }
    // default paths relative to this binary's repo layout
    std::string exe_dir = []() {
        std::string p = "/proc/self/exe";
        char buf[4096]; ssize_t r = readlink(p.c_str(), buf, 4095);
        if (r <= 0) return std::string(".");
        buf[r] = 0;
        std::string s(buf);
        size_t pos = s.rfind('/');
        return pos == std::string::npos ? std::string(".") : s.substr(0, pos);
    }();
    std::string default_zeros = exe_dir + "/../../zeros50k.txt";
    std::string default_golden = exe_dir + "/../golden/abcloud_golden.json";
    std::string zeros_path = data.empty() ? default_zeros : data;
    std::string golden_path = golden.empty() ? default_golden : golden;

    if (cmd == "selftest") {
        std::vector<double> z;
        load_zeros(zeros_path, z);
        run_selftest(z, golden_path);
        return 0;
    }
    if (cmd == "zeros") {
        std::vector<double> z;
        load_zeros(zeros_path, z);
        if (ncut) z.resize(std::min(z.size(), (size_t)ncut));
        std::vector<double> sp;
        normalized_spacings(z, sp);
        double mean = 0; for (double s : sp) mean += s; mean /= sp.size();
        double var = 0; for (double s : sp) var += (s-mean)*(s-mean); var /= (sp.size()-1);
        double D, p; ks_test(sp, D, p);
        printf("zeros: n=%zu  g1=%.6f  gN=%.6f\n", z.size(), z.front(), z.back());
        printf("spacings: n=%zu  mean=%.6f  var=%.6f\n", sp.size(), mean, var);
        printf("KS  : D=%.6f  p=%.6e\n", D, p);
        printf("CvM : W2=%.6f\n", cvm_test(sp));
        printf("A2  : %.6f\n", anderson_darling_stat(sp));
        double chi2, pchi; int df;
        chi2_gue_test(sp, 30, chi2, df, pchi);
        printf("chi2: %.4f  df=%d  p=%.6e\n", chi2, df, pchi);
        double r; long n_r;
        mean_adjacent_spacing_ratio(z, r, n_r);
        printf("<r> : %.6f  (n_r=%ld; GUE 0.5992, Poisson 0.6243)\n", r, n_r);
        std::vector<double> pos;
        unfolded_positions(z, pos);
        MT19937 rng(777);
        double Ls[] = {5.0, 10.0, 20.0, 50.0, 100.0};
        for (double L : Ls)
            printf("S2(L=%6.1f) = %.6f  [Poisson %.1f]\n", L, number_variance(pos, L, 3000, rng), L);
        double Ld[] = {5.0, 10.0, 20.0, 50.0};
        for (double L : Ld)
            printf("D3(L=%6.1f) = %.6f  [Poisson %.4f]\n", L, delta3_rigidity(pos, L, 300, 300, rng), L/15.0);
        std::vector<double> tvals;
        for (int i = 1; i <= 30; ++i) tvals.push_back(0.1 * i);
        std::vector<double> K;
        compute_K_form_factor(z, tvals, K);
        for (double t : {0.2, 0.5, 1.0, 2.0, 3.0}) {
            size_t i = (size_t)std::lround(t / 0.1) - 1;
            printf("K(t=%.1f) = %.6f  [GUE envelope %.6f]\n", t, K[i], tvals_envelope(t));
        }
        return 0;
    }
    if (cmd == "suite") {
        std::vector<double> z;
        load_zeros(zeros_path, z);
        run_suite(z, test);
        return 0;
    }
    if (cmd == "ham") {
        // §8 vector tier: monumental scenarios + entanglement/topology metrics
        struct Scn { const char* name; ABCloudConfig cfg; int L; };
        std::vector<Scn> scns = {
            {"L8_open_a025_2vort", ABCloudConfig(8, 8, {{3.5, 3.5, 1.0}, {6.5, 6.5, -1.0}},
                                                 0.25, 1.0, "open", 0.0, 96, "monumental"), 8},
            {"L10_open_a03_clean", ABCloudConfig(10, 10, {}, 0.3, 1.0, "open", 0.0, 96, "monumental"), 10},
            {"L12_open_a03_clean", ABCloudConfig(12, 12, {}, 0.3, 1.0, "open", 0.0, 96, "monumental"), 12},
        };
        for (auto& scn : scns) {
            HamTier T;
            ham_tier_compute(scn.cfg, scn.L, T);
            printf("%s  (L=%d, N=%ld)\n", scn.name, scn.L, (long)scn.cfg.Nx * scn.cfg.Ny);
            for (int c = 0; c < 3; ++c) {
                printf("  c%d: S(f=0.25)=%.9f  S(f=0.5)=%.9f  S(f=0.75)=%.9f  IPR=%.9f\n",
                       c, T.S[(size_t)c * 3], T.S[(size_t)c * 3 + 1], T.S[(size_t)c * 3 + 2],
                       T.ipr[c]);
            }
            printf("  TEE: slope=%.9f  gamma_top=%.9f  S_mean(f=0.5)=%.9f  S_std(f=0.5)=%.9f\n",
                   T.slope, T.gamma_top, T.S_mean[MON_TEE_IDX[1]], T.S_std[MON_TEE_IDX[1]]);
            std::vector<double> cb;
            central_band_eigs(T.ev, 0.6, cb);
            double D, p; rh_band_ks(cb, D, p);
            double r; long ncb;
            mean_adjacent_spacing_ratio(cb, r, ncb);
            printf("  RH metrics (central 0.6): n=%ld  D=%.6f  p=%.4e  <r>=%.6f\n", ncb, D, p, r);
        }
        return 0;
    }
    if (cmd == "bN") {
        std::vector<double> z;
        load_zeros(zeros_path, z);
        if (Ns.empty()) Ns = {100, 1000, 10000};
        for (long N : Ns)
            printf("b(N=%6ld, offset=%ld) = %.10f\n", N, offset, compute_bN(z, N, offset));
        return 0;
    }
    if (cmd == "gram") {
        if (Ns.empty()) Ns = {1, 10, 100};
        for (long n : Ns) printf("g_%ld = %.10f\n", n, gram_point(n));
        return 0;
    }
    if (cmd == "test11") {
        std::vector<double> z;
        load_zeros(zeros_path, z);
        std::vector<double> sp;
        normalized_spacings(z, sp);
        double A2 = anderson_darling_stat(sp);
        printf("Test 11 (honest): exact A2 on n=%zu spacings: %.6f\n", sp.size(), A2);
        if (mc > 0) {
            MT19937 rng((uint32_t)seed);
            std::vector<double> buf(sp.size());
            int count = 0;
            for (int it = 0; it < mc; ++it) {
                RMT.sample(rng, buf);
                if (anderson_darling_stat(buf) >= A2) count++;
            }
            printf("MC null (law-exact inverse-CDF, %d draws): p = %.6f  (%d/%d >= A2)\n",
                   mc, (count + 1.0) / (mc + 1.0), count, mc);
        }
        return 0;
    }
    if (cmd == "hp") {
        std::vector<double> z;
        load_zeros(zeros_path, z);
        if (ncut) z.resize(std::min(z.size(), (size_t)ncut));
        std::vector<double> om;
        for (int k = 0; k < 726; ++k) om.push_back(0.3 + 0.004 * k);
        size_t n = z.size();
        std::vector<double> w(n);
        for (size_t i = 0; i < n; ++i)
            w[i] = 0.5 * (1.0 - std::cos(2 * PI * (double)i / (double)std::max<size_t>(n - 1, 1)));
        double sw2 = 0; for (double wi : w) sw2 += wi * wi;
        std::vector<double> P(om.size());
        for (size_t fi = 0; fi < om.size(); ++fi) {
            double re = 0, im = 0;
            for (size_t i = 0; i < n; ++i) {
                re += w[i] * std::cos(om[fi] * z[i]);
                im -= w[i] * std::sin(om[fi] * z[i]);
            }
            P[fi] = (re*re + im*im) / sw2;
        }
        std::vector<double> Ps(P); std::sort(Ps.begin(), Ps.end());
        double med = 0.5 * (Ps[Ps.size()/2 - 1] + Ps[Ps.size()/2]);
        printf("H1 primary detector on %zu positions (band median %.6e):\n", n, med);
        int primes[] = {2, 3, 5, 7, 11, 13};
        int hits = 0;
        for (int pr : primes) {
            double tgt = std::log((double)pr);
            size_t best = 0; double bd = 1e300;
            for (size_t i = 0; i < om.size(); ++i) {
                double d = std::fabs(om[i] - tgt);
                if (d < bd) { bd = d; best = i; }
            }
            double snr = P[best] / med;
            if (snr >= 10.0) hits++;
            printf("  SNR(log %2d) = %.6e  [%s]\n", pr, snr, snr >= 10.0 ? "PEAK" : "-");
        }
        printf("  verdict: %d/6 prime harmonics above SNR 10\n", hits);
        return 0;
    }
    if (cmd == "sweep") {
        std::vector<double> z;
        load_zeros(zeros_path, z);
        if (Ns.empty()) Ns = {100, 500, 1000, 5000, 10000, 50000};
        printf("  N        b(N)\n");
        for (long N : Ns)
            printf("%6ld  %.8f\n", N, compute_bN(z, N));
        return 0;
    }
    std::fprintf(stderr, "unknown command: %s\n", cmd.c_str());
    return 2;
}
