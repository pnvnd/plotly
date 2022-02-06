from dash import dash, dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

# url = 'https://data.ontario.ca/dataset/f4f86e54-872d-43f8-8a86-3892fd3cb5e6/resource/ed270bb8-340b-41f9-a7c6-e8ef587e6d11/download/covidtesting.csv'
url = 'csv/covidtesting.csv'
df = pd.read_csv(url)

app = dash.Dash()

app.layout = html.Div([
    dcc.Graph(id='graphs'),
    dcc.Dropdown(id='option-picker', options=[{"label": x, "value": x} for x in df.columns[1:]], value=df.columns[1])
])

@app.callback(Output('graphs', 'figure'), [Input('option-picker', 'value')])
def update_figure(selected_option):   
    return {
        'data': [go.Scatter(x=df['Reported Date'], y=df[selected_option], mode='lines')],
        'layout': go.Layout(title='COVID Data', xaxis={'title': 'Date'}, yaxis={'title': 'Number of Cases'})
    }

if __name__ == '__main__':
    app.run_server()