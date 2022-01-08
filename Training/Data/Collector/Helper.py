import pandas as pd

class GoldAPIPriceInfoHelper:

    @staticmethod
    def parse2HourlyDataFrame(df_daily):
        df_daily.index = pd.to_datetime(df_daily["date"])
        df_hourly = df_daily.resample("H").fillna("pad")
        df_hourly.rename(columns={"price": "gold-price"}, inplace=True)
        print(df_hourly)
