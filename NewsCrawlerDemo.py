from NewsCrawler import LTNNewsClient, YahooNewsClient, cnYESNewsClient, MoneyUdnNewsClient, NewsCrawler, BitCoinComNewsClient
from datetime import datetime, date
from PandasHelper import PandasDataFrameHelper
from NewsInfo import NewsInfoHelper

# sources = ["LTN", "cnYES", "MoneyUdn", "Bitcoin.com"]
# sources = ["LTN", "cnYES", "Bitcoin.com"]
sources = ["cnYES", "MoneyUdn"]
start = datetime.now()
crawler = NewsCrawler(news_sources=sources)
since_date = date.fromisoformat('2021-11-01')
news_list = crawler.findBySinceDate(since_date)
end = datetime.now()

# for news in news_list:
#     print(news)
# print("total nums = ", len(news_list))
# print("cost = ", (end - start))
df = NewsInfoHelper.parseInfoList2DataFrame(news_list, desig_col_list=["pubDateTime", "title"])
print(df)
# PandasDataFrameHelper.parseObjectList2DataFrame(news_list)

# --------------------------------- 以下是 自由時報格式 ---------------------------------
"""
start = datetime.now()
ltn_client = LTNNewsClient()

#ltn_news_list = ltn_client.findByMaxPages()
since_date = date.fromisoformat('2021-01-01')
ltn_news_list = ltn_client.findBySinceDate(since_date)
end = datetime.now()

#print(ltn_news_list)
for ltn_news in ltn_news_list:
    print(ltn_news)
print("total nums = ", len(ltn_news_list))
print("cost = ", (end - start))
"""
# --------------------------------- 以上是 自由時報格式 ---------------------------------

# --------------------------------- 以下是 Yahoo 新聞 ---------------------------------
"""
start = datetime.now()
yahoo_news_client = YahooNewsClient(headless=True)

news_list = yahoo_news_client.findByMaxPages(max_pages=3)
end = datetime.now()

for news in news_list:
    print(news)
print("total nums = ", len(news_list))
print("cost = ", (end - start))
"""
# --------------------------------- 以上是 Yahoo 新聞 ---------------------------------


# --------------------------------- 以下是 鉅亨網 ---------------------------------
"""
start = datetime.now()
cnYES_news_client = cnYESNewsClient(headless=True)

# news_list = cnYES_news_client.findByMaxPages(max_pages=10)

since_date = date.fromisoformat('2021-10-01')
news_list = cnYES_news_client.findBySinceDate(since_date=since_date)

end = datetime.now()

for news in news_list:
    print(news)
print("total nums = ", len(news_list))
print("cost = ", (end - start))
"""
# --------------------------------- 以上是 鉅亨網 ---------------------------------



# --------------------------------- 以下是 經濟日報 ---------------------------------
"""
start = datetime.now()
money_udn_news_client = MoneyUdnNewsClient(headless=True)

# news_list = money_udn_news_client.findByMaxPages(max_pages=10)

since_date = date.fromisoformat('2021-10-01')
news_list = money_udn_news_client.findBySinceDate(since_date=since_date)

end = datetime.now()

for news in news_list:
    print(news)
print("total nums = ", len(news_list))
print("cost = ", (end - start))
"""
# --------------------------------- 以上是 經濟日報 ---------------------------------


# --------------------------------- 以下是 Bitcoin.com ---------------------------------
"""
start = datetime.now()
bitconin_com_client = BitCoinComNewsClient()

# news_list = bitconin_com_client.findByMaxPages(max_pages=1)

since_date = date.fromisoformat('2021-10-01')
news_list = bitconin_com_client.findBySinceDate(since_date)
end = datetime.now()

#print(ltn_news_list)
for news in news_list:
    print(news)
print("total nums = ", len(news_list))
print("cost = ", (end - start))
"""
# --------------------------------- 以上是 Bitcoin.com ---------------------------------
