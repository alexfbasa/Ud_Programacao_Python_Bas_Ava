import pandas as pd
from prettytable import PrettyTable

# Read data from CSV file
weather_data = pd.read_csv("weather_data.csv")

# Create a table to display the data
weather_table = PrettyTable()

# Add columns to the table
weather_table.field_names = ["Day", "Temperature (C)", "Condition"]

# Add rows to the table
for index, row in weather_data.iterrows():
    # Format the temperature column with units
    temperature = f"{row['temp']} C"

    # Add a row to the table with a different color for each row
    if index % 2 == 0:
        weather_table.add_row([row['day'], temperature, row['condition']])
    else:
        weather_table.add_row([row['day'], temperature, row['condition']])

# Set the style of the table
weather_table.border = True
weather_table.header_style = "upper"
weather_table.align = "l"

# Display the table
print(weather_table)
