#-----------------------------------------------------------------------------------------------------------------------------------------#
#                                                          IMPORT                                                                         #
#-----------------------------------------------------------------------------------------------------------------------------------------#

import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table
import plotly.graph_objs as go
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd

#-----------------------------------------------------------------------------------------------------------------------------------------#
#                                                    LAYOUT HOME                                                                          #
#-----------------------------------------------------------------------------------------------------------------------------------------#

#-------------------------------------------------------DASH------------------------------------------------------------------------------#
layoutHome = html.Div(
                style={'height': '130vh','color':'white','backgroundImage': 'url(../assets/pexels-jessica-lewis-583846.jpg)','background-attachment':'fixed'},
                children=[
                    html.Div(id='app-home-display-value'),
                    html.Div(
                        style={'padding-top':'30px'},
                        className="app-header",
                        children=[
                            html.Div('De toutes les universités, quelles sont les meilleures ?',className="app-header--title")]),
                            html.Section(
                                style={'height':'70vh', 'display':'flex', 'justify-content':' space-around'}, 
                                children=[
                                    html.Div(
                                        style={'height':'70vh', 'width':'80vw','padding-top':'30px','margin-top':'2vh'}, 
                                        children=[
                                            dcc.Markdown('''## Contexte du projet
### Classement des universités

Le classement des universités est une pratique difficile, politique et controversée. Il existe des centaines de systèmes de classement universitaires nationaux et internationaux différents, dont beaucoup sont en désaccord les uns avec les autres.

**Le Times Higher Education World University Ranking** est largement considéré comme l'une des mesures universitaires les plus influentes et les plus largement observées. Fondée au Royaume-Uni en 2010, elle a été critiquée pour sa commercialisation et pour avoir "affaibli" les établissements non anglophones.

### Analyse en Composantes Principales
**Pour vous aider dans votre analyse du jeux de données, vous réaliserez une Analyse en Composantes Principales.**

Cette analyse permettra de répondre à certaines questions du type : quelles ressemblances peut-il y avoir d'une université à une autre. Quelles ressemblances existent-il entre différents critères d'évaluation des universités ? Vous pourrez ainsi définir quand est-ce que 2 universités se ressemblent et quand est-ce qu'elles se ressemblent du point de vue de l'ensemble des colonnes (c'est-à-dire des critères d'évaluation du Times Higher Education World University Ranking).

Est-il possible de faire un bilan des ressemblances ? ( Vous chercherez ici à faire une typologie, une partition des universités, c'est-à-dire à construire des groupes d'universités homogènes du point de vue de l'ensemble des variables. A l'intérieur d'un groupe, les individus se ressemblent et d'un groupe à l'autre ils sont différents.
### Modalités pédagogiques
1. Réaliser une veille sur la librairie Dash.
2. Faire une analyse du jeu de données correspondant au classement des 50 meilleures universités en 2016.
3. Réaliser une Analyse en Composantes Principales (vous pourrez vous appuyer sur la librairie Scikit-Learn) https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html
4. Mettre en place un Dashbord Dash multi-pages permettant de répondre à la question initiale : De toutes les universités du monde, quelles sont les meilleures ? La première page de votre Dashbord mettra en évidence l'analyse des données des 50 meilleures universités de l'année 2016 (avant L'ACP).
#### 1ère page

* Dans cette première page se trouvera notamment une table des données des 50 meilleurs universités de l'année 2016 avec un bouton de téléchargement permettant de télécharger un tableau .csv des données.
* Plusieurs graphiques mettant en évidences des corrélations entre certains critères (par exemple : qualité de la recherche en fonction du rand mondial du classement des universités etc..)'''),
        ##button data table
                html.Div([
                dbc.Button("Data Table", color="primary",href="/apps/page1" ,id="loading-button"),
                dbc.Spinner(html.Div(id="loading-output"))]),
                dcc.Markdown('''#### 2eme page

Cette page permettra d'afficher les résultats issus de l'ACP. On pourra ainsi y trouver des graphiques ainsi que des paragraphes de textes mettant en évidence des variables explicatives (par exemple la valeur propre, la proportion, le cumulé, les composantes principales (CP), les scores, les distances).

1. Vous mettrez en ligne votre Dashboard Dash sur le serveur Cloud Heroku
                    '''),
                html.Div([
                dbc.Button("Cas d'étude", color="primary",href="/apps/page2" ,id="loading-button"),
                dbc.Spinner(html.Div(id="loading-output"))]
                        ),
        dcc.Markdown('''### Modalités d'évaluation
Un rendu individuel est demandé. Vous pourrez travailler en groupe de 5 ou 6. Le rendu final devra être envoyé le vendredi 4 décembre à 15h30.'''),
                html.Div([
                dbc.Button("Page to remove(testing-zone)", color="primary",href="/apps/page3" ,id="loading-button"),
                dbc.Spinner(html.Div(id="loading-output"))])
        ])
    ])
])

