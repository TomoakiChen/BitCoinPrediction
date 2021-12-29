from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import bs4
import urllib.request as req

class HttpClient:

    # 這支有可能給繼承使用，所以 protected 的 _ (單底線)
    def _obtainHeaders(self, user_headers=None):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
        }
        if user_headers != None:
            headers.update(user_headers)
        return headers

    def _processGetRequestUrl(self, ori_url, queryParams):
        if queryParams == None:
            return ori_url
        else:
            result_url = ori_url
            result_url += "?"
            for index, (queryParamKey, queryParamValue) in enumerate(queryParams.items()):
                if index >= 1:
                    result_url += "&"
                result_url += queryParamKey
                result_url += "="
                result_url += str(queryParamValue)
                # print("index = " + str(index) + ", queryParamKey = " + queryParamKey + ", queryParamValue = " + queryParamValue)
            return result_url

    def _obtainPostFormParamsData(self, formParams):
        pass

    def sendRequest(self, url, method="GET", user_headers=None, params=None):
        if method == "GET":
            return self.sendGetRequest(url, user_headers=user_headers, queryParams=params)
        elif method == "POST":
            return self.sendPostRequest(url, user_headers=user_headers, formParams=params)
        else:
            return self.sendGetRequest(url, user_headers=user_headers, queryParams=params)

    def sendGetRequest(self, url, encoded="utf-8", user_headers=None, queryParams=None):
        headers = self._obtainHeaders(user_headers)
        print("url = " + url)
        print("headers = " + str(headers))        
        url = self._processGetRequestUrl(url, queryParams)
        URL = req.Request(url, headers=headers)
        with req.urlopen(URL) as res:
            pageData = res.read().decode(encoded)
        return pageData

    def sendPostRequest(self, url , encoded="utf-8", user_headers=None, formParams=None):
        headers = self._obtainHeaders(user_headers)
        datas = self._obtainPostFormParamsData(formParams)
        URL = req.Request(url, headers=headers)
        with req.urlopen(URL) as res:
            pageData = res.read().decode(encoded)
        return pageData

    def close(self):
        print("HttpClient.close()")
        pass

class HtmlClient:

    def __init__(self):
        self.__httpClient = HttpClient()

    def getHtml(self, url, params=None):
        pageData = self.__httpClient.sendRequest(url, params=params)
        parsedData = bs4.BeautifulSoup(pageData, "lxml")
        return parsedData

    def close(self):
        self.__httpClient.close()

# ============================================================================================================================================
class WebDriverClient:
    # _auto_load_website_actions_ =
    def __init__(self, driver_type='Chrome', browser_less=False, console_log_less=False):
        self._browser_driver = self.__setupBrowserDriver(driver_type, browser_less, console_log_less)

    def __setupBrowserDriver(self, driver_type, browser_less, console_log_less):
        if driver_type == 'Chrome':
            op = webdriver.ChromeOptions()
            if browser_less:
                # 這樣可以不用打開實際的瀏覽器 https://stackoverflow.com/questions/7593611/selenium-testing-without-browser
                op.add_argument('headless')

            if console_log_less:
                op.add_argument("--log-level=3")
            return webdriver.Chrome(options=op)
        elif driver_type == 'Firefox':
            return webdriver.Firefox()
        else:
            return self.__setupBrowserDriver('Chrome', browser_less, console_log_less)

    def getHtml(self, url, action_chains=None):
        # self._browser_driver.get(url)
        if action_chains != None:
            action_chains.perform()
        page_data = (self._browser_driver.page_source).encode('utf-8') # https://stackoverflow.com/questions/16823086/selenium-webdriver-and-unicode
        parsed_data = bs4.BeautifulSoup(page_data, "lxml")
        # print("parsed_data = " + str(parsed_data) )
        return parsed_data

    def close(self):
        print("WebDriverClient close()")
        self._browser_driver.quit()

    """
    # 目前難以寫成一種方便使用的底層 method，此專案中先在 YahooNewsClient
    # 中自行處理webdriver
    def obtainAction4BottomLoad(self):
        container_element = self._browser_driver.find_element(By.TAG_NAME, 'body')
        actions = webdriver.ActionChains(self._browser_driver)
        actions.click(container_element)
        actions.key_down(Keys.END)
        actions.pause(2)
        actions.key_down(Keys.END)
        actions.pause(2)
        actions.key_down(Keys.END)
        return actions
    """
