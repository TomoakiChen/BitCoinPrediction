import pandas as pd
from datetime import date as DateUtils
from datetime import datetime as DateTimeUtils
# df = pd.read_csv('https://www.cryptodatadownload.com/cdd/Binance_BTCUSDT_d.csv')
# print(df[0])


class CryptoDatadownloadBinaceClient:

    __url_dict = {
        'Daily': 'https://www.cryptodatadownload.com/cdd/Binance_BTCUSDT_d.csv',
        'Hourly': 'https://www.cryptodatadownload.com/cdd/Binance_BTCUSDT_1h.csv',
        'Minute': 'https://www.cryptodatadownload.com/cdd/Binance_BTCUSDT_minute.csv'
    }

    def __init__(self):
        pass

    # ==================================================== 以下是 csv初始的 DataFrame 格式 ====================================================
    def getDailyDataFrame(self, desig_col_list=None):
        # 第一行是 CryptoDatadownload 的標註
        df = pd.read_csv(self.__url_dict.get('Daily'), header=1)
        if desig_col_list == None:
            return df
        else:
            return df[desig_col_list]

    def getHourlyDataFrame(self, desig_col_list=None):
        df = pd.read_csv(self.__url_dict.get('Hourly'), header=1)
        if desig_col_list == None:
            return df
        else:
            return df[desig_col_list]
    # ==================================================== 以上是 csv初始的 DataFrame 格式 ====================================================

    def getDailyClosedPriceList(self):
        df = self.getDailyDataFrame(["date", "close"])
        daily_closed_price_info_list = []
        daily_closed_price_list = df.to_numpy()
        for daily_closed_price in daily_closed_price_list:
            daily_closed_price_info = []

            str_date = daily_closed_price[0].replace(' 00:00:00', '')
            date = DateUtils.fromisoformat(str_date)

            price = daily_closed_price[1]
            # print("date= ", str_date, ", price= ", str_price)
            # print(type(str_date), ", ",type(price))
            daily_price_info = [date, price]
            daily_closed_price_info_list.append(daily_price_info)

        daily_closed_price_info_list.reverse()
        return daily_closed_price_info_list

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


    def getHourlyClosedPriceList(self):
        hourly_closed_price_info_list = []

        df = self.getHourlyDataFrame(["date", "close"])
        hourly_closed_price_list = df.to_numpy()
        for hourly_closed_price in hourly_closed_price_list:
            hourly_closed_price_info = []

            str_date_time = hourly_closed_price[0] # .strip()
            if str_date_time.__contains__('AM') or str_date_time.__contains__('PM'):
                date_time = DateTimeUtils.strptime(str_date_time, "%Y-%m-%d %I-%p")
            else:
                date_time = pd.to_datetime(str_date_time) # DateTimeUtils.strptime("%Y-%m-%d %H:%M:%S", str_date_time)

            price = hourly_closed_price[1]
            hourly_price_info = [date_time, price]
            hourly_closed_price_info_list.append(hourly_price_info)

        hourly_closed_price_info_list.reverse()
        return hourly_closed_price_info_list

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

# 要拆出來比較要想，先暫時留著不實作
class CryptoDatadownloadBinaceCsvParser:

    @staticmethod
    def parseCsv(df_csv):
        pass


class FinanceHelper:

    @staticmethod
    def countSampleReturn(now_price, pre_price):
        return (now_price - pre_price) / pre_price
