from CoinPriceLib import CryptoDatadownloadBinaceClient, CryptoDatadownloadBinaceCsvDataParser
import pandas as pd

client = CryptoDatadownloadBinaceClient()


hourly_df = pd.DataFrame({
    "date" : ["2021-11-12 13:00:00", "2021-11-12 12:00", "2021-11-11 07:00", "2021-10-01 08:00"],
    "close" : [10000, 20000, 30000, 100]
})
hourly_df["date"] = CryptoDatadownloadBinaceCsvDataParser.parseDateInfo(hourly_df["date"])

#hourly_df = client.getHourlyDataFrame(desig_col_list=["date", "close"])

#print(hourly_df)
grouper = pd.Grouper(key="date", freq="7D")
grouped_hourly_df = hourly_df.groupby(grouper)

# print(grouped_hourly_df.mean())

groups = grouped_hourly_df.groups
indices = grouped_hourly_df.indices
print(type(groups)) # dict
print(type(indices)) # defaultdict

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

print(groups.keys())
print(groups.values())

print(indices.keys())
print(indices.values())
