import pandas
from prettytable import PrettyTable


new_data_pada = pandas.read_csv("weather_data.csv")
table = PrettyTable()
table.add_column("Day", new_data_pada.day)
table.add_column("Temperature", new_data_pada.temp)
table.add_column("Condition", new_data_pada.condition)
print(new_data_pada['temp'].mean())
print(new_data_pada['temp'].max())

print(table)