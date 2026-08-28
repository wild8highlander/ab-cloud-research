module Main where

import System.Environment (getArgs)
import System.Exit (exitFailure)
import ZerosLoader (loadZeros)
import VerifyEN (objection1EN, objection2EN, objection3EN)
import VerifyRU (objection1RU, objection2RU, objection3RU)

data Config = Config
  { cfgZeros    :: Int
  , cfgSource   :: String
  , cfgObjection :: String
  , cfgLang     :: String
  }

defaultConfig :: Config
defaultConfig = Config
  { cfgZeros     = 10000
  , cfgSource    = "auto"
  , cfgObjection = "all"
  , cfgLang      = "en"
  }

-- | Parse CLI arguments into Config.
parseArgs :: [String] -> Config -> Config
parseArgs [] cfg = cfg
parseArgs ("--zeros":n:rest) cfg = case reads n of
  [(v, "")] -> parseArgs rest cfg { cfgZeros = v }
  _         -> parseArgs rest cfg
parseArgs ("--source":s:rest) cfg = parseArgs rest cfg { cfgSource = s }
parseArgs ("--objection":o:rest) cfg = parseArgs rest cfg { cfgObjection = o }
parseArgs ("--lang":l:rest) cfg = parseArgs rest cfg { cfgLang = l }
parseArgs (_:rest) cfg = parseArgs rest cfg

banner :: String
banner = unlines
  [ ""
  , "  ╔═══════════════════════════════════════════════════════╗"
  , "  ║        AB-Cloud Verification Suite  (Haskell)        ║"
  , "  ╚═══════════════════════════════════════════════════════╝"
  , ""
  ]

footer :: String
footer = unlines
  [ ""
  , "  ══════════════════════════════════════════════════════"
  , "  AB-Cloud Verification Suite — complete."
  , ""
  ]

main :: IO ()
main = do
  args <- getArgs
  let cfg = parseArgs args defaultConfig

  putStr banner
  putStrLn $ "  Config: zeros=" ++ show (cfgZeros cfg)
           ++ "  source=" ++ cfgSource cfg
           ++ "  objection=" ++ cfgObjection cfg
           ++ "  lang=" ++ cfgLang cfg
  putStrLn ""

  zeros <- loadZeros "../data" (cfgZeros cfg) (cfgSource cfg)
  putStrLn $ "  Loaded " ++ show (length zeros) ++ " zeros from source '"
           ++ cfgSource cfg ++ "'."
  putStrLn ""

  let runObj id_ = case cfgLang cfg of
        "ru" -> case id_ of
          1 -> putStr $ objection1RU zeros
          2 -> putStr $ objection2RU zeros
          3 -> putStr $ objection3RU zeros
          _ -> return ()
        _ -> case id_ of
          1 -> putStr $ objection1EN zeros
          2 -> putStr $ objection2EN zeros
          3 -> putStr $ objection3EN zeros
          _ -> return ()

  case cfgObjection cfg of
    "1"   -> runObj 1
    "2"   -> runObj 2
    "3"   -> runObj 3
    "all" -> mapM_ runObj [1, 2, 3]
    other -> do
      putStrLn $ "Unknown objection: " ++ other ++ " (use 1, 2, 3, or all)"
      exitFailure

  putStr footer
