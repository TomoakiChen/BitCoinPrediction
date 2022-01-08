import pandas as pd
import urllib
from datetime import date as DateUtils
from datetime import datetime as DateTimeUtils
from datetime import timedelta
from PandasHelper import PandasDataFrameHelper
import numpy
from CoinPriceLib.Helper import *

class CryptoDatadownloadBinaceClient:

    __url_dict = {
        'Daily': 'https://www.cryptodatadownload.com/cdd/Binance_BTCUSDT_d.csv',
        'Hourly': 'https://www.cryptodatadownload.com/cdd/Binance_BTCUSDT_1h.csv',
        # 'Hourly': './Binance_BTCUSDT_1h.csv',
        'Minute': 'https://www.cryptodatadownload.com/cdd/Binance_BTCUSDT_minute.csv'
    }

    def __init__(self):
        pass

    def _readCsv(self, url):
        try:
            df = pd.read_csv(url, header=1)
        except urllib.error.URLError:
            # 有遇到一般的 urllib.request 不會說SSL問題，但是 pandas使用的方法(底也是urllib)報錯。
            import ssl
            ssl._create_default_https_context = ssl._create_unverified_context
            df = pd.read_csv(url, header=1)
        df = self._processingDataFrame(df)
        return df

    def _processingDataFrame(self, df):
        df = self._processingDateInfo(df)
        return df

    def _processingDateInfo(self, df):
        date_datas = []
        for date_data in df["date"]:
            date_datas.append(CryptoDatadownloadBinaceCsvDataParser.parseDateInfo(date_data))
        df["date"] = date_datas
        return df

    # ==================================================== 以下是 csv初始的 DataFrame 格式 ====================================================
    def getDailyDataFrame(self, desig_col_list=None, since=None, until=None, sort_by_date=True, asc_by_date=True):
        # 第一行是 CryptoDatadownload 的標註
        df = self._readCsv(self.__url_dict.get('Daily'))
        df = CrpytoDatadownloadBinanceDataHelper.filteringDateRange(df, since, until)
        df = CrpytoDatadownloadBinanceDataHelper.sortingDate(df, sort_by_date, asc_by_date)
        if desig_col_list == None:
            return df
        else:
            return df[desig_col_list]

    def getHourlyDataFrame(self, desig_col_list=None, since=None, until=None, sort_by_date=True, asc_by_date=True):
        df = self._readCsv(self.__url_dict.get('Hourly'))
        df = CrpytoDatadownloadBinanceDataHelper.filteringDateRange(df, since, until)
        df = CrpytoDatadownloadBinanceDataHelper.sortingDate(df, sort_by_date, asc_by_date)
        if desig_col_list == None:
            return df
        else:
            return df[desig_col_list]

    def getHourlyDataFrame4Test(self):
        hourly_df = pd.DataFrame({
            "date" : ["2021-11-12 13:00:00", "2021-11-12 12:00", "2021-11-11 07:00", "2021-10-01 08:00"],
            "close" : [10000, 20000, 30000, 100]
        })
        hourly_df["date"] = CryptoDatadownloadBinaceCsvDataParser.parseDateInfo(hourly_df["date"])
        return hourly_df
    # ==================================================== 以上是 csv初始的 DataFrame 格式 ====================================================

    # ==================================================== 以下是 Numpy 格式 ====================================================
    def getDailyClosedPriceList(self):
        df = self.getDailyDataFrame(["date", "close"])
        daily_closed_price_info_list = CryptoDatadownloadBinaceCsvDataParser.parseCsv2PeriodlyClosedPriceList(df)
        return daily_closed_price_info_list

    """
    def getDailyClosedPriceChangeList(self):
        daily_closed_price_change_info_list = []
        daily_closed_price_info_list = self.getDailyClosedPriceList()
        for index, daily_closed_price_info in enumerate(daily_closed_price_info_list):
            price_changed_rate = None
            today = daily_closed_price_info[0]
            if index > 0:
                preday_daily_closed_price_info = daily_closed_price_info_list[index - 1]
                preday_price = preday_daily_closed_price_info[1]
                today_price = daily_closed_price_info[1]
                price_changed_rate = FinanceHelper.countSampleReturn(today_price, preday_price)

            daily_closed_price_change_info = [today, price_changed_rate]
            daily_closed_price_change_info_list.append(daily_closed_price_change_info)
        return daily_closed_price_change_info_list
    """
    def getDailyClosedPriceNumpy(self):
        pass


    def getHourlyClosedPriceList(self):
        df = self.getHourlyDataFrame(["date", "close"])
        hourly_closed_price_info_list = CryptoDatadownloadBinaceCsvDataParser.parseCsv2PeriodlyClosedPriceList(df)
        return hourly_closed_price_info_list

    """
    def getHourlyClosedPriceChangeList(self):
        hourly_closed_price_change_info_list = []
        hourly_closed_price_info_list = self.getHourlyClosedPriceList()
        for index, hourly_closed_price_info in enumerate(hourly_closed_price_info_list):
            price_changed_rate = None
            record_datetime = hourly_closed_price_info[0]
            if index > 0:
                prehour_closed_price_info = hourly_closed_price_info_list[index - 1]
                prehour_price = prehour_closed_price_info[1]
                record_price = hourly_closed_price_info[1]
                price_changed_rate = FinanceHelper.countSampleReturn(record_price, prehour_price)

            hourly_closed_price_change_info = [record_datetime, price_changed_rate]
            hourly_closed_price_change_info_list.append(hourly_closed_price_change_info)
        return hourly_closed_price_change_info_list
    """
    # ==================================================== 以上是 Numpy 格式 ====================================================
