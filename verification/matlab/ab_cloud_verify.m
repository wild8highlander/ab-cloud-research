function results = ab_cloud_verify(varargin)
% ==============================================================================
% AB-Cloud Verification Suite — MATLAB Implementation (Bilingual: EN/RU)
% ==============================================================================
% Verifies three key objections against Riemann zeta zero data:
%   Objection 1: b(N) convergence  (Gram-point deviation via Lambert W)
%   Objection 2: GUE spacing KS test
%   Objection 3: Large-T decay slope ≈ -0.5
%
% Usage:
%   results = ab_cloud_verify()
%   results = ab_cloud_verify('dataDir', '../data', 'zeros', 50000, ...
%                             'source', 'auto', 'objection', 'all', 'lang', 'en')
%
% Parameters (name-value pairs):
%   dataDir   - Path to data directory     (default: '../data')
%   zeros     - Number of zeros to use     (default: 0 = all)
%   source    - Data source name           (default: 'auto')
%   objection - '1','2','3','all'          (default: 'all')
%   lang      - 'en' or 'ru'              (default: 'en')
% ==============================================================================

    % --- Parse input parameters ----------------------------------------------
    p = inputParser;
    addParameter(p, 'dataDir',   '../data',  @ischar);
    addParameter(p, 'zeros',     0,          @isnumeric);
    addParameter(p, 'source',    'auto',     @ischar);
    addParameter(p, 'objection', 'all',      @ischar);
    addParameter(p, 'lang',      'en',       @ischar);
    parse(p, varargin{:});
    dataDir   = p.Results.dataDir;
    nZeros    = p.Results.zeros;
    src       = p.Results.source;
    obj       = p.Results.objection;
    lang      = p.Results.lang;

    % --- Bilingual message table ---------------------------------------------
    MSG = get_messages(lang);

    % --- Print header --------------------------------------------------------
    fprintf('\n%s\n%s\n%s\n', MSG.separator, MSG.header, MSG.separator);

    % --- Load zeros ----------------------------------------------------------
    gammas = load_zeros(dataDir, nZeros, src, MSG);
    if isempty(gammas)
        fprintf('%s\n', MSG.no_data);
        results = []; return;
    end

    % --- Run selected objections ---------------------------------------------
    results = struct();
    if ismember(obj, {'all', '1'})
        results.obj1 = objection_1(gammas, MSG);
    end
    if ismember(obj, {'all', '2'})
        results.obj2 = objection_2(gammas, MSG);
    end
    if ismember(obj, {'all', '3'})
        results.obj3 = objection_3(gammas, MSG);
    end

    fprintf('\n%s\n%s\n\n', MSG.separator, MSG.done);
end

% ==============================================================================
% Bilingual message tables
% ==============================================================================
function MSG = get_messages(lang)
    if strcmp(lang, 'ru')
        MSG = struct( ...
            'header',       'Комплекс проверки AB-Cloud — MATLAB', ...
            'separator',    '──────────────────────────────────────────────────────', ...
            'loading',      'Загрузка нулей из: %s', ...
            'loaded',       'Загружено %d нулей из %s', ...
            'obj1_title',   'Возражение 1: Сходимость b(N)', ...
            'obj1_desc',    'b(N) = (1/N) * Σ|γ_k - γ̃_k|, точки Грама через W Ламберта', ...
            'obj1_converge','СХОДИТСЯ — b(N) → 0 подтверждает AB-Cloud', ...
            'obj1_stable',  'СТАБИЛЬНО — b(N) ≈ 0, AB-Cloud согласуется', ...
            'obj1_diverge', 'РАСХОДИТСЯ — b(N) ↛ 0, возражение подтверждено', ...
            'obj2_title',   'Возражение 2: KS-тест интервалов GUE', ...
            'obj2_desc',    's_k = (γ_{k+1}-γ_k)·log(γ_k/2π)/(2π), сравн. с p(s)=(πs/2)·exp(-πs²/4)', ...
            'obj2_pass',    'ПРОЙДЕНО — интервалы GUE подтверждены (p > 0.05)', ...
            'obj2_fail',    'НЕ ПРОЙДЕНО — интервалы GUE отклонены (p ≤ 0.05)', ...
            'obj3_title',   'Возражение 3: Наклон убывания при больших T', ...
            'obj3_desc',    'Регрессия log|γ_k - γ̃_k| от log(γ_k), ожид. наклон ≈ -0.5', ...
            'obj3_pass',    'ПРОЙДЕНО — Наклон ≈ -0.5, убывание AB-Cloud подтверждено', ...
            'obj3_fail',    'НЕ ПРОЙДЕНО — Наклон отклоняется от -0.5', ...
            'no_data',      'ОШИБКА: Нули не загружены. Проверьте каталог данных.', ...
            'done',         'Проверка завершена.' ...
        );
    else
        MSG = struct( ...
            'header',       'AB-Cloud Verification Suite — MATLAB', ...
            'separator',    '──────────────────────────────────────────────────────', ...
            'loading',      'Loading zeros from: %s', ...
            'loaded',       'Loaded %d zeros from %s', ...
            'obj1_title',   'Objection 1: b(N) Convergence', ...
            'obj1_desc',    'b(N) = (1/N) * Σ|γ_k - γ̃_k|, Gram points via Lambert W', ...
            'obj1_converge','CONVERGING — b(N) → 0 supports AB-Cloud', ...
            'obj1_stable',  'STABLE — b(N) near zero, AB-Cloud consistent', ...
            'obj1_diverge', 'DIVERGING — b(N) not → 0, objection upheld', ...
            'obj2_title',   'Objection 2: GUE Spacing KS Test', ...
            'obj2_desc',    's_k = (γ_{k+1}-γ_k)·log(γ_k/2π)/(2π), vs p(s)=(πs/2)·exp(-πs²/4)', ...
            'obj2_pass',    'PASS — GUE spacing confirmed (p > 0.05)', ...
            'obj2_fail',    'FAIL — GUE spacing rejected (p ≤ 0.05)', ...
            'obj3_title',   'Objection 3: Large-T Decay Slope', ...
            'obj3_desc',    'Linear regression of log|γ_k - γ̃_k| vs log(γ_k), expect slope ≈ -0.5', ...
            'obj3_pass',    'PASS — Slope ≈ -0.5, AB-Cloud decay confirmed', ...
            'obj3_fail',    'FAIL — Slope deviates from -0.5', ...
            'no_data',      'ERROR: No zeros loaded. Check data directory.', ...
            'done',         'Verification complete.' ...
        );
    end
