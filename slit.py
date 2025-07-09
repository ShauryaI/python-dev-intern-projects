import streamlit as st

# Streamlit app
st.set_page_config(layout="wide")  # Use wide layout for better visualization

with st.sidebar:
    st.title("Stock Ticker")
    stock_ticker = st.selectbox("Select an option:", ["AAPL", "GOOGL", "MSFT", "AMZN", "META", "TSLA", "GS", "DJIA", "SPX", "COMP"])
    generate_button = st.button("Generate Dashboard")

col1, col2 = st.columns(2)

with col1:
    st.title("Stock Analysis Dashboard")

with col2:
    if generate_button:
        pass