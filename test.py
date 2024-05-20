import pandas as pd

# Read the CSV file
data = pd.read_csv("2015.csv")

# View the first 5 rows

'''data = data.sort_values("Region")

current_legion = ""
for index, row in data.iterrows():
    if current_legion != row["Region"]:
        current_legion = row["Region"]
        print(current_legion)
    print("{ key: \""+ row["Country"] + "\", value: "+ str(row["Happiness Score"]) + "},")
'''


for index, row in data.iterrows():
    print("{ key: \""+ row["Country"] + "\", value: "+ str(row["Happiness Score"]) + "},")
    print("{ key: \"Economy (GDP per Capita)\", value: "+ str(row["Economy (GDP per Capita)"]) + "},")
    print("{ key: \"Health (Life Expectancy)\", value: "+ str(row["Health (Life Expectancy)"]) + "},")
    print("{ key: \"Trust (Government Corruption)\", value: "+ str(row["Trust (Government Corruption)"]) + "},")
    



