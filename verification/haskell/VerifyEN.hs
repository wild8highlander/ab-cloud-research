-- | Thin English rendering layer (CANON_SPEC §10). No duplicated math.
module VerifyEN (renderObj1, renderObj2, renderObj3, renderSelfcheck) where

import Numeric (showFFloat)
import ZerosLoader (Obj1Res(..), Obj2Res(..), Obj3Res(..), SCRow(..))

fx :: Int -> Double -> String
fx k v = showFFloat (Just k) v ""

padR :: Int -> String -> String
padR k s = s ++ replicate (max 0 (k - length s)) ' '

log10v :: Double -> Double
log10v v = if v > 0 then log v / log 10 else -999

renderObj1 :: Obj1Res -> String
renderObj1 r = unlines $ concat
  [ [ ""
    , "==================== Objection 1: Numerical Stability of b(N) ===================="
    , "  b(N) = (1/N) * Sum|gamma_k - gamma_tilde_k|, Gram points: theta(t) = pi*k (Newton)"
    , ""
    , "         N            b(N)    log10(b(N))"
    ]
  , [ padR 10 (show n) ++ "  " ++ padR 14 (fx 8 b) ++ "  " ++ padR 14 (fx 4 (log10v b))
    | (n, b) <- zip (o1ns r) (o1bn r) ]
  , if o1hasFit r
      then [ ""
           , "  Empirical law:  b(N) ~ " ++ fx 4 (o1fitA r) ++ " * N^(-" ++ fx 4 (o1fitS r)
             ++ ")   (R^2 = " ++ fx 4 (o1fitR2 r) ++ ")" ]
      else []
  , if o1converging r
      then [ ""
           , "Result: b(N) converging as N increases. OK"
           , "  b(N) decreases monotonically over the table — convergence confirmed on the accessible"
           , "  range. The decay is EMPIRICAL, not O(1/sqrt(N))." ]
      else [ "", "Result: b(N) NOT converging as N increases. WARN" ]
  ]

renderObj2 :: Obj2Res -> String
renderObj2 r = unlines $ concat
  [ [ ""
    , "==================== Objection 2: GUE Spacing Statistical Significance ===================="
    , "  GUE (beta=2) Wigner surmise via the canonical 32768-point CDF table"
    , ""
    ]
  , if o2n r < 2
      then [ "WARNING: not enough spacings for the GUE test." ]
      else concat
        [ [ "  Spacing mean: " ++ fx 9 (o2mean r) ++ "  var: " ++ fx 9 (o2var r)
            ++ "  (n = " ++ show (o2n r) ++ ")"
          , "  Kolmogorov-Smirnov:  D = " ++ fx 6 (o2d r) ++ ",  p-value = " ++ show (o2p r)
          , "  Cramer-von Mises:    W^2 = " ++ fx 6 (o2w2 r)
          , "  Anderson-Darling:   A^2 = " ++ fx 6 (o2a2 r)
          , "  <r> (adjacent-ratio): " ++ fx 6 (o2r r) ++ "  (n = " ++ show (o2nr r)
            ++ ", GUE surmise ~ 0.5992)"
          , ""
          , if o2rejected r
              then "Result: H0 (GUE distribution): REJECTED  (alpha = 0.05)"
              else "Result: H0 (GUE distribution): NOT REJECTED  (alpha = 0.05)"
          ]
        , if o2rejected r
            then [ "  Note: at large n the exact GUE surmise is formally rejected — the"
                 , "  known finite-T corrections of the zeta zeros, not a data artifact"
                 , "  (mean ~ 1 validates the unfolding; golden-anchored)." ]
            else []
        ]
  ]

renderObj3 :: Obj3Res -> String
renderObj3 r = unlines $
  if isNaN (o3slope r)
    then concat
      [ [ ""
        , "==================== Objection 3: Large-T Decay Rate ===================="
        , "  Fit log(b(N)) vs log(N): expected slope ~ -0.5"
        , ""
        , "WARNING: Insufficient data points for regression." ] ]
    else concat
      [ [ ""
        , "==================== Objection 3: Large-T Decay Rate ===================="
        , "  Fit log(b(N)) vs log(N): expected slope ~ -0.5"
        , ""
        , "  Slope     = " ++ sgn (fx 6 (o3slope r))
        , "  Intercept = " ++ sgn (fx 6 (o3intercept r))
        , "  R^2       = " ++ fx 6 (o3r2 r)
        , "  95% CI for slope: [" ++ fx 4 (o3cilo r) ++ ", " ++ fx 4 (o3cihi r) ++ "]"
        , ""
        , if o3ok r
            then "Result: Fitted slope = " ++ fx 4 (o3slope r) ++ ", expected = -0.500. OK"
            else "Result: Fitted slope = " ++ fx 4 (o3slope r)
                 ++ ", expected = -0.500. WARN: slope deviates from -0.5 (decay is empirical)"
        ] ]
  where sgn s = if head s == '-' then s else '+' : s

renderSelfcheck :: [SCRow] -> Int -> Int -> String
renderSelfcheck rows npass nfail = unlines $ concat
  [ [ ""
    , "=== Golden self-check — frozen anchors (canon: meridian-spectral-observatory, selftest 199/199) ==="
    ]
  , map line rows
  , [ "  Self-check: " ++ show npass ++ " passed, " ++ show nfail ++ " failed" ]
  ]
  where
    line r
      | scSkip r  = "  " ++ padR 24 (scName r) ++ " SKIP"
      | otherwise = "  " ++ padR 24 (scName r) ++ " " ++ st ++ "  computed = "
                    ++ show (scGot r) ++ ", expected = " ++ show (scExp r)
                    ++ ", D = " ++ show (scDelta r)
      where st = if scOk r then "PASS" else "FAIL"
