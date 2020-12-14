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
                style={'height': '220vh','color':'white','backgroundImage': 'url(../assets/pexels-jessica-lewis-583846.jpg)','background-attachment':'fixed'},
                children=[
                    html.Div(
                        style={'padding-top':'30px'}, 
                        className="app-header",
                        children=[
                            html.Div('La roue des émotions',className="app-header--title")]),
                            html.Section(
                                style={'height':'70vh', 'display':'flex', 'justify-content':' space-around'}, 
                                children=[
                                    html.Div(
                                        style={'height':'70vh', 'width':'80vw','padding-top':'30px','margin-top':'2vh','margin-bop':'2vh'}, 
                                        children=[
                                            dcc.Markdown('''## Contexte du projet
Depuis quelques années, les dispositifs de communication médiatisée par ordinateur (CMO) sont massivement utilisés, aussi bien dans les activités professionnelles que personnelles. Ces dispositifs permettent à des participants distants physiquement de communiquer. La plupart implique une communication écrite médiatisée par ordinateur (CEMO) : forums de discussion, courrier électronique, messagerie instantanée. Les participants ne s’entendent pas et ne se voient pas mais peuvent communiquer par l’envoi de messages écrits, qui combinent, généralement, certaines caractéristiques des registres écrit et oral (Marcoccia, 2000a ; Marcoccia, Gauducheau, 2007 ; Riva, 2001).

Imaginez que vous souhaitez savoir ce qui se passe derrière votre écran d'ordinateur, quels sont vos contacts les plus actifs et quelle est leur personnalité (pas banal comme question !!). Vous allez alors vous lancer dans l’analyse de leur narration et tenter d’extraire quelle émotion se dégage de chacune des phrases.

Chez Simplon nous utilisons tous les jours des outils de discussion textuels et nous construisons nos relations sociales et professionnelles autour de ces dispositifs. Pour entretenir des rapports sociaux stables, sereins, de confiance et efficaces, au travers des outils de communication écrites, lorsqu'il n'est pas possible d'avoir la visio (avec caméra), il est nécessaire de détecter des éléments "clés" dans les channels de discussions / mails qui nous permettront de déceler de la colère, de la frustration, de la tristesse ou encore de la joie de la part d'un collègue ou d'un amis pour adapter nos relations sociales. En tant qu'expert en data science, nous allons vous demander de développer un modèle de machine learning permettant de classer les phrases suivant l'émotion principale qui en ressort.

Pour des questions d’ordre privé, nous ne vous demanderons pas de nous communiquer les conversations provenant de votre réseau social favori ou de vos emails mais nous allons plutôt vous proposer deux jeux de données contenant des phrases, ces fichiers ayant déjà été annoté.

Vous devrez proposer plusieurs modèles de classification des émotions et proposer une analyse qualitative et quantitative de ces modèles en fonction de critères d'évaluation. Vous pourrez notamment vous appuyer sur les outils de reporting des librairies déjà étudiées. Vous devrez investiguer aux travers de librairies d'apprentissage automatique standards et de traitement automatique du langage naturel comment obtenir les meilleurs performance de prédiction possible en prenant en compte l'aspect multi-class du problème et en explorant l'impact sur la prédiction de divers prétraitement tel que la suppression des stop-words, la lemmatisation et l'utilisation de n-grams, et différente approche pour la vectorisation.

**Vous devrez travailler dans un premier temps avec le jeu de données issu de Kaggle pour réaliser vos apprentissage et l'évaluation de vos modèles.**

**Dans l'objectif d'enrichir notre prédictions nous souhaitons augmenter notre jeux de donneés. Vous devrez donc travailler dans un deuxième temps avec le jeux de données fournie, issue de data.world afin de :**

**1. Comparez d'une part si les résultats de classification sur votre premier jeu de données sont similaires avec le second. Commenter.**

**2. Combiner les deux jeux de données pour tenter d'améliorer vos résultats de prédiction.**

**3. Prédire les nouvelles émotions présentes dans ce jeu de données sur les messages du premier, et observer si les résultats sont pertinents.**

Vous devrez ensuite présenter vos résultats sous la forme d'un dashboard multi-pages Dash. **La première page du Dashboard sera dédiée à l'analyse et au traitement des données.** Vous pourrez par exemple présenter les données "brut" sous la forme d'un tableau puis les données pré-traitées dans le même tableau avec un bouton ou menu déroulant permettant de passer d'un type de données à un autre (n'afficher qu'un échantillon des résultats, on dans une fenêtre "scrollable"). Sur cette première page de dashboard seront accessibles vos graphiques ayant trait à votre première analyse de données (histogramme, bubble chart, scatterplot etc), notamment

**1. L'histogramme représentant la fréquence d’apparition des mots (commenter)**

**2. L'histogramme des émotions (commenter)**'''),
                    html.Div([
                    dbc.Button("Page 1", color="primary",href="/apps/page1" ,id="loading-button"),
                    dbc.Spinner(html.Div(id="loading-output"))]),
                    html.Br(),
                    dcc.Markdown('''
**Une deuxième page du Dashboard sera dédiée aux résultats issues des classifications . Il vous est demandé de comparer les résultats, d'au moins 5 classifiers, présentés dans un tableau permettant de visualiser vos mesures.** Sur cette page de dashboard pourra se trouver par exemple, des courbes de rappel de précision (permette de tracer la précision et le rappel pour différents seuils de probabilité), un rapport de classification (un rapport de classification visuel qui affiche la precision, le recall, le f1-score, support, ou encore une matrice de confusion ou encore une graphique permettant de visualiser les mots les plus représentatif associé à chaque émotions.**Héberger le dashboard sur le cloud de visualisation de données Héroku (https://www.heroku.com/).**

**BONUS Créer une application client/serveur permettant à un utilisateur d'envoyer du texte via un champ de recherche (ou un fichier sur le disque du client) et de lui renvoyer l'émotion du texte envoyé.**

**(Bonus du bonus)** la roue des émotions du document (exemple: quelle proportion de chacune des émotions contient le document ?)'''),
        ##button data table
                html.Div([
                dbc.Button("Page 2", color="primary",href="/apps/page1" ,id="loading-button"),
                dbc.Spinner(html.Div(id="loading-output"))]),
                html.Br(),
                dcc.Markdown('''## Modalités pédagogiques
Vos travaux devront être “poussés” sur Github et sur Heroku au plus tard le **Jeudi 17 Décembre à 17h30** (les liens seront accessibles via Simplonline).

**Les rendus tardifs ne seront pas pris en compte et les compétences ne seront donc pas validées !**

Travaille en groupe de 5/6 + rôles durée: 7 jours
                    '''),
        dcc.Markdown('''## Critères de performance
Un dashboard Dash permettra de visualiser et de comparer les performances issues de différents classifiers.'''),
                html.Div([
                dbc.Button("Page 3", color="primary",href="/apps/page2" ,id="loading-button"),
                dbc.Spinner(html.Div(id="loading-output"))]),
                html.Br(),
                html.Div([
                dbc.Button("Page 4", color="primary",href="/apps/page3" ,id="loading-button"),
                dbc.Spinner(html.Div(id="loading-output"))]),
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

#------------------------------------------------------FIGURE2----------------------------------------------------------------------------#

#------------------------------------------------------FIGURE3----------------------------------------------------------------------------#

#-------------------------------------------------------DASH------------------------------------------------------------------------------#
layout1 = html.Div(
            style={'height': '320vh','color':'white','backgroundImage': 'url(../assets/pexels-jessica-lewis-583846.jpg)','background-attachment':'fixed'},
            children=[
                    html.Div('Page 1',style={'text-align':'center','font-size':'40px','padding':'30px'}),
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

    