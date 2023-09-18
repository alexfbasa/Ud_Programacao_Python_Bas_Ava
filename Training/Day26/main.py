import pandas

user_input = input("Enter a word: ").title()
user_input_list = [letter for letter in user_input]


data = pandas.read_csv("nato_phonetic_alphabet.csv")


