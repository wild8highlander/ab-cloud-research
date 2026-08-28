// ==============================================================================
// AB-Cloud Verification Suite — JavaScript/Node.js (Russian)
// ==============================================================================
// Русская версия. Для двуязычной, используйте ab_cloud_verify.js
// ==============================================================================

'use strict';

const fs = require('fs');
const path = require('path');
const readline = require('readline');
const zlib = require('zlib');

// --- Русские сообщения --------------------------------------------------------

const MSG_RU = {
  header:       'Комплекс проверки AB-Cloud — JavaScript/Node.js',
  separator:    '──────────────────────────────────────────────────────',
  loading:      'Загрузка нулей из: %s',
  loaded:       'Загружено %d нулей из %s',
  obj1_title:   'Возражение 1: Сходимость b(N)',
  obj1_desc:    'b(N) = (1/N) * Σ|γ_k - γ̃_k|, точки Грама через W Ламберта',
  obj1_n:       'N',
  obj1_bN:      'b(N)',
  obj1_status:  'Статус',
  obj1_converge:'СХОДИТСЯ — b(N) → 0 подтверждает AB-Cloud',
  obj1_stable:  'СТАБИЛЬНО — b(N) ≈ 0, AB-Cloud согласуется',
  obj1_diverge: 'РАСХОДИТСЯ — b(N) ↛ 0, возражение подтверждено',
  obj2_title:   'Возражение 2: KS-тест интервалов GUE',
  obj2_desc:    's_k = (γ_{k+1}-γ_k)·log(γ_k/2π)/(2π), сравн. с p(s)=(πs/2)·exp(-πs²/4)',
  obj2_stat:    'D-статистика',
  obj2_pval:    'p-значение',
  obj2_result:  'Результат',
  obj2_pass:    'ПРОЙДЕНО — интервалы GUE подтверждены (p > 0.05)',
  obj2_fail:    'НЕ ПРОЙДЕНО — интервалы GUE отклонены (p ≤ 0.05)',
  obj3_title:   'Возражение 3: Наклон убывания при больших T',
  obj3_desc:    'Регрессия log|γ_k - γ̃_k| от log(γ_k), ожид. наклон ≈ -0.5',
  obj3_slope:   'Наклон',
  obj3_stderr:  'Стд. ошибка',
  obj3_target:  'Цель',
  obj3_result:  'Результат',
  obj3_pass:    'ПРОЙДЕНО — Наклон ≈ -0.5, убывание AB-Cloud подтверждено',
  obj3_fail:    'НЕ ПРОЙДЕНО — Наклон отклоняется от -0.5',
  no_data:      'ОШИБКА: Нули не загружены. Проверьте каталог данных.',
  done:         'Проверка завершена.',
};

// --- Функция W Ламберта (главная ветвь), метод Халли -------------------------

function lambertW0(x) {
  if (x === 0) return 0;
  let w = x > 1 ? Math.log(x) - Math.log(Math.log(x)) : x;
  for (let iter = 0; iter < 50; iter++) {
    const ew = Math.exp(w), f = w * ew - x, fp = ew * (1 + w), fpp = ew * (2 + w);
    w -= (2 * f * fp) / (2 * fp * fp - f * fpp);
    if (Math.abs(f) < 1e-12 * Math.abs(x + 1)) break;
  }
  return w;
}

// --- Вычисление точки Грама через W Ламберта ---------------------------------

function gramPoint(n) {
  if (n <= 0) return 0;
  const TWO_PI = 2 * Math.PI;
  let g = TWO_PI * n / lambertW0(n / Math.E);
  for (let iter = 0; iter < 3; iter++) {
    const theta = 0.5 * g * Math.log(g / TWO_PI) - 0.5 * g - Math.PI / 8;
    const dtheta = 0.5 * Math.log(g / TWO_PI);
    g += (Math.PI * n - theta) / dtheta;
  }
  return g;
}

function gramPointsVec(nVec) { return nVec.map(n => gramPoint(n)); }

// --- Функция распределения интервалов GUE (гипотеза Вигнера) -----------------

function gueCDF(s) { return 1 - Math.exp(-Math.PI * s * s / 4); }

// --- Загрузка нулей из файлов данных (потоковая, поддерживает .gz) -----------

