import matplotlib.pyplot as plt
import pandas as pd
import os

path = './data'
output_path =os.path.join(path,'table.csv')


url = "https://en.wikipedia.org/wiki/Road_safety_in_Europe"

df = pd.read_html(url)
required_cols = [
"Country","Year","Area (thousands of km2)[21]",
"Population in 2018[22]","GDP per capita in 2018[23]",
"Population density (inhabitants per km2) in 2017[24]",
"Vehicle ownership (per thousand inhabitants) in 2016[25]",
"Total Road Deaths in 2018[27]",
"Road deaths per Million Inhabitants in 2018[27]"]


table=df[1].sort_values("Road deaths per Million Inhabitants in 2018[27]")

table["Year"]="2018"
table.loc[:,required_cols].to_csv(output_path,index=False)

df2 = pd.read_csv("./data/table.csv")
df2["Country"].replace("United Kingdom","UK",inplace=True)
df2["Country"].replace("Czech Republic","Czech",inplace=True)
df2["Country"].replace("Netherlands","Holland",inplace=True)
df2.plot(kind="bar",x="Country",y="Road deaths per Million Inhabitants in 2018[27]")
plt.show()



