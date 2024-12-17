# Import packages
from dash import Dash, html, dash_table as dt, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/Dash-Course/makeup-shades/shades.csv')

# Initialize the app
app = Dash()

group_strings = ["Fenty Beauty's PRO FILT'R Foundation Only", 
                "Make Up For Ever's Ultra HD Foundation Only", 
                "US Best Sellers", 
                "BIPOC-recommended Brands with BIPOC Founders", 
                "BIPOC-recommended Brands with White Founders",
                "Nigerian Best Sellers", 
                "Japanese Best Sellers",
                "Indian Best Sellers"]

# App layout

app.layout = [
    # Title
    html.Div(className = 'row', children = 'Assignment 1', 
            style = {'textAlign': 'center', 'color': 'black', 'fontSize': 30}), 

    # Dropdown
    html.Div([
        dcc.Dropdown(options = [{'label': x, 'value': x} for x in set(df.get('brand'))], 
                    value = 'Revlon', id = 'Dropdown')
        ]),

    # Radio Buttons
    html.Div(className = 'row', children = [
        dcc.RadioItems(options = [{'label': group_strings[x], 'value': x} for x in list(set(df.get('group')))],
                       inline = True, id = 'Radio Buttons')
    ]),
]

# Add controls to build the interaction

# Run the app
if __name__ == '__main__':
    app.run(debug=True)