# Author Shaishav Maisuria
# this is main code file



# please keep all the imports as we will use it
import csv
from collections import defaultdict
import plotly.graph_objs as go
import pandas as pd
import plotly.offline as pyo
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# as you import the files it will run it back ground once you run this file so will see multiple charts when you run this program
from Plots import TotalDeathUs as tdus
from Plots import TotalDeathWorlWide as tdw
from Plots import confirmed_Globally as cg
from Plots import confirmed_US as cus
from Plots import recovered_global as rg
from Plots import covidTrackingUs as tds

app = dash.Dash()
# example
dataConfirmedUSCases = cus.data
date = cus.date
print(dataConfirmedUSCases)

data_ConfirmedUSCases = [go.Scatter(x=date, y=dataConfirmedUSCases, mode='lines', name='USCases')]
data_TotalUSDeath = [go.Scatter(x=date, y=tdus.usDeath, mode='lines', name='USDeath')]
data_TotalDeaths = [go.Scatter(x=date, y=tdw.dataDeathGlobally, mode='lines', name='TotalDeaths')]
data_ConfirmedGlobally = [go.Scatter(x=date, y=cg.dataConfirmedGlobally, mode='lines', name='confirmedGlobal')]
data_recoveredCasesGlobally = [go.Scatter(x=date, y=rg.dataConfirmedGlobally, mode='lines', name='recovered')]
data_positiveCases = [go.Scatter(x=date, y=tds.positiveCases, mode='lines', name='Tested Positive')]
data_negativeCases = [go.Scatter(x=date, y=tds.negativeCases, mode='lines', name='Tested Negative')]
data_pending = [go.Scatter(x=date, y=tds.pending, mode='lines', name='Pending Test Cases')]
data_hospitalizedCurr = [go.Scatter(x=date, y=tds.hospitalizedCurrently, mode='lines', name='Hospitalized')]
data_hospitalizedCumul = [go.Scatter(x=date, y=tds.hospitalizedCumulative, mode='lines', name='Hospitalized Cumulative')]
data_ICUCurrently = [go.Scatter(x=date, y=tds.inIcuCurrently, mode='lines', name='ICU Currently')]
data_ICUCumulative = [go.Scatter(x=date, y=tds.inIcuCumulative, mode='lines', name='ICU Cumulative')]
data_ventilatorsCurr = [go.Scatter(x=date, y=tds.onVentilatorCurrently, mode='lines', name='Ventilators Currently')]
data_recoveredUS = [go.Scatter(x=date, y=tds.recovered, mode='lines', name='US recovered Cases')]
data_deathIncrease = [go.Scatter(x=date, y=tds.deathIncrease, mode='lines', name='Death Increase')]
data_hospitalizedIncrease = [go.Scatter(x=date, y=tds.hospitalizedIncrease, mode='lines', name='Hospitalized')]
data_negativeIncrease = [go.Scatter(x=date, y=tds.negativeIncrease, mode='lines', name='Hospitalized')]
data_positiveIncrease = [go.Scatter(x=date, y=tds.positiveIncrease, mode='lines', name='Hospitalized')]
data_testResultsIncrease = [go.Scatter(x=date, y=tds.totalTestResultsIncrease, mode='lines', name='Hospitalized')]




