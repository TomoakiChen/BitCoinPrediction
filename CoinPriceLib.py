import pandas as pd
from datetime import date as DateUtils
from datetime import datetime as DateTimeUtils
# df = pd.read_csv('https://www.cryptodatadownload.com/cdd/Binance_BTCUSDT_d.csv')
# print(df[0])
import urllib


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

    def getDailyClosedPriceNumpy(self):
        df = self.getDailyDataFrame(["date", "close"])
        daily_closed_price_info_list = CryptoDatadownloadBinaceCsvDataParser.parseCsv2ClosePriceNumpy(df)
        return daily_closed_price_info_list

    def getDailyClosedPriceChangNumpy(self):
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


    def getHourlyClosedPriceNumpy(self):
        df = self.getHourlyDataFrame(["date", "close"])
        hourly_closed_price_info_list = CryptoDatadownloadBinaceCsvDataParser.parseCsv2ClosePriceNumpy(df)
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


# ========================================================= 以下 輔佐將 csv data 轉換 =========================================================
class CryptoDatadownloadBinaceCsvDataParser:

    @staticmethod
    def parseCsv2ClosePriceNumpy(df):
        periodly_closed_price_info_list = []
        periodly_closed_price_list = df.to_numpy()
        for periodly_closed_price in periodly_closed_price_list:
            periodly_closed_price_info = []

            period_label = periodly_closed_price[0]

            price = periodly_closed_price[1]

            periodly_closed_price_info = [period_label, price]
            periodly_closed_price_info_list.append(periodly_closed_price_info)

        periodly_closed_price_info_list.reverse()
        return periodly_closed_price_info_list

    @staticmethod
    def parseDateInfo(str_date_time):
        if str_date_time.__contains__('AM') or str_date_time.__contains__('PM'):
            date_time = DateTimeUtils.strptime(str_date_time, "%Y-%m-%d %I-%p")
        else:
            date_time = pd.to_datetime(str_date_time) # DateTimeUtils.strptime("%Y-%m-%d %H:%M:%S", str_date_time)
        return date_time
# ========================================================= 以上 輔佐將 csv data 轉換 =========================================================


# ========================================================= 以下 一些財經相關的算式(?)的methods =========================================================
class FinanceHelper:

    @staticmethod
    def countSampleReturn(now_price, pre_price):
        return (now_price - pre_price) / pre_price
# ========================================================= 以上 一些財經相關的算式(?)的methods =========================================================
