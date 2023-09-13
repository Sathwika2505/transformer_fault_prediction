import pandas as pd
from loading_data import loading_data

def data_preprocess():
    data1, data2 = loading_data()
    whole_df = pd.merge(data2, data1, on='DeviceTimeStamp')
    whole_df = whole_df.drop(['DeviceTimeStamp'], axis=1)
    whole_df.drop(['OTI_A','OTI_T','WTI'], axis=1,inplace=True)
    print(whole_df)
    print(whole_df.duplicated())
    print(whole_df.isnull().sum())
    whole_df['MOG_A'] = whole_df['MOG_A'].astype('int')
    whole_df.columns = whole_df.columns.str.replace(' ', '_') 
    return whole_df

data_preprocess()
