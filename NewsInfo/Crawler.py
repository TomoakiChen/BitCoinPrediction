# -*- coding: utf-8 -*-
# import datetime #https://stackoverflow.com/questions/50639415/attributeerror-module-datetime-has-no-attribute-now 這個用起來有點問題，換下面的

from NewsInfo.Client import *

class NewsCrawler:
    """
    __client_dic = {
      "LTN": LTNNewsClient(),
      "Yahoo": YahooNewsClient(headless=True),
      "cnYES": cnYESNewsClient(headless=True),
      "MoneyUdn": MoneyUdnNewsClient(headless=True),
      "Bitcoin.Com": BitCoinComNewsClient()
    }
    """
    # __client_dic = {
    #   "LTN": LTNNewsClient(),
    #   "Yahoo": YahooNewsClient(headless=True),
    #   "cnYES": cnYESNewsClient(headless=True),
    #   "MoneyUdn": MoneyUdnNewsClient(headless=True),
    #   "Bitcoin.com": BitCoinComNewsClient()
    # }
    __client_clazz_dict = {
        "LTN": LTNNewsClient,
        "Yahoo": YahooNewsClient,
        "cnYES": cnYESNewsClient,
        "MoneyUdn": MoneyUdnNewsClient,
        "Bitcoin.com": BitCoinComNewsClient
    }
    __client_dict = dict()

    """
    def __init__(self, news_sources=None):
        self.__client_list = []
        self.__setupClientList(news_sources)


    def __setupClientList(self, news_sources):
        if news_sources == None:
            news_sources = list(self.__client_dic.keys() )
        for news_code in news_sources:
            client = self.__client_dic.get(news_code)
            if client != None:
                self.__client_list.append(client)
            else:
                print("[Warning] Cannot found client by [" + news_code + "]")

    def findBySinceDate(self, since_date, close_after_iter = True):
        all_news_info_list = []
        for clientClazz in self.__client_list:
            client = clientClazz()
            news_info_list = client.findBySinceDate(since_date)
            all_news_info_list.extend(news_info_list)
            if close_after_iter == True:
                client.close()
        return all_news_info_list
    """

    def __init__(self, news_sources=None):
        self.__setupClientDict(news_sources)

    def __obtainClient(self, client_clazz):
        return client_clazz()

    def __setupClientDict(self, news_sources):
        if news_sources == None:
            news_sources = list(self.__client_clazz_dict.keys())

        for news_code in news_sources:
            client_clazz = self.__client_clazz_dict.get(news_code)

            if client_clazz != None:
                client = client_clazz()
                self.__client_dict[news_code] = client
            else:
                print("[Warning] Cannot found client_clazz by [" + news_code + "]")

    def getClientDict(self):
        return self.__client_dict

    def findByInterval(self, since_date, until_date, close_after_iter=True):
        all_news_info_list = []
        client_list = list(self.__client_dict.values())
        for client in client_list:
            news_info_list = client.findByInterval(since_date, until_date)
            all_news_info_list.extend(news_info_list)
            if close_after_iter == True:
                client.close()
        return all_news_info_list

    def findBySinceDate(self, since_date, close_after_iter=True):
        all_news_info_list = []
        client_list = list(self.__client_dict.values())
        for client in client_list:
            news_info_list = client.findBySinceDate(since_date)
            all_news_info_list.extend(news_info_list)
            if close_after_iter == True:
                client.close()
        return all_news_info_list

    def closeAll(self):
        client_list = list(self.__client_dict.values())
        for client in client_list:
            client.close()


class NewsCsvCrawler(NewsCrawler):

    def __init__(self, news_sources=None):
        super().__init__(news_sources)

    def save2Csv(self, since_date, days_freq=7):
        """
        news_info_list = list()
        now_since_date = date.today()
        the_timedelta = timedelta(days=days_freq)
        while True:
            # 可能要分類，利用 WebDriverClient (或該說，利用 refresh 機制的網站)，應該要最後直接下到最後一天?
            now_since_date = now_since_date - the_timedelta
            if now_since_date < since_date:
                now_since_date = since_date # 如果已經到希望的前面 since_date，則只讓他到這個 since_date

            part_news_info_list = self.findBySinceDate(now_since_date, close_after_iter = False)
            #這裡對於「url 指定 page num 」的可以變成繼續撈「尚未撈過的」，但對於那種頁面到底的反而還是不行


            if now_since_date == since_date:
                self.closeAll()
                break
        """
