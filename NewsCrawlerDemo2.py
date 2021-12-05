"""
from NewsCrawler import LTNNewsClient, YahooNewsClient, cnYESNewsClient, MoneyUdnNewsClient, NewsCrawler, BitCoinComNewsClient, AkiDateTimeUtil
from datetime import datetime, date
from PandasHelper import PandasDataFrameHelper
from NewsInfo import NewsInfoHelper

since = datetime.fromisoformat('2021-11-01')
until = datetime.fromisoformat('2021-12-01')
now = datetime.now()
print(AkiDateTimeUtil.checkIsInInterval(now, since_date = since, until_date = until))
"""
from NewsCrawler import NewsCsvCrawler
from datetime import datetime, date
from PandasHelper import PandasDataFrameHelper
from NewsInfo import NewsInfoHelper

since_date = date.fromisoformat('2021-10-01')
news_csv_cralwer = NewsCsvCrawler()
news_csv_cralwer.save2Csv(since_date)
