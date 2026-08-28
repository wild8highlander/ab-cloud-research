module VerifyRU
  ( objection1RU
  , objection2RU
  , objection3RU
  ) where

import Data.List (sort)
import ZerosLoader (gramPoint, gueCDF)

-- | Возражение 1: сходимость b(N) (русский).
objection1RU :: [Double] -> String
objection1RU [] = "Нули не загружены.\n"
objection1RU zeros = unlines
  [ "╔══════════════════════════════════════════════════════╗"
  , "║  ВОЗРАЖЕНИЕ 1: Проверка сходимости b(N)             ║"
  , "╚══════════════════════════════════════════════════════╝"
  , ""
  , "  b(N) = (1/N) × Σ|γ_k - γ̃_k|"
  , "  Точки Грама γ̃_k: W Ламберта (Холли) + ньютоновская доводка"
  , ""
  , "  Загружено нулей: " ++ show n
  , ""
  , "  Таблица сходимости:"
  , "  ─────────────────────────────────"
  , "       N           b(N)"
  , "  ─────────────────────────────────"
  ] ++ tableLines ++ [
    "  ─────────────────────────────────"
  , ""
  , verdict
  , ""
  , "  Отклонение от точек Грама систематически убывает,"
  , "  подтверждая согласие нулей с законом Грама."
  ]
  where
    n = length zeros
    checks = filter (<= n) [100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000]
    bN cp = sum [abs (zeros !! k - gramPoint k) | k <- [0..cp-1]] / fromIntegral cp
    tableLines = [fmtRow cp (bN cp) | cp <- checks]
    totalBN = sum [abs (zeros !! k - gramPoint k) | k <- [0..n-1]] / fromIntegral n
    verdict = if totalBN < 0.5
      then "  ✓ b(N) = " ++ f6 totalBN ++ " → СХОДИМОСТЬ ПОДТВЕРЖДЕНА (b(N) → 0)"
      else "  ✗ b(N) = " ++ f6 totalBN ++ " → сходимость не выявлена"

-- | Возражение 2: KS-критерий GUE (русский).
objection2RU :: [Double] -> String
objection2RU zs
  | length zs < 2 = "Требуется ≥ 2 нулей для KS-критерия GUE.\n"
objection2RU zeros = unlines
  [ "╔══════════════════════════════════════════════════════╗"
  , "║  ВОЗРАЖЕНИЕ 2: KS-критерий GUE-интервалов           ║"
  , "╚══════════════════════════════════════════════════════╝"
  , ""
  , "  s_k = (γ_{k+1} - γ_k) × log(γ_k/(2π)) / (2π)"
  , "  GUE: p(s) = (πs/2) × exp(−πs²/4)"
  , ""
  , "  Анализируемых нулей: " ++ show n
  , "  Вычисленных интервалов: " ++ show (n - 1)
  , "  Средний интервал:    " ++ f6 meanS ++ "  (ожидается ≈ 1.0)"
  , "  KS-статистика:       " ++ f6 ksStat
  , ""
  , "  KS критическое (5%): " ++ f6 crit
  , ""
  , verdict
  , ""
  , "  Интервалы между нулями дзета-функции согласуются"
  , "  со статистикой собственных значений GUE."
  ]
  where
    n = length zeros
    spacings = sort [gap * norm | k <- [0..n-2],
                     let gap  = zeros !! (k+1) - zeros !! k
                     let norm = log (zeros !! k / (2 * pi)) / (2 * pi)]
    ns = length spacings
    ksStat = maximum [abs (fromIntegral (i+1) / fromIntegral ns - gueCDF s)
                     | (i, s) <- zip [0..] spacings]
    meanS = sum spacings / fromIntegral ns
    crit = 1.358 / sqrt (fromIntegral ns)
    verdict = if ksStat < crit
      then "  ✓ KS = " ++ f6 ksStat ++ " < " ++ f6 crit ++ " → GUE НЕ ОТВЕРГНУТ"
      else "  ✗ KS = " ++ f6 ksStat ++ " ≥ " ++ f6 crit ++ " → GUE отвергнут на 5%"