#-----------------------------------------------------------------------------------------------------------------------------------------#
#                                                     LAYOUT ONE                                                                          #
#-----------------------------------------------------------------------------------------------------------------------------------------#

#------------------------------------------------------DATAFRAME--------------------------------------------------------------------------#

df = pd.read_csv("./data/timesData.csv")
df2016 = df[df.year == 2016].iloc[:50,:]
df2016.world_rank = [int(each.replace('=','')) for each in df2016.world_rank]
df2016 = df2016.dropna()
df2016.international_students = [str(each).replace('%','') for each in df2016.international_students]
df2016.rename(columns = {"international_students":'international_students_%'})
df2016.num_students  = [float(each.replace(',','.')) for each in df2016.num_students]
df2016['female_male_ratio'] = [str(each).split() for each in df2016.female_male_ratio]
df2016.female_male_ratio = [(float(each[0]) / float(each[2])) for each in df2016.female_male_ratio] 
df2016.female_male_ratio = pd.to_numeric(df2016.female_male_ratio, errors='coerce')
df2016.international = pd.to_numeric(df2016.international, errors='coerce')
df2016.income  = pd.to_numeric(df2016.income , errors='coerce')
df2016.total_score  = pd.to_numeric(df2016.total_score , errors='coerce')
df2016.international_students  = pd.to_numeric(df2016.international_students , errors='coerce')

#------------------------------------------------------GRAPH------------------------------------------------------------------------------#

#------------------------------------------------------FIGURE1----------------------------------------------------------------------------#
df2016_heat = df2016[['international','num_students','student_staff_ratio','international_students','female_male_ratio','teaching','research','citations','income','total_score']]
corr = df2016_heat.corr()

trace_heat = go.Heatmap(
                   z=corr.values,
                   x=corr.index.values,
                   y=corr.columns.values,
                   opacity = 0.95,
                   colorscale='Viridis')

heat_layout = go.Layout(
                    height=500,
                    font=dict(
                        family="sans serif",
                        size=16,
                        color="white"),
                    paper_bgcolor='rgba(0,0,0,0.65)',
                    plot_bgcolor='rgba(0,0,0,1)')

heat_lay1 = go.Figure(data = trace_heat,layout=heat_layout)
#------------------------------------------------------FIGURE2----------------------------------------------------------------------------#
scat_matrix = go.Splom(
                dimensions=[dict(label='teaching',
                                 values=df2016['teaching']),
                            dict(label='research',
                                 values=df2016['research']),
                            dict(label='citations',
                                 values=df2016['citations']),
                            dict(label='income',
                                 values=df2016['income']),
                            dict(label='total_score',
                                 values=df2016['total_score'])     
                                 ],
                text=df2016['world_rank'],
                marker=dict(showscale=False, # colors encode categorical variables
                            # line_color='white', line_width=0.5
                            )
                )

scat_matrix_layout = go.Layout(
                    title="Les columns teaching, research, citations, income total_score sont-elles corrélées?",
                    height=800,
                    font=dict(
                        family="sans serif",
                        size=14,
                        color="white"),
                    paper_bgcolor='rgba(0,0,0,0.65)',
                    plot_bgcolor='rgba(0,0,0,0.65)')
scat_matrix_lay1 = go.Figure(data = scat_matrix,layout=scat_matrix_layout)
#------------------------------------------------------FIGURE3----------------------------------------------------------------------------#
scat_matrix2 = go.Splom(
                dimensions=[dict(label='inter',
                                 values=df2016['international']),
                            dict(label='num_stud',
                                 values=df2016['num_students']),
                            dict(label='stud_staff_ratio',
                                 values=df2016['student_staff_ratio']),
                            dict(label='inter_stud',
                                 values=df2016['international_students']),
                            dict(label='f_m_ratio',
                                 values=df2016['female_male_ratio'])     
                                 ],
                text=df2016['world_rank'],
                marker=dict(showscale=False, # colors encode categorical variables
                            # line_color='white', line_width=0.5
                            )
                )

