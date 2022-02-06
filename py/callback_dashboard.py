from dash import dash, dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

url = 'csv/covidtesting.csv'
df = pd.read_csv(url)

app = dash.Dash()

# list = df.columns[1:]

# filter_options = []
# for option in list:
#     filter_options.append({'label': str(option), 'value': option})

app.layout = html.Div([
    dcc.Graph(id='graphs'),
    dcc.Dropdown(
        id='option-picker',
        options=[{"label": x, "value": x} for x in df.columns[1:]],
        value=df.columns[1]
    )
])


@app.callback(
    Output('graphs', 'figure'),
    [Input('option-picker', 'value')])
def update_figure(selected_option):   
    # fig = px.line(df, x='Reported Date', y=selected_option)
    # return fig

    return {
        'data': [go.Scatter(x=df['Reported Date'], y=df[selected_option], mode='lines')],
        'layout': go.Layout(
            title='COVID Data',
            xaxis={'title': 'Date'},
            yaxis={'title': 'Number of Cases'}
        )
    }

if __name__ == '__main__':
    app.run_server()