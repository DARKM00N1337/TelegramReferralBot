# TelegramReferralBot

[English version](ENREADME.md)

TelegramReferralBot - это Python-скрипт, который автоматизирует процесс присоединения к Telegram-боту по реферальным ссылкам с использованием нескольких аккаунтов. Скрипт поддерживает использование прокси и позволяет настроить задержку между действиями аккаунтов.

## Возможности

- Присоединение к Telegram-ботам по реферальным ссылкам.
- Поддержка нескольких сессий.
- Опциональное использование прокси для дополнительной безопасности и анонимности.
- Настраиваемая задержка между действиями аккаунтов для избежания пометки как спам.

## Требования

- Python 3.6 или выше
- Библиотека `pyrogram`
- Библиотека `tgcrypto`

## Установка

1. Клонируйте репозиторий:

    ```sh
    git clone https://github.com/DARKM00N1337/TelegramReferralBot.git
    cd TelegramReferralBot
    ```

2. Установите необходимые библиотеки Python:

    ```sh
    pip install -r requirements.txt
    ```

3. Поместите файлы сессий в директорию `sessions`.

4. (Опционально) Если вы используете прокси, поместите список прокси в файл `proxies.txt`.

## Использование

1. Запустите скрипт:

    ```sh
    python3 telegram_referral_bot.py
    ```

2. Введите вашу реферальную ссылку при появлении запроса.

3. Выберите, использовать ли прокси, введя "y" или "n".

## Пример

```sh
$ python3 telegram_referral_bot.py
Введите вашу реферальную ссылку: https://t.me/Govnobot?start=referral_146728
Использовать прокси? (y/n): y
