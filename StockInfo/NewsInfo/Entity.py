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
