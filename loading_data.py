import  pandas as pd
import numpy as np

def loading_data():
    df_1 = pd.read_csv("Overview.csv")
    df_2 = pd.read_csv("CurrentVoltage.csv")
    # print("df1 data : ", df_1)
    # print("df2 data : ", df_2)
    return df_1, df_2

loading_data()