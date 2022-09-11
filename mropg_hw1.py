from cmath import nan
import pandas as pd
from statistics import mean
import datetime 
pd.options.plotting.backend = "plotly"
# import plotly.express as px

df = pd.read_csv("rww-weather-data.csv")
for i in range(len(df['#DATE'])):
    datem = datetime.datetime.strptime(df['#DATE'][i], "%Y-%m-%d")
    df['#DATE'][i] = datem.year
final_df = df.groupby(['#DATE'], as_index=False).mean()
y = df.groupby('#DATE',as_index=False).sum()
final_df["Total_PRCP"] = y["PRCP"]
print(final_df)
fig = final_df.plot.line(x = '#DATE', y = ["TMAX", "TMIN","Total_PRCP"], title="Weather Changes Over The Year", labels = {
    'value': 'Temperatures',
    '#DATE': 'Date'
})
fig.update_traces(textposition="bottom right")
fig.show()
