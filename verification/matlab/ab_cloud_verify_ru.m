function results = ab_cloud_verify_ru(varargin)
% ==============================================================================
% AB-Cloud Verification Suite — MATLAB (Russian)
% ==============================================================================
% Русская версия. Для двуязычной, используйте ab_cloud_verify.m
%
% Использование:
%   results = ab_cloud_verify_ru()
%   results = ab_cloud_verify_ru('dataDir', '../data', 'zeros', 50000, ...
%                                'source', 'auto', 'objection', 'all')
% ==============================================================================

    % --- Разбор параметров ---------------------------------------------------
    p = inputParser;
    addParameter(p, 'dataDir',   '../data',  @ischar);
    addParameter(p, 'zeros',     0,          @isnumeric);
    addParameter(p, 'source',    'auto',     @ischar);
    addParameter(p, 'objection', 'all',      @ischar);
    parse(p, varargin{:});
    dataDir = p.Results.dataDir;
    nZeros  = p.Results.zeros;
    src     = p.Results.source;
    obj     = p.Results.objection;

    % --- Русские сообщения ---------------------------------------------------
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

    fprintf('\n%s\n%s\n%s\n', MSG.separator, MSG.header, MSG.separator);
    gammas = load_zeros_ru(dataDir, nZeros, src, MSG);
    if isempty(gammas)
        fprintf('%s\n', MSG.no_data); results = []; return;
    end

    results = struct();
    if ismember(obj, {'all', '1'}), results.obj1 = obj1_ru(gammas, MSG); end
    if ismember(obj, {'all', '2'}), results.obj2 = obj2_ru(gammas, MSG); end
    if ismember(obj, {'all', '3'}), results.obj3 = obj3_ru(gammas, MSG); end
    fprintf('\n%s\n%s\n\n', MSG.separator, MSG.done);
end

% --- Загрузка нулей ----------------------------------------------------------
function gammas = load_zeros_ru(dataDir, count, source, MSG)
    files = struct( ...
        'zeta_zeros_50000',     fullfile(dataDir,'zeta_zeros_50000.txt'), ...
        'zeta_zeros_500k',      fullfile(dataDir,'zeta_zeros_500k_odlyzko.txt'), ...
        'zeta_zeros_2M',        fullfile(dataDir,'zeta_zeros_2M_odlyzko.txt'), ...
        'zeta_zeros_highT',     fullfile(dataDir,'zeta_zeros_highT_blocks.txt'), ...
        'zeros6',               fullfile(dataDir,'zeros6.txt'), ...
        'zeta_zeros_50000_csv', fullfile(dataDir,'zeta_zeros_50000.csv') ...
    );
    fnames = fieldnames(files);
    selected = '';
    if ~strcmp(source,'auto') && isfield(files,source)
        selected = files.(source);
    else
        for i = 1:numel(fnames)
            fp = files.(fnames{i});
            if exist(fp,'file'), selected = fp;
                if count>0 && count<=50000 && strcmp(fnames{i},'zeta_zeros_50000'), break; end
            end
        end
    end
    if isempty(selected) || ~exist(selected,'file'), error('Файл данных не найден в: %s',dataDir); end
    fprintf(MSG.loading+'\n', selected);
    [~,~,ext] = fileparts(selected);
    if strcmpi(ext,'.csv')
        T = readtable(selected,'FileType','text','ReadVariableNames',false);
        gammas = T{:,1};
    else
        fid = fopen(selected,'r');
        if fid==-1, error('Не удалось открыть: %s',selected); end
        gammas = [];
        while ~feof(fid)
            line = fgetl(fid); if ~ischar(line), continue; end
            line = strtrim(line); if isempty(line)||line(1)=='#', continue; end
            vals = sscanf(line,'%f'); gammas = [gammas; vals(:)];
        end
        fclose(fid);
    end
    gammas = gammas(:);
    if count>0 && count<numel(gammas), gammas = gammas(1:count); end
    fprintf(MSG.loaded+'\n', numel(gammas), selected(1:min(end,50)));
end

% --- W Ламберта (главная ветвь) ---------------------------------------------
function w = lambert_W0_ru(x)
    if x==0, w=0; return; end
    w = log(x)-log(log(x)); if x<=1, w=x; end
    for iter=1:50
        ew=exp(w); f=w*ew-x; fp=ew*(1+w); fpp=ew*(2+w);
        w=w-(2*f*fp)/(2*fp*fp-f*fpp);
        if abs(f)<1e-12*abs(x+1), break; end
    end
