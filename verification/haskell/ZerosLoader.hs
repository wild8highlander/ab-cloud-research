{-# LANGUAGE ForeignFunctionInterface #-}
-- | Zeros loading + the canonical numeric kernel (CANON_SPEC.md v3.0).
-- Canon: meridian-spectral-observatory golden (selftest 199/199).
module ZerosLoader
  ( loadZeros
  , lambertW
  , gramPoint
  , gueCDF
  , myErf
  , computeBN
  , computeBNOffset
  , computeSpacings
  , ksTestDP
  , ksAsymptoticPValue
  , cvmTest
  , adStat
  , meanRatio
  , linreg
  , selfcheck
  , SCRow(..)
  , Obj1Res(..)
  , Obj2Res(..)
  , Obj3Res(..)
  , LinregRes(..)
  , runObjection1
  , runObjection2
  , runObjection3
  ) where

import Data.Char (isSpace)
import Data.List (foldl', sort, sortBy)
import Data.Array (Array, listArray, (!), bounds)
import System.IO
import Text.Read (readMaybe)

-- | Available zero data sources (CANON_SPEC §9).
data ZeroSource = ZeroSource
  { srcName     :: String
  , srcFile     :: String
  , srcMaxZeros :: Int
  }

zeroSources :: [ZeroSource]
zeroSources =
  [ ZeroSource "50k"      "zeta_zeros_50000.txt"           13661
  , ZeroSource "50k_full" "zeta_zeros_50000_embedded.txt"  50000
  , ZeroSource "500k"     "zeta_zeros_500k_odlyzko.txt"    500000
  , ZeroSource "2M"       "zeta_zeros_2M_odlyzko.txt"      2001052
  , ZeroSource "highT"    "zeta_zeros_highT_blocks.txt"    30000
  , ZeroSource "csv"      "zeta_zeros_50000.csv"           13661
  , ZeroSource "zeros6"   "zeros6.txt"                     2001052
  ]

autoSelect :: Int -> ZeroSource
autoSelect count =
  case foldl' step Nothing zeroSources of
    Just s  -> s
    Nothing -> last zeroSources
  where
    step (Just best) s = Just (if srcMaxZeros s >= count && srcMaxZeros s < srcMaxZeros best then s else best)
    step Nothing s     = if srcMaxZeros s >= count then Just s else Nothing

findSource :: String -> Maybe ZeroSource
findSource name = case filter ((== name) . srcName) zeroSources of
  (s:_) -> Just s
  []    -> Nothing

-- | Load zeros from dataDir, truncating to count when count > 0.
loadZeros :: FilePath -> Int -> String -> IO [Double]
loadZeros dataDir count source = do
  let src = case source of
        ""     -> autoSelect count
        "auto" -> autoSelect count
        name   -> maybe (autoSelect count) id (findSource name)
  let path = dataDir ++ "/" ++ srcFile src
  putStrLn ("  Data file: " ++ path ++ " (source '" ++ srcName src ++ "')")
  zs <- parseZeroFile path (srcName src == "csv") (srcName src == "highT")
  let sorted = sort zs
  return $ if count > 0 && count < length sorted then take count sorted else sorted

strip :: String -> String
strip = f . f where f = reverse . dropWhile isSpace

-- | Parse a zero file: '#' comments, blanks; csv = 2nd field; highT block offsets.
parseZeroFile :: FilePath -> Bool -> Bool -> IO [Double]
parseZeroFile path isCSV isHighT = do
  contents <- readFile path
  return $ parseLines (lines contents) 0
  where
    parseLines [] _ = []
    parseLines (l:ls) off =
      let t = strip l
      in case t of
           "" -> parseLines ls off
           ('#':_) ->
             let off' = if isHighT
                        then case findOffset t of
                               Just v  -> v
                               Nothing -> off
                        else off
             in parseLines ls off'
           _ -> case value of
                  Just v  -> (if v + off > 0 then [v + off] else []) ++ parseLines ls off
                  Nothing -> parseLines ls off
      where
        value | isCSV = case break (== ',') t of
                          (_, ',' : rest) -> readMaybe (strip (takeWhile (/= ',') rest))
                          _               -> Nothing
              | otherwise = readMaybe t

findOffset :: String -> Maybe Double
findOffset s = go (words s)
  where
    go [] = Nothing
    go (w:ws) = case break (== '=') w of
      ("offset", '=' : v) -> readMaybe v
      _                   -> go ws

-- ---------------------------------------------------------------------------
-- Lambert W (CANON_SPEC §1)
-- ---------------------------------------------------------------------------
lambertW :: Double -> Double
lambertW x
  | x <= 0    = 0
  | otherwise = go (if w0 < 0 then x else w0) (50 :: Int)
  where
    w0 = log x
    go w i
      | i <= 0    = w
      | abs delta < 1e-14 * (1 + abs w) = w'
      | abs fp < 1e-30  = w
      | otherwise       = go w' (i - 1)
      where
        ew = exp w
        fp = ew * (w + 1)
        delta = (w * ew - x) / fp
        w' = w - delta

-- ---------------------------------------------------------------------------
-- Gram point (CANON_SPEC §2): seed + EXACTLY 8 Newton iterations, 5-term theta
-- ---------------------------------------------------------------------------
gramPoint :: Int -> Double
gramPoint n
  | n <= 0    = 0
  | otherwise = iterateN 8 step t0
  where
    nf = fromIntegral n :: Double
    t0 = 2 * pi * nf / lambertW (nf / exp 1)
    step t =
      let arg = t / (2 * pi)
          theta = 0.5 * t * log arg - 0.5 * t - pi / 8
                  + 1 / (48 * t) + 7 / (5760 * t^3)
          dtheta = 0.5 * log arg - 1 / (48 * t^2) - 21 / (5760 * t^4)
      in if abs dtheta < 1e-30 then t else t - (theta - nf * pi) / dtheta
    iterateN 0 _ x = x
    iterateN k f x = iterateN (k - 1) f (f x)

-- ---------------------------------------------------------------------------
-- erf (base Haskell has none): series |x|<2.2, Lentz CF erfc beyond (DLMF 7.9.1)
-- ---------------------------------------------------------------------------
myErf :: Double -> Double
myErf x
  | ax < 2.2  = 2 / sqrt pi * series ax
  | otherwise = if x >= 0 then v else negate v
  where
    ax = abs x
    v = 1 - erfcCF ax
    series a =
      let x2 = a * a
          go term s k
            | abs add < 1e-18 * abs s = s
            | otherwise = go next (s + add) (k + 1)
            where
              next = term * negate x2 / fromIntegral k
              add  = next / (2 * fromIntegral k + 1)
      in go a a (1 :: Int)

-- erfc via modified Lentz on sqrt(pi) e^{z^2} erfc(z) ~ 1/(z + (1/2)/(z + ...))
erfcCF :: Double -> Double
erfcCF z = exp (negate (z * z)) / (sqrt pi * f)
  where
    (_, _, _, f) = foldl' step (z, z, 0.0 :: Double, z) [1 .. 200 :: Int]
    -- state: (c, dLast, _, f)
    step (c, dLast, _, f) k =
      let a = fromIntegral k / 2
          d0 = z + a * dLast
          d1 = if d0 == 0 then 1e-300 else d0
          d2 = 1 / d1
          c1 = z + a / c
          c2 = if c1 == 0 then 1e-300 else c1
          delta = c2 * d2
          f' = f * delta
      in (c2, d1, (), if abs (delta - 1) < 1e-17 then f' else f')
    -- NOTE: we keep iterating; the last f wins (delta converged value stable)

-- ---------------------------------------------------------------------------
-- GUE CDF: canonical 32768-point table (CANON_SPEC §5)
-- ---------------------------------------------------------------------------
gueTN, gueSMAXD :: Int
gueTN = 32768

gueSMAX :: Double
gueSMAX = 5.0

gueExact :: Double -> Double
gueExact s
  | s <= 0    = 0
  | otherwise = myErf (2 * s / sqrt pi) - (4 * s / pi) * exp (negate (4 * s * s / pi))

gueTable :: Array Int Double
gueTable = listArray (0, gueTN - 1)
  [ gueExact (fromIntegral i * gueSMAX / fromIntegral (gueTN - 1)) | i <- [0 .. gueTN - 1] ]

-- | GUE (beta=2) Wigner surmise CDF via the canonical table.
gueCDF :: Double -> Double
gueCDF s
  | s <= 0    = 0
  | s >= gueSMAX = gueExact s
  | i < 0 || i >= gueTN - 1 = gueExact s
  | otherwise = (1 - t) * gueTable ! i + t * gueTable ! (i + 1)
  where
    x = s * fromIntegral (gueTN - 1) / gueSMAX
    i = floor x :: Int
    t = x - fromIntegral i

-- ---------------------------------------------------------------------------
-- b(N), spacings, statistics (CANON_SPEC §3–§6)
-- ---------------------------------------------------------------------------
computeBN :: [Double] -> Int -> Double
computeBN zeros n
  | n <= 0 || n > length zeros = 0/0
  | otherwise = go (take n zeros) 1 0 / fromIntegral n
  where
    go [] _ acc = acc
    go (z:zs) k acc = go zs (k + 1) (acc + abs (z - gramPoint k))

computeBNOffset :: [Double] -> Int -> Int -> Double
computeBNOffset zeros n off
  | n <= 0 || off + n > length zeros = 0/0
  | otherwise = go (take n zeros) (off + 1) 0 / fromIntegral n
  where
    go [] _ acc = acc
    go (z:zs) k acc = go zs (k + 1) (acc + abs (z - gramPoint k))

computeSpacings :: [Double] -> [Double]
computeSpacings [] = []
computeSpacings zs = go zs
  where
    go (a:b:rest)
      | a <= 0    = go (b : rest)
      | otherwise = (b - a) * log (a / (2 * pi)) / (2 * pi) : go (b : rest)
    go _ = []

ksAsymptoticPValue :: Double -> Double
ksAsymptoticPValue lam
  | lam <= 0  = 1
  | lam < 0.6 = clamp (1 - sqrt (2 * pi) / lam * s2)
  | otherwise = clamp (2 * s)
  where
    clamp v = max 0 (min 1 v)
    s2 = sum' (takeWhile (\t -> t >= 1e-18)
               [exp (negate ((fromIntegral (2*k - 1)^2 * pi^2) / (8 * lam^2))) | k <- [1..1000]])
    s  = sum' (takeWhile (\t -> abs t >= 1e-18)
               [fromIntegral ((-1)^(k+1)) * exp (negate (2 * fromIntegral k^2 * lam^2)) | k <- [1..100]])
    sum' = foldl' (+) 0