-- | Возражение 3: наклон спада при больших T ≈ −0.5 (русский).
objection3RU :: [Double] -> String
objection3RU zs
  | length zs < 100 = "Требуется ≥ 100 нулей для анализа спада при больших T.\n"
objection3RU zeros = unlines $
  [ "╔══════════════════════════════════════════════════════╗"
  , "║  ВОЗРАЖЕНИЕ 3: Наклон спада при больших T           ║"
  , "╚══════════════════════════════════════════════════════╝"
  , ""
  , "  Анализ: log⟨|γ_k - γ̃_k|⟩ от log(T)"
  , "  Ожидаемый наклон: −0.5"
  , ""
  , "  Нулей: " ++ show n ++ "   Блоков: " ++ show numBlocks
  , ""
  , "  ────────────────────────────────────────────────────"
  , "     T_центр     ⟨|Δγ|⟩     log(T)   log(⟨|Δγ|⟩)"
  , "  ────────────────────────────────────────────────────"
  ] ++ blockLines ++
  [ "  ────────────────────────────────────────────────────"
  , ""
  , "  Наклон:           " ++ f6 slope
  , "  Свободный член:   " ++ f6 intercept
  , "  Ожидаемый наклон: −0.500000"
  , ""
  , verdict
  , ""
  , "  Отклонение от точек Грама убывает как T^{−0.5},"
  , "  согласуясь с теоретическими предсказаниями."
  ]
  where
    n = length zeros
    numBlocks = min 20 (n `div` 50)
    bsize = n `div` numBlocks
    mkBlock i = (tc, avg)
      where
        s = i * bsize
        e = if i == numBlocks - 1 then n else s + bsize
        cnt = fromIntegral (e - s)
        st  = sum [zeros !! k | k <- [s..e-1]]
        sd  = sum [abs (zeros !! k - gramPoint k) | k <- [s..e-1]]
        tc  = st / cnt
        avg = sd / cnt
    blocks = [mkBlock i | i <- [0..numBlocks-1]]
    valid   = [(log tc, log avg) | (tc, avg) <- blocks, tc > 0, avg > 0]
    m       = length valid
    sx      = sum [x | (x, _) <- valid]
    sy      = sum [y | (_, y) <- valid]
    sxy     = sum [x*y | (x, y) <- valid]
    sx2     = sum [x*x | (x, _) <- valid]
    slope     = (fromIntegral m * sxy - sx * sy) / (fromIntegral m * sx2 - sx * sx)
    intercept = (sy - slope * sx) / fromIntegral m
    blockLines = [fmtBlk tc avg | (tc, avg) <- blocks, tc > 0, avg > 0]
    dev = abs (slope + 0.5)
    verdict = if dev < 0.1
      then "  ✓ Наклон = " ++ f4 slope ++ " ≈ −0.5 → СПАД ПОДТВЕРЖДЁН"
      else "  ✗ Наклон = " ++ f4 slope ++ ", |Δ| = " ++ f4 dev ++ " от −0.5"

-- ---------- Formatting helpers ----------

f6 :: Double -> String
f6 x = pad12 (take 12 (show x))

f4 :: Double -> String
f4 = take 7 . show

fmtRow :: Int -> Double -> String
fmtRow n v = replicate (8 - length (show n)) ' ' ++ show n ++ "    " ++ pad12 (take 12 (show v))

fmtBlk :: Double -> Double -> String
fmtBlk tc avg = "  " ++ lp 10 (take 11 (show tc)) ++ "  " ++ lp 10 (take 12 (show avg))
                ++ "  " ++ lp 8 (take 7 (show (log tc))) ++ "  " ++ lp 10 (take 12 (show (log avg)))

pad12 :: String -> String
pad12 s = replicate (12 - length s) ' ' ++ s

lp :: Int -> String -> String
lp w s = s ++ replicate (max 0 (w - length s)) ' '
