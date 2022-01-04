import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from CoinPriceLib import CryptoDatadownloadBinaceClient, CryptoDatadownloadBinaceCsvDataParser, PeriodlyCoinPriceInfo
from PandasHelper import PandasDataFrameHelper

plt.style.available
plt.style.use('seaborn')

fig, ax = plt.subplots()
ax.margins(0.05) # Optional, just adds 5% padding to the autoscaling

client = CryptoDatadownloadBinaceClient()

hourly_df = client.getHourlyDataFrame(desig_col_list=["date", "close"])
mean_noarmalzied_df = PandasDataFrameHelper.processDataNormalizationByMean(hourly_df, ["close"])

mean_normal_pcpi = PeriodlyCoinPriceInfo(mean_noarmalzied_df)
for period in mean_normal_pcpi.getPeriodList():
    ax.plot(list(range(0,168)), mean_normal_pcpi.getPeriodPericeListDict().get(period), label=period)


print("draw plt")
plt.title("Bitcoin Pre-Processed Dataset")
plt.ylabel("Price $")
plt.xlabel("7D (168hrs)")
plt.xticks(range(0,169,24))
plt.show()
