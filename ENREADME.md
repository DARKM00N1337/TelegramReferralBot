# TelegramReferralBot

[Русская версия](README.md)

TelegramReferralBot is a Python script that automates the process of joining a Telegram bot using referral links with multiple accounts. It supports the use of proxies and allows for customizable delays between account actions.

## Features

- Join Telegram bots using referral links.
- Support for multiple sessions.
- Optional use of proxies for added security and anonymity.
- Customizable delay between account actions to avoid being flagged as spam.

## Requirements

- Python 3.6 or higher
- `pyrogram` library
- `tgcrypto` library

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/TelegramReferralBot.git
    cd TelegramReferralBot
    ```

2. Install the required Python libraries:

    ```sh
    pip install -r requirements.txt
    ```

3. Place your session files in the `sessions` directory.

4. (Optional) If using proxies, place your proxy list in `proxies.txt`.

## Usage

1. Run the script:

    ```sh
    python3 telegram_referral_bot.py
    ```

2. Enter your referral link when prompted.

3. Choose whether to use proxies by typing "y" or "n".

## Example

```sh
$ python3 telegram_referral_bot.py
Введите вашу реферальную ссылку: https://t.me/gOVNOBOT?start=referral_102920
Использовать прокси? (y/n): y
