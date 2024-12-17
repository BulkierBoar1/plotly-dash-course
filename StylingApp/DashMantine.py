from dash import Dash, dash_table as dt, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash_mantine_components as dmc

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

app = Dash()

# App layout
app.layout = dmc.Container([
    dmc.Title('Dash Mantine', color = 'Black', size = 'h3'),
    dmc.RadioGroup(
            [dmc.Radio(i, value = i) for i in ['pop', 'lifeExp', 'gdpPercap']],
            id = 'DMC Radio Item',
            value = 'lifeExp',
            size = 'sm'
        ),
    dmc.Grid([
        dmc.Col([
            dt.DataTable(data = df.to_dict('records'), page_size = 12, style_table = {'overflowX': 'auto'})
        ], span = 6),

        dmc.Col([
            dcc.Graph(figure = {}, id = 'Graph Placeholder')
        ], span = 6),
    ]),
], fluid = True)

@callback(
    Output(component_id = 'Graph Placeholder', component_property = 'figure'),
    Input(component_id = 'DMC Radio Item', component_property = 'value')
)
def update_graph(col_chosen):
    fig = px.histogram(df, x = 'continent', y = col_chosen, histfunc = 'avg')
    return fig

if __name__ == '__main__':
    app.run(debug=True)