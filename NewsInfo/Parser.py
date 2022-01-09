from PandasHelper import PandasDataFrameHelper
class NewsInfoParser:

    @staticmethod
    def parseInfoList2DataFrame(newsInfoList, desig_col_list=None):
        return PandasDataFrameHelper.parseObjectList2DataFrame(newsInfoList, NewsInfoParser.parseInfo2Dict, desig_col_list)


    @staticmethod
    def parseInfoList2DictList(newsInfoList):
        dict_list = []
        for newsInfo in newsInfoList:
            dict = NewsInfoParser.parseInfo2Dict(newsInfo)
            dict_list.append(newsInfo)
        return news_info

    @staticmethod
    def parseInfo2Dict(newsInfo):
        dict = {}
        dict["link"] = newsInfo.getLink()
        dict["title"] = newsInfo.getTitle()
        dict["content"] = newsInfo.getContent()
        dict["pubDateTime"] = newsInfo.getPubDateTime().strftime("%Y-%m-%d %H:%M:%S")
        return dict
