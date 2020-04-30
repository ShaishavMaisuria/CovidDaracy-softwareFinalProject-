import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

# as you import the files it will run it back ground once you run this file so will see multiple charts when you run this program
from Plots import TotalDeathUs as tdus
from Plots import confirmed_US as cus

# Load CSV file from Datasets folder

app = dash.Dash()

# Line Chart

data_linechart = [go.Scatter(x=cus.date, y=tdus.usDeath, mode='lines', name='Death in US')]


# Layout
app.layout = html.Div(children=[
    html.H1(children='Python Dash',
            style={
                'textAlign': 'center',
                'color': '#ef3e18'
            }
            ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Line chart', style={'color': '#df1e56'}),
    html.Div('This line chart represent the Corona Virus confirmed cases of all reported cases in the given period.'),
    dcc.Graph(id='graph4',
              figure={
                  'data': data_linechart,
                  'layout': go.Layout(title='Corona Virus Confirmed Cases From 2020-01-22 to Till now',
                                      xaxis={'title': 'Date'}, yaxis={'title': 'Number of cases'})
              }
              )
])




if __name__ == '__main__':
    app.run_server()
