import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd
import dash_table

#-----------------------------------------------------------------------------------------------------------------------------------------#
#                                            LAYOUT HOME                                                                            #
#-----------------------------------------------------------------------------------------------------------------------------------------#

layoutHome = html.Div(style={'height': '130vh','color':'white', 'backgroundImage': 'url(../assets/pexels-jessica-lewis-583846.jpg)'},children=[
    html.Div(id='app-home-display-value'),
    html.Div(
        style={'padding-top':'30px'},
        className="app-header",
        children=[html.Div('De toutes les universités, quelles sont les meilleures ?',className="app-header--title")]),
            html.Section(style={'height':'70vh', 'display':'flex', 'justify-content':' space-around'}, 
            children=[
                html.Div(style={'height':'70vh', 'width':'90vw','padding-top':'30px'}, 
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
* Plusieurs graphiques mettant en évidences des corrélations entre certains critères (par exemple : qualité de la recherche en fonction du rand mondial du classement des universités etc..)'''
                                    ),
        ##button data table
                html.Div([
                dbc.Button("Data Table", color="primary",href="/apps/page1" ,id="loading-button"),
                dbc.Spinner(html.Div(id="loading-output")),]
                        ),
            dcc.Markdown('''#### 2eme page

Cette page permettra d'afficher les résultats issus de l'ACP. On pourra ainsi y trouver des graphiques ainsi que des paragraphes de textes mettant en évidence des variables explicatives (par exemple la valeur propre, la proportion, le cumulé, les composantes principales (CP), les scores, les distances).

1. Vous mettrez en ligne votre Dashboard Dash sur le serveur Cloud Heroku
                    '''),
                html.Div([
                dbc.Button("Cas d'étude", color="primary",href="/apps/page2" ,id="loading-button"),
                dbc.Spinner(html.Div(id="loading-output")),]
                        ),
        dcc.Markdown('''### Modalités d'évaluation
Un rendu individuel est demandé. Vous pourrez travailler en groupe de 5 ou 6. Le rendu final devra être envoyé le vendredi 4 décembre à 15h30.          '''),
                html.Div([
                dbc.Button("Page to remove(testing-zone)", color="primary",href="/apps/page3" ,id="loading-button"),
                dbc.Spinner(html.Div(id="loading-output")),]
                )
        ])
    ])
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
    html.Div(
        className="app-header",
        children=[html.Div('Data Table',className="app-header--title")]),
    dash_table.DataTable(
    id='app-1-dropdown',
    columns=[{'id': c, 'name': c} for c in df2016.columns],
    data= df2016.to_dict('records') ,
    #Style table as list view
    #style_as_list_view=True,
    fixed_rows={'headers': True},
    fixed_columns={'headers': True, 'data' :1},
    style_table={
                'maxHeight': '50ex',
                'overflow': 'auto',
                'width': '90%',
                'minWidth': '90%',
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
dbc.Button("Back to head ", color="primary", className="mr-1", href="/apps/app1"),
html.Br(),
    html.Div(
    [
        dbc.Button("Back to home", color="primary",href="/" ,id="loading-button"),
        dbc.Spinner(html.Div(id="loading-output")),
    ]
)
])

#-----------------------------------------------------------------------------------------------------------------------------------------#
#                                                   LAYOUT TWO                                                                            #
#-----------------------------------------------------------------------------------------------------------------------------------------#

layout2 =  html.Div(style={ 'height': '70vh', 'backgroundImage': 'url(../assets/pexels-jessica-lewis-583846.jpg)'} , children=[

    ]),  
#-----------------------------------------------------------------------------------------------------------------------------------------#
#                                                   LAYOUT TREE                                                                           #
#-----------------------------------------------------------------------------------------------------------------------------------------#

layout3 =  html.Div(style={ 'height': '70vh', 'backgroundImage': 'url(../assets/pexels-jessica-lewis-583846.jpg)'} , children=[

    ]),  