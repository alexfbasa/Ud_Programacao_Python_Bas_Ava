import pandas
from prettytable import PrettyTable
# Load data from CSV file
data_source = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# Filter squirrel fur by primary color
gray_squirrels = data_source[data_source['Primary Fur Color'] == 'Gray']
gray_squirrels_cinnamon = data_source[data_source['Primary Fur Color'] == 'Cinnamon']
gray_squirrels_black = data_source[data_source['Primary Fur Color'] == 'Black']

# Count the number of squirrels in each category
gray_count = len(data_source[data_source['Primary Fur Color'] == 'Gray'])
cinnamon_count = len(data_source[data_source['Primary Fur Color'] == 'Cinnamon'])
black_count = len(data_source[data_source['Primary Fur Color'] == 'Black'])

# Create a table to display the data
table = PrettyTable()

table.field_names = ['Primary Fur Color', 'Count']
table.add_row(['Gray', gray_count])
table.add_row(['Cinnamon', cinnamon_count])
table.add_row(['Black', black_count])
print(table)