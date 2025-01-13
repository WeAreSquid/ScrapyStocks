import mplfinance as mpf
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

df = yf.download(["FTS", "IDA"], start='2023-01-13', end='2024-01-13')

df["Ratio Close"] = df["Close","FTS"] / df["Close", "IDA"]
df["Ratio High"] = df["High","FTS"] / df["High", "IDA"]
df["Ratio Low"] = df["Low","FTS"] / df["Low", "IDA"]
df["Ratio Open"] = df["Open","FTS"] / df["Open", "IDA"]
df["Ratio Volume"] = df["Volume","FTS"] / df["Volume", "IDA"]
new_df = df[["Ratio Close", "Ratio High", "Ratio Low", "Ratio Open", "Ratio Volume"]]
new_df.columns = ["Close", "High", "Low", "Open", "Volume"]
print(new_df.head())

mpf.plot(new_df, type='candle',style='yahoo',volume=True, block=False)

average_ratio = new_df['Close'].mean()
print('Average Ratio:')
print(average_ratio)
#plt.show()