scat_matrix2_layout = go.Layout(
                    title="Les columns International, num_students, student_staff_ratio, international_students et female_male_ratio sont-elles corrélées?",
                    height=800,
                    font=dict(
                        family="sans serif",
                        size=13,
                        color="white"),
                    paper_bgcolor='rgba(0,0,0,0.60)',
                    plot_bgcolor='rgba(0,0,0,0.60)',
                    )
scat_matrix2_lay1 = go.Figure(data = scat_matrix2,layout=scat_matrix2_layout)
#-------------------------------------------------------DASH------------------------------------------------------------------------------#
layout1 = html.Div(
            style={'height': '320vh','color':'white','backgroundImage': 'url(../assets/pexels-jessica-lewis-583846.jpg)','background-attachment':'fixed'},
            children=[
                html.Br(),
                html.Div(
                    className="app-header",
                    children=[html.Div('Data Table',className="app-header--title")]),
                        html.Div(
                            style={'padding-left':'5vw','padding-right':'5vw','margin-bottom':'2vh'},
                            children=[
                                dash_table.DataTable(
                                    columns=[{'id': c, 'name': c} for c in df2016.columns],
                                    data= df2016.to_dict('records'),
                                    #Style table as list view
                                    #style_as_list_view=True,
                                    fixed_rows={'headers': True},
                                    fixed_columns={'headers': True, 'data' :1},
                                    export_format='csv',
                                    style_table={'opacity':'0.80',
                                                'maxHeight': '50ex',
                                                'overflowX': 'auto',
                                                'overflowY': 'auto',
                                                'width': '100%',
                                                'minWidth': '100%',
                                                'margin-left':'auto',
                                                'margin-right':'auto'},
                                    #Cell dim + textpos
                                    style_cell_conditional=[{'height': 'auto',
                                        # all three widths are needed
                                        'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                                        'whiteSpace': 'normal','textAlign':'center'}],
                                    #Line strip
                                    style_cell={'color': 'black'},
                                    style_data_conditional=[{
                                            'if': {'row_index': 'odd'},
                                            'backgroundColor': 'rgb(248, 248, 248)'}],
                                    style_header={
                                        'backgroundColor': 'rgb(50, 50, 50)',
                                        'fontWeight': 'bold',
                                        'color':'white'}),
                                ]),
                html.H1('Matrice de corrélation',style={'textAlign': 'center','font-family':'sans-serif','margin-bottom':'2vh'}),
                #Graph section
                html.Div(style={'padding-left':'15vw','padding-right':'15vw'},children=[
                dcc.Graph(
                      id ='example-graph-1-1',
                      figure = heat_lay1
                      )
                      ]),
                html.Div(style={'padding-left':'5vw','padding-right':'5vw','margin-bottom':'5vh'},
                        children=[
                  ## Fig 1 : Correlation Matrix
                    html.Br(),
                    dcc.Graph(
                      id='example-graph-1-1',
                      figure=scat_matrix_lay1
                      ),
                    html.Br(),
                    dcc.Graph(
                      id='example-graph-1-1',
                      figure=scat_matrix2_lay1
                      ),
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
df1 = pd.read_csv('../data/emotion_final.csv')
df1

layout2 =  html.Div(
                style={'height': '320vh','color':'white','backgroundImage': 'url(../assets/pexels-jessica-lewis-583846.jpg)','background-attachment':'fixed'},
                children=[
                    dash_table.DataTable(
                                    columns=[{'id': c, 'name': c} for c in df1.columns],
                                    data= df1.to_dict('records'),
                ]))
#-----------------------------------------------------------------------------------------------------------------------------------------#
#                                                   LAYOUT TREE                                                                           #
#-----------------------------------------------------------------------------------------------------------------------------------------#

layout3 =  html.Div(
                style={'height': '320vh','color':'white','backgroundImage': 'url(../assets/pexels-jessica-lewis-583846.jpg)','background-attachment':'fixed'}, 
                children=[])

    