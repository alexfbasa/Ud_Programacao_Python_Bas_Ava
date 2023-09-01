import csv
from prettytable import PrettyTable


table = PrettyTable()


with open("weather_data.csv") as data_weather:
    weather_csv = csv.reader(data_weather)
    temperatures = []
    for row in weather_csv:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)
print(table)
