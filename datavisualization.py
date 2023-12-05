from feature_engineering import feature_engineering
import pandas as pd
import plotly.express as px
from IPython.display import Image
import warnings
warnings.filterwarnings("ignore")
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff
import plotly.io as pio
import io
from PIL import Image
a =[]
def data_visualization():
    data = feature_engineering()
    data.drop(['OTI_A','OTI_T','WTI'], axis=1,inplace=True)
    col=list(data.columns)
    col.remove("MOG_A")
    print(col)
    for x in col:
        q75,q25 = np.percentile(copy_df3.loc[:,x],[75,25])
        intr_qr = q75-q25 
        max = q75+(1.5*intr_qr)
        min = q25-(1.5*intr_qr) 
        copy_df3.loc[copy_df3[x] < min,x] = np.nan
        copy_df3.loc[copy_df3[x] > max,x] = np.nan
    for i in col:
        fig = px.box(data, y=i)
        fig.update_layout(template='plotly_dark')
        #fig.update_layout(plot_bgcolor = "plotly_dark")
        fig.update_xaxes(showgrid=False,zeroline=False)
        fig.update_yaxes(showgrid=False,zeroline=False)
        # fig.show()
        fig.write_image(f"{i}.jpg")
        # a.append(fig)
    # for i in col:
    #     fig = ff.create_distplot([data[i].values],group_labels=[i])
    #     fig.update_layout(template='plotly_dark')
    #     #fig.update_layout(plot_bgcolor = "plotly_dark")
    #     fig.update_xaxes(showgrid=False,zeroline=False)
    #     fig.update_yaxes(showgrid=False,zeroline=False)
        # fig.show()
        # a.append(fig)
    df=data.drop("MOG_A",axis=1)
    y=df.corr().columns.tolist()
    z=df.corr().values.tolist()
    z_text = np.around(z, decimals=4) # Only show rounded value (full value on hover)
    fig = ff.create_annotated_heatmap(z,x=y,y=y,annotation_text=z_text,colorscale=px.colors.sequential.Cividis_r,showscale=True)
    fig.update_layout(template='plotly_dark')
    # fig.show()
    fig.write_image("img.jpg")
    # a.append(fig)
    
    return data

data_visualization()
