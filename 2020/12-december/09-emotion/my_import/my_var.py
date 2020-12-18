#-----------------------------------------------------------------------------------------------------------------------------------------#
#                                                          IMPORT                                                                         #
#-----------------------------------------------------------------------------------------------------------------------------------------#

from my_import.my_lib import *
from my_import.my_func import get_top_n_words, tokenize , run_pipes , print_table
#------------------------------------------------------DATAFRAME--------------------------------------------------------------------------#
df0_brut = pd.read_csv('./data/kaggle_emotion.csv')
df0_pre = pd.read_csv('./data/kaggle_emotion_pre.csv')
df1_brut = pd.read_csv('./data/yes_emotion.csv')
df1_pre = pd.read_csv('./data/yes_emotion_pre.csv')
df0_pipe = pd.read_csv('./data/kaggle_pre.csv')
df1_pipe = pd.read_csv('./data/yes_pre.csv')

# df0_pre.rename(columns={'Unnamed: 0': 'id_auto'}, inplace=True)
# df0_pre.drop(columns=['id_auto'])
# # df0_pre = pd.read_csv('./data/emotion_final.csv')
# # exclude = set(string.punctuation) # exclude = punctuation strings
# # stop_word = stopwords.words('english') # we choosing stop words of english dict
# # stop_word_punct = stop_word.extend(exclude) # we add strings punctions to stop word dict
# # lemma = WordNetLemmatizer()
# # stemmer = SnowballStemmer("english") # we choosing the language english for the stemmization 
# # porter = PorterStemmer() 
# # lancaster=LancasterStemmer()

# # df0_pre['Text'] = df0_pre.apply(lambda row: word_tokenize(row['Text']), axis=1) # Tokenization
# # df0_pre['Text'] = df0_pre['Text'].apply(lambda x: [item for item in x if item not in stop_word]) # Stop wordization :) coucou anne-laure
# # df0_pre['Text'] = [[lemma.lemmatize(word) for word in each if word not in stop_word] for each in df0_pre['Text']]  # Lemmization
# # # df_pre['Text'] = df1['Text'].apply(lambda x: [stemmer.stem(y) for y in x]) # Stem every word. with snowball('english')
# # # df_pre['Text'] = df1['Text'].apply(lambda x: [porter.stem(y) for y in x]) # Stem every word. with porter
# # # df_pre['Text'] = df1['Text'].apply(lambda x: [lancaster.stem(y) for y in x]) # Stem every word. with lancaster
# # dz = df0_pre['Text']
# # dz = [[' '.join(i)][0] for i in dz] 
# # df0_pre['Text'] = dz
#-------------------------------------------------------INPUTPRED--------------------------------------------------------------------------#
targets = df0_brut['Emotion']
corpus = df0_brut['Text']
X_train, X_test, y_train, y_test = train_test_split(corpus, targets, random_state=0)

pipe0 = Pipeline([
    ('vect', CountVectorizer()),
    ('sgd', SGDClassifier()),
    ])
pipe0.fit(X_train, y_train)


#-------------------------------------------------------MARKDOWN--------------------------------------------------------------------------#
md1= dcc.Markdown('''## Contexte du projet
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

**2. L'histogramme des émotions (commenter)**''')

md2 = dcc.Markdown('''
**Une deuxième page du Dashboard sera dédiée aux résultats issues des classifications . Il vous est demandé de comparer les résultats, d'au moins 5 classifiers, présentés dans un tableau permettant de visualiser vos mesures.** Sur cette page de dashboard pourra se trouver par exemple, des courbes de rappel de précision (permette de tracer la précision et le rappel pour différents seuils de probabilité), un rapport de classification (un rapport de classification visuel qui affiche la precision, le recall, le f1-score, support, ou encore une matrice de confusion ou encore une graphique permettant de visualiser les mots les plus représentatif associé à chaque émotions.**Héberger le dashboard sur le cloud de visualisation de données Héroku (https://www.heroku.com/).**

**BONUS Créer une application client/serveur permettant à un utilisateur d'envoyer du texte via un champ de recherche (ou un fichier sur le disque du client) et de lui renvoyer l'émotion du texte envoyé.**

**(Bonus du bonus)** la roue des émotions du document (exemple: quelle proportion de chacune des émotions contient le document ?)''')
md3 = dcc.Markdown('''## Modalités pédagogiques
Vos travaux devront être “poussés” sur Github et sur Heroku au plus tard le **Jeudi 17 Décembre à 17h30** (les liens seront accessibles via Simplonline).

**Les rendus tardifs ne seront pas pris en compte et les compétences ne seront donc pas validées !**

Travaille en groupe de 5/6 + rôles durée: 7 jours
                    ''')

md_source = dcc.Markdown('''
                ## Ressources :
                * [Tutoriel TAL pour les débutants : Classification de texte](https://www.actuia.com/contribution/victorbigand/tutoriel-tal-pour-les-debutants-classification-de-texte/)
                * [Text Classification with NLTK and Scikit-Learn](https://bbengfort.github.io/tutorials/2016/05/19/text-classification-nltk-sckit-learn.html)
                * [Use Sentiment Analysis With Python to Classify Movie Reviews](https://medium.com/neuronio/from-sentiment-analysis-to-emotion-recognition-a-nlp-story-bcc9d6ff61ae)
                * [From Sentiment Analysis to Emotion Recognition: A NLP story](https://realpython.com/sentiment-analysis-python/#how-classification-works)''')


