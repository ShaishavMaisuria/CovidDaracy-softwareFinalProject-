#includes us death
#Author Shaishav Maisuria

import pandas as pd


df2 = pd.read_csv(r"C:\Users\maisu\PycharmProjects\Test\Datasets\time_series_covid19_deaths_global.csv")

df2.iloc[:,5]
header=list(df2.head(0))
header=header[4:]


usDeath=list(df2.loc[225])
usDeath=usDeath[4:] #list that has list of all the death per day along with sum count. which means each values in list is sum of pervious indexes its based on csv data
#so its sum of death in each cells till that day
print(usDeath)

TotalusDeath=usDeath[-1]
print(TotalusDeath)

#to do
# make list which show number of death per day not the sum till that date