end

% ==============================================================================
% Load zeros from data files
% ==============================================================================
function gammas = load_zeros(dataDir, count, source, MSG)
    files = struct( ...
        'zeta_zeros_50000',     fullfile(dataDir, 'zeta_zeros_50000.txt'), ...
        'zeta_zeros_500k',      fullfile(dataDir, 'zeta_zeros_500k_odlyzko.txt'), ...
        'zeta_zeros_2M',        fullfile(dataDir, 'zeta_zeros_2M_odlyzko.txt'), ...
        'zeta_zeros_highT',     fullfile(dataDir, 'zeta_zeros_highT_blocks.txt'), ...
        'zeros6',               fullfile(dataDir, 'zeros6.txt'), ...
        'zeta_zeros_50000_csv', fullfile(dataDir, 'zeta_zeros_50000.csv') ...
    );
    fnames = fieldnames(files);

    % Source override or auto-select
    selected = '';
    if ~strcmp(source, 'auto') && isfield(files, source)
        selected = files.(source);
    else
        for i = 1:numel(fnames)
            fp = files.(fnames{i});
            if exist(fp, 'file')
                selected = fp;
                if count > 0 && count <= 50000 && strcmp(fnames{i}, 'zeta_zeros_50000')
                    break;
                end
            end
        end
    end

    if isempty(selected) || ~exist(selected, 'file')
        error('No data file found in: %s', dataDir);
    end

    fprintf(MSG.loading + '\n', selected);

    % Read based on extension
    [~, ~, ext] = fileparts(selected);
    if strcmpi(ext, '.csv')
        T = readtable(selected, 'FileType', 'text', 'ReadVariableNames', false);
        gammas = T{:, 1};
    else
        % textscan: read all floats, skip comment lines
        fid = fopen(selected, 'r');
        if fid == -1, error('Cannot open: %s', selected); end
        gammas = [];
        while ~feof(fid)
            line = fgetl(fid);
            if ~ischar(line), continue; end
            line = strtrim(line);
            if isempty(line) || line(1) == '#', continue; end
            vals = sscanf(line, '%f');
            gammas = [gammas; vals(:)];
        end
        fclose(fid);
    end

    gammas = gammas(:);
    if count > 0 && count < numel(gammas)
        gammas = gammas(1:count);
    end

    fprintf(MSG.loaded + '\n', numel(gammas), selected(1:min(end,50)));
end

% ==============================================================================
% Lambert W (principal branch) — Halley's method
% ==============================================================================
function w = lambert_W0(x)
    if x == 0, w = 0; return; end
    if x > 1
        w = log(x) - log(log(x));
    else
        w = x;
    end
    for iter = 1:50
        ew  = exp(w);
        f   = w * ew - x;
        fp  = ew * (1 + w);
        fpp = ew * (2 + w);
        w   = w - (2 * f * fp) / (2 * fp * fp - f * fpp);
        if abs(f) < 1e-12 * abs(x + 1), break; end
    end
end

% ==============================================================================
% Gram point via Lambert W with Newton refinement
% ==============================================================================
function g = gram_point(n)
    if n <= 0, g = 0; return; end
    g = 2 * pi * n / lambert_W0(n / exp(1));
    % Newton refinement using exact θ(t)
    for iter = 1:3
        theta  = 0.5 * g * log(g / (2*pi)) - 0.5 * g - pi/8;
        dtheta = 0.5 * log(g / (2*pi));
        g = g + (pi * n - theta) / dtheta;
    end
