import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('csv/covidtesting.csv')
# print(df.head())

#df2 = df[df['Reported Date'] > '2021-01-01']

#list = ["Reported Date", "Confirmed Positive", "Deaths"]
list = df.columns[1:]

#df2 = df2[list]
#print(df2["Deaths"])

# data = [
#     go.Scatter(x=df2["Reported Date"],y=df2["Confirmed Positive"],mode="lines",name="Confirmed Positive"),
#     go.Scatter(x=df2["Reported Date"],y=df2["Deaths"],mode="lines",name="Deaths")
# ]

data = []

for item in list:
    trace = go.Scatter(x=df["Reported Date"], y=df[item], mode="lines", name=item)
    data.append(trace)


layout = go.Layout(title="Ontario COVID Data")

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename="html/line2.html")