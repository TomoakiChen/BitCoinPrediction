import pandas as pd

class PandasDataFrameHelper:

    @staticmethod
    def analyzeNums4Rows(df):
        return df.shape[0]

    @staticmethod
    def analyzeNums4Cols(df):
        return df.shape[1]