end

function gvec = gram_points_vec(nvec)
    gvec = zeros(size(nvec));
    for i = 1:numel(nvec)
        gvec(i) = gram_point(nvec(i));
    end
end

% ==============================================================================
% Objection 1: b(N) Convergence
% ==============================================================================
function res = objection_1(gammas, MSG)
    N = numel(gammas);
    fprintf('\n%s\n%s\n%s\n%s\n', MSG.separator, MSG.obj1_title, ...
            MSG.obj1_desc, MSG.separator);

    checkpoints = [100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000];
    checkpoints = checkpoints(checkpoints <= N);

    fprintf('\n%10s  %14s  %8s\n', 'N', 'b(N)', 'Status');
    fprintf('%10s  %14s  %8s\n', '----------', '--------------', '--------');

    prev_bN = NaN;
    res = struct('N', {}, 'bN', {}, 'Status', {});
    for ci = 1:numel(checkpoints)
        cp = checkpoints(ci);
        idx = 1:cp;
        gram = gram_points_vec(idx');
        bN = mean(abs(gammas(idx) - gram));

        if isnan(prev_bN)
            status = '—';
        elseif bN < prev_bN * 1.05
            status = '↓';
        else
            status = '↑';
        end
        fprintf('%10d  %14.8f  %8s\n', cp, bN, status);
        res(ci).N = cp; res(ci).bN = bN; res(ci).Status = status;
        prev_bN = bN;
    end

    final_bN = res(end).bN;
    if final_bN < 0.01
        verdict = MSG.obj1_converge;
    elseif final_bN < 0.5
        verdict = MSG.obj1_stable;
    else
        verdict = MSG.obj1_diverge;
    end
    fprintf('\n%s\n', verdict);
end

% ==============================================================================
% Objection 2: GUE Spacing KS Test
% ==============================================================================
function res = objection_2(gammas, MSG)
    N = numel(gammas);
    fprintf('\n%s\n%s\n%s\n%s\n', MSG.separator, MSG.obj2_title, ...
            MSG.obj2_desc, MSG.separator);

    gam  = gammas(1:N-1);
    dlt  = gammas(2:N) - gammas(1:N-1);
    lfac = log(gam / (2*pi)) / (2*pi);
    s    = dlt .* lfac;
    s    = s(isfinite(s) & s > 0);

    % KS test: compare empirical CDF to GUE CDF
    s_sort = sort(s);
    n_s = numel(s_sort);
    emp_cdf = (1:n_s)' / n_s;
    gue_cdf = 1 - exp(-pi * s_sort.^2 / 4);

    D_plus  = max(emp_cdf - gue_cdf);
    D_minus = max(gue_cdf - [0; emp_cdf(1:end-1)]);
    D = max(D_plus, D_minus);

    % Approximate p-value for one-sample KS test
    lambda = (sqrt(n_s) + 0.12 + 0.11/sqrt(n_s)) * D;
    p_val = 0;
    for k = -5:5
        p_val = p_val + (-1)^k * exp(-2 * k^2 * lambda^2);
    end
    p_val = max(0, min(1, p_val));

    fprintf('\n%18s: %.8f\n', 'D-statistic', D);
    fprintf('%18s: %.6e\n', 'p-value', p_val);

    if p_val > 0.05
        verdict = MSG.obj2_pass;
    else
        verdict = MSG.obj2_fail;
    end
    fprintf('\n%s\n', verdict);
    res = struct('D', D, 'pvalue', p_val);
end

% ==============================================================================
% Objection 3: Large-T Decay Slope
% ==============================================================================
function res = objection_3(gammas, MSG)
    N = numel(gammas);
    fprintf('\n%s\n%s\n%s\n%s\n', MSG.separator, MSG.obj3_title, ...
            MSG.obj3_desc, MSG.separator);

    start = max(1, floor(N * 0.5));
    idx = start:N;
    gram = gram_points_vec(idx');
    dev = abs(gammas(idx) - gram);

    valid = isfinite(dev) & dev > 0;
    log_gamma = log(gammas(idx(valid)));
    log_dev   = log(dev(valid));

    % Linear regression
    X = [ones(numel(log_gamma),1), log_gamma];
    beta = X \ log_dev;
    slope = beta(2);

    % Standard error
    residuals = log_dev - X * beta;
    s2 = sum(residuals.^2) / (numel(log_gamma) - 2);
    XtXinv = inv(X' * X);
    stderr = sqrt(s2 * XtXinv(2,2));

    fprintf('\n%18s: %.6f\n', 'Slope', slope);
    fprintf('%18s: %.6f\n', 'Std Error', stderr);
    fprintf('%18s: -0.5\n', 'Target');

    if abs(slope - (-0.5)) < 0.15
        verdict = MSG.obj3_pass;
    else
        verdict = MSG.obj3_fail;
    end
    fprintf('\n%s\n', verdict);
    res = struct('slope', slope, 'stderr', stderr);
end
