#Author Shaishav Maisuria
import os
import csv
from collections import defaultdict
import plotly.graph_objs as go
import pandas as pd
import plotly.offline as pyo

df2 = pd.read_csv(r"C:\Users\maisu\PycharmProjects\Test\Datasets\time_series_covid19_confirmed_US.csv")

df2.iloc[:,11]
header=list(df2.head(0))
header=header[11:]
#print(header)dicForRowColumn={}
dicForRowColumn = {}
dicAllRowColumn = {}
dicForRowSum = {}
dicAllRowSum = {}
TotalCases = 0
for row in header:
    column = df2.loc[:, row]
    date = row

    column = list(column)
    sumPerDay = sum(column)
    # print("sum Per day:",sumPerDay)
    TotalCases += sumPerDay
    # print("Total Number of Cases:",TotalCases)
    newdf = pd.DataFrame(column)
    dicForRowColumn.clear()
    dicForRowColumn = {
        date: column
    }
    dicAllRowColumn.update(dicForRowColumn)
    dicForRowSum = {
        date: sumPerDay
    }
    dicAllRowSum.update(dicForRowSum)

print(dicAllRowSum)
# print(dic2)
# print("Total Number of Cases:",TotalCases)
date = header
print("-------------------")
print(date)

dataframeNew=pd.DataFrame(dicAllRowSum,index=[0])
print(dataframeNew)
date=dataframeNew.keys()
print(date)
data=dataframeNew.values[0]
print(data)

data_linechart = [go.Scatter(x=date, y=data, mode='lines', name='Death')]

# Preparing layout
layout = go.Layout(title='Corona Virus Confirmed Cases From 2020-01-22 to 2020-03-17', xaxis_title="Date",
                   yaxis_title="Number of cases")

# Plot the figure and saving in a html file
fig = go.Figure(data=data_linechart, layout=layout)
pyo.plot(fig, filename='linechart.html')




print("-------------------")

dataframeNew=pd.DataFrame(dicAllRowSum,index=[0])

print(dataframeNew)

#values
print("data frame values")
date=dataframeNew.keys()
print(date)
data=dataframeNew.values[0]
print(data)
