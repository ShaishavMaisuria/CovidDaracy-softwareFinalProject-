#Author Shaishav Maisuria
#this file is focusing on cleaning the data and putting in csv file
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




print("-------------------")

import csv

# field names


# data rows of csv file
rows = data
rows=zip(rows)
# name of csv file
filename = "university_records.csv"

# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    fields=('Name')
    csvwriter = csv.writer(csvfile,lineterminator='\n')

    #tranforming row in column and printing it to csv
    for word in rows:
        csvwriter.writerow(word)
    csvfile.close()









