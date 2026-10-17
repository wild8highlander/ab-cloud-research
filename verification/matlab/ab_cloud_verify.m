function results = ab_cloud_verify(varargin)
% ==============================================================================
% AB-Cloud Verification Suite — MATLAB / GNU Octave kernel (bilingual EN/RU)
% ==============================================================================
% Canon: verification/CANON_SPEC.md (v3.0), bit-compatible with the frozen
% golden reference data/abcloud_golden.json (meridian-spectral-observatory,
% selftest 199/199, Julia 1.10.9, first 50 000 Odlyzko zeros).
%
% Verifies three reviewer objections against actual Riemann zeta zeros:
%   1. Numerical stability of b(N) convergence
%   2. GUE spacing statistical significance (KS + Cramer-von Mises + AD + <r>)
%   3. Large-T decay rate O(1/sqrt(N))
%
% A frozen-anchor self-check (CANON_SPEC §8) runs FIRST; every verdict below
% is printed only in the branch chosen by the computed numbers — no canned
% verdict strings. The CLI runner run_verify.m exits with status 1 if any
% anchor fails.
%
% Usage (name/value pairs; parser-free manual loop, Octave-safe):
%   results = ab_cloud_verify();
%   results = ab_cloud_verify('dataDir', '../data', 'zeros', 50000, ...
%                             'source', 'auto', 'objection', 'all', 'lang', 'en');
%
% Parameters:
%   dataDir    - data directory (default: ../data relative to this file)
%   zeros      - number of zeros to use (default 50000; 0 = all loaded)
%   source     - auto|50k|50k_full|500k|2M|highT|2M_gz|csv|zeros6 (default auto)
%   objection  - '1'|'2'|'3'|'all' (default 'all')
%   lang       - 'en'|'ru' (default: auto-detect from the LANG environment)
%   selfcheck  - 'on'|'off' (default 'on')
%
% Octave-compatible by construction: no string class, no arguments blocks,
% no tables, no inputParser — char arrays, cell arrays, printf/fprintf only.
% ==============================================================================

    % --- options (manual name/value parse) ------------------------------------
    dataDir = '';
    nZeros  = 50000;
    src     = 'auto';
    obj     = 'all';
    lang    = '';
    doSC    = true;
    i = 1;
    while i <= numel(varargin)
        if ~ischar(varargin{i}) || i + 1 > numel(varargin)
            error('ab_cloud_verify:args', 'Expected name/value pairs (see function header).');
        end
        key = lower(varargin{i});
        switch key
            case {'datadir', 'data-dir', 'data_dir'}
                dataDir = varargin{i+1};
            case 'zeros'
                nZeros = varargin{i+1};
            case 'source'
                src = varargin{i+1};
            case 'objection'
                obj = varargin{i+1};
            case 'lang'
                lang = varargin{i+1};
            case 'selfcheck'
                doSC = abv_truthy(varargin{i+1});
            otherwise
                error('ab_cloud_verify:args', 'Unknown option: %s', varargin{i});
        end
        i = i + 2;
    end

    if ischar(nZeros)
        nZeros = str2double(nZeros);
    end
    if isnan(nZeros) || nZeros < 0
        error('ab_cloud_verify:args', 'zeros must be a non-negative number.');
    end
    if ~any(strcmp(obj, {'1', '2', '3', 'all'}))
        error('ab_cloud_verify:args', 'objection must be 1|2|3|all, got: %s', obj);
    end

    if isempty(dataDir)
        here = mfilename('fullpath');
        here = fileparts(here);
        if isempty(here)
            dataDir = '../data';
        else
            dataDir = fullfile(here, '..', 'data');
        end
    end
    if isempty(lang)
        lg = lower(getenv('LANG'));
        if ~isempty(strfind(lg, 'ru'))
            lang = 'ru';
        else
            lang = 'en';
        end
    end

    MSG = get_msg(lang);

    % --- load zeros (CANON_SPEC §9 source registry) ----------------------------
    [gammas, srcUsed] = load_zeros(dataDir, nZeros, src, MSG);
    if isempty(gammas)
        results = [];
        return
    end

    results = struct('lang', lang, 'n', numel(gammas), 'source', srcUsed);

    % --- shared b(N) prefix: pref(k+1) = sum_{j=1..k} |z_j - gram_point(j)| ----
    % Sequential accumulation exactly as spec §3; b(N) = pref(N+1)/N is
    % bit-identical to the direct sum (CANON_SPEC §7 allows the prefix).
    needPref = doSC || strcmp(obj, 'all') || strcmp(obj, '1') || strcmp(obj, '3');
    if needPref
        pref = bn_prefix(gammas);
    else
        pref = [];
    end

    % --- frozen-anchor self-check (CANON_SPEC §8) -------------------------------
    scPass = -1; scFail = -1; scSkip = 0;
    if doSC
        [scPass, scFail, scSkip] = selfcheck(gammas, pref, MSG);
        results.selfcheck = struct('pass', scPass, 'fail', scFail, 'skip', scSkip);
    end

    % --- objections (CANON_SPEC §7, honest branch-selected verdicts) ------------
    ran = {};
    if strcmp(obj, 'all') || strcmp(obj, '1')
        results.obj1 = objection_1(gammas, pref, MSG);
        ran{end+1} = '1';
    end
    if strcmp(obj, 'all') || strcmp(obj, '2')
        results.obj2 = objection_2(gammas, MSG);
        ran{end+1} = '2';
    end
    if strcmp(obj, 'all') || strcmp(obj, '3')
        results.obj3 = objection_3(gammas, pref, MSG);
        ran{end+1} = '3';
    end

    % --- summary: self-check n/n first, then per-objection status ----------------
    fprintf('\n%s\n%s\n', repmat('=', 1, 60), MSG.summary);
    if doSC
        fprintf(MSG.selfcheck_result, scPass, scFail);
    end
    for i = 1:numel(ran)
        if strcmp(ran{i}, '1')
            if results.obj1.converged, st = MSG.pass_; else, st = MSG.warn; end
        elseif strcmp(ran{i}, '2')
            if ~results.obj2.rejected, st = MSG.pass_; else, st = MSG.fail; end
        else
            if results.obj3.consistent, st = MSG.pass_; else, st = MSG.fail; end
        end
        fprintf(MSG.summary_line, ran{i}, st);
    end
    fprintf('%s\n', repmat('=', 1, 60));