#------------------------------------------------------DASHTABLE--------------------------------------------------------------------------#

table0_brut = dash_table.DataTable(
                                    columns=[{'id': c, 'name': c} for c in df0_brut.columns],
                                    data= df0_brut.to_dict('records'),
                                    #Style table as list view
                                    #style_as_list_view=True,
                                    fixed_rows={'headers': True},
                                    # fixed_columns={'headers': True, 'data' :1},
                                    export_format='csv',
                                    style_table={'opacity':'0.85',
                                                'maxHeight': '50ex',
                                                'overflow': 'scrol',
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
                                    # page_size = 15,
                                    style_data_conditional=[{
                                            'if': {'row_index': 'odd'},
                                            'backgroundColor': 'rgb(248, 248, 248)'}],
                                    style_header={
                                        'backgroundColor': 'rgb(50, 50, 50)',
                                        'fontWeight': 'bold',
                                        'color':'white'})

table0_pre = dash_table.DataTable(
                                    
                                    columns=[{'id': c, 'name': c} for c in df0_pre[['Text','Emotion']]],
                                    data= df0_pre.to_dict('records'),
                                    #Style table as list view
                                    #style_as_list_view=True,
                                    fixed_rows={'headers': True},
                                    # fixed_columns={'headers': True, 'data' :1},
                                    export_format='csv',
                                    style_table={'opacity':'0.85',
                                                'maxHeight': '50ex',
                                                'overflow': 'scrol',
                                                'width': '100%',    
                                                'minWidth': '100%',
                                                'margin-left':'auto',
                                                'margin-right':'auto'},
                                    #Cell dim + textpos
                                    style_cell_conditional=[{'height': 'auto',
                                        #all three widths are needed
                                        'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                                        'whiteSpace': 'normal','textAlign':'center'}],
                                    #Line strip
                                    style_cell={'color': 'black'},
                                    # page_size = 15,
                                    style_data_conditional=[{
                                            'if': {'row_index': 'odd'},
                                            'backgroundColor': 'rgb(248, 248, 248)'}],
                                    style_header={
                                        'backgroundColor': 'rgb(50, 50, 50)',
                                        'fontWeight': 'bold',
                                        'color':'white'})

table1_brut = dash_table.DataTable(
                                    columns=[{'id': c, 'name': c} for c in df1_brut.columns],
                                    data= df1_brut.to_dict('records'),
                                    #Style table as list view
                                    #style_as_list_view=True,
                                    fixed_rows={'headers': True},
                                    # fixed_columns={'headers': True, 'data' :1},
                                    export_format='csv',
                                    style_table={'opacity':'0.85',
                                                'maxHeight': '50ex',
                                                'overflow': 'scroll',
                                                'width': '100%',    
                                                'minWidth': '1font-size: 40px;00%',
                                                'margin-left':'auto',
                                                'margin-right':'auto'},
                                    #Cell dim + textpos
                                    style_cell_conditional=[{'height': 'auto',
                                        # all three widths are needed
                                        'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                                        'whiteSpace': 'normal','textAlign':'center'}],
                                    #Line strip
                                    style_cell={'color': 'black'},
                                    # page_size = 15,
                                    style_data_conditional=[{
                                            'if': {'row_index': 'odd'},
                                            'backgroundColor': 'rgb(248, 248, 248)'}],
                                    style_header={
                                        'backgroundColor': 'rgb(50, 50, 50)',
                                        'fontWeight': 'bold',
                                        'color':'white'})


table1_pre = dash_table.DataTable(
                                    columns=[{'id': c, 'name': c} for c in df1_pre[['tweet_id','sentiment','author','content']]],
                                    data= df1_pre.to_dict('records'),
                                    #Style table as list view
                                    #style_as_list_view=True,
                                    fixed_rows={'headers': True},
                                    # fixed_columns={'headers': True, 'data' :1},
                                    export_format='csv',
                                    style_table={'opacity':'0.85',
                                                'maxHeight': '50ex',
                                                'overflow': 'scroll',
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
                                    # page_size = 15,
                                    style_data_conditional=[{
                                            'if': {'row_index': 'odd'},
                                            'backgroundColor': 'rgb(248, 248, 248)'}],
                                    style_header={
                                        'backgroundColor': 'rgb(50, 50, 50)',
                                        'fontWeight': 'bold',
                                        'color':'white'})
table0_pipe = dash_table.DataTable(
                                    columns=[{'id': c, 'name': c} for c in df0_pipe[['Name',"Time/ms","F1 Score | Ecart",'Precision','Recall']]],
                                    data= df0_pipe.to_dict('records'),
                                    #Style table as list view
                                    #style_as_list_view=True,
                                    fixed_rows={'headers': True},
                                    # fixed_columns={'headers': True, 'data' :1},
                                    export_format='csv',
                                    style_table={'opacity':'0.85',
                                                'maxHeight': '50ex',
                                                'overflow': 'scroll',
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
                                    # page_size = 15,
                                    style_data_conditional=[{
                                            'if': {'row_index': 'odd'},
                                            'backgroundColor': 'rgb(248, 248, 248)'}],
                                    style_header={
                                        'backgroundColor': 'rgb(50, 50, 50)',
                                        'fontWeight': 'bold',
                                        'color':'white'})

table1_pipe = dash_table.DataTable(
                                    columns=[{'id': c, 'name': c} for c in df1_pipe[['Name',"Time/ms","F1 Score | Ecart",'Precision','Recall']]],
                                    data= df1_pipe.to_dict('records'),
                                    #Style table as list view
                                    #style_as_list_view=True,
                                    fixed_rows={'headers': True},
                                    # fixed_columns={'headers': True, 'data' :1},
                                    export_format='csv',
                                    style_table={'opacity':'0.85',
                                                'maxHeight': '50ex',
                                                'overflow': 'scroll',
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
                                    # page_size = 15,
                                    style_data_conditional=[{
                                            'if': {'row_index': 'odd'},
                                            'backgroundColor': 'rgb(248, 248, 248)'}],
                                    style_header={
                                        'backgroundColor': 'rgb(50, 50, 50)',
                                        'fontWeight': 'bold',
                                        'color':'white'})                                       
#------------------------------------------------------GRAPH------------------------------------------------------------------------------#

#------------------------------------------------------FIGURE1----------------------------------------------------------------------------#
x = df0_brut.Text
y = df0_brut.Emotion

freq_top = get_top_n_words(x,"up",100)

df_up = pd.DataFrame(freq_top, columns =['Word','Number of times'])
y_nbr = df_up['Number of times']
x_word = df_up['Word']

freq_p1 = go.Bar(
                x = x_word.head(30),
                y = y_nbr,
                name = "Le score universitaire pour le transfert de connaissances par pays",
                marker = dict(color = 'rgba(25,211,243 0.5)', line = dict(color ='rgb(222,226,230)',width =2.5)),
                text = df_up['Word'])

freq_lay_p1 = go.Layout(barmode = "group",
                  title = 'Fréquence d’apparition des mots ',
                  yaxis = dict(title = 'word frequency'),
                  xaxis = dict(title = 'word rank'),
                  font=dict(
                        family="sans serif",
                        size=14,
                        color="white"),
                    paper_bgcolor='rgba(0,0,0,0.70)',
                    plot_bgcolor='rgba(0,0,0,0.70)')
freq_word_bar = go.Figure(data = freq_p1 , layout = freq_lay_p1)

#------------------------------------------------------FIGURE2----------------------------------------------------------------------------#

emotion_hist = go.Figure(px.histogram(df0_brut, x="Emotion", color= "Emotion").update_xaxes(categoryorder ="total descending"))
emotion_hist.update_layout(
                 title = 'Histogramme des émotions Kaggle data',
                  yaxis = dict(title = "Nombre d'entrées"),
                  xaxis = dict(title = 'Emotion'),
                  font=dict(
                        family="Courier",
                        size=14,
                        color="white"),
                paper_bgcolor='rgba(0,0,0,0.70)',
                plot_bgcolor='rgba(0,0,0,0.70)')



#------------------------------------------------------FIGURE3----------------------------------------------------------------------------#
# emotion2_hist = go.Figure(px.histogram(df1_brut, x="sentiment", color= "sentiment", title="Histogramme Emotion").update_xaxes(categoryorder ="total descending"))
# emotion_hist.update_layout(
#                 title = 'Histogramme des émotions Yes data',
#                             yaxis = dict(title = "Nombre d'entrées"),
#                             xaxis = dict(title = 'Emotion'),
#                             font=dict(
#                                     family="Courier",
#                                     size=14,
#                                     color="white"),
#                             paper_bgcolor='rgba(0,0,0,0.70)',
#                             plot_bgcolor='rgba(0,0,0,0.70)')



#------------------------------------------------------NAVBAR----------------------------------------------------------------------------#
p1_buton = dbc.NavItem(dbc.NavLink("Page 1", href='/apps/page1', active=True, style={'margin-right':'5px'}, className="bootstrap_s_buton"))
p2_buton = dbc.NavItem(dbc.NavLink("Page 2", href='/apps/page2', active=True, className="bootstrap_s_buton"))

nav_bar = dbc.Navbar(
    [
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(html.Img(src="/assets/favicon.ico",height = "40px" ,style={'margin-left':'50px'})),
                    dbc.Col(dbc.NavbarBrand("HomePage", className="bootstrap_buton")),
                ],
                align="center",
                no_gutters=True,
            ),
            href="/",
        ),
        dbc.NavbarToggler(id="navbar-toggler"),
        dbc.Collapse(
            dbc.Nav(style={'margin-left':'auto'},
                    children=[
                p1_buton,
                p2_buton
                ]
                ,pills=True), 
            id="navbar-collapse", 
            navbar=True),
    ],
    color ='black',
    style = {'opacity':0.90},
    fixed = "top",
    dark = True

)
