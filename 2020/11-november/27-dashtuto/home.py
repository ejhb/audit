import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import dash_table

app.larout = html.Div

layout1 = html.Div([
    html.H3('Table des données TimesData'),
    dash_table.DataTable(
        id='timesData',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records')
),
    
    html.Div(id='app-1-display-value'),
    dcc.Link('Back to head.', href='/apps/app1')
])