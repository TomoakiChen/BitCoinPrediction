from CoinPriceLib import CryptoDatadownloadBinaceClient
import pandas as pd

client = CryptoDatadownloadBinaceClient()

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
data_closed_price_list = client.getDailyClosedPriceList()
print(data_closed_price_list)
"""

""""
daily_price_changed_info_list = client.getDailyClosedPriceChangeList()
print(daily_price_changed_info_list[:])
"""

"""
hourly_price_info_list = client.getHourlyClosedPriceList()
print(hourly_price_info_list)
"""

hourly_price_changed_info_list = client.getHourlyClosedPriceChangeList()
print(hourly_price_changed_info_list)
