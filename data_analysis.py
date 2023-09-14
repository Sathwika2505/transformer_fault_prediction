from loading_data import loading_data

def data_analysis():
    data1, data2 = loading_data()
    print(data1.info())
    print(data2.info())
    print(data1.describe())
    print(data2.describe())
    print(data1.columns)
    print(data1.shape)
    print(data1.head())
    print(data1.tail())
    print(data2.columns)
    print(data2.shape)
    print(data2.head())
    print(data2.tail())
    print(data1.isnull().sum())
    print(data2.isnull().sum())
    for col in data1.columns:
        print(col, data1[col].nunique())
    for col in data2.columns:
        print(col, data2[col].nunique())
    return data1, data2

data_analysis()
