import yfinance as yf
import pandas as pd

# Using the download function
data = yf.download("AAPL", start="2024-01-01", end="2024-12-31")
print(data.head())

# Using the Ticker object
ticker = yf.Ticker("AAPL")
data_ticker = ticker.history(period="1y")
print(data_ticker.head())

# Let's continue with data
# Calculate 20-day SMA
data['SMA_20'] = data['Close'].rolling(window=20).mean()

# Calculate 20-day EMA
data['EMA_20'] = data['Close'].ewm(span=20, adjust=False).mean()

# Calculate 14-period RSI
# Calculate price changes
delta = data['Close'].diff()

# Calculate gains and losses
gain = delta.where(delta > 0, 0)
loss = -delta.where(delta < 0, 0)

# Calculate average gains and losses
avg_gain = gain.ewm(com=13, adjust=False).mean()
avg_loss = loss.ewm(com=13, adjust=False).mean()

# Calculate Relative Strength (RS)
rs = avg_gain / avg_loss

# Calculate RSI
data['RSI'] = 100 - (100 / (1 + rs))

print(data[['Close', 'SMA_20', 'EMA_20', 'RSI']].tail())
