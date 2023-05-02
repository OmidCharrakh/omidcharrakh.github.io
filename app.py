import dash
from dash import dcc
from dash import html
import plotly.express as px
import plotly


import json

# create a sample scatter plot
df = px.data.iris()
scatter_data = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
scatter_data_json = json.dumps(scatter_data.data[0], cls=plotly.utils.PlotlyJSONEncoder)
scatter_data_layout_json = json.dumps(scatter_data.layout, cls=plotly.utils.PlotlyJSONEncoder)


app = dash.Dash(__name__)

# Define app layout
app.layout = html.Div([
    html.H1("My Landing Page"),
    html.P("Welcome to my landing page! Here is a scatter plot of some data:"),
    html.Script(
        f"var x = {json.dumps(df['sepal_width'].tolist())};"
        f"var y = {json.dumps(df['sepal_length'].tolist())};"
        f"var color = {json.dumps(df['species'].astype(str).tolist())};"
    ),
    html.Div(id='scatter_plot_data', style={'display': 'none'}, children=[scatter_data_json]),
    html.Div(id='scatter_plot_layout', style={'display': 'none'}, children=[scatter_data_layout_json]),
    html.Div(id='scatter_plot', style={'width': '100%', 'height': '500px'}),
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


# Define callback for scatter plot
@app.callback(
    Output('scatter_plot', 'children'),
    Input('scatter_plot_data', 'children'),
    Input('scatter_plot_layout', 'children')
)
def update_scatter_plot(data, layout):
    scatter_data = json.loads(data)
    scatter_layout = json.loads(layout)
    fig = go.Figure(data=scatter_data, layout=scatter_layout)
    fig.update_traces(mode='markers', marker={'size': 8, 'opacity': 0.6})
    fig.update_layout(
        title='Iris Dataset - Sepal Width vs. Sepal Length',
        xaxis_title='Sepal Width',
        yaxis_title='Sepal Length'
    )
    return dcc.Graph(figure=fig)


if __name__ == '__main__':
    #app.run_server(host='127.0.0.1', port=8050, debug=True)
    app.run_server()
