from PyWeb import HttpClient
from datetime import datetime as DateTime, date as Date, timedelta as TimeDelta
import pandas as pd
import json
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

    def __obtainDatePathParam(self, date):
        path_param_date = str(date)
        path_param_date = path_param_date.replace("-", "")
        return path_param_date

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

    def getJsonGoldAPIPrice(self, date=None, metal_symbol="XAU", currency="USD"):
        url = self.__base_url + "/" + metal_symbol + "/" + currency
        if date != None:
            url += "/" + self.__obtainDatePathParam(date)
        # url = self.__base_url + "/price" + "/" + metal_symbol + "/" + currency + "/" + date
        str_price_json = super().sendGetRequest(url, user_headers=self.__user_headers)
        return str_price_json

    def getDictGoldAPIPrice(self, date=None, metal_symbol="XAU", currency="USD"):
        str_price_json = self.getJsonGoldAPIPrice(date, metal_symbol, currency)
        dict_price = json.loads(str_price_json)
        return dict_price

class GoldPriceClient():

    __gold_api_client: GoldAPIClient
    __cache_csv_path: str

    def __init__(self, api_key, base_url="https://www.goldapi.io/api", cache_csv_path="./GoldPriceCache.csv"):
        self.__gold_api_client = GoldAPIClient(api_key, base_url=base_url)
        self.__cache_csv_path = cache_csv_path

    # def test(self):
    #     datas = self.__gold_api_client.getJsonPrice()
    #     print(datas)

    def __tryLoadCacheDateFrame(self):
        if self.__cache_csv_path != None:
            df_cache = pd.read_csv(self.__cache_csv_path)
            # df_cache["date"] = pd.to_datetime(df_cache["date"])
            # df_cache = GoldPriceHelper.processGoldPriceDataFrame(df_cache)
            # print(df_cache)
            return df_cache
        else:
            return None

    def __obtainSearchDateList(self, since, until, df_cache):
        search_date_list = []
        time_delta = TimeDelta(days=1)
        now_date = since
        while(True):
            # daily_price = self.__gold_api_client.getDictGoldAPIPrice(date=now_date)
            # price_list.append(daily_price)
            if isinstance(df_cache, type(None)) == False:
            # if df_cache not None:
                # str_now_date = str(now_date)
                # print(now_date)
                # df_cache_4_desig_date =  df_cache[(df_cache["date"] == now_date)]
                # print(df_cache_4_desig_date)
                df_cache_4_desig_date =  df_cache[(GoldPriceHelper.processDate4GoldPriceDataFrame(df_cache)["date"] == now_date)]
                if isinstance(df_cache_4_desig_date, type(None)) == False and df_cache_4_desig_date.empty: # 找不到 cache 資料才需要 search
                    search_date_list.append(now_date)
            else:
                search_date_list.append(now_date)
            now_date += time_delta
            if now_date > until:
                break
        return search_date_list


    def __obtainBasePriceList(self, df_cache):
        if isinstance(df_cache, type(None)) == True:
            price_list = list()
        else:
            price_list = df_cache.to_dict('records')
        return price_list



    def _getGoldAPIPriceDictList(self, since=Date.today(), until=Date.today()):
        df_cache = self.__tryLoadCacheDateFrame()
        price_list = self.__obtainBasePriceList(df_cache)

        if isinstance(since, str):
             since = Date.fromisoformat(since)

        if isinstance(until, str):
             until = Date.fromisoformat(until)

        # time_delta = TimeDelta(days=1)
        # now_date = since
        # while(True):
        #     daily_price = self.__gold_api_client.getDictGoldAPIPrice(date=now_date)
        #     price_list.append(daily_price)
        #     now_date += time_delta
        #     if now_date > until:
        #         break
        need_search_date_list = self.__obtainSearchDateList(since, until, df_cache)
        for desig_date in need_search_date_list:
            daily_price = self.__gold_api_client.getDictGoldAPIPrice(date=desig_date)
            price_list.append(daily_price)
        return price_list

    def getGoldAPIPriceDataFrame(self, since=Date.today(), until=Date.today()):
        price_list = self._getGoldAPIPriceDictList(since, until)
        df = pd.DataFrame(price_list)
        df = df.sort_values(by=["date"])
        if self.__cache_csv_path != None:
            df.to_csv(self.__cache_csv_path, index=False)
        return df

class GoldPriceHelper:

    @staticmethod
    def processGoldPriceDataFrame(df_price):
        df_price = GoldPriceHelper.processDate4GoldPriceDataFrame(df_price)
        return df_price


    @staticmethod
    def processDate4GoldPriceDataFrame(df_price):
        # str_date_list = df_price["date"].values
        # date_list = [Date.fromisoformat(str_date.split("T")[0]) for str_date in str_date_list]
        # df_price["date"] = date_list
        # return df_price
        df_price["date"] = GoldPriceHelper.processDateDataFrame(df_price["date"])
        return df_price

    def processDateDataFrame(df_date):
        str_date_list = df_date.values
        date_list = [Date.fromisoformat(str(str_date).split("T")[0]) for str_date in str_date_list]
        df_date = date_list
        return df_date
