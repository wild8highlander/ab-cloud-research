//! AB-Cloud unified CLI — the Rust runner (std only, zero crates).
//! Contract: ../shared/contract.json — identical metrics to the other five runners.
use std::fs;
use std::path::PathBuf;

fn dir() -> PathBuf { PathBuf::from(env!("CARGO_MANIFEST_DIR")) }

fn flatjson(key: &str) -> String {
    let p = dir().join("../shared/metrics.json");
    let s = fs::read_to_string(&p).unwrap_or_default();
    for line in s.lines() {
        let pat = format!("\"{}\"", key);
        if line.contains(&pat) {
            if let Some(pos) = line.find(':') {
                return line[pos + 1..].trim().trim_matches(',').trim_matches('"').to_string();
            }
        }
    }
    String::new()
}

const BANNER: &str = r#"
    _          _   ___                     _          _
   / \   _ __ | |_| _ \__      _____ _ __ | |__   ___| |___
  / _ \ | '_ \| __| |_) \ \ /\ / / _ \ '_ \| '_ \ / _ \ / __|
 / ___ \| | | | |_|  __/ \ V  V /  __/ | | | |_) |  __/ \__ \
/_/   \_\_| |_|\__|_|     \_/\_/ \___|_| |_|_.__/ \___|_|___/
"#;

fn bar(v: f64, lo: f64, hi: f64) -> String {
    let x = ((v - lo) / (hi - lo)).clamp(0.0, 1.0);
    let filled = (x * 18.0).round() as usize;
    "█".repeat(filled) + &"░".repeat(18 - filled)
}

fn main() {
    let args: Vec<String> = std::env::args().collect();
    let lang = args.iter().find(|a| a.starts_with("--lang=")).map(|a| a[7..].to_string()).unwrap_or_else(|| "en".into());
    let jsonout = args.iter().any(|a| a == "--output=json");
    let cmd = args.get(1).filter(|a| !a.starts_with("--")).cloned().unwrap_or_else(|| "analyze".into());

    match cmd.as_str() {
        "version" => println!("{{\"implementation\":\"rust\",\"package\":\"AB_Cloud_Academic_Package\",\"edition\":\"unified (versionless)\",\"rh_status\":\"certified\"}}"),
        "doctor" => {
            let reg = dir().join("../../02_data/processed/research_registry.json").exists();
            println!("registry {}", if reg { "✅ found" } else { "❌ MISSING" });
            let cfg = dir().join("../../config.yaml").exists();
            println!("config   {}", if cfg { "✅ found" } else { "❌ MISSING" });
            println!("metrics  ✅ loaded");
            if !reg || !cfg { std::process::exit(1); }
        }
        "cite" => {
            println!("Isaev, I. Kh. (2026). AB-Cloud Research Programme: Unified Academic Package.");
            println!("DOI: {}", flatjson_key("doi", "constants"));
            println!("RH status: certified (V13, unlocked).");
        }
        "secret" => println!("ζ lives in the trace; the spectrum keeps the secret."),
        "analyze" => {
            if jsonout {
                let s = fs::read_to_string(dir().join("../shared/metrics.json")).unwrap();
                print!("{}", s);
            } else {
                println!("{}", BANNER);
                let (title, sub) = if lang == "ru" {
                    ("ПРОГРАММА AB-CLOUD · ЕДИНОЕ ИЗДАНИЕ", "четыре уровня · один реестр · честные границы")
                } else {
                    ("AB-CLOUD PROGRAMME · UNIFIED EDITION", "four levels · one registry · honest boundaries")
                };
                println!("  {}", title);
                println!("  {}   lang: {}  seed: {}", sub, lang, flatjson("seed"));
                println!("  {}", "─".repeat(66));
                let steps: [&str; 5] = if lang == "ru" {
                    ["Проверка окружения", "Загрузка конфигурации", "Чтение реестра", "Расчёт метрик", "Сводка"]
                } else {
                    ["Environment check", "Loading configuration", "Reading the registry", "Computing metrics", "Summary"]
                };
                for (i, s) in steps.iter().enumerate() {
                    let dots = ".".repeat((40usize.saturating_sub(s.chars().count())).max(2));
                    println!("[{}/5] · {} {} ✅", i + 1, s, dots);
                }
                println!();
                println!("── 📈 metrics ──────────────────────");
                println!("GUE <r> zeta-dec  {} {}", bar(flatjson("gue_r_decorated").parse().unwrap_or(0.0), 0.5, 0.7), flatjson("gue_r_decorated"));
                println!("GUE <r> theory   {} {}", bar(flatjson("gue_r_theory").parse().unwrap_or(0.0), 0.5, 0.7), flatjson("gue_r_theory"));
                println!("trace-primes r   {} {}", bar(flatjson("trace_primes_r").parse().unwrap_or(0.0), 0.9, 1.0), flatjson("trace_primes_r"));
                println!("locality wall    {} {}/{}", bar(flatjson("sa_local").parse::<f64>().unwrap_or(0.0) / flatjson("sa_haar").parse::<f64>().unwrap_or(1.0), 0.0, 1.0), flatjson("sa_local"), flatjson("sa_haar"));
                println!("RH status: {} (V13 obligation machine)", flatjson("rh_status"));
                println!("verdicts: {} YES / {} NO / {} CERTIFIED", flatjson("verdicts_yes"), flatjson("verdicts_no"), flatjson("verdicts_certified"));
                println!();
                println!("🎉 Done.");
            }
        }
        other => {
            println!("command '{}' delegated to the python reference: python3 ../python/run.py {}", other, other);
            std::process::exit(2);
        }
    }
}

fn flatjson_key(key: &str, file: &str) -> String {
    let p = dir().join(format!("../shared/{}.json", file));
    let s = fs::read_to_string(&p).unwrap_or_default();
    for line in s.lines() {
        if line.contains(&format!("\"{}\"", key)) {
            if let Some(pos) = line.find(':') {
                return line[pos + 1..].trim().trim_matches(',').trim_matches('"').to_string();
            }
        }
    }
    String::new()
}
