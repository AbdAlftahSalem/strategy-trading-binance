import boost
import send_to_tele
import stratgy
import tickers

tickerString = ""
tickers = tickers.getTicker(150)
localList = [{"1hFrameWork": []}, {"4hFrameWork": []}, {"1dFrameWork": []}]
frames = ["1h", "4h", "1d"]
for i in range(len(tickers)):
    for j in range(len(frames)):
        boost.boost(stratgy.strategy, tickers[i], frames[j], 100)
        localList[j][f'{frames[j]}FrameWork'] = stratgy.tickerList
        stratgy.tickerList = []

for i in range(len(localList)):
    data = localList[i][f'{frames[i]}FrameWork']
    for j in data:
        tickerString += "\n\n" + "❇" + j["ticker"] + "\n✳Frame : " + j["frameWork"] + "\n\n   🟢High: " + str(
            j["DCA1"]["high"]) + "\n   🔴Low: " + str(
            j["DCA1"]["low"]) + "\n\n   🟢High: " + str(j["DCA2"]["high"]) + "\n   🔴Low: " + str(
            j["DCA2"]["low"])
send_to_tele.sentToTelegram(f'⏰⏰System will search in⏰⏰:\n\n{tickerString}')
