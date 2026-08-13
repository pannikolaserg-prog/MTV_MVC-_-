import requests
from django.conf import settings

def send_telegram_message(chat_id, text):
    token = settings.TELEGRAM_BOT_TOKEN
    if not token:
        return False
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    try:
        requests.post(url, json={'chat_id': chat_id, 'text': text})
        return True
    except:
        return False
