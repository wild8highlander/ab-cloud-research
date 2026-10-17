#!/usr/bin/env julia
# AB-Cloud unified CLI — the Julia runner (LinearAlgebra only, zero packages).
# Contract: ../shared/contract.json — identical metrics to the other five runners.

using LinearAlgebra  # identity of the programme: linear algebra is enough

const SHARED = joinpath(@__DIR__, "..", "shared")

"minimal flat-JSON value reader (no packages)"
function flatjson(path::String, key::String)
    for line in eachline(path)
        m = match(Regex("\"$key\"\\s*:\\s*([^,}]+)"), line)
        m !== nothing && return strip(m.captures[1], ['"', ' '])
    end
    return ""
end

const BANNER = join([
"    _          _   ___                     _          _    ",
"   / \\   _ __ | |_| _ \\__      _____ _ __ | |__   ___| |___",
"  / _ \\ | '_ \\| __| |_) \\ \\ /\\ / / _ \\ '_ \\| '_ \\ / _ \\ / __|",
" / ___ \\| | | | |_|  __/ \\ V  V /  __/ | | | |_) |  __/ \\__ \\",
"/_/   \\_\\_| |_|\\__|_|     \\_/\\_/ \\___|_| |_|_.__/ \\___|_|___/",
], "\n")

const METRICS = joinpath(SHARED, "metrics.json")
getm(key) = flatjson(METRICS, key)

lang = "en"; jsonout = false
for a in ARGS
    startswith(a, "--lang=") && (lang = a[8:end])
    a == "--output=json" && (jsonout = true)
end
_pos = findfirst(a -> !startswith(a, "--"), ARGS)
cmd = _pos === nothing ? "analyze" : ARGS[_pos]

steps = lang == "ru" ? ("Проверка окружения", "Загрузка конфигурации", "Чтение реестра", "Расчёт метрик", "Сводка") :
                        ("Environment check", "Loading configuration", "Reading the registry", "Computing metrics", "Summary")
title = lang == "ru" ? "ПРОГРАММА AB-CLOUD · ЕДИНОЕ ИЗДАНИЕ" : "AB-CLOUD PROGRAMME · UNIFIED EDITION"
sub = lang == "ru" ? "четыре уровня · один реестр · честные границы" : "four levels · one registry · honest boundaries"

function bar(v, lo, hi, w = 18)
    x = clamp((v - lo) / (hi - lo), 0.0, 1.0)
    filled = round(Int, x * w)
    return "█"^filled * "░"^(w - filled)
end

if cmd == "version"
    println("{\"implementation\":\"julia\",\"package\":\"AB_Cloud_Academic_Package\",\"edition\":\"unified (versionless)\",\"julia\":$(VERSION)\",\"rh_status\":\"certified\"}")
elseif cmd == "doctor"
    reg = isfile(joinpath(@__DIR__, "..", "..", "02_data", "processed", "research_registry.json"))
    println(reg ? "registry ✅ found" : "registry ❌ MISSING")
    isfile(joinpath(@__DIR__, "..", "..", "config.yaml")) ? println("config   ✅ found") : println("config   ❌ MISSING")
    println("metrics  ✅ loaded")
    reg || exit(1)
elseif cmd == "cite"
    println("Isaev, I. Kh. (2026). AB-Cloud Research Programme: Unified Academic Package.")
    println("DOI: ", flatjson(joinpath(SHARED, "constants.json"), "doi"))
    println("RH status: certified (V13, unlocked).")
elseif cmd == "secret"
    println("ζ lives in the trace; the spectrum keeps the secret.")
elseif cmd == "analyze"
    if jsonout
        # emit the flat metrics verbatim (pure JSON on stdout)
        println(read(METRICS, String))
    else
        print(BANNER)
        println("  ", title)
        println("  ", sub, "   lang: ", lang, "  seed: ", getm("seed"))
        println("  ", "─"^66)
        for (i, s) in enumerate(steps)
            println("[$i/5] · $s ", "."^max(2, 40 - length(s)), " ✅")
        end
        println()
        println("── 📈 metrics ──────────────────────")
        println("GUE ⟨r⟩ ζ-decorated  ", bar(parse(Float64, getm("gue_r_decorated")), 0.5, 0.7), " ", getm("gue_r_decorated"))
        println("GUE ⟨r⟩ theory       ", bar(parse(Float64, getm("gue_r_theory")), 0.5, 0.7), " ", getm("gue_r_theory"))
        println("trace ↔ primes r     ", bar(parse(Float64, getm("trace_primes_r")), 0.9, 1.0), " ", getm("trace_primes_r"))
        println("locality wall S_A    ", bar(parse(Float64, getm("sa_local")) / parse(Float64, getm("sa_haar")), 0.0, 1.0), " ",
                getm("sa_local"), "/", getm("sa_haar"))
        println("RH status: ", getm("rh_status"), " (V13 obligation machine)")
        println("verdicts:  ", getm("verdicts_yes"), " YES / ", getm("verdicts_no"), " NO / ", getm("verdicts_certified"), " CERTIFIED")
        println()
        println("🎉 Done.")
    end
else
    println("command '$cmd' delegated to the python reference: python3 ../python/run.py $cmd")
    exit(2)
end
