import random

def fetch_live_signals():
    # Simulated chaos signals
    signals = [
        {"source": "investing.com", "content": "Central bank warns of stagflation", "type": "macro"},
        {"source": "reddit/finance", "content": "Retail traders rush into leverage ETFs", "type": "retail"},
        {"source": "x.com", "content": "AI stock bubble incoming?", "type": "tech"},
        {"source": "rss/bloomberg", "content": "Gold surges on geopolitical tensions", "type": "commodities"}
    ]
    return random.sample(signals, 2)