import yfinance as yf

# Define the stock ticker symbol (e.g., 'AAPL' for Apple)
tickers = ["FTS", "IDA"]

# Fetch historical data (e.g., last 3 months)

for tick in tickers:
    stock_data = yf.Ticker(tick)
    historical_data = stock_data.history(period="3mo")  # Available periods: '1d', '5d', '1mo', etc.

    # Calculate the average volume
    average_volume = historical_data['Volume'].mean()

    latest_data = stock_data.history(period="1d")
    latest_price = latest_data['Close'].iloc[-1]
    liquidity = average_volume*latest_price

    print(f"The liquidity for {tick} over the is: {liquidity}")
    
    # START WITH THE LESS LIQUIDITY