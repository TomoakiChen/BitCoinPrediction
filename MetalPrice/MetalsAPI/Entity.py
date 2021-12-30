class MetalsAPISymbol:

    __code = None
    __label = None

    def __init__(self, code, label):
        self.__code = code
        self.__label = label

    def getCode(self):
        return self.__code

    def setCode(self):
        self.__code = code

    def getLabel(self):
        return self.__label

    def setLabel(self, label):
        self.__label = label




class MetalsAPITimeSeriesData:

    __success = False
    __timeseries = False
    __start_date = None
    __end_date = None
    __base = None
    __rates = None

    def __init__(self):
        pass


class MetalsAPIRate:

    def __init__(self):
        pass
