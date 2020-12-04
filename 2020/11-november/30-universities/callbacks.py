from dash.dependencies import Input, Output
import time
from app import app




# @app.callback(
#     Output('app-home-display-value', 'children'),
#     Input('app-home-dropdown', 'value'))
# def display_value(value):
#     return 'You have selected "{}"'.format(value)

@app.callback(
    Output("loading-output", "children"), [Input("loading-button", "n_clicks")]
)
def load_output(n):
    if n:
        time.sleep(1)
        return 
    return 


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