import plotly.figure_factory as ff
import pandas as pd
import csv
import plotly

df = pd.read_csv("C:/Users/Somisetty Karthik/Dropbox/My PC (LAPTOP-PJB0FTAK)/Downloads/108.csv")
#fig = ff.create_distplot([df["Height(Inches)"].to_list()],["height"],show_hist=False)
fig = ff.create_distplot([df["Weight(Pounds)"].to_list()],["weight"],show_hist=False)
plotly.offline.plot(fig)