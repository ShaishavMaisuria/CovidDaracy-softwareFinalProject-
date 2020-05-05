#Author Shaishav Maisuria
#this is file that has number of confirmed cases US

#JHU datasets
# link website https://github.com/CSSEGISandData/COVID-19


import pandas as pd
import pathlib

df2 = pd.read_csv(str(pathlib.Path().absolute())+r"\datasetsJHU\time_series_covid19_confirmed_US.csv")


df2.iloc[:,11]
header=list(df2.head(0))
header=header[11:]

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

    TotalCases += sumPerDay

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

date = header
print("-------------------")
print(date)

dataframeNew=pd.DataFrame(dicAllRowSum,index=[0])
print(dataframeNew)
date=dataframeNew.keys()
print(date)
data=dataframeNew.values[0]
print(data)
