import yfinance as yf
import matplotlib.pyplot as plt

stocks = ["JPM", "AAPL", "MSFT"]

for symbol in stocks:
    data = yf.Ticker(symbol).history(period="1mo")
    plt.plot(data.index, data["Close"], label=symbol)

plt.title("Stock Prices - Last Month")
plt.xlabel("Date")
plt.ylabel("Closing Price ($)")
plt.legend()

plt.show()
