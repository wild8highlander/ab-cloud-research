// spinor38.cpp — Test 38: 64 spinor structures of the Klein quartic (C++ port)
//
// Verifies, using ONLY the frozen data files and a self-implemented cyclic
// Jacobi eigenvalue algorithm (no BLAS/LAPACK):
//   1. the 28 odd (Arf=1) spinor structures of the Klein quartic are exactly
//      isospectral (max pairwise spectral distance ~ 1e-14) — no spinor
//      structure is unique (corrects the v21 monograph claim about idx=38);
//   2. the spacing-ratio statistic <r> of the representative spectrum matches
//      the reference value 0.4515710792825435.
//
// Build:  g++ -O2 -std=c++17 -o spinor38 spinor38.cpp
// Run:    ./spinor38 [path/to/repo-root]   (default: walk up from CWD)
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <string>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>

struct ClassRow { int cls; int orbit; int arf; std::vector<double> signs; };

static std::string slurp(const std::string& path) {
    std::ifstream f(path.c_str());
    if (!f) { std::fprintf(stderr, "cannot open %s\n", path.c_str()); std::exit(2); }
    std::ostringstream ss; ss << f.rdbuf(); return ss.str();
}

static std::string find_data_dir(const char* override_root) {
    std::string roots[2];
    if (override_root && override_root[0]) roots[0] = override_root;
    roots[1] = ".";
    for (int r = 0; r < 2; ++r) {
        std::string base = roots[r];
        for (int up = 0; up < 6; ++up) {
            std::string cand = base + "/verification/spinor64/data/spinor_classes.csv";
            std::ifstream f(cand.c_str());
            if (f) return base + "/verification/spinor64/data";
            base += "/..";
        }
    }
    std::fprintf(stderr, "data dir not found; pass repo root as argument\n");
    std::exit(2);
}

// classic cyclic Jacobi eigenvalue algorithm for a real symmetric matrix
static void jacobi_eigenvalues(std::vector<std::vector<double> >& A,
                               std::vector<double>& eig) {
    int n = (int)A.size();
    for (int sweep = 0; sweep < 200; ++sweep) {
        double off = 0.0;
        for (int p = 0; p < n; ++p)
            for (int q = p + 1; q < n; ++q) off += A[p][q] * A[p][q];
        if (off < 1e-24) break;
        for (int p = 0; p < n; ++p) {
            for (int q = p + 1; q < n; ++q) {
                if (std::fabs(A[p][q]) < 1e-15) continue;
                double tau = (A[q][q] - A[p][p]) / (2.0 * A[p][q]);
                double t = (tau >= 0.0 ? 1.0 : -1.0) /
                           (std::fabs(tau) + std::sqrt(1.0 + tau * tau));
                double c = 1.0 / std::sqrt(1.0 + t * t);
                double s = t * c;
                for (int k = 0; k < n; ++k) {
                    double akp = A[k][p], akq = A[k][q];
                    A[k][p] = c * akp - s * akq;
                    A[k][q] = s * akp + c * akq;
                }
                for (int k = 0; k < n; ++k) {
                    double apk = A[p][k], aqk = A[q][k];
                    A[p][k] = c * apk - s * aqk;
                    A[q][k] = s * apk + c * aqk;
                }
            }
        }
    }
    eig.resize(n);
    for (int i = 0; i < n; ++i) eig[i] = A[i][i];
    std::sort(eig.begin(), eig.end());
}