end

% ==============================================================================
% Bilingual message catalogs (printf format strings; %% escapes a literal %)
% ==============================================================================
function MSG = get_msg(lang)
    if strcmp(lang, 'ru')
        MSG = msg_ru();
    else
        MSG = msg_en();
    end
end

function MSG = msg_en()
    MSG = struct();
    MSG.loading        = 'Loading %d zeros from ''%s'' ...\n';
    MSG.loaded         = 'Loaded %d zeros from ''%s''  |  T ∈ [%.4f, %.4f]\n';
    MSG.auto_select    = 'Auto-selected ''%s'' (needs ≥%d zeros, file has %d)\n';
    MSG.file_not_found = 'ERROR: Data file not found: ''%s''\n';
    MSG.no_source      = 'ERROR: No data source available for %d zeros\n';
    MSG.obj1_title     = 'Objection 1: Numerical Stability of b(N)';
    MSG.obj1_converge  = 'Convergence table — b(N) = (1/N) Σ|γ_k − γ̃_k|';
    MSG.obj1_fit       = 'Empirical law:  b(N) ≈ %.4f · N^(−%.4f)   (R² = %.4f)\n';
    MSG.obj1_honest    = '  b(N) decreases monotonically over the table — convergence confirmed\n  on the accessible range. The decay is EMPIRICAL, not O(1/√N) (see Objection 3).\n';
    MSG.obj1_notmono   = '  b(N) is NOT monotonically decreasing over this table — convergence NOT\n  confirmed on the accessible range (honest verdict).\n';
    MSG.obj2_title     = 'Objection 2: GUE Spacing Statistical Significance';
    MSG.obj2_mean      = '  Spacing mean: %.9f  var: %.9f  (n = %d)\n';
    MSG.obj2_ks        = '  Kolmogorov-Smirnov:  D = %.6f,  p-value = %.6f\n';
    MSG.obj2_cvm       = '  Cramér-von Mises:    W² = %.6f\n';
    MSG.obj2_ad        = '  Anderson-Darling:   A² = %.6f\n';
    MSG.obj2_rmean     = '  ⟨r⟩ (adjacent-ratio): %.6f  (n = %d, GUE surmise ≈ 0.5992)\n';
    MSG.obj2_result    = '  H₀ (GUE distribution): %s  (α = 0.05)\n';
    MSG.obj2_reject    = 'REJECTED';
    MSG.obj2_not_reject = 'NOT REJECTED';
    MSG.obj2_note      = '  Note: at large n the exact GUE surmise is formally rejected — the\n  known finite-T corrections of the zeta zeros, not a data artifact\n  (mean ≈ 1 validates the unfolding; golden-anchored).\n';
    MSG.obj3_title     = 'Objection 3: Large-T Decay Rate';
    MSG.obj3_fit       = '  Linear fit  log(b(N)) = %.4f · log(N) + %.4f\n';
    MSG.obj3_expected  = '  Expected slope ≈ −0.5  (b(N) = O(1/√N))';
    MSG.obj3_ci        = '  95%% CI for slope: [%.4f, %.4f]\n';
    MSG.obj3_verdict   = '  Slope %.4f is %s −0.5 ± 0.1 → %s\n';
    MSG.obj3_consistent = 'CONSISTENT with O(1/√N)';
    MSG.obj3_inconsistent = 'INCONSISTENT with O(1/√N)';
    MSG.obj3_within    = 'within';
    MSG.obj3_outside   = 'outside';
    MSG.selfcheck_title = 'Golden self-check — frozen anchors (canon: meridian-spectral-observatory, selftest 199/199)';
    MSG.selfcheck_line = '  %-24s %s  computed = %.12g, expected = %.12g, Δ = %.3e\n';
    MSG.selfcheck_ok   = 'PASS';
    MSG.selfcheck_bad  = 'FAIL';
    MSG.selfcheck_skip = '  %-24s SKIP  (needs %d zeros, have %d)\n';
    MSG.selfcheck_result = '  Self-check: %d passed, %d failed\n';
    MSG.summary        = 'Verification Summary';
    MSG.summary_line   = '  Objection %s: %s\n';
    MSG.pass_          = 'PASS';
    MSG.fail           = 'FAIL';
    MSG.warn           = 'WARN';
end

