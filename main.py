import boost
import send_to_tele
import stratgy
import tickers

tickerString = ""
tickers = tickers.getTicker(150)
for i in range(len(tickers)):
    boost.boost(stratgy.strategy, tickers[i], "1h", 100)
for i in stratgy.tickerList:
    tickerString += "❇" + i["ticker"] + "\n\n   🟢High: " + str(i["high"]) + "\n   🔴Low: " + str(
        i["low"]) + "\n\n\n"
send_to_tele.sentToTelegram(f'⏰⏰System will search in⏰⏰:\n\n{tickerString}')
# stratgy.strategy("BTCUSDT", "4h", 100)
