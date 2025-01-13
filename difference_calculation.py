import mplfinance as mpf
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import pandas_ta as ta

df = yf.download(["FTS", "IDA"], start='2020-01-13', end='2022-01-13')
df = df.reset_index()

df['Date'] = df['Date', '']
df["Diff Close"] = df["Close","FTS"] - df["Close", "IDA"]* 0.4024281131217958
df["Diff High"] = df["High","FTS"] - df["High", "IDA"] * 0.4024281131217958
df["Diff Low"] = df["Low","FTS"] - df["Low", "IDA"] * 0.4024281131217958
df["Diff Open"] = df["Open","FTS"] - df["Open", "IDA"] * 0.4024281131217958
df["Diff Volume"] = df["Volume","FTS"] - df["Volume", "IDA"] *0.4024281131217958

new_df = df[["Date", "Diff Close", "Diff High", "Diff Low", "Diff Open", "Diff Volume"]]
new_df.columns = ["Date", "Close", "High", "Low", "Open", "Volume"]
print(new_df.head())

#mpf.plot(new_df, type='candle',style='yahoo',volume=True, block=False)
#plt.show()

ta_df = new_df.ta.bbands(close="Close", length=20, std=2).fillna(0)

final_df = pd.concat([new_df, ta_df], axis=1)

# Plot the Close prices and Bollinger Bands
plt.figure(figsize=(12, 6))
plt.plot(final_df["Date"], final_df["Close"], label="Close Price", color="blue")
plt.plot(final_df["Date"], final_df["BBU_20_2.0"], label="Upper Band", linestyle="--", color="green")
plt.plot(final_df["Date"], final_df["BBM_20_2.0"], label="Middle Band", linestyle="--", color="orange")
plt.plot(final_df["Date"], final_df["BBL_20_2.0"], label="Lower Band", linestyle="--", color="red")

plt.title("Bollinger Bands and Stock Prices")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid()
plt.show()

#################### IMPORTANT#################3
#SHORTING THE FIRST, LONGIND THE SECOND, UP IN THE BAND
# OUT ALWAYS UN THE AVERAGE OF THE BAND
#LONG THE FIRST, SHORT THE SECOND, DOWN IN THE BAND, STOP LOSS GRANDES PARA ABAJO = NO ME QUIERO IR!


