import java.io.*;
import java.nio.file.*;
import java.util.*;

/**
 * Spinor38.java — Test 38: 64 spinor structures of the Klein quartic (Java port).
 * Self-implemented cyclic Jacobi eigenvalue algorithm (JDK only, no libs).
 * Build: javac Spinor38.java   Run: java Spinor38 [repo-root]
 */
public class Spinor38 {

    static class Cls { int cls, orbit, arf; double[] signs; }

    static Path findDataDir(String rootArg) {
        List<String> roots = new ArrayList<>();
        if (rootArg != null) roots.add(rootArg);
        roots.add(System.getProperty("user.dir"));
        for (String r : roots) {
            Path b = Paths.get(r).toAbsolutePath().normalize();
            for (int up = 0; up < 6; up++) {
                Path cand = b.resolve(Paths.get("verification", "spinor64",
                        "data", "spinor_classes.csv"));
                if (Files.exists(cand)) return b.resolve(Paths.get("verification",
                        "spinor64", "data"));
                b = b.getParent();
                if (b == null) break;
            }
        }
        System.err.println("data dir not found; pass repo root as argument");
        System.exit(2);
        return null;
    }

    static List<String> readLines(Path p) throws IOException {
        return Files.readAllLines(p);
    }

    // cyclic Jacobi eigenvalues of a real symmetric matrix
    static double[] jacobiEigen(double[][] Ain) {
        int n = Ain.length;
        double[][] A = new double[n][n];
        for (int i = 0; i < n; i++) A[i] = Ain[i].clone();
        for (int sweep = 0; sweep < 200; sweep++) {
            double off = 0;
            for (int p = 0; p < n; p++)
                for (int q = p + 1; q < n; q++) off += A[p][q] * A[p][q];
            if (off < 1e-24) break;
            for (int p = 0; p < n; p++) {
                for (int q = p + 1; q < n; q++) {
                    if (Math.abs(A[p][q]) < 1e-15) continue;
                    double tau = (A[q][q] - A[p][p]) / (2 * A[p][q]);
                    double t = (tau >= 0 ? 1 : -1) /
                            (Math.abs(tau) + Math.sqrt(1 + tau * tau));
                    double c = 1 / Math.sqrt(1 + t * t);
                    double s = t * c;
                    for (int k = 0; k < n; k++) {
                        double akp = A[k][p], akq = A[k][q];
                        A[k][p] = c * akp - s * akq;
                        A[k][q] = s * akp + c * akq;
                    }
                    for (int k = 0; k < n; k++) {
                        double apk = A[p][k], aqk = A[q][k];
                        A[p][k] = c * apk - s * aqk;
                        A[q][k] = s * apk + c * aqk;
                    }
                }
            }
        }
        double[] eig = new double[n];
        for (int i = 0; i < n; i++) eig[i] = A[i][i];
        Arrays.sort(eig);
        return eig;
    }

    public static void main(String[] args) throws IOException {
        Path dd = findDataDir(args.length > 0 ? args[0] : null);
        List<Cls> classes = new ArrayList<>();
        boolean first = true;
        for (String line : readLines(dd.resolve("spinor_classes.csv"))) {
            if (first) { first = false; continue; }
            if (line.isEmpty()) continue;
            String[] head = line.split(",", 4);
            Cls c = new Cls();
            c.cls = Integer.parseInt(head[0]);
            c.orbit = Integer.parseInt(head[1]);
            c.arf = Integer.parseInt(head[2]);
            String[] sgn = head[3].trim().split("\\s+");
            c.signs = new double[sgn.length];
            for (int i = 0; i < sgn.length; i++) c.signs[i] = Double.parseDouble(sgn[i]);
            classes.add(c);
        }
        List<int[]> edges = new ArrayList<>();
        first = true;
        for (String line : readLines(dd.resolve("klein_graph_edges.csv"))) {
            if (first) { first = false; continue; }
            if (line.isEmpty()) continue;
            String[] p = line.split(",");
            edges.add(new int[]{Integer.parseInt(p[1]), Integer.parseInt(p[2])});
        }
        String js = new String(Files.readAllBytes(dd.resolve("reference_stats.json")));
        double rRef = Double.parseDouble(extractJson(js, "r_mean_reference"));
        int nZeroRef = (int) Double.parseDouble(extractJson(js, "n_zero_modes"));
        int representative = (int) Double.parseDouble(extractJson(js, "representative_class"));

        final int N = 56;
        int nOdd = 0;
        for (Cls c : classes) if (c.orbit == 0) nOdd++;

        List<double[]> spectra = new ArrayList<>();
        double[] repSpectrum = null;
        for (Cls c : classes) {
            if (c.orbit != 0) continue;
            double[][] A = new double[N][N];
            for (int k = 0; k < edges.size(); k++) {
                int u = edges.get(k)[0], v = edges.get(k)[1];
                double s = c.signs[k];
                A[u][v] = s; A[v][u] = s;
            }
            double[] w = jacobiEigen(A);
            if (c.cls == representative) repSpectrum = w;
            spectra.add(w);
        }

        double isomax = 0;
        for (int a = 0; a < spectra.size(); a++)
            for (int b = a + 1; b < spectra.size(); b++)
                for (int i = 0; i < N; i++)
                    isomax = Math.max(isomax, Math.abs(spectra.get(a)[i] - spectra.get(b)[i]));

        int nZero = 0;
        double[] lam = new double[N];
        for (int i = 0; i < N; i++) {
            lam[i] = Math.abs(repSpectrum[i]);
            if (lam[i] < 1e-8) nZero++;
        }
        Arrays.sort(lam);
        List<Double> dsp = new ArrayList<>();
        for (int i = 0; i + 1 < N; i++) {
            double d = lam[i + 1] - lam[i];
            if (d > 1e-8) dsp.add(d);
        }
        double rsum = 0;
        for (int i = 0; i + 1 < dsp.size(); i++) {
            double mn = Math.min(dsp.get(i), dsp.get(i + 1));
            double mx = Math.max(dsp.get(i), dsp.get(i + 1));
            rsum += mn / mx;
        }
        double rMean = rsum / (dsp.size() - 1);

        System.out.println("Test 38 - 64 spinor structures of the Klein quartic (Java port)");
        System.out.printf("classes loaded: %d | odd-orbit members: %d%n", classes.size(), nOdd);
        System.out.printf("isospectrality within the odd orbit: max|dlambda| = %.3e -> %s%n",
                isomax, isomax < 1e-9 ? "PASS" : "FAIL");
        System.out.printf("zero modes (representative): %d (expected %d)%n", nZero, nZeroRef);
        boolean rOk = Math.abs(rMean - rRef) < 1e-6;
        System.out.printf("<r> (representative): %.10f (reference 0.4515710793) -> %s%n",
                rMean, rOk ? "PASS" : "FAIL");
        boolean ok = isomax < 1e-9 && nZero == nZeroRef && rOk;
        System.out.println("VERDICT: " + (ok ? "PASS" : "FAIL"));
        System.exit(ok ? 0 : 1);
    }

    static String extractJson(String js, String key) {
        int i = js.indexOf("\"" + key + "\":");
        if (i < 0) return "0";
        int j = i + key.length() + 3;
        int k = j;
        while (k < js.length() && "0123456789.eE-".indexOf(js.charAt(k)) >= 0) k++;
        return js.substring(j, k);
    }
}
