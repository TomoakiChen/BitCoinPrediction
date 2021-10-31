class NewsInfo:
    def __init__(self):
        self._link = ''#None
        self._title = ''#None
        self._content =''# None
        self._pub_date_time = None

    def getLink(self):
        return self._link

    def setLink(self, link):
        self._link = link

    def getTitle(self):
        return self._title

    def setTitle(self, title):
        self._title = title

    def getContent(self):
        return self._content

    def setContent(self, content):
        self._content = content

    def getPubDateTime(self):
        return self._pub_date_time

    def setPubDateTime(self, pub_date_time):
        self._pub_date_time = pub_date_time

    def __str__(self):
        result = '{'
        result += 'link = "' + self._link + '"'
        result += ', '
        result += 'title = "' + self._title + '"'
        result += ', '
        result += 'content = "' + self._content + '"'
        result += ', '
        result += 'pub_date_time = "' + str(self._pub_date_time) + '"'  # https://stackoverflow.com/questions/27980579/concatenate-str-and-nonetype-objects
        result += '}'
        return result
