# with open("weather_data.csv") as weather_file:
#     weather_content = weather_file.readlines()
#
# print(weather_content[0])
import csv
import pandas

with open("weather_data.csv") as weather_file:
    data = csv.reader(weather_file)
    temperatures = []
    for row in data:
        if row[1] != 'temp':
            temperatures.append(int(row[1]))

    print(temperatures)

data_weather = pandas.read_csv('weather_data.csv')
print(data_weather)
print(data_weather['temp'])
