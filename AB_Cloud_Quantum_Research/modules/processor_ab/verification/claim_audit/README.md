# verification/claim_audit — the claim audit (the V14 scheme)

Each claim file contains: statement / premises / code / controls /
does_not_prove / status + numerical cross-checks (a path in the verdict →
a value → a tolerance). Audit: `python3 -c "import sys; sys.path.insert(0,'.'); from rpbridge import audit; print(audit.run())"`.

| Claim | Status |
|---|---|
| claim_v20.json — the AB-processor compiler (P0) | committed, audit PASS |