ksTestDP :: [Double] -> (Double, Double)
ksTestDP sp = (d, ksAsymptoticPValue lam)
  where
    s = sort sp
    n = fromIntegral (length s) :: Double
    d = maximum' 0 [max (abs (fromIntegral i / n - f)) (abs (fromIntegral (i - 1) / n - f))
                    | (i, x) <- zip [1 ..] s, let f = gueCDF x]
    maximum' acc [] = acc
    maximum' acc (x:xs) = maximum' (max acc x) xs
    lam = (sqrt n + 0.12 + 0.11 / sqrt n) * d

cvmTest :: [Double] -> Double
cvmTest sp = 1 / (12 * n) + foldl' (+) 0
  [ let u = gueCDF x
        d = u - (2 * fromIntegral i - 1) / (2 * n)
    in d * d
  | (i, x) <- zip [1 ..] (sort sp) ]
  where n = fromIntegral (length sp) :: Double

adStat :: [Double] -> Double
adStat sp
  | length sp < 2 = 0/0
  | otherwise = negate n - acc / n
  where
    s = sort sp
    n = fromIntegral (length s) :: Double
    -- pair s_i with s_{n+1-i} in O(n): zip with the reversed list
    acc = foldl' (+) 0
      [ fromIntegral (2*i - 1) * (log (clampL fi) + log (clampL (1 - fni)))
      | (i, (x, xr)) <- zip [1 ..] (zip s (reverse s))
      , let fi = gueCDF x
      , let fni = gueCDF xr ]
    clampL v = max 1e-300 (min (1 - 1e-16) v)

