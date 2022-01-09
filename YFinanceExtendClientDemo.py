from StockInfo.YahooFinanceAPI.Client import yfinanceExClient
import pandas as pd

client = yfinanceExClient()
df = client.getHourlyData(stock_symbol="^IXIC")
print(df)
# print(df.index)
# df2 = df[(df.index >= pd.to_datetime("2020-01-01 00:00:00"))]
# print(df2)

# df2.to_csv('test.csv')
