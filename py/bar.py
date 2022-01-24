import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# source = "https://data.ontario.ca/dataset/f4112442-bdc8-45d2-be3c-12efae72fb27/resource/455fd63b-603d-4608-8216-7d8647f43350/download/conposcovidloc.csv"
df = pd.read_csv("csv/conposcovidloc.csv")

Age_Group = ['<20', '20s', '30s', '40s', '50s', '60s', '70s','80s', '90+', 'UNKNOWN']
# Age_Group = df["Age_Group"].unique().tolist()
# Age_Group.sort()

# Client_Gender = df["Client_Gender"].unique().tolist()

# counts = [288,215010,169138,144525,133131,79938,39486,26266,13507,175376]
# counts = []
# for age in Age_Group:
#     counts.append(df[(df["Age_Group"]==age)]["Age_Group"].count())
# trace = go.Bar(x=Age_Group, y=counts)
# data = [trace]

count_female = []
count_male = []
count_unspecified = []
count_diverse = []

for age in Age_Group:
    count_female.append(df[(df["Age_Group"]==age) & (df["Client_Gender"]=="FEMALE")]["Age_Group"].count())
    count_male.append(df[(df["Age_Group"]==age) & (df["Client_Gender"]=="MALE")]["Age_Group"].count())
    count_unspecified.append(df[(df["Age_Group"]==age) & (df["Client_Gender"]=="UNSPECIFIED")]["Age_Group"].count())
    count_diverse.append(df[(df["Age_Group"]==age) & (df["Client_Gender"]=="GENDER DIVERSE")]["Age_Group"].count())

trace1 = go.Bar(x=Age_Group, y=count_female, name="Female", marker={"color": "#FFD700"})
trace2 = go.Bar(x=Age_Group, y=count_male, name="Male", marker={"color": "#9EA0A1"})
trace3 = go.Bar(x=Age_Group, y=count_unspecified, name="Unspecified", marker={"color": "#CD7F32"})
trace4 = go.Bar(x=Age_Group, y=count_diverse, name="Gender Diverse", marker={"color": "#000000"})

data = [trace1, trace2, trace3, trace4]
layout = go.Layout(title="Ontario COVID-19 Case Breakdown by Age Group and Gender", barmode="stack") # Remove barmode to get nested 

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename="html/bar.html")