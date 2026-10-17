function run_verify(varargin)
% ==============================================================================
% AB-Cloud Verification Suite — thin CLI runner (MATLAB / GNU Octave)
% ==============================================================================
% Thin by construction (CANON_SPEC §10): it only parses the shared flag
% language, delegates ALL computation to ab_cloud_verify.m, and maps the
% frozen-anchor self-check result to the process exit status.
%
% Usage (as a function, identical in MATLAB and Octave):
%   run_verify                                          % defaults below
%   run_verify('--zeros', 50000, '--objection', 'all')
%   run_verify('--source', '50k_full', '--lang', 'ru')
%
% From the shell:
%   matlab -batch "run_verify('--zeros', 50000)"
%   octave --eval "run_verify('--zeros', 50000)"
%   octave run_verify.m -- --zeros 50000                % argv() pickup
%   AB_CLOUD_ARGS='--zeros 50000 --lang ru' octave --eval run_verify
%
% Flags (CANON_SPEC §9):
%   --zeros N          number of zeros to use (default 50000, 0 = all loaded)
%   --source NAME      auto|50k|50k_full|500k|2M|highT|2M_gz|csv|zeros6
%   --objection X      1|2|3|all          (default all)
%   --lang L           en|ru              (default: LANG auto-detect)
%   --data-dir DIR     data directory     (default ../data next to this file)
%   --no-selfcheck     skip the frozen-anchor self-check
%   --help             show this help
%
% Exit status: 1 if any self-check anchor FAILS (exit(1) under a shell
% launch, error() otherwise — both yield status 1 in matlab -batch /
% octave CLI runs); 0 otherwise.
% ==============================================================================

    opts = struct('zeros', 50000, 'source', 'auto', 'objection', 'all', ...
                  'lang', '', 'dataDir', '', 'selfcheck', 'on');

    args = varargin;
    cliMode = false;

    if isempty(args)
        % Shell-launch hook: space-separated flags in an environment variable.
        env = getenv('AB_CLOUD_ARGS');
        if isempty(env)
            env = getenv('MATLAB_CLI_ARGS');   % legacy alias
        end
        if ~isempty(strtrim(env))
            args = strsplit(strtrim(env));
            cliMode = true;
        end
    end
    if isempty(args)
        % Octave argv() pickup: `octave run_verify.m --zeros 50000`.
        % Only enter CLI mode if argv actually contains a KNOWN flag, so
        % Octave's own options (--eval payloads etc.) can never confuse this.
        if exist('OCTAVE_VERSION', 'builtin') > 0
            known = {'--zeros', '--source', '--objection', '--lang', ...
                     '--data-dir', '--no-selfcheck', '--help'};
            av = argv();
            idx = 0;
            for j = 1:numel(av)
                if any(strcmp(av{j}, known))
                    idx = j;
                    break
                end
            end
            if idx > 0
                args = av(idx:end);
                cliMode = true;
            end
        end
    end

    % --- manual flag loop (parser-free, Octave-safe) ---------------------------
    i = 1;
    while i <= numel(args)
        fl = args{i};
        if strcmp(fl, '--no-selfcheck')
            opts.selfcheck = 'off';
            i = i + 1;
        elseif strcmp(fl, '--help') || strcmp(fl, '-h')
            print_help();
            return
        elseif i + 1 > numel(args)
            error('run_verify:args', 'Missing value for flag: %s (see --help)', fl);
        else
            v = args{i+1};
            if strcmp(fl, '--zeros')
                opts.zeros = str2double(v);
            elseif strcmp(fl, '--source')
                opts.source = v;
            elseif strcmp(fl, '--objection')
                opts.objection = v;
            elseif strcmp(fl, '--lang')
                opts.lang = v;
            elseif strcmp(fl, '--data-dir')
                opts.dataDir = v;
            else
                error('run_verify:args', 'Unknown flag: %s (see --help)', fl);
            end
            i = i + 2;
        end
    end

    % --- run the canonical kernel ----------------------------------------------
    results = ab_cloud_verify('dataDir', opts.dataDir, ...
                              'zeros', opts.zeros, ...
                              'source', opts.source, ...
                              'objection', opts.objection, ...
                              'lang', opts.lang, ...
                              'selfcheck', opts.selfcheck);

    if isempty(results)
        % Nothing loaded: mirrors the canon CLI, which exits 0 when no
        % self-check ran (the loader already reported the reason on stderr).
        fprintf('Verification aborted — no zeros loaded.\n');
        return
    end

    if isfield(results, 'selfcheck') && results.selfcheck.fail > 0
        msgtxt = sprintf(['SELF-CHECK FAILED: %d of %d anchors disagree with ' ...
                          'the frozen golden values (exit status 1).'], ...
                         results.selfcheck.fail, ...
                         results.selfcheck.pass + results.selfcheck.fail);
        if cliMode
            fprintf(2, '%s\n', msgtxt);
            exit(1);
        else
            error('run_verify:selfcheck', '%s', msgtxt);
        end
    end
end

function print_help()
    L = { ...
    'AB-Cloud Verification Suite — MATLAB/Octave runner', ...
    '', ...
    'Usage: run_verify [''--zeros'', N] [''--source'', NAME] [''--objection'', X] ...', ...
    '', ...
    'Flags:', ...
    '  --zeros N          number of zeros to use (default 50000, 0 = all loaded)', ...
    '  --source NAME      auto|50k|50k_full|500k|2M|highT|2M_gz|csv|zeros6', ...
    '  --objection X      1|2|3|all  (default all)', ...
    '  --lang L           en|ru  (default: auto-detect from LANG)', ...
    '  --data-dir DIR     data directory (default ../data next to this file)', ...
    '  --no-selfcheck     skip the frozen-anchor self-check', ...
    '  --help             show this help', ...
    '', ...
    'Shell examples:', ...
    '  matlab -batch "run_verify(''--zeros'', 50000)"', ...
    '  octave --eval "run_verify(''--source'', ''50k_full'')"', ...
    '  AB_CLOUD_ARGS=''--zeros 2000'' octave --eval run_verify', ...
    '', ...
    'Exit status: 1 if any golden self-check anchor fails, else 0.'};
    for i = 1:numel(L)
        fprintf('%s\n', L{i});
    end
end
