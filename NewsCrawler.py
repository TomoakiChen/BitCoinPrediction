# -*- coding: utf-8 -*-
#import datetime #https://stackoverflow.com/questions/50639415/attributeerror-module-datetime-has-no-attribute-now 這個用起來有點問題，換下面的
from datetime import datetime, date, timedelta
from AkiPyDateTime import AkiDateTimeUtil
from PyWeb import HtmlClient, WebDriverClient
from NewsInfo import NewsInfo
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewsInfoHelper:
    @staticmethod
    def filterBySincaDate(ori_news_info_list, since_date):
        since_datetime = datetime.combine(since_date, datetime.min.time())
        filtered_news_info_list = [news_info for news_info in ori_news_info_list if news_info.getPubDateTime() != None and news_info.getPubDateTime().timestamp() >= since_datetime.timestamp()]
        return filtered_news_info_list

    @staticmethod
    def checkIsAfterSinceDate(news_info, since_date):
        pub_datetime = news_info.getPubDateTime()
        return AkiDateTimeUtil(pub_datetime, since_date)

    @staticmethod
    def checkIsBeforeEqUntilDate(news_info, since_date):
        pub_datetime = news_info.getPubDateTime()
        return AkiDateTimeUtil(pub_datetime, since_date)

class NewsCrawlerHelper:
    @staticmethod
    def needStopMining(news_info_list, filtered_news_info_list):
        return len(filtered_news_info_list) != len(news_info_list)

class LTNNewsClient(HtmlClient):

    def __init__(self):
        super().__init__()
        self.__url_pattern = 'https://news.ltn.com.tw/topic/%E6%AF%94%E7%89%B9%E5%B9%A3/${PAGE}'
        # self.__news_since = None # news_since
        self.__news_until = None # news_until

        self.__now_url = None
        self.__now_page = 1
        self.__pub_datetime_formats = ['%Y/%m/%d %H:%M', '%Y/%m/%d']

    def findByMaxPages(self, max_pages=10):
        # 如果 __init__ 沒有，下面嘗試設定，這樣不行
        self.__now_url = None
        self.__now_page = 1
        news_info_list = []
        while self.__now_page <= max_pages:
            part_news_info_list = self.__miningOnePage()
            news_info_list.extend(part_news_info_list)
        return news_info_list

    def findBySinceDate(self, since_date = date.today()):
        news_info_list = []
        # since_datetime = datetime.combine(since_date, datetime.min.time())
        while True:
            part_news_info_list = self.__miningOnePage()
            filtered_part_news_info_list = NewsInfoHelper.filterBySincaDate(part_news_info_list, since_date) # [news_info for news_info in part_news_info_list if news_info.getPubDateTime() >= since_datetime]
            news_info_list.extend(filtered_part_news_info_list)

            if len(filtered_part_news_info_list) != len(part_news_info_list):
                break;
        return news_info_list

    def findByInterval(self,):
        pass


    def __doSetupNowUrl(self):
        self.__now_url = self.__url_pattern.replace('${PAGE}', str(self.__now_page) )
        #print(self._now_url)
        self.__now_page += 1

    def __miningOnePage(self):
        part_news_info_list = []
        self.__doSetupNowUrl()
        html_parsed_data = self.getHtml(self.__now_url) #目前花時最多的

        # data-desc='新聞列表' > class='searchlist' > li
        news_element_list = html_parsed_data.find(class_='searchlist').findAll('li') #新聞(標題)清單
        for news_element in news_element_list:
            news_info = self.__obtainNewsInfo(news_element)
            part_news_info_list.append(news_info)
        return part_news_info_list

    def __obtainPubDateTime(self, str_pub_datetime):
        for pub_datetime_format in self.__pub_datetime_formats:
            try:
                return datetime.strptime(str_pub_datetime, pub_datetime_format)
            except ValueError:
                pass # Do Nothing
        return None

    def __obtainNewsInfo(self, news_element):
        news_info = NewsInfo()
        tag_link_element = news_element.find("a", class_="immtag")
        pub_datetime_element = news_element.findNext('span')
        str_pub_datetime = pub_datetime_element.getText()
        #news_info.setPubDateTime(datetime.strptime(str_pub_datetime, self._pub_datetime_format))
        news_info.setPubDateTime(self.__obtainPubDateTime(str_pub_datetime))

        title_link_element = news_element.find("a", class_="tit")
        news_info.setLink(title_link_element['href']) #新聞連結
        news_info.setTitle(title_link_element.find('h3').getText()) #新聞標題

        return news_info

