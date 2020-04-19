#Author Shaishav Maisuria
#this is main code file
# use this file to make all code interactive for html, or other analysis which needs to be shown
# if you want to create bar chart or anything create here
#To Do : Need to implement all analysis to dashboard
# decide and add more features
# look through all files to make sure you understand


#please keep all the imports as we will use it
import csv
from collections import defaultdict
import plotly.graph_objs as go
import pandas as pd
import plotly.offline as pyo

# as you import the files it will run it back ground once you run this file so will see multiple charts when you run this program
from Plots import TotalDeathUs as tdus
from Plots import TotalDeathWorlWide as tdw
from Plots import confirmed_Globally as cg
from Plots import confirmed_US as cus
from Plots import recovered_global as rg


#example
dataConfirmedCases=cus.data
date=cus.date
print(dataConfirmedCases)

data_linechart = [go.Scatter(x=date, y=dataConfirmedCases, mode='lines', name='Death')]

# Preparing layout
layout = go.Layout(title='Corona Virus Confirmed Cases From 2020-01-22 to till', xaxis_title="Date",
                   yaxis_title="Number of cases")

# Plot the figure and saving in a html file
fig = go.Figure(data=data_linechart, layout=layout)
pyo.plot(fig, filename='linechart.html')

#example over


