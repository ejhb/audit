#  1. Quels sont les pays dans lesquels le score universitaire pour le revenu de l'industrie se démarque ? 
# Utiliser un ou plusieurs graphique pour justifier votre réponse.

import plotly.graph_objs as go
import pandas as pd
import plotly.express as px

timesData = pd.read_csv("~/data/timesData.csv")

dfClass = timesData.sort_values('income', ascending=False)[:20]

# Création de la première trace 
trace1 = go.Bar(
                x = dfClass.country,
                y = dfClass.income,
                name = "revenu",
                marker = dict(color = 'rgba(250, 184, 1, 0.5)',
                             line = dict(color ='rgb(0,0,0)',width =1.5)),
                text = dfClass.university_name)

layout = dict(title = "Classement des universités par score d'enseignement",
            xaxis_title="Enseignement",
            yaxis_title="Classement mondial",
            showlegend=True,
            legend=dict(x=0.029,y=1.038,font=dict(size=12),traceorder="normal")   
             )
data = [trace1]
layout = go.Layout(barmode = "stack",
                    title = "Top pays selon le revenu cumulé des universités",
                    xaxis_title="Pays",
                    yaxis_title="Classement mondial cumulé")
fig = px.scatter(timesData, x='country', y='income', color='year', title='Income per country', color_continuous_scale=px.colors.sequential.Viridis )
fig.show()
print('Pas suffisemment de données des pays avec les plus faibles revenu')
print("Grande variation au sein d'un même pays des scores de ses différentes universités en une année donnée") 