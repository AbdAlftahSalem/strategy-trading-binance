import requests

binanceTickerAPI = "https://api1.binance.com/api/v1/ticker/allPrices"
highRankTickerAPI = "https://api.coinstats.app/public/v1/coins?skip=0&limit="
allBinanceTickers = []


def highRankTicker(rank):
    x = requests.get(f'{highRankTickerAPI}{rank}')
    return x.json()["coins"]


def binanceTicker():
    x = requests.get(binanceTickerAPI)
    x = x.json()
    for i in x:
        if i["symbol"].endswith("USDT"):
            allBinanceTickers.append(i["symbol"])

    return allBinanceTickers


def getTicker(limit):
    binanceTickers = binanceTicker()
    highRankTickers = highRankTicker(100)
    allTicker = []
    length = 0
    newTicker = []
    localTicker = []
    for i in highRankTickers:
        ticker = i["symbol"] + "USDT"
        if ticker in binanceTickers:
            allTicker.append(ticker)
    for i in range(len(allTicker)):
        if length < 10:
            localTicker.append(allTicker[i])
        if length == 10:
            newTicker.append(localTicker)
            localTicker = []
            length = 0
        length += 1
    return newTicker
