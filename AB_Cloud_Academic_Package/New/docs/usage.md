# Usage in five commands

```bash
./06_code/cli/run.sh --lang=ru --theme=neon analyze   # the guided tour
python3 06_code/python/run.py doctor                   # environment check
python3 06_code/python/run.py --output=json analyze    # clean JSON contract
python3 -m pytest 09_tests/python -q                   # integrity suite
bash reproduce.sh                                     # one-button reproduction
```

Every runner speaks the same contract
([`06_code/shared/contract.json`](../06_code/shared/contract.json)):
identical flags, identical metrics, identical JSON.
