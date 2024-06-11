import os
import glob
import asyncio
from pyrogram import Client
from itertools import cycle
import re

# Конфигурация
API_ID = 123 #не трогай
API_HASH = 'fvdad'#это тоже
PROXY_TYPE = "http"  # "socks4", "socks5" and "http" are supported
WORKDIR = "sessions/" #pyrogram .sessions путь
PROXIES_FILE = 'bot/config/proxies.txt' #proxy путь
DELAY_BETWEEN_TASKS = 3  # Задержка между задачами в секундах

def get_session_names():
    session_names = glob.glob(f'{WORKDIR}/*.session')
    session_names = [os.path.splitext(os.path.basename(file))[0] for file in session_names]
    return session_names

def get_proxies():
    with open(PROXIES_FILE, encoding='utf-8-sig') as file:
        proxies = [line.strip() for line in file]
    return proxies

async def get_tg_clients():
    session_names = get_session_names()
    if not session_names:
        raise FileNotFoundError("Не найдено файлов сессий")

    tg_clients = [
        Client(
            name=session_name,
            api_id=API_ID,
            api_hash=API_HASH,
            workdir=WORKDIR
        ) for session_name in session_names
    ]
    return tg_clients

def parse_referral_link(link):
    pattern = r"https://t\.me/(?P<bot_username>[\w_]+)\?start=(?P<referral_code>[\w_]+)"
    match = re.match(pattern, link)
    if match:
        return match.group("bot_username"), match.group("referral_code")
    else:
        raise ValueError("Неверный формат реферальной ссылки. Ожидается формат: https://t.me/имябота?start=реферальный_код")

async def join_bot_with_session(tg_client, proxy, bot_username, referral_code):
    if proxy:
        proxy_dict = {
            "scheme": PROXY_TYPE,
            "hostname": proxy.split(":")[1].split("@")[1],
            "port": int(proxy.split(":")[2]),
            "username": proxy.split(":")[0],
            "password": proxy.split(":")[1].split("@")[0]
        }
        tg_client.proxy = proxy_dict

    await tg_client.start()
    try:
        # Отправка реферальной команды боту
        await tg_client.send_message(bot_username, f"/start {referral_code}")
        print(f"Аккаунт {tg_client.name} авторизован в боте {bot_username}.")
        await asyncio.sleep(3)  # Ждем 3 секунды
    except Exception as e:
        print(f"Ошибка при обработке сессии {tg_client.name}: {e}")
    finally:
        await tg_client.stop()

async def run_tasks(tg_clients, use_proxies, proxies, bot_username, referral_code):
    proxies_cycle = cycle(proxies) if proxies else None
    for tg_client in tg_clients:
        proxy = next(proxies_cycle) if use_proxies and proxies_cycle else None
        await join_bot_with_session(tg_client, proxy, bot_username, referral_code)
        await asyncio.sleep(DELAY_BETWEEN_TASKS)  # Ждем между задачами

async def main():
    referral_link = input("Введите вашу реферальную ссылку: ")
    bot_username, referral_code = parse_referral_link(referral_link)

    use_proxies = input("Использовать прокси? (y/n): ").strip().lower() == 'y'
    
    tg_clients = await get_tg_clients()
    proxies = get_proxies() if use_proxies else []
    await run_tasks(tg_clients, use_proxies, proxies, bot_username, referral_code)

if __name__ == "__main__":
    asyncio.run(main())
