import pandas as pd
import plotly.graph_objs as go
import datetime
import os
import csv
from collections import defaultdict

df2 = pd.read_csv(r"C:\Users\maisu\PycharmProjects\Test\Datasets\time_series_covid19_confirmed_US.csv")

df2.iloc[:,11]
header=list(df2.head(0))
header=header[11:]
#print(header)
dic = {}
dic2 = {}
for row in header:
    column = df2.loc[:, row]

    column = list(column)
    sum1=sum(column)
    newdf = pd.DataFrame(column)
    dic.clear()
    dic = {
        row: column
    }
    dic2.update(dic)

print(dic2.values())

print("-------------------")