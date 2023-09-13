import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from feature_engineering import feature_engineering

def data_visualization():

    dataset = feature_engineering()
    plt.figure(figsize=(10,8))
    sns.heatmap(dataset.corr(), annot=True, cmap="coolwarm", fmt=".2f")
    plt.show()

    categ = ['MOG_A']
    numer = ['VL1', 'VL2', 'VL3', 'IL1', 'IL2', 'IL3', 'VL12', 'VL23', 'VL31',
       'INUT', 'OTI', 'ATI', 'OLI']
    for x in numer:
        q75,q25 = np.percentile(dataset.loc[:,x],[75,25])
        intr_qr = q75-q25    
        max = q75+(1.5*intr_qr)
        min = q25-(1.5*intr_qr)    
        dataset.loc[dataset[x] < min,x] = np.nan
        dataset.loc[dataset[x] > max,x] = np.nan
    # Box plots
    for num in numer:
        plt.figure(figsize=(5, 5))
        sns.boxplot(data=dataset, x=num)
        plt.xlabel(num)
    plt.show()
    for numeric in numer:
        plt.subplots(1,1, figsize=(5,5))
        sns.distplot(x = dataset[numeric])
        plt.xlabel(numeric)
        plt.title(numeric)
    plt.show()
    return dataset

data_visualization()