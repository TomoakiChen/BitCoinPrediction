# -*- coding: utf-8 -*-
from PyWeb import HtmlClient
from NewsInfo import NewsInfo
class LTNClient:
    def __init__(self, html_client = None):
        self._html_client = html_client
    def _setupHtmlClient(html_client):
        self._html_client = HtmlClient()
# --------------------------------- 以下是 自由時報格式 ---------------------------------
news_info_list = []
url = 'https://news.ltn.com.tw/topic/%E6%AF%94%E7%89%B9%E5%B9%A3'
if(html)
html_client = HtmlClient()
html_parsed_data = html_client.getHtml(url)
#print(parsed_data)

# data-desc='新聞列表' > class='searchlist' > li
news_list = html_parsed_data.find(class_='searchlist').findAll('li') #新聞(標題)清單
for news in news_list:
    news_info = NewsInfo()
    links = news.findAll('a')
    #print(links)

    #print(links[1].href).setTitle())
    news_info.setLink(links[1]['href']) #新聞連結
    news_info.setTitle(links[1].find('h3').getText()) #新聞標題
    print(news_info)
# --------------------------------- 以上是 自由時報格式 ---------------------------------
