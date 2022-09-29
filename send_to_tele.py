import requests

import const


def sentToTelegram(msg):
    sendMessage = 'https://api.telegram.org/bot' + const.token + '/sendMessage?chat_id=' + const.chatId1 + '&text=' + msg
    requests.get(sendMessage)

    sendMessage = 'https://api.telegram.org/bot' + const.token + '/sendMessage?chat_id=' + const.chatId2 + '&text=' + msg
    requests.get(sendMessage)
