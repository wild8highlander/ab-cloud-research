-- | CLI dispatcher for the AB-Cloud Verification Suite (Haskell).
-- The numeric kernel lives in ZerosLoader.hs; VerifyEN/VerifyRU are thin
-- rendering layers (CANON_SPEC §10).
module Main (main) where

import System.Environment (getArgs)
import System.Exit (exitWith, ExitCode(..))
import ZerosLoader ( loadZeros, selfcheck
                   , runObjection1, runObjection2, runObjection3 )
import qualified VerifyEN
import qualified VerifyRU

data Config = Config
  { cfgZeros     :: Int
  , cfgSource    :: String
  , cfgObjection :: String
  , cfgLang      :: String
  , cfgDataDir   :: String
  , cfgSelfcheck :: Bool
  }

defaultConfig :: Config
defaultConfig = Config 50000 "auto" "all" "en" "../data" True

parseArgs :: [String] -> Config -> Config
parseArgs [] cfg = cfg
parseArgs args cfg = case args of
  ("--zeros" : n : rest)      -> parseArgs rest cfg { cfgZeros = readOrDefault n (cfgZeros cfg) }
  ("--source" : s : rest)     -> parseArgs rest cfg { cfgSource = s }
  ("--objection" : o : rest)  -> parseArgs rest cfg { cfgObjection = o }
  ("--lang" : l : rest)       -> parseArgs rest cfg { cfgLang = l }
  ("--data-dir" : d : rest)   -> parseArgs rest cfg { cfgDataDir = d }
  ("--no-selfcheck" : rest)   -> parseArgs rest cfg { cfgSelfcheck = False }
  (_ : rest)                  -> parseArgs rest cfg

readOrDefault :: String -> Int -> Int
readOrDefault s d = case reads s of
  [(v, "")] -> v
  _         -> d

main :: IO ()
main = do
  args <- getArgs
  let cfg = parseArgs args defaultConfig

  putStrLn ""
  if cfgLang cfg == "ru"
    then putStrLn "  ╔═══════════════════════════════════════════════╗"
    else putStrLn "  ╔═══════════════════════════════════════════════╗"
  putStrLn "  ║        AB-Cloud Verification Suite  (Haskell) ║"
  putStrLn "  ╚═══════════════════════════════════════════════╝"
  putStrLn ""
  putStrLn ("  Config: zeros=" ++ show (cfgZeros cfg) ++ "  source=" ++ cfgSource cfg
            ++ "  objection=" ++ cfgObjection cfg ++ "  lang=" ++ cfgLang cfg)
  putStrLn ""

  zeros <- loadZeros (cfgDataDir cfg) (cfgZeros cfg) (cfgSource cfg)
  putStrLn ("  Loaded " ++ show (length zeros) ++ " zeros.")
  putStrLn ""

  let lang = cfgLang cfg == "ru"

  scFail <- if cfgSelfcheck cfg
    then do
      let (rows, npass, nfail) = selfcheck zeros
      putStr (if lang then VerifyRU.renderSelfcheck rows npass nfail
                      else VerifyEN.renderSelfcheck rows npass nfail)
      return nfail
    else return (-1)

  let run1 = putStr (if lang then VerifyRU.renderObj1 (runObjection1 zeros)
                             else VerifyEN.renderObj1 (runObjection1 zeros))
      run2 = putStr (if lang then VerifyRU.renderObj2 (runObjection2 zeros)
                             else VerifyEN.renderObj2 (runObjection2 zeros))
      run3 = putStr (if lang then VerifyRU.renderObj3 (runObjection3 zeros)
                             else VerifyEN.renderObj3 (runObjection3 zeros))

  case cfgObjection cfg of
    "1"   -> run1
    "2"   -> run2
    "3"   -> run3
    "all" -> run1 >> run2 >> run3
    other -> do
      putStrLn ("Unknown objection: " ++ other ++ " (use 1, 2, 3, or all)")
      exitWith (ExitFailure 2)

  putStrLn ""
  putStrLn "  AB-Cloud Verification Suite — complete."
  putStrLn ""

  if scFail > 0 then exitWith (ExitFailure 1) else return ()
