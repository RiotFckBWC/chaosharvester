
import streamlit as st
import requests
import os

st.set_page_config(page_title="ChaosHarvester Dashboard", layout="wide")
st.title("📡 ChaosHarvester Intelligence Panel")

# Show current config (for testing purposes only)
st.subheader("Environment Configuration")
st.write({
    "OpenAI Key Exists": bool(os.getenv("OPENAI_API_KEY")),
    "Supabase URL": os.getenv("SUPABASE_URL", "Not Found"),
    "Discord Webhook": "Loaded" if os.getenv("DISCORD_WEBHOOK") else "Missing",
    "Telegram Setup": "Ready" if os.getenv("TELEGRAM_BOT_TOKEN") and os.getenv("TELEGRAM_CHAT_ID") else "Missing"
})

# Simulated chaos forecast trigger
if st.button("🧠 Trigger Forecast"):
    st.success("Forecasting initiated... (simulated)")
    st.markdown("**Signal:** Macro instability detected via multi-source entropy scan.")
    st.markdown("**Forecast:** High probability of rate hike. Recommend defensive positioning.")
    st.info("Check Discord/Telegram for alert and Supabase for log.")
