import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import dash_table

df = pd.read_csv("./data/timesData.csv")

layout1 = html.Div([
    html.H3('App 1'),
    dash_table.DataTable(
        id='timesData',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records')
),
    
    html.Div(id='app-1-display-value'),
    dcc.Link('Go to App 1', href='/apps/app1')
])

layout2 = html.Div([
    html.H3('App 2'),
    dcc.Dropdown(
        id='app-2-dropdown',
        options=[
            {'label': 'App 2 - {}'.format(i), 'value': i} for i in [
                'NYC', 'MTL', 'LA'
            ]
        ]
    ),
    html.Div(id='app-2-display-value'),
    dcc.Link('Go to App 1', href='/apps/app1')
])