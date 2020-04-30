#this is file which plot recovered cases of entire world
# No file was avaible for any recovered cases for us for JHU website
#Author Shaishav Maisuria

import plotly.graph_objs as go
import pandas as pd
import plotly.offline as pyo

#JHU datasets
# link website https://github.com/CSSEGISandData/COVID-19
df2 = pd.read_csv(r"C:\Users\maisu\PycharmProjects\Test\Datasets\time_series_covid19_recovered_global.csv")
# link website https://github.com/CSSEGISandData/COVID-19
df2.iloc[:,4]
header=list(df2.head(0))
header=header[4:]
#print(header)dicForRowColumn={}
dicForRowColumnConfirmedGlobally = {}
dicAllRowColumnConfirmedGlobally = {}
dicForRowSumConfirmedGlobally = {}
dicAllRowSumConfirmedGlobally = {}
TotalConfirmedGlobally = 0

for row in header:
    columnConfirmedGlobally = df2.loc[:, row]
    date = row

    columnConfirmedGlobally = list(columnConfirmedGlobally)
    sumPerDay = sum(columnConfirmedGlobally)
    # print("sum Per day:",sumPerDay)
    TotalConfirmedGlobally += sumPerDay
    # print("Total Number of Cases:",TotalCases)
    newdf = pd.DataFrame(columnConfirmedGlobally)
    dicForRowColumnConfirmedGlobally.clear()
    dicForRowColumnConfirmedGlobally = {
        date: columnConfirmedGlobally
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

dataframeConfirmedGloballyNew=pd.DataFrame(dicAllRowSumConfirmedGlobally, index=[0])
print(dataframeConfirmedGloballyNew)
date=dataframeConfirmedGloballyNew.keys()
print(date)
dataConfirmedGlobally=dataframeConfirmedGloballyNew.values[0]
print(dataConfirmedGlobally)

data_linechart = [go.Scatter(x=date, y=dataConfirmedGlobally, mode='lines', name='Death')]

# Preparing layout
layout = go.Layout(title='Corona Recovered cases globally', xaxis_title="Date",
                   yaxis_title="Number of cases")

# Plot the figure and saving in a html file
fig = go.Figure(data=data_linechart, layout=layout)
pyo.plot(fig, filename='linechart.html')


print("-------------------")

dataframeConfirmedGloballyNew=pd.DataFrame(dicAllRowSumConfirmedGlobally, index=[0])

print(dataframeConfirmedGloballyNew)

#values
print("data frame values")
date=dataframeConfirmedGloballyNew.keys()
print(date)
dataConfirmedGlobally=dataframeConfirmedGloballyNew.values[0]
print(dataConfirmedGlobally)
