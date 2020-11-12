# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import numpy as np
import pandas as pd
import plotly.graph_objs as go
from sqlalchemy import create_engine
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn import svm



engine = create_engine("mysql+pymysql://root@localhost/dataAi")
df = pd.read_sql_table('cardata',engine)

X = df['Year'].values
y = df['Transmission_Bool'].values.ravel()
x = np.array(X).reshape(-1,1)

scaler = StandardScaler()
scaler.fit_transform(x)
regr = svm.SVR(kernel = "linear")
regr.fit(x,y)

resultat = regr.predict(x)


# plt.figure(figsize=(13,5))
# plt.plot(x, y, 'o', label='original data')
# plt.plot(x, resultat, 'r', label='fitted line')
# plt.legend()
# plt.show()

app = dash.Dash()

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

# app.layout = html.Div([
#     dcc.Graph(
#         id='graph',
#         figure={
#             'data': [
#                 go.Scatter(
#                 { 'x': df['Year'], 'y': df['Selling_Price'], 'type': 'scatter', 'marker':{'color':'darkred'},'name':'Price'}
#                 ,{ 'x': df['Year'], 'y': resultat, 'type': 'line', 'marker':{'color':'blue'},'name':'Year'}
#             )],
#             'layout': go.Layout(
#                 xaxis={'type': 'log', 'title': 'GDP Per Capita'},
#                 yaxis={'title': 'Life Expectancy'},
#                 margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
#                 legend={'x': 0, 'y': 1.20},
#                 hovermode= 'closest'
#             )
#         }
#     )
# ])

html.Div([  
dcc.Graph(
    id='plot2011',
    figure={
        'data': [
                go.Scatter(name='Values', x=df["Year"], y=df["Selling_Price"], mode='markers' ) #end of go.Scatter
        ], #end of data
        'layout': go.Layout(
                xaxis={'type': 'log', 'title': 'GDP Per Capita'},
                yaxis={'title': 'Life Expectancy'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1.20},
                hovermode= 'closest' 
                ) #end of layout
    }  # end of figure
)])

if __name__ == '__main__':
    app.run_server(debug=True)


# , 'marker':{'color':'blue'},'name':'Year'


# app.layout = html.Div([
#     dcc.Graph(
#         id='graph',
#         figure={
#             'data': [
#                 [
#                 { 'x': df['Year'], 'y': df['Selling_Price'], 'type': 'scatter', 'marker':{'color':'darkred'},'name':'SOBER'}
#                 ,{ 'x': df['Year'], 'y': resultat, 'type': 'line', 'marker':{'color':'blue'},'name':'HIGH'}
#             ]],
#             'layout': {
#             'title': 'COMPARATIF DU NOMBRE DE TIR À LA TÊTE EN FONCTION DE L\'ÉTAT MENTAL SUR 87 JOUEURS','xaxis':{'title':'NOMBRE DE TIRS'},'yaxis':{'title':'NOMBRE DE HEADSHOTS'}
#             }
#         }
#     )
# ])
