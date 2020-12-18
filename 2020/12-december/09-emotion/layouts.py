#-----------------------------------------------------------------------------------------------------------------------------------------#
#                                                          IMPORT                                                                         #
#-----------------------------------------------------------------------------------------------------------------------------------------#

import sys
from my_import.my_lib import *
from my_import.my_func import get_top_n_words, tokenize , run_pipes , print_table
from my_import.my_var import md1 , md2 , md3 , md_source ,table0_brut, table0_pre ,table1_brut, table1_pre, freq_word_bar , emotion_hist , nav_bar , table0_pipe , table1_pipe 


#-----------------------------------------------------------------------------------------------------------------------------------------#
#                                                    LAYOUT HOME                                                                          #
#-----------------------------------------------------------------------------------------------------------------------------------------#

#-------------------------------------------------------DASH------------------------------------------------------------------------------#
layoutHome = html.Div(
                style={'width': '100%','height':'100%','color':'white','backgroundImage': 'url(../assets/pexels-jessica-lewis-583846.jpg)','background-attachment':'fixed','background-size': 'cover'},
                children=[
                    nav_bar,
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Div('La Roue des Emotions',style={'background-color':'Black','opacity':'0.65','font-size':'50px','textAlign':'center'}),
                    html.Section(
                        style={'padding-left':'8vw','padding-right':'8vw','background-color':'Black','opacity':'0.65'}, 
                        children=[
                                    md1,
                                    html.Div([
                                    dbc.Button("Page 1", color="primary",href="/apps/page1" ,id="loading-button"),
                                    dbc.Spinner(html.Div(id="loading-output"))]),
                                    html.Br(),
                                    md2,
                                    ##button data table
                                    html.Div([
                                    dbc.Button("Page 2", color="primary",href="/apps/page2" ,id="loading-button"),
                                    dbc.Spinner(html.Div(id="loading-output"))]),
                                    html.Br(),
                                    md3,
                                    dcc.Markdown('''## Critères de performance
Un dashboard Dash permettra de visualiser et de comparer les performances issues de différents classifiers.'''),
                                    html.Div([
                                    dbc.Button("Page 3", color="primary",href="/apps/page2" ,id="loading-button"),
                                    dbc.Spinner(html.Div(id="loading-output"))]),
                                    html.Br(),
                                    md_source,
                                    html.Br(),
                ])
    ])


#-----------------------------------------------------------------------------------------------------------------------------------------#
#                                                     LAYOUT ONE                                                                          #
#-----------------------------------------------------------------------------------------------------------------------------------------#

#------------------------------------------------------DATAFRAME--------------------------------------------------------------------------#


layout1 = html.Div(
            style={'width': '100%','height':'100%','background-position':'center center','background-size': 'cover','color':'white','backgroundImage': 'url(../assets/bg_default_wheel.png)','background-attachment':'fixed'},
            children=[
                nav_bar,
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
                html.Div('Data Frame', className = "app-header",style={'color':'black','font-size':'50px'}),
                html.Section(   
                    style={'padding-left':'7vw','padding-right':'7vw'}, 
                    children=[
                        html.Br(),
                        dbc.Tabs(children=[
                        dbc.Tab(table0_brut, label="Kaggle Data",tab_style={'background-color':'black','opacity':'0.70'},label_style={"color": "#00AEF9"},loading_state={'is_loading':'True'}),
                        dbc.Tab(table0_pre, label="Kaggle Data NLP",tab_style={'background-color':'black','opacity':'0.65'},label_style={"color": "#00AEF9"},loading_state={'is_loading':'True'}),
                        dbc.Tab(table1_brut, label="Yes Data",tab_style={'background-color':'black','opacity':'0.65'},label_style={"color": "#00AEF9"},loading_state={'is_loading':'True'}),
                        dbc.Tab(table1_pre, label="Yes Data NLP",tab_style={'background-color':'black','opacity':'0.65'},label_style={"color": "#00AEF9"},loading_state={'is_loading':'True'}),
                                    ]),
                        html.Br(),
                        html.Br(),
                        dcc.Graph(figure=freq_word_bar),
                        html.Br(),
                        dcc.Graph(figure=emotion_hist),
                        html.Br(),
                        html.Br(),
                        html.Article(style={'display':'flex','width':'20vw'},
                            children=[               
                                html.Div([
                                dbc.Button("Back to head", color="primary",href="/apps/page1" ,id="loading-button"),
                                dbc.Spinner(html.Div(id="loading-output"))]
                                        ),
                                html.Div(style={'margin-left':'0.5vw'},
                                        children=[
                                            dbc.Button("Back to home", color="primary",href="/" ,id="loading-button"),
                                            dbc.Spinner(html.Div(id="loading-output"))])
                                            ]),
                        html.Br(),
                        ])
])
#-----------------------------------------------------------------------------------------------------------------------------------------#
#                                                   LAYOUT TWO                                                                            #
#-----------------------------------------------------------------------------------------------------------------------------------------#

layout2 =  html.Div(
                style={'width': '100%','height':'100%','background-position':'center center','background-size': 'cover','color':'white','backgroundImage': 'url(../assets/bg_default_wheel.png)','background-attachment':'fixed'},
                children=[
                   nav_bar,
                   html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                html.Div('Dataframe of pipeline result', className = "app-header"),
                html.Section(   
                    style={'padding-left':'7vw','padding-right':'7vw'}, 
                    children=[
                    dbc.Tabs(children=[
                        dbc.Tab(table0_pipe, label="Kaggle Data",tab_style={'background-color':'black','opacity':'0.70'},label_style={"color": "#00AEF9"},loading_state={'is_loading':'True'}),
                        dbc.Tab(table1_pipe, label="Oui Data",tab_style={'background-color':'black','opacity':'0.65'},label_style={"color": "#00AEF9"},loading_state={'is_loading':'True'}),
                    ]),
                        html.Br(),
                        html.Br(),
                        html.Div('Input prediction made of Kaggle\'s dataset model', className = "app-header"),
                        dbc.Input(id="input", placeholder="Predict an emotion entering a single word", type="text"),
                        html.Br(),
                        dbc.Button("Submit", color="secondary",id='submit-val', n_clicks=0),
                        html.P(id="output"),
                        html.Div(id='app-2-display-value'),
                        html.Article(style={'display':'flex','heigh':'15vw','width':'20vw'},
                            children=[               
                                html.Div([
                                dbc.Button("Back to head", color="primary",href="/apps/page1" ,id="loading-button"),
                                dbc.Spinner(html.Div(id="loading-output"))]
                                        ),
                                html.Div(style={'margin-left':'0.5vw'},
                                        children=[
                                            dbc.Button("Back to home", color="primary",href="/" ,id="loading-button"),
                                            dbc.Spinner(html.Div(id="loading-output"))
                                            ])
                                ]),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                ])
])
#-----------------------------------------------------------------------------------------------------------------------------------------#
#                                                   LAYOUT TREE                                                                           #
#-----------------------------------------------------------------------------------------------------------------------------------------#

layout3 =  html.Div(
                style={'height': '320vh','color':'white','backgroundImage': 'url(../assets/pexels-jessica-lewis-583846.jpg)','background-attachment':'fixed'}, 
                children=[])