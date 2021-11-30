from PyWeb import HttpClient


# class GlassNodeClinet(GlassNodeJsonClinet):




# =========================================== 以下是 核心「純粹拿到 json string」 的 client(X)，不分了 ===========================================
# =========================================== 以上是 核心「純粹拿到 json string」 的 client ===========================================

# class GlassNodeJsonClinet(HttpClient):
class GlassNodeClinet(HttpClient):

    # _apiKey = None
    __apiBaseUrl = "https://api.glassnode.com"
    __apiResourceUrlDict = {
        "assetsList": "/v1/metrics/assets"
    }
    __apiKey = None

    def __init__(self, apiKey, apiBaseUrl=None):
        self.__apiKey = apiKey
        if apiBaseUrl != None:
            self.__apiBaseUrl = apiBaseUrl

    def __obtainUrl(self, code):
        resourceUrl = self.__apiResourceUrlDict.get(code)
        return self.__apiBaseUrl + resourceUrl



    def getAssetsList(self):
        jsonStr = self._getJsonAssetsList()
            

    # =========================================== 以下是 比較底層 method，純粹拿到 json string」 ===========================================
    def _getJsonAssetsList(self):
        url = self.__obtainUrl("assetsList")
        params={'a': 'BTC', 'api_key': self.__apiKey}
        return self.sendGetRequest(url, queryParams=params)
    # =========================================== 以上是 比較底層 method，純粹拿到 json string」===========================================
