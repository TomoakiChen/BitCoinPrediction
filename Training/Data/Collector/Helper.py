import pandas as pd

class GoldAPIPriceInfoHelper:

    @staticmethod
    def parse2HourlyDataFrame(df_daily, replace_columns):
        df_daily.index = pd.to_datetime(df_daily["date"])
        df_hourly = df_daily.resample("H").fillna("pad")
        df_hourly.rename(columns=replace_columns, inplace=True)
        print(df_hourly)
