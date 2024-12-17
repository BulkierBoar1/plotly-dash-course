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

# Scatter

fig_df = df.to_dict('records')

fig = px.scatter(data_frame = fig_df,
                x = [d['V'] for d in fig_df], 
                y = [d['S'] for d in fig_df],
                color = 'hex',
                hover_name = 'brand')

# App layout
app.layout = html.Div([
    grid,
    dcc.Graph(figure = fig)
])

# Add controls to build the interaction

# Run the app
if __name__ == '__main__':
    app.run(debug=True)