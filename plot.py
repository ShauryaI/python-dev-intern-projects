import plotly.graph_objects as go
import pandas as pd

# Sample data (replace with your actual data)
data = pd.DataFrame({
    'Date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05']),
    'Open': [100, 102, 105, 103, 106],
    'High': [103, 106, 107, 105, 108],
    'Low': [99, 101, 103, 102, 104],
    'Close': [102, 105, 104, 106, 107]
})

# Example for a line graph (e.g., a Simple Moving Average)
data['SMA_5'] = data['Close'].rolling(window=2).mean()

fig = go.Figure(data=[go.Candlestick(x=data['Date'],
                                     open=data['Open'],
                                     high=data['High'],
                                     low=data['Low'],
                                     close=data['Close'],
                                     name='Candlestick'),
                      go.Scatter(x=data['Date'], y=data['SMA_5'], mode='lines', name='5-Period SMA',
                                 line=dict(color='blue'))])

fig.update_layout(title='Candlestick Chart with SMA',
                  xaxis_title='Date',
                  yaxis_title='Price',
                  xaxis_rangeslider_visible=False)  # Hide range slider if not needed

fig.show()