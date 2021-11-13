import pandas as pd
from CoinPriceLib import CryptoDatadownloadBinaceClient, CryptoDatadownloadBinaceCsvDataParser
from PandasHelper import PandasDataFrameHelper

client = CryptoDatadownloadBinaceClient()

"""
hourly_df = client.getHourlyDataFrame(desig_col_list=["date", "close"])
hourly_numpy = CryptoDatadownloadBinaceCsvDataParser.parseCsv2ClosePriceInfo(hourly_df)
"""

hourly_numpy = client.getHourlyClosedPriceNumpy()
print(hourly_numpy)
