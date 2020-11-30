import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import dash_table

df = pd.read_csv("./data/timesData.csv")

layoutHome = html.Div([
    html.H1('HomePage',style={'textAlign': 'center','font-family':'sans-serif'}),
    html.Div(id='app-home-display-value'),
    dcc.Link('Table des données - TimesData', href='/apps/app1'),
    html.Br(),
    dcc.Link("Cas d'étude.", href='/apps/app2')
])

layout1 = html.Div([
    html.H1('Table des données',style={'textAlign': 'center','font-family':'sans-serif'}),
    #Standby#dcc.Dropdown(id='app-home-dropdown'),  
    dash_table.DataTable(
    export_format='csv',
    id='app-1-dropdown',
    columns=[{'id': c, 'name': c} for c in df.columns],
    data= df.to_dict('records'),
    #Style table as list view
    #style_as_list_view=True,
    fixed_rows={'headers': True},
    style_table={'overflowX': 'auto','overflowY': 'auto','maxHeight':'800px','maxWidth':'1600px'},
    #Cell dim + textpos
    style_cell_conditional=[{'height': 'auto',
        # all three widths are needed
        'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
        'whiteSpace': 'normal','textAlign':'center'}
    ],
    #Line strip
    style_data_conditional=[
        {
            'if': {'row_index': 'odd'},
            'backgroundColor': 'rgb(248, 248, 248)'
        }
    ],
    style_header={
        'backgroundColor': 'rgb(50, 50, 50)',
        'fontWeight': 'bold',
        'color':'white'},
),
html.Br(),
html.H1('Quel est la meilleure Université',style={'textAlign': 'center','font-family':'sans-serif'}),
dcc.Link('Back to Head', href='/apps/app1'),
html.Br(),
dcc.Link('Back to Home', href='/')
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