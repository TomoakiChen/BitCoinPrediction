from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import bs4
import urllib.request as req


class HttpClient:

    def obtainHeaders(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
        }
        return headers

    def sendRequest(self, url, encoded="utf-8"):
        headers = self.obtainHeaders()
        URL = req.Request(url, headers=headers)
        with req.urlopen(URL) as res:
            pageData = res.read().decode(encoded)
        return pageData


class HtmlClient:

    def __init__(self):
        self._httpClient = HttpClient()

    def getHtml(self, url):
        pageData = self._httpClient.sendRequest(url)
        parsedData = bs4.BeautifulSoup(pageData, "lxml")
        return parsedData


# ============================================================================================================================================
class WebDriverClient:
    # _auto_load_website_actions_ =
    def __init__(self, driver_type='Chrome'):
        self._browser_driver = self._setupBrowserDriver(driver_type)

    def _setupBrowserDriver(self, driver_type):
        if driver_type == 'Chrome':
            op = webdriver.ChromeOptions()
            # 這樣可以不用打開實際的瀏覽器 https://stackoverflow.com/questions/7593611/selenium-testing-without-browser
            op.add_argument('headless')
            return webdriver.Chrome(options=op)
        elif driver_type == 'Firefox':
            return webdriver.Firefox()
        else:
            return webdriver.Chrome()

    def getHtml(self, url, action_chains=None):
        self._browser_driver.get(url)
        action_chains = self.obtainAction4BottomLoad()
        if action_chains != None:
            action_chains.perform()
        page_data = self._browser_driver.page_source
        parsed_data = bs4.BeautifulSoup(page_data, "lxml")
        return parsed_data

    """
    # 目前難以寫成一種方便使用的底層 method，此專案中先在 YahooNewsClient
    # 中自行處理
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
