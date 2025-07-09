import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import io
import base64

def get_last_year_finance_data(ticker_symbol):
    ticker = yf.Ticker(ticker_symbol)
    data_ticker = ticker.history(period="1y")
    return data_ticker

def calculate_stock_indicator(stock_data):
    # Calculate 20-day, 50-day and 100-day SMA
    stock_data['SMA_20'] = stock_data['Close'].rolling(window=20).mean()
    stock_data['SMA_50'] = stock_data['Close'].rolling(window=50).mean()
    stock_data['SMA_100'] = stock_data['Close'].rolling(window=100).mean()

    # Calculate 20-day and 50-day EMA
    stock_data['EMA_20'] = stock_data['Close'].ewm(span=20, adjust=False).mean()
    stock_data['EMA_50'] = stock_data['Close'].ewm(span=50, adjust=False).mean()

    # Calculate 14-period RSI
    # Calculate price changes
    delta = stock_data['Close'].diff()

    # Calculate gains and losses
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    # Calculate average gains and losses
    avg_gain = gain.ewm(com=13, adjust=False).mean()
    avg_loss = loss.ewm(com=13, adjust=False).mean()

    # Calculate Relative Strength (RS)
    rs = avg_gain / avg_loss

    # Calculate RSI
    stock_data['RSI'] = 100 - (100 / (1 + rs))

    # Generate buy and sell signals
    stock_data['Buy_Signal'] = (stock_data['EMA_50'] > stock_data['SMA_100']) & (stock_data['RSI'] < 30)
    stock_data['Sell_Signal'] = (stock_data['EMA_50'] < stock_data['SMA_100']) | (stock_data['RSI'] > 70)

    return stock_data

def plot(stock_data, ticker_symbol, chart_identifier):
    # Create subplots
    fig = make_subplots(rows=3, cols=1, shared_xaxes=True,
                        vertical_spacing=0.01, row_width=[0.2, 0.2, 0.8])

    # Add candlestick chart to the first subplot
    fig.add_trace(go.Candlestick(x=stock_data.index,
                                 open=stock_data['Open'],
                                 high=stock_data['High'],
                                 low=stock_data['Low'],
                                 close=stock_data['Close'],
                                 name='Candlesticks'), row=1, col=1)

    # Add SMA lines
    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['SMA_20'], line=dict(color='blue', width=1), name='SMA 20'), row=1, col=1)

    # Add EMA lines
    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['EMA_20'], line=dict(color='green', width=1), name='EMA 20'), row=1,
                  col=1)

    # Add RSI to the second subplot
    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['RSI'], line=dict(color='red', width=1), name='RSI'),
                  row=2, col=1)
    # Add overbought and oversold lines for RSI
    fig.add_hline(y=70, line_dash='dash', line_color='red', line_width=1, row=2, col=1)
    fig.add_hline(y=30, line_dash='dash', line_color='green', line_width=1, row=2, col=1)

    # Add buy signals as markers on the candlestick chart
    fig.add_trace(go.Scatter(
        x=stock_data.index,
        y=stock_data['Buy_Signal'],
        mode='markers',
        marker=dict(
            color='green',
            symbol='triangle-up',
            size=10,
            line=dict(width=1, color='DarkSlateGrey')
        ),
        name='Buy Signal'
    ), row=3, col=1)

    # Add sell signals as markers on the candlestick chart
    fig.add_trace(go.Scatter(
        x=stock_data.index,
        y=stock_data['Sell_Signal'],
        mode='markers',
        marker=dict(
            color='red',
            symbol='triangle-down',
            size=10,
            line=dict(width=1, color='DarkSlateGrey')
        ),
        name='Sell Signal'
    ), row=3, col=1)

    # Update layout
    fig.update_layout(title=f"{ticker_symbol} Candlestick Chart with SMAs, EMAs, and RSI",

                      xaxis_rangeslider_visible=False)
    fig.update_yaxes(title_text='Price', row=1, col=1)
    fig.update_yaxes(title_text='RSI', row=2, col=1)
    fig.update_yaxes(title_text='Signals', row=3, col=1)
    #fig.show()
    st.plotly_chart(fig, use_container_width=True, key=f"stock_chart_{chart_identifier}")

def create_download_link(stock_data, filename="stock_data.csv"):
    csv_file = io.StringIO()  # Create an in-memory text buffer
    stock_data.to_csv(csv_file, index=False)  # Save DataFrame to buffer as CSV
    csv_file.seek(0) # Reset buffer's cursor
    csv_string = csv_file.read()  # Read buffer content as string
    # Encode string for download
    b64 = base64.b64encode(csv_string.encode()).decode()
    # Create a download link (HTML)
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}">Download as CSV</a>'
    return href

# Streamlit app
st.set_page_config(layout="wide", page_title="Stock Analysis Dashboard")  # Use wide layout for better visualization

with st.sidebar:
    st.title("Stock Ticker")
    stock_ticker = st.selectbox("Select an option:", ["AAPL", "GOOGL", "MSFT", "AMZN", "META", "TSLA", "GS", "DJIA", "SPX", "COMP"])
    generate_button = st.button("Generate Dashboard")
    export_button = st.button("Export Data to CSV")

with st.container():
    st.header("Stock Analysis Dashboard")

if generate_button:
    with st.container():
        data = get_last_year_finance_data(stock_ticker)
        updated_data = calculate_stock_indicator(data)
        updated_data.dropna(inplace=True)
        # updated_data.reset_index(inplace=True) for using x=stock_data['Date'] else use x=stock_data.index
        plot(updated_data, stock_ticker, 1)

if export_button:
    with st.container():
        data = get_last_year_finance_data(stock_ticker)
        updated_data = calculate_stock_indicator(data)
        updated_data.dropna(inplace=True)
        updated_data.reset_index(inplace=True)
        download_link = create_download_link(updated_data)
        st.markdown(download_link, unsafe_allow_html=True)
        st.write(updated_data)
        #st.success("Data successfully loaded!")