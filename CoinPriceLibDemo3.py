import pandas as pd
from CoinPriceLib.Client import CryptoDatadownloadBinaceClient, CryptoDatadownloadBinaceCsvDataParser
from PandasHelper import PandasDataFrameHelper
from datetime import datetime as DateTime, date as Date

client = CryptoDatadownloadBinaceClient()

start = Date.fromisoformat("2022-01-01")
end = Date.fromisoformat("2022-01-06")
hourly_df = client.getHourlyDataFrame(desig_col_list=["date", "close"], since=start, until=end)
print(hourly_df)

# hourly_numpy = client.getHourlyClosedPriceNumpy()
# print(hourly_numpy)
