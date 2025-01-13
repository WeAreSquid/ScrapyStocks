import mplfinance as mpf
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


df1 = yf.download("FTS", start='2023-01-13', end='2024-01-13')
print(df1.head())
df1.columns = ["Close", "High", "Low", "Open", "Volume"]

df2 = yf.download("IDA", start='2023-01-13', end='2024-01-13')
df2.columns = ["Close", "High", "Low", "Open", "Volume"]

mpf.plot(df1, type='candle',style='yahoo',volume=True, block=False)
mpf.plot(df2, type='candle',style='yahoo',volume=True, block=False)
plt.show()