const FILE_MAP = {
  zeta_zeros_50000:     'zeta_zeros_50000.txt',
  zeta_zeros_500k:      'zeta_zeros_500k_odlyzko.txt',
  zeta_zeros_2M:        'zeta_zeros_2M_odlyzko.txt',
  zeta_zeros_highT:     'zeta_zeros_highT_blocks.txt',
  zeros6:               'zeros6.txt',
  zeta_zeros_50000_csv: 'zeta_zeros_50000.csv',
};

async function loadZeros(dataDir, count = 0, source = 'auto') {
  let selectedFile = null;
  if (source !== 'auto' && FILE_MAP[source]) {
    selectedFile = path.join(dataDir, FILE_MAP[source]);
  } else {
    for (const nm of Object.keys(FILE_MAP)) {
      const fp = path.join(dataDir, FILE_MAP[nm]);
      if (fs.existsSync(fp)) {
        selectedFile = fp;
        if (count > 0 && count <= 50000 && nm === 'zeta_zeros_50000') break;
      }
    }
  }
  if (!selectedFile || !fs.existsSync(selectedFile)) {
    throw new Error(`Файл данных не найден в: ${dataDir}`);
  }
  console.log(`Загрузка нулей из: ${selectedFile}`);

  const zeros = [];
  const isGz = selectedFile.endsWith('.gz');
  const isCsv = path.extname(selectedFile).toLowerCase() === '.csv';

  let stream = fs.createReadStream(selectedFile, { encoding: 'utf8' });
  if (isGz) {
    stream = fs.createReadStream(selectedFile).pipe(zlib.createGunzip()).setEncoding('utf8');
  }
  const rl = readline.createInterface({ input: stream, crlfDelay: Infinity });

  for await (const line of rl) {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith('#')) continue;
    if (isCsv) {
      const val = parseFloat(trimmed.split(',')[0]);
      if (!isNaN(val) && isFinite(val)) zeros.push(val);
    } else {
      for (const tok of trimmed.split(/\s+/).filter(t => t.length > 0)) {
        const val = parseFloat(tok);
        if (!isNaN(val) && isFinite(val)) zeros.push(val);
      }
    }
    if (count > 0 && zeros.length >= count) { rl.close(); break; }
  }
  if (count > 0 && zeros.length > count) zeros.length = count;
  console.log(`Загружено ${zeros.length} нулей из ${path.basename(selectedFile)}`);
  return zeros;
}

// --- Вспомогательные функции форматирования -----------------------------------

function padL(str, len) { return String(str).padStart(len); }
function padR(str, len) { return String(str).padEnd(len); }

// --- Возражение 1: Сходимость b(N) -------------------------------------------

function objection1(zeros) {
  const M = MSG_RU, N = zeros.length;
  console.log(`\n${M.separator}\n${M.obj1_title}\n${M.obj1_desc}\n${M.separator}`);
  const cp = [100,500,1000,5000,10000,50000,100000,500000,1000000].filter(c => c <= N);
  console.log(`\n${padR(M.obj1_n,10)}  ${padR(M.obj1_bN,14)}  ${padR(M.obj1_status,8)}`);
  console.log(`${padR('──────────',10)}  ${padR('──────────────',14)}  ${padR('────────',8)}`);
  const results = []; let prev = NaN;
  for (const c of cp) {
    const idx = Array.from({length:c},(_,i)=>i+1);
    const gram = gramPointsVec(idx);
    let sum = 0; for (let i=0;i<c;i++) sum += Math.abs(zeros[i]-gram[i]);
    const bN = sum/c;
    const st = isNaN(prev) ? '—' : bN < prev*1.05 ? '↓' : '↑';
    console.log(`${padL(c,10)}  ${padL(bN.toFixed(8),14)}  ${padR(st,8)}`);
    results.push({N:c,bN,status:st}); prev = bN;
  }
  const fb = results[results.length-1].bN;
  const v = fb<0.01 ? M.obj1_converge : fb<0.5 ? M.obj1_stable : M.obj1_diverge;
  console.log(`\n${v}`);
  return results;
}

// --- Возражение 2: KS-тест интервалов GUE ------------------------------------

