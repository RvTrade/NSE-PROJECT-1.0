import streamlit as st
from stocks import get_top_stocks, get_stock_predictions
from options import get_options_signal
from analysis import get_technical_indicators, get_fundamentals
from news import fetch_market_news
from telegram_alerts import send_telegram_alert

st.set_page_config(page_title="Ultimate NSE Cockpit", layout="wide", page_icon="💹")
st.title("Ultimate NSE Cockpit - AI & ML Powered Stock Dashboard")

# Dark mode styling
st.markdown("""
<style>
body {
background-color: #0E1117;
color: #FFFFFF;
}
</style>
""", unsafe_allow_html=True)

tabs = st.tabs(["Top Stocks", "Predictions", "Options", "Technical & Fundamentals", "News", "Alerts"])

# ---------------------- Top Stocks ----------------------
with tabs[0]:
st.header("Top 50 NSE Stocks Today")
top_stocks = get_top_stocks()
st.dataframe(top_stocks)

# ---------------------- Predictions ----------------------
with tabs[1]:
st.header("Stock Predictions")
stock_symbol = st.selectbox("Select Stock", top_stocks['Symbol'])
predictions = get_stock_predictions(stock_symbol)
st.line_chart(predictions)

# ---------------------- Options ----------------------
with tabs[2]:
st.header("Options Strategies & Signals")
stock_symbol_opt = st.selectbox("Select Stock for Options", top_stocks['Symbol'])
option_signal = get_options_signal(stock_symbol_opt)
st.write(option_signal)

# ---------------------- Technical & Fundamentals ----------------------
with tabs[3]:
st.header("Technical Indicators & Fundamentals")
tech_indicators = get_technical_indicators(stock_symbol)
fundamentals = get_fundamentals(stock_symbol)
st.write(tech_indicators)
st.write(fundamentals)

# ---------------------- News ----------------------
with tabs[4]:
st.header("Latest Market News")
news = fetch_market_news()
for n in news:
st.write(f"**{n['title']}** - {n['link']}")

# ---------------------- Telegram Alerts ----------------------
with tabs[5]:
st.header("Send Telegram Alerts")
msg = st.text_input("Enter message to send to Telegram")
if st.button("Send Alert"):
send_telegram_alert(msg)
st.success("Message sent successfully!")