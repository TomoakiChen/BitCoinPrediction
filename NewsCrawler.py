# -*- coding: utf-8 -*-
#import datetime
from datetime import datetime
from PyWeb import HtmlClient
from NewsInfo import NewsInfo


class LTNClient(HtmlClient):

    def __init__(self, news_since=datetime.now().date(), news_until=datetime.now().date(), max_pages=10):
        super().__init__()
        self._url_pattern = 'https://news.ltn.com.tw/topic/%E6%AF%94%E7%89%B9%E5%B9%A3/${PAGE}'
        self._news_since = news_since
        self._news_until = news_until

        self._now_url = None
        self._now_page = 1
        self._max_pages = max_pages

    def getNewsInfoList(self):
        news_info_list = []
        while self._now_page <= self._max_pages:
            #self._miningOnePage(news_info_list)
            news_info_list = self._miningOnePage(news_info_list)
        return news_info_list

    def _doSetupNowUrl(self):
        self._now_url = self._url_pattern.replace('${PAGE}', str(self._now_page) )
        #print(self._now_url)
        self._now_page += 1

    #def _doMiningOnePage(self):
    def _miningOnePage(self, news_info_list):
        self._doSetupNowUrl()
        html_parsed_data = self.getHtml(self._now_url)

        # data-desc='新聞列表' > class='searchlist' > li
        news_list = html_parsed_data.find(class_='searchlist').findAll('li') #新聞(標題)清單
        for news in news_list:
            news_info = NewsInfo()
            links = news.findAll('a')
            #print(links)

            #print(links[1].href).setTitle())
            news_info.setLink(links[1]['href']) #新聞連結
            news_info.setTitle(links[1].find('h3').getText()) #新聞標題
            # print(news_info)

            news_info_list.append(news_info)
        return news_info_list

# --------------------------------- 以下是 自由時報格式 ---------------------------------
ltn_client = LTNClient()

ltn_news_list = ltn_client.getNewsInfoList()
print(len(ltn_news_list))

for ltn_news in ltn_news_list:
    print(ltn_news)

# --------------------------------- 以上是 自由時報格式 ---------------------------------
