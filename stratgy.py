import get_data

tickerList = []


def strategy(ticker, frameWork, limit):
    try:
        df = get_data.getFromBinance(ticker, frameWork, limit)
        getHighestVolume(df, ticker, frameWork)
    except:
        pass


def getHighestVolume(df, ticker, frameWork):
    global bestCandle, secCandle
    maxValues = df["volume"].nlargest(10)
    length = 0
    for i in maxValues:
        index = getIndex(df, "volume", i)
        if index > 3:
            currentCandle = df.iloc[index]
            if not checkRedCandle(currentCandle):
                preCandle = df.iloc[index - 1]
                prePreCandle = df.iloc[index - 2]
                if length < 2:
                    if preCandle["volume"] * 2 < currentCandle["volume"] and prePreCandle["volume"] * 2 < currentCandle[
                        "volume"]:

                        newDf = df[index:]
                        minClose = min(newDf["close"])
                        maxClose = max(newDf["close"])

                        if minClose < df.iloc[index - 1]["close"]:
                            break

                        elif maxClose < df.iloc[index - 1]["close"]:
                            break


                        else:
                            length += 1
                            if length == 1:
                                bestCandle = currentCandle
                            else:
                                secCandle = currentCandle
                                data = {"ticker": ticker, "frameWork": frameWork,
                                        "DCA1": {"high": bestCandle["high"],
                                                 "low": bestCandle["low"],
                                                 "close": bestCandle["close"],
                                                 "open": bestCandle["open"],
                                                 "volume": bestCandle["volume"],
                                                 "date": bestCandle["date"]},
                                        "DCA2": {"high": secCandle["high"],
                                                 "low": secCandle["low"],
                                                 "close": secCandle["close"],
                                                 "open": secCandle["open"],
                                                 "volume": secCandle["volume"],
                                                 "date": secCandle["date"]}}
                                print(ticker)
                                print(data["DCA1"])
                                print(data["DCA2"])
                                print(f'Mid High {(data["DCA1"]["high"] + data["DCA2"]["high"]) / 2}')
                                print(f'Mid low {(data["DCA1"]["low"] + data["DCA2"]["low"]) / 2}')
                                print("---------------------------------------------------")
                                tickerList.append(data)
                                break


def getIndex(df, title, value):
    return next(iter(df[df[title] == value].index), 'no match')


def checkRedCandle(candle):
    if candle['open'] > candle["close"]:
        return True
    else:
        return False
