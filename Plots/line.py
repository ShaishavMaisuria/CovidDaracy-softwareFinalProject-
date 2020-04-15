import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import datetime
import os
import csv
from collections import defaultdict

path_name='../Datasets/time_series_covid19_confirmed_US.csv'

# Load CSV file from Datasets folder
df1 = pd.read_csv('../Datasets/04-12-2020.csv')
df2 = pd.read_csv('../Datasets/time_series_covid19_confirmed_US.csv')



file = open(os.path.join(path_name), "rU")
reader = csv.reader(file, delimiter=',')


count=0
for column in reader:
    count=count+1
    print(column[11:])

    if count ==2:
        break


count=0
for row in reader:
    count=count+1
    included_cols=row[11:]

    df3 = df2.set_index(row[11:], drop=False)
    df2.loc[0:,11:]

   # column_data=list(for i in included_cols: row(i) row(i) )
    for column in included_cols:
        print(column)
    if count ==3:
        break