end

% --- Точка Грама ------------------------------------------------------------
function g = gram_point_ru(n)
    if n<=0, g=0; return; end
    g = 2*pi*n/lambert_W0_ru(n/exp(1));
    for iter=1:3
        theta=0.5*g*log(g/(2*pi))-0.5*g-pi/8; dtheta=0.5*log(g/(2*pi));
        g=g+(pi*n-theta)/dtheta;
    end
end
function gv = gram_vec_ru(nv)
    gv=zeros(size(nv)); for i=1:numel(nv), gv(i)=gram_point_ru(nv(i)); end
end

% --- Возражение 1 -----------------------------------------------------------
function res = obj1_ru(gammas, MSG)
    N=numel(gammas);
    fprintf('\n%s\n%s\n%s\n%s\n',MSG.separator,MSG.obj1_title,MSG.obj1_desc,MSG.separator);
    cp=[100,500,1000,5000,10000,50000,100000,500000,1000000]; cp=cp(cp<=N);
    fprintf('\n%10s  %14s  %8s\n','N','b(N)','Статус');
    fprintf('%10s  %14s  %8s\n','──────────','──────────────','────────');
    prev=NaN; res=struct('N',{},'bN',{},'Status',{});
    for ci=1:numel(cp)
        idx=1:cp(ci); gram=gram_vec_ru(idx'); bN=mean(abs(gammas(idx)-gram));
        if isnan(prev), st='—'; elseif bN<prev*1.05, st='↓'; else, st='↑'; end
        fprintf('%10d  %14.8f  %8s\n',cp(ci),bN,st);
        res(ci).N=cp(ci); res(ci).bN=bN; res(ci).Status=st; prev=bN;
    end
    fb=res(end).bN;
    if fb<0.01, v=MSG.obj1_converge; elseif fb<0.5, v=MSG.obj1_stable; else, v=MSG.obj1_diverge; end
    fprintf('\n%s\n',v);
end

% --- Возражение 2 -----------------------------------------------------------
function res = obj2_ru(gammas, MSG)
    N=numel(gammas);
    fprintf('\n%s\n%s\n%s\n%s\n',MSG.separator,MSG.obj2_title,MSG.obj2_desc,MSG.separator);
    gam=gammas(1:N-1); dlt=gammas(2:N)-gammas(1:N-1);
    lfac=log(gam/(2*pi))/(2*pi); s=dlt.*lfac; s=s(isfinite(s)&s>0);
    ss=sort(s); ns=numel(ss); ecdf=(1:ns)'/ns; gcdf=1-exp(-pi*ss.^2/4);
    Dp=max(ecdf-gcdf); Dm=max(gcdf-[0;ecdf(1:end-1)]); D=max(Dp,Dm);
    lam=(sqrt(ns)+0.12+0.11/sqrt(ns))*D; pv=0;
    for k=-5:5, pv=pv+(-1)^k*exp(-2*k^2*lam^2); end
    pv=max(0,min(1,pv));
    fprintf('\n%18s: %.8f\n','D-статистика',D); fprintf('%18s: %.6e\n','p-значение',pv);
    if pv>0.05, v=MSG.obj2_pass; else, v=MSG.obj2_fail; end
    fprintf('\n%s\n',v); res=struct('D',D,'pvalue',pv);
end

% --- Возражение 3 -----------------------------------------------------------
function res = obj3_ru(gammas, MSG)
    N=numel(gammas);
    fprintf('\n%s\n%s\n%s\n%s\n',MSG.separator,MSG.obj3_title,MSG.obj3_desc,MSG.separator);
    st=max(1,floor(N*0.5)); idx=st:N; gram=gram_vec_ru(idx'); dev=abs(gammas(idx)-gram);
    val=isfinite(dev)&dev>0; lg=log(gammas(idx(val))); ld=log(dev(val));
    X=[ones(numel(lg),1),lg]; beta=X\ld; slope=beta(2);
    resid=ld-X*beta; s2=sum(resid.^2)/(numel(lg)-2); XtXi=inv(X'*X); se=sqrt(s2*XtXi(2,2));
    fprintf('\n%18s: %.6f\n','Наклон',slope); fprintf('%18s: %.6f\n','Стд. ошибка',se);
    fprintf('%18s: -0.5\n','Цель');
    if abs(slope-(-0.5))<0.15, v=MSG.obj3_pass; else, v=MSG.obj3_fail; end
    fprintf('\n%s\n',v); res=struct('slope',slope,'stderr',se);
end
