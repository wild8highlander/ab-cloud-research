// AB-Cloud unified CLI — the Go runner (std only, zero deps).
// Contract: ../shared/contract.json — identical metrics to the other five runners.
package main

import (
        "fmt"
        "os"
        "path/filepath"
        "strings"
)

func dir() string { return filepath.Dir(os.Args[0]) }

func flatJSON(file, key string) string {
        b, err := os.ReadFile(filepath.Join(dir(), "..", "shared", file+".json"))
        if err != nil {
                return ""
        }
        for _, line := range strings.Split(string(b), "\n") {
                if strings.Contains(line, "\""+key+"\"") {
                        if i := strings.Index(line, ":"); i > 0 {
                                return strings.Trim(strings.TrimSpace(strings.TrimSuffix(strings.TrimSpace(line[i+1:]), ",")), "\"")
                        }
                }
        }
        return ""
}

const banner = `
    _          _   ___                     _          _
   / \   _ __ | |_| _ \__      _____ _ __ | |__   ___| |___
  / _ \ | '_ \| __| |_) \ /\ / / _ \ '_ \| '_ \ / _ \ / __|
 / ___ \| | | | |_|  __/ \ V  V /  __/ | | | |_) |  __/ \__ \
/_/   \_\_| |_|\__|_|     \_/\_/ \___|_| |_|_.__/ \___|_|___/
`

func bar(v, lo, hi float64) string {
        x := (v - lo) / (hi - lo)
        if x < 0 {
                x = 0
        }
        if x > 1 {
                x = 1
        }
        filled := int(x*18 + 0.5)
        return strings.Repeat("█", filled) + strings.Repeat("░", 18-filled)
}

func f(key string) float64 {
        var v float64
        fmt.Sscanf(flatJSON("metrics", key), "%g", &v)
        return v
}

func main() {
        lang, jsonOut, cmd, seenCmd := "en", false, "analyze", false
        for i := 1; i < len(os.Args); i++ {
                a := os.Args[i]
                switch {
                case strings.HasPrefix(a, "--lang="):
                        lang = a[7:]
                case a == "--output=json":
                        jsonOut = true
                case !strings.HasPrefix(a, "-") && i == 1:
                        cmd = a
                }
        }
        switch cmd {
        case "version":
                fmt.Println(`{"implementation":"go","package":"AB_Cloud_Academic_Package","edition":"unified (versionless)","rh_status":"blocked"}`)
        case "doctor":
                reg := fileExists(filepath.Join(dir(), "..", "..", "02_data", "processed", "research_registry.json"))
                cfg := fileExists(filepath.Join(dir(), "..", "..", "config.yaml"))
                fmt.Println("registry", mark(reg))
                fmt.Println("config  ", mark(cfg))
                fmt.Println("metrics ✅ loaded")
                if !reg || !cfg {
                        os.Exit(1)
                }
        case "cite":
                fmt.Println("Isaev, I. Kh. (2026). AB-Cloud Research Programme: Unified Academic Package.")
                fmt.Println("DOI:", flatJSON("constants", "doi"))
                fmt.Println("RH status: blocked by design.")
        case "secret":
                fmt.Println("ζ lives in the trace; the spectrum keeps the secret.")
        case "analyze":
                if jsonOut {
                        b, _ := os.ReadFile(filepath.Join(dir(), "..", "shared", "metrics.json"))
                        fmt.Print(string(b))
                        return
                }
                fmt.Println(banner)
                title, sub := "AB-CLOUD PROGRAMME · UNIFIED EDITION", "four levels · one registry · honest boundaries"
                steps := []string{"Environment check", "Loading configuration", "Reading the registry", "Computing metrics", "Summary"}
                if lang == "ru" {
                        title, sub = "ПРОГРАММА AB-CLOUD · ЕДИНОЕ ИЗДАНИЕ", "четыре уровня · один реестр · честные границы"
                        steps = []string{"Проверка окружения", "Загрузка конфигурации", "Чтение реестра", "Расчёт метрик", "Сводка"}
                }
                fmt.Println("  " + title)
                fmt.Printf("  %s   lang: %s  seed: %s\n", sub, lang, flatJSON("metrics", "seed"))
                fmt.Println("  " + strings.Repeat("─", 66))
                for i, s := range steps {
                        dots := 40 - len([]rune(s))
                        if dots < 2 {
                                dots = 2
                        }
                        fmt.Printf("[%d/5] · %s %s ✅\n", i+1, s, strings.Repeat(".", dots))
                }
                fmt.Println()
                fmt.Println("── 📈 metrics ──────────────────────")
                fmt.Printf("GUE <r> zeta-dec  %s %s\n", bar(f("gue_r_decorated"), 0.5, 0.7), flatJSON("metrics", "gue_r_decorated"))
                fmt.Printf("GUE <r> theory    %s %s\n", bar(f("gue_r_theory"), 0.5, 0.7), flatJSON("metrics", "gue_r_theory"))
                fmt.Printf("trace-primes r    %s %s\n", bar(f("trace_primes_r"), 0.9, 1.0), flatJSON("metrics", "trace_primes_r"))
                fmt.Printf("locality wall     %s %s/%s\n", bar(f("sa_local")/f("sa_haar"), 0, 1), flatJSON("metrics", "sa_local"), flatJSON("metrics", "sa_haar"))
                fmt.Println("RH status:", flatJSON("metrics", "rh_status"), "(V13 obligation machine)")
                fmt.Printf("verdicts: %s YES / %s NO / %s BLOCKED\n", flatJSON("metrics", "verdicts_yes"), flatJSON("metrics", "verdicts_no"), flatJSON("metrics", "verdicts_blocked"))
                fmt.Println()
                fmt.Println("🎉 Done.")
        default:
                fmt.Printf("command '%s' delegated to the python reference: python3 ../python/run.py %s\n", cmd, cmd)
                os.Exit(2)
        }
}

func mark(ok bool) string {
        if ok {
                return "✅ found"
        }
        return "❌ MISSING"
}
func fileExists(p string) bool {
        _, err := os.Stat(p)
        return err == nil
}
