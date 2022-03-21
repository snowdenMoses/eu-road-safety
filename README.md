Steps taken to make the script

1.  import dependencies (the dependencies include pandas, matplotlib, os), pandas, matplotlib can only be imported after "pip installing them" using the pip install dependency_name command

    pip install pandas
    pip install matplotlib

    import pandas as pd
    import matplotlib.pyplot as plt
    import os

    *Pandas is for getting the data and converting it to csv
    *matplotlib is for ploting of graph (visualization)
    *os is for easier directory navigation


2.  Use pandas.read_html() command to read the url that contains the table.
    url = "https://en.wikipedia.org/wiki/Road_safety_in_Europe"
    df = pd.read_html(url)

    *If the url has more than one table, the required table can be selected by indexing.
        table = df[1]
    the required table is the second table on the website

    *the table.sort_value() method is used to sort by any desired column
        table.sort_values("Road deaths per Million Inhabitants in 2018[27]")

    *Create a new column and assigned 2018 as all its values
        table["Year"]="2018"

    *Converted the fields on the table to a csv file, using only desired columns, and save it in the data folder

        folder = './data'
        output_path =os.path.join(folder,'table.csv')
        table.loc[:,required_cols].to_csv(output_path,index=False)


3.  Visualization

    This is where matplotlib comes in. Here it was used for creating a bar chart. in other to do this, the following steps are taken

    *read the csv file using pandas read_csv() method 
        df2 = pd.read_csv("./data/table.csv")

    *plot the chart using matplotlib plot() method. the method carries 3 arguments (kind,x-axis value, y-axis value)
        df2.plot(kind="bar",x="Country",y="Road deaths per Million Inhabitants in 2018[27]")

    *use the show() method to show the chart
        plt.show()

    NB: png version of the chart is saved inside the data folder.



