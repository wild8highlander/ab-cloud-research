#!/usr/bin/env julia
# =============================================================================
# AB-CLOUD Verification — Julia Standalone Runner
# =============================================================================
# Usage: julia run_verify.jl [options]
#   --zeros N        Number of zeta zeros (default: 10000)
#   --source NAME    Data file name in ../data/ (default: auto)
#   --objection 1|2|3|all  Which objection (default: all)
#   --lang en|ru     Language output (default: en)
# =============================================================================

function main()
    n_zeros = 10000
    source  = "auto"
    objection = "all"
    lang    = "en"

    args = ARGS
    i = 1
    while i ≤ length(args)
        arg = args[i]
        if arg == "--zeros" && i+1 ≤ length(args)
            i += 1; n_zeros = parse(Int, args[i])
        elseif arg == "--source" && i+1 ≤ length(args)
            i += 1; source = args[i]
        elseif arg == "--objection" && i+1 ≤ length(args)
            i += 1; objection = args[i]
        elseif arg == "--lang" && i+1 ≤ length(args)
            i += 1; lang = args[i]
        elseif arg == "--help" || arg == "-h"
            println("""
            AB-CLOUD Julia Verification Runner

            Usage: julia run_verify.jl [options]

            Options:
              --zeros N          Number of zeta zeros (default: 10000)
              --source NAME      Data file in ../data/ (default: auto)
              --objection 1|2|3|all  Which objection to run (default: all)
              --lang en|ru       Output language (default: en)
              --help             Show this help
            """)
            exit(0)
        end
        i += 1
    end

    # Select script based on language
    script = if lang == "en"
        "ab_cloud_verify_en.jl"
    elseif lang == "ru"
        "ab_cloud_verify_ru.jl"
    else
        "ab_cloud_verify.jl"
    end

    println("==========================================")
    println("  AB-CLOUD Julia Verification")
    println("==========================================")
    println("  Script:    $script")
    println("  Zeros:     $n_zeros")
    println("  Source:    $source")
    println("  Objection: $objection")
    println("  Language:  $lang")
    println("==========================================")
    println()

    # Build command args
    cmd_args = ["--zeros", string(n_zeros), "--source", source, "--objection", objection]
    if lang != "en"
        push!(cmd_args, "--lang", lang)
    end

    # Run the selected verification script
    run(`julia $script $cmd_args`)
end

main()
