import pandas as pd
import urllib
from datetime import date as DateUtils
from datetime import datetime as DateTimeUtils
from PandasHelper import PandasDataFrameHelper
import numpy

class CryptoDatadownloadBinaceClient:

    __url_dict = {
        'Daily': 'https://www.cryptodatadownload.com/cdd/Binance_BTCUSDT_d.csv',
        'Hourly': 'https://www.cryptodatadownload.com/cdd/Binance_BTCUSDT_1h.csv',
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
    def getDailyDataFrame(self, desig_col_list=None):
        # 第一行是 CryptoDatadownload 的標註
        df = self._readCsv(self.__url_dict.get('Daily'))
        if desig_col_list == None:
            return df
        else:
            return df[desig_col_list]

    def getHourlyDataFrame(self, desig_col_list=None):
        df = self._readCsv(self.__url_dict.get('Hourly'))
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
    def getDailyClosedPriceNumpy(self):
        df = self.getDailyDataFrame(["date", "close"])
        daily_closed_price_info_list = CryptoDatadownloadBinaceCsvDataParser.parseCsv2PeriodlyClosedPriceNumpy(df)
        return daily_closed_price_info_list

    def getDailyClosedPriceChangeNumpy(self):
        daily_closed_price_change_info_list = []
        daily_closed_price_info_list = self.getDailyClosedPriceNumpy()
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

    def getDailyClosedPriceNumpy(self):
        pass


    def getHourlyClosedPriceNumpy(self):
        df = self.getHourlyDataFrame(["date", "close"])
        hourly_closed_price_info_list = CryptoDatadownloadBinaceCsvDataParser.parseCsv2PeriodlyClosedPriceNumpy(df)
        return hourly_closed_price_info_list

    def getHourlyClosedPriceChangeNumpy(self):
        hourly_closed_price_change_info_list = []
        hourly_closed_price_info_list = self.getHourlyClosedPriceNumpy()
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
    # ==================================================== 以上是 Numpy 格式 ====================================================


# ========================================================= 以下 輔佐將 csv data 轉換 =========================================================
class CryptoDatadownloadBinaceCsvDataParser:

    """
    numpy 覺得就是該單欄資料(暫時限close資料狀況下)
    """
    @staticmethod
    def parseCsv2PeriodlyClosedPriceNumpy(df):
        # periodly_closed_price_info_numpy = numpy.asarray([])
        periodly_closed_price_info_numpy = numpy.empty(shape=2)
        periodly_closed_price_list = df.to_numpy()
        # print(type(periodly_closed_price_list))
        for periodly_closed_price in periodly_closed_price_list:
            period_label = periodly_closed_price[0]

            price = periodly_closed_price[1]

            periodly_closed_price_info = numpy.asarray([period_label, price])
            periodly_closed_price_info_numpy = numpy.append(periodly_closed_price_info_numpy, periodly_closed_price_info, axis=1)

        periodly_closed_price_info_numpy = numpy.flip(periodly_closed_price_info_numpy, axis=0)
        # print(type(periodly_closed_price_info_list))
        return periodly_closed_price_info_numpy

    @staticmethod
    def parseCsv2ClosedPriceNumpy(df):
        closed_price_info_list = []
        periodly_closed_price_list = df.to_numpy()
        for periodly_closed_price in periodly_closed_price_list:
            closed_price_info = []

            period_label = periodly_closed_price[0]

            price = periodly_closed_price[1]

            closed_price_info = price
            closed_price_info_list.append(closed_price_info)

        closed_price_info_list.reverse()
        return closed_price_info_list


    @staticmethod
    def parseDateInfo(str_date_time):
        if str_date_time.__contains__('AM') or str_date_time.__contains__('PM'):
            date_time = DateTimeUtils.strptime(str_date_time, "%Y-%m-%d %I-%p")
        else:
            date_time = pd.to_datetime(str_date_time) # DateTimeUtils.strptime("%Y-%m-%d %H:%M:%S", str_date_time)
        return date_time
# ========================================================= 以上 輔佐將 csv data 轉換 =========================================================


# ========================================================= 以下 轉換 =========================================================
class PeriodlyCoinPriceInfo:

    _period_col = None
    _period_freq = None
    _pre_df = None
    _filter_not_completed_period = None

    _period_list = []
    _period_df_dict = {}
    _period_numpy_dict = {}

    def __init__(self, df, period_col="date", period_freq="7D", filter_not_completed_period = True):
        self._pre_df = df
        self._period_col = period_col
        self._period_freq = period_freq
        self._filter_not_completed_period = filter_not_completed_period

        self._doSetupInfo()

    """
    def __iter__(self):
        return
    """

    def _doSetupInfo(self):
        period_grouper = pd.Grouper(key=self._period_col, freq=self._period_freq, origin="start")
        df_groupby = self._pre_df.groupby(period_grouper)
        #self._period_list = df_groupby.indices
        period_list = df_groupby.indices

        """
        self._period_list = [period for period in period_list if PandasDataFrameHelper.analyzeNums4Rows(df_groupby) == 168]
        """
        for period_name in period_list:
            periodly_df = df_groupby.get_group(period_name)
            rows = PandasDataFrameHelper.analyzeNums4Rows(periodly_df)
            if rows == 168:
                self._period_list.append(period_name)
                self._period_df_dict[period_name] = periodly_df
                print(CryptoDatadownloadBinaceCsvDataParser.parseCsv2ClosePriceNumpy(periodly_df))
                self._period_numpy_dict[period_name] = CryptoDatadownloadBinaceCsvDataParser.parseCsv2ClosePriceNumpy(periodly_df)
                self._period_numpy_dict[period_name].reverse() #實測periodly_df會被反賺順序 ==> 不對，之前本來就是轉換後反晚?

        print("_pre_df : ")
        print(self._pre_df)

    def getPeriodList(self):
        return self._period_list

    def getPeriodNumpyDict(self):
        return self._period_numpy_dict

    def getPeriodDataFrameDict(self):
        return self._period_df_dict

    def getPeriodNumpyList(self):
        return self._period_numpy_dict.values()
# ========================================================= 以上 轉換 =========================================================


# ========================================================= 以下 一些財經相關的算式(?)的methods =========================================================
class FinanceHelper:

    @staticmethod
    def countSampleReturn(now_price, pre_price):
        return (now_price - pre_price) / pre_price
# ========================================================= 以上 一些財經相關的算式(?)的methods =========================================================