function MSG = msg_ru()
    MSG = struct();
    MSG.loading        = 'Загрузка %d нулей из ''%s'' ...\n';
    MSG.loaded         = 'Загружено %d нулей из ''%s''  |  T ∈ [%.4f, %.4f]\n';
    MSG.auto_select    = 'Авто-выбор ''%s'' (нужно ≥%d нулей, файл содержит %d)\n';
    MSG.file_not_found = 'ОШИБКА: Файл данных не найден: ''%s''\n';
    MSG.no_source      = 'ОШИБКА: Нет источника данных для %d нулей\n';
    MSG.obj1_title     = 'Возражение 1: Численная устойчивость b(N)';
    MSG.obj1_converge  = 'Таблица сходимости — b(N) = (1/N) Σ|γ_k − γ̃_k|';
    MSG.obj1_fit       = 'Эмпирический закон:  b(N) ≈ %.4f · N^(−%.4f)   (R² = %.4f)\n';
    MSG.obj1_honest    = '  b(N) монотонно убывает по таблице — сходимость подтверждена\n  на доступном диапазоне. Убывание ЭМПИРИЧЕСКОЕ, это не O(1/√N) (см. Возражение 3).\n';
    MSG.obj1_notmono   = '  b(N) НЕ монотонно убывает по этой таблице — сходимость НЕ подтверждена\n  на доступном диапазоне (честный вердикт).\n';
    MSG.obj2_title     = 'Возражение 2: Статистическая значимость GUE-распределения';
    MSG.obj2_mean      = '  Средний спейсинг: %.9f  дисперсия: %.9f  (n = %d)\n';
    MSG.obj2_ks        = '  Колмогоров-Смирнов:  D = %.6f,  p-значение = %.6f\n';
    MSG.obj2_cvm       = '  Крамер-фон Мизес:    W² = %.6f\n';
    MSG.obj2_ad        = '  Андерсон-Дарлинг:     A² = %.6f\n';
    MSG.obj2_rmean     = '  ⟨r⟩ (отношение соседних): %.6f  (n = %d, GUE ≈ 0.5992)\n';
    MSG.obj2_result    = '  H₀ (GUE-распределение): %s  (α = 0.05)\n';
    MSG.obj2_reject    = 'ОТВЕРГНУТА';
    MSG.obj2_not_reject = 'НЕ ОТВЕРГНУТА';
    MSG.obj2_note      = '  Примечание: при больших n точная GUE-сурьмида формально отвергается — это\n  известные поправки конечных T у нулей ζ, а не дефект данных\n  (среднее ≈ 1 подтверждает развёртку; якоря golden).\n';
    MSG.obj3_title     = 'Возражение 3: Скорость убывания при больших T';
    MSG.obj3_fit       = '  Линейная аппроксимация  log(b(N)) = %.4f · log(N) + %.4f\n';
    MSG.obj3_expected  = '  Ожидаемый наклон ≈ −0.5  (b(N) = O(1/√N))';
    MSG.obj3_ci        = '  95%% ДИ для наклона: [%.4f, %.4f]\n';
    MSG.obj3_verdict   = '  Наклон %.4f %s −0.5 ± 0.1 → %s\n';
    MSG.obj3_consistent = 'СОГЛАСУЕТСЯ с O(1/√N)';
    MSG.obj3_inconsistent = 'НЕ СОГЛАСУЕТСЯ с O(1/√N)';
    MSG.obj3_within    = 'внутри';
    MSG.obj3_outside   = 'вне';
    MSG.selfcheck_title = 'Само-проверка golden — замороженные якоря (канон: meridian-spectral-observatory, selftest 199/199)';
    MSG.selfcheck_line = '  %-24s %s  вычислено = %.12g, ожидание = %.12g, Δ = %.3e\n';
    MSG.selfcheck_ok   = 'ПРОЙДЕНО';
    MSG.selfcheck_bad  = 'СБОЙ';
    MSG.selfcheck_skip = '  %-24s ПРОПУСК  (нужно %d нулей, есть %d)\n';
    MSG.selfcheck_result = '  Само-проверка: %d пройдено, %d провалено\n';
    MSG.summary        = 'Итоги проверки';
    MSG.summary_line   = '  Возражение %s: %s\n';
    MSG.pass_          = 'ПРОЙДЕНО';
    MSG.fail           = 'СБОЙ';
    MSG.warn           = 'ПРЕДУПР.';
end

