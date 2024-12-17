from dash import Dash, html

# Initialize the app
app = Dash()

# App layout
app.layout = [html.Div(children = 'Hello World')]

# App layout
if __name__ == '__main__':
    app.run(debug = True)