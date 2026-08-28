module ZerosLoader
  ( loadZeros
  , lambertW
  , gramPoint
  , gueCDF
  ) where

import Data.Char (isDigit, isSpace)
import Data.List (isPrefixOf)
import System.IO
import Text.Read (readMaybe)

-- | Available zero data sources.
data ZeroSource = ZeroSource
  { srcName     :: String
  , srcFile     :: String
  , srcMaxZeros :: Int   -- 0 = unknown
  }

zeroSources :: [ZeroSource]
zeroSources =
  [ ZeroSource "50000" "zeta_zeros_50000.txt"           13661
  , ZeroSource "500k"  "zeta_zeros_500k_odlyzko.txt"    500000
  , ZeroSource "2M"    "zeta_zeros_2M_odlyzko.txt"      2000000
  , ZeroSource "highT" "zeta_zeros_highT_blocks.txt"    0
  , ZeroSource "zeros6" "zeros6.txt"                     2000000
  ]

-- | Auto-select smallest source that can hold `count` zeros.
autoSelect :: Int -> ZeroSource
autoSelect count = case filter ok zeroSources of
  (s:_) -> s
  []    -> last zeroSources
  where ok s = srcMaxZeros s >= count || srcMaxZeros s == 0

-- | Find a source by name.
findSource :: String -> Maybe ZeroSource
findSource name = case filter ((== name) . srcName) zeroSources of
  (s:_) -> Just s
  []    -> Nothing

-- | Load zeros from dataDir, optionally truncating to count.
loadZeros :: FilePath -> Int -> String -> IO [Double]
loadZeros dataDir count source = do
  let src = case source of
        ""    -> autoSelect count
        "auto" -> autoSelect count
        name  -> case findSource name of
          Just s  -> s
          Nothing -> autoSelect count
  let path = dataDir ++ "/" ++ srcFile src
  zs <- parseZeroFile path
  return $ if count > 0 && count < length zs then take count zs else zs

-- | Parse a zero file — lazy I/O via readFile + lines.
parseZeroFile :: FilePath -> IO [Double]
parseZeroFile path = do
  contents <- readFile path
  return $ map read . filter isValid . map strip $ lines contents
  where
    strip = reverse . dropWhile isSpace . reverse . dropWhile isSpace
    isValid l = not (null l) && not ("#" `isPrefixOf` l) && hasDigit l
    hasDigit = any (\c -> isDigit c || c == '.' || c == 'e' || c == 'E' || c == '-' || c == '+')

-- ---------- Lambert W & Gram-point math ----------

-- | Lambert W (principal branch W₀) via Halley's iteration.
lambertW :: Double -> Double
lambertW z
  | z <= 0    = 0
  | otherwise = go (max 0.01 (log z)) 0
  where
    go w i
      | i >= 50   = w
      | abs delta < 1e-15 * max 1 (abs w) = w
      | abs denom < 1e-30                 = w
      | otherwise = go (w - delta) (i + 1)
      where
        ew     = exp w
        f      = w * ew - z
        fp     = ew * (w + 1)
        fpp    = ew * (w + 2)
        denom  = 2 * fp * fp - f * fpp
        delta  = 2 * f * fp / denom

-- | Riemann-Siegel theta (asymptotic).
rsTheta :: Double -> Double
rsTheta t = 0.5 * t * log (t / (2 * pi)) - 0.5 * t - pi / 8

-- | Derivative of theta.
rsThetaPrime :: Double -> Double
rsThetaPrime t = 0.5 * log (t / (2 * pi))

-- | Gram point γ̃_n via Lambert W initial + Newton refinement.
gramPoint :: Int -> Double
gramPoint n
  | n <= 0    = 17.44
  | otherwise = newton (2 * pi * exp 1 * exp (lambertW (nf / exp 1))) (nf * pi) 0
  where
    nf = fromIntegral n
    newton t target i
      | i >= 30                      = t
      | abs delta < 1e-12 * t        = t
      | abs fp < 1e-30               = t
      | otherwise                    = newton (t - delta) target (i + 1)
      where
        f     = rsTheta t - target
        fp    = rsThetaPrime t
        delta = f / fp

-- | GUE cumulative distribution function: 1 - exp(-πs²/4).
gueCDF :: Double -> Double
gueCDF s = 1 - exp (-pi * s * s / 4)
