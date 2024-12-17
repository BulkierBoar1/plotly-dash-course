# Import packages
from dash import Dash, html, dash_table as dt, dcc, callback, Output, Input
import dash_ag_grid as dag
import pandas as pd
import plotly.express as px

# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/Dash-Course/makeup-shades/shades.csv')

# Initialize the app
app = Dash()

# Grid

grid = dag.AgGrid(
    id = 'Grid',
    rowData = df.to_dict('records'),
    columnDefs = [{"field": i} for i in df.columns],
    columnSize = 'sizeToFit',
    defaultColDef={"filter": True},
    dashGridOptions={"pagination": True, "animateRows": False},
)

# App layout
app.layout = html.Div([grid])

# Add controls to build the interaction

# Run the app
if __name__ == '__main__':
    app.run(debug=True)