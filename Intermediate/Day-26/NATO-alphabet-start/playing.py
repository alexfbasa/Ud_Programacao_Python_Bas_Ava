# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
import pandas

alphabet = pandas.read_csv('nato_phonetic_alphabet.csv')

nato_dic = {value.letter: value.code for (column, value) in alphabet.iterrows()}
print(nato_dic)
# get_user_letter = input('Insert the word: ').upper()


# grey_squirrels = data[data['Primary Fur Color'] == 'Gray']
