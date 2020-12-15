from dash.dependencies import Input, Output
import time
from app import app
from layouts import layoutHome,layout1, layout2 ,layout3
# from my_import.my_var import table0_brut , table0_pre 

@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/' :
         return layoutHome
    elif pathname == '/apps/page1':
        return layout1
    elif pathname == '/apps/page2':
         return layout2
    elif pathname == '/apps/page3':
         return layout3
    else:
        return '404'

@app.callback(
    Output("loading-output", "children"), [Input("loading-button", "n_clicks")])
def load_output(n):
    if n:
        time.sleep(1)
        return 
    return 

# @app.callback(Output('tabs-example-content', 'children'),
#               Input('tabs-example', 'value'))
# def render_content(tab):
#     if tab == 'tab-1':
#         return table0_brut
#     elif tab == 'tab-2':
#         return table0_pre
     
# @app.callback(
#     Output('app-home-display-value', 'children'),
#     Input('app-home-dropdown', 'value'))
# def display_value(value):
#     return 'You have selected "{}"'.format(value)

# @app.callback(
#     Output('app-1-display-value', 'children'),
#     Input('app-1-dropdown', 'value'))
# def display_value(value):
#     return 'You have selected "{}"'.format(value)

# @app.callback(
#     Output('app-2-display-value', 'children'),
#     Input('app-2-dropdown', 'value'))
# def display_value(value):
#     return 'You have selected "{}"'.format(value)