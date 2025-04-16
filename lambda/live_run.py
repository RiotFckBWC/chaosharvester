from feeds.aggregator import fetch_live_signals
from llm_core.gpt_trigger import gpt_forecast
import requests
import os

def handler(event=None, context=None):
    chaos = fetch_live_signals()
    if not chaos:
        return "No signals"

    alerts = []
    for sig in chaos:
        if "warn" in sig['content'].lower() or "bubble" in sig['content'].lower():
            forecast = gpt_forecast(sig['content'])
            alerts.append((sig['content'], forecast))

    for msg, fc in alerts:
        discord = os.getenv("DISCORD_WEBHOOK")
        if discord:
            requests.post(discord, json={"content": f"⚠️ Chaos Detected:
{msg}
🧠 Forecast: {fc}"})

        token = os.getenv("TELEGRAM_BOT_TOKEN")
        chat = os.getenv("TELEGRAM_CHAT_ID")
        if token and chat:
            url = f"https://api.telegram.org/bot{token}/sendMessage"
            requests.post(url, data={"chat_id": chat, "text": f"⚠️ Chaos:
{msg}
🧠 {fc}"})
    return "Done"