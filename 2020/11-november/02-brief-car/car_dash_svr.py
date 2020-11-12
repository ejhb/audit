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

######## SVR calculation

engine = create_engine("mysql+pymysql://root@localhost/dataAi")
df = pd.read_sql_table('cardata',engine)

X = df['Year'].values
y = df['Selling_Price']
x = np.array(X).reshape(-1,1)

scaler = StandardScaler()
scaler.fit_transform(x)
regr = svm.SVR(kernel = "linear")
regr.fit(x,y)

resultat = regr.predict(x)


############# Dash
app = dash.Dash()

fig=go.Figure()
fig.add_trace(go.Scatter(name='Values', x=df["Year"], y=df["Selling_Price"], mode='markers'))
fig.add_trace(go.Scatter(name='Regression', x=df["Year"], y=resultat, mode='lines'))

fig.update_layout(title='Regression linéaire',
                  yaxis_zeroline=False, xaxis_zeroline=False)
fig.update_xaxes(title_text="Year")
fig.update_yaxes(title_text="Selling Price")

app.layout = html.Div([
    dcc.Graph(
        id='example-graph',
        figure=fig
        )
])
if __name__ == '__main__':
    app.run_server(debug=True)  