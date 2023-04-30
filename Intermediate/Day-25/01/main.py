# with open("weather_data.csv") as weather_file:
#     weather_content = weather_file.readlines()
#
# print(weather_content[0])
import csv
import pandas
from prettytable import PrettyTable

with open("weather_data.csv") as weather_file:
    data = csv.reader(weather_file)
    temperatures = []
    for row in data:
        if row[1] != 'temp':
            temperatures.append(int(row[1]))

    print(temperatures)

data_weather = pandas.read_csv('weather_data.csv')
print(data_weather)

table = PrettyTable()
# Panda get the column name as a input, like in data_weather."day"
table.add_column("Day", data_weather.day)
table.add_column("Temperature", data_weather["temp"])
table.add_column("Condition", data_weather["condition"])
#
# for day in data_weather:
#     table.ad
print(table)
