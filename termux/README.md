# Termux Push Kit — Publish This Repository from an Android Phone

One-command publication of this repository to GitHub straight from Termux
on Android. The script does everything: installs missing packages,
relocates the repo out of shared storage, offers two login modes, pushes
`main` + tags, verifies the remote SHA, and opens the repository in your
browser. The token exists in process memory only — nothing is written to
disk or to `.git/config`.

## Files

| File | Purpose |
|---|---|
| `install_and_push.sh` | the all-in-one push script (Termux first, works on Linux/macOS too) |
| `README.md` | this English quick guide |
| `README_RU.md` | the full step-by-step Russian instruction (installing Termux, creating a PAT, troubleshooting) |
| `../HOW_TO_PUSH_FROM_ANDROID.md` | one-page cheat sheet in the repo root |

## TL;DR (after Termux is installed)

```bash
pkg update -y && pkg install -y git curl unzip
termux-setup-storage
unzip ~/storage/downloads/ab-cloud-research-v1.2.0.zip -d ~/repo-ab-cloud
cd ~/repo-ab-cloud
bash termux/install_and_push.sh
```

The script then asks:

1. **Repository URL** — press Enter (your repo is pre-filled);
2. **Login mode**:
   - `1` — **PAT token**: enter the username (Enter = `wild8highlander`)
     and paste the token (input hidden; the token is verified via the
     GitHub API *before* any push, including the push-permission check);
   - `2` — **browser login**: the script installs GitHub CLI, shows a
     one-time code (`XXXX-XXXX`) and opens `https://github.com/login/device`
     — type the code in the browser, authorize, done. No token needed at all;
3. If the histories diverge, it asks to update `main` with
   `--force-with-lease` (default Y);
4. At the end it offers to open the repository in the browser.

## What the script automates

- installs `git`, `curl`, `gh` on demand (`pkg install`);
- takes a Termux wake-lock so Android cannot kill the push;
- if the repository sits under `/sdcard` or `/storage`, copies it into
  Termux home (`~/repo-ab-cloud`) where git works reliably;
- commits pending changes if any appear;
- configures `origin`, fetches, compares histories, chooses fast-forward
  or lease-protected force push;
- pushes `main` + all tags, then verifies via `ls-remote` that GitHub
  holds exactly your commit;
- opens `https://github.com/<owner>/<repo>/tree/main` on request.

Safety: the token is passed to git through an **in-memory credential
helper** (`git -c credential.helper=…`) — it is never stored, never echoed,
and cleared on exit. `DRY_RUN=1 bash termux/install_and_push.sh` rehearses
every step without touching anything.

## Create a PAT (mode 1)

<https://github.com/settings/tokens> → *Generate new token (classic)* →
scope **repo**; or a fine-grained token with **Contents: Read and write**
on this repository. The full illustrated walkthrough and a troubleshooting
table (401/403, non-fast-forward, disk space, mirrors) live in
[`README_RU.md`](README_RU.md), §7 and §9.

## Кратко (по-русски)

- Комплект для публикации репозитория с телефона: скрипт сам ставит
  пакеты, переносит репозиторий из /sdcard в память Termux, делает push
  main + тегов и открывает репозиторий в браузере.
- Два способа входа: PAT-токен (скрытый ввод, проверка через API до
  отправки) или браузерный одноразовый код GitHub CLI — токен не нужен.
- Токен живёт только в памяти процесса; есть безопасный `DRY_RUN=1`.
- Полная инструкция по-русски — `README_RU.md`.
