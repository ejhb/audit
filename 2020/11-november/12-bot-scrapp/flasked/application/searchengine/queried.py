import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from .layout import html_layout
import pymysql
import plotly.graph_objects as go
    
db = pymysql.connect("localhost", "root", "", "gamedata")

def create_qman(server):
    qman_app = dash.Dash(server=server,
                         routes_pathname_prefix='/queried/',
                         external_stylesheets=['/static/dist/css/styles.css',
                                               'https://fonts.googleapis.com/css?family=Lato']
                         )
    sql_query = pd.read_sql_query("SELECT * FROM pkmn", db)
    df = pd.DataFrame(sql_query)


    qman_app.index_string = html_layout
    
    qman_app.layout = html.Div(

    return dash_app.server
