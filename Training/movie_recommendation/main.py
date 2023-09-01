import pandas as pd
from prettytable import PrettyTable

data = pd.read_csv("MoviesTopRated.csv")

columns_to_extract = ['title', 'popularity', 'vote_average']

temp_data = data[columns_to_extract]

table = PrettyTable(field_names=columns_to_extract)

for _, row in temp_data.iterrows():
    table.add_row(row)

table.sortby = 'vote_average'
table.reversesort = True

movie_max_vote = data[data.vote_count == data.vote_count.max()]
print(movie_max_vote.title)
# print(table)
