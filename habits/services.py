import requests

from config.settings import TELEGRAM_URL, TELEGRAM_TOKEN


def  send_telegram_message(tg_chat_id, message):
    """Отправка сообщения в телеграм."""

    params = {
        "text": message,
        "chat_id": tg_chat_id,
    }
    requests.get(f"{TELEGRAM_URL}{TELEGRAM_TOKEN}/sendMessage", params=params)
