# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 09:34:05 2018

@author: n0250949
"""

# Stack a bunch of csvs and xlsx files into one data frame

import pandas as pd
import os

#%%  Stack files function
def stack_files(input_folder,drop_duplicates=False):
    # Create an empty list
    dfs = []
    for file in os.listdir(input_folder):
        print(file)
        extension = os.path.splitext(file)[1]
        if extension == ".csv":
            df = pd.read_csv(os.path.join(input_folder,file),encoding="Latin-1")
            dfs.append(df)
        elif extension in [".xlsx",".xls"]:
            df = pd.read_excel(os.path.join(input_folder,file),encoding="Latin-1")        
            dfs.append(df)
    # Put list of data frames into one data frame
    df_output=pd.concat(dfs)
    if drop_duplicates == True:
        df_output.drop_duplicates(inplace=True)
    return(df_output)
