import pandas as pd
import urllib
from datetime import date as Date, datetime as DateTime, timedelta
from PandasHelper import PandasDataFrameHelper
import numpy
from AkiPyUtil.AkiPyDateTime import AkiDateTimeUtil



# ========================================================= 以下輔佐對 CryptoDatadownloadBinace 資料的操作
class CrpytoDatadownloadBinanceDataHelper:
    @staticmethod
    def filteringDateRange(df, since, until):
        if since == None and until == None:
            return df
        elif since != None and until == None:
            if isinstance(since, Date) or isinstance(since, DateTime):
                since = pd.to_datetime(since)
            return df[(df['date'] >= since)]
        elif since == None and until != None:
            if isinstance(until, Date) or isinstance(until, DateTime):
                if isinstance(until, Date):
                    until = DateTime.combine(until, DateTime.max.time())
                until = pd.to_datetime(until)
            return df[(df['date'] <= until)]
        else:
            if isinstance(since, Date) or isinstance(since, DateTime):
                since = pd.to_datetime(since)
            if isinstance(until, Date) or isinstance(until, DateTime):
                if isinstance(until, Date):
                    until = DateTime.combine(until, DateTime.max.time())               
                until = pd.to_datetime(until)
            return df[(df['date'] >= since) & (df['date'] <= until)]

    @staticmethod
    def sortingDate(df, sort_by_date, asc_by_date):
        if sort_by_date == True:
            df = df.sort_values(by="date", ascending=asc_by_date, ignore_index=True)
        return df


    @staticmethod
    def fillingMissingData(df, abs_desig_timedelta, fill_in_method='linear'):
        since = df["date"][0]
        until = df["date"][len(df)-1]
        asc_by_date = None
        if until >= since:
            asc_by_date = True
        else:
            asc_by_date = False

        desig_datetime = since
        while(desig_datetime <= until):
            data = df[df["date"] == desig_datetime]
            if data.empty == True:
                # print("missing data for date= " + str(desig_datetime) )
                new_data_4_df = pd.Series({"date": desig_datetime, "close": None})
                df = df.append(new_data_4_df, ignore_index=True)
            else:
                nums_of_data = len(data)
                if(nums_of_data >= 2):
                    # print("duplicate data for date(index=" + str(data.index) +  ") = " + str(desig_datetime) + " nums = " +  str(nums_of_data))
                    # print(data)
                    mean_data = data.mean(numeric_only=None)
                    new_data_4_df = pd.Series({"date": desig_datetime, "close": mean_data["close"]})
                    df = df.drop(data.index)
                    df = df.append(new_data_4_df, ignore_index=True)
            if asc_by_date:
                desig_datetime = desig_datetime + abs_desig_timedelta
            else:
                desig_datetime = desig_datetime - abs_desig_timedelta

        df = CrpytoDatadownloadBinanceDataHelper.sortingDate(df, True, asc_by_date)

        if fill_in_method != None:
            df["close"].interpolate(method=fill_in_method, inplace=True)
            # df.astype(float).interpolate(method=fill_in_method, inplace=True)
        return df
# ========================================================= 以上輔佐對 CryptoDatadownloadBinace 資料的操作



# ========================================================= 以下 輔佐將 csv data 轉換 =========================================================
class CryptoDatadownloadBinaceCsvDataParser:

    """
    numpy 覺得就是該單欄資料(暫時限close資料狀況下)
    """
    @staticmethod
    def parseCsv2PeriodlyClosedPriceList(df):
        periodly_closed_price_info_list = []
        periodly_closed_price_list = df.to_numpy()
        for periodly_closed_price in periodly_closed_price_list:
            periodly_closed_price_info = []

            period_label = periodly_closed_price[0]

            price = periodly_closed_price[1]

            # periodly_closed_price_info = [period_label, price]
            periodly_closed_price_info = price # 跟下面那隻同 parseCsv2ClosedPriceNumpy，因為覺得list的時候，日期時間無意義
            periodly_closed_price_info_list.append(periodly_closed_price_info)

        periodly_closed_price_info_list.reverse()
        return periodly_closed_price_info_list

    """
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
    """
    @staticmethod
    def parseDateInfo(str_date_time):
        if str_date_time.__contains__('AM') or str_date_time.__contains__('PM'):
            date_time = DateTime.strptime(str_date_time, "%Y-%m-%d %I-%p")
        else:
            date_time = pd.to_datetime(str_date_time) # DateTime.strptime("%Y-%m-%d %H:%M:%S", str_date_time)
        return date_time
# ========================================================= 以上 輔佐將 csv data 轉換 =========================================================



# ========================================================= 以下 利用指定區間將資料分組 =========================================================
class PeriodlyCoinPriceInfo:

    _period_col = None
    _period_freq = None
    _pre_df = None
    _filter_not_completed_period = None

    _period_list = []
    _period_df_dict = {}
    _period_price_list_dict = {}

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
                # print(CryptoDatadownloadBinaceCsvDataParser.parseCsv2PeriodlyClosedPriceList(periodly_df))
                self._period_price_list_dict[period_name] = CryptoDatadownloadBinaceCsvDataParser.parseCsv2PeriodlyClosedPriceList(periodly_df)
                self._period_price_list_dict[period_name].reverse() #實測periodly_df會被反賺順序 ==> 不對，之前本來就是轉換後反晚?

        # print("_pre_df : ")
        # print(self._pre_df)

    def getPeriodList(self):
        return self._period_list

    def getPeriodPericeListDict(self):
        return self._period_price_list_dict

    def getPeriodDataFrameDict(self):
        return self._period_df_dict

    def getAllPriceList(self):
        return list(self._period_price_list_dict.values())
# ========================================================= 以上 利用指定區間將資料分組 =========================================================



# ========================================================= 以下 一些財經相關的算式(?)的methods =========================================================
class FinanceHelper:

    @staticmethod
    def countSampleReturn(now_price, pre_price):
        return (now_price - pre_price) / pre_price
# ========================================================= 以上 一些財經相關的算式(?)的methods =========================================================
