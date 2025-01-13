import mplfinance as mpf
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import pandas_ta as ta

""" SUPONGAMOS QUE TENGO 8800 dolares en la cuente, estoy dispuesto a perder 2%, == 176 $
entonces:
HABLEMOS 1ero de estar abajo en la bollinger:
supongamos que toca la bollinger baja en -4 el par.
y ponemos stop loss the -10 (pq es suficientemente grande)
entonces estamos dispuestos a perder 6 dolares. entonces 176/6 me da para comprar
29.33 shares! de esta manera si me retiro con stop loss perdi 176 dolares que es a lo q estaba dispuesto a perder
SUP: dos dias despues, caigo en el take profit (el cual tiene q estar en la linea promedio el precio ahi es -1.5), en este punto me retiraria.
ACA estamos ganando 29.33*(-1.5 - -4) = 72 dolares! esto es el 1 porciento aprox de lo que tenia, y paso en dos dias!
"""