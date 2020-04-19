#Author Shaishav Maisuria
#this is main code file which includes interactive line chart
import os
import csv
from collections import defaultdict
import plotly.graph_objs as go
import pandas as pd
import plotly.offline as pyo

df2 = pd.read_csv(r"C:\Users\maisu\PycharmProjects\Test\Datasets\time_series_covid19_confirmed_global.csv")

df2.iloc[:,4]
header=list(df2.head(0))
header=header[4:]
#print(header)dicForRowColumn={}
dicForRowColumnConfirmedGlobally = {}
dicAllRowColumnConfirmedGlobally = {}
dicForRowSumConfirmedGlobally = {}
dicAllRowSumConfirmedGlobally = {}
TotalCasesConfirmedGlobally = 0
for row in header:
    column = df2.loc[:, row]
    date = row

    column = list(column)
    sumPerDay = sum(column)
    # print("sum Per day:",sumPerDay)
    TotalCasesConfirmedGlobally += sumPerDay
    # print("Total Number of Cases:",TotalCases)
    newdf = pd.DataFrame(column)
    dicForRowColumnConfirmedGlobally.clear()
    dicForRowColumnConfirmedGlobally = {
        date: column
    }
    dicAllRowColumnConfirmedGlobally.update(dicForRowColumnConfirmedGlobally)
    dicForRowSumConfirmedGlobally = {
        date: sumPerDay
    }
    dicAllRowSumConfirmedGlobally.update(dicForRowSumConfirmedGlobally)

print(dicAllRowSumConfirmedGlobally)
# print(dic2)
# print("Total Number of Cases:",TotalCases)
date = header
print("-------------------")
print(date)

dataframeNew=pd.DataFrame(dicAllRowSumConfirmedGlobally, index=[0])
print(dataframeNew)
date=dataframeNew.keys()
print(date)
dataConfirmedGlobally=dataframeNew.values[0]
print(dataConfirmedGlobally)

data_linechart = [go.Scatter(x=date, y=dataConfirmedGlobally, mode='lines', name='Death')]

# Preparing layout
layout = go.Layout(title='Corona Virus Confirmed Cases globally From 2020-01-22 to till', xaxis_title="Date",
                   yaxis_title="Number of cases")

# Plot the figure and saving in a html file
fig = go.Figure(data=data_linechart, layout=layout)
pyo.plot(fig, filename='linechart.html')




print("-------------------")

dataframeNew=pd.DataFrame(dicAllRowSumConfirmedGlobally, index=[0])

print(dataframeNew)

#values
print("data frame values")
date=dataframeNew.keys()
print(date)
dataConfirmedGlobally=dataframeNew.values[0]
print(dataConfirmedGlobally)

len(dataConfirmedGlobally)
from Plots import TotalDeathUs as td


recovered= dataConfirmedGlobally - td.usDeath
len(recovered)
print(recovered)


