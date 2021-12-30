from PyWeb import HttpClient
import ssl
# class TestClient(HttpClient):
#
#     def doGetTest(self):
#         return super().sendGetRequest("https://www.google.com")

class GoldAPIClient(HttpClient):
    __api_key = None
    __base_url = None

    __user_headers = dict()

    def __init__(self, api_key, base_url="https://www.goldapi.io/api"):
        self.__api_key = api_key
        self.__base_url = base_url
        self.__doSetupUserHeaders()
        # https://blog.csdn.net/anjingshen/article/details/121459239
        # ssl._create_default_https_context = ssl._create_unverified_context

    def __doSetupUserHeaders(self):
        self.__user_headers["x-access-token"] = self.__api_key
        self.__user_headers["Content-Type"] = "application/json"

    def getJsonStatus(self):
        url = self.__base_url + "/status"
        print(url)
        # str_status_json = self.super().sendGetRequest(url, user_headers=self.__user_headers)
        str_status_json = super().sendGetRequest(url, user_headers=self.__user_headers)
        return str_status_json

    def getJsonStat(self):
        url = self.__base_url + "/stat"
        str_stat_json = super().sendGetRequest(url, user_headers=self.__user_headers)
        return str_stat_json

    def getJsonPrice(self, date, metal_symbol="XAU", currency="USD"):
        url = self.__base_url + "/price" + "/" + metal_symbol + "/" + currency + "/" + date
        print("url = " + url)
        str_price_json = super().sendGetRequest(url, user_headers=self.__user_headers)
        return str_price_json
