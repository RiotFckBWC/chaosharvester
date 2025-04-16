
import streamlit as st
import os

st.set_page_config(page_title="ChaosHarvester v2", layout="wide")
st.title("🔥 ChaosHarvester: Live Chaos Intelligence System")

col1, col2 = st.columns(2)

with col1:
    st.subheader("System Status")
    st.write({
        "OpenAI Key": bool(os.getenv("OPENAI_API_KEY")),
        "Supabase": os.getenv("SUPABASE_URL", "Missing"),
        "Discord": "Ready" if os.getenv("DISCORD_WEBHOOK") else "Missing",
        "Telegram": "Ready" if os.getenv("TELEGRAM_BOT_TOKEN") else "Missing"
    })
    if st.button("🧠 Manual Forecast Trigger"):
        st.success("Triggered GPT Forecast (live hook ready)")
        st.markdown("**Signal:** Real-time macro pressure signal")
        st.markdown("**Forecast:** Expect increased volatility in tech sector.")

with col2:
    st.subheader("📊 Visual Intelligence")
    st.markdown("🧱 *Entropy Heatmap*")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Heatmap.png/600px-Heatmap.png")

st.subheader("🧪 Live Feed Simulation")
st.code("""
[
  {"source": "x.com", "content": "IMF warns of stagflation."},
  {"source": "reddit/finance", "content": "NVIDIA insiders offloading shares"},
  {"source": "investing.com", "content": "Gold spikes on currency devaluation fears"}
]
""")
