import plotly.offline as pyo
import plotly.figure_factory as ff
import pandas as pd

#x = np.random.randn(1000)
df = pd.read_csv("csv/covidtesting.csv")

x1 = df["Number of patients hospitalized with COVID-19"].fillna(0)
x2 = df["Number of patients in ICU due to COVID-19"].fillna(0)
x3 = df["Number of patients in ICU on a ventilator due to COVID-19"].fillna(0)

hist_data = [x1, x2, x3]
group_labels = ["Hospitalized with COVID-19", "In ICU due to COVID-19", "On a ventilator due to COVID-19"]

fig = ff.create_distplot(
    hist_data,
    group_labels,
    bin_size=[25,25,25]
)

pyo.plot(fig, filename="html/distplot.html")