% ==============================================================================
% Zero loader (CANON_SPEC §9)
% ==============================================================================
function [gammas, srcUsed] = load_zeros(dataDir, count, source, MSG)
    % Source registry: {name, filename, approx zero count} (CANON_SPEC §9)
    REG = { ...
        '50k',      'zeta_zeros_50000.txt',           13661; ...
        '50k_full', 'zeta_zeros_50000_embedded.txt',  50000; ...
        '500k',     'zeta_zeros_500k_odlyzko.txt',    500000; ...
        '2M',       'zeta_zeros_2M_odlyzko.txt',      2001052; ...
        'highT',    'zeta_zeros_highT_blocks.txt',    30000; ...
        '2M_gz',    'zeta_zeros_2M_odlyzko.txt.gz',   2001052; ...
        'csv',      'zeta_zeros_50000.csv',           13661; ...
        'zeros6',   'zeros6.txt',                     2001052 };
    gammas  = [];
    srcUsed = '';

    if strcmp(source, 'auto')
        % auto = smallest registered file whose approximate count >= count
        avails = zeros(1, size(REG, 1));
        for r = 1:size(REG, 1)
            avails(r) = REG{r, 3};
        end
        cand = find(avails >= count);
        if isempty(cand)
            fprintf(2, MSG.no_source, count);
            return
        end
        [mn, ~] = min(avails(cand));
        row = cand(find(avails(cand) == mn, 1, 'first'));
        srcUsed = REG{row, 1};
        fprintf(MSG.auto_select, srcUsed, count, avails(row));
    else
        row = 0;
        for r = 1:size(REG, 1)
            if strcmp(REG{r, 1}, source)
                row = r;
                break
            end
        end
        if row == 0
            fprintf(2, MSG.no_source, count);
            return
        end
        srcUsed = REG{row, 1};
    end

    fname    = REG{row, 2};
    filepath = fullfile(dataDir, fname);
    fprintf(MSG.loading, count, fname);

    if exist(filepath, 'file') == 0
        fprintf(2, MSG.file_not_found, filepath);
        gammas  = [];
        srcUsed = '';
        return
    end

    if ~isempty(strfind(fname, '.gz'))
        % gzipped plain table — unpack into a temp dir (gunzip is core in
        % both MATLAB and Octave); the temp file is removed after parsing.
        try
            tmpd = fullfile(tempdir, 'abcloud_gz_extract');
            if exist(tmpd, 'dir') ~= 7
                mkdir(tmpd);
            end
            out = gunzip(filepath, tmpd);
            if iscell(out)
                gzpath = out{1};
            else
                gzpath = out;
            end
            gammas = parse_plain(gzpath);
            try
                delete(gzpath);
            catch
            end
        catch gz_err
            fprintf(2, 'ERROR: cannot read %s: %s\n', filepath, gz_err.message);
            gammas  = [];
            srcUsed = '';
            return
        end
    elseif strcmp(source, 'highT')
        gammas = parse_highT(filepath);
    elseif strcmp(source, 'csv')
        gammas = parse_csv(filepath);
    else
        gammas = parse_plain(filepath);
    end

    % Sort ascending first, then truncate (exact canon order).
    gammas = sort(gammas(:));
    if count > 0 && count < numel(gammas)
        gammas = gammas(1:count);
    end
    if ~isempty(gammas)
        fprintf(MSG.loaded, numel(gammas), fname, gammas(1), gammas(end));
    end
end

function z = parse_plain(path)
    % Plain table: one float per line; '#' comments and blanks skipped.
    z = [];
    raw = fileread(path);
    if isempty(raw)
        return
    end
    lines = strsplit(raw, {'\r\n', '\n', '\r'});
    vals  = str2double(strtrim(lines));   % NaN for comments/blanks/garbage
    z = vals(~isnan(vals));
    z = z(:);
end

function z = parse_csv(path)
    % CSV with columns index,t,s_real,s_imag,zero_number — column 2 is t.
    z = [];
    raw = fileread(path);
    if isempty(raw)
        return
    end
    lines = strsplit(raw, {'\r\n', '\n', '\r'});
    buf   = zeros(1, numel(lines));
    cnt   = 0;
    for i = 1:numel(lines)
        ln = strtrim(lines{i});
        if isempty(ln) || ln(1) == '#'
            continue
        end
        parts = strsplit(ln, ',');
        if numel(parts) < 2
            continue
        end
        v = str2double(parts{2});   % header line -> NaN -> skipped
        if isnan(v)
            continue
        end
        cnt = cnt + 1;
        buf(cnt) = v;
    end
    z = buf(1:cnt);
    z = z(:);
end

function z = parse_highT(path)
    % BLOCK-offset format: '# BLOCK index=... offset=BASE' headers; each
    % value line is an offset from the current BASE.
    z = [];
    raw = fileread(path);
    if isempty(raw)
        return
    end
    lines = strsplit(raw, {'\r\n', '\n', '\r'});
    buf   = zeros(1, numel(lines));
    cnt   = 0;
    base  = 0.0;
    for i = 1:numel(lines)
        ln = strtrim(lines{i});
        if isempty(ln)
            continue
        end
        if ln(1) == '#'
            if ~isempty(strfind(ln, 'BLOCK'))
                tok = regexp(ln, 'offset=(\S+)', 'tokens', 'once');
                if ~isempty(tok)
                    b = str2double(tok{1});
                    if ~isnan(b)
                        base = b;
                    end
                end
            end
            continue
        end
        v = str2double(ln);
        if isnan(v)
            continue
        end
        cnt = cnt + 1;
        buf(cnt) = base + v;
    end
    z = buf(1:cnt);
    z = z(:);
end

% ==============================================================================
% Lambert W, principal branch (CANON_SPEC §1)
% ==============================================================================
function w = lambert_w(x)
    % Newton: w*exp(w) = x. x <= 0 -> 0. Seed w = log(x), w -= log(w) when
    % w > 0; for 0 < x < 1 the seed is w = x (the log seed sits exactly on
    % the w = -1 degeneracy fp = 0 at x = 1/e, which the golden canon also
    % avoids). Up to 50 iterations, stop when |delta| < 1e-14*(1+|w|).
    if x <= 0
        w = 0.0;
        return
    end
    w = log(x);
    if w < 0
        w = x;
    elseif w > 0
        w = w - log(w);
    end
    for it = 1:50
        ew = exp(w);
        f  = w * ew - x;
        fp = ew * (w + 1.0);
        if abs(fp) < 1e-30
            break
        end
        delta = f / fp;
        w = w - delta;
        if abs(delta) < 1e-14 * (1.0 + abs(w))
            break
        end
    end
end

