class NewsInfo:
    def __init__(self):
        self.__link = ''#None
        self.__title = ''#None
        self.__content =''# None
        self.__pub_date_time = None

    def getLink(self):
        return self.__link

    def setLink(self, link):
        self.__link = link

    def getTitle(self):
        return self.__title

    def setTitle(self, title):
        self.__title = title

    def getContent(self):
        return self.__content

    def setContent(self, content):
        self.__content = content

    def getPubDateTime(self):
        return self.__pub_date_time

    def setPubDateTime(self, pub_date_time):
        self.__pub_date_time = pub_date_time

    def __str__(self):
        result = '{'
        result += 'link = "' + self.__link + '"'
        result += ', '
        result += 'title = "' + self.__title + '"'
        result += ', '
        result += 'content = "' + self.__content + '"'
        result += ', '
        result += 'pub_date_time = "' + str(self.__pub_date_time) + '"'  # https://stackoverflow.com/questions/27980579/concatenate-str-and-nonetype-objects
        result += '}'
        return result

# ================================================= 以下暫時寫在這支裡面

"""
class NewsInfoConverter:

    def __init__(self):
        pass
"""
from PandasHelper import PandasDataFrameHelper
class NewsInfoHelper:

    @staticmethod
    def parseInfoList2DataFrame(newsInfoList, desig_col_list=None):
        return PandasDataFrameHelper.parseObjectList2DataFrame(newsInfoList, NewsInfoHelper.parseInfo2Dict, desig_col_list)


    @staticmethod
    def parseInfoList2DictList(newsInfoList):
        dict_list = []
        for newsInfo in newsInfoList:
            dict = NewsInfoHelper.parseInfo2Dict(newsInfo)
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
