import pandas

data = pandas.read_csv('weather_data.csv')

monday = data[data.day == 'Monday']
monday_temp = int(monday.temp)
print(monday_temp)
monday_temp_F = (monday_temp * 9 / 5) + 32
print(monday_temp_F)

# Create a DataFrame from the scratch
data_dict = {
    "students": ["Amin", "James", "Angela"],
    "scores": [76, 56, 65]
}
data_v2 = pandas.DataFrame(data_dict)
# Create a csv file
data_v2.to_csv('new_file.csv')
