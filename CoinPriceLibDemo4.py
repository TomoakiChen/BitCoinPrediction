import pandas as pd
from CoinPriceLib import CryptoDatadownloadBinaceClient, CryptoDatadownloadBinaceCsvDataParser, PeriodlyCoinPriceInfo

client = CryptoDatadownloadBinaceClient()

hourly_df = client.getHourlyDataFrame(desig_col_list=["date", "close"])

"""
# 印出觀察
seven_days_grouper = pd.Grouper(key="date", freq="7D")
grouped_hourly_df = hourly_df.groupby(seven_days_grouper)

counter = 0
indices = grouped_hourly_df.indices
group_names = indices.keys()

for group_name in group_names:
    counter+=1
    if counter > 3:
        break


    group_df = grouped_hourly_df.get_group(group_name)
    print("Rows = " + str(PandasDataFrameHelper.analyzeNums4Rows(group_df)) )
    print(group_df)
    print("==============================================================")
"""

pcpi = PeriodlyCoinPriceInfo(hourly_df)
period_list = pcpi.getPeriodList()
numpy_dict = pcpi.getPeriodNumpyDict()
df_dict = pcpi.getPeriodDataFrameDict()

"""
period = period_list[-1]
print(period)
print(numpy_dict[period])
"""
for period in period_list:
    df = df_dict[period]
    print(period)
    print(df)
    print("============================================")
