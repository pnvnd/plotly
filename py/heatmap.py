import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
from plotly import tools

df1 = pd.read_csv("csv/conposcovidloc.csv")
df2 = pd.read_csv("csv/conposcovidloc.csv")
df3 = pd.read_csv("csv/conposcovidloc.csv")

trace1 = [go.Heatmap(
    x=df1["Age_Group"],
    y=df1["Case_Reported_Date"],
    z=df1["Client_Gender"].values.tolist(),
    colorscale="Jet"
)]

trace2 = [go.Heatmap(
    x=df2["Age_Group"],
    y=df2["Case_Reported_Date"],
    z=df2["Client_Gender"].values.tolist(),
    colorscale="Jet"
)]


trace3 = [go.Heatmap(
    x=df2["Age_Group"],
    y=df2["Case_Reported_Date"],
    z=df2["Client_Gender"].values.tolist(),
    colorscale="Jet"
)]

fig = tools.make_subplots(rows=1, cols=3,subplot_titles=["AK","SB","AZ"], shared_yaxes=True)

fig.append_trace(trace1,1,1)
fig.append_trace(trace2,1,2)
fig.append_trace(trace3,1,3)

layout = go.Layout(title="COVID-19")

# fig = go.Figure(data=data, layout=layout)

fig["layout"].update(title="Temps for 3 Cities")
pyo.plot(fig, filename="html/heatmap.html")