% ==============================================================================
% Gram point (CANON_SPEC §2 — the old seed-only formula is WRONG)
% ==============================================================================
function t = gram_point(k)
    % k-th Gram point: theta(t_k) = pi*k. Seed t = 2*pi*k / W(k/e), then
    % EXACTLY 8 Newton iterations on the 5-term Riemann–Siegel theta:
    %   theta(t)  = (t/2)*ln(t/2pi) - t/2 - pi/8 + 1/(48t) + 7/(5760 t^3)
    %   dtheta(t) = 0.5*ln(t/2pi) - 1/(48 t^2) - 21/(5760 t^4)
    if k <= 0
        t = 0.0;
        return
    end
    t = 2.0 * pi * k / lambert_w(k / exp(1));
    for it = 1:8
        arg = t / (2.0 * pi);
        if arg <= 0
            break
        end
        theta  = (t / 2.0) * log(arg) - t / 2.0 - pi / 8.0 ...
                 + 1.0 / (48.0 * t) + 7.0 / (5760.0 * t * t * t);
        dtheta = 0.5 * log(arg) - 1.0 / (48.0 * t * t) ...
                 - 21.0 / (5760.0 * t * t * t * t);
        if abs(dtheta) < 1e-30
            break
        end
        t = t - (theta - pi * k) / dtheta;
    end
end

% ==============================================================================
% b(N) with the exact sequential summation order (CANON_SPEC §3)
% ==============================================================================
function pref = bn_prefix(z)
    % pref(k+1) = sum_{j=1..k} |z_j - gram_point(j)|, accumulated sequentially;
    % b(N) = pref(N+1)/N is bit-identical to the direct sum.
    n = numel(z);
    pref = zeros(1, n + 1);
    acc = 0.0;
    for k = 1:n
        acc = acc + abs(z(k) - gram_point(k));
        pref(k + 1) = acc;
    end
end

function b = bN_off(z, N, off)
    % b(N; offset) — zeros 1..N against Gram points off+1 .. off+N.
    if N <= 0 || off + N > numel(z)
        b = NaN;
        return
    end
    total = 0.0;
    for k = 1:N
        total = total + abs(z(k) - gram_point(off + k));
    end
    b = total / N;
end

% ==============================================================================
% Normalized spacings (CANON_SPEC §4)
% ==============================================================================
function sp = spacings_of(z)
    % s = (z_{k+1} - z_k) * log(z_k / (2*pi)) / (2*pi)  for z_k > 0.
    % Vectorized form keeps the k order and the per-element op order.
    if numel(z) < 2
        sp = zeros(0, 1);
        return
    end
    zk  = z(1:end-1);
    zk1 = z(2:end);
    m   = zk > 0;
    sp  = (zk1(m) - zk(m)) .* log(zk(m) / (2 * pi)) / (2 * pi);
    sp  = sp(:);
end

% ==============================================================================
% GUE CDF via 32768-point interpolation table (CANON_SPEC §5)
% ==============================================================================
function F = gue_cdf_exact(s)
    % Exact Wigner–Dyson beta=2 surmise CDF:
    %   F(s) = erf(2s/sqrt(pi)) - (4s/pi)*exp(-4s^2/pi)
    F = erf(2.0 * s / sqrt(pi)) - (4.0 * s / pi) .* exp(-4.0 * s * s / pi);
end

function F = gue_cdf(s)
    % Table-backed CDF: TN = 32768 points on [0, SMAX = 5], built lazily once
    % and cached in a persistent. MATLAB is 1-indexed: TBL(i+1) = table[i]
    % (0-based canon index i), so the interpolation reads TBL(i+1), TBL(i+2).
    persistent TBL
    TN   = 32768;
    SMAX = 5.0;
    if s <= 0
        F = 0.0;
        return
    end
    if s >= SMAX
        F = gue_cdf_exact(s);
        return
    end
    if isempty(TBL)
        TBL = gue_cdf_exact((0:TN-1) * SMAX / (TN - 1));  % TBL(j) = exact((j-1)*SMAX/(TN-1))
    end
    x = s * (TN - 1) / SMAX;
    i = floor(x);
    if i < 0 || i >= TN - 1
        F = gue_cdf_exact(s);
        return
    end
    t = x - i;
    F = (1.0 - t) * TBL(i + 1) + t * TBL(i + 2);
end

% ==============================================================================
% Statistics (CANON_SPEC §6)
% ==============================================================================
function p = ks_pvalue(lam)
    % Kolmogorov asymptotic p-value, two branches + clamp to [0,1].
    if lam <= 0
        p = 1.0;
        return
    end
    if lam < 0.6
        s2 = 0.0;
        for k = 1:1000
            term = exp(-(((2.0 * k - 1.0)^2) * (pi^2)) / (8.0 * lam * lam));
            s2 = s2 + term;
            if term < 1e-18
                break
            end
        end
        v = 1.0 - sqrt(2.0 * pi) / lam * s2;
    else
        s = 0.0;
        sgn = 1.0;
        for k = 1:100
            term = sgn * exp(-2.0 * k * k * lam * lam);
            s = s + term;
            sgn = -sgn;
            if abs(term) < 1e-18
                break
            end
        end
        v = 2.0 * s;
    end
    p = min(1.0, max(0.0, v));
end

function [D, p] = ks_test(sp)
    % Two-sided KS D + lambda-corrected p-value on sorted spacings.
    n = numel(sp);
    if n == 0
        D = 0.0; p = 1.0;
        return
    end
    ss = sort(sp(:));
    D = 0.0;
    for i = 1:n
        Fx = gue_cdf(ss(i));
        d1 = abs(i / n - Fx);
        d2 = abs((i - 1) / n - Fx);
        if d1 > D, D = d1; end
        if d2 > D, D = d2; end
    end
    lam = (sqrt(n) + 0.12 + 0.11 / sqrt(n)) * D;
    p = ks_pvalue(lam);
