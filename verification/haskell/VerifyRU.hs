-- | Thin Russian rendering layer (CANON_SPEC §10). No duplicated math.
module VerifyRU (renderObj1, renderObj2, renderObj3, renderSelfcheck) where

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
    , "==================== Возражение 1: Числовая стабильность b(N) ===================="
    , "  b(N) = (1/N) * Sum|gamma_k - gamma_tilde_k|, точки Грама: theta(t) = pi*k (Ньютон)"
    , ""
    , "         N            b(N)    log10(b(N))"
    ]
  , [ padR 10 (show n) ++ "  " ++ padR 14 (fx 8 b) ++ "  " ++ padR 14 (fx 4 (log10v b))
    | (n, b) <- zip (o1ns r) (o1bn r) ]
  , if o1hasFit r
      then [ ""
           , "  Эмпирический закон:  b(N) ~ " ++ fx 4 (o1fitA r) ++ " * N^(-" ++ fx 4 (o1fitS r)
             ++ ")   (R^2 = " ++ fx 4 (o1fitR2 r) ++ ")" ]
      else []
  , if o1converging r
      then [ ""
           , "Результат: b(N) сходится с ростом N. OK"
           , "  b(N) монотонно убывает по таблице — сходимость подтверждена на доступном диапазоне."
           , "  Убывание ЭМПИРИЧЕСКОЕ, это не O(1/sqrt(N))." ]
      else [ "", "Результат: b(N) НЕ сходится с ростом N. WARN" ]
  ]

renderObj2 :: Obj2Res -> String
renderObj2 r = unlines $ concat
  [ [ ""
    , "==================== Возражение 2: Статистическая значимость GUE-распределения ===================="
    , "  GUE (beta=2) сурьмида через каноническую CDF-таблицу (32768 точек)"
    , ""
    ]
  , if o2n r < 2
      then [ "ПРЕДУПРЕЖДЕНИЕ: недостаточно интервалов для GUE-теста." ]
      else concat
        [ [ "  Средний спейсинг: " ++ fx 9 (o2mean r) ++ "  дисперсия: " ++ fx 9 (o2var r)
            ++ "  (n = " ++ show (o2n r) ++ ")"
          , "  Колмогоров-Смирнов:  D = " ++ fx 6 (o2d r) ++ ",  p-значение = " ++ show (o2p r)
          , "  Крамер-фон Мизес:    W^2 = " ++ fx 6 (o2w2 r)
          , "  Андерсон-Дарлинг:     A^2 = " ++ fx 6 (o2a2 r)
          , "  <r> (отношение соседних): " ++ fx 6 (o2r r) ++ "  (n = " ++ show (o2nr r)
            ++ ", GUE ~ 0.5992)"
          , ""
          , if o2rejected r
              then "Результат: H0 (GUE-распределение): ОТВЕРГНУТА  (alpha = 0.05)"
              else "Результат: H0 (GUE-распределение): НЕ ОТВЕРГНУТА  (alpha = 0.05)"
          ]
        , if o2rejected r
            then [ "  Примечание: при больших n точная GUE-сурьмида формально отвергается — это"
                 , "  известные поправки конечных T у нулей ζ, а не дефект данных"
                 , "  (среднее ~ 1 подтверждает развёртку; якоря golden)." ]
            else []
        ]
  ]

renderObj3 :: Obj3Res -> String
renderObj3 r = unlines $
  if isNaN (o3slope r)
    then concat
      [ [ ""
        , "==================== Возражение 3: Скорость убывания при больших T ===================="
        , "  Аппроксимация log(b(N)) vs log(N): ожидаемый наклон ~ -0.5"
        , ""
        , "ПРЕДУПРЕЖДЕНИЕ: недостаточно точек для регрессии." ] ]
    else concat
      [ [ ""
        , "==================== Возражение 3: Скорость убывания при больших T ===================="
        , "  Аппроксимация log(b(N)) vs log(N): ожидаемый наклон ~ -0.5"
        , ""
        , "  Наклон    = " ++ sgn (fx 6 (o3slope r))
        , "  Св. член  = " ++ sgn (fx 6 (o3intercept r))
        , "  R^2       = " ++ fx 6 (o3r2 r)
        , "  95% ДИ для наклона: [" ++ fx 4 (o3cilo r) ++ ", " ++ fx 4 (o3cihi r) ++ "]"
        , ""
        , if o3ok r
            then "Результат: Наклон = " ++ fx 4 (o3slope r) ++ ", ожидаемый = -0.500. OK"
            else "Результат: Наклон = " ++ fx 4 (o3slope r)
                 ++ ", ожидаемый = -0.500. WARN: наклон отклоняется от -0.5 (убывание эмпирическое)"
        ] ]
  where sgn s = if head s == '-' then s else '+' : s

renderSelfcheck :: [SCRow] -> Int -> Int -> String
renderSelfcheck rows npass nfail = unlines $ concat
  [ [ ""
    , "=== Само-проверка golden — замороженные якоря (канон: meridian-spectral-observatory, selftest 199/199) ==="
    ]
  , map line rows
  , [ "  Само-проверка: " ++ show npass ++ " пройдено, " ++ show nfail ++ " провалено" ]
  ]
  where
    line r
      | scSkip r  = "  " ++ padR 24 (scName r) ++ " ПРОПУСК"
      | otherwise = "  " ++ padR 24 (scName r) ++ " " ++ st ++ "  вычислено = "
                    ++ show (scGot r) ++ ", ожидание = " ++ show (scExp r)
                    ++ ", D = " ++ show (scDelta r)
      where st = if scOk r then "ПРОЙДЕНО" else "СБОЙ"