function objection2(zeros) {
  const M = MSG_RU, N = zeros.length;
  console.log(`\n${M.separator}\n${M.obj2_title}\n${M.obj2_desc}\n${M.separator}`);
  const sp = [];
  for (let k=0;k<N-1;k++) {
    const d = (zeros[k+1]-zeros[k]) * Math.log(zeros[k]/(2*Math.PI)) / (2*Math.PI);
    if (isFinite(d)&&d>0) sp.push(d);
  }
  sp.sort((a,b)=>a-b);
  const n = sp.length;
  let Dp=0, Dm=0;
  for (let i=0;i<n;i++) {
    Dp = Math.max(Dp, (i+1)/n - gueCDF(sp[i]));
    Dm = Math.max(Dm, gueCDF(sp[i]) - i/n);
  }
  const D = Math.max(Dp,Dm);
  const lam = (Math.sqrt(n)+0.12+0.11/Math.sqrt(n))*D;
  let pv = 0;
  for (let k=-5;k<=5;k++) pv += Math.pow(-1,k)*Math.exp(-2*k*k*lam*lam);
  pv = Math.max(0,Math.min(1,pv));
  console.log(`\n${padR(M.obj2_stat+':',18)} ${D.toFixed(8)}`);
  console.log(`${padR(M.obj2_pval+':',18)} ${pv.toExponential(6)}`);
  console.log(`\n${pv>0.05 ? M.obj2_pass : M.obj2_fail}`);
  return {D, pValue:pv};
}

// --- Возражение 3: Наклон убывания при больших T -----------------------------

function objection3(zeros) {
  const M = MSG_RU, N = zeros.length;
  console.log(`\n${M.separator}\n${M.obj3_title}\n${M.obj3_desc}\n${M.separator}`);
  const start = Math.max(1,Math.floor(N*0.5));
  const idx = []; for (let i=start;i<=N;i++) idx.push(i);
  const gram = gramPointsVec(idx);
  const lg=[], ld=[];
  for (let i=0;i<idx.length;i++) {
    const dev = Math.abs(zeros[idx[i]-1]-gram[i]);
    if (isFinite(dev)&&dev>0) { lg.push(Math.log(zeros[idx[i]-1])); ld.push(Math.log(dev)); }
  }
  const n=lg.length;
  let sx=0,sy=0,sxy=0,sx2=0;
  for (let i=0;i<n;i++) { sx+=lg[i]; sy+=ld[i]; sxy+=lg[i]*ld[i]; sx2+=lg[i]*lg[i]; }
  const den=n*sx2-sx*sx;
  const a=(sy*sx2-sx*sxy)/den, slope=(n*sxy-sx*sy)/den;
  let ssr=0; for (let i=0;i<n;i++) ssr+=Math.pow(ld[i]-(a+slope*lg[i]),2);
  const se=Math.sqrt(ssr/(n-2)*n/den);
  console.log(`\n${padR(M.obj3_slope+':',18)} ${slope.toFixed(6)}`);
  console.log(`${padR(M.obj3_stderr+':',18)} ${se.toFixed(6)}`);
  console.log(`${padR(M.obj3_target+':',18)} -0.5`);
  console.log(`\n${Math.abs(slope-(-0.5))<0.15 ? M.obj3_pass : M.obj3_fail}`);
  return {slope, stderr:se};
}

// --- Главная функция (только русский) ----------------------------------------

async function abCloudVerifyRu(options = {}) {
  const { dataDir='../data', zeros=0, source='auto', objection='all' } = options;
  const M = MSG_RU;
  console.log(`\n${M.separator}\n${M.header}\n${M.separator}`);
  const gammas = await loadZeros(dataDir, zeros, source);
  if (gammas.length===0) { console.log(M.no_data); return null; }
  const results = {};
  if (['all','1'].includes(objection)) results.obj1 = objection1(gammas);
  if (['all','2'].includes(objection)) results.obj2 = objection2(gammas);
  if (['all','3'].includes(objection)) results.obj3 = objection3(gammas);
  console.log(`\n${M.separator}\n${M.done}\n`);
  return results;
}

module.exports = { abCloudVerifyRu, loadZeros, objection1, objection2, objection3, MSG_RU };
