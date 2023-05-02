import dash
from dash import dcc
from dash import html
import plotly.express as px


# create a sample scatter plot
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length")

app = dash.Dash(__name__)


# Define scatter plot div
scatter_plot_div = dcc.Graph(
    id="scatter_plot",
    figure=fig,
    style={"height": "100%", "width": "100%"}
)


# Define app layout
app.layout = html.Div([
    html.H1("My Landing Page"),
    html.P("Welcome to my landing page! Here's a scatter plot of some data:"),
    scatter_plot_div,
    html.Div([
        html.H2("My Other Projects"),
        html.Ul([
            html.Li([
                html.A("Quantum CGNN", href="https://github.com/OmidCharrakh/Quantum_CGNN")
            ]),
            html.Li([
                html.A("Quantum RCC", href="https://github.com/OmidCharrakh/Quantum_RCC")
            ]),
            html.Li([
                html.A("Wildlife ML", href="https://github.com/slds-lmu/wildlife-ml")
            ])
        ])
    ])
])


if __name__ == '__main__':
    app.run_server(host='127.0.0.1', port=8050, debug=True)
    #app.run_server()
