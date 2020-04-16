# En reprenant le fichier de données du classement des universités, timesData.csv
# Créer un dashboard Dash affichant un scatter plots avec le nombred’étudiants total en fonction du Ratio étudiant féminin / étudiant masculin, pour les 20 premières université du classement.

# Y en fonction de X

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go


app = dash.Dash()

timesData = pd.read_csv("~/data/timesData.csv")
df = timesData.iloc[:20,:]

app.layout = html.Div([
    dcc.Graph(
        id='students_vs_male-female-ratio',
        figure={
            'data': [
                go.Scatter(
                    x=df['female_male_ratio'][:20],
                    y=df['num_students'][:20],
                    text=df['university_name'][:20],
                    mode='markers',
                    opacity=0.8,
                    marker={
                        'size': 20,
                        'color':'darkred',
                        'line': {'width': 1, 'color': 'white'}
                    }
                )
            ],
            'layout': go.Layout(
                xaxis={'title': 'Female to male ratio'},
                yaxis={'title': 'Total number of students'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                hovermode='closest',
                width=800,
                height=400
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)