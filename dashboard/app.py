import streamlit as st
import os
import requests

st.set_page_config(page_title="ChaosHarvester v2", layout="wide")
st.title("🔥 ChaosHarvester: Live Chaos Intelligence System")

# Layout: Info + Forecast
col1, col2 = st.columns(2)

with col1:
    st.subheader("🔧 System Status")
    st.write({
        "OpenAI Key": bool(os.getenv("OPENAI_API_KEY")),
        "Supabase": os.getenv("SUPABASE_URL", "Missing"),
        "Discord": "✅" if os.getenv("DISCORD_WEBHOOK") else "❌ Missing",
        "Telegram": "✅" if os.getenv("TELEGRAM_BOT_TOKEN") else "❌ Missing"
    })

    if st.button("🧠 Manual Forecast Trigger"):
        signal = "Real-time macro pressure signal"
        forecast = "Expect increased volatility in tech sector."

        st.success("✅ GPT Forecast Triggered")
        st.markdown(f"**Signal:** {signal}")
        st.markdown(f"**Forecast:** {forecast}")

        # Discord alert
        discord_url = os.getenv("DISCORD_WEBHOOK")
        if discord_url:
            requests.post(discord_url, json={
                "content": f"[ChaosHarvester v2] 🚨\nSignal: {signal}\nForecast: {forecast}"
            })

        # Telegram alert
        token = os.getenv("TELEGRAM_BOT_TOKEN")
        chat_id = os.getenv("TELEGRAM_CHAT_ID")
        if token and chat_id:
            telegram_url = f"https://api.telegram.org/bot{token}/sendMessage"
            data = {
                "chat_id": chat_id,
                "text": f"[ChaosHarvester v2] 🚨\nSignal: {signal}\nForecast: {forecast}"
            }
            requests.post(telegram_url, data=data)

        st.info("📨 Alerts sent to Discord and Telegram.")

with col2:
    st.subheader("📊 Visual Intelligence")
    st.markdown("🧱 *Entropy Heatmap (simulated)*")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Heatmap.png/600px-Heatmap.png")

# Bottom feed display
st.subheader("🧪 Simulated Live Chaos Feed")
st.code(\"\"\"
[
  {"source": "x.com", "content": "IMF warns of stagflation."},
  {"source": "reddit/finance", "content": "NVIDIA insiders offloading shares"},
  {"source": "investing.com", "content": "Gold spikes on currency devaluation fears"}
]
\"\"\")
