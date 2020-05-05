#Author Shaishav Maisuria
#this is file which plot recovered cases of entire world
#JHU datasets
# link website https://github.com/CSSEGISandData/COVID-19

import pandas as pd
import pathlib



df2 = pd.read_csv(str(pathlib.Path().absolute())+r"\datasetsJHU\time_series_covid19_recovered_global.csv")



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



print("-------------------")

dataframeConfirmedGloballyNew=pd.DataFrame(dicAllRowSumConfirmedGlobally, index=[0])

print(dataframeConfirmedGloballyNew)

#values
print("data frame values")
date=dataframeConfirmedGloballyNew.keys()
print(date)
dataConfirmedGlobally=dataframeConfirmedGloballyNew.values[0]
print(dataConfirmedGlobally)
