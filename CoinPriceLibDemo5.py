import pandas as pd
from CoinPriceLib import CryptoDatadownloadBinaceClient, CryptoDatadownloadBinaceCsvDataParser, PeriodlyCoinPriceInfo
from PandasHelper import PandasDataFrameHelper

client = CryptoDatadownloadBinaceClient()

hourly_df = client.getHourlyDataFrame(desig_col_list=["date", "close"])
# hourly_df = client.getHourlyDataFrame4Test()
# close_df = hourly_df["close"]
# print(close_df.mean())
maxmin_noarmalzied_df = PandasDataFrameHelper.processDataNormalizationByMaxMin(hourly_df, ["close"])
# print(maxmin_noarmalzied_df)

mean_noarmalzied_df = PandasDataFrameHelper.processDataNormalizationByMean(hourly_df, ["close"])
# print(mean_noarmalzied_df)


maxmin_normal_pcpi = PeriodlyCoinPriceInfo(maxmin_noarmalzied_df)
mean_normal_pcpi = PeriodlyCoinPriceInfo(mean_noarmalzied_df)


"""
print("maxmin_normal_pcpi：")
for period in maxmin_normal_pcpi.getPeriodList():
    print(period)
    # df = maxmin_normal_pcpi.getPeriodDataFrameDict()[period]
    # print(df)
    numpy = maxmin_normal_pcpi.getPeriodNumpyDict()[period]
    print(numpy)
    print("==========================================================================================")

print("**********************************************************************************************")
print("mean_normal_pcpi：")
for period in mean_normal_pcpi.getPeriodList():
    print(period)
    # df = mean_normal_pcpi.getPeriodDataFrameDict()[period]
    # print(df)
    numpy = maxmin_normal_pcpi.getPeriodNumpyDict()[period]
    print(numpy)
    print("==========================================================================================")
"""
print(maxmin_normal_pcpi.getAllPriceList())
