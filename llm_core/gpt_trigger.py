import os
import openai

def gpt_forecast(signal):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    prompt = f"Analyze this market signal and forecast risk: {signal}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content