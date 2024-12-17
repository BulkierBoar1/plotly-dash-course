from dash import Dash, dcc, html, Input, Output, no_update
import pandas as pd
import plotly.express as px

app = Dash(__name__)
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/Dash-Course/US-Exports/2011_us_ag_exports.csv')

# The bar chart should use the df dataset, have “state” on the x-axis and “pork” on the y-axis.

fig = px.bar(data_frame = df, x = 'state', y = 'pork', range_y = [0, 200], text_auto = True)
fig.update_xaxes(title = None)

app.layout = html.Div([
   html.Div(id = "Title", children = "Us Agricultural Exports in 2011"),
   dcc.Graph(id = "Graph", figure = fig),
])

if __name__ == '__main__':
  app.run(debug=True)