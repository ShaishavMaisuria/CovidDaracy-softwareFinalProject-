# SoftwareFinalProject
PLEASE READ THIS BEFORE DOWNLOADING AND RUNNING

PLEASE READ THIS BEFORE DOWNLOADING AND RUNNING

# Project Description:
Overall, the idea for this project is to analyze the number of cases of COVID-19 and the fatality rate. Using this data we created a chart that constantly updates with new information about cases in the US and possibly around the world and to provide an accurate number of cases. Using various datasets we combined the different features together.

# File description: 
User is supposed to run the main.py in order to obtain results displayed using the dash

You must install the following packages in your Python IDE before running the code!

from collections import defaultdict             
import plotly.graph_objs as go            
import pandas as pd         
import plotly.offline as pyo        
import dash        
import dash_core_components as dcc       
import dash_html_components as html        
from dash.dependencies import Input, Output       
from Plots import TotalDeathUs as tdus     
from Plots import TotalDeathWorlWide as tdw     
from Plots import confirmed_Globally as cg    
from Plots import confirmed_US as cus    
from Plots import recovered_global as rg      



# Datasets 
Datasets have been acquired from the following GitHub repositories:    
   
Johns Hopkins Whiting School of engineering - https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_time_series       
       
CovidTrackingApp - https://github.com/COVID19Tracking/covid-tracking-data     




This is for a software engineering class project. This repository and code are purely used for educational purposes.

Thank you for understanding!
