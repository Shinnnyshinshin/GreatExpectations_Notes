from great_expectations.dataset import PandasDataset, MetaPandasDataset


# -*- coding: utf-8 -*-
def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True
        

class CustomPandasDataset(PandasDataset):

    _data_asset_type = "CustomPandasDataset"

    @MetaPandasDataset.column_map_expectation
    def expect_column_to_be_english(self, column):
        return column.map(isEnglish)
        
    @MetaPandasDataset.column_map_expectation
    def expect_count_to_be_1(self, column):
        return column.map(lambda x: x==1)
        