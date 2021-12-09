import pandas as pd

class PandasDataFrameHelper:

    @staticmethod
    def analyzeNums4Rows(df):
        return df.shape[0]

    @staticmethod
    def analyzeNums4Cols(df):
        return df.shape[1]

    @staticmethod
    def parseObjectList2DataFrame(objList, obj2DictFunc, desig_col_list=None):
        dict_list = list()
        for obj in objList:
            # dictObj = obj.__dict__
            # for key in dictObj.keys():
            #     print(key)
            dict = obj2DictFunc(obj)
            dict_list.append(dict)
        return PandasDataFrameHelper.parseDictList2DataFrame(dict_list, desig_col_list)

    @staticmethod
    def parseDictList2DataFrame(dictList, desig_col_list=None):
        if dictList == None or len(dictList) == 0:
            return None

        if desig_col_list == None:
            desig_col_list = PandasDataFrameHelper.__obtainDictColList(dictList)

        col_values_dict = dict()
        for desig_col in desig_col_list:
            col_values = col_values_dict.get(desig_col)
            if col_values == None:
                col_values = list()
            for dictInfo in dictList:
                col_value = dictInfo.get(desig_col)
                col_values.append(col_value)
            col_values_dict[desig_col] = col_values
        return pd.DataFrame(col_values_dict)

    @staticmethod
    def __obtainDictColList(dictList):
        dict_example = dictList.pop(0)
        return list(dict_example.keys())

    @staticmethod
    def processDataNormalizationByMean(df, desig_col_list):
        normalized_df = df
        desig_col_df = normalized_df[desig_col_list]
        normalized_desig_col_df = (desig_col_df - desig_col_df.mean()) / desig_col_df.std()
        normalized_df[desig_col_list] = normalized_desig_col_df
        return normalized_df

    @staticmethod
    def processDataNormalizationByMaxMin(df, desig_col_list):
        normalized_df = df
        desig_col_df = df[desig_col_list]
        normalized_desig_col_df = (desig_col_df - desig_col_df.min()) / (desig_col_df.max() - desig_col_df.min())
        normalized_df[desig_col_list] = normalized_desig_col_df
        return normalized_df
