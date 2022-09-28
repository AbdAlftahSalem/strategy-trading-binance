import get_data

tickerList = []


def strategy(ticker, frame, limit):
    try:
        df = get_data.getFromBinance(ticker, frame, limit)
        getHighestVolume(df, ticker)
    except:
        pass


def getHighestVolume(df, ticker):
    maxValues = df["volume"].nlargest(10)
    for i in maxValues:
        index = getIndex(df, "volume", i)
        if index > 3:
            currentCandle = df.iloc[index]
            if not checkRedCandle(currentCandle):
                preCandle = df.iloc[index - 1]
                prePreCandle = df.iloc[index - 2]
                if preCandle["volume"] * 2 < currentCandle["volume"] and prePreCandle["volume"] * 2 < currentCandle[
                    "volume"]:
                    data = {"ticker": "BINANCE:" + ticker, "high": currentCandle["high"], "low": currentCandle["low"],
                            "close": currentCandle["close"], "open": currentCandle["open"],
                            "volume": currentCandle["volume"], "date": currentCandle["date"]}
                    tickerList.append(data)
                    print(data)
                    break


def getIndex(df, title, value):
    return next(iter(df[df[title] == value].index), 'no match')


def checkRedCandle(candle):
    if candle['open'] > candle["close"]:
        return True
    else:
        return False
