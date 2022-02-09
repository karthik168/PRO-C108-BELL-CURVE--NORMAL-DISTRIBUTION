  
import pandas as pd 
import plotly.figure_factory as ff 
df = pd.read_csv("brand.csv")
fig = ff.create_distplot([df["Avg Rating"].tolist()], ["Ratings"])
fig.show()

# Code written by saanvi 