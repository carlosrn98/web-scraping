import pandas as pd
import numpy as np

class FrameService:
    def __init__(self, array):
        """
            This initialization method created a Pandas Dataframe coming from a list.
            At the same time, it replaces all blanks with a NaN value.
        """
        self.df = pd.DataFrame(array)
        self.df = self.df.replace('', np.nan)
    
    def show_df(self):
        """
            Method that prints the Pandas DataFrame.
        """
        print(self.df)

    def get_row_num(self):
        """
            Method that returns the number of rows that the Pandas Dataframe has.
        """
        return self.df.shape[0]

    def group_by_file_format(self):
        """
            This method transforms all the records to lower case and then it returns
            the number of rows by file type (format).
        """
        self.df["format"] = self.df["format"].str.lower()
        return self.df.groupby(["format"], dropna=False).count()["id"]