from Training.Data.Collector.Helper import GoldAPIPriceInfoHelper
from MetalPrice.GoldAPI.Client import GoldPriceClient
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

api_key = "goldapi-2rdpxtkxtumogz-io"
gold_price_client = GoldPriceClient(api_key, cache_csv_path='./GoldPriceCache.csv')
df_daily_gold_price = gold_price_client.getGoldAPIPriceDataFrame(since="2020-01-01", desig_col_list=["date", "price"])

df_hourly_gold_price =  GoldAPIPriceInfoHelper.parse2HourlyDataFrame(df_daily_gold_price)
