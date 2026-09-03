# Быстрый push с Android (Termux) — шпаргалка

Полная версия инструкции: **`termux/README_RU.md`**.

## Кратко: 5 шагов

1. **Установите Termux** — из F-Droid: <https://f-droid.org/packages/com.termux/>
   (не из Google Play!). Альтернатива: <https://github.com/termux/termux-app/releases>
2. **Настройте Termux** (первый запуск):

   ```bash
   pkg update -y && pkg install -y git curl unzip
   termux-setup-storage
   ```

   На запрос доступа к файлам — «Разрешить».

3. **Распакуйте архив** в домашнюю папку Termux (не в /sdcard):

   ```bash
   unzip ~/storage/downloads/ab-cloud-research-v1.1.0.zip -d ~/repo-ab-cloud
   ```

4. **Запустите скрипт**:

   ```bash
   cd ~/repo-ab-cloud
   bash termux/install_and_push.sh
   ```

5. **Ответьте на вопросы**:
   - URL репозитория — просто Enter (уже вписан ваш);
   - способ входа:
     - `1` = PAT-токен (создать: <https://github.com/settings/tokens>,
       classic с областью `repo`, либо fine-grained с
       Contents: Read and write);
     - `2` = вход через браузер: скрипт покажет одноразовый код и откроет
       `https://github.com/login/device` — введите код, подтвердите доступ.
   - в конце разрешите открыть репозиторий в браузере и убедитесь,
   что последний коммит обновился.

## Что делает скрипт

Сам ставит git/curl/gh, переносит репозиторий из /sdcard в память Termux,
делает push ветки `main` + тегов, сверяет SHA на GitHub. Токен существует
только в памяти процесса и нигде не сохраняется.

## Частые проблемы

- **401** — токен неверный/истёк → создайте новый.
- **403 / нет права записи** — для classic отметьте `repo`; для fine-grained —
  Contents: Read and write на этот репозиторий.
- **non-fast-forward** — скрипт сам предложит обновление с
  `--force-with-lease`; ответьте Y, чтобы содержимое архива заменило
  ветку `main` на GitHub.
- **Нет места** — нужно ~3 ГБ свободных.
- **pkg ругается** — `termux-change-repo`, смените зеркало.
