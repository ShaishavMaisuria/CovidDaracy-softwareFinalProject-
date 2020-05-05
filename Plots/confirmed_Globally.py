#Author Shaishav Maisuria
#this is file that has number of confirmed cases globally

#JHU datasets
# link website https://github.com/CSSEGISandData/COVID-19



import pandas as pd
import pathlib


df2 = pd.read_csv(str(pathlib.Path().absolute())+r"\datasetsJHU\time_series_covid19_confirmed_global.csv")



df2.iloc[:,4]
header=list(df2.head(0))
header=header[4:]
dicForRowColumnConfirmedGlobally = {}
dicAllRowColumnConfirmedGlobally = {}
dicForRowSumConfirmedGlobally = {}
dicAllRowSumConfirmedGlobally = {}
TotalCasesConfirmedGlobally = 0
#goes vertically and added the data based on csv format
for row in header:
    column = df2.loc[:, row]
    date = row

    column = list(column)
    sumPerDay = sum(column)

    TotalCasesConfirmedGlobally += sumPerDay

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
date = header
print("-------------------")
print(date)

dataframeNew=pd.DataFrame(dicAllRowSumConfirmedGlobally, index=[0])
print(dataframeNew)
date=dataframeNew.keys()
print(date)
dataConfirmedGlobally=dataframeNew.values[0]
print(dataConfirmedGlobally)





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