end

function W2 = cvm_stat(sp)
    % Cramer-von Mises W2 = 1/(12n) + sum_i ( F(s_i) - (2i-1)/(2n) )^2.
    n = numel(sp);
    if n == 0
        W2 = 0.0;
        return
    end
    ss = sort(sp(:));
    W2 = 1.0 / (12.0 * n);
    for i = 1:n
        Fx = gue_cdf(ss(i));
        W2 = W2 + ((2.0 * i - 1.0) / (2.0 * n) - Fx)^2;
    end
end

function A2 = ad_stat(sp)
    % Anderson-Darling A2 with 1e-300 / 1-1e-16 tail clamps.
    n = numel(sp);
    if n < 2
        A2 = NaN;
        return
    end
    ss = sort(sp(:));
    acc = 0.0;
    for i = 1:n
        Fi  = min(max(gue_cdf(ss(i)),     1e-300), 1.0 - 1e-16);
        Fni = min(max(gue_cdf(ss(n + 1 - i)), 1e-300), 1.0 - 1e-16);
        acc = acc + (2.0 * i - 1.0) * (log(Fi) + log(1.0 - Fni));
    end
    A2 = -n - acc / n;
end

function [r, cnt] = adjacent_ratio(z)
    % <r> = mean over adjacent gap pairs of min(d_i,d_{i+1})/max(d_i,d_{i+1}),
    % skipping pairs where both gaps are 0; cnt = number of counted pairs.
    n = numel(z);
    if n < 3
        r = NaN; cnt = 0;
        return
    end
    d = z(2:n) - z(1:n-1);
    acc = 0.0;
    cnt = 0;
    for i = 1:n-2
        a = d(i);
        b = d(i + 1);
        if a == 0.0 && b == 0.0
            continue
        end
        acc = acc + min(a, b) / max(a, b);
        cnt = cnt + 1;
    end
    if cnt == 0
        r = NaN;
    else
        r = acc / cnt;
    end
end

function s = ssum(v)
    % Strictly sequential left-to-right sum (bit-parity with the canon sum()).
    s = 0.0;
    for i = 1:numel(v)
        s = s + v(i);
    end
end

function [mn, vr] = mean_var_s(sp)
    % Mean and sample variance (divide by n-1).
    n = numel(sp);
    if n == 0
        mn = NaN; vr = NaN;
        return
    end
    mn = ssum(sp) / n;
    if n > 1
        vr = ssum((sp - mn).^2) / (n - 1);
    else
        vr = NaN;
    end
end

function [slope, intercept, se, r2] = linreg(x, y)
    % OLS y = slope*x + intercept with slope stderr
    % se^2 = (SSres/(m-2)) * m / (m*Sxx - Sx^2)  (CANON_SPEC §7, Obj 3).
    slope = 0.0; intercept = 0.0; se = 0.0; r2 = 0.0;
    n = numel(x);
    if n < 2 || numel(y) ~= n
        return
    end
    sx = 0.0; sy = 0.0; sxx = 0.0; sxy = 0.0;
    for i = 1:n
        sx  = sx + x(i);
        sy  = sy + y(i);
        sxx = sxx + x(i) * x(i);
        sxy = sxy + x(i) * y(i);
    end
    denom = n * sxx - sx * sx;
    if abs(denom) < 1e-30
        return
    end
    slope = (n * sxy - sx * sy) / denom;
    intercept = (sy - slope * sx) / n;
    ymean = sy / n;
    ss_tot = 0.0; ss_res = 0.0;
    for i = 1:n
        ss_tot = ss_tot + (y(i) - ymean)^2;
        ss_res = ss_res + (y(i) - (slope * x(i) + intercept))^2;
    end
    if ss_tot > 0
        r2 = 1.0 - ss_res / ss_tot;
    else
        r2 = 0.0;
    end
    if n > 2
        mse = ss_res / (n - 2);
    else
        mse = 0.0;
    end
    if denom > 0
        se = sqrt(mse * n / denom);
    else
        se = 0.0;
    end
end

% ==============================================================================
% Objection 1: b(N) convergence table (CANON_SPEC §7)
% ==============================================================================
function r1 = objection_1(z, pref, MSG)
    % Print order matches the canon exactly: '=', title, table caption,
    % column header, then the dashed rule.
    fprintf('\n%s\n%s\n%s\n', repmat('=', 1, 60), MSG.obj1_title, ...
            MSG.obj1_converge);
    fprintf('%10s  %20s  %20s\n', 'N', 'b(N)', 'Δb = b(N)−b(N/2)');
    fprintf('%s\n', repmat('-', 1, 60));

    n = numel(z);
    G = [100, 500, 1000, 5000, 10000, 50000];
    G = G(G <= n);
    if isempty(G)
        G = min(n, 100);
    end

    bv = zeros(1, numel(G));
    prev = NaN;
    for ci = 1:numel(G)
        N = G(ci);
        bN = pref(N + 1) / N;
        bv(ci) = bN;
        if isnan(prev)
            ds = '—';
        else
            ds = sprintf('%+.10f', bN - prev);
        end
        fprintf('%10d  %20.10f  %20s\n', N, bN, ds);
        prev = bN;
    end

    % Optional empirical power-law fit on the printed grid (log-log OLS).
    slope = NaN; r2 = 0.0;
    keep = (G > 1) & (bv > 0);
    if numel(find(keep)) >= 3
        [slope, intercept, ~, r2] = linreg(log(double(G(keep))), log(bv(keep)));
        fprintf(MSG.obj1_fit, exp(intercept), -slope, r2);
    end

    % Honest convergence verdict: monotone decrease across the table.
    mono = true;
    for i = 1:numel(bv) - 1
        if ~(bv(i + 1) < bv(i))
            mono = false;
            break
        end
    end
    converged = mono && numel(bv) >= 3;
    if converged
        fprintf('%s\n', MSG.obj1_honest);
    else
        fprintf('%s\n', MSG.obj1_notmono);
    end

    r1 = struct('N_values', G, 'bN_values', bv, 'converged', converged, ...
                'slope', slope, 'r2', r2);
