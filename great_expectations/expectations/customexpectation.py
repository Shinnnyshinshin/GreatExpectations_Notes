from great_expectations.dataset import PandasDataset, MetaPandasDataset
import string

# 

class CustomPandasDataset(PandasDataset):

    _data_asset_type = "CustomPandasDataset"

    @MetaPandasDataset.column_english_expectation
    def expect_column_to_be_english(self, column):
        printable = set(string.printable)
        return column.map(lambda x: x in printable)
