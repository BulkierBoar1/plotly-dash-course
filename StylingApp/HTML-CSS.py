# Import packages
from dash import Dash, html, dash_table as dt, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# Initialize the app (Incorporate CSS)
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(external_stylesheets = external_stylesheets)

# App layout
app.layout = [
    # Title
    html.Div(className = 'row', children = 'My First App with Data, Graph, and Controls', 
            style = {'textAlign': 'center', 'color': 'blue', 'fontSize': 30}), 

    # Radio Buttons
    html.Div(className = 'row', children = [
        dcc.RadioItems(options = ['pop', 'lifeExp', 'gdpPercap'],
                       value = 'lifeExp',
                       inline = True,
                       id = 'Radio Buttons')
    ]),

    # Data Table and Graph
    html.Div(className = 'row', children = [
        html.Div(className = 'six columns', children = [
            dt.DataTable(data = df.to_dict('records'), 
                        page_size = 11,
                        style_table = {'overflowX': 'auto'})
        ]),

        html.Div(className = 'six columns', children = [
            dcc.Graph(figure = {}, id = 'Histo Chart')
        ])
    ])
]

# Add controls to build the interaction
@callback(
    Output(component_id = 'Histo Chart', component_property = 'figure'),
    Input(component_id = 'Radio Buttons', component_property = 'value')
)
def update_graph(col_chosen):
    fig = px.histogram(df, x = 'continent', y = col_chosen, histfunc = 'avg')
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)