class YahooNewsClient(WebDriverClient):

    def __init__(self, url='https://tw.news.yahoo.com/tag/比特幣', headless=True):
        super().__init__(headless=headless)
        self.__url = url

        self.__now_page = 0

    def findByMaxPages(self, max_pages=10):
        self.__doReadyLoadPage()
        news_info_list = []
        while self.__now_page <= max_pages:
            #news_info_list = self.__miningOnePage(news_info_list)
            news_info_list = self.__miningOnePage()
        return news_info_list

    def __doReadyLoadPage(self):
        self._browser_driver.get(self.__url)
        container_element = self._browser_driver.find_element(By.TAG_NAME, 'body')
        actions = webdriver.ActionChains(self._browser_driver)
        actions.click(container_element)
        actions.perform()

    def __miningOnePage(self):
        actions = webdriver.ActionChains(self._browser_driver)
        actions.key_down(Keys.END)
        actions.pause(5)
        # actions.perform()
        parsed_data = self.getHtml(self.__url, action_chains=actions)
        self.__now_page += 1

        news_info_list = []
        news_element_list = parsed_data.findAll(class_='StreamMegaItem')
        for news_element in news_element_list:
            news_info = self.__obtainNewsInfo(news_element)
            news_info_list.append(news_info)
        return news_info_list

    def __obtainNewsInfo(self, news_element):
        news_info = NewsInfo()
        link_element = news_element.find("a", class_="mega-item-header-link")
        link_url = link_element['href']
        text = link_element.getText() #此method會忽略掉 註解和tag

        news_info.setTitle(text)
        news_info.setLink(link_url)
        return news_info

class cnYESNewsClient(WebDriverClient):

    def __init__(self, url='https://www.cnyes.com/search/news?keyword=比特幣', headless=True):
        super().__init__(headless=headless)
        self.__url = url
        self.__now_page = 0

    def findByMaxPages(self, max_pages=10):
        self.__doReadyLoadPage()
        news_info_list = []
        while self.__now_page <= max_pages:
            #news_info_list = self.__miningOnePage(news_info_list)
            news_info_list = self.__miningOnePage()
        return news_info_list

    def findBySinceDate(self, since_date=date.today()):
        self.__doReadyLoadPage()
        news_info_list = []
        while True:
            ori_news_info_list = self.__miningOnePage()
            filtered_news_info_list = NewsInfoHelper.filterBySincaDate(ori_news_info_list, since_date)
            news_info_list = filtered_news_info_list
            if NewsCrawlerHelper.needStopMining(ori_news_info_list, filtered_news_info_list):
                break
        return news_info_list

    def __doReadyLoadPage(self):
        self._browser_driver.get(self.__url)
        container_element = self._browser_driver.find_element(By.TAG_NAME, 'body')
        actions = webdriver.ActionChains(self._browser_driver)
        actions.click(container_element)
        actions.perform()

    def __miningOnePage(self):
        actions = webdriver.ActionChains(self._browser_driver)
        actions.key_down(Keys.END)
        actions.pause(5)
        # actions.perform()
        parsed_data = self.getHtml(self.__url, action_chains=actions)
        # print("parsed_data=", parsed_data)
        self.__now_page += 1

        news_info_list = []
        # '[id="__SearchAll"]'(搜尋結果外框) > a[class="news"] (每一條新聞)
        news_element_list = parsed_data.find(id="_SearchAll").findAll("a", class_='news')
        for news_element in news_element_list:
            news_info = self.__obtainNewsInfo(news_element)
            news_info_list.append(news_info)
        return news_info_list

    def __obtainNewsInfo(self, news_element):
        news_info = NewsInfo()
        link_url = news_element["href"]

        time_element = news_element.find(class_="cat_time").find("time")
        str_pub_datetime = time_element["datetime"]
        pub_datetime = datetime.fromisoformat(str_pub_datetime)
        # print("pub_datetime = ", pub_datetime)

        title_element = news_element.find(class_="news_title").find("h3")
        title = title_element.getText()
        # print("title = ", title)

        news_info.setTitle(title)
        news_info.setLink(link_url)
        news_info.setPubDateTime(pub_datetime)
        return news_info

