%% spinor38.m — Test 38: 64 spinor structures of the Klein quartic (MATLAB/Octave port)
% Self-implemented cyclic Jacobi eigenvalue algorithm (eig() NOT used).
% Run (Octave): octave spinor38.m [repo-root]   |   MATLAB: spinor38('repo-root')
%
% Validated C++ reference output: isospectrality max|dlambda| = 3.419e-14,
% <r> = 0.4515710793, VERDICT PASS.

function spinor38()
  dd = find_data_dir();
  % ---- classes ----
  fid = fopen(fullfile(dd, 'spinor_classes.csv'), 'r');
  hdr = fgetl(fid);
  classes = {};
  while true
    ln = fgetl(fid);
    if ~ischar(ln), break; end
    if isempty(strtrim(ln)), continue; end
    classes{end+1} = ln; %#ok<AGROW>
  end
  fclose(fid);
  nclasses = numel(classes);
  cls_idx = zeros(nclasses,1); orbit = zeros(nclasses,1); arf = zeros(nclasses,1);
  signs = zeros(nclasses,84);
  for i = 1:nclasses
    parts = strsplit(classes{i}, ',', 'CollapseDelimiters', false);
    cls_idx(i) = str2double(parts{1});
    orbit(i) = str2double(parts{2});
    arf(i) = str2double(parts{3});
    sv = regexp(strtrim(parts{4}), '\s+', 'split');
    for k = 1:84
      signs(i,k) = str2double(sv{k});
    end
  end
  % ---- edges ----
  fid = fopen(fullfile(dd, 'klein_graph_edges.csv'), 'r');
  fgetl(fid);
  edges = [];
  while true
    ln = fgetl(fid);
    if ~ischar(ln), break; end
    if isempty(strtrim(ln)), continue; end
    p = strsplit(strtrim(ln), ',');
    edges = [edges; str2double(p{2}), str2double(p{3})]; %#ok<AGROW>
  end
  fclose(fid);
  % ---- reference stats ----
  fid = fopen(fullfile(dd, 'reference_stats.json'), 'r');
  js = fread(fid, '*char')';
  fclose(fid);
  r_ref = json_num(js, 'r_mean_reference');
  n_zero_ref = round(json_num(js, 'n_zero_modes'));
  representative = round(json_num(js, 'representative_class'));

  N = 56;
  n_odd = sum(orbit == 0);

  % ---- spectra of all odd-orbit classes (self-implemented Jacobi) ----
  k = 0;
  spectra = zeros(N, n_odd);
  rep = zeros(N,1);
  for i = 1:nclasses
    if orbit(i) ~= 0, continue; end
    A = zeros(N, N);
    for e = 1:size(edges,1)
      u = edges(e,1) + 1; v = edges(e,2) + 1;
      A(u,v) = signs(i,e);
      A(v,u) = signs(i,e);
    end
    k = k + 1;
    spectra(:,k) = jacobi_eigen(A);
    if cls_idx(i) == representative
      rep = spectra(:,k);
    end
  end

  % ---- isospectrality ----
  isomax = 0;
  for a = 1:k
    for b = (a+1):k
      isomax = max(isomax, max(abs(spectra(:,a) - spectra(:,b))));
    end
  end

  % ---- zero modes and <r> (fold |lambda|) ----
  lam = abs(rep);
  n_zero = sum(lam < 1e-8);
  lam = sort(lam);
  dsp = diff(lam);
  dsp = dsp(dsp > 1e-8);
  ratios = min(dsp(1:end-1), dsp(2:end)) ./ max(dsp(1:end-1), dsp(2:end));
  r_mean = mean(ratios);

  iok = isomax < 1e-9;
  rok = abs(r_mean - r_ref) < 1e-6;
  ok = iok && rok && (n_zero == n_zero_ref);

  fprintf('Test 38 - 64 spinor structures of the Klein quartic (MATLAB port)\n');
  fprintf('classes loaded: %d | odd-orbit members: %d\n', nclasses, n_odd);
  fprintf('isospectrality within the odd orbit: max|dlambda| = %.3e -> %s\n', ...
          isomax, ternary(iok, 'PASS', 'FAIL'));
  fprintf('zero modes (representative): %d (expected %d)\n', n_zero, n_zero_ref);
  fprintf('<r> (representative): %.10f (reference 0.4515710793) -> %s\n', ...
          r_mean, ternary(rok, 'PASS', 'FAIL'));
  fprintf('VERDICT: %s\n', ternary(ok, 'PASS', 'FAIL'));
  if ~ok, exit(1); end
end

function v = json_num(js, key)
  pat = ['"' key '":'];
  i = strfind(js, pat);
  if isempty(i), v = 0; return; end
  rest = js(i(1)+numel(pat):end);
  tok = strtok(strtrim(rest), ' ,}');
  v = str2double(tok);
end

function out = ternary(cond, a, b)
  if cond, out = a; else, out = b; end
end

function w = jacobi_eigen(Ain)
  N = size(Ain, 1);
  A = Ain;
  for sweep = 1:200
    off = 0;
    for p = 1:N-1
      for q = p+1:N
        off = off + A(p,q)^2;
      end
    end
    if off < 1e-24, break; end
    for p = 1:N-1
      for q = p+1:N
        if abs(A(p,q)) < 1e-15, continue; end
        tau = (A(q,q) - A(p,p)) / (2 * A(p,q));
        t = sign(tau) / (abs(tau) + sqrt(1 + tau^2));
        c = 1 / sqrt(1 + t^2);
        s = t * c;
        for kk = 1:N
          akp = A(kk,p); akq = A(kk,q);
          A(kk,p) = c*akp - s*akq;
          A(kk,q) = s*akp + c*akq;
        end
        for kk = 1:N
          apk = A(p,kk); aqk = A(q,kk);
          A(p,kk) = c*apk - s*aqk;
          A(q,kk) = s*apk + c*aqk;
        end
      end
    end
  end
  w = diag(A)';
  w = sort(w);
end

function dd = find_data_dir()
  dd = pwd();
  for up = 1:6
    cand = fullfile(dd, 'verification', 'spinor64', 'data', 'spinor_classes.csv');
    if exist(cand, 'file'), return; end
    dd = fullfile(dd, '..');
  end
  error('data dir not found; run from inside the repository');
end