meanRatio :: [Double] -> (Double, Int)
meanRatio zs
  | length zs < 3 = (0/0, 0)
  | cnt == 0      = (0/0, 0)
  | otherwise     = (acc / fromIntegral cnt, cnt)
  where
    ds = zipWith (-) (drop 1 zs) zs
    pairs = zip ds (drop 1 ds)
    (acc, cnt) = foldl' step (0, 0) pairs
    step (a, c) (x, y) =
      let m = max x y
      in if x == 0 && y == 0 then (a, c) else (a + min x y / m, c + 1)

data LinregRes = LinregRes { lrSlope :: Double, lrIntercept :: Double, lrSE :: Double, lrR2 :: Double }

linreg :: [Double] -> [Double] -> LinregRes
linreg xs ys
  | abs den < 1e-30 = LinregRes 0 0 0 0
  | otherwise = LinregRes slope intercept se r2
  where
    n = fromIntegral (length xs) :: Double
    sx = foldl' (+) 0 xs
    sy = foldl' (+) 0 ys
    sxx = foldl' (+) 0 (map (\x -> x * x) xs)
    sxy = foldl' (+) 0 (zipWith (*) xs ys)
    syy = foldl' (+) 0 (map (\y -> y * y) ys)
    den = n * sxx - sx * sx
    slope = (n * sxy - sx * sy) / den
    intercept = (sy - slope * sx) / n
    ssTot = syy - sy * sy / n
    ssRes = foldl' (+) 0 [ (y - (slope * x + intercept))^2 | (x, y) <- zip xs ys ]
    r2 = if ssTot > 0 then 1 - ssRes / ssTot else 0
    se = if length xs > 2 && den > 0
           then sqrt ((ssRes / (n - 2)) * n / den)
           else 0