"""
經濟日報
"""
class MoneyUdnNewsClient(WebDriverClient):

    def __init__(self, url='https://money.udn.com/search/result/1001/比特幣', headless=True):
        super().__init__(headless=headless)
        self.__url = url

        self.__now_page = 0

    def findByMaxPages(self, max_pages=10):
        self.__doReadyLoadPage()
        news_info_list = []
        while self.__now_page <= max_pages:
            #news_info_list = self.__miningOnePage(news_info_list)
            news_info_list = self.__miningOnePage()
        return news_info_list

    def findBySinceDate(self, since_date=date.today()):
        self.__doReadyLoadPage()
        news_info_list = []
        while True:
            ori_news_info_list = self.__miningOnePage()
            filtered_news_info_list = NewsInfoHelper.filterBySincaDate(ori_news_info_list, since_date)
            news_info_list = filtered_news_info_list
            if NewsCrawlerHelper.needStopMining(ori_news_info_list, filtered_news_info_list):
                break
        return news_info_list

    def __doReadyLoadPage(self):
        self._browser_driver.get(self.__url)
        container_element = self._browser_driver.find_element(By.TAG_NAME, 'body')
        actions = webdriver.ActionChains(self._browser_driver)
        actions.click(container_element)
        actions.perform()

    def __miningOnePage(self):
        actions = webdriver.ActionChains(self._browser_driver)
        actions.key_down(Keys.END)
        actions.pause(5)
        # actions.perform()
        parsed_data = self.getHtml(self.__url, action_chains=actions)
        #print("parsed_data=", parsed_data)
        self.__now_page += 1

        news_info_list = []
        # '[id="__SearchAll"]'(搜尋結果外框) > a[class="news"] (每一條新聞)
        news_element_list = parsed_data.find("ul", class_="story-list-holder").findAll("li", class_='story-headline-wrapper')
        for news_element in news_element_list:
            news_info = self.__obtainNewsInfo(news_element)
            news_info_list.append(news_info)
        return news_info_list

    def __obtainNewsInfo(self, news_element):
        news_info = NewsInfo()
        story_content_element = news_element.find("div", class_="story__content")

        time_element = story_content_element.find("time")
        str_pub_datetime = time_element.getText()

        title_element = story_content_element.find("h3", class_="story__headline")
        title = title_element.getText().strip() # 此網頁會將搜尋的字眼化底線...(會多一個 <u></u>) --> 不曉得是不是自動處理掉了，反而是要處理前後空白

        link_element = story_content_element.find("a")
        link_url = link_element["href"]

        news_info.setTitle(title)
        news_info.setLink(link_url)
        # news_info.setPubDateTime(pub_datetime)
        return news_info

