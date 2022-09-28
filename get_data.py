import ccxt
import pandas as pd


def getFromBinance(ticker, interval, limit):
    try:
        exchange = ccxt.binance()
        exchange.enableRateLimit = True
        bars = exchange.fetch_ohlcv(ticker, timeframe=interval, limit=limit)
        df = pd.DataFrame(
            bars, columns=['date', 'open', 'high', 'low', 'close', 'volume'])
        df['date'] = pd.to_datetime(df["date"], unit='ms')

        return df

    except:
        print("Error binance  ", ticker)
