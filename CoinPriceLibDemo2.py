import pandas as pd
from CoinPriceLib import CryptoDatadownloadBinaceClient, CryptoDatadownloadBinaceCsvDataParser
from PandasHelper import PandasDataFrameHelper

client = CryptoDatadownloadBinaceClient()


# hourly_df = client.getHourlyDataFrame4Test()
hourly_df = client.getHourlyDataFrame(desig_col_list=["date", "close"])

#print(hourly_df)
grouper = pd.Grouper(key="date", freq="7D")
grouped_hourly_df = hourly_df.groupby(grouper)

# print(grouped_hourly_df.mean())

groups = grouped_hourly_df.groups
indices = grouped_hourly_df.indices

"""
# ==================================================== 以下印出 groups、indices 的屬性 ====================================================
print(type(groups)) # dict
print(type(indices)) # defaultdict

print(groups.keys())
print(groups.values())

print(indices.keys())
print(indices.values())
# ==================================================== 以上印出 groups、indices 的屬性 ====================================================
"""

"""
for group, indice in zip(groups, indices):
    print(group)
    print(indice)
    if True:
        break
"""

"""
for group in groups:
    print("group = " + str(group) + " ,type = " + str(type(group)))
    if True:
        break
"""


"""
group_names = groups.keys()
print(type(group_names))

for group_name in group_names:
    # group_df = grouped_hourly_df[group_name]
    group_df = grouped_hourly_df.get_group(group_name)
    print(group_df)
"""

group_names = indices.keys()
print(type(group_names))

for group_name in group_names:
    # group_df = grouped_hourly_df[group_name] 用錯成這個會顯示 object is not subscriptable
    group_df = grouped_hourly_df.get_group(group_name)
    print("type = " + str( type(group_df) ) )
    print("size = " + str(group_df.size) )
    print("shape = " + str(group_df.shape) )
    print("Rows = " + str(PandasDataFrameHelper.analyzeNums4Rows(group_df)) )
    print(group_df)
    print("==============================================================")
