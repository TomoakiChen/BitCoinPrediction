import pandas as pd

class PandasDataFrameHelper:

    @staticmethod
    def analyzeNums4Rows(df):
        return df.shape[0]

    @staticmethod
    def analyzeNums4Cols(df):
        return df.shape[1]

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
