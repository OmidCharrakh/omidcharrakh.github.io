import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

df = pd.read_csv('./files/seaborn_tips.csv')

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1('My Plotly Dash App'),
    dcc.Graph(
        figure=px.scatter(df, x='total_bill', y='tip')
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
