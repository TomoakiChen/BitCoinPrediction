# https://www.metals-api.com/documentation
from PyWeb import HttpClient
import MetalPrice.MetalsAPI.Entity as MetalsAPIEntity
from datetime import datetime, date
import ssl
import json

class MatalsAPIClient(HttpClient):

    __base_url = None
    __api_key = None

    def __init__(self, api_key, base_url="https://www.metals-api.com/api"):
        self.__api_key = api_key
        self.__base_url = base_url

    def __obtainBaseQueryParams(self):
        queryParams = dict()
        queryParams["access_key"] = self.__api_key
        return queryParams

    def __obtainSymbolsQueryParamValue(self, symbols):
        # try:
        #     iterator = iter(symbols)
        # except TypeError:
        #     # not iterable
        #     return symbols
        # else:
        #     return (",").join(symbols)
        if isinstance(symbols, (list, tuple)):
            return ",".join(symbols)
        else:
            return symbols


    def __doGet(self, url, user_query_params=None):
        query_params = self.__obtainBaseQueryParams()
        if user_query_params != None:
            query_params.update(user_query_params)
        print("url= " + url)
        print("query_params= " + str(query_params) )
        str_json = self.sendGetRequest(url, queryParams=query_params)
        return str_json

    # ========================================== 以下為基礎的 method ，直接 call API endpoint ==========================================
    def getJsonCurrencySymbolsData(self):
        url = self.__base_url + "/symbols"
        str_json = self.__doGet(url)
        return str_json

    # def getJsonTimeSeriesData(self, start_date=date.today(), end_date=date.today(), base="USD", symbols=""):
    #     queryParams = self.__obtainBaseQueryParams()
    #     queryParams["start_date"] = start_date
    #     queryParams["end_date"] = end_date
    #     url = self.__base_url + "/timeseries"
    #     str_json = self.sendGetRequest(url, queryParams=queryParams)
    #     return str_json

    def getJsonTimeSeriesData(self, start_date=date.today(), end_date=date.today(), base="USD", symbols=["USD"]):
        user_query_params = dict()
        user_query_params["start_date"] = str(start_date)
        user_query_params["end_date"] = str(end_date)
        user_query_params["base"] = base
        user_query_params["symbols"] = self.__obtainSymbolsQueryParamValue(symbols)
        url = self.__base_url + "/timeseries"
        str_json = self.__doGet(url, user_query_params=user_query_params)
        return str_json
    # ========================================== 以上為基礎的 method ，直接 call API endpoint ==========================================

    def getCurrencySymbolsData(self):
        data_list = list()
        str_json = self.getJsonCurrencySymbolsData()
        symbol_dict = json.loads(str_json)
        for code, label in symbol_dict.items():
            data = Entity.MetalsAPISymbol(code, label)
            data_list.append(data)
        return data_list

    def getDesigCurrencySymbolDataByCode(self, desig_code):
        str_json = self.getJsonCurrencySymbolsData()
        symbol_dict = json.loads(str_json)
        for code, label in symbol_dict.items():
            if desig_code == code:
                return MetalsAPIEntity.MetalsAPISymbol(code, label)
        return None

    def getDesigCurrencySymbolDataByLabel(self, keyword):
        data_list = None
        str_json = self.getJsonCurrencySymbolsData()
        symbol_dict = json.loads(str_json)
        for code, label in symbol_dict.items():
            if keyword in label:
                data = MetalsAPIEntity.MetalsAPISymbol(code, label)
                if data_list == None:
                    data_list = list()
                data_list.append(data)
        return data_list


class GoldPriceClient():

    __metal_api_client = None

    def __init__(self, api_key, base_url="https://www.metals-api.com/api"):
        self.__metal_api_client = MatalsAPIClient(api_key, base_url=base_url)

    def getJsonPrices(self, start_date=date.today(), end_date=date.today()):
        return self.__metal_api_client.getJsonTimeSeriesData(start_date=start_date, end_date=end_date, base="XAU", symbols=["USD"])
