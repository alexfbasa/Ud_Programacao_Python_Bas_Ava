import pandas
from datetime import datetime as dt

birthday_data = pandas.read_csv("birhtday.csv")

currently_date = dt.now()
today_tuple = (currently_date.month, currently_date.day)

birthday_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in birthday_data.iterrows()}

if today_tuple in birthday_dict:
    current_person = birthday_dict[today_tuple]
    print(current_person)
