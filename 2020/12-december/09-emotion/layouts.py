#-----------------------------------------------------------------------------------------------------------------------------------------#
#                                                          IMPORT                                                                         #
#-----------------------------------------------------------------------------------------------------------------------------------------#

import sys
from my_import.my_lib import *
from my_import.my_func import get_top_n_words, tokenize , run_pipes , print_table
from my_import.my_var import md1 , md2 , md3 , md_source ,table0_brut , table0_pre , freq_word_bar

#-----------------------------------------------------------------------------------------------------------------------------------------#
#                                                    LAYOUT HOME                                                                          #
#-----------------------------------------------------------------------------------------------------------------------------------------#

#-------------------------------------------------------DASH------------------------------------------------------------------------------#
layoutHome = html.Div(
                style={'height': '220vh','color':'white','backgroundImage': 'url(../assets/pexels-jessica-lewis-583846.jpg)','background-attachment':'fixed'},
                children=[
                    html.Div('La Roue des Emotions',style={'text-align':'center','font-size':'40px','padding':'30px'}),
                    html.Section(
                        style={'height':'70vh', 'display':'flex', 'justify-content':' space-around'}, 
                        children=[
                            html.Div(
                                style={'height':'70vh', 'width':'80vw','margin-top':'2vh','margin-bop':'2vh'}, 
                                children=[md1,
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
                                    html.Div([
                                    dbc.Button("Page 4", color="primary",href="/apps/page3" ,id="loading-button"),
                                    dbc.Spinner(html.Div(id="loading-output"))]),
                                    md_source
                
        ])
    ])
])

#-----------------------------------------------------------------------------------------------------------------------------------------#
#                                                     LAYOUT ONE                                                                          #
#-----------------------------------------------------------------------------------------------------------------------------------------#

#------------------------------------------------------DATAFRAME--------------------------------------------------------------------------#


layout1 = html.Div(
            style={'height': '320vh','color':'white','backgroundImage': 'url(../assets/pexels-jessica-lewis-583846.jpg)','background-attachment':'fixed'},
            children=[
                html.Div('Page 1', className = "app-header"),
                html.Section(   
                    style={'padding-left':'5vw','padding-right':'5vw','margin-bottom':'2vh'}, 
                    children=[
                        table0_brut,
                        html.Br(),
                        html.Br(),
                        dcc.Graph(figure=freq_word_bar),
                        table0_pre
                        ]),
                        html.Article(style={'padding-left':'5vw','display':'flex','width':'20vw'},
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
                                    ])
                        
])
#-----------------------------------------------------------------------------------------------------------------------------------------#
#                                                   LAYOUT TWO                                                                            #
#-----------------------------------------------------------------------------------------------------------------------------------------#

layout2 =  html.Div(
                style={'height': '320vh','color':'white','backgroundImage': 'url(../assets/pexels-jessica-lewis-583846.jpg)','background-attachment':'fixed'},
                children=[dbc.Tabs(
    [
        dbc.Tab(table0_brut, label="Tab 1"),
        dbc.Tab(table0_pre, label="Tab 2"),
    ]
) ]
)
#-----------------------------------------------------------------------------------------------------------------------------------------#
#                                                   LAYOUT TREE                                                                           #
#-----------------------------------------------------------------------------------------------------------------------------------------#

layout3 =  html.Div(
                style={'height': '320vh','color':'white','backgroundImage': 'url(../assets/pexels-jessica-lewis-583846.jpg)','background-attachment':'fixed'}, 
                children=[])

    