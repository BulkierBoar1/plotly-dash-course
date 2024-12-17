# Import packages
import os
from dash import Dash, html, dash_table as dt, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

# Data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/refs/heads/master/Dash-Course/US-Exports/2011_us_ag_exports.csv')

# App
app = Dash()

# Layout

app.layout = [
    # Title
    html.Div(className = 'row', children = 'US Agricultural Exports in 2011', id = 'Title', 
            style = {'textAlign': 'left', 'color': 'black', 'fontSize': 20}), 

    # Dropdown
    dcc.Dropdown(options = df.state.unique(), value = ['Alabama', 'Arkansas'], 
                    multi = True, id = 'State Dropdown'),

    # Graph
    dcc.Graph(figure = {}, id = 'Graph 1')
]

# Callback
@callback(
    Output(component_id = 'Graph 1', component_property = 'figure'),
    Input(component_id = 'State Dropdown', component_property = 'value'),
)

def update(states):
    data = [d for d in df.to_dict('records') if d['state'] in states]
    # Solution: data = df[df.state.isin(states)]
    bar_chart = px.bar(data_frame = data, x = 'state', y = ['beef','pork','fruits fresh'])

    return bar_chart

# Run
if __name__ == '__main__':
    app.run(debug=True)