end

% ==============================================================================
% Objection 2: GUE spacing statistical significance (CANON_SPEC §7)
% ==============================================================================
function r2s = objection_2(z, MSG)
    fprintf('\n%s\n%s\n', repmat('=', 1, 60), MSG.obj2_title);

    sp = spacings_of(z);
    fprintf('  Computed %d normalized spacings\n', numel(sp));

    [mn, vr] = mean_var_s(sp);
    fprintf(MSG.obj2_mean, mn, vr, numel(sp));

    [D, pv] = ks_test(sp);
    fprintf(MSG.obj2_ks, D, pv);

    W2 = cvm_stat(sp);
    fprintf(MSG.obj2_cvm, W2);

    A2 = ad_stat(sp);
    fprintf(MSG.obj2_ad, A2);

    [rr, nr] = adjacent_ratio(z);
    fprintf(MSG.obj2_rmean, rr, nr);

    % Verdict: p < 0.05 -> H0 rejected (with the honest finite-T note).
    alpha = 0.05;
    rejected = pv < alpha;
    if rejected
        verdict = MSG.obj2_reject;
    else
        verdict = MSG.obj2_not_reject;
    end
    fprintf(MSG.obj2_result, verdict);
    if rejected
        fprintf('%s\n', MSG.obj2_note);
    end

    r2s = struct('D', D, 'p_value', pv, 'W2', W2, 'A2', A2, 'r_mean', rr, ...
                 'n_r', nr, 'mean', mn, 'var', vr, 'rejected', rejected, ...
                 'n_spacings', numel(sp));
end

% ==============================================================================
% Objection 3: large-T decay rate O(1/sqrt(N)) (CANON_SPEC §7)
% ==============================================================================
function r3 = objection_3(z, pref, MSG)
    fprintf('\n%s\n%s\n', repmat('=', 1, 60), MSG.obj3_title);

    n = numel(z);
    Nvals = [];
    v = 50;
    while v <= n
        Nvals(end+1) = v;
        v = v * 2;
    end
    if ~isempty(Nvals)
        if Nvals(end) ~= n && n > 100
            Nvals(end+1) = n;
        end
    end

    fprintf('  Computing b(N) at multiple N values ...\n');
    logN = [];
    logB = [];
    for i = 1:numel(Nvals)
        N = Nvals(i);
        bN = pref(N + 1) / N;
        if bN <= 0
            continue
        end
        logN(end+1) = log(double(N));
        logB(end+1) = log(bN);
        fprintf('    N = %8d  b(N) = %.10f  log(b) = %.6f\n', N, bN, log(bN));
    end

    if numel(logN) < 3
        fprintf('  WARNING: Not enough data points for regression\n');
        r3 = struct('slope', NaN, 'intercept', NaN, 'se', NaN, ...
                    'ci_lo', NaN, 'ci_hi', NaN, 'consistent', false, ...
                    'r2', 0.0, 'N_values', Nvals, 'bN_values', []);
        return
    end

    [slope, intercept, se, r2] = linreg(logN, logB);
    ci_lo = slope - 1.96 * se;
    ci_hi = slope + 1.96 * se;

    fprintf(MSG.obj3_fit, slope, intercept);
    fprintf('  R² = %.6f\n', r2);
    fprintf('%s\n', MSG.obj3_expected);
    fprintf(MSG.obj3_ci, ci_lo, ci_hi);

    % Honest verdict: |slope - (-0.5)| <= 0.1 -> consistent, else INCONSISTENT.
    consistent = abs(slope - (-0.5)) <= 0.1;
    if consistent
        rel = MSG.obj3_within;
        vd  = MSG.obj3_consistent;
    else
        rel = MSG.obj3_outside;
        vd  = MSG.obj3_inconsistent;
    end
    fprintf(MSG.obj3_verdict, slope, rel, vd);

    r3 = struct('slope', slope, 'intercept', intercept, 'se', se, ...
                'ci_lo', ci_lo, 'ci_hi', ci_hi, 'consistent', consistent, ...
                'r2', r2, 'N_values', Nvals, 'bN_values', exp(logB));
end

