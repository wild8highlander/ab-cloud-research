% ==============================================================================
% AB-Cloud Verification Suite — MATLAB Runner Script
% ==============================================================================
% Usage:
%   run_verify                    (default: all objections, English, ../data)
%   run_verify --zeros 50000
%   run_verify --objection 2 --lang ru
%   run_verify --source zeta_zeros_500k --zeros 100000
%
% Options:
%   --zeros N         Number of zeros to use (0 = all)
%   --source NAME     Data source: auto|zeta_zeros_50000|zeta_zeros_500k|
%                       zeta_zeros_2M|zeta_zeros_highT|zeros6|zeta_zeros_50000_csv
%   --objection 1|2|3|all   Which objection to verify
%   --lang en|ru      Output language
%   --data-dir DIR    Data directory (default: ../data)
% ==============================================================================

% --- Default options ---------------------------------------------------------
opts = struct( ...
    'zeros',     0, ...
    'source',    'auto', ...
    'objection', 'all', ...
    'lang',      'en', ...
    'dataDir',   '../data' ...
);

% --- Parse command-line arguments --------------------------------------------
args = varargin;
if nargin == 0 && ~isempty(getenv('MATLAB_CLI_ARGS'))
    args = strsplit(getenv('MATLAB_CLI_ARGS'));
end

i = 1;
while i <= numel(args)
    flag = args{i};
    if strcmp(flag, '--zeros') && i + 1 <= numel(args)
        opts.zeros = str2double(args{i+1}); i = i + 2;
    elseif strcmp(flag, '--source') && i + 1 <= numel(args)
        opts.source = args{i+1}; i = i + 2;
    elseif strcmp(flag, '--objection') && i + 1 <= numel(args)
        opts.objection = args{i+1}; i = i + 2;
    elseif strcmp(flag, '--lang') && i + 1 <= numel(args)
        opts.lang = args{i+1}; i = i + 2;
    elseif strcmp(flag, '--data-dir') && i + 1 <= numel(args)
        opts.dataDir = args{i+1}; i = i + 2;
    elseif strcmp(flag, '--help')
        fprintf('\nAB-Cloud Verification Suite — MATLAB Runner\n\n');
        fprintf('Usage: run_verify [options]\n\n');
        fprintf('Options:\n');
        fprintf('  --zeros N           Number of zeros to use (0 = all)\n');
        fprintf('  --source NAME       Data source (auto, zeta_zeros_50000, zeta_zeros_500k,\n');
        fprintf('                        zeta_zeros_2M, zeta_zeros_highT, zeros6,\n');
        fprintf('                        zeta_zeros_50000_csv)\n');
        fprintf('  --objection 1|2|3|all   Which objection(s) to verify\n');
        fprintf('  --lang en|ru        Output language\n');
        fprintf('  --data-dir DIR      Path to data directory (default: ../data)\n');
        fprintf('  --help              Show this help message\n\n');
        fprintf('Examples:\n');
        fprintf('  run_verify(''--zeros'', ''50000'', ''--objection'', ''1'', ''--lang'', ''en'')\n');
        fprintf('  run_verify(''--source'', ''zeta_zeros_500k'', ''--objection'', ''all'')\n\n');
        return;
    else
        fprintf('Unknown option: %s\n', flag);
        return;
    end
end

% --- Display configuration ---------------------------------------------------
fprintf('AB-Cloud MATLAB Runner\n');
fprintf('  Data dir:   %s\n', opts.dataDir);
fprintf('  Zeros:      %s\n', num2str(opts.zeros));
fprintf('  Source:     %s\n', opts.source);
fprintf('  Objection:  %s\n', opts.objection);
fprintf('  Language:   %s\n\n', opts.lang);

% --- Run verification --------------------------------------------------------
results = ab_cloud_verify( ...
    'dataDir',   opts.dataDir, ...
    'zeros',     opts.zeros, ...
    'source',    opts.source, ...
    'objection', opts.objection, ...
    'lang',      opts.lang ...
);

% --- Summary ----------------------------------------------------------------
if isempty(results)
    fprintf('Verification FAILED — no results returned.\n');
else
    fprintf('Verification completed successfully.\n');
end
