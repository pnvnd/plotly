import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv("csv/covidtesting.csv")

data = [go.Histogram(
    x=df["Number of patients hospitalized with COVID-19"],
    xbins=dict(
        start = 0,
        end = 500,
        size = 10
    )
)]

layout = go.Layout(title="Histogram")
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename="html/histogram.html")
