# -*- coding: utf-8 -*-
#import datetime #https://stackoverflow.com/questions/50639415/attributeerror-module-datetime-has-no-attribute-now 這個用起來有點問題，換下面的
from datetime import datetime
from PyWeb import HtmlClient, WebDriverClient
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
        self._pub_datetime_formats = ['%Y/%m/%d %H:%M', '%Y/%m/%d']

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
        news_element_list = html_parsed_data.find(class_='searchlist').findAll('li') #新聞(標題)清單
        for news_element in news_element_list:
            news_info = NewsInfo()
            """
            links = news.findAll('a')
            #print(links)

            #print(links[1].href).setTitle()),
            news_info.setLink(links[1]['href']) #新聞連結
            news_info.setTitle(links[1].find('h3').getText()) #新聞標題
            # print(news_info)
            """
            tag_link_element = news_element.find("a", class_="immtag")
            pub_datetime_element = news_element.findNext('span')
            str_pub_datetime = pub_datetime_element.getText()
            #news_info.setPubDateTime(datetime.strptime(str_pub_datetime, self._pub_datetime_format))
            news_info.setPubDateTime(self._obtainPubDateTime(str_pub_datetime))

            title_link_element = news_element.find("a", class_="tit")
            news_info.setLink(title_link_element['href']) #新聞連結
            news_info.setTitle(title_link_element.find('h3').getText()) #新聞標題

            news_info_list.append(news_info)
        return news_info_list

    def _obtainPubDateTime(self, str_pub_datetime):
        for pub_datetime_format in self._pub_datetime_formats:
            try:
                return datetime.strptime(str_pub_datetime, pub_datetime_format)
            except ValueError:
                pass # Do Nothing

        return None

class YahooNewsClient(WebDriverClient):

    def __init__(self, url='https://tw.news.yahoo.com/tag/比特幣'):
        super().__init__()
        self._url = url

    def getNewsInfoList(self, new_amount):
        news_info_list = []
        while self._now_page <= self._max_pages:
            #self._miningOnePage(news_info_list)
            news_info_list = self._miningOnePage(news_info_list)
        return news_info_list


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
