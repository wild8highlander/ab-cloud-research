/**
 * ab_cloud_verify_en.cpp — AB-Cloud Verification Suite: English-Only Module
 *
 * Addresses three reviewer objections regarding the AB-cloud framework
 * for Riemann zeta zero verification. All output messages in English.
 *
 *   Objection 1: Numerical stability of b(N) = (1/N) Σ|γ_k − γ̃_k|
 *   Objection 2: GUE spacing statistics (Kolmogorov–Smirnov test)
 *   Objection 3: Large-T decay rate via log-log regression
 *
 * Compile:  g++ -std=c++17 -O2 -o ab_cloud_verify_en ab_cloud_verify_en.cpp -lm
 * Usage:    ./ab_cloud_verify_en --zeros 200000 --source 500k --objection all
 *
 * Author:   AB-Cloud Verification Team
 * License:  MIT
 */

#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <vector>

#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

// ============================================================================
// English Message Constants
// ============================================================================

namespace Msg {

constexpr const char* BANNER         = "=== AB-Cloud Verification Suite (English) ===";
constexpr const char* LOADING        = "Loading zeros...";
constexpr const char* LOADED         = "Loaded %d zeros from source '%s'";
constexpr const char* ERR_OPEN       = "ERROR: Cannot open data file: %s";
constexpr const char* ERR_EMPTY      = "ERROR: No zeros loaded. Check data directory and source.";
constexpr const char* ERR_FEW        = "ERROR: Need at least 2 zeros, got %d";
constexpr const char* ERR_SRC        = "ERROR: Unknown source '%s'. Use: 50k, 500k, 2M, highT, zeros6, auto";

constexpr const char* OBJ1_HDR       = "\n--- Objection 1: Numerical Stability of b(N) ---";
constexpr const char* OBJ1_DESC      = "b(N) = (1/N) * Sum|gamma_k - gamma_tilde_k|";
constexpr const char* OBJ1_GRAM      = "Gram points via Lambert W (Halley iteration)";
constexpr const char* OBJ1_CONV_Y    = "converging";
constexpr const char* OBJ1_CONV_N    = "NOT converging";

constexpr const char* OBJ2_HDR       = "\n--- Objection 2: GUE Spacing Statistics ---";
constexpr const char* OBJ2_DESC      = "Normalized spacings: s_k = (gamma_{k+1} - gamma_k) * log(gamma_k/(2*pi)) / (2*pi)";
constexpr const char* OBJ2_GUE       = "GUE PDF: p(s) = (pi*s/2) * exp(-pi*s^2/4)";
constexpr const char* OBJ2_KS        = "Kolmogorov-Smirnov test: D = max|F_emp - F_GUE|";

constexpr const char* OBJ3_HDR       = "\n--- Objection 3: Large-T Decay Rate ---";
constexpr const char* OBJ3_DESC      = "Fit log(b(N)) vs log(N): expected slope ~ -0.5";

constexpr const char* SUMMARY_HDR    = "\n=== Verification Summary ===";
constexpr const char* SUMMARY_OK     = "All objections addressed successfully.";
constexpr const char* SUMMARY_FAIL   = "Some objections require further investigation.";
constexpr const char* DONE           = "\nVerification complete.";

} // namespace Msg

// ============================================================================
// Zero Loader
// ============================================================================

static std::string trim(const std::string& s) {
    size_t start = s.find_first_not_of(" \t\r\n\v\f");
    if (start == std::string::npos) return "";
    size_t end = s.find_last_not_of(" \t\r\n\v\f");
    return s.substr(start, end - start + 1);
}

/**
 * Load Riemann zeta zeros (imaginary parts) from data files.
 *
 * @param data_dir  Path to data directory (e.g., "../data")
 * @param count     Maximum number of zeros to load (0 = all)
 * @param source    Source identifier: "50k", "500k", "2M", "highT", "zeros6", "auto"
 * @return          Vector of imaginary parts of zeta zeros
 */
