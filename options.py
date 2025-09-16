def get_options_signal(symbol):
    # Example options strategy
    return {
        "Stock": symbol,
        "Strategy": "Bull Call Spread",
        "Signal": "Buy",
        "Strike Prices": {"Call Buy": 5000, "Call Sell": 5100},
        "Expiry": "2025-09-30"
    }