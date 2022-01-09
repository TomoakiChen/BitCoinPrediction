from AkiPyUtil.AkiPyDateTime import AkiDateTimeUtil

class NewsInfoHelper:
    @staticmethod
    def filterBySincaDate(ori_news_info_list, since_date):
        since_datetime = datetime.combine(since_date, datetime.min.time())
        filtered_news_info_list = [news_info for news_info in ori_news_info_list if news_info.getPubDateTime(
        ) != None and news_info.getPubDateTime().timestamp() >= since_datetime.timestamp()]
        return filtered_news_info_list

    @staticmethod
    def filterByInterval(ori_news_info_list, since_date, end_date):
        filtered_news_info_list = [news_info for news_info in ori_news_info_list if NewsInfoHelper.checkIsInInterval(news_info, since_date, end_date)]
        # print("ori-nums = " + str(len(ori_news_info_list)) + " filterd_nums = " + str(len(ori_news_info_list))  )
        return filtered_news_info_list

    @staticmethod
    def checkIsAfterEqSinceDate(news_info, since_date=None):
        pub_datetime = news_info.getPubDateTime()
        if pub_datetime == None:
            return False
        return AkiDateTimeUtil.checkIsAfterEqSinceDate(pub_datetime, since_date)

    @staticmethod
    def checkIsBeforeEqUntilDate(news_info, until_date=None):
        pub_datetime = news_info.getPubDateTime()
        if pub_datetime == None:
            return False
        return AkiDateTimeUtil.checkIsBeforeEqUntilDate(pub_datetime, since_date)

    @staticmethod
    def checkIsInInterval(news_info, since_date=None, until_date=None):
        pub_datetime = news_info.getPubDateTime()
        if pub_datetime == None:
            return False
        return AkiDateTimeUtil.checkIsInInterval(pub_datetime, since_date, until_date)


class NewsCrawlerHelper:
    @staticmethod
    def needStopMining(news_info_list, filtered_news_info_list):
        return len(filtered_news_info_list) != len(news_info_list)