-- ---------------------------------------------------------------------------
-- Objections (CANON_SPEC §7) — structured results
-- ---------------------------------------------------------------------------
data Obj1Res = Obj1Res
  { o1ns :: [Int], o1bn :: [Double], o1converging :: Bool
  , o1hasFit :: Bool, o1fitA :: Double, o1fitS :: Double, o1fitR2 :: Double }

runObjection1 :: [Double] -> Obj1Res
runObjection1 zeros = Obj1Res ns bn converging hasFit fitA fitS fitR2
  where
    maxZ = length zeros
    ns0 = filter (<= maxZ) [100, 500, 1000, 5000, 10000, 50000]
    ns = if null ns0 then [min maxZ 100] else ns0
    bn = map (computeBN zeros) ns
    converging = and (zipWith (<) (drop 1 bn) bn)
    (hasFit, fitA, fitS, fitR2) =
      if length ns >= 3
        then let lx = [log (fromIntegral n) | (n, b) <- zip ns bn, n > 1, b > 0]
                 ly = [log b | (n, b) <- zip ns bn, n > 1, b > 0]
             in if length lx >= 3
                  then let lr = linreg lx ly
                       in (True, exp (lrIntercept lr), negate (lrSlope lr), lrR2 lr)
                  else (False, 0, 0, 0)
        else (False, 0, 0, 0)

data Obj2Res = Obj2Res
  { o2n :: Int, o2mean :: Double, o2var :: Double, o2d :: Double, o2p :: Double
  , o2w2 :: Double, o2a2 :: Double, o2r :: Double, o2nr :: Int, o2rejected :: Bool }

runObjection2 :: [Double] -> Obj2Res
runObjection2 zeros
  | length sp < 2 = Obj2Res (length sp) (0/0) (0/0) (0/0) (0/0) (0/0) (0/0) (0/0) 0 False
  | otherwise = Obj2Res (length sp) mean var d p (cvmTest sp) (adStat sp) r nr (p < 0.05)
  where
    sp = computeSpacings zeros
    mean = foldl' (+) 0 sp / fromIntegral (length sp)
    var = foldl' (+) 0 [ (s - mean)^2 | s <- sp ] / fromIntegral (length sp - 1)
    (d, p) = ksTestDP sp
    (r, nr) = meanRatio zeros

data Obj3Res = Obj3Res
  { o3slope :: Double, o3intercept :: Double, o3r2 :: Double
  , o3cilo :: Double, o3cihi :: Double, o3ok :: Bool }

