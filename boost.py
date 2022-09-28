import threading


def boost(callback, tickers, interval, depth):
    try:
        thread_list = []
        for i in range(len(tickers)):
            th = threading.Thread(target=callback, args=(tickers[i], interval, depth))
            thread_list.append(th)
            th.start()

        for thrd in thread_list:
            thrd.join()

    except:
        pass
