from NewsCrawler import LTNNewsClient, YahooNewsClient
from datetime import datetime, date

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

start = datetime.now()
yahoo_news_client = YahooNewsClient(headless=True)

news_list = yahoo_news_client.findByMaxPages(max_pages=3)
end = datetime.now()

for news in news_list:
    print(news)
print("total nums = ", len(news_list))
print("cost = ", (end - start))
