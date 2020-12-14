#-----------------------------------------------------------------------------------------------------------------------------------------#
#                                                          IMPORT                                                                         #
#-----------------------------------------------------------------------------------------------------------------------------------------#

import sys
from my_import.my_func import * 
from my_import.my_var import md1 , md2 , md3 , md_source

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
                                    dbc.Button("Page 2", color="primary",href="/apps/page1" ,id="loading-button"),
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

# df = pd.read_csv("./data/timesData.csv")
# df2016 = df[df.year == 2016].iloc[:50,:]
# df2016.world_rank = [int(each.replace('=','')) for each in df2016.world_rank]
# df2016 = df2016.dropna()
# df2016.international_students = [str(each).replace('%','') for each in df2016.international_students]
# df2016.rename(columns = {"international_students":'international_students_%'})
# df2016.num_students  = [float(each.replace(',','.')) for each in df2016.num_students]
# df2016['female_male_ratio'] = [str(each).split() for each in df2016.female_male_ratio]
# df2016.female_male_ratio = [(float(each[0]) / float(each[2])) for each in df2016.female_male_ratio] 
# df2016.female_male_ratio = pd.to_numeric(df2016.female_male_ratio, errors='coerce')
# df2016.international = pd.to_numeric(df2016.international, errors='coerce')
# df2016.income  = pd.to_numeric(df2016.income , errors='coerce')
# df2016.total_score  = pd.to_numeric(df2016.total_score , errors='coerce')
# df2016.international_students  = pd.to_numeric(df2016.international_students , errors='coerce')

#------------------------------------------------------GRAPH------------------------------------------------------------------------------#

#------------------------------------------------------FIGURE1----------------------------------------------------------------------------#
df1 = pd.read_csv('./data/emotion_final.csv')

x = df1.Text
y = df1.Emotion

freq_top = get_top_n_words(x,"up",100)


df_up = pd.DataFrame(freq_top, columns =['Word','Number of times'])
y_nbr = df_up['Number of times']
x_word = df_up['Word']

freq_p1 = go.Bar(
                x = x_word.head(30),
                y = y_nbr,
                name = "Le score universitaire pour le transfert de connaissances par pays",
                marker = dict(color = 'rgba(255, 87, 51, 0.5)', line = dict(color ='rgb(0,0,0)',width =2.5)),
                text = df_up['Word'])

freq_lay_p1 = go.Layout(barmode = "group",
                  title = 'Fréquence d’apparition des mots ',
                  yaxis = dict(title = 'word frequency'),
                  xaxis = dict(title = 'word rank'))
freq_word_bar = go.Figure(data = freq_p1 , layout = freq_lay_p1)


#------------------------------------------------------FIGURE2----------------------------------------------------------------------------#

#------------------------------------------------------FIGURE3----------------------------------------------------------------------------#

#-------------------------------------------------------DASH------------------------------------------------------------------------------#


layout1 = html.Div(
            style={'height': '320vh','color':'white','backgroundImage': 'url(../assets/pexels-jessica-lewis-583846.jpg)','background-attachment':'fixed'},
            children=[
                html.Div('Page 1',style={'text-align':'center','font-size':'40px','padding':'30px'}),
                dcc.Graph(
                    figure=freq_word_bar
                    ),
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
                children=[])
#-----------------------------------------------------------------------------------------------------------------------------------------#
#                                                   LAYOUT TREE                                                                           #
#-----------------------------------------------------------------------------------------------------------------------------------------#

layout3 =  html.Div(
                style={'height': '320vh','color':'white','backgroundImage': 'url(../assets/pexels-jessica-lewis-583846.jpg)','background-attachment':'fixed'}, 
                children=[])

    