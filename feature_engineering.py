import pandas as pd
import numpy as np
from data_preprocessing import data_preprocess

def feature_engineering():

    data = data_preprocess()
    # print(data)
    count_0, count_1 = data['MOG_A'].value_counts()
    class_0 = data[data['MOG_A'] == 0]
    class_1 = data[data['MOG_A'] == 1]
    Target_1_over = class_1.sample(count_0,replace=True)
    # print(Target_1_over)
    dataset_balanced = pd.concat([Target_1_over,class_0], axis=0)
    # print(dataset_balanced)

    data = dataset_balanced.copy()
    data.to_csv("transformer_fault_prediction.csv", index = False)
    return data

feature_engineering()