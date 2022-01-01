from PyWeb import HttpClient
from datetime import datetime as DateTime, date as Date, timedelta as TimeDelta
import pandas as pd
import json
import time

# ====================================== 以下算更核心的 Client、Helper ======================================
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
        str_date = dict_price["date"]
        date = MetalPriceHelper.parseStrDate(str_date)
        dict_price["date"] = date
        return dict_price

class MetalPriceClient():

    __gold_api_client: GoldAPIClient
    __cache_csv_path: str
    __metal_code: str
    __wait_sec: int
    __currency = "USD"

    def __init__(self, api_key, metal_code, cache_csv_path, base_url="https://www.goldapi.io/api", wait_sec=1):
        self.__gold_api_client = GoldAPIClient(api_key, base_url=base_url)
        self.__cache_csv_path = cache_csv_path
        self.__metal_code = metal_code
        self.__wait_sec = wait_sec

    def __tryLoadCacheDateFrame(self):
        if self.__cache_csv_path != None:
            try:
                df_cache = pd.read_csv(self.__cache_csv_path)
                df_cache = MetalPriceHelper.processGoldPriceDataFrame(df_cache) #保持原有格式，所以不真的 replace --> 202112312039 DataFrame 裡面讓她是處理過的
                return df_cache
            except FileNotFoundError:
                print("No Cache File Now")
                return None
        else:
            return None

    def __obtainSearchDateList(self, since, until, df_cache):
        search_date_list = []
        time_delta = TimeDelta(days=1)
        now_date = since
        while(True):
            if isinstance(df_cache, type(None)) == False:
            # if df_cache not None: # 這種不行
                df_cache_4_desig_date =  df_cache[(MetalPriceHelper.processDate4GoldPriceDataFrame(df_cache)["date"] == now_date)]
                # df_cache_4_desig_date =  df_cache[(df_cache["date"] == str(now_date))]
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
            price_list = df_cache.to_dict('records') # https://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.DataFrame.to_dict.html#pandas.DataFrame.to_dict
        return price_list



    def _getGoldAPIPriceDictList(self, since=Date.today(), until=Date.today()):
        df_cache = self.__tryLoadCacheDateFrame()
        # print(df_cache)
        price_list = self.__obtainBasePriceList(df_cache)

        if isinstance(since, str):
             since = Date.fromisoformat(since)

        if isinstance(until, str):
             until = Date.fromisoformat(until)

        need_search_date_list = self.__obtainSearchDateList(since, until, df_cache)
        # print(need_search_date_list)
        for desig_date in need_search_date_list:
            daily_price = self.__gold_api_client.getDictGoldAPIPrice(date=desig_date, metal_symbol=self.__metal_code)
            price_list.append(daily_price)
            if self.__wait_sec != None:
                print("wait for : " + str(self.__wait_sec) + "sec")
                time.sleep(self.__wait_sec)
        return price_list

    def getGoldAPIPriceDataFrame(self, since=Date.today(), until=Date.today(), desig_col_list=None):
        price_list = self._getGoldAPIPriceDictList(since, until)
        df = pd.DataFrame(price_list)
        df = df.sort_values(by=["date"]) # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html
        if self.__cache_csv_path != None:
            df.to_csv(self.__cache_csv_path, index=False)

        df = MetalPriceHelper.filteringDateRange(df, since, until)
        if desig_col_list is None:
            return df
        else:
            return df[desig_col_list]
class MetalPriceHelper:
    @staticmethod
    def parseStrDate(str_api_date):
        str_api_date = str(str_api_date)
        if "T" in str_api_date:
            return Date.fromisoformat(str_api_date.split("T")[0])
        else:
            return Date.fromisoformat(str_api_date)
    @staticmethod
    def processGoldPriceDataFrame(df_price):
        df_price = MetalPriceHelper.processDate4GoldPriceDataFrame(df_price)
        return df_price


    @staticmethod
    def processDate4GoldPriceDataFrame(df_price):
        df_price["date"] = MetalPriceHelper.processDateDataFrame(df_price["date"])
        return df_price

    def processDateDataFrame(df_date):
        str_date_list = df_date.values
        # date_list = [MetalPriceHelper.parseStrDate(str_date) for str_date in str_date_list]
        date_list = [MetalPriceHelper.parseStrDate(str_date) for str_date in str_date_list]
        df_date = date_list
        return df_date

    # @staticmethod
    # def filteringDateRange(df, since, until):
    #     if since == None and until == None:
    #         return df
    #     elif since != None and until == None:
    #         if isinstance(since, Date) or isinstance(since, DateTime):
    #             since = str(since)
    #         return df[(df['date'] >= since)]
    #     elif since == None and until != None:
    #         if isinstance(until, Date) or isinstance(until, DateTime):
    #             until = str(until)
    #         return df[(df['date'] <= until)]
    #     else:
    #         if isinstance(since, Date) or isinstance(since, DateTime):
    #             since = str(since)
    #         if isinstance(until, Date) or isinstance(until, DateTime):
    #             until = str(until)
    #         return df[(df['date'] >= since) & (df['date'] <= until)]
    @staticmethod
    def filteringDateRange(df, since, until):
        if since == None and until == None:
            return df
        elif since != None and until == None:
            if isinstance(since, str):
                since = Date.fromisoformat(since)
            return df[(df['date'] >= since)]
        elif since == None and until != None:
            if isinstance(until,str):
                until = Date.fromisoformat(until)
            return df[(df['date'] <= until)]
        else:
            if isinstance(since, str):
                since = Date.fromisoformat(since)
            if isinstance(until, str):
                until = Date.fromisoformat(until)
            return df[(df['date'] >= since) & (df['date'] <= until)]
# ====================================== 以上算更核心的 Client、Helper ======================================


class GoldPriceClient(MetalPriceClient):
    def __init__(self, api_key, base_url="https://www.goldapi.io/api", cache_csv_path="./GoldPriceCache.csv"):
        super().__init__(api_key, "XAU", cache_csv_path, base_url)


class SilverPriceClient(MetalPriceClient):
    def __init__(self, api_key, base_url="https://www.goldapi.io/api", cache_csv_path="./SilverPriceCache.csv"):
        super().__init__(api_key, "XAG", cache_csv_path, base_url)

class PlatinumPriceClient(MetalPriceClient):
    def __init__(self, api_key, base_url="https://www.goldapi.io/api", cache_csv_path="./SilverPriceCache.csv"):
        super().__init__(api_key, "XPT", cache_csv_path, base_url)
