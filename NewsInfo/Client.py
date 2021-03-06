from datetime import datetime, date, timedelta
from AkiPyUtil.AkiPyDateTime import AkiDateTimeUtil
from PyWeb import HtmlClient, WebDriverClient
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from NewsInfo.Entity import NewsInfo
from NewsInfo.Helper import NewsInfoHelper, NewsCrawlerHelper


class PaginationClient(HtmlClient):

    def __init__(self):
        super().__init__()


class AjaxRefreshClient(WebDriverClient):

    def __init__(self, browser_less=True, console_log_less=True):
        super().__init__(browser_less=browser_less, console_log_less=console_log_less)


class LTNNewsClient(PaginationClient):

    def __init__(self):
        super().__init__()
        self.__url_pattern = 'https://news.ltn.com.tw/topic/%E6%AF%94%E7%89%B9%E5%B9%A3/${PAGE}'
        # self.__news_since = None # news_since
        self.__news_until = None  # news_until

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

    def findBySinceDate(self, since_date=date.today()):
        return self.findByInterval(since_date, None)

    def findByInterval(self, since_date=date.today(), until_date=date.today()):
        news_info_list = []
        # since_datetime = datetime.combine(since_date, datetime.min.time())
        while True:
            part_news_info_list = self.__miningOnePage()
            # [news_info for news_info in part_news_info_list if news_info.getPubDateTime() >= since_datetime]
            filtered_part_news_info_list = NewsInfoHelper.filterByInterval(part_news_info_list, since_date, until_date)
            news_info_list.extend(filtered_part_news_info_list)

            earliest_news_info = part_news_info_list[-1]
            earliest_pub_datetime = earliest_news_info.getPubDateTime()
            if(NewsInfoHelper.checkIsAfterEqSinceDate(earliest_news_info, since_date) == False):
                break
        return news_info_list

    def __doSetupNowUrl(self):
        self.__now_url = self.__url_pattern.replace('${PAGE}', str(self.__now_page))
        # print(self._now_url)
        self.__now_page += 1

    def __miningOnePage(self):
        part_news_info_list = []
        self.__doSetupNowUrl()
        html_parsed_data = self.getHtml(self.__now_url)  # 目前花時最多的

        # data-desc='新聞列表' > class='searchlist' > li
        news_element_list = html_parsed_data.find(class_='searchlist').findAll('li')  # 新聞(標題)清單
        for news_element in news_element_list:
            news_info = self.__obtainNewsInfo(news_element)
            part_news_info_list.append(news_info)
        return part_news_info_list

    # ============================ 下面跟 NewsInfo 有關 ============================
    def __obtainPubDateTime(self, str_pub_datetime):
        for pub_datetime_format in self.__pub_datetime_formats:
            try:
                return datetime.strptime(str_pub_datetime, pub_datetime_format)
            except ValueError:
                pass  # Do Nothing
        return None

    def __obtainNewsInfo(self, news_element):
        news_info = NewsInfo()
        tag_link_element = news_element.find("a", class_="immtag")
        pub_datetime_element = news_element.findNext('span')
        str_pub_datetime = pub_datetime_element.getText()
        #news_info.setPubDateTime(datetime.strptime(str_pub_datetime, self._pub_datetime_format))
        news_info.setPubDateTime(self.__obtainPubDateTime(str_pub_datetime))

        title_link_element = news_element.find("a", class_="tit")
        news_info.setLink(title_link_element['href'])  # 新聞連結
        news_info.setTitle(title_link_element.find('h3').getText())  # 新聞標題

        return news_info
    # ============================ 上面跟 NewsInfo 有關 ============================


class YahooNewsClient(AjaxRefreshClient):

    def __init__(self, url='https://tw.news.yahoo.com/tag/比特幣', browser_less=True):
        super().__init__(browser_less=browser_less)
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
        container_element = self._browser_driver.find_element(
            By.TAG_NAME, 'body')
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
        text = link_element.getText()  # 此method會忽略掉 註解和tag

        news_info.setTitle(text)
        news_info.setLink(link_url)
        return news_info


