# python-dev-intern-projects
Python Developer Internship Projects

Each branch in this repository is a project/task and hence not meant to be merged.

## Stock Analysis Dashboard ##

## How Streamlit works - check file slit.py ##
1. This is used for rapid creation and sharing of custom web applications, particularly for data science and machine learning projects. It allows users to transform Python scripts into interactive web apps with minimal effort, eliminating the need for extensive web development knowledge.
2. pip install streamlit
3. Execute - streamlit run slit.py
   - It will open the Streamlit application in web browser.
   - It will ask for email for the first time. Leave it blank.
   - You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501                                                                                                                  
  Network URL: http://192.168.225.137:8501

## What is Stock Ticker? ##
Stock symbols are a shorthand way of describing a company's stock on an exchange. They're also referred to as ticker symbols.
    Apple Inc. (AAPL)
    Alphabet Inc. (GOOGL)
    Microsoft Corporation (MSFT)
    Amazon.com, Inc. (AMZN)
    Meta (formerly Facebook) Inc. (META)
    Tesla Motors (TSLA)
    The Goldman Sachs Group, Inc. (GS)
    The Dow Jones Industrial Average (DJIA)
    The S&P 500 Index (SPX)
    The NASDAQ Composite Index (COMP)

## To retrieve historical stock data from Yahoo Finance ##
1. Check file yfin.py
2. pip install yfinance pandas ta
3. 2 Methods - download function and ticker object with history method

## Calculations ##

# Simple Moving Average (SMA):
Definition:
The SMA is the average of a given set of prices over a specific number of periods.
SMA = (Sum of Closing Prices over N periods) / N
    Where 'N' is the number of periods (e.g., 10 days, 20 days).

# Exponential Moving Average (EMA):
Definition:
The EMA gives more weight to recent prices, making it more responsive to new information than the SMA.
Formula:

    First, calculate the SMA for the chosen period (this is the initial EMA value).
    Then, use the following formula for subsequent EMAs:
        EMA = (Price - Previous EMA) * (2 / (N + 1)) + Previous EMA
            Where 'N' is the number of periods.
            'Price' is the current closing price.
            'Previous EMA' is the EMA calculated for the previous period. 

Example:
For a 10-day EMA, you would first calculate the 10-day SMA. Then, on the 11th day, you would use the SMA as the 'Previous EMA' in the formula to calculate the 10-day EMA for that day.

# Relative Strength Index (RSI):
Definition:
RSI is a momentum oscillator that measures the magnitude of recent price changes to evaluate overbought or oversold conditions in the price of a stock or other asset.
Formula:
    RSI = 100 - (100 / (1 + (Average Gain / Average Loss)))
        To calculate RSI, you first need to calculate the average gain and average loss over a specific period (usually 14 periods).
        Average Gain = (Sum of Gains over N periods) / N
        Average Loss = (Sum of Losses over N periods) / N
        Gain: If the current period's price is higher than the previous period's price, the gain is the difference. Otherwise, the gain is 0.
        Loss: If the current period's price is lower than the previous period's price, the loss is the absolute value of the difference. Otherwise, the loss is 0. 
Example:
    To calculate a 14-day RSI, you would first calculate the average gain and average loss over the past 14 periods. Then, plug those values into the RSI formula.

In Summary:

    SMA is a simple average of past prices.
    EMA gives more weight to recent prices, making it more responsive. 

    RSI measures momentum and identifies overbought/oversold conditions.

These indicators are often used together by traders to identify potential buy and sell signals.
The ta library simplifies the calculation of more complex indicators like RSI.

## Extras ##
>>> pip install numpy
>>> pip install ta-lib
>>> pip install pandas_ta
ImportError: cannot import name 'NaN' from 'numpy' due to pandas_ta -  compatibility issue between your pandas_ta version and your numpy version
pip install --upgrade pandas-ta - upgrade
pip install numpy<2.0 - downgrade
pip install numpy==1.26.3

RSI - manually calculated

Now Plot candlestick and line graphs.
>>> pip install plotly

A KeyError: 'date' in
If 'date' is intended to be a regular column but is currently the index, use df.reset_index(inplace=True) to convert the index into a column.

Display performance summary
Strategy Logic: A buy signal might be triggered when the 50-day EMA crosses above the 100-day SMA, indicating an upward trend, and the 14-period RSI is above 30, suggesting the asset is not oversold. A sell signal might be generated when the 50-day EMA crosses below the 100-day SMA and the RSI is below 70. Stop loss and take profit conditions are implemented to manage risk

Now, create the figure with three subplots:

    Candlestick chart with SMA and EMA
    RSI indicator
    Buy/Sell signals

Streamlit reruns the entire script from top to bottom every time a user interacts with a widget.

Steps to Share on Streamlit Community Cloud:

    Host your code on GitHub: Make sure your Streamlit app and its dependencies (listed in a requirements.txt file) are in a GitHub repository.
    Sign up for Streamlit Community Cloud: Go to the Streamlit website and sign up or log in using your GitHub account.
    Create a New App: In your Streamlit Cloud dashboard, click "New App," select your GitHub repository and branch, and click "Deploy".
    Share the URL: Once deployed, Streamlit will provide a URL that you can share with others.

## Deliverables ## 
Check folder deliverables
Check your installed library version with >>> pip show yfinance