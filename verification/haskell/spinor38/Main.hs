-- Main.hs — Test 38: 64 spinor structures of the Klein quartic (Haskell port)
-- Self-implemented cyclic Jacobi eigenvalue algorithm (std only).
-- Build: ghc -O2 Main.hs -o spinor38    Run: ./spinor38 [repo-root]
{-# LANGUAGE BangPatterns #-}

module Main (main) where

import           Data.List       (foldl', sort)
import           Control.Monad
import           Data.Array.ST
import           System.Directory (doesFileExist)
import           System.Environment (getArgs)
import           System.Exit
import           System.FilePath ((</>))
import           Text.Printf (printf)

data Cls = Cls { cIdx :: Int, cOrbit :: Int, cSigns :: [Double] }

findDataDir :: Maybe String -> IO (Maybe FilePath)
findDataDir mroot = firstJust (map tryRoot roots)
  where
    roots = maybe [] (: []) mroot ++ ["."]
    tryRoot r = up r (6 :: Int)
    up b 0 = return Nothing
    up b n = do
      ok <- doesFileExist (b </> "verification/spinor64/data/spinor_classes.csv")
      if ok
        then return (Just (b </> "verification/spinor64/data"))
        else up (b </> "..") (n - 1)
    firstJust [] = return Nothing
    firstJust (x : xs) = maybe (firstJust xs) (return . Just) x

parseClasses :: FilePath -> IO [Cls]
parseClasses f = do
  ls <- drop 1 . lines <$> readFile f
  return
    [ Cls (read a) (read b) (map read (words d))
    | l <- ls
    , not (null l)
    , let (a, r1) = break (== ',') l
    , let (b, r2) = break (== ',') (drop 1 r1)
    , let d = drop 1 r2
    ]

parseEdges :: FilePath -> IO [(Int, Int)]
parseEdges f = do
  ls <- drop 1 . lines <$> readFile f
  return
    [ (read a, read b)
    | l <- ls
    , not (null l)
    , let (a, r1) = break (== ',') l
    , let b = drop 1 r1
    ]

jsonNum :: String -> String -> Double
jsonNum js key = go (words js)
  where
    needle = '"' : key ++ "\":"
    go [] = 0
    go (t : ts)
      | needle `prefixOf` t = readNum (drop (length needle) t)
      | otherwise = go ts
    prefixOf pfx s = take (length pfx) s == pfx
    readNum = readTaking
    readTaking s = case reads (stripTrailing s) of
      [(v, _)] -> v
      _        -> 0
    stripTrailing = reverse . dropWhile (`elem` ",} ") . reverse

-- cyclic Jacobi eigenvalues of a real symmetric n x n matrix
jacobiEigen :: Int -> [((Int, Int), Double)] -> [Double]
jacobiEigen n entries = runST $ do
  arr <- newArray ((0, 0), (n - 1, n - 1)) 0.0
    :: ST s (STArray s (Int, Int) Double)
  forM_ entries $ \(ix, v) -> writeArray arr ix v
  let sweepLoop = do
        off <- offNorm arr
        when (off >= 1e-24) $ do
          forM_ [0 .. n - 2] $ \p ->
            forM_ [p + 1 .. n - 1] $ \q -> rotate arr p q
          sweepLoop
  sweepLoop
  diag <- forM [0 .. n - 1] $ \i -> readArray arr (i, i)
  return (sort diag)
  where
    offNorm arr = do
      vals <- forM [0 .. n - 2] $ \p ->
        forM [p + 1 .. n - 1] $ \q -> readArray arr (p, q)
      return (foldl' (\acc row -> acc + sum (map (\x -> x * x) row)) 0.0 vals)
    rotate arr p q = do
      apq <- readArray arr (p, q)
      when (abs apq >= 1e-15) $ do
        app <- readArray arr (p, p)
        aqq <- readArray arr (q, q)
        let tau = (aqq - app) / (2 * apq)
            t = (if tau >= 0 then 1 else -1)
                / (abs tau + sqrt (1 + tau * tau))
            c = 1 / sqrt (1 + t * t)
            s = t * c
        forM_ [0 .. n - 1] $ \k -> do
          akp <- readArray arr (k, p)
          akq <- readArray arr (k, q)
          writeArray arr (k, p) (c * akp - s * akq)
          writeArray arr (k, q) (s * akp + c * akq)
        forM_ [0 .. n - 1] $ \k -> do
          apk <- readArray arr (p, k)
          aqk <- readArray arr (q, k)
          writeArray arr (p, k) (c * apk - s * aqk)
          writeArray arr (q, k) (s * apk + c * aqk)

main :: IO ()
main = do
  args <- getArgs
  mdd <- findDataDir (case args of (a : _) -> Just a; _ -> Nothing)
  dd <- case mdd of
    Just d  -> return d
    Nothing -> do
      putStrLn "data dir not found; pass repo root as argument"
      exitWith (ExitFailure 2)
  classes <- parseClasses (dd </> "spinor_classes.csv")
  edges <- parseEdges (dd </> "klein_graph_edges.csv")
  js <- readFile (dd </> "reference_stats.json")
  let rRef = jsonNum js "r_mean_reference"
      nZeroRef = round (jsonNum js "n_zero_modes") :: Int
      representative = round (jsonNum js "representative_class") :: Int
      n = 56
      oddCls = filter ((== 0) . cOrbit) classes
      nOdd = length oddCls
      entries c =
        [ ((u, v), sg), ((v, u), sg)
        | (k, (u, v)) <- zip [0 ..] edges
        , let sg = cSigns c !! k ]
      spectra = [ jacobiEigen n (entries c) | c <- oddCls ]
      repSpectrum =
        head [ sp | (sp, c) <- zip spectra oddCls, cIdx c == representative ]
      isomax = maximum
        [ abs (x - y)
        | a <- spectra
        , b <- spectra
        , a /= b
        , (x, y) <- zip a b ]
      lam = sort (map abs repSpectrum)
      nZero = length (filter (< 1e-8) lam)
      dsp = [ d | d <- zipWith (-) (drop 1 lam) lam, d > 1e-8 ]
      ratios = [ min x y / max x y | (x, y) <- zip dsp (drop 1 dsp) ]
      rMean = sum ratios / fromIntegral (length ratios)
      iok = isomax < 1e-9
      rok = abs (rMean - rRef) < 1e-6
      ok = iok && rok && (nZero == nZeroRef)
  printf "Test 38 - 64 spinor structures of the Klein quartic (Haskell port)\n"
  printf "classes loaded: %d | odd-orbit members: %d\n" (length classes) nOdd
  printf "isospectrality within the odd orbit: max|dlambda| = %.3e -> %s\n"
    isomax (if iok then "PASS" else "FAIL")
  printf "zero modes (representative): %d (expected %d)\n" nZero nZeroRef
  printf "<r> (representative): %.10f (reference 0.4515710793) -> %s\n"
    rMean (if rok then "PASS" else "FAIL")
  printf "VERDICT: %s\n" (if ok then "PASS" else "FAIL")
  when (not ok) $ exitWith (ExitFailure 1)
