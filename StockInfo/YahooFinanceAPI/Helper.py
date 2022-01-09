from datetime import timedelta as TimeDelta

class yfinaceHelper:

    @staticmethod
    def reindexHourlyDataFrame(hourly_yfinace_df):
        timedelta = TimeDelta(minutes=30)
        hourly_yfinace_df.index = hourly_yfinace_df.index+timedelta
        return hourly_yfinace_df
