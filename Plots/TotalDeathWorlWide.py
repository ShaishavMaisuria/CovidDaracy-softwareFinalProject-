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
dicForRowColumnDeathGlobally = {}
dicAllRowColumnDeathGlobally = {}
dicForRowSumDeathGlobally = {}
dicAllRowSumDeathGlobally = {}
TotalDeathCasesGlobally = 0

for row in header:
    columnDeathGlobally = df2.loc[:, row]
    date = row

    columnDeathGlobally = list(columnDeathGlobally)
    sumPerDay = sum(columnDeathGlobally)
    # print("sum Per day:",sumPerDay)
    TotalDeathCasesGlobally += sumPerDay
    # print("Total Number of Cases:",TotalCases)
    newdf = pd.DataFrame(columnDeathGlobally)
    dicForRowColumnDeathGlobally.clear()
    dicForRowColumnDeathGlobally = {
        date: columnDeathGlobally
    }
    dicAllRowColumnDeathGlobally.update(dicForRowColumnDeathGlobally)
    dicForRowSumDeathGlobally = {
        date: sumPerDay
    }
    dicAllRowSumDeathGlobally.update(dicForRowSumDeathGlobally)

print(dicAllRowSumDeathGlobally)
# print(dic2)
# print("Total Number of Cases:",TotalCases)
date = header
print("-------------------")
print(date)

dataframeDeathNew=pd.DataFrame(dicAllRowSumDeathGlobally, index=[0])
print(dataframeDeathNew)
date=dataframeDeathNew.keys()
print(date)
dataDeathGlobally=dataframeDeathNew.values[0]
print(dataDeathGlobally)