class BitCoinComNewsClient(HtmlClient):
    def __init__(self):
        super().__init__()
        # self.__url_pattern = 'https://news.bitcoin.com/page/${PAGE}/?s=Bitcoin'
        self.__url_pattern = 'https://news.bitcoin.com/page/${PAGE}/'
        self.__news_until = None # news_until

        self.__now_url = None
        self.__now_page = 1

    def findByMaxPages(self, max_pages=10):
        # 如果 __init__ 沒有，下面嘗試設定，這樣不行
        self.__now_url = None
        self.__now_page = 1
        news_info_list = []
        while self.__now_page <= max_pages:
            part_news_info_list = self.__miningOnePage()
            news_info_list.extend(part_news_info_list)
        return news_info_list

    def findBySinceDate(self, since_date = date.today()):
        news_info_list = []
        since_datetime = datetime.combine(since_date, datetime.min.time())
        while True:
            part_news_info_list = self.__miningOnePage()
            filtered_part_news_info_list = NewsInfoHelper.filterBySincaDate(part_news_info_list, since_date)
            news_info_list.extend(filtered_part_news_info_list)
            if len(filtered_part_news_info_list) != len(part_news_info_list):
                break;
        return news_info_list

    def findByInterval(self):
        pass


    def __doSetupNowUrl(self):
        self.__now_url = self.__url_pattern.replace('${PAGE}', str(self.__now_page) )
        #print(self._now_url)
        self.__now_page += 1

    def __miningOnePage(self):
        part_news_info_list = []

        self.__doSetupNowUrl()
        # s=Bitcoin
        params = {"s": "Bitcoin"}
        html_parsed_data = self.getHtml(self.__now_url, params=params) #目前花時最多的

        # data-desc='新聞列表' > class='searchlist' > li
        news_element_list = html_parsed_data.find("div", class_='td-main-content').findAll(class_='td-animation-stack') #新聞(標題)清單
        for news_element in news_element_list:
            news_info = self.__obtainNewsInfo(news_element)
            part_news_info_list.append(news_info)
        return part_news_info_list

    def __obtainPubDateTime(self, str_pub_datetime):
        for pub_datetime_format in self.__pub_datetime_formats:
            try:
                return datetime.strptime(str_pub_datetime, pub_datetime_format)
            except ValueError:
                pass # Do Nothing
        return None

    def __obtainNewsInfo(self, news_element):
        news_info = NewsInfo()
        items_detail_element = news_element.find(class_="item-details")

        title_element = items_detail_element.find(class_="entry-title")
        link_element = title_element.find("a")
        link_url = link_element["href"]
        title = link_element.getText()

        meta_info_element = items_detail_element.find(class_="td-module-meta-info")
        datetime_eleent = meta_info_element.find("time", class_="entry-date")
        str_pub_datetime = datetime_eleent["datetime"]
        pub_datetime = datetime.fromisoformat(str_pub_datetime)

        news_info.setTitle(title)
        news_info.setLink(link_url)
        news_info.setPubDateTime(pub_datetime)
        return news_info

class CNBCNewsClient(WebDriverClient):

    def __init__(self, url='https://www.cnbc.com/search/?query=Bitcoin&qsearchterm=Bitcoin', headless=True):
        super().__init__(headless=headless)
        self.__url = url
        self.__now_page = 0

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
            news_sources = list(self.__client_clazz_dict.keys() )

        for news_code in news_sources:
            client_clazz = self.__client_clazz_dict.get(news_code)

            if client_clazz != None:
                client = client_clazz()
                self.__client_dict[news_code] = client
            else:
                print("[Warning] Cannot found client_clazz by [" + news_code + "]")

    def findBySinceDate(self, since_date, close_after_iter = True):
        all_news_info_list = []
        client_list = list(self.__client_dict.values() )
        for client in client_list:
            news_info_list = client.findBySinceDate(since_date)
            all_news_info_list.extend(news_info_list)
            if close_after_iter == True:
                client.close()
        return all_news_info_list


    def closeAll(self):
        for client in self.__client_list:
            client.close()

class NewsCsvCrawler(NewsCrawler):

    def __init__(self, news_sources = None):
        super().__init__(news_sources)


    def save2Csv(self, since_date, days_freq=7):
        now_since_date = date.today()
        the_timedelta = timedelta(days=days_freq)
        while True:
            now_since_date = now_since_date - the_timedelta
            if now_since_date < since_date:
                now_since_date = since_date # 如果已經到希望的前面 since_date，則只讓他到這個 since_date

            self.findBySinceDate(now_since_date) #這裡對於「url 指定 page num 」的可以變成繼續撈「尚未撈過的」，但對於那種頁面到底的反而還是不行

            if now_since_date == since_date:
                break
