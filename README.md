## 基本面資料
### 1. 比特幣價格
  * #### 所需準備
    * Python Dependency
      * 標準函示庫
        * datetime
        * urllib
      * 另需安裝函示庫
        * pandas
          ```shell
            pip install pandas
          ```
        * numpy
          ```shell
            pip install numpt
          ```
  * #### 使用方式
    * CryptoDatadownloadBinaceClient 抓幣安資料
      * 初始化參數
        無
      * getDailyDataFrame
      * getHourlyDataFrame
      * getDailyClosedPriceList
      * getHourlyClosedPriceList

## 市場面資料
### 1. GlassNode
  * 參考資料：[GlassNode APIs](https://docs.glassnode.com/basic-api/api) 

## 消息面資料
### 1. 新聞爬蟲
  * #### 所需準備
    * Python Dependency
      * 標準函示庫
        * datatime
        * urllib
      * 需另外安裝函示庫
        * selenium
          ```shell
            pip install selenium
          ```
    * 需下載 Web Driver，如專案內的 chromedriver.exe

* #### 目前支援的新聞網站
  * |新聞網站| 代碼 |獨立Client Class|備註|
    |--------|-----|----------|---------|
    |自由時報 |LTN|LTNNewsClient||
    |Yahoo新聞|Yahoo|YahooNewsClient|目前不支援 getBySinceDate()|
    |鉅亨網|cnYES|cnYESNewsClient||
    |經濟日報|MoneyUdn|MoneyUdnNewsClient||
    |Bitcoin.com|Bitcoin.com|BitCoinComNewsClient||



* #### 使用方式：
  * 一次爬很多網站 - NewsCrawler
    * 初始化參數：
      * news_sources ：網站代碼，即「目前支援的新聞網站」中的代碼。
    * findBySinceDate(since_date)：
      參數：
      * since_date：**預設為今日**，爬蟲將會爬此日期之後的所有新聞
        ```Python
        # 要搜尋那些站，此例子會查詢 Bitcoin.com 、自由時報這幾個網站
        crawler = NewsCrawler(news_sources=["LTN", "Bitcoin.com"])

        # 搜尋所有 2021-10-01 之後的新聞
        since_date = date.fromisoformat('2021-10-01')
        news_list = crawler.findBySinceDate(since_date)
        ```

  * 單一網站 - 以自由時報資料為例，基本上所有Client都有相關 method：
    * findBySinceDate(since_date)
      參數：

      * since_date：爬蟲將會爬此日期之後的所有新聞，**預設為今日**，即今日的所有新聞。
        ```Python
        # 搜尋所有 2021-10-01 之後的新聞
         ltn_news_client = LTNNewsClient()
         since_date = date.fromisoformat('2021-10-01')
         news_list = ltn_news_client.findBySinceDate(since_date)
        ```
    * findByMaxPages(max_pages=10)
      參數：

      * max_pages：要爬該網站幾頁，**預設為10頁**。
        ```Python
        # 搜尋 5頁 的新聞
         ltn_news_client = LTNNewsClient()
         news_list = ltn_news_client.findByMaxPages(max_pages=5)
        ```

  * #### 回傳的資料格式
    ```json
      [
        {
          "link": "https://news.bitcoin.com/sec-chairman-gary-gensler-looks-forward-review-bitcoin-futures-etf-filings/",
          "title": "SEC Chairman Gary Gensler Looks Forward to Review of Bitcoin Futures ETF Filings",
          "content": "",
          "pub_date_time": "2021-09-30 20:30:15+00:00"
        },
        {
          "link": "https://news.bitcoin.com/billionaire-orlando-bravo-owns-bitcoin-it-will-increase-significantly-very-bullish/",
          "title": "Billionaire Orlando Bravo Owns Bitcoin, Says ‘It Will Increase Significantly, I’m Very Bullish’",
          "content": "",
          "pub_date_time": "2021-09-30 18:30:46+00:00"
        }
      ]
    ```
    回傳的為 NewsInfo 裡面的 NewsInfo Entity。
    其中有幾項資料
    * link：新聞連結
    * title：新聞標題
    * content：新聞內文 **(目前尚未實際抓取)**
    * pub_date_time：新聞發布時間

### 2.  社群軟體
