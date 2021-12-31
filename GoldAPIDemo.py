from MetalPrice.GoldAPI.Client import GoldAPIClient, GoldPriceClient
import ssl
import pandas as pd

ssl._create_default_https_context = ssl._create_unverified_context

# client = GoldAPIClient("goldapi-14sk9jtkxqaji16-io")
# # datas = client.getJsonStatus()
# datas = client.getJsonPrice("20211228")
# print(datas)

# df = pd.read_csv('./GoldPrice_2021-01-01-2021-12-28.csv')
# df.to_csv('./GoldPriceCache.csv', index=False)

# api_key = "goldapi-14sk9jtkxqaji16-io"
api_key = "goldapi-2rdpxtkxtumogz-io"
since = "2021-01-01"
until = "2021-12-28"
gold_price_client = GoldPriceClient(api_key)
df_price = gold_price_client.getGoldAPIPriceDataFrame(since=since, until=until)
print(df_price)