% ==============================================================================
% Golden self-check — frozen anchors (CANON_SPEC §8)
% ==============================================================================
function [npass, nfail, nskip] = selfcheck(z, pref, MSG)
    fprintf('\n%s\n%s\n', repmat('=', 1, 60), MSG.selfcheck_title);
    rows = {};
    nskip = 0;
    n = numel(z);

    % lambert_w anchors (tolerance 1e-12 relative)
    LW = { ...
        '0.5',     0.5,   0.35173371124919584; ...
        '1.0',     1.0,   0.5671432904097838; ...
        '3.7',     3.7,   1.1599531786120223; ...
        '10.0',    10.0,  1.7455280027406992; ...
        '271.8',   271.8, 4.17576816800275; ...
        '12345.6', 12345.6, 7.417247034540566 };
    for i = 1:size(LW, 1)
        rows = abv_check(rows, sprintf('lambert_w(%s)', LW{i, 1}), ...
                         lambert_w(LW{i, 2}), LW{i, 3}, 1e-12, true);
    end

    % gram_point anchors (tolerance 1e-6 absolute)
    GP = { ...
        1,     23.17028270133466; ...
        2,     27.670182217848343; ...
        3,     31.71797995477886; ...
        10,    54.67523744685398; ...
        100,   238.58259051450293; ...
        1000,  1421.25638903275; ...
        10000, 9878.910118894457; ...
        50000, 40434.6952780045 };
    for i = 1:size(GP, 1)
        rows = abv_check(rows, sprintf('gram_point(n=%d)', GP{i, 1}), ...
                         gram_point(GP{i, 1}), GP{i, 2}, 1e-6, false);
    end

    % bN anchors (tolerance 1e-6 absolute; need N <= n)
    BN = { ...
        100,   3.3321638710140165; ...
        500,   2.3912304957476382; ...
        1000,  2.1072522951855435; ...
        5000,  1.6299485869022874; ...
        10000, 1.4794053414584762; ...
        50000, 1.2125526772588608 };
    for i = 1:size(BN, 1)
        N = BN{i, 1};
        if N <= n
            rows = abv_check(rows, sprintf('bN(N=%d)', N), ...
                             pref(N + 1) / N, BN{i, 2}, 1e-6, false);
        else
            fprintf(MSG.selfcheck_skip, sprintf('bN(N=%d)', N), N, n);
            nskip = nskip + 1;
        end
    end

    % bN_off anchor (needs n >= 1500)
    if n >= 1500
        rows = abv_check(rows, 'bN(N=1000,off=500)', bN_off(z, 1000, 500), ...
                         624.6201618180231, 1e-6, false);
    else
        fprintf(MSG.selfcheck_skip, 'bN(N=1000,off=500)', 1500, n);
        nskip = nskip + 1;
    end

    % Statistics anchors — FIRST 50000 zeros only (skip if fewer are loaded)
    if n >= 50000
        z5 = z(1:50000);
        sp = spacings_of(z5);
        [mn, vr] = mean_var_s(sp);
        [D, pv]  = ks_test(sp);
        W2 = cvm_stat(sp);
        A2 = ad_stat(sp);
        [rr, nr] = adjacent_ratio(z5);
        rows = abv_check(rows, 'spacings.mean', mn, 0.999976001221201, 1e-9, false);
        rows = abv_check(rows, 'spacings.var',  vr, 0.1590654827835423, 1e-9, false);
        rows = abv_check(rows, 'ks_zeros.D',    D,  0.021619337032982328, 1e-9, false);
        rows = abv_check(rows, 'ks_zeros.p',    pv, 9.567870399361496e-21, 1e-6, true);
        rows = abv_check(rows, 'cvm_zeros.W2',  W2, 8.177703317829403, 1e-9, true);
        rows = abv_check(rows, 'ad_zeros.A2',   A2, 61.49242624209728, 1e-9, true);
        rows = abv_check(rows, 'rmean_zeros.r', rr, 0.6118798907208398, 1e-9, false);
        %#ok<NASGU> % nr is cross-checked by the rmean anchor (canon: n_r = 49998)
    else
        skipnames = {'spacings.mean/var', 'ks_zeros.D/p', 'cvm_zeros.W2', ...
                     'ad_zeros.A2', 'rmean_zeros.r'};
        for i = 1:numel(skipnames)
            fprintf(MSG.selfcheck_skip, skipnames{i}, 50000, n);
            nskip = nskip + 1;
        end
    end

    % PASS/FAIL table with deltas
    npass = 0;
    nfail = 0;
    for i = 1:size(rows, 1)
        if rows{i, 2}
            npass = npass + 1;
            status = MSG.selfcheck_ok;
        else
            nfail = nfail + 1;
            status = MSG.selfcheck_bad;
        end
        fprintf(MSG.selfcheck_line, rows{i, 1}, status, rows{i, 3}, rows{i, 4}, rows{i, 5});
    end
    fprintf(MSG.selfcheck_result, npass, nfail);
end

function rows = abv_check(rows, name, got, expected, tol, rel)
    % Append one anchor row {name, ok, got, expected, delta}.
    if isnan(got)
        rows(end+1, :) = {name, false, got, expected, Inf};
        return
    end
    if rel
        d = abs(got - expected) / abs(expected);
    else
        d = abs(got - expected);
    end
    rows(end+1, :) = {name, d <= tol, got, expected, d};
end

% ==============================================================================
% Small helpers
% ==============================================================================
function tf = abv_truthy(v)
    % Accept logical / numeric / 'on'|'off'|'true'|'false'|'yes'|'no'|'1'|'0'.
    if islogical(v)
        tf = v;
        return
    end
    if isnumeric(v)
        tf = v ~= 0;
        return
    end
    if ischar(v)
        s = lower(v);
        tf = strcmp(s, 'on') || strcmp(s, 'true') || strcmp(s, 'yes') || strcmp(s, '1');
        return
    end
    tf = ~isempty(v);
end
