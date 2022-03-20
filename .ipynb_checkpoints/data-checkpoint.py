import matplotlib.pyplot as plt
import pandas as pd
url = "https://en.wikipedia.org/wiki/Road_safety_in_Europe"
tables = pd.read_html(url,attrs={"class":"wikitable sortable jquery-tablesorter"})
type(tables)
print(len(tables))
print(tables)


print("Hello")

