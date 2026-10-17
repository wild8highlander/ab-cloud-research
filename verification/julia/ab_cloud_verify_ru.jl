# Thin language pin (CANON_SPEC §10): Russian output. No duplicated math.
include("ab_cloud_verify.jl")

if abspath(PROGRAM_FILE) == @__FILE__
    # re-dispatch CLI with lang pinned to :ru
    zeros = 50000; source = "auto"; objection = "all"
    data_dir = "../data"; selfcheck_on = true
    i = 1
    while i <= length(ARGS)
        a = ARGS[i]
        if a == "--zeros" && i < length(ARGS); i += 1; zeros = parse(Int, ARGS[i])
        elseif a == "--source" && i < length(ARGS); i += 1; source = ARGS[i]
        elseif a == "--objection" && i < length(ARGS); i += 1; objection = ARGS[i]
        elseif a == "--data-dir" && i < length(ARGS); i += 1; data_dir = ARGS[i]
        elseif a == "--no-selfcheck"; selfcheck_on = false
        end
        i += 1
    end
    sc = run_suite(zeros=zeros, source=source, objection=objection, lang=:ru,
                   data_dir=data_dir, selfcheck_on=selfcheck_on)
    sc > 0 && exit(1)
end