runObjection3 :: [Double] -> Obj3Res
runObjection3 zeros
  | length lx < 3 = Obj3Res (0/0) (0/0) (0/0) (0/0) (0/0) False
  | otherwise = Obj3Res (lrSlope lr) (lrIntercept lr) (lrR2 lr)
                        (lrSlope lr - 1.96 * lrSE lr) (lrSlope lr + 1.96 * lrSE lr)
                        (abs (lrSlope lr + 0.5) < 0.1)
  where
    maxZ = length zeros
    ns0 = takeWhile (<= maxZ) (iterate (* 2) 50)
    ns = if (not (null ns0)) && last ns0 /= maxZ && maxZ > 100 then ns0 ++ [maxZ] else ns0
    bn = map (computeBN zeros) ns
    lx = [log (fromIntegral n) | (n, b) <- zip ns bn, b > 0]
    ly = [log b | (_, b) <- zip ns bn, b > 0]
    lr = linreg lx ly

-- ---------------------------------------------------------------------------
-- Self-check (CANON_SPEC §8)
-- ---------------------------------------------------------------------------
data SCRow = SCRow
  { scName :: String, scSkip :: Bool, scOk :: Bool
  , scGot :: Double, scExp :: Double, scDelta :: Double }

selfcheck :: [Double] -> ([SCRow], Int, Int)
selfcheck zeros = (rows, npass, nfail)
  where
    (rowsR, npass, nfail) = go [] 0 0 checks
    go rows np nf [] = (reverse rows, np, nf)
    go rows np nf (c:cs) =
      let r = c
      in if scSkip r
           then go (r : rows) np nf cs
           else go (r : rows) (if scOk r then np + 1 else np) (if scOk r then nf else nf + 1) cs
    add name got expv tol rel =
      let d = abs (got - expv) / (if rel then abs expv else 1.0)
          ok = not (isNaN got) && d <= tol
      in SCRow name False ok got expv d
    skipRow name = SCRow name True False 0 0 0
    checks = concat
      [ [ add ("lambert_w(" ++ show x ++ ")") (lambertW x) e 1e-12 True
        | (x, e) <- [ (0.5, 0.35173371124919584), (1.0, 0.5671432904097838)
                    , (3.7, 1.1599531786120223), (10.0, 1.7455280027406992)
                    , (271.8, 4.17576816800275), (12345.6, 7.417247034540566) ] ]
      , [ add ("gram_point(n=" ++ show n ++ ")") (gramPoint n) e 1e-6 False
        | (n, e) <- [ (1, 23.17028270133466), (2, 27.670182217848343)
                    , (3, 31.71797995477886), (10, 54.67523744685398)
                    , (100, 238.58259051450293), (1000, 1421.25638903275)
                    , (10000, 9878.910118894457), (50000, 40434.6952780045) ] ]
      , [ if n <= length zeros
            then add ("bN(N=" ++ show n ++ ")") (computeBN zeros n) e 1e-6 False
            else skipRow ("bN(N=" ++ show n ++ ")")
        | (n, e) <- [ (100, 3.3321638710140165), (500, 2.3912304957476382)
                    , (1000, 2.1072522951855435), (5000, 1.6299485869022874)
                    , (10000, 1.4794053414584762), (50000, 1.2125526772588608) ] ]
      , [ if length zeros >= 1500
            then add "bN(N=1000,off=500)" (computeBNOffset zeros 1000 500) 624.6201618180231 1e-6 False
            else skipRow "bN(N=1000,off=500)" ]
      , if length zeros >= 50000
          then let z5 = take 50000 zeros
                   sp = computeSpacings z5
                   mean = foldl' (+) 0 sp / fromIntegral (length sp)
                   var = foldl' (+) 0 [ (s - mean)^2 | s <- sp ] / fromIntegral (length sp - 1)
                   (d, p) = ksTestDP sp
                   (r, _) = meanRatio z5
               in [ add "spacings.mean" mean 0.999976001221201 1e-9 False
                  , add "spacings.var" var 0.1590654827835423 1e-9 False
                  , add "ks_zeros.D" d 0.021619337032982328 1e-9 False
                  , add "ks_zeros.p" p 9.567870399361496e-21 1e-6 True
                  , add "cvm_zeros.W2" (cvmTest sp) 8.177703317829403 1e-9 True
                  , add "ad_zeros.A2" (adStat sp) 61.49242624209728 1e-9 True
                  , add "rmean_zeros.r" r 0.6118798907208398 1e-9 False ]
          else map skipRow ["spacings.mean/var", "ks_zeros.D/p", "cvm_zeros.W2", "ad_zeros.A2", "rmean_zeros.r"]
      ]
