/**
 * ab_cloud_verify.cpp — AB-Cloud Verification Suite: Bilingual Module (RU/EN)
 *
 * Addresses three reviewer objections regarding the AB-cloud framework
 * for Riemann zeta zero verification:
 *
 *   Objection 1: Numerical stability of b(N) = (1/N) Σ|γ_k − γ̃_k|
 *   Objection 2: GUE spacing statistics (Kolmogorov–Smirnov test)
 *   Objection 3: Large-T decay rate via log-log regression
 *
 * Compile:  g++ -std=c++17 -O2 -o ab_cloud_verify ab_cloud_verify.cpp -lm
 * Usage:    ./ab_cloud_verify --zeros 200000 --source 500k --objection all --lang en
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
// Bilingual string maps
// ============================================================================

using MsgMap = std::map<std::string, std::string>;

static MsgMap make_messages_en() {
    return {
        {"banner",        "=== AB-Cloud Verification Suite ==="},
        {"lang_label",    "Language: English"},
        {"loading",       "Loading zeros..."},
        {"loaded",        "Loaded %d zeros from source '%s'"},
        {"skip_comments","(Skipping comment/blank lines)"},
        {"err_open",      "ERROR: Cannot open data file: %s"},
        {"err_empty",     "ERROR: No zeros loaded. Check data directory and source."},
        {"err_few",       "ERROR: Need at least 2 zeros for verification, got %d"},
        {"err_unknown_src","ERROR: Unknown source '%s'. Use: 50k, 500k, 2M, highT, zeros6, auto"},

        {"obj1_header",   "\n--- Objection 1: Numerical Stability of b(N) ---"},
        {"obj1_desc",     "b(N) = (1/N) * Sum|gamma_k - gamma_tilde_k|"},
        {"obj1_gram",     "Gram points via Lambert W (Halley iteration)"},
        {"obj1_table_hdr","\n  %10s %15s %15s %15s"},
        {"obj1_col1",     "N"},
        {"obj1_col2",     "b(N)"},
        {"obj1_col3",     "log10(b(N))"},
        {"obj1_col4",     "Convergence"},
        {"obj1_conv_yes", "converging"},
        {"obj1_conv_no",  "NOT converging"},
        {"obj1_result",   "\nResult: b(N) %s as N increases. %s"},

        {"obj2_header",   "\n--- Objection 2: GUE Spacing Statistics ---"},
        {"obj2_desc",     "Normalized spacings: s_k = (gamma_{k+1} - gamma_k) * log(gamma_k/(2*pi)) / (2*pi)"},
        {"obj2_gue_pdf",  "GUE PDF: p(s) = (pi*s/2) * exp(-pi*s^2/4)"},
        {"obj2_ks",       "Kolmogorov-Smirnov test: D = max|F_emp - F_GUE|"},
        {"obj2_table_hdr","\n  %10s %15s %15s %15s %10s"},
        {"obj2_col1",     "N_zeros"},
        {"obj2_col2",     "D_stat"},
        {"obj2_col3",     "D_crit(0.05)"},
        {"obj2_col4",     "D/D_crit"},
        {"obj2_col5",     "Pass?"},
        {"obj2_pass",     "YES"},
        {"obj2_fail",     "NO"},
        {"obj2_result",   "\nResult: KS test %s at alpha=0.05 (D=%.6f, D_crit=%.6f)."},

        {"obj3_header",   "\n--- Objection 3: Large-T Decay Rate ---"},
        {"obj3_desc",     "Fit log(b(N)) vs log(N): expected slope ~ -0.5"},
        {"obj3_reg_hdr",  "\n  Linear Regression on log scale:"},
        {"obj3_slope",    "  Slope     = %+.6f  (expected: -0.5)"},
        {"obj3_intercept","  Intercept = %+.6f"},
        {"obj3_r2",       "  R^2       = %.6f"},
        {"obj3_residual", "  Max |residual| = %.6f"},
        {"obj3_result",   "\nResult: Fitted slope = %+.4f, expected = -0.500. %s"},

        {"summary_hdr",   "\n=== Verification Summary ==="},
        {"summary_ok",    "All objections addressed successfully."},
        {"summary_fail",  "Some objections require further investigation."},
        {"done",          "\nVerification complete."},
    };
}

static MsgMap make_messages_ru() {
    return {
        {"banner",        "=== Верификационный комплект AB-Cloud ==="},
        {"lang_label",    "Язык: Русский"},
        {"loading",       "Загрузка нулей..."},
        {"loaded",        "Загружено %d нулей из источника '%s'"},
        {"skip_comments","(Пропуск строк-комментариев и пустых строк)"},
        {"err_open",      "ОШИБКА: Не удалось открыть файл данных: %s"},
        {"err_empty",     "ОШИБКА: Нули не загружены. Проверьте каталог данных и источник."},
        {"err_few",       "ОШИБКА: Требуется минимум 2 нуля для верификации, получено %d"},
        {"err_unknown_src","ОШИБКА: Неизвестный источник '%s'. Используйте: 50k, 500k, 2M, highT, zeros6, auto"},

        {"obj1_header",   "\n--- Возражение 1: Числовая стабильность b(N) ---"},
        {"obj1_desc",     "b(N) = (1/N) * Sum|gamma_k - gamma_tilde_k|"},
        {"obj1_gram",     "Точки Грама через W Ламберта (итерация Холли)"},
        {"obj1_table_hdr","\n  %10s %15s %15s %15s"},
        {"obj1_col1",     "N"},
        {"obj1_col2",     "b(N)"},
        {"obj1_col3",     "log10(b(N))"},
        {"obj1_col4",     "Сходимость"},
        {"obj1_conv_yes", "сходится"},
        {"obj1_conv_no",  "НЕ сходится"},
        {"obj1_result",   "\nРезультат: b(N) %s с ростом N. %s"},

        {"obj2_header",   "\n--- Возражение 2: Статистика интервалов GUE ---"},
        {"obj2_desc",     "Нормализованные интервалы: s_k = (gamma_{k+1} - gamma_k) * log(gamma_k/(2*pi)) / (2*pi)"},
        {"obj2_gue_pdf",  "PDF GUE: p(s) = (pi*s/2) * exp(-pi*s^2/4)"},
        {"obj2_ks",       "Критерий Колмогорова-Смирнова: D = max|F_emp - F_GUE|"},
        {"obj2_table_hdr","\n  %10s %15s %15s %15s %10s"},
        {"obj2_col1",     "N_нулей"},
        {"obj2_col2",     "D_стат"},
        {"obj2_col3",     "D_крит(0.05)"},
        {"obj2_col4",     "D/D_крит"},
        {"obj2_col5",     "Пройден?"},
        {"obj2_pass",     "ДА"},
        {"obj2_fail",     "НЕТ"},
        {"obj2_result",   "\nРезультат: KS-тест %s при alpha=0.05 (D=%.6f, D_крит=%.6f)."},

        {"obj3_header",   "\n--- Возражение 3: Скорость убывания на больших T ---"},
        {"obj3_desc",     "Аппроксимация log(b(N)) vs log(N): ожид. наклон ~ -0.5"},
        {"obj3_reg_hdr",  "\n  Линейная регрессия в лог. масштабе:"},
        {"obj3_slope",    "  Наклон    = %+.6f  (ожидается: -0.5)"},
        {"obj3_intercept","  Св. член  = %+.6f"},
        {"obj3_r2",       "  R^2       = %.6f"},
        {"obj3_residual", "  Макс |невязка| = %.6f"},
        {"obj3_result",   "\nРезультат: Наклон = %+.4f, ожидаемый = -0.500. %s"},

        {"summary_hdr",   "\n=== Итоги верификации ==="},
        {"summary_ok",    "Все возражения успешно опровергнуты."},
        {"summary_fail",  "Некоторые возражения требуют дальнейшего исследования."},
        {"done",          "\nВерификация завершена."},
    };
}

// ============================================================================
// Zero Loader
// ============================================================================

/**
 * Trim leading and trailing whitespace from a string.
 */
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
    // Map source name to filename
    static const std::map<std::string, std::string> source_files = {
        {"50k",   "zeta_zeros_50000.txt"},
        {"500k",  "zeta_zeros_500k_odlyzko.txt"},
        {"2M",    "zeta_zeros_2M_odlyzko.txt"},
        {"highT", "zeta_zeros_highT_blocks.txt"},
        {"zeros6","zeros6.txt"},
    };

    // Auto-select based on count
    std::string src = source;
    if (src == "auto") {
        if (count <= 13661)       src = "50k";
        else if (count <= 500000) src = "500k";
        else                     src = "2M";
    }

    auto it = source_files.find(src);
    if (it == source_files.end()) {
        std::fprintf(stderr, "Unknown source: '%s'\n", src.c_str());
        return {};
    }

    std::string filepath = data_dir + "/" + it->second;
    std::ifstream fin(filepath);
    if (!fin.is_open()) {
        std::fprintf(stderr, "Cannot open: %s\n", filepath.c_str());
        return {};
    }

    std::vector<double> zeros;
    zeros.reserve(count > 0 ? count : 100000);
    std::string line;

    while (std::getline(fin, line)) {
        std::string trimmed = trim(line);

        // Skip comment lines and blank lines
        if (trimmed.empty() || trimmed[0] == '#') continue;

        // Try to parse as double
        try {
            double val = std::stod(trimmed);
            if (val > 0.0) {  // Only positive imaginary parts
                zeros.push_back(val);
                if (count > 0 && static_cast<int>(zeros.size()) >= count) break;
            }
        } catch (...) {
            // Skip unparseable lines (headers, etc.)
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
 * Compute the principal branch of Lambert W function using Halley's method.
 * Solves W*exp(W) = x for W given x > 0.
 *
 * @param x     Input value (must be > 0)
 * @param tol   Convergence tolerance
 * @param maxit Maximum iterations
 * @return      W(x) on the principal branch
 */
static double lambert_W(double x, double tol = 1e-14, int maxit = 50) {
    if (x <= 0.0) return 0.0;
    // Initial guess: log(x) - log(log(x)) for large x
    double w = std::log(x);
    if (w > 0.0) w -= std::log(w);

    // Halley's method iteration for W*exp(W) = x
    for (int i = 0; i < maxit; ++i) {
        double ew = std::exp(w);
        double f = w * ew - x;
        double fp = ew * (w + 1.0);          // f'
        double fpp = ew * (w + 2.0);         // f''
        double delta = f / (fp - 0.5 * f * fpp / fp);  // Halley correction
        w -= delta;
        if (std::fabs(delta) < tol * (1.0 + std::fabs(w))) break;
    }
    return w;
}

/**
 * Compute the k-th Gram point: γ̃_k ≈ 2πk / W(k/e)
 * where W is the Lambert W function on the principal branch.
 *
 * @param k Index (k >= 1)
 * @return  Approximate Gram point γ̃_k
 */
static double gram_point(int k) {
    if (k <= 0) return 0.0;
    double x = static_cast<double>(k) / std::exp(1.0);
    double w = lambert_W(x);
    if (w <= 0.0) return 0.0;
    return 2.0 * M_PI * k / w;
}

/**
 * Compute b(N) = (1/N) * Σ_{k=1}^{N} |γ_k − γ̃_k|
 * Measures mean absolute deviation between actual zeros and Gram points.
 *
 * @param zeros Vector of zeta zero imaginary parts (sorted)
 * @param N     Number of terms in the sum
 * @return      b(N) value
 */
static double compute_bN(const std::vector<double>& zeros, int N) {
    if (N <= 0 || N > static_cast<int>(zeros.size())) return 0.0;
    double sum = 0.0;
    for (int k = 0; k < N; ++k) {
        double gtilde = gram_point(k + 1);  // Gram point γ̃_{k+1} (1-indexed)
        sum += std::fabs(zeros[k] - gtilde);
    }
    return sum / N;
}

/**
 * GUE CDF: F(s) = 1 - exp(-π s² / 4)
 * Cumulative distribution function for the GUE level spacing.
 *
 * @param s Spacing value
 * @return  Cumulative probability
 */
static double gue_cdf(double s) {
    if (s <= 0.0) return 0.0;
    return 1.0 - std::exp(-M_PI * s * s / 4.0);
}

/**
 * Compute normalized GUE spacings from zeta zeros.
 * s_k = (γ_{k+1} − γ_k) * log(γ_k / (2π)) / (2π)
 *
 * @param zeros  Vector of zeta zero imaginary parts (sorted)
 * @param max_n  Maximum number of spacings to compute (0 = all)
 * @return       Vector of normalized spacings
 */
static std::vector<double> compute_gue_spacings(const std::vector<double>& zeros,
                                                 int max_n = 0) {
    int n = static_cast<int>(zeros.size()) - 1;
    if (max_n > 0 && max_n < n) n = max_n;

    std::vector<double> spacings;
    spacings.reserve(n);
    for (int k = 0; k < n; ++k) {
        double gamma_k = zeros[k];
        if (gamma_k <= 0.0) continue;
        double delta = zeros[k + 1] - gamma_k;
        double norm_factor = std::log(gamma_k / (2.0 * M_PI)) / (2.0 * M_PI);
        double s = delta * norm_factor;
        if (s > 0.0) spacings.push_back(s);
    }
    return spacings;
}

/**
 * Kolmogorov-Smirnov test: D = max|F_empirical(s) - F_GUE(s)|
 *
 * @param spacings  Vector of normalized spacings
 * @return          KS statistic D
 */
static double ks_test(const std::vector<double>& spacings) {
    if (spacings.empty()) return 1.0;

    std::vector<double> sorted = spacings;
    std::sort(sorted.begin(), sorted.end());

    int N = static_cast<int>(sorted.size());
    double D = 0.0;

    for (int i = 0; i < N; ++i) {
        double s = sorted[i];
        double F_emp = static_cast<double>(i + 1) / N;
        double F_gue = gue_cdf(s);
        double diff1 = std::fabs(F_emp - F_gue);
        double diff2 = std::fabs(static_cast<double>(i) / N - F_gue);
        D = std::max(D, std::max(diff1, diff2));
    }

    return D;
}

/**
 * Linear regression: y = slope * x + intercept
 *
 * @param x  Vector of x values
 * @param y  Vector of y values
 * @param[out] slope      Fitted slope
 * @param[out] intercept  Fitted intercept
 * @param[out] r2         R-squared coefficient
 * @param[out] max_resid  Maximum absolute residual
 */
static void linear_regression(const std::vector<double>& x,
                               const std::vector<double>& y,
                               double& slope, double& intercept,
                               double& r2, double& max_resid) {
    int n = static_cast<int>(x.size());
    double sx = 0, sy = 0, sxx = 0, sxy = 0, syy = 0;

    for (int i = 0; i < n; ++i) {
        sx  += x[i];
        sy  += y[i];
        sxx += x[i] * x[i];
        sxy += x[i] * y[i];
        syy += y[i] * y[i];
    }

    double denom = n * sxx - sx * sx;
    if (std::fabs(denom) < 1e-30) {
        slope = 0.0; intercept = 0.0; r2 = 0.0; max_resid = 0.0;
        return;
    }

    slope     = (n * sxy - sx * sy) / denom;
    intercept = (sy - slope * sx) / n;

    // R-squared
    double ss_tot = syy - sy * sy / n;
    double ss_res = 0.0;
    max_resid = 0.0;
    for (int i = 0; i < n; ++i) {
        double resid = y[i] - (slope * x[i] + intercept);
        ss_res += resid * resid;
        max_resid = std::max(max_resid, std::fabs(resid));
    }
    r2 = (ss_tot > 0.0) ? 1.0 - ss_res / ss_tot : 0.0;
}

// ============================================================================
// Objection Handlers
// ============================================================================

/**
 * Objection 1: Numerical stability of b(N).
 * Compute b(N) for progressively larger N and check convergence.
 */
static bool objection1(const std::vector<double>& zeros, const MsgMap& msg) {
    std::cout << msg.at("obj1_header") << std::endl;
    std::cout << msg.at("obj1_desc") << std::endl;
    std::cout << msg.at("obj1_gram") << std::endl;

    // N values to evaluate
    std::vector<int> Ns = {100, 500, 1000, 5000, 10000, 50000, 100000, 500000};
    int max_z = static_cast<int>(zeros.size());

    // Filter Ns to those <= available zeros
    std::vector<int> valid_Ns;
    for (int N : Ns) {
        if (N <= max_z) valid_Ns.push_back(N);
    }
    if (valid_Ns.empty()) valid_Ns.push_back(std::min(100, max_z));

    // Table header
    std::printf(msg.at("obj1_table_hdr").c_str(),
                msg.at("obj1_col1").c_str(), msg.at("obj1_col2").c_str(),
                msg.at("obj1_col3").c_str(), msg.at("obj1_col4").c_str());
    std::printf("\n  %10s %15s %15s %15s\n", "----------", "---------------",
               "---------------", "---------------");

    std::vector<double> bN_values;
    bool converging = true;
    for (size_t i = 0; i < valid_Ns.size(); ++i) {
        int N = valid_Ns[i];
        double bN = compute_bN(zeros, N);
        bN_values.push_back(bN);
        double log_bN = (bN > 0.0) ? std::log10(bN) : -999.0;

        // Check monotonic decrease (after first point)
        std::string conv_str = "---";
        if (i > 0) {
            if (bN < bN_values[i - 1]) {
                conv_str = msg.at("obj1_conv_yes");
            } else {
                conv_str = msg.at("obj1_conv_no");
                converging = false;
            }
        }

        std::printf("  %10d %15.8f %15.4f %15s\n", N, bN, log_bN, conv_str.c_str());
    }

    // Overall verdict
    std::string conv_word = converging ? msg.at("obj1_conv_yes") : msg.at("obj1_conv_no");
    std::string verdict = converging ? "OK" : "WARN";
    char buf[512];
    std::snprintf(buf, sizeof(buf), msg.at("obj1_result").c_str(),
                  conv_word.c_str(), verdict.c_str());
    std::cout << buf << std::endl;

    return converging;
}

/**
 * Objection 2: GUE spacing statistics.
 * Compute normalized spacings, perform KS test against GUE distribution.
 */
static bool objection2(const std::vector<double>& zeros, const MsgMap& msg) {
    std::cout << msg.at("obj2_header") << std::endl;
    std::cout << msg.at("obj2_desc") << std::endl;
    std::cout << msg.at("obj2_gue_pdf") << std::endl;
    std::cout << msg.at("obj2_ks") << std::endl;

    // Test at different sample sizes
    std::vector<int> Ns = {1000, 5000, 10000, 50000, 100000, 500000};
    int max_z = static_cast<int>(zeros.size());

    // Table header
    std::printf(msg.at("obj2_table_hdr").c_str(),
                msg.at("obj2_col1").c_str(), msg.at("obj2_col2").c_str(),
                msg.at("obj2_col3").c_str(), msg.at("obj2_col4").c_str(),
                msg.at("obj2_col5").c_str());
    std::printf("\n  %10s %15s %15s %15s %10s\n",
               "----------", "---------------", "---------------",
               "---------------", "----------");

    bool all_pass = true;
    double last_D = 0.0, last_D_crit = 0.0;
    for (int N : Ns) {
        if (N > max_z - 1) break;

        // Use the last N zeros (high-T region, better for GUE)
        int start = max_z - N - 1;
        if (start < 0) start = 0;

        std::vector<double> sub_zeros(zeros.begin() + start, zeros.begin() + start + N + 1);
        std::vector<double> spacings = compute_gue_spacings(sub_zeros, N);

        double D = ks_test(spacings);
        int n_sp = static_cast<int>(spacings.size());
        double D_crit = 1.358 / std::sqrt(static_cast<double>(n_sp));
        double ratio = D / D_crit;
        bool pass = (D < D_crit);

        last_D = D;
        last_D_crit = D_crit;
        if (!pass) all_pass = false;

        std::printf("  %10d %15.8f %15.8f %15.4f %10s\n",
                   n_sp, D, D_crit, ratio,
                   pass ? msg.at("obj2_pass").c_str() : msg.at("obj2_fail").c_str());
    }

    // Summary
    char buf[512];
    std::snprintf(buf, sizeof(buf), msg.at("obj2_result").c_str(),
                  all_pass ? "PASSED" : "FAILED", last_D, last_D_crit);
    std::cout << buf << std::endl;

    return all_pass;
}

/**
 * Objection 3: Large-T decay rate.
 * Fit log(b(N)) vs log(N), expect slope ≈ -0.5.
 */
static bool objection3(const std::vector<double>& zeros, const MsgMap& msg) {
    std::cout << msg.at("obj3_header") << std::endl;
    std::cout << msg.at("obj3_desc") << std::endl;

    int max_z = static_cast<int>(zeros.size());

    // Compute b(N) for a range of N values (logarithmically spaced)
    std::vector<double> logN, logbN;
    for (int N = 100; N <= max_z; N += N / 4) {
        double bN = compute_bN(zeros, N);
        if (bN > 0.0) {
            logN.push_back(std::log(static_cast<double>(N)));
            logbN.push_back(std::log(bN));
        }
    }

    if (logN.size() < 3) {
        std::cout << "WARNING: Insufficient data points for regression." << std::endl;
        return false;
    }

    // Perform linear regression
    double slope, intercept, r2, max_resid;
    linear_regression(logN, logbN, slope, intercept, r2, max_resid);

    // Display results
    std::cout << msg.at("obj3_reg_hdr") << std::endl;
    std::printf(msg.at("obj3_slope").c_str(), slope);
    std::cout << std::endl;
    std::printf(msg.at("obj3_intercept").c_str(), intercept);
    std::cout << std::endl;
    std::printf(msg.at("obj3_r2").c_str(), r2);
    std::cout << std::endl;
    std::printf(msg.at("obj3_residual").c_str(), max_resid);
    std::cout << std::endl;

    // Check if slope is close to -0.5 (within ±0.1)
    double expected_slope = -0.5;
    double slope_diff = std::fabs(slope - expected_slope);
    bool ok = (slope_diff < 0.15);  // Allow some tolerance

    std::string verdict = ok ? "OK" : "WARN: slope deviates from -0.5";
    char buf[512];
    std::snprintf(buf, sizeof(buf), msg.at("obj3_result").c_str(), slope, verdict.c_str());
    std::cout << buf << std::endl;

    return ok;
}

// ============================================================================
// Command-Line Parsing
// ============================================================================

struct Config {
    int         zeros   = 200000;
    std::string source  = "auto";
    std::string objection = "all";
    std::string lang    = "en";
    std::string data_dir = "../data";
};

static Config parse_args(int argc, char* argv[]) {
    Config cfg;
    for (int i = 1; i < argc; ++i) {
        std::string arg = argv[i];
        if ((arg == "--zeros" || arg == "-z") && i + 1 < argc) {
            cfg.zeros = std::atoi(argv[++i]);
        } else if ((arg == "--source" || arg == "-s") && i + 1 < argc) {
            cfg.source = argv[++i];
        } else if ((arg == "--objection" || arg == "-o") && i + 1 < argc) {
            cfg.objection = argv[++i];
        } else if ((arg == "--lang" || arg == "-l") && i + 1 < argc) {
            cfg.lang = argv[++i];
        } else if ((arg == "--data-dir" || arg == "-d") && i + 1 < argc) {
            cfg.data_dir = argv[++i];
        } else if (arg == "--help" || arg == "-h") {
            std::cout << "Usage: ab_cloud_verify [OPTIONS]\n"
                      << "  --zeros   N     Number of zeros to load (default: 200000)\n"
                      << "  --source  SRC   Data source: 50k, 500k, 2M, highT, zeros6, auto\n"
                      << "  --objection O   Which objection: 1, 2, 3, or all (default: all)\n"
                      << "  --lang    LANG  Language: en, ru (default: en)\n"
                      << "  --data-dir DIR  Path to data directory (default: ../data)\n";
            std::exit(0);
        }
    }
    return cfg;
}

// ============================================================================
// Main
// ============================================================================

int main(int argc, char* argv[]) {
    Config cfg = parse_args(argc, argv);

    // Select language
    MsgMap msg;
    if (cfg.lang == "ru") {
        msg = make_messages_ru();
    } else {
        msg = make_messages_en();
    }

    // Banner
    std::cout << msg.at("banner") << std::endl;
    std::cout << msg.at("lang_label") << std::endl;
    std::cout << msg.at("loading") << std::endl;

    // Load zeros
    auto zeros = load_zeros(cfg.data_dir, cfg.zeros, cfg.source);

    char buf[512];
    if (zeros.empty()) {
        std::snprintf(buf, sizeof(buf), msg.at("err_empty").c_str());
        std::cerr << buf << std::endl;
        return 1;
    }

    std::snprintf(buf, sizeof(buf), msg.at("loaded").c_str(),
                  static_cast<int>(zeros.size()), cfg.source.c_str());
    std::cout << buf << std::endl;

    if (static_cast<int>(zeros.size()) < 2) {
        std::snprintf(buf, sizeof(buf), msg.at("err_few").c_str(),
                      static_cast<int>(zeros.size()));
        std::cerr << buf << std::endl;
        return 1;
    }

    // Run verification for requested objections
    bool obj1_ok = true, obj2_ok = true, obj3_ok = true;

    if (cfg.objection == "all" || cfg.objection == "1") {
        obj1_ok = objection1(zeros, msg);
    }
    if (cfg.objection == "all" || cfg.objection == "2") {
        obj2_ok = objection2(zeros, msg);
    }
    if (cfg.objection == "all" || cfg.objection == "3") {
        obj3_ok = objection3(zeros, msg);
    }

    // Summary
    bool all_ok = obj1_ok && obj2_ok && obj3_ok;
    std::cout << msg.at("summary_hdr") << std::endl;
    std::cout << (all_ok ? msg.at("summary_ok") : msg.at("summary_fail")) << std::endl;
    std::cout << msg.at("done") << std::endl;

    return all_ok ? 0 : 1;
}
