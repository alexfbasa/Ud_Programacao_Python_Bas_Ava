import pandas as pd
from prettytable import PrettyTable

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_fur_count = len(data[data['Primary Fur Color'] == 'Gray'])
black_fur_count = len(data[data['Primary Fur Color'] == 'Black'])
cinnamon_fur_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])

squirrels_dict = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [gray_fur_count, black_fur_count, cinnamon_fur_count]
}

df = pd.DataFrame(squirrels_dict)

df.to_csv("squirrels_table.csv")

table = PrettyTable(field_names=squirrels_dict.keys())

for row_data in zip(*squirrels_dict.values()):
    table.add_row(row_data)
    
print(table)