class cnYESNewsClient(AjaxRefreshClient):

    def __init__(self, url='https://www.cnyes.com/search/news?keyword=比特幣', browser_less=True):
        super().__init__(browser_less=browser_less)
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
        return self.findByInterval(since_date, None)

    def findByUntilDate(self, until_date=date.today()):
        return self.findByInterval(None, until_date)

    def findByInterval(self, since_date=date.today(), until_date=date.today()):
        self.__doReadyLoadPage()
        news_info_list = []
        while True:
            news_element_list = self.__miningOnePage()
            earliest_news_element = news_element_list[-1]
            earliest_news_info = self.__obtainNewsInfo(earliest_news_element)
            print("earliest_news_info = " + str(earliest_news_info))
            print("since_date = " + str(since_date))
            if(NewsInfoHelper.checkIsAfterEqSinceDate(earliest_news_info, since_date) == False):
                for news_element in news_element_list:
                    news_info = self.__obtainNewsInfo(news_element)
                    if NewsInfoHelper.checkIsInInterval(news_info, since_date, until_date):
                        news_info_list.append(news_info)
                break
        return news_info_list

    def __doReadyLoadPage(self):
        self._browser_driver.get(self.__url)
        container_element = self._browser_driver.find_element(
            By.TAG_NAME, 'body')
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
        # '[id="__SearchAll"]'(搜尋結果外框) > a[class="news"] (每一條新聞)
        news_element_list = parsed_data.find(
            id="_SearchAll").findAll("a", class_='news')
        return news_element_list

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
class MoneyUdnNewsClient(AjaxRefreshClient):

    def __init__(self, url='https://money.udn.com/search/result/1001/比特幣', browser_less=True):
        super().__init__(browser_less=browser_less)
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
        return self.findByInterval(since_date, None)

    def findByUntilDate(self, until_date=date.today()):
        return self.findByInterval(None, until_date)

    def findByInterval(self, since_date=date.today(), until_date=date.today()):
        self.__doReadyLoadPage()
        news_info_list = []
        while True:
            news_element_list = self.__miningOnePage()
            earliest_news_element = news_element_list[-1]
            earliest_news_info = self.__obtainNewsInfo(earliest_news_element)
            print("earliest_news_info = " + str(earliest_news_info))
            print("since_date = " + str(since_date))
            if(NewsInfoHelper.checkIsAfterEqSinceDate(earliest_news_info, since_date) == False):
                for news_element in news_element_list:
                    news_info = self.__obtainNewsInfo(news_element)
                    if NewsInfoHelper.checkIsInInterval(news_info, since_date, until_date):
                        news_info_list.append(news_info)
                break
        return news_info_list

    def __doReadyLoadPage(self):
        self._browser_driver.get(self.__url)
        container_element = self._browser_driver.find_element(
            By.TAG_NAME, 'body')
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
        return news_element_list

    def __obtainNewsInfo(self, news_element):
        news_info = NewsInfo()
        story_content_element = news_element.find(
            "div", class_="story__content")

        time_element = story_content_element.find("time")
        str_pub_datetime = time_element.getText()

        title_element = story_content_element.find(
            "h3", class_="story__headline")
        # 此網頁會將搜尋的字眼化底線...(會多一個 <u></u>) --> 不曉得是不是自動處理掉了，反而是要處理前後空白
        title = title_element.getText().strip()

        link_element = story_content_element.find("a")
        link_url = link_element["href"]

        news_info.setTitle(title)
        news_info.setLink(link_url)
        # news_info.setPubDateTime(pub_datetime)
        return news_info


class BitCoinComNewsClient(PaginationClient):
    def __init__(self):
        super().__init__()
        # self.__url_pattern = 'https://news.bitcoin.com/page/${PAGE}/?s=Bitcoin'
        self.__url_pattern = 'https://news.bitcoin.com/page/${PAGE}/'
        self.__news_until = None  # news_until

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

    """
    def findBySinceDate(self, since_date=date.today()):
        news_info_list = []
        since_datetime = datetime.combine(since_date, datetime.min.time())
        while True:
            part_news_info_list = self.__miningOnePage()
            filtered_part_news_info_list = NewsInfoHelper.filterBySincaDate(
                part_news_info_list, since_date)
            news_info_list.extend(filtered_part_news_info_list)
            if len(filtered_part_news_info_list) != len(part_news_info_list):
                break
        return news_info_list

    def findByInterval(self):
        pass
    """
    def findBySinceDate(self, since_date=date.today()):
        return self.findByInterval(since_date, None)

    def findByInterval(self, since_date=date.today(), until_date=date.today()):
        news_info_list = []
        # since_datetime = datetime.combine(since_date, datetime.min.time())
        while True:
            part_news_info_list = self.__miningOnePage()
            # [news_info for news_info in part_news_info_list if news_info.getPubDateTime() >= since_datetime]
            filtered_part_news_info_list = NewsInfoHelper.filterByInterval(part_news_info_list, since_date, until_date)
            news_info_list.extend(filtered_part_news_info_list)

            earliest_news_info = part_news_info_list[-1]
            earliest_pub_datetime = earliest_news_info.getPubDateTime()
            if(NewsInfoHelper.checkIsAfterEqSinceDate(earliest_news_info, since_date) == False):
                break
        return news_info_list

    def __doSetupNowUrl(self):
        self.__now_url = self.__url_pattern.replace('${PAGE}', str(self.__now_page))
        # print(self._now_url)
        self.__now_page += 1

    def __miningOnePage(self):
        part_news_info_list = []

        self.__doSetupNowUrl()
        # s=Bitcoin
        params = {"s": "Bitcoin"}
        html_parsed_data = self.getHtml(
            self.__now_url, params=params)  # 目前花時最多的

        # data-desc='新聞列表' > class='searchlist' > li
        news_element_list = html_parsed_data.find("div", class_='td-main-content').findAll(class_='td-animation-stack')  # 新聞(標題)清單
        for news_element in news_element_list:
            news_info = self.__obtainNewsInfo(news_element)
            part_news_info_list.append(news_info)
        return part_news_info_list

    def __obtainPubDateTime(self, str_pub_datetime):
        for pub_datetime_format in self.__pub_datetime_formats:
            try:
                return datetime.strptime(str_pub_datetime, pub_datetime_format)
            except ValueError:
                pass  # Do Nothing
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


class CNBCNewsClient(AjaxRefreshClient):

    def __init__(self, url='https://www.cnbc.com/search/?query=Bitcoin&qsearchterm=Bitcoin', browser_less=True):
        super().__init__(browser_less=browser_less)
        self.__url = url
        self.__now_page = 0