std::vector<double> load_zeros(const std::string& data_dir, int count,
                                const std::string& source) {
    static const std::map<std::string, std::string> source_files = {
        {"50k",   "zeta_zeros_50000.txt"},
        {"500k",  "zeta_zeros_500k_odlyzko.txt"},
        {"2M",    "zeta_zeros_2M_odlyzko.txt"},
        {"highT", "zeta_zeros_highT_blocks.txt"},
        {"zeros6","zeros6.txt"},
    };

    // Auto-select based on requested count
    std::string src = source;
    if (src == "auto") {
        if (count <= 13661)       src = "50k";
        else if (count <= 500000) src = "500k";
        else                     src = "2M";
    }

    auto it = source_files.find(src);
    if (it == source_files.end()) {
        std::fprintf(stderr, Msg::ERR_SRC, src.c_str());
        std::cerr << std::endl;
        return {};
    }

    std::string filepath = data_dir + "/" + it->second;
    std::ifstream fin(filepath);
    if (!fin.is_open()) {
        std::fprintf(stderr, Msg::ERR_OPEN, filepath.c_str());
        std::cerr << std::endl;
        return {};
    }

    std::vector<double> zeros;
    zeros.reserve(count > 0 ? count : 100000);
    std::string line;

    while (std::getline(fin, line)) {
        std::string t = trim(line);
        if (t.empty() || t[0] == '#') continue;
        try {
            double val = std::stod(t);
            if (val > 0.0) {
                zeros.push_back(val);
                if (count > 0 && static_cast<int>(zeros.size()) >= count) break;
            }
        } catch (...) {
            continue;
        }
    }
    fin.close();
    return zeros;
}

// ============================================================================
// Mathematical Utilities
// ============================================================================

/**
 * Lambert W function (principal branch) via Halley's method.
 * Solves W * exp(W) = x for x > 0.
 */
static double lambert_W(double x, double tol = 1e-14, int maxit = 50) {
    if (x <= 0.0) return 0.0;
    double w = std::log(x);
    if (w > 0.0) w -= std::log(w);
    for (int i = 0; i < maxit; ++i) {
        double ew = std::exp(w);
        double f  = w * ew - x;
        double fp = ew * (w + 1.0);
        double fpp = ew * (w + 2.0);
        double delta = f / (fp - 0.5 * f * fpp / fp);
        w -= delta;
        if (std::fabs(delta) < tol * (1.0 + std::fabs(w))) break;
    }
    return w;
}

/** Gram point: γ̃_k ≈ 2πk / W(k/e) */
static double gram_point(int k) {
    if (k <= 0) return 0.0;
    double w = lambert_W(static_cast<double>(k) / std::exp(1.0));
    return (w > 0.0) ? 2.0 * M_PI * k / w : 0.0;
}

/** b(N) = (1/N) Σ|γ_k − γ̃_k| */
static double compute_bN(const std::vector<double>& zeros, int N) {
    if (N <= 0 || N > static_cast<int>(zeros.size())) return 0.0;
    double sum = 0.0;
    for (int k = 0; k < N; ++k) {
        sum += std::fabs(zeros[k] - gram_point(k + 1));
    }
    return sum / N;
}

/** GUE CDF: F(s) = 1 − exp(−π s² / 4) */
static double gue_cdf(double s) {
    return (s <= 0.0) ? 0.0 : 1.0 - std::exp(-M_PI * s * s / 4.0);
}

/** Compute normalized GUE spacings */
static std::vector<double> compute_gue_spacings(const std::vector<double>& zeros,
                                                 int max_n = 0) {
    int n = static_cast<int>(zeros.size()) - 1;
    if (max_n > 0 && max_n < n) n = max_n;
    std::vector<double> sp;
    sp.reserve(n);
    for (int k = 0; k < n; ++k) {
        double gk = zeros[k];
        if (gk <= 0.0) continue;
        double s = (zeros[k + 1] - gk) * std::log(gk / (2.0 * M_PI)) / (2.0 * M_PI);
        if (s > 0.0) sp.push_back(s);
    }
    return sp;
}

/** KS test: D = max|F_emp − F_GUE| */
static double ks_test(const std::vector<double>& spacings) {
    if (spacings.empty()) return 1.0;
    std::vector<double> sorted = spacings;
    std::sort(sorted.begin(), sorted.end());
    int N = static_cast<int>(sorted.size());
    double D = 0.0;
    for (int i = 0; i < N; ++i) {
        double F_gue = gue_cdf(sorted[i]);
        D = std::max(D, std::fabs(static_cast<double>(i + 1) / N - F_gue));
        D = std::max(D, std::fabs(static_cast<double>(i) / N - F_gue));
    }
    return D;
}