int main(int argc, char** argv) {
    const char* root = (argc > 1) ? argv[1] : nullptr;
    std::string dd = find_data_dir(root);

    std::vector<ClassRow> classes;
    {
        std::istringstream in(slurp(dd + "/spinor_classes.csv"));
        std::string line;
        std::getline(in, line); // header
        while (std::getline(in, line)) {
            if (line.empty()) continue;
            size_t p1 = line.find(','), p2 = line.find(',', p1 + 1),
                   p3 = line.find(',', p2 + 1);
            ClassRow row;
            row.cls = std::atoi(line.substr(0, p1).c_str());
            row.orbit = std::atoi(line.substr(p1 + 1, p2 - p1 - 1).c_str());
            row.arf = std::atoi(line.substr(p2 + 1, p3 - p2 - 1).c_str());
            std::istringstream ss(line.substr(p3 + 1));
            double v;
            while (ss >> v) row.signs.push_back(v);
            classes.push_back(row);
        }
    }
    std::vector<int> eu, ev;
    {
        std::istringstream in(slurp(dd + "/klein_graph_edges.csv"));
        std::string line;
        std::getline(in, line);
        while (std::getline(in, line)) {
            if (line.empty()) continue;
            size_t p1 = line.find(','), p2 = line.find(',', p1 + 1);
            eu.push_back(std::atoi(line.substr(p1 + 1, p2 - p1 - 1).c_str()));
            ev.push_back(std::atoi(line.substr(p2 + 1).c_str()));
        }
    }
    double r_ref = 0.0; int n_zero_ref = 0; int representative = 0;
    {
        std::string js = slurp(dd + "/reference_stats.json");
        const char* pat = "\"r_mean_reference\":";
        const char* p = std::strstr(js.c_str(), pat);
        if (p) r_ref = std::atof(p + std::strlen(pat));
        pat = "\"n_zero_modes\":";
        p = std::strstr(js.c_str(), pat);
        if (p) n_zero_ref = std::atoi(p + std::strlen(pat));
        pat = "\"representative_class\":";
        p = std::strstr(js.c_str(), pat);
        if (p) representative = std::atoi(p + std::strlen(pat));
    }

    const int N = 56;
    int n_odd = 0;
    for (size_t i = 0; i < classes.size(); ++i)
        if (classes[i].orbit == 0) n_odd++;

    std::vector<std::vector<double> > spectra;
    std::vector<double> rep_spectrum;
    for (size_t i = 0; i < classes.size(); ++i) {
        if (classes[i].orbit != 0) continue;
        std::vector<std::vector<double> > A(N, std::vector<double>(N, 0.0));
        for (size_t k = 0; k < eu.size(); ++k) {
            double s = classes[i].signs[k];
            A[eu[k]][ev[k]] = s;
            A[ev[k]][eu[k]] = s;
        }
        std::vector<double> w;
        jacobi_eigenvalues(A, w);
        if ((int)classes[i].cls == representative) rep_spectrum = w;
        spectra.push_back(w);
    }

    double isomax = 0.0;
    for (size_t a = 0; a < spectra.size(); ++a)
        for (size_t b = a + 1; b < spectra.size(); ++b)
            for (int i = 0; i < N; ++i) {
                double d = std::fabs(spectra[a][i] - spectra[b][i]);
                if (d > isomax) isomax = d;
            }

    int n_zero = 0;
    std::vector<double> lam;
    for (int i = 0; i < N; ++i) {
        if (std::fabs(rep_spectrum[i]) < 1e-8) n_zero++;
        lam.push_back(std::fabs(rep_spectrum[i]));  // fold |lambda| (zeros kept)
    }
    std::sort(lam.begin(), lam.end());
    // spacings; drop the zero spacing between the two zero modes
    std::vector<double> dsp;
    for (int i = 0; i + 1 < N; ++i) {
        double d = lam[i + 1] - lam[i];
        if (d > 1e-8) dsp.push_back(d);
    }
    double rsum = 0.0; int nr = 0;
    for (size_t i = 0; i + 1 < dsp.size(); ++i) {
        double mn = std::min(dsp[i], dsp[i + 1]);
        double mx = std::max(dsp[i], dsp[i + 1]);
        rsum += mn / mx; nr++;
    }
    double r_mean = rsum / nr;

    printf("Test 38 - 64 spinor structures of the Klein quartic (C++ port)\n");
    printf("classes loaded: %d | odd-orbit members: %d\n", (int)classes.size(), n_odd);
    printf("isospectrality within the odd orbit: max|dlambda| = %.3e -> %s\n",
           isomax, isomax < 1e-9 ? "PASS" : "FAIL");
    printf("zero modes (representative): %d (expected %d)\n", n_zero, n_zero_ref);
    printf("<r> (representative): %.10f (reference 0.4515710793) -> %s\n",
           r_mean, std::fabs(r_mean - r_ref) < 1e-6 ? "PASS" : "FAIL");
    bool ok = (isomax < 1e-9) && (n_zero == n_zero_ref) &&
              (std::fabs(r_mean - r_ref) < 1e-6);
    printf("VERDICT: %s\n", ok ? "PASS" : "FAIL");
    return ok ? 0 : 1;
}
