import plotly.offline as pyo
import plotly.graph_objs as go


y = [1,14,14,15,16,18,18,19,19,20,20,23,24,26,27,27,28,29,33,54]

snodgrass = [.209,.205,.196,.210,.202,.207,.224,.223,.220,.201]

twain = [.225,.262,.217,.240,.230,.229,.235,.217]



data1 = [go.Box(
    y=y,
    boxpoints="all",
    jitter=0.3,
    pointpos=0)
]

data2 = [go.Box(
    y=y,
    boxpoints="outliers",
    jitter=0.3,
    pointpos=0)
]

data3 = [
    go.Box(y=snodgrass, name="Snodgrass"),
    go.Box(y=twain, name="Twain"),
]

# import numpy as np
# import pandas as pd

# df = pd.read_csv("csv/data.csv")
# a = np.random.choice(df["rings"], 10, replace=False)
# b = np.random.choice(df["rings"], 20, replace=False)

# data4 = [
#     go.Box(y=a, Name="A"),
#     go.Box(y=b, name="B")
# ]

# layout = go.Layout(title="Two Random Samples")

# fig = go.Figure(data=data4, layout=layout)

pyo.plot(data3, filename = "html/box.html")
