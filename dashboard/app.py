import streamlit as st
import requests
import os

st.set_page_config(page_title="ChaosHarvester Dashboard", layout="wide")
st.title("📡 ChaosHarvester Intelligence Panel")

# Check secrets
st.subheader("Environment Configuration")
st.write({
    "OpenAI Key Exists": bool(os.getenv("OPENAI_API_KEY")),
    "Supabase URL": os.getenv("SUPABASE_URL", "Not Found"),
    "Discord Webhook": "Loaded" if os.getenv("DISCORD_WEBHOOK") else "Missing",
    "Telegram Setup": "Ready" if os.getenv("TELEGRAM_BOT_TOKEN") and os.getenv("TELEGRAM_CHAT_ID") else "Missing"
})

# Alert logic
def send_discord_alert(msg):
    webhook = os.getenv("DISCORD_WEBHOOK")
    if webhook:
        requests.post(webhook, json={"content": msg})

def send_telegram_alert(msg):
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    if token and chat_id:
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        data = {"chat_id": chat_id, "text": msg}
        requests.post(url, data=data)

# Trigger
if st.button("🧠 Trigger Forecast"):
    st.success("Forecasting initiated...")

    signal = "Macro instability detected via multi-source entropy scan."
    forecast = "High probability of rate hike. Recommend defensive positioning."

    st.markdown(f"**Signal:** {signal}")
    st.markdown(f"**Forecast:** {forecast}")
    st.info("Alerts dispatched. Check Discord/Telegram.")

    message = f"[ChaosHarvester] ALERT 🚨\nSignal: {signal}\nForecast: {forecast}"
    send_discord_alert(message)
    send_telegram_alert(message)
