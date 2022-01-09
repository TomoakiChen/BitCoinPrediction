import yfinance
import pandas as pd
from datetime import datetime as DateTime, date as Date, timedelta as TimeDelta
from dateutil.relativedelta  import relativedelta as RelativeDelta
from pytz import timezone as TimeZone, all_timezones

from AkiPyUtil.AkiPyDateTime import AkiDateTimeUtil
from StockInfo.YahooFinanceAPI.Helper import *


class yfinanceExClient:

    __market_rest_date_dict = {
        "2020-01-01": "2019-12-31"
    }

    # __2y_time_delta= TimeDelta(years=2)

    __limit_since_date= Date

    def __init__(self):
        time_delta_4_2y = RelativeDelta(years=2)
        today = Date.today()
        self.__limit_since_date = today - time_delta_4_2y
        # self.__limit_since_datetime = AkiDateTimeUtil.obtainFirstTimeOfDate(self.__limit_since_date)

    # def __count2YLimit(self):
    #     pass

    # # 超過2y的需要
    # def __splitDailyPeriod(self):
    #     pass

    def __obtainSearchSinceDateTime(self, desig_date, time_zone):
        if desig_date == None:
            return None
        since_datetime = AkiDateTimeUtil.obtainFirstTimeOfDate(desig_date)
        since_datetime = time_zone.localize(since_datetime)
        return since_datetime

    def __obtainSearchUntilDateTime(self, desig_date, time_zone):
        if desig_date == None:
            return None
        until_datetime = AkiDateTimeUtil.obtainLastTimeOfDate(desig_date)
        until_datetime = time_zone.localize(until_datetime)
        return until_datetime

    def __solveMissingData4LastDateProblem(self, df_result, until):
        until_datetime = AkiDateTimeUtil.obtainLastTimeOfDate(until)
        df_lastdate = df_result[df_result.index == pd.to_datetime(until_datetime)]
        dict_empty_data = dict()
        if df_lastdate.empty:
            for col in list(df_lastdate.columns):
                dict_empty_data[col] = None
            df_lastdate = pd.DataFrame(dict_empty_data, index=[pd.to_datetime(until_datetime)])
            df_result = pd.concat([df_result, df_lastdate])
        # print(df_result)
        return df_result

    def __solveMissingData4MarketRestProblem(self, df_result, stock_symbol, col_list, time_zone):
        print("[yfinanceExClient] __solveMissingData4MarketRestProblem(): ")
        market_rest_date_list = list(self.__market_rest_date_dict.keys())
        df_missing_list = list()
        df_missing_list.append(df_result)
        for rest_date in market_rest_date_list:
            fixed_date = self.__market_rest_date_dict[rest_date]
            start_datetime = self.__obtainSearchSinceDateTime(fixed_date, time_zone)
            end_datetime = self.__obtainSearchSinceDateTime(fixed_date, time_zone) + TimeDelta(days=1)
            df_missing = yfinance.download(stock_symbol, start=start_datetime, end=end_datetime, interval = "1d")
            df_missing  = df_missing[col_list]
            rest_datetime = pd.to_datetime(rest_date)
            print(df_missing.index)
            print([rest_datetime])
            df_missing.index = [rest_datetime]
            df_missing_list.append(df_missing)
        df_result = pd.concat(df_missing_list)
        return df_result

    def __solveSinceMoreProblem(self, df_result, since):
        since_datetime = AkiDateTimeUtil.obtainFirstTimeOfDate(since)
        return df_result[(df_result.index >= pd.to_datetime(str(since_datetime)))]


    def __obtainOverRangeDailyDataFrame(self, stock_symbol, col_list, since_datetime, limit_since_datetime, time_zone):
        overrange_since_datetime = since_datetime
        overrange_until_datetime = self.__obtainSearchUntilDateTime(self.__limit_since_date, time_zone)
        print("[yfinanceExClient] getHourlyData(): limit_since_datetime=%s, overrange_since_datetime= %s, overrange_until_datetime= %s"
             % (limit_since_datetime, overrange_since_datetime, overrange_until_datetime))

        df_daily_overrange = yfinance.download(stock_symbol, start=overrange_since_datetime, end=overrange_until_datetime, interval = "1d")
        df_daily_overrange = df_daily_overrange[col_list]
        return df_daily_overrange

    def __obtainTwoYearsHourlyDataFrame(self, stock_symbol, col_list):
        df_hourly_2y = yfinance.download(stock_symbol, period="2y", interval = "1h")

        df_hourly_2y = df_hourly_2y[col_list]
        new_index_list = [pd.to_datetime(str(the_index).replace('-05:00', '').replace('-04:00', '')) for the_index in df_hourly_2y.index]
        df_hourly_2y.index = new_index_list
        df_hourly_2y = yfinaceHelper.reindexHourlyDataFrame(df_hourly_2y)
        return df_hourly_2y



    def getHourlyDataFrame(self, stock_symbol, since=Date.fromisoformat("2020-01-01"), until=Date.today(), time_zone=TimeZone("US/Eastern"), col_list=["Close"]):
        since_datetime = self.__obtainSearchSinceDateTime(since, time_zone)
        until_datetime = self.__obtainSearchUntilDateTime(until, time_zone)
        limit_since_datetime = self.__obtainSearchSinceDateTime(self.__limit_since_date, time_zone)
        if limit_since_datetime > since_datetime:
            df_daily_overrange = self.__obtainOverRangeDailyDataFrame(stock_symbol, col_list, since_datetime, limit_since_datetime, time_zone)
            df_hourly_2y = self.__obtainTwoYearsHourlyDataFrame(stock_symbol, col_list)
            df_result = pd.concat([df_daily_overrange, df_hourly_2y])
            df_result = self.__solveMissingData4LastDateProblem(df_result, until)
            df_result = self.__solveMissingData4MarketRestProblem(df_result, stock_symbol, col_list, time_zone)
            df_result = df_result.resample('H').fillna('pad')
            df_result = self.__solveSinceMoreProblem(df_result, since)
            # df_result["date"] = df_result.index
        else:
            df_range = yfinance.download(stock_symbol, start=overrange_since_datetime, end=overrange_until_datetime, interval="1h")
            df_result = df_range[col_list]

        return df_result

    # def getHourlyData(self, stock_symbol, since=Date.fromisoformat("2020-01-01"), until=Date.today(), time_zone=TimeZone("US/Eastern"), col_list=["Close"]):
    #     since_datetime = self.__obtainSearchSinceDateTime(since, time_zone)
    #     until_datetime = self.__obtainSearchUntilDateTime(until, time_zone)
    #     limit_since_datetime = self.__obtainSearchSinceDateTime(self.__limit_since_date, time_zone)
    #     if limit_since_datetime > since_datetime:
    #         overrange_since_datetime = since_datetime
    #         overrange_until_datetime = self.__obtainSearchUntilDateTime(self.__limit_since_date, time_zone)
    #         print("[yfinanceExClient] getHourlyData(): limit_since_datetime=%s, overrange_since_datetime= %s, overrange_until_datetime= %s"
    #              % (limit_since_datetime, overrange_since_datetime, overrange_until_datetime))
    #
    #         # print( yfinance.download(stock_symbol, start="2019-12-31", end="2020-01-02", interval = "1d"))
    #
    #         df_daily_overrange = yfinance.download(stock_symbol, start=overrange_since_datetime, end=overrange_until_datetime, interval = "1d")
    #         df_hourly_2y = yfinance.download(stock_symbol, period="2y", interval = "1h")
    #
    #         df_daily_overrange = df_daily_overrange[col_list]
    #
    #         df_hourly_2y = df_hourly_2y[col_list]
    #         new_index_list = [pd.to_datetime(str(the_index).replace('-05:00', '').replace('-04:00', '')) for the_index in df_hourly_2y.index]
    #         df_hourly_2y.index = new_index_list
    #         df_hourly_2y = yfinaceHelper.reindexHourlyDataFrame(df_hourly_2y)
    #
    #
    #         df_result = pd.concat([df_daily_overrange, df_hourly_2y])
    #         df_result = self.__solveMissingData4LastDateProblem(df_result, until)
    #         self.__solveMissingData4MarketRestProblem(df_result)
    #         df_result = df_result.resample('H').fillna('pad')
    #         df_result = self.__solveSinceMoreProblem(df_result, since)
    #         # df_result["date"] = df_result.index
    #     else:
    #         df_range = yfinance.download(stock_symbol, start=overrange_since_datetime, end=overrange_until_datetime, interval="1h")
    #         df_result = df_range[col_list]
    #
    #     return df_result
