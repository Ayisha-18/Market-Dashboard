import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

# Dashboard title
st.title("📈 Global Markets Analytics Dashboard")

st.write("Analyze real stock market data using Python")

# Stock selection
stock_symbol = st.selectbox(
    "Choose a stock:",
    ["JPM", "AAPL", "MSFT", "TSLA", "NVDA"]
)

# Download stock data
stock = yf.Ticker(stock_symbol)

data = stock.history(period="1mo")
data["Moving Average"] = data["Close"].rolling(window=5).mean()

# Latest price
latest_price = data["Close"].iloc[-1]

previous_price = data["Close"].iloc[-2]

daily_change = ((latest_price - previous_price) / previous_price) * 100

month_high = data["High"].max()

month_low = data["Low"].min()

volume = data["Volume"].iloc[-1]


col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Current Price",
        f"${latest_price:.2f}"
    )

with col2:
    st.metric(
        "Daily Change",
        f"{daily_change:.2f}%"
    )

with col3:
    st.metric(
        "Month High",
        f"${month_high:.2f}"
    )

with col4:
    st.metric(
        "Month Low",
        f"${month_low:.2f}"
    )

# Chart
st.subheader("📊 Closing Price - Last Month")

fig, ax = plt.subplots()

ax.plot(
    data.index,
    data["Close"],
    label="Closing Price"
)

ax.plot(
    data.index,
    data["Moving Average"],
    label="5-Day Moving Average"
)

ax.legend()

ax.set_xlabel("Date")
ax.set_ylabel("Price ($)")

st.pyplot(fig)