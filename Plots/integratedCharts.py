#Author Shaishav Maisuria
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df1 = pd.read_csv('../Datasets/04-12-2020.csv').T
df2 = pd.read_csv('../Datasets/CoronaTimeSeries.csv.csv')

app = dash.Dash()

# Line Chart
line_df = df2
line_df['Date'] = pd.to_datetime(line_df['Da'
                                         'te'])
data_linechart = [go.Scatter(x=line_df['Date'], y=line_df['Confirmed'], mode='lines', name='Death')]


# Layout
app.layout = html.Div(children=[
    html.H1(children='Python Dash',
            style={
                'textAlign': 'center',
                'color': '#ef3e18'
            }
            ),
    html.Div('Web dashboard for Data Visualization using Python', style={'textAlign': 'center'}),
    html.Div('Coronavirus COVID-19 Global Cases -  1/22/2020 to 3/17/2020', style={'textAlign': 'center'}),
    html.Br(),
    html.Br(),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Interactive Bar chart', style={'color': '#df1e56'}),
    html.Div('This bar chart represent the number of confirmed cases in the first 20 countries of selected continent.'),
    dcc.Graph(id='graph1'),
    html.Div('Please select a continent', style={'color': '#ef3e18', 'margin':'10px'}),
    dcc.Dropdown(
        id='select-continent',
        options=[
            {'label': 'Asia', 'value': 'Asia'},
            {'label': 'Africa', 'value': 'Africa'},
            {'label': 'Europe', 'value': 'Europe'},
            {'label': 'North America', 'value': 'North America'},
            {'label': 'Oceania', 'value': 'Oceania'},
            {'label': 'South America', 'value': 'South America'}
        ],
        value='Europe'
    ),

    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Line chart', style={'color': '#df1e56'}),
    html.Div('This line chart represent the Corona Virus confirmed cases of all reported cases in the given period.'),
    dcc.Graph(id='graph4',
              figure={
                  'data': data_linechart,
                  'layout': go.Layout(title='Corona Virus Confirmed Cases From 2020-01-22 to 2020-03-17',
                                      xaxis={'title': 'Date'}, yaxis={'title': 'Number of cases'})
              }
              )
])


@app.callback(Output('graph1', 'figure'),
              [Input('select-continent', 'value')])
def update_figure(selected_continent):
    filtered_df = df1[df1['Continent'] == selected_continent]

    filtered_df = filtered_df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    new_df = filtered_df.groupby(['Country'])['Confirmed'].sum().reset_index()
    new_df = new_df.sort_values(by=['Confirmed'], ascending=[False]).head(20)
    data_interactive_barchart = [go.Bar(x=new_df['Country'], y=new_df['Confirmed'])]
    return {'data': data_interactive_barchart, 'layout': go.Layout(title='Corona Virus Confirmed Cases in '+selected_continent,
                                                                   xaxis={'title': 'Country'},
                                                                   yaxis={'title': 'Number of confirmed cases'})}


if __name__ == '__main__':
    app.run_server()
