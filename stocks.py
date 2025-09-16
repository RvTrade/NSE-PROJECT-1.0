import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta


def get_top_stocks():
    # Example: Top 50 NSE stocks (can replace with real NSE scraping/API)
    top_symbols = ['RELIANCE.NS', 'TCS.NS', 'HDFCBANK.NS', 'INFY.NS', 'ICICIBANK.NS']
    data = []
    for sym in top_symbols:
        stock = yf.Ticker(sym)
        price = stock.history(period='1d')['Close'][-1]
        data.append({'Symbol': sym, 'Price': price})
    return pd.DataFrame(data)


def get_stock_predictions(symbol):
    # Example: dummy ML predictions for 1-90 days
    import numpy as np
    today = datetime.today()
    dates = [today + timedelta(days=i) for i in range(1, 91)]
    prices = np.linspace(100, 150, 90) # Replace with ML model output
    return pd.DataFrame({'Date': dates, 'Predicted Price': prices}).set_index('Date')