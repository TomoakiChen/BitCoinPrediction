import pandas as pd
from pytz import timezone as TimeZone

def processPubDateTime4NewsDataFrame(ori_df, time_zone):
    new_df = ori_df
    new_df["pubDateTime"] = [time_zone.localize(pd.to_datetime(pub_date_time)) for pub_date_time in new_df["pubDateTime"].values]
    return new_df


tw_timezone = TimeZone("Asia/Taipei")
en_timezone = TimeZone('Europe/London')

df_news = pd.read_excel('./新聞_2021-01-01-2021-05-31.xlsx')
# df_news = pd.read_excel('./Training/Data/新聞_2021-01-01-2021-05-31.xlsx')
# df2 = df_news.loc(0:1)
"""
loc 和 iloc 的差異展示
df2 = df_news.loc[0:344]
print(df2)

df2 = df_news.iloc[0:344]
print(df2)
"""

"""
df_news_tw = df_news.loc[0:343]
# df_news_tw["pubDateTime"] = tw_timezone.localize(df_news_tw["pubDateTime"].values)
df_news_tw["pubDateTime"] = [tw_timezone.localize(pd.to_datetime(pub_date_time)) for pub_date_time in df_news_tw["pubDateTime"].values]
print(df_news_tw)

df_news_en = df_news.loc[344:]
print(df_news_en)
"""
df_news_tw = df_news.loc[0:343,:]
df_news_tw = processPubDateTime4NewsDataFrame(df_news_tw, tw_timezone)
print(df_news_tw)

df_news_en = df_news.loc[344:,:]
df_news_en = processPubDateTime4NewsDataFrame(df_news_en, en_timezone)
print(df_news_en)
