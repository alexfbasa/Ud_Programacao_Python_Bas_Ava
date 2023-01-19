import pandas

data = pandas.read_csv('weather_data.csv')

# Single way to calculate average
print(data['temp'].mean())
print(data['temp'].max())

# Get Data in Columns
print(data['condition'])
# or fil out the column name as a attribute after dot.
print(data.condition)

# Get Data in ROW
print(data[data.day == 'Monday'])

print(data[data.temp == data.temp.max()])