#this is file which plot deaths of entire world
#Author Shaishav Maisuria
import os
import csv
from collections import defaultdict
import plotly.graph_objs as go
import pandas as pd
import plotly.offline as pyo

df2 = pd.read_csv(r"C:\Users\maisu\PycharmProjects\Test\Datasets\time_series_covid19_deaths_global.csv")
# link website https://github.com/CSSEGISandData/COVID-19
df2.iloc[:,5]
header=list(df2.head(0))
header=header[5:]
#print(header)dicForRowColumn={}
dicForRowColumnDeath = {}
dicAllRowColumnDeath = {}
dicForRowSumDeath = {}
dicAllRowSumDeath = {}
TotalDeathCases = 0

for row in header:
    columnDeath = df2.loc[:, row]
    date = row

    columnDeath = list(columnDeath)
    sumPerDay = sum(columnDeath)
    # print("sum Per day:",sumPerDay)
    TotalDeathCases += sumPerDay
    # print("Total Number of Cases:",TotalCases)
    newdf = pd.DataFrame(columnDeath)
    dicForRowColumnDeath.clear()
    dicForRowColumnDeath = {
        date: columnDeath
    }
    dicAllRowColumnDeath.update(dicForRowColumnDeath)
    dicForRowSumDeath = {
        date: sumPerDay
    }
    dicAllRowSumDeath.update(dicForRowSumDeath)

print(dicAllRowSumDeath)
# print(dic2)
# print("Total Number of Cases:",TotalCases)
date = header
print("-------------------")
print(date)

dataframeDeathNew=pd.DataFrame(dicAllRowSumDeath, index=[0])
print(dataframeDeathNew)
date=dataframeDeathNew.keys()
print(date)
data=dataframeDeathNew.values[0]
print(data)

data_linechart = [go.Scatter(x=date, y=data, mode='lines', name='Death')]

# Preparing layout
layout = go.Layout(title='Corona Virus Death', xaxis_title="Date",
                   yaxis_title="Number of cases")

# Plot the figure and saving in a html file
fig = go.Figure(data=data_linechart, layout=layout)
pyo.plot(fig, filename='linechart.html')




print("-------------------")

dataframeDeathNew=pd.DataFrame(dicAllRowSumDeath, index=[0])

print(dataframeDeathNew)

#values
print("data frame values")
date=dataframeDeathNew.keys()
print(date)
data=dataframeDeathNew.values[0]
print(data)
