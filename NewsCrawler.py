# -*- coding: utf-8 -*-
#import datetime #https://stackoverflow.com/questions/50639415/attributeerror-module-datetime-has-no-attribute-now 這個用起來有點問題，換下面的
from datetime import datetime, date
from PyWeb import HtmlClient, WebDriverClient
from NewsInfo import NewsInfo


class LTNNewsClient(HtmlClient):

    def __init__(self):
        super().__init__()
        self.__url_pattern = 'https://news.ltn.com.tw/topic/%E6%AF%94%E7%89%B9%E5%B9%A3/${PAGE}'
        self.__news_since = None # news_since
        self.__news_until = None # news_until

        self.__now_url = None
        self.__now_page = 1
        self.__pub_datetime_formats = ['%Y/%m/%d %H:%M', '%Y/%m/%d']

    def findByMaxPages(self, max_pages=10):
        news_info_list = []
        while self.__now_page <= max_pages:
            part_news_info_list = self.__miningOnePage()
            news_info_list.extend(part_news_info_list)
        return news_info_list

    def findBySinceDate(self, since_date = date.today()):
        news_info_list = []
        since_datetime = datetime.combine(since_date, datetime.min.time())
        while True:
            # start1 = datetime.now()
            part_news_info_list = self.__miningOnePage()
            # end1 = datetime.now()
            # print("cost1 = ", (end1 - start1))

            # start2 = datetime.now()
            filtered_part_news_info_list = [news_info for news_info in part_news_info_list if news_info.getPubDateTime() >= since_datetime]
            # end2 = datetime.now()
            # print("cost2 = ", (end2 - start2))

            # start3 = datetime.now()
            news_info_list.extend(filtered_part_news_info_list)
            # end3 = datetime.now()
            # print("cost3 = ", (end3 - start3))


            if len(filtered_part_news_info_list) != len(part_news_info_list):
                break;
        return news_info_list

    def findByInterval(self):
        pass


    def _doSetupNowUrl(self):
        self.__now_url = self.__url_pattern.replace('${PAGE}', str(self.__now_page) )
        #print(self._now_url)
        self.__now_page += 1

    def __miningOnePage(self):
        part_news_info_list = []

        # start1_1 = datetime.now()
        self._doSetupNowUrl()
        html_parsed_data = self.getHtml(self.__now_url)
        # end1_1 = datetime.now()
        # print("cost1_1 = ", (end1_1 - start1_1))

        # data-desc='新聞列表' > class='searchlist' > li
        # start1_2 = datetime.now()
        news_element_list = html_parsed_data.find(class_='searchlist').findAll('li') #新聞(標題)清單
        for news_element in news_element_list:
            news_info = NewsInfo()
            tag_link_element = news_element.find("a", class_="immtag")
            pub_datetime_element = news_element.findNext('span')
            str_pub_datetime = pub_datetime_element.getText()
            #news_info.setPubDateTime(datetime.strptime(str_pub_datetime, self._pub_datetime_format))
            news_info.setPubDateTime(self.__obtainPubDateTime(str_pub_datetime))

            title_link_element = news_element.find("a", class_="tit")
            news_info.setLink(title_link_element['href']) #新聞連結
            news_info.setTitle(title_link_element.find('h3').getText()) #新聞標題

            part_news_info_list.append(news_info)
        end1_2 = datetime.now()
        # print("cost1_2 = ", (end1_2 - start1_2))
        return part_news_info_list

    def __obtainPubDateTime(self, str_pub_datetime):
        for pub_datetime_format in self.__pub_datetime_formats:
            try:
                return datetime.strptime(str_pub_datetime, pub_datetime_format)
            except ValueError:
                pass # Do Nothing

        return None

class YahooNewsClient(WebDriverClient):

    def __init__(self, url='https://tw.news.yahoo.com/tag/比特幣'):
        super().__init__()
        self.__url = url

    def getNewsInfoList(self, new_amount):
        news_info_list = []
        while self.__now_page <= self.__max_pages:
            news_info_list = self._miningOnePage(news_info_list)
        return news_info_list


    #def _doMiningOnePage(self):
    def __miningOnePage(self, news_info_list):
        start1_1 = datetime.now()
        self.__doSetupNowUrl()
        html_parsed_data = self.getHtml(self.__now_url)
        end1_1 = datetime.now()
        print("cost1_1 = ", (end1_1 - start1_1))

        # data-desc='新聞列表' > class='searchlist' > li
        start1_2 = datetime.now()
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
        end1_2 = datetime.now()
        print("cost1_2 = ", (end1_2 - start1_2))

        return news_info_list


# --------------------------------- 以下是 自由時報格式 ---------------------------------
ltn_client = LTNNewsClient()

#ltn_news_list = ltn_client.findByMaxPages()
since_date = date.fromisoformat('2021-01-01')
ltn_news_list = ltn_client.findBySinceDate(since_date)

#print(ltn_news_list)
for ltn_news in ltn_news_list:
    print(ltn_news)
print("total nums = ", len(ltn_news_list))

# --------------------------------- 以上是 自由時報格式 ---------------------------------
