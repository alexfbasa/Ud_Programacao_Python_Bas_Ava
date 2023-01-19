import pandas

data_weather = pandas.read_csv('weather_data.csv')
print(type(data_weather))  # Panda DataFrame -whole file is DataFrame
print(type(data_weather['temp']))  # Panda Series -temp is a Series, -condition, etc.

data_dict = data_weather.to_dict()
print(data_dict)
data_list = data_weather['temp'].to_list()
print(data_list)