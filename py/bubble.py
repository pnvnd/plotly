import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv("csv/covidtesting.csv").fillna(0)

data = [go.Scatter(
        x=df["Confirmed Positive"],
        y=df["Number of patients in ICU on a ventilator due to COVID-19"],
        text="okay",
        mode="markers",
        marker=dict(
            size=df["Number of patients hospitalized with COVID-19"]/50,
            color=df["Number of patients in ICU due to COVID-19"],
            showscale=True
        )
    )
]

layout = go.Layout(
    title="Bubble Chart",
    xaxis=dict(title="Confirmed Positive Case"),
    yaxis=dict(title="Patients in ICU on Ventilator"),
    hovermode="closest"
)

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename="html/bubble.html")