from dash import Dash, dcc, html, State, Input, Output
import pandas as pd
import plotly.express as px

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/Dash-Course/US-Exports/2011_us_ag_exports.csv')

app = Dash(__name__)
server = app.server

app.layout = html.Div([
   html.Div(id = 'Title', children = "Us Agricultural Exports in 2011"),
   dcc.Dropdown(id = 'State Dropdown', options = df.state.unique(), value = ['Alabama', 'Arkansas'], multi = True),
   html.Button(id = 'State Button', children = 'Submit'),
   dcc.Graph(id = 'Graph'),
])

@app.callback(
   Output('Graph', 'figure'),
   Input('State Button', 'n_clicks'),
   State('State Dropdown', 'value'),
   prevent_initial_call = True
)

def update_graph(clicks, states_selected):
    if clicks > 0:
        print(states_selected)
        df_states = df[df.state.isin(states_selected)]
        fig1 = px.bar(data_frame = df_states, x = 'state', y = ['beef','pork','fruits fresh'])
    else: fig1 = px.bar()
    return fig1


if __name__ == '__main__':
  app.run(debug=True)