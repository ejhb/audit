import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd
import dash_table


#-----------------------------------------------------------------------------------------------------------------------------------------#
#                                                   LAYOUT HOME                                                                            #
#-----------------------------------------------------------------------------------------------------------------------------------------#

layoutHome = html.Div([
    html.Div(
        className="app-header",
        children=[html.Div('HomePage',className="app-header--title")]),
    html.Div(id='app-home-display-value'),
    dcc.Link('Table des données - TimesData', href='/apps/app1'),
    html.Br(),
    dcc.Link("Cas d'étude.", href='/apps/app2')
])

#-----------------------------------------------------------------------------------------------------------------------------------------#
#                                                   LAYOUT ONE                                                                            #
#-----------------------------------------------------------------------------------------------------------------------------------------#
#------------------------------------------------------TABLE------------------------------------------------------------------------------#
df = pd.read_csv("./data/timesData.csv")
df2016 = df[df.year == 2016].iloc[:50,:]
df2016.world_rank = [int(each.replace('=','')) for each in df2016.world_rank]
df2016 = df2016.dropna()
df2016.international_students = [str(each).replace('%','') for each in df2016.international_students]
df2016.rename(columns = {"international_students":'international_students_%'})
df2016['female_male_ratio'] = [str(each).split() for each in df2016.female_male_ratio]
df2016.female_male_ratio = [(float(each[0]) / float(each[2])) for each in df2016.female_male_ratio] 
df2016.female_male_ratio = pd.to_numeric(df2016.female_male_ratio, errors='coerce')
df2016

#-------------------------------------------------------DASH------------------------------------------------------------------------------#
layout1 = html.Div([
    # html.Div(
    #     className="app-header",
    #     children=[html.Div('Data Table',className="app-header--title")]),
    #Standby#dcc.Dropdown(id='app-home-dropdown'),  
    dash_table.DataTable(
    export_format='csv',
    id='app-1-dropdown',
    columns=[{'id': c, 'name': c} for c in df.columns],
    data= df2016.to_dict('records') ,
    #Style table as list view
    #style_as_list_view=True,
    fixed_rows={'headers': True},
    fixed_columns={'headers': True, 'data' :1},
    style_cell={
                'fontFamily': 'Open Sans',
                'textAlign': 'center',
                'height': '60px',
                'padding': '2px 22px',
                'whiteSpace': 'inherit',
                'overflow': 'hidden',
                'textOverflow': 'ellipsis',},
    style_table={
                'maxHeight': '50ex',
                'overflowY': 'auto',
                'overflowx': 'auto',
                'width': '97%',
                'minWidth': '97%',
                'margin-left':'auto',
                'margin-right':'auto',
            },
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
dcc.Link('Back to Home', href='/'),
dbc.Button("Primary", color="primary", className="mr-1"),
])

#-----------------------------------------------------------------------------------------------------------------------------------------#
#                                                   LAYOUT TWO                                                                            #
#-----------------------------------------------------------------------------------------------------------------------------------------#

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