/** Linear regression: y = slope*x + intercept */
static void linreg(const std::vector<double>& x, const std::vector<double>& y,
                   double& slope, double& intercept, double& r2, double& max_resid) {
    int n = static_cast<int>(x.size());
    double sx = 0, sy = 0, sxx = 0, sxy = 0, syy = 0;
    for (int i = 0; i < n; ++i) {
        sx += x[i]; sy += y[i];
        sxx += x[i] * x[i]; sxy += x[i] * y[i]; syy += y[i] * y[i];
    }
    double denom = n * sxx - sx * sx;
    if (std::fabs(denom) < 1e-30) { slope = intercept = r2 = max_resid = 0; return; }
    slope = (n * sxy - sx * sy) / denom;
    intercept = (sy - slope * sx) / n;
    double ss_tot = syy - sy * sy / n, ss_res = 0;
    max_resid = 0;
    for (int i = 0; i < n; ++i) {
        double r = y[i] - (slope * x[i] + intercept);
        ss_res += r * r;
        max_resid = std::max(max_resid, std::fabs(r));
    }
    r2 = (ss_tot > 0) ? 1.0 - ss_res / ss_tot : 0;
}

// ============================================================================
// Objection Handlers
// ============================================================================

static bool objection1(const std::vector<double>& zeros) {
    std::cout << Msg::OBJ1_HDR << "\n" << Msg::OBJ1_DESC << "\n" << Msg::OBJ1_GRAM << std::endl;

    std::vector<int> Ns = {100, 500, 1000, 5000, 10000, 50000, 100000, 500000};
    int max_z = static_cast<int>(zeros.size());
    std::vector<int> valid;
    for (int N : Ns) if (N <= max_z) valid.push_back(N);
    if (valid.empty()) valid.push_back(std::min(100, max_z));

    std::printf("\n  %10s %15s %15s %15s\n", "N", "b(N)", "log10(b(N))", "Convergence");
    std::printf("  %10s %15s %15s %15s\n", "----------", "---------------", "---------------", "---------------");

    std::vector<double> bvals;
    bool converging = true;
    for (size_t i = 0; i < valid.size(); ++i) {
        double bN = compute_bN(zeros, valid[i]);
        bvals.push_back(bN);
        double lb = (bN > 0) ? std::log10(bN) : -999.0;
        std::string conv = "---";
        if (i > 0) {
            conv = (bN < bvals[i - 1]) ? Msg::OBJ1_CONV_Y : (converging = false, Msg::OBJ1_CONV_N);
        }
        std::printf("  %10d %15.8f %15.4f %15s\n", valid[i], bN, lb, conv.c_str());
    }

    std::cout << "\nResult: b(N) " << (converging ? "converges" : "does NOT converge")
              << " as N increases. " << (converging ? "OK" : "WARN") << std::endl;
    return converging;
}

static bool objection2(const std::vector<double>& zeros) {
    std::cout << Msg::OBJ2_HDR << "\n" << Msg::OBJ2_DESC << "\n"
              << Msg::OBJ2_GUE << "\n" << Msg::OBJ2_KS << std::endl;

    std::vector<int> Ns = {1000, 5000, 10000, 50000, 100000, 500000};
    int max_z = static_cast<int>(zeros.size());

    std::printf("\n  %10s %15s %15s %15s %10s\n",
               "N_zeros", "D_stat", "D_crit(0.05)", "D/D_crit", "Pass?");
    std::printf("  %10s %15s %15s %15s %10s\n",
               "----------", "---------------", "---------------", "---------------", "----------");

    bool all_pass = true;
    for (int N : Ns) {
        if (N > max_z - 1) break;
        int start = std::max(0, max_z - N - 1);
        std::vector<double> sub(zeros.begin() + start, zeros.begin() + start + N + 1);
        auto sp = compute_gue_spacings(sub, N);
        double D = ks_test(sp);
        double D_crit = 1.358 / std::sqrt(static_cast<double>(sp.size()));
        double ratio = D / D_crit;
        bool pass = D < D_crit;
        if (!pass) all_pass = false;
        std::printf("  %10d %15.8f %15.8f %15.4f %10s\n",
                   (int)sp.size(), D, D_crit, ratio, pass ? "YES" : "NO");
    }

    std::cout << "\nResult: KS test " << (all_pass ? "PASSED" : "FAILED")
              << " at alpha=0.05." << std::endl;
    return all_pass;
}

static bool objection3(const std::vector<double>& zeros) {
    std::cout << Msg::OBJ3_HDR << "\n" << Msg::OBJ3_DESC << std::endl;

    int max_z = static_cast<int>(zeros.size());
    std::vector<double> logN, logbN;
    for (int N = 100; N <= max_z; N += N / 4) {
        double bN = compute_bN(zeros, N);
        if (bN > 0) { logN.push_back(std::log((double)N)); logbN.push_back(std::log(bN)); }
    }
    if (logN.size() < 3) {
        std::cout << "WARNING: Insufficient data for regression." << std::endl;
        return false;
    }

    double slope, intercept, r2, max_resid;
    linreg(logN, logbN, slope, intercept, r2, max_resid);

    std::cout << "\n  Linear Regression on log scale:" << std::endl;
    std::printf("  Slope     = %+.6f  (expected: -0.5)\n", slope);
    std::printf("  Intercept = %+.6f\n", intercept);
    std::printf("  R^2       = %.6f\n", r2);
    std::printf("  Max |residual| = %.6f\n", max_resid);

    bool ok = std::fabs(slope - (-0.5)) < 0.15;
    std::printf("\nResult: Fitted slope = %+.4f, expected = -0.500. %s\n",
               slope, ok ? "OK" : "WARN: slope deviates from -0.5");
    return ok;
}

// ============================================================================
// Command-Line Parsing & Main
// ============================================================================

struct Config {
    int         zeros    = 200000;
    std::string source   = "auto";
    std::string objection = "all";
    std::string data_dir = "../data";
};

static Config parse_args(int argc, char* argv[]) {
    Config cfg;
    for (int i = 1; i < argc; ++i) {
        std::string a = argv[i];
        if ((a == "--zeros" || a == "-z") && i+1 < argc) cfg.zeros = std::atoi(argv[++i]);
        else if ((a == "--source" || a == "-s") && i+1 < argc) cfg.source = argv[++i];
        else if ((a == "--objection" || a == "-o") && i+1 < argc) cfg.objection = argv[++i];
        else if ((a == "--data-dir" || a == "-d") && i+1 < argc) cfg.data_dir = argv[++i];
        else if (a == "--help" || a == "-h") {
            std::cout << "Usage: ab_cloud_verify_en [OPTIONS]\n"
                      << "  --zeros   N     Number of zeros (default: 200000)\n"
                      << "  --source  SRC   50k, 500k, 2M, highT, zeros6, auto\n"
                      << "  --objection O   1, 2, 3, or all (default: all)\n"
                      << "  --data-dir DIR  Data directory (default: ../data)\n";
            std::exit(0);
        }
    }
    return cfg;
}

int main(int argc, char* argv[]) {
    Config cfg = parse_args(argc, argv);

    std::cout << Msg::BANNER << std::endl;
    std::cout << Msg::LOADING << std::endl;

    auto zeros = load_zeros(cfg.data_dir, cfg.zeros, cfg.source);
    if (zeros.empty()) { std::cerr << Msg::ERR_EMPTY << std::endl; return 1; }

    char buf[256];
    std::snprintf(buf, sizeof(buf), Msg::LOADED, (int)zeros.size(), cfg.source.c_str());
    std::cout << buf << std::endl;

    if (zeros.size() < 2) {
        std::snprintf(buf, sizeof(buf), Msg::ERR_FEW, (int)zeros.size());
        std::cerr << buf << std::endl; return 1;
    }

    bool o1 = true, o2 = true, o3 = true;
    if (cfg.objection == "all" || cfg.objection == "1") o1 = objection1(zeros);
    if (cfg.objection == "all" || cfg.objection == "2") o2 = objection2(zeros);
    if (cfg.objection == "all" || cfg.objection == "3") o3 = objection3(zeros);

    bool ok = o1 && o2 && o3;
    std::cout << Msg::SUMMARY_HDR << "\n"
              << (ok ? Msg::SUMMARY_OK : Msg::SUMMARY_FAIL) << "\n"
              << Msg::DONE << std::endl;
    return ok ? 0 : 1;
}
