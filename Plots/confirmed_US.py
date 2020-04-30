#Author Shaishav Maisuria
#this is main code file which includes interactive line chart

#JHU datasets
# link website https://github.com/CSSEGISandData/COVID-19


import pandas as pd


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