# Layout
app.layout = html.Div(children=[
    html.H1(children='Python Dash',
            style={
                'textAlign': 'center',
            }
            ),
    html.Div('Web dashboard for Data Visualization using Python', style={'textAlign': 'center'}),
    html.Br(),
    html.Br(),
    html.H2('Coronavirus (COVID-19) Global Cases -  1/22/2020 to 5/6/2020', style={'textAlign': 'center', 'color': 'blue'}),
    html.Br(),
    html.Hr(style={'color': '#7FDBFF'}),

    html.H3('Confirmed Deaths Globally', style={'color': 'blue'}),
    html.Div('This line chart represent the total number of confirmed deaths globally.'),
    dcc.Graph(id='TotalDeathsGlobally',
              figure={
                  'data': data_TotalDeaths,
                  'layout': go.Layout(title='Total Corona Virus Deaths', xaxis_title="Date",
                                      yaxis_title="Number of cases")
              }
              ),

    html.H3('Confirmed Cases Globally', style={'color': 'blue'}),
    html.Div('This line chart represents the total number of confirmed cases globally.'),
    dcc.Graph(id='ConfirmedGlobally',
              figure={
                  'data': data_ConfirmedGlobally,
                  'layout': go.Layout(title='Total Corona Deaths in US', xaxis_title="Date",
                                      yaxis_title="Number of cases")
              }
              ),
    html.H3('Recovered Cases Globally', style={'color': 'blue'}),
    html.Div('This line chart represents the total number of recovered cases globally.'),
    dcc.Graph(id='RecoveredCasesGlobally',
              figure={
                  'data': data_recoveredCasesGlobally,
                  'layout': go.Layout(title='Total Recovered Cases Globally', xaxis_title="Date",
                                      yaxis_title="Number of cases")
              }
              ),
    html.Br(),
    html.Hr(style={'color': '#7FDBFF'}),
    html.Br(),
    html.H2('Coronavirus (COVID-19) United States Cases -  1/22/2020 to 5/6/2020', style={'textAlign': 'center', 'color': 'red'}),
    html.Br(),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Confirmed Cases in the US', style={'color': 'red'}),
    html.Div('This line chart represent the total number of confirmed cases in the United States.'),


    dcc.Graph(id='CasesUS',
              figure={
                  'data': data_ConfirmedUSCases,
                  'layout': go.Layout(title='Corona Virus Confirmed Cases From 2020-01-22 to till', xaxis_title="Date",
                                      yaxis_title="Number of cases")
              }
              ),
    html.H3('Confirmed Deaths in the US', style={'color': 'red'}),
    html.Div('This line chart represents the total number of confirmed deaths in the United States.'),
    dcc.Graph(id='TotalUSDeaths',
              figure={
                  'data': data_TotalUSDeath,
                  'layout': go.Layout(title='Total Corona Deaths in US', xaxis_title="Date",
                                      yaxis_title="Number of cases")
              }
              ),
    html.H3('Death Increases of COVID-19 in the US', style={'color': 'red'}),
    html.Div('This line chart represents the death increase of the corona virus in the United States.'),
    dcc.Graph(id='DeathIncrease',
              figure={
                  'data': data_deathIncrease,
                  'layout': go.Layout(title='Death Increase', xaxis_title="Date",
                                      yaxis_title="Number of cases")
              }
              ),
    html.H3('Testing Positive For COVID-19 in the US', style={'color': 'red'}),
    html.Div('This line chart represents the total number of postive testing for the corona virus in the United States.'),
    dcc.Graph(id='PositiveCases',
              figure={
                  'data': data_positiveCases,
                  'layout': go.Layout(title='Positive Tests', xaxis_title="Date",
                                      yaxis_title="Number of cases")
              }
              ),
    html.H3('Number of Increasing Positive Tests in the US', style={'color': 'red'}),
    html.Div('This line chart represents the number of increased positive tests because of the corona virus in the United States.'),
    dcc.Graph(id='PositiveIncrease',
              figure={
                  'data': data_positiveIncrease,
                  'layout': go.Layout(title='Number of Increased Positive Tests', xaxis_title="Date",
                                      yaxis_title="Number of cases")
              }
              ),
    html.H3('Testing Negative For COVID-19 in the US', style={'color': 'red'}),
    html.Div('This line chart represents the total number of negative testing for the corona virus in the United States.'),
    dcc.Graph(id='NegativeCases',
              figure={
                  'data': data_negativeCases,
                  'layout': go.Layout(title='Negative Tests', xaxis_title="Date",
                                      yaxis_title="Number of cases")
              }
              ),
    html.H3('Number of Increasing Negative Tests in the US', style={'color': 'red'}),
    html.Div('This line chart represents the number of increased negative tests because of the corona virus in the United States.'),
    dcc.Graph(id='NegativeIncrease',
              figure={
                  'data': data_negativeIncrease,
                  'layout': go.Layout(title='Number of Increased Negative Tests', xaxis_title="Date",
                                      yaxis_title="Number of cases")
              }
              ),
    html.H3('Pending Tests For COVID-19 in the US', style={'color': 'red'}),
    html.Div('This line chart represents the total number of pending tests for the corona virus in the United States.'),
    dcc.Graph(id='PendingCases',
              figure={
                  'data': data_pending,
                  'layout': go.Layout(title='Pending Tests', xaxis_title="Date",
                                      yaxis_title="Number of cases")
              }
              ),
    html.H3('Total Recovered Cases of COVID-19 in the US', style={'color': 'red'}),
    html.Div('This line chart represents the total number of recovered cases of the corona virus in the United States.'),
    dcc.Graph(id='RecoveredCases',
              figure={
                  'data': data_recoveredUS,
                  'layout': go.Layout(title='Total Recovered Cases', xaxis_title="Date",
                                      yaxis_title="Number of cases")
              }
              ),

    html.H3('Current Hospitalizations of COVID-19 in the US', style={'color': 'red'}),
    html.Div('This line chart represents the current hospitalizations of the corona virus in the United States.'),
    dcc.Graph(id='CurrentHospitalizations',
              figure={
                  'data': data_hospitalizedCurr,
                  'layout': go.Layout(title='Number of Current Hospitalizations', xaxis_title="Date",
                                      yaxis_title="Number of cases")
              }
              ),
    html.H3('Cumulative Hospitalizations of COVID-19 in the US', style={'color': 'red'}),
    html.Div('This line chart represents cumulative hospitalizations because of the corona virus in the United States.'),
    dcc.Graph(id='CumulativeHospitalizations',
              figure={
                  'data': data_hospitalizedCumul,
                  'layout': go.Layout(title='Number of Cumulative Hospitalizations', xaxis_title="Date",
                                      yaxis_title="Number of cases")
              }
              ),
    html.H3('Number of Increased Hospitalizations because of COVID-19 in the US', style={'color': 'red'}),
    html.Div('This line chart represents the number of increased hospitalizations because of the corona virus in the United States.'),
    dcc.Graph(id='HospitalizedIncrease',
              figure={
                  'data': data_hospitalizedIncrease,
                  'layout': go.Layout(title='Number of Increased Hospitalizations', xaxis_title="Date",
                                      yaxis_title="Number of cases")
              }
              ),
    html.H3('Cumulative Number of People in the ICU in the US', style={'color': 'red'}),
    html.Div('This line chart represents the cumulative number of people in the ICU because of the corona virus in the United States.'),
    dcc.Graph(id='CumulativeICU',
              figure={
                  'data': data_ICUCumulative,
                  'layout': go.Layout(title='Cumulative Number of People in the ICU', xaxis_title="Date",
                                      yaxis_title="Number of cases")
              }
              ),
    html.H3('Current Number of People in the ICU in the US', style={'color': 'red'}),
    html.Div('This line chart represents the current number of people in the ICU because of the corona virus in the United States.'),
    dcc.Graph(id='CurrentICU',
              figure={
                  'data': data_ICUCurrently,
                  'layout': go.Layout(title='Current Number of People in the ICU', xaxis_title="Date",
                                      yaxis_title="Number of cases")
              }
              ),
    html.H3('Current Ventilators Being Used in the US', style={'color': 'red'}),
    html.Div('This line chart represents the number of ventilators currently being used because of the corona virus in the United States.'),
    dcc.Graph(id='CurrentVentilators',
              figure={
                  'data': data_ventilatorsCurr,
                  'layout': go.Layout(title='Number of People Currently on a Ventilator', xaxis_title="Date",
                                      yaxis_title="Number of Ventilators Being Used")
              }
              ),


    html.H3('Number of Total Test Results Increase in the US', style={'color': 'red'}),
    html.Div('This line chart represents the total number of increased tests results because of the corona virus in the United States.'),
    dcc.Graph(id='TestResultsIncrease',
              figure={
                  'data': data_testResultsIncrease,
                  'layout': go.Layout(title='Number of Increased Tests Results', xaxis_title="Date",
                                      yaxis_title="Number of cases")
              }
              )

])


if __name__ == '__main__':
    app.run_server()
