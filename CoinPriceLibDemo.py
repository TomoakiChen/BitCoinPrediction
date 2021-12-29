from CoinPriceLib import CryptoDatadownloadBinaceClient, CrpytoDatadownloadBinanceDataHelper
import pandas as pd
from datetime import datetime, timedelta

def tryFindNoData(df, timedelta):
    since = df["date"][0]
    until = df["date"][len(df)-1]
    now = since
    while(now <= until):
        data = df[df["date"] == now]
        if data.empty == True:
            # print("missing data for date = " + str(now) )
            new_data_4_df = pd.Series({"date": now, "close": None})
            df = df.append(new_data_4_df, ignore_index=True)
        else:
            nums_of_data = len(data)
            if(nums_of_data >= 2):
                # print("duplicate data for date = " + str(now) + " nums = " +  str(nums_of_data))
                # print(data)
                mean_data = data.mean(numeric_only=None)
                new_data_4_df = pd.Series({"date": now, "close": mean_data["close"]})
                df = df.drop(list(data.index) )
                df = df.append(new_data_4_df, ignore_index=True)
        now = now + timedelta
    print(df)
    print(CrpytoDatadownloadBinanceDataHelper.filteringDateRange(df, datetime.fromisoformat('2020-11-20 07:00:00'), datetime.fromisoformat('2020-11-20 07:00:00') ))

client = CryptoDatadownloadBinaceClient()

df = client.getHourlyDataFrame(desig_col_list=["date", "close"])
hourly_time_delta = timedelta(hours=1)
# print(df)
# print(df["date"][0])
# print(df[df["date"] == datetime.fromisoformat("2021-12-10 00:00:00")])
# tryFindNoData(df, hourly_time_delta)

print(df[df["date"] == datetime.fromisoformat("2020-11-30 06:00:00")])
print(df[df["date"] == datetime.fromisoformat("2020-11-20 07:00:00")])
df = CrpytoDatadownloadBinanceDataHelper.fillingMissingData(df, hourly_time_delta)
# print(df)
print(df[df["date"] == datetime.fromisoformat("2020-11-30 06:00:00")])
print(df[df["date"] == datetime.fromisoformat("2020-11-20 07:00:00")])
# df.to_csv(path_or_buf='./Price.csv', index=False)

# df = CrpytoDatadownloadBinanceDataHelper.fillEmpty(df, 'pad')
# print(df)

"""
df = client.getDailyDataFrame()
df_date = df["date"]
df_close = df["close"]
df_new = pd.DataFrame()
df_new = df_new.add(df_date, axis = "date") # 不行
df_new = df_new.add(df_close, axis = "close") # 不行
print(df_new)
"""

"""
df = client.getDailyDataFrame()
df_new = df[["date", "close"]]
print(df_new)
"""

"""
df = client.getDailyDataFrame(desig_col_list=["date", "close"])
print(df)
"""

"""
df = client.getDailyDataFrame(desig_col_list=["date", "close"])
df["date"] = pd.to_datetime(df["date"])
print(df)
"""

"""
data_closed_price_list = client.getDailyClosedPriceNumpy()
print(data_closed_price_list)
"""

""""
daily_price_changed_info_list = client.getDailyClosedPriceChangeNumpy()
print(daily_price_changed_info_list[:])
"""


"""
hourly_price_info_list = client.getHourlyClosedPriceList()
print(hourly_price_info_list)
"""

"""
hourly_price_changed_info_list = client.getHourlyClosedPriceChangeNumpy()
print(hourly_price_changed_info_list)
"""
