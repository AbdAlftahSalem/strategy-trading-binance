import requests

import const


# https://api.telegram.org/bot5593961098:AAEfdla6P5VI18EElqhVtr9o_GxR5TsMyLI/sendMessage?chat_id=-1001573769581&text=hello
def sentToTelegram(msg):
    sendMessage = 'https://api.telegram.org/bot' + const.token + '/sendMessage?chat_id=' + const.chatId1 + '&text=' + msg
    requests.get(sendMessage)

    sendMessage = 'https://api.telegram.org/bot' + const.token + '/sendMessage?chat_id=' + const.chatId2 + '&text=' + msg
    requests.get(sendMessage)

