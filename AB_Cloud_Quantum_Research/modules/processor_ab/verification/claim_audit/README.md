# verification/claim_audit — аудит утверждений (схема V14)

Каждый claim-файл содержит: statement / premises / code / controls /
does_not_prove / status + числовые согласования (путь в вердикте →
значение → допуск). Аудит: `python3 -c "import sys; sys.path.insert(0,'.'); from rpbridge import audit; print(audit.run())"`.

| Claim | Статус |
|---|---|
| claim_v20.json — компилятор AB-процессора (P0) | committed, аудит